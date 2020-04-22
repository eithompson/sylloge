# Sylloge Spec

## Purpose and basics

Sylloge is a topic search system whose purpose is to increase the long-term value of a corpus of text to readers and writers. The user provides a search term ("topic") and is returned a document which contains all selections from the corpus that match the topic, and which is itself organized by the source document of each selection. This should be especially useful with corpora containing very long documents which cover many different topics (e.g., books, detailed book reviews/summaries, etc).

The topic tagging NLP model (which determines whether a selection should be returned in a topic search) will be trained on Wikipedia data - this will restrict query-able topics to Wikipedia article titles. A selection of text will be determined as relevant to a topic if the selection is linguistically similar to the topic's Wikipedia page, **or** if it is linguistically similar to Wikipedia pages which are "close" to the topic's Wikipedia page. "Close" is measured by hyperlinks and Wikipedia "metastructures" (e.g., [Categories](https://en.wikipedia.org/wiki/Category:2007_video_games), [Portals](https://en.wikipedia.org/wiki/Portal:History), etc).

### A clarification

The original motivation of Sylloge was to maximize the value of the users' own personal writings (such as a blog, or a personal collection of book summaries), ideally with the consequence of encouraging the user to write more by providing a way to usefully access their writings by topic. While this may continue to be a focus of the project, I have realized from scraping a blog (in order to provide some testing data) that indexing _others'_ writings may be just as useful. For instance, the user could add their favorite bloggers or writers to their corpus and easily search through their collected writings. Alternatively, bloggers could add this functionality to their site. Robin Hanson, Tyler Cowen, etc have all written enormous amounts of blog posts. Ideally, Sylloge would provide a better solution to search than bloggers' manual tagging, and plaintext search.

## The multi-topic model

The primary building block of Sylloge is what we'll call the **single-topic model**. This is a standard topic tagging NLP model **trained on Wikipedia**, whose input is a topic and a selection of text, and whose output is a boolean indicator of whether the text is a match for the topic. This can either be a simple bag-of-words approach ("does the frequency of each word in the selection from the corpus roughly correspond to the frequency of each word in the topic's wikipedia page?") or any of a number of more advanced models.

On its own, this approach is limited. Imagine a section of an essay talking about [Touch of Evil](https://en.wikipedia.org/wiki/Touch_of_Evil). We could have the best NLP model in the world, which could identify a selection of text as being about Touch of Evil even without mentioning the name of the film ("Now let's talk about Orson Welles's 1958 classic, which is so legendary I don't even need to say the name.")

However, what if the user instead searched for film noir? Surely we would want this selection to be returned to the user. But would it? The language used in our selection might be similar enough to the [film noir page](https://en.wikipedia.org/wiki/Film_noir) (perhaps based on the frequency of Welles's name alone), but then again it might not. The phrase "film noir" is only used two times in the article's text.

Other examples are easy to think of. Is a selection of text which is about Super Mario Galaxy likely to be linguistically similar to the video game Wikipedia page? Probably not. Do we want a search for "video game" to return this selection? Definitely.

Solution: the **multi-topic model**. In the film noir example, the very first link in the Touch of Evil article text is to the film noir page. At the bottom of the article, we see that one of Touch of Evil's categories is film noir. Our text selection may not be similar to the text of the film noir page, but it *is* similar to a page that is clearly connected to film noir. So: we can use the structure of Wikipedia to build a meta-model which matches text to topic either by similarity between text and topic, or by similarity between text and adjacent-topic.

To facilitate this, we will use [Neo4j](https://en.wikipedia.org/wiki/Neo4j) to store the [Wikipedia data](https://en.wikipedia.org/wiki/Wikipedia:Database_download) in a graph format. Nodes are articles, edges are links. We will need to construct our own links which determine the rules of whether similarity to page x should trigger a match on page y (this might not be transitive!). I call this the **association model**: it is what ties the single-topic models together into a multi-topic model. It will also live in Neo4j.

## Infrastructure and workflow

(will write commentary on this in detail later)

![Infrastructure and workflow](images/infra-1.png)

## Interface

Need to flesh out ideas for this. Not urgent, though. Creating the actual interface will likely be the last part - we will probably just be generating markdown files for a while.

## Note on neighborhoods

We need to check different neighborhoods of each source document against the model. We're not just trying to find source documents that match our search term - we want _selections from_ source documents that match. But how big are the "neighborhoods" that define our candidates for selectionhood? Too narrow, and the returned selections will be too out-of-context. Too wide and there will just be too much text returned from each hit. Simple options for delineating neighbhorhoods: paragraphs, or a set number of sentences.  Another option could be a minimum/maximum between paragraphs and words/characters. As many full paragraphs as are required to reach 100 words, or something like that.

There may be some kind of mathematical trick here if the model is simply frequency-based. Like a kernel density estimate (moving average, basically) combined with a minimum density cutoff. This way we just have a score at each word which gets its actual "neighborhood" score and we only take sentences whose words all score above the cutoff. This seems more elegant.
