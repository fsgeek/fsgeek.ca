# To FUSE or Not to FUSE: Performance of User-Space File Systems

2019-06-20 · https://fsgeek.ca/log/to-fuse-or-not-to-fuse-performance-of-user-space-file-systems/

_[To FUSE or Not to FUSE: Performance of User-Space File Systems](https://www.usenix.org/system/files/conference/fast17/fast17-vangoor.pdf)_  
Bharath Kumar Reddy Vangoor, Vasily Tarasov, and Erez Zadok,  
in _The 15th USENIX Conference on File and Storage Technologies_ (FAST '17),  
February 27 - March 2, 2017, Santa Clara, CA, USA.

Previously, I discussed some of the rationale behind [FUSE ](https://fsgeek.ca/?p=694)and a basic introduction to why we use it. This paper is actually a detailed analysis of the _performance_ of FUSE. I have spent a fair bit of time reading - and re-reading - this paper, in order to understand what some of the bottlenecks are within FUSE itself. One area I have previously explored are possible ways of improving its performance; indeed, this is one of my current projects.

![Figure 1 from original Vangoor Paper](/media/2019/06/Figure-1.png)

Figure 1 in the paper is actually a basic block diagram providing an interface model for how FUSE fits into the file systems layer. FUSE consists of:

  * The kernel mode FUSE driver; on Linux this is part of the kernel; and
  * The user mode FUSE library. This handles interactions between the FUSE file system _driver_ and the user mode file system _process_ (referred to as a "daemon" or "background process") in the diagram.
  * The user mode FUSE file system itself - this is the code that implements the FUSE library interface (one of them, since there are two different interfaces).



Applications can then access this FUSE file system without knowing any details of the implementation.

![FUSE kernel driver queuing model.](/media/2019/06/Figure-2.png)

In Figure 2 from the paper, the authors show the internal structure of how the FUSE kernel driver manages various internal data structures that handle events between the user mode file system and the kernel mode file system support. This includes the messages between the kernel and user mode application (requests and their corresponding replies) as well as synchronous and asynchronous file system operations and the cache invalidation mechanisms ("forgets").

Caching is an essential part of the system because it allows the system to quickly respond to repetitive events. The downside to caches are that they can become invalid because the underlying state _changes_. Thus, there is a mechanism for invalidating the cache itself.

The author describes the model within the FUSE library and the two interfaces it exposes: the _low level API_ , which provides greater control to the user mode file system, at the cost of more state management - specifically the mapping of a _path name_ to the _inode_ (**index node**).

The authors describe how they constructed a new FUSE file system, **StackFS** , for evaluating the behavior of the system. StackFS sits on top of an existing file system and attempts to minimize the amount of mapping it performs, since the goal of the authors is to evaluate the performance of FUSE itself.

![Table 3 from the paper](https://i1.wp.com/fsgeek.ca/wp-content/uploads/2019/06/Figure-3.png?fit=600%2C813&ssl=1)

The authors summarize their findings in _Table 3_ , using both a hard disk and an SSD, the two most common types of storage media used on modern computer systems. 

These results were both surprising _and_ interesting to me because some of them surprised me. The performance bottlenecks were not for I/O as much as they were for meta-data operations. Random write performance (which is what we see with databases, for example) is not ideal, but their optimizations did a good job of addressing this, bringing the I/O overhead of the FUSE model down substantially relative to the native file system.

Bottom line: the challenge in improving FUSE performance now moves squarely into the arena of _meta-data_ operations. Creating and deleting files is quite expensive in FUSE. 

The authors conclude by pointing out that there is further room for improvement; they suggest some potential future directions. I have been looking at ways to improve this as well and I will discuss those in a future post.
