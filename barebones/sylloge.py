from ssc import parse_ssc
from sys import argv

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
if len(argv) != 3:
    raise Exception("Supply three arguments: search term and directory of corpus")
corpus = argv[1]
search_term = argv[2].lower()
corpus_dir = argv[3]

output_dir = "output/" + "corpus/"
mkdir(output_dir)
output_filepath = output_dir + search_term + "_" +  now + ".md"

def parse_file(filepath, corpus):
    '''
    Return a dictionary of title, url, and body.
    Making the user specify the corpus in anticipation of us having more
    than just ssc (which may have different formats).
    '''
    if corpus == "ssc":
       parsed_dict = parse_ssc(filepath) 
   else:
       raise ValueError("Please supply valid corpus")
    return parsed_dict

def find_selections(content, search_term):
    '''
    Takes a list of one source's paragraphs.
    Outputs a list of lists of the selections that match the search term, context included.
    Adjacent hit-paragraphs are concatenated into one selection.
    '''
    hits = [idx for idx, val in enumerate(content) if search_term.lower() in val.lower()]
    if hits == []:
        return None
    context = [max(0, hit - 1) for hit in hits] + [min(len(hits), hit + 1) for hit in hits]  
    # combine, dedupe, order
    hits_with_context = sorted(list(set(hits + context)))

    # now, find our selections
    selections_list = []
    for idx in range(len(hits_with_context)):
        paragraph = content[idx]
        if selections_list == []:
            # starting
            selections_list.append([paragraph])
        elif hits_with_context[idx - 1] == idx - 1:
            # still in same selection as last time. add to it.
            selections_list[-1].append(paragraph)
        else:
            # new selection
            selections_list.append([paragraph])

    return selections_list




