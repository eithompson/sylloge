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



