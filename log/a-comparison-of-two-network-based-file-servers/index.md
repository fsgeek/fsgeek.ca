# A Comparison of Two Network-Based File Servers

2019-07-11 · https://fsgeek.ca/log/a-comparison-of-two-network-based-file-servers/

[A Comparison of Two Network-Based File Servers](https://dl.acm.org/citation.cfm?id=358475)  
James G. Mitchell and Jeremy Dion, in _Communications of the ACM, April 1982, Volume 25, Number 4._

![PAir of File Servers](/media/2019/07/two-file-servers-196x300.jpg)

I previously described the [Cambridge File Server](/log/the-cambridge-file-server/) (CFS). In this 1981 SOSP paper the inner details of it and the Xerox Distributed File System (XDFS) are compared. This paper provides an interesting insight into the inner workings of these file servers.

Of course, the scale and scope of a file server in 1982 was _vastly_ smaller than the scale and scope of file servers today. In 1982 the disk drives used for their file servers were as large as 300MB.

![SD Cards](/media/2019/07/AdobeStock_168577948-Converted-266x300.png)

This stands in stark contract to the sheer _size_ of modern SD cards; I think of them as _slow_ but compared to the disk drives of that era they are quite a bit faster not to mention smaller. I suspect the authors of this paper might be rather surprised at how the scale has changed, yet many of the basic considerations they were making back in the early 1980s are still important today.

  * Access Control (Security) - CFS was, of course, a capability based system. XDFS was an identity based system; most systems today are identity based systems, though we find aspects of both in use.
  * Storage Management - the interesting challenge here is how to ensure that storage is not wasted. The naive model is to shift responsibility for proper cleanup to the clients. Of course, the _reality_ is that this is not a good model; even in the simple case of a client that crashes, it is unlikely the client will robustly ensure that space is reclaimed in such circumstances. CFS handles this using a graph file system and performing garbage collection in which an unreachable node is deemed subject to reclamation. XDFS uses the more naive model, but mitigates this by providing a directory service that can handle proper cleanup for clients - thus clients _can_ "do it right" with minimal fuss, but are not constrained to do so.
  * Data Consistency - the authors point to the need to have some form of transactional update model. They observe that both CFS and XDFS offer atomic transactions; this represents the strong semantic end of the design spectrum for network file servers and we will observe that one of the most successful designs (Sun's NFS) went to a much weaker end of the design spectrum. Some of this likely reflects the database background of the authors.
  * Network Protocols - I enjoyed this section, since this is very early networking, with CFS using the predecessor of token ring and XDFS using the 3Mb/s version of Ethernet. They discuss the issues inherent in the network communcations: flow and error control (so message exchange and exception/error handling) and how the two respective systems handle them 



The authors also compare details of the implementation:

  * They describe a scheme in CFS in which small files use a direct block, and larger files use indirect blocks (blocks of pointers to direct blocks). This means that small files are faster. It is similar to the model that we see in other (later) file systems, while XDFS uses binary tree, used to track allocation of blocks to files, and a bitmap, used to indicate free/used space information.
  * They discuss _redundancy_ , with an eye towards handling (partial) disk failures. Like any physical device, the disk drives of that era did wear out and fail. 
  * They discuss their transaction log and how each system guaranteed consistency: they both use _shadow pages_ , but their implementation of them is different. Ultimately, they both have similar issues, and similar impact. Shadow pages are a technique that we still use.



The evaluation is interesting: it is not so much a measure of performance but rather insights into the strengths and weaknesses of each approach. For XDFS they note that their transaction support has been successful and it permits database transactions (in essence, XDFS becomes a form of simple database service). They point to the lack of support for both normal and special files; from their description a special file is one with guaranteed write semantics. They also observe that ownership of files is easily lost, which in turn leads to inefficient storage utilization. They observe that it is not clear if the B-tree is win or lose of XDFS. 

For CFS they point to the performance requirements as being a strength, though it sounds more like a design constraint that forced the CFS developers to make "hard choices" to optimize for performance. Similarly, they observe that the directed graph model of CFS is successful and capabilities are simple to implement. Interestingly, they also point to the index as well as string of names and access rights as being a success point. They also point to the fact that CFS generalizes well ("[t]wo quite different filling systems built in this way coexist on the CFS storage.") They also point to automatic garbage collection as being a net win for CFS, though they also point out that CFS uses a reference count in addition to the garbage collection model. They list the CFS limitation of transactions to a single file or index as being one of its shortcomings and point to real-world experience porting other operating systems to use CFS as an indicator of the cost of this limitation. Interestingly, the limitation they point to ("... since file directories are implemented as an index with an associated file, it is currently impossible to update both structures in a single transaction.") They conclude by arguing that XDFS has a better data layout, arguing that XDFS's strategy of page allocation and intention logging is ultimately better than CFS's cylinder maps: "... the redundancy function of cylinder maps does not seem to be as successful as those of page allocation and intentions logging; the program to reconstruct a corrupted block is not trivial."

Ensuring correct recovery in a transactional system certainly challenging in my experience, so I can understand the authors' concerns about simplicity and scalability.

Overall, it is an interesting read as I can see may of the issues described here as being _file systems_ issues; many of the techniques they describe in this paper show up in subsequent file systems. The distinction between file system and file server also becomes more clearly separated in future work.
