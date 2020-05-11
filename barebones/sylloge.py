from ssc import ssc_parse
from sys import argv
from os import listdir, mkdir, path
from datetime import datetime
from re import finditer

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
if len(argv) != 4: # argv[0] is filename
    raise Exception("Supply three arguments: search term, corpus, and directory of corpus")
search_term = argv[1]
corpus = argv[2]
corpus_dir = argv[3]

if not path.exists("output/"):
    mkdir("output/")
if not path.exists("output/" + corpus):
    mkdir("output/" + corpus)
output_filepath = "output/" + corpus + "/" + search_term + "_" +  now + ".md"

def parse_file(filepath, corpus):
    '''
    Return a dictionary of title, url, and body.
    Making the user specify the corpus in anticipation of us having more
    than just ssc (which may have different formats).
    '''
    if corpus == "ssc":
       parsed_dict = ssc_parse(filepath) 

    else:
       raise ValueError("Please supply valid corpus")
    return parsed_dict

def single_source_selections(content, search_term):
    '''
    Takes a list of one source's paragraphs.
    Outputs a list of lists of the selections that match the search term, context included.
    Adjacent hit-paragraphs are concatenated into one selection.
    '''
    hits = [idx for idx, val in enumerate(content) if search_term.lower() in val.lower()]
    if hits == []:
        return None
    context = [max(0, hit - 1) for hit in hits] + [min(len(content) - 1, hit + 1) for hit in hits]  
    # combine, dedupe, order
    hits_with_context = sorted(list(set(hits + context)))
    # now, find our selections
    selections_list = []
    for idx in range(len(hits_with_context)):
        paragraph_i = hits_with_context[idx]
        paragraph = content[paragraph_i]
        if selections_list == []:
            # starting
            selections_list.append([paragraph])
        elif hits_with_context[idx - 1] == paragraph_i - 1:
            # still in same selection as last time. add to it.
            selections_list[-1].append(paragraph)
        else:
            # new selection
            selections_list.append([paragraph])

    return selections_list

def bold_selection(sel, search_term):
    '''
    We've already searched through the text to find our selections in the first place
    so it's a little inefficient to do it again. Fast enough.
    Have to search case-insensitive but return original case.
    This implementation sucks - would rather have regex
    '''
    finds = finditer(search_term.lower(), sel.lower())
    starts = [r.start() for r in finds]
    sel_bolded = sel
    # we have to bump up our index each time by 2 * len("**") == 4
    # hence, adding 2*idx to our calculated starts
    for idx, start in enumerate(starts):
        updated_start = start + idx * 4
        sel_bolded = sel_bolded[:updated_start] + "**" + sel_bolded[updated_start:]
        end = updated_start + len(search_term) + 2
        sel_bolded = sel_bolded[:end] + "**" + sel_bolded[end:]
    return sel_bolded

# build markdown.
md = "# " + search_term + "\n\n"
for filename in listdir(corpus_dir):
    parsed = parse_file(corpus_dir + "/" + filename, corpus)
    selections = single_source_selections(parsed["body"], search_term) 
    if selections is not None:
        url = parsed["url"][0:-1] # don't want newline
        title = parsed["title"][0:-1] # don't want newline
        md = md + "## " + "[" + title + "](" + url + ")\n\n"

        for idx, sels in enumerate(selections):
            joined_sels = "\n".join(sels)
            bolded_sels = bold_selection(joined_sels, search_term)
            # only give selection sub-sub-headers if we will loop more than once
            if len(selections) > 1: md = md + "### Selection " + str(idx + 1) + "\n\n"
            md = md + bolded_sels + "\n"

with open(output_filepath, "w") as f:
   f.write(md) 
