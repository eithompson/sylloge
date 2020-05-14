def ssc_parse(filepath):
    '''
    Returns dictionary containing title, url, and body.
    Title and url are strings. Body is a list of strings (paragraphs).
    '''

    with open(filepath, encoding="utf-8") as f:
        content = f.readlines()
    parsed_dict = {"title": content[0],
            "url": content[1],
            "body":  content[4:]}
    return parsed_dict
