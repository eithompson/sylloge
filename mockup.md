# "French Revolution" Search Results

## Table of contents
1. An Essay on Three Revolutions (2 locations, exact match, max relevance score 97%)
2. A History of the Guillotine (1 location, match via "Robespierre", max relevance score 70%) 
3. Coldplay: Genius or Mediocre? (1 location, exact match, max relevance score 5%) 

## An Essay on Three Revolutions

### Location 1
*Exact match. Relevance: 97%*

And now we move to the most important revolution of the 18th century.

I am of course speaking of the **French Revolution** (Sylloge bolds the matches). This part of the document mentions many topics that emphasize the centrality of the French Revolution to it: Paris, the Bastille, Louis XVI, Marie Antoinette, blah blah blah. The single-topic model, which uses the Wikipedia page for this topic, tells Sylloge that all of these words mean this part of the text is very much on-topic. This means that this location gets a high relevance score.

It even has another paragraph that's very clearly relevant to the search term. Three estates, liberalism, Edmund Burke, etc.

On the other hand, this other revolution I am about to start talking about is not so relevant. Now I'm onto a new topic. This is just surrounding text that Sylloge provides for context (and perhaps as proof to the user that we cut the selection off at the right place).

### Location 2
*Exact match. Relevance 80%*

But back to the big one.

Now we're talking about the **French Revolution** again. This part has a lower relevance score because there aren't as many terms like the Bastille and political upheaval, but it is still pretty relevant. 

And now we're off the topic again.

## A History of the Guillotine

### Location 1
*Match via "Robespierre". Relevance 70%*

This part of the document is about famous people who have been killed by the guillotine.

Now it starts talking about **Robespierre**. Like in the above document, many terms are mentioned that indicate this portion of the document is relevant: upheaval, terror, 1789, etc. However, unlike the above document, this one does not ever mention the search term directly. Maybe the writer assumed that the reader would know who Robespierre was and which revolution he was a part of. Ultimately, we want Sylloge to match this to our search term since it's clearly relevant, despite not explicitly containing our search term. Our neo4j "multi-topic model" makes this possible.

Some surrounding text.

## Coldplay: Genius or Mediocre?

### Location 1
*Exact match. Relevance 10%*

Coldplay has nothing to do with our search term.

However, this paragraph mentions our search term, but only to clarify that the painting on the cover of *Viva La Vida* is not actually a depiction of the **French Revolution**; it's a painting of the July Revolution of 1830. This paragraph goes on to talk about how the band picked the font used on the cover, which has nothing to do with our search term. Our topic model is able to pick this up, because the distribution of words looks nothing like our search term's Wiki page.

Now we're onto a completely different topic.
