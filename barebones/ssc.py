def ssc_parse(raw_text):
    '''
    Returns dictionary containing title, url, and body.
    Title and url are strings. Body is a list of strings (paragraphs).
    '''
    parsed_dict = {"title": raw_text[0].strip(),
            "url": raw_text[1].strip(),
            "body":  raw_text[4:(len(raw_text) - 1)]}
    return parsed_dict
