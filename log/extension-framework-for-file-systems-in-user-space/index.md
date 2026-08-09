# Extension Framework for File Systems in User space

2019-07-09 · https://fsgeek.ca/log/extension-framework-for-file-systems-in-user-space/

[Extension Framework for File Systems in User space](https://www.usenix.org/conference/atc19/presentation/bijlani), Ashish Bijlani and Umakishore Ramachandran, USENIX Annual Technical Conference, 2019.

![](https://i2.wp.com/fsgeek.ca/wp-content/uploads/2019/06/AdobeStock_108250546.jpeg?fit=600%2C400&ssl=1)Useful Extensions

The idea of improving [FUSE ](/log/fuse-file-systems-in-user-space/)performance has become a common theme. This paper, which will be presented this week at USENIX ATC 2019 in Renton, WA, is one more to explore how we can improve FUSE performance.

One bit of feedback I received from the _[last](/log/direct-fuse-removing-the-middleman-for-high-performance-fuse-file-system-support/)_[ FUSE performance paper ](/log/direct-fuse-removing-the-middleman-for-high-performance-fuse-file-system-support/)I reviewed (last week) suggested that people do want to build file systems in user space for a variety of reasons, not the least of which is because they want to move that complexity out of the kernel environment. Thus, the argument is that the _reason_ people build kernel file systems is because of performance. While I remain unconvinced that this is not the only impediment to a broader adoption of FUSE file systems, I will save that for a future discussion.

The approach the authors take this time does seem to try and bridge the gap: they're proposal is to add kernel extensions that permit user mode file systems developers to add small modular components to the file system to optimize performance critical aspects. They address the increased security considerations inherent in allowing "kernel extensions" by sandboxing those extensions into an "in-kernel Virtual Machine (VM) runtime that safely executes the extensions".

Their description of FUSE is quite a bit different than what I got from the [FUSE performance paper at FAST 2018](/log/to-fuse-or-not-to-fuse-performance-of-user-space-file-systems/) \- this paper describes FUSE as a "simple interposition layer"; the earlier description made it sound more complex than that. They do point out that FUSE file systems in production are becoming more common and point to Gluster, Ceph, and even Android's SD card file system. For network file systems the overhead of FUSE is unlikely to have a material impact all but the most performance sensitive environments because the overhead of the network likely dominates. Similarly, SD card media is typically slow so once again the rate-limiting overhead is likely not the FUSE library and driver.

In addition to proposing an extension model, the authors also point out that there are a class of "unneeded" operations that are difficult to omit because the level of control offered by FUSE presently is not sufficiently fine grained enough; the authors propose enhancing FUSE to address these issues as well.

They set forth an interesting set of design considerations:

  * **Compatibility** \- their observation is that the extension model must be something that works with existing file systems without requiring redesign or extensive coding.
  * **Extensibility** \- the features offered by **ExtFuse** must allow adding specific features in a clean, minimalistic fashion, so that a FUSE file system developer can pick the specific features needed for their use case.
  * **Safe _and_ Performant** \- these are competing goals; the primary purpose of their work is to improve performance but they cannot do so at the expense of sacrificing security.
  * **Correctness** \- they point out the challenge of having two operational paths (the "fast" path and the "slow" path, where the latter corresponds to the legacy path) 

![](/media/2019/07/Figure1.png)(Figure 1 from Paper)

The authors' provide a graphical description of the architecture of their system in Figure 1 of the paper, which I have reproduced here. It shows the fact there are dual paths: the traditional FUSE path, as well as their accelerated path. 

They move on to describe the extensions they implemented to demonstrate the range of functionality with their extension model:

  * Meta-data caching - the idea is that VFS itself cannot do effective caching due to the nature of its interface; the tighter interface between the extension and the user mode file system make this more practical.
  * I/O stacking - the concept here is that data may have multiple processing layers, such as logging, or union file systems. By permitting the extension to handle this, the overhead is minimized; indeed, this reminded me of the [Scout Operating Systems work](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.87.49&rep=rep1&type=pdf), which focuses on constructing optimized pipelines for such work.



Their evaluation focuses on a handful of critical operations: _getattr_ , _setattr_ , _getxattr_ , and _read/write_. They looked at a mix of optimization models: the use of a smart attribute cache is clearly a win based upon their performance analysis. FUSE remains slower than a native file system in many scenarios however (e.g., they use EXT4 as a benchmark comparison) though the performance seems to be much closer than we've seen in prior work. 

They also ported multiple different file systems to their extension library: StackFS, BindFS, Android's sdcard file system, MergerFS, and LoggedFS. None of them required even 1,000 lines of new code for the kernel extensions. While the authors do discuss some of the observed performance improvements for those file systems, they do not provide us with general benchmark comparisons.

Overall, this is an interesting paper, which combines a number of ideas together into an intriguing package. It will be interesting to see if this gains traction in the FUSE community.
