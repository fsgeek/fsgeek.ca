# 360° Semantic File System: Augmented Directory Navigation for Nonhierarchical Retrieval of Files

2019-07-18 · https://fsgeek.ca/log/360-semantic-file-system-augmented-directory-navigation-for-nonhierarchical-retrieval-of-files/

[360° Semantic File System: Augmented Directory Navigation for Nonhierarchical Retrieval of Files](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8618600), Syed Rahman Mashwani and Shah Kusro, in IEEE _Access_ , January 29, 2019.

![360° Perspective](/media/2019/07/AdobeStock_132012080.jpeg)360° Perspective

This paper makes some interesting observations that resonate with my own research observations, though I will end up arguing (in a future blog post) that they don't go far enough. But they do a good job of laying out the problem and why some solutions do not work. One of the common themes I have heard when discussing my own work is an insistence there really isn't a problem, though usually a longer conversation ends up with us agreeing things _could****_ be done better.

The abstract is a bit long, but clearly describes the essence of the paper:

> The organization of files in any desktop computer has been an issue since their inception. The file systems that are available today organize files in a strict hierarchy that facilitates their retrieval either through navigation, clicking directories and sub-directories, in a tree-like structure or by searching (which allows for finding of the desired files using a search tool). Research studies show that the users rarely (4% - 15%) use the latter approach, thus leaving navigation as the main mechanism for retrieving files.   
> However, navigation does not allow a user to retrieve files nonhierarchically, which makes it limited in terms of time, human effort, and cognitive overload. To mitigate this issue, several semantic file systems (SFSs) have been periodically proposed that have made the nonhierarchical navigation of files possible by exploiting some basic semantics but no more than that. None of these systems consider aspects such as time, location, file movement, content similarity, and territory together with learning from user file retrieval behaviors in identifying the desired file and accessing it in less time and with minimum human and cognitive efforts.   
> Moreover, most of the available SFSs replace the existing le system metaphor, which is normally not acceptable to users. To mitigate these issues, this research paper proposes 360 SFS that exploits the SFS ontology to capture all the possible relevant file metadata and learns from user browsing behaviors to semantically retrieve the desired files both easily and timely. Based on user studies, the evaluation results show that the proposed 360 SFS outperforms the existing traditional directory navigation and recently open files.
> 
> Paper Abstract

Of course, the problem existed before the appearance of the desktop computer: the [original UNIX ](/log/the-unix-time-sharing-operating-system/)contained the _permuted index server_ , which suggests to me that even in 1973 people were struggling to find things. What I do find interesting is the observation that people really do not like search - I [recently described this insightful (to me at least) observation](/log/the-ubiquitous-digital-file-a-review-of-file-management-research/). Here it is once again, complete with references (in the paper) to prior work demonstrating this point. Indeed, it suggests to me one alternative explanation as to why the [Google Desktop Search](https://en.wikipedia.org/wiki/Google_Desktop) project was ultimately cancelled - not because it was "no longer necessary" but rather because it wasn't useful to most computer users.

Another thing that I have observed, repeatedly, when working with students, is there seems to be a natural aversion to _searching_ for answers. Thus, students will post on class forums (such as Piazza, with which I am most familiary) asking questions, _even if the question has already been asked and answered_. Searching for the answer does not seem to come naturally to such students. Indeed, I often find myself using search engines to find the answer and giving the results back to the original question. I have wondered about this "laziness" in the past and with this new insight I wonder if it is just because people prefer to _navigate_ \- and being told where to go is certainly one form of navigation.

Interestingly, like the [Graph File System](/log/gfs-a-graph-based-file-system-enhanced-with-semantic-features/) paper I described previously, these authors also argue that we cannot abandon the hierarchical _view_ of files. I am not convinced of this, but I can understand the appeal of starting from it as a basic premise. We have been doing some work recently on a graph visualization model for the file system, more as a prototype, but it is surprisingly functional and encouraging us to look at alternative visualizations of file system data _for navigation_. In other words, thinking of the problem as a _search_ problem ultimately seems to be the wrong path - yet that is the point of things like semantic file systems, to improve search.

The paper has an extensive review of prior work, much of which I've also previous described, though there were a few systems I had not previously seen. Table 1 of the paper has a comparison of features across the various file systems. Thus, the authors distinguish themselves from prior by focusing on providing enhanced functionality, using auxiliary directories, in which they display related content. They focus on:

  * Temporal characteristics - they focus on _when_ files are being used, not merely frequency. This is an idea we've been exploring as well.
  * Geographical location - this is intriguing; identifying **where** the user was when they accessed a given file.
  * File movement - when files are reorganized and moved around.
  * File access patterns - they cluster files as related based upon the temporal proximity of their access; another idea we've been exploring. I found it insightful they describe this as a "relationship" though they do not explore a broader range of relationships.
  * Content similarity - files that are identical or substantially similar can be associated together; this is another technique that we've been actively investigating.
  * Manual tagging



They describe the file system they implement, which is essentially a layered file system in which they add two virtual directories: **NOW** and **TAGS**. They describe the interface for adding this information as well, which I found cumbersome, but it is in keeping with their goal of not deviating from the existing hierarchical interface. They do also permit the creation of custom virtual directories as well, though that is only briefly mentioned in the paper.

One of the problems they highlight, which resonated with me because we've been discussing the same problem, is how much information to display to users - in essence, when confronted with _too many_ options, users quickly become overwhelmed. 

Their evaluation focuses on the amount of time it took users to locate their files when using their enhanced file systems model and they lay out a case for the fact their system works well for their study group. One limitation of their study group is that it is based upon an experienced computer user group, but this is reflective of their environment.

One interesting comment was that while they used Linux for their evaluation, Windows would have been a better platform because of its broader usage within their organization. I have wondered how much the use of Linux tends to create a bias in an evaluation of this type, since most people are using Windows or Apple computers. Would the results be similar?

The authors do point to their open source implementation of their file system. I have not yet evaluated it, but it is definitely something on my (all too long) list of things to do.
