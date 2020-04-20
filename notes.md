# Notes

## Topic modeling - Elliott

Some possible search terms:

Content-filtering recommender systems

Latent semantic analysis (LSA)

Latent semantic indexing (LSI)

Topic modelling

Latent Dirichlet allocation (LDA)

Non-negative matrix factorization (NMF)

Pachinko allocation (PAM)


Some links about the above:

<https://en.wikipedia.org/wiki/Pachinko_allocation>

<https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation>

<https://en.wikipedia.org/wiki/Latent_semantic_analysis>

<https://en.wikipedia.org/wiki/Topic_model>

<https://nlpforhackers.io/topic-modeling/>

<https://github.com/topics/latent-semantic-analysis>

<https://medium.com/@lettier/how-does-lda-work-ill-explain-using-emoji-108abf40fa7d>

<https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0>

<https://www.analyticsvidhya.com/blog/2018/10/stepwise-guide-topic-modeling-latent-semantic-analysis/>

One thing to note is that topic models don't use human-understandable topics out of the box. If you want human-understandable topics, you need to do some mapping from topics to the terms, but this will be very very hard. If you come up with a generalizable version of this, you've got a PhD thesis.

You might consider doing LDA then checking each document against some query. Using LDA is probably where I would start.

Another thing you might try is to consider the similarity of each document to the other documents it links to, then try to use some system where you are "recommending" documents by showing similar documents to documents that directly match a search term (kind of like the recommendations you get on Amazon where looking at a book shows you similar books).

With anything, I think you'll need an n-best sort-and-discard step to get only the most relevant documents (and probably show fewer than n documents if the similarity is beneath some threshold).

I've also attached some PDFs about LSI and LDA ([one](https://drive.google.com/open?id=1EPrMEmUN-0UGJe3SmIFM837UyujBBtHs), [two](https://drive.google.com/open?id=1EPrMEmUN-0UGJe3SmIFM837UyujBBtHs), [three](https://drive.google.com/open?id=1EPrMEmUN-0UGJe3SmIFM837UyujBBtHs)).

## Aaron H

It seems like the highest monetization ceiling would be freemium with licenses for academic institutions/school system. 

Some thoughts on it as public facing site:
I agree that academia is the most obvious market for this sort of product. Some sort of integration with existing productivity/social networking/research tools would be pretty important I think. Connecting to their JSTOR, Google Scholar, academia.edu, boutique journal, etc. will be a good way to get around them having to upload or manually enter all of their notes. 

One issue I can see is the way in which people are taught to annotate/take notes is to interact directly with the text. I imagine many academics who are taking notes are doing so manually. Long term I guess this could build out into looking for highlighted words, underlines, dog eared pages and reading handwriting, I guess. But that almost sounds like a different project. The flip side of that, however, is that it should be much easier to collect annotations from uploaded digital pdfs.I love the browser extension idea. That sort of integration is what will get people using the site who wouldn't otherwise.

LaTeX and syntax are both really smart. 

I'm also thinking about this site's functionality as a productivity tool for writing more generally. The layperson may use this to remind themselves about something that they read. But writers, even those outside of academia, have a much stronger use case for this as an outlining tool. Maybe there is an "outlining page" that would be a user-generated version of the wikis. The writer could pull their notes from topics that are relevant to the article/chapter/book they are working on and push them to its outlining page. Then they could reorder the outlining page to structure their work. 

Even more than academics, I imagine writers (fiction and non-fiction), and especially journalists would benefit from this because they likely aren't as concerned with details as an academic would be.

Some sort of in-app note-taking would be necessary for the site's success. I think you identified the major pain point of the site: ' What's the point, though? '. You're asking that question because you don't see yourself looking at a word document with your notes in it. But most people will just ask that question about the site in general. Even before you sell the organizational component to the layman, you need to sell the benefit of taking notes to begin with. That's partially done through marketing. But it's also done by reducing the barriers the user has to take to start building their knowledge base. They need to be presented with a place to start taking notes so they have something to organize. I'm thinking something with a build in structure and reward system, maybe relying on something like the Cornell Note-taking System and including things like pomodoro timers and habit forming tools (streak calculators, setting goals, or calendar based to-do lists)?

That's kind of outside the scope of the organizing project. But people just don't take notes on the things they read. You also identified the big exception to that: students. Even more so than academics, these are people who are forced to take a large volume of notes. 

It would be cool if someone could share their generated, or user-generated pages on a topic, or notes on a topic. What if you could follow someone so that not only your notes appear on a wiki page, but theirs do too. I don't know how insightful I would be about the crusades. But I the professor I follow's public notes on it would definitely be better and more interesting than the wiki page on it. I can see this feature taking off with the open-source, self-help, and with students sharing their summary's of their chemistry lecture. 

In terms of structure, it seems like the first feature would just be a site you can upload notes to to be tagged and organized. From there you can build out the backend the indexing tool to self-generate the wikis and organize by topic, and integrate the other features
All in all I like it.

## Ken B

Some initial thought: before you said academic I was thinking similar but actually for students writing research papers and especially PhD students and senior working on theses. My major question from a market perspective while reading the first 3/4 of the email was, how many people actually write articles or summaries of what they read. Made me realize I don't really understand consumer reading behavior and it varies very widely. I'll sometimes take a picture of a passage that I will probably never look at again, or I'll write something in notes. A really nice feature is highlighting in kindle, and if I could query all highlighted passages or sort to view them by source book or article that would be cool in theory, still I don't see myself using much 

Biggest question for me is what is the goal here? Make a product adopted by many, the goal of which is to make money, or a fun side project to beef up your buddy's sw skills and you get a useful personal tool out of it?

I think either is possible, but you would need to very clearly state who the specific market(s) is/are (academics who blah blah, students working in blah, etc...)

Then do some qual research (discovery interviews) to understand if enough people work in a way where this could integrate in a useful way (or if this would be so valuable it could alter their behavior) 

Then with that you would go back to your feature set and refine further 

But at the high level I think it's a cool idea and I also see expansion opportunities beyond literature (video games, episodes of television, movies, etc..)

Oh and music and art reviews too. Could be cool for that
