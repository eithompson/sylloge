# sylloge

## Link to SSC data
[Here](https://drive.google.com/open?id=1s7H9gqXPLpEFBpU9fgH7XvW9aWKbinjQ) is my scraped data of Slate Star Codex. Didn't want to store this in Github so I added a gitignore.

I think he's a good test case because he's written a lot about MANY different topics. 

## Outline for v1

My proposition, super simple:

The program should take a search term along with the corpus, and output a Markdown file in which each section is a document in which the search term was found. The text within each section is basically the surrounding n paragraphs/words/whatever around the location where the search term was matched.

Sub-sections reflecting those of the actual source document would be nice. If someone searches "term" and it shows up in section a of document x, and it shows up in document z which has no sections, then:

    # Document x
    
    ## Section a 
    
    blah blah term blah blah
    
    # Document z
    
    blah blah term blah blah

## To-do

### Main

- Fully spec out v1

### SSC scraper

- Fix bug where we don't get the entire post. It seems like blockquotes mess it up.
- Scrape each post's tags (rel="tag") 
- Differentiate which lines are "header" lines for sections within the post. Sadly, he just just seems to bold these lines instead of using a real differentiator.


### Managerial

- Set up a trello board. Not trying to jump the gun - this won't be necessary for a little while.
