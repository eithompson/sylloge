"""
Scrapes posts from slate star codex. First line is title, second is url, third begins the post.

Provide command-line arg if you want to get a random sample of posts.
The argument is the desired number of samples.
Otherwise, we scrape all posts in order.

We use a wayback version of the archive page so that this is reproducible.

Known problem: sometimes get_post_soup() will not get the entire post.
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
    soup = BeautifulSoup(con.read(), "html.parser")
    return soup.find("div", attrs={"class": "pjgm-postcontent"})

def get_real_link(url):
    """Extract actual ssc link from the link to a wayback archived version"""
    return url[url.find("https", 1):]

def straighten_quotes(string):
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
links_len = len(links)
n_pad = ceil(log10(links_len))

for idx, link in enumerate(links):
    print(idx)
    link_url = get_real_link(link.get("href"))
    post_title = straighten_quotes(link.string)
    post_filename = post_title.lower().replace(" ", "_")
    post_filename = str(idx).zfill(n_pad) + "_" + sub("[^A-Za-z0-9_]+", "", post_filename) + ".txt"
    post_soup = get_post_soup(link_url)
    post_contents = straighten_quotes(post_soup.get_text())
    with open(output_dir + post_filename, "w") as f:
        # why do we need newline in between first two but not last two?
        f.writelines([post_title, "\n", link_url, post_contents])
    sleep(0.25)
