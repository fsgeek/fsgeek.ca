# Laundry Baskets: The New File System Namespace Model

2021-09-28 · https://fsgeek.ca/log/laundry-baskets-the-new-file-system-namespace-model/

![A large pile of laundry in a laundry basket, with a cat sleeping on the top.](/media/2021/09/laundry-basket-with-cat-on-top-1024x1024.png)The "Laundry Basket" model for storage.

While I've been _quiet_ about what I've been doing research-wise, I have been making forward progress. Only recently have ideas been converging towards a concrete thesis and the corresponding research questions that I need to explore as part of verifying my thesis.

I received an interesting article today showing that my research is far more relevant than I'd considered: "[FILE NOT FOUND](https://www.theverge.com/22684730/students-file-folder-directory-structure-education-gen-z)". The article describes that the predominant organizational scheme for "Gen Z" students is the "Laundry Basket" in which all of their files are placed. This is coming as a surprise to people who have been trained in the ways of the hierarchical folder metaphor.

While going through older work, I have found it is intriguing that early researchers did not see the hierarchical design as being the pinnacle of design; rather they saw it as a stop-gap measure on the way to richer models. Researchers have explored richer models. [Jeff Mogul](https://research.google/people/JeffreyMogul/), now at Google Research, did his PhD thesis around various ideas about improving file organization. [Eno Thereska](https://enothereska.wordpress.com/), now at Amazon, wrote an intriguing paper while at Microsoft Research entitled "[Beyond file systems: understanding the nature of places where people store their data](https://www.microsoft.com/en-us/research/wp-content/uploads/2013/02/MSR-TR-2013-26.pdf)" in which he and his team pointed out that cloud storage was creating a tension between file systems and cloud storage. The article from the Verge that prompted me to write this post logically makes sense in the context of what Thereska was saying back in 2014.

The _challenge_ is to figure out what comes instead. Two summers ago I was fortunate enough to have a very talented young intern working with me for a couple months and during that time one of the interesting things he built was a tool that viewed files as a _graph_ rather than a tree. The focus was always at the center, but then it would be surrounded by related files. Pick one of those files and it became the central focus, with a breadcrumb trail showing how you got there but also showing other related files.

The relationships we used were fairly simple and extracted from existing file meta-data. What was actually quite fascinating about it though was that we constructed it to tie two disjoint storage locations (his local laptop and his Google Drive) together into a single namespace. It was really an electrifying demonstration and I have been working to figure out how to enable that more fully - what we had was a mock-up, with static information, but the visualization aspects of "navigating" through files was quite powerful.

I have been writing my thesis proposal, and as part of that I've been working through and identifying key work that has already been done. Of course _my_ goal is to build on top of this prior work and while I have identified ways of doing this, I also see that to be truly effective it should use as much of the prior work as possible. The idea of not having directories is a surprisingly powerful one. What I hadn't heard previously was the idea of considering it to be a "laundry basket" yet the metaphor is quite apt. Thus, the question is how to enable building tools to find the specific thing you want from the basket as quickly as possible.

For example, the author of the Verge article observed: "More broadly, directory structure connotes physical placement — the idea that a file stored on a computer is  _located_ somewhere on that computer, in a specific and discrete location." Here is what I recently wrote in an early draft of my thesis proposal: "This work proposes to develop a model to separate naming from location, which enables the construction of dynamic cross-silo human usable name-spaces and show how that model extends the utility of computer storage to better meet the needs of human users."

Naming tied to location _is_ broken, at least for human users. Oh, sure, we need to keep track of **where** something is stored to actually retrieve the contents, but there is absolutely no reason that we need to embed that within the name we use to find that file. One reason for this is that we often choose the location due to external factors. For example, we might use cloud storage for sharing specific content with others. People that work with large data sets often use storage locations that are _tuned to the needs of that particular data set_. There is, however, no reason why you should store the Excel spreadsheet or Python notebook that you used to _analyze_ that data in the same location. Right now, with hierarchical names, you need to do so in order to put them into the "right directory" with each other. 

That's just broken. 

However, it's _also_ broken to expect human users to do the grunt work here. The reason Gen Z is using a "laundry basket" is because it doesn't require any effort on their part to put something into that basket. The work then becomes when they need to find a particular item. 

This isn't a new idea. Vannevar Bush described this idea in 1945: 

“Consider a future device for individual use, which is a sort of  
mechanized private file and library. It needs a name, and, to coin  
one at random, ”memex” will do. A memex is a device in which  
an individual stores all his books, records, and communications,  
and which is mechanized so that it may be consulted with exceeding  
speed and flexibility. It is an enlarged intimate supplement to his  
memory.”

He also did a good job of explaining why indexing (the basis of hierarchical file systems) was broken:

“Our ineptitude in getting at the record is largely caused by the artificiality of systems of indexing. When data of any sort are placed in storage, they are filed alphabetically or numerically, and information is found (when it is) by tracing it down from subclass to subclass. It can be in only one place, unless duplicates are used; one has to have rules as to which path will locate it, and the rules are cumbersome. Having found one item, moreover, one has to emerge from the system and re-enter on a new path. 

“The human mind does not work that way. It operates by association. With one item in its grasp, it snaps instantly to the next that is suggested by the association of thoughts, in accordance with some intricate web of trails carried by the cells of the brain. It has other characteristics, of course; trails that are not frequently followed are prone to fade, items are not fully permanent, memory is transitory. Yet the speed of action, the intricacy of trails, the detail of mental  
pictures, is awe-inspiring beyond all else in nature.”

**We knew it was broken in 1945**. What we've been doing since then is using what we've been given and making it work as best we can. We knew it was broken. Seltzer wrote "[Hierarchical File Systems Are Dead](https://dash.harvard.edu/bitstream/handle/1/5136361/Seltzer%20-%20Hierarchical%20File%20Systems%20are%20Dead.pdf)" back in 2009. Yet, that's what computers still serve up as our primary interface.

The question then is what the right primary interface is. Of course, while I find that interesting I work with computer systems and I am equally concerned about how we can build in better support, using the vast amount of data that we have in modern computer systems, to construct better tools for navigating through the laundry basket to find the _correct_ thing.

How I think that should be done will have to wait for another post, since that's the point of my thesis proposal. 

![](/media/2021/09/AdobeStock_67771381-200x300.jpeg)
