# Graph File Systems

2019-05-09 · https://fsgeek.ca/log/graph-file-systems/

We [submitted a paper to HotOS 2019 ](/media/2019/04/notdead.pdf)in which we (unsuccessfully) made the argument that file systems as hierarchies is hobbling our ability to enhance the usability of file systems. 

One of the blind reviews pointed to a pair of papers, [one of which I've already reviewed](https://fsgeek.ca/?p=603) (I'll review the other, but I didn't consider it to be the same thing, except vaguely in name as it ends up being a semantic tagging system). This paper actually pre-dates the work I submitted to [Eurosys ](/log/eurosys-2019/)and profoundly influenced that work.

Five pages isn't really much space to explore this area. Further, it was about a week before the deadline that I found out HotOS, while an ACM workshop now, uses an older template for its format, with wider margins and larger text, so the five page draft version we had became 6.5 pages! After surgery, it was back down to five pages but missing some useful discussions.

After submission of the HotOS paper, someone pointed me to a Stack Overflow article describing a 1958 paper (_An Information Filing and Retrieval System for the Engineering and Management Records of a Large-Scale Computer Development Project)_ that may be the earliest record of hierarchical file structure (Figure 1).

![](/media/2019/04/erma.png)Figure 1: ERMA Diagram mapping file folders to hierarcy

This is certainly not "new knowledge" as it has been extensively discussed in prior work - hierarchical structure fits the model in which physical filing was actually done.

This becomes clear by the time we get to [Multics ](/log/multics-i-o/)(Figure 2). We now have a model of directories and files organized in a strict hierarchical fashion.

![](https://i1.wp.com/fsgeek.ca/wp-content/uploads/2019/04/multics-file-system-hierarchy-redrawn.png?fit=600%2C397&ssl=1)Figure 2: 1965 Daley, et. al. Multics I/O Diagram (redrawn)

In my experience, when one presents a model and then finds it necessary to "hack" the model to be usable, it suggests that _maybe_ the model is wrong - or at least not optimal. In the _[same paper](/log/multics-i-o/)_ the authors observe that they found it useful to augment hierarchy with _links_. But the introduction of links converts their hierarchy into a _directed acyclic graph_. Similar, yet not the same.

![](/media/2019/04/multics-file-system-hierarchy-with-links-redrawn.png)Figure 3: 1965 Daley, et. al. Multics I/O Diagram _with links_ (redrawn)

In all fairness to the Multics folks, this was a reasonable option at that point. They had substantial limitations that would make graph processing impractical at that point (indeed, there are some who are likely to question whether or not graph processing at this level is practical _now_).

![Simplified graph file system model](/media/2019/04/Model-Graph.png)Figure 4: Simplified Graph Model

So what is it I envision? In Figure 4 I've started with a simplified graph model. In the model I'm envisioning (please keep in mind, this is a _work in progress_ and quite likely to change) is that we have a clear separation between the _name space_ (which is the graph) and the _storage manager_ (which deals with figuring out how to deal with data).

One important benefit to come out of the rejection was identification of the [QMDS paper ](https://fsgeek.ca/?p=603)\- it helps establish _why_ hierarchy isn't good, even if the solution they put forward has limitations. For me, this is a blessing in disguise because I've had to spend so much time justifying _why there is even a research question here_ that pointing to prior work (which wrestled with the same issues and made many similar arguments) allows me to focus future work more on the solution.

The graph model makes sense to me because it generalizes the hierarchical tree (a _minimally connected graph_) and existing relationships, including links. We are much more familiar with graphs now than we have been in the past: [Facebook](https://www.facebook.com/) and [LinkedIn ](https://www.linkedin.com)are at their heart relationship graphs. Computer memories are much larger than in 1965, as are storage capacities. During the Eurosys Doctoral Workshop someone asked me about the overhead of such a system and I made the bold statement that I would be willing to spend 10% of my storage space if it dramatically improved my ability to find things. Surprisingly, that seemed to mollify the person asking.

It is the capture of _relationships_ that distinguishes this approach from the more classic tagging approach. A **tag** represents an extension of some property of what a file **is** , not **how it relates to other files**. We've actually had tagging systems for a very long time - when I worked on [Episode](https://pdfs.semanticscholar.org/acca/916dcf29e548a8f3bd53b05acd18380b0f03.pdf) we explicitly decided to add "property lists" as a form of extended attribute; not quite as general as _streams_ in NTFS, but a similar idea (as I understand it, they chose to do something similar in ReFS - they support alternate data streams, but they are limited to 128KB. Episode had a 64KB limitation for property lists.)

Why aren't _tags_ enough? Because they associate information with the specific file (or directory). What they fail to capture is relationships across file system objects. Why do we want relationships?

Up to this point I've been arguing that we want relationships because they provide us with the ability to _find_ things. One of the very intriguing take-aways from _[The Ubiquitous Digital File](https://fsgeek.ca/?p=597)_[ paper](https://fsgeek.ca/?p=597) is the observation that **people prefer navigation to search**. That's a pretty profound observation when viewed against 30 _years_ of research into tagging systems. Apple's Spotlight and Microsoft's search focus on improving _search ability_.

I'm pretty old-school here. When I am looking for something I often resort to searching for it by name from the command line and _once I find it_ I navigate to the containing directory. I had not really considered that for me navigation is my **primary** mechanism and I use search as a secondary mechanism.

One of the most common uses of graphs by "real people" are maps. I've known this and I have considered visualizations of data as being a map between data elements. What I had not really considered is that _we navigate maps all the time_. If our data is organized in a graph fashion, we could consider navigating it much like we might navigate a map, or walk through relationship graphs such as Facebook or LinkedIn.

The foundation of this research direction is the relationship graph. Thus, the next phase of my work is really to explore what a reasonable representation of the namespace in this system would look like. More to discuss and consider in a future post!
