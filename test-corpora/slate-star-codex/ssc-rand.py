"""
Scrapes posts from slate star codex.
First line is title, second is url, third are "category" tags,
fourth are regular tags, fifth begins the post.

Provide command-line arg if you want to get a random sample of posts.
The argument is the desired number of samples.
Otherwise, we scrape all posts in order.

We use a wayback version of the archive page so that this is reproducible.

Known problem: sometimes extract_text() will not get the entire post.
You can see this here: https://slatestarcodex.com/2020/04/10/coronalinks-4-10-second-derivative/
It stops picking it up starting with the blockquote
"""
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from random import shuffle, seed
from os import mkdir
from datetime import datetime
from time import sleep
from re import sub
from sys import argv
from math import log10, ceil

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
output_dir = "posts/" + now + "/"
mkdir(output_dir)
seed(321)
archive_link = "https://web.archive.org/web/20200417005254/https://slatestarcodex.com/archives/"
if len(argv) > 1:
    # user supplied argument
    n_posts = int(argv[1])
else:
    # otherwise, we will get all posts
    n_posts = None

def get_post_soup(url):
    """Works for archives page and actual posts."""
    req = Request(url, headers={"User-Agent" : "Magic Browser"})
    con = urlopen(req)
    return BeautifulSoup(con.read(), "html.parser")

def extract_text(soup, straighten_quotes = True):
    """Works for archives page and actual posts."""
    raw_soup_contents = soup.find("div", attrs={"class": "pjgm-postcontent"})
    text = raw_soup_contents.get_text()
    if straighten_quotes:
        text = fix_quotes(text)
    return text

def extract_tags(soup):
    """
    Get post tags delimited by semicolons.
    Strangely, soup.find_all(rel='tag') also returns rel='category_tags'
    We want this stuff, but I don't understand how this works so we need
    to be ready to throw an error.
    """
    list_dict = {"category_tags": [], "tags": []}
    tag_soups = soup.find_all(rel="tag") # this also gets rel = "category tag"
    for tag_soup in tag_soups:
        if tag_soup["rel"] == ["category", "tag"]:
            list_dict["category_tags"].append(tag_soup.get_text())
        elif tag_soup["rel"] == ["tag"]:
            list_dict["tags"].append(tag_soup.get_text())
        else:
            raise ValueError("Unknown rel: " + ';'.join(tag_soup["rel"]))
    out_dict = {"category_tags": ";".join(list_dict["category_tags"]),
            "tags": ";".join(list_dict["tags"])}
    return out_dict

def extract_real_link(url):
    """Extract actual ssc link from the link to a wayback archived version"""
    return url[url.find("https", 1):]

def fix_quotes(string):
    return string.replace('“','"').replace('”','"').replace("‘", "'").replace("’", "'")

archives_soup = get_post_soup(archive_link)
links = archives_soup.find_all("a", attrs={"rel": "bookmark"})
links = [link for link in links if link.string[0:11] != "Open Thread" and link.string[0:2] != "OT"]

if n_posts is None:
    # no command-line arg so we want to get them in order.
    # need to flip to go oldest first
    links.reverse()
else:
    # user supplied command-line arg so we want to randomly sample
    shuffle(links)
    links = links[0:n_posts]

# need correct number of zeroes to pad number in filename
n_pad = len(str(len(links)))

for idx, link in enumerate(links):
    print(idx)
    link_url = extract_real_link(link.get("href"))
    title = fix_quotes(link.string)
    filename = title.lower().replace(" ", "_")
    filename = str(idx).zfill(n_pad) + "_" + sub("[^A-Za-z0-9_]+", "", filename) + ".txt"
    post_soup = get_post_soup(link_url)
    contents_text = extract_text(post_soup)
    post_tags = extract_tags(post_soup)
    with open(output_dir + filename, "w") as f:
        f.writelines([title, "\n",
            link_url, "\n",
            post_tags["category_tags"], "\n",
            post_tags["tags"], # contents start with newline - no need here
            contents_text])
    sleep(0.25)
