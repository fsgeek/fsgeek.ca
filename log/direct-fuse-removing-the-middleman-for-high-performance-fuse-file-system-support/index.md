# Direct-FUSE: Removing the Middleman for High-Performance FUSE File System Support

2019-07-02 · https://fsgeek.ca/log/direct-fuse-removing-the-middleman-for-high-performance-fuse-file-system-support/

[Direct-FUSE: Removing the Middleman for High-Performance FUSE File System Support](https://www.osti.gov/servlets/purl/1458703), Yue Zhu, Teng Wang, Kathryn Mohror, Adam Moody, Kento Sato, Muhib Khan, and Weikuan Yu, in _Proceedings of the 8th International Workshop on Runtime Operating Systems for Supercomputers_ , page 6, 2018.

![Modern Fuse, circuit breakers instead of actual fuses.
](/media/2019/06/AdobeStock_170179784.jpeg)Modern Fuse

There are quite a few papers that discuss the performance of the [FUSE model.](/log/fuse-file-systems-in-user-space/) I already discussed a recent paper that explored the [performance of FUSE on Linux](/log/to-fuse-or-not-to-fuse-performance-of-user-space-file-systems/) and that paper observed that I/O performance for FUSE is reasonably good due to the optimization work that has been done to minimize the data copy overhead that can occur with a naive implementation.

What I do find surprising is the emphasis on FUSE performance; this leads me to think that people look to user mode file systems as something viable for implementing _production_ file systems. Of course, one motivation for this is that building a FUSE file system is generally simpler than implementing an in-kernel file system. Some of this is environmental - the kernel is a harsh development environment, in which the smallest bugs lead to the system crashing.

Of course, virtual machine technologies have done quite a lot to minimize this overhead, as the "machine" that crashes is now more like an application. If you are developing code for the UNIX, Linux, or Windows kernel you are likely to be developing using C, the most commonly used systems language these days. It is possible to bravely branch out and use other languages, but then you inherit other interesting restrictions and frequently find that you are developing the _tools_ as much as you are developing the file system.

Thus, one benefit of the user space file systems model is that you can use other development tools - FUSE file system implementations us a much larger range of programming languages than is normally found in kernel file systems. The FUSE model also permits fairly rapid development of a prototypical file system.

Today's paper touches on these traditional issues and points out that sometimes what you need isn't a general-purpose file system but rather something that is specifically crafted to solve the problem at hand. For the HPC community, _performance_ is an important driver for the specialized file systems of choice. The authors' use an optimized library, _libsysio_ , that provides a POSIX-like interface which intercepts I/O operations to a remote file system - in essence, a sort of automated mechanism for turning I/O calls into something reminiscent of RPC.

The emphasis of the authors is in eliminating the overhead of system calls. Their approach is certainly focused: this solution works for a _single_ application that requires high performance operations. 

They start off by evaluating the cost overhead of using FUSE. Because their emphasis is on I/O, that is what they evaluate. Thus, unlike the [earlier FUSE analysis](/log/to-fuse-or-not-to-fuse-performance-of-user-space-file-systems/), which indicated that meta-data operations were the most significant bottleneck, this work concludes there is still substantial impact on I/O performance as well.

They take an existing library from Sandia Labs, _libsysio_. I found multiple different versions of this library available on the Internet and was interested to find that it has been integrated into other file systems, including _[Lustre](http://lustre.org/)_ , with which I have some familiarity from past work. The authors' don't discuss if their approach is better than using other HPC file systems, focusing on improving the performance of their specific use case.

One interesting design consideration for Direct-FUSE is they seek to support _multiple_ FUSE file systems from a single application, using the same high performance communications approach. This is not usually an issue for applications with pure FUSE file systems because to the application the FUSE file system appears to be functionally equivalent to every other file system. This is, however, an issue that can arise when incorporating multiple I/O library based models into a single application; something they address in Direct-FUSE.

They describe their implementation model for supporting multiple distinct file systems, differentiating between file systems via a prefix matching model, and then forwarding name based requests as appropriate. File handle based operations work by using an indirection table for encapsulating the additional state needed to determine which file system should be used to satisfy requests against the particular file handle. 

Much of the paper focuses on the evaluation of their solution. In keeping with their focus on raw I/O performance, the evaluation is _all_ about bandwidth at various I/O sizes. Their results indicate that they are able to achieve performance that is comparable to similar native file systems (they use ext4 and tmpfs implementations for these benchmarks). Thus, they demonstrate that their approach has comparable performance to the native ext4 and tmpfs implementations.

They also compare their performance in the distributed file systems arena using FusionFS, an existing FUSE file system. They show comparable performance for read I/O bandwidth (including scalability to multiple nodes) as well as improved write I/O bandwidth. 

They then evaluate the context switch difference between the two solutions (FUSE and Direct-FUSE) and observe that they have eliminated the context switch overhead.

Bottom line, they have found a way to improve performance over traditional FUSE file systems. They do not compare to other HPC oriented file system (e.g., Lustre) and thus it is difficult for me to tell if this is a viable contender for larger scale distributed file systems work. Nevertheless, they do point out the impact of the context switch costs inherent in the traditional FUSE model.

I am left asking myself "is the goal to make FUSE performance close enough to native kernel file systems that it makes sense to simply implement in FUSE?" Since they only focus on I/O bandwidth, I am not sure if they will achieve this goal for broader benchmarks.
