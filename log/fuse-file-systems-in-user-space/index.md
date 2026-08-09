# FUSE: File Systems in User Space

2019-06-18 · https://fsgeek.ca/log/fuse-file-systems-in-user-space/

File systems are notoriously difficult to implement: of all the pieces that appear in an operating system, they have the highest quality bar and are often called upon more than almost any other part of the operating system; virtual memory management may be called upon more.

Of course, the fact that modern operating systems tend to make the boundaries of file systems and virtual memory a bit fuzzy doesn't really diminish their difficulty.

So, what makes building a file system challenging?

  * _Persistence_ \- file systems do things "for keeps". If you build an application program, you can quit when things go bad. The user can just restart from scratch. A crashing application might leave its own files damaged and require recovery. When a file system gets it wrong (particularly a physical media file system) _it can wipe out all the files_.
  * _Multi-threading_ \- modern operating systems are heavily multi-threaded and often performing I/O. Frequently, that I/O is going through the file system. A multi-threaded application needs to worry about its own data. A file system needs to worry about its own data that's being accessed by _numerous_ threads across _numerous_ applications.
  * _Security_ \- modern operating systems are written with the idea of multi-tenancy in mind. We can use lots of different isolation techniques to help mitigate some of these problems but file systems are fundamentally a layer that revolves around _sharing_ data. I could (and have and probably will again) argue that sharing data might not always be what we want to do. Remember the [CAP file system](/log/the-cap-file-system/ )? One of its interesting features was that it did attempt to hide data and only expose it via capabilities.
  * _Performance_ \- file systems are _extremely_ performance sensitive. Hard disks are slow, with high latencies and modest bandwidth. Of course, SSDs have fixed some of that, with lower latencies and higher bandwidth. They do introduce their own issues that file systems have had to adapt to handle.
  * _Features_ \- each feature you add in a file system tends to create an interference pattern with other features. For example, NTFS implements a file caching scheme for applications called _oplocks_ (opportunistic locks). It _also_ implements byte range locks. The two were not compatible. Then a new set of oplocks were added and they became compatible. The old oplocks are supported, the new oplocks are supported. The good news is that very few applications use byte range locks. It's not the _only_ example, it's just _one_ example.



In my experience, the file systems development cycle starts out with a bold new design: we're going to fix all of the ills of prior file systems and/or implement bold, new features. We'll be faster and more capable. We've studied the work that's already been done and _we know that we can do it better_. Then you build your bold new design and begin to construct your file system. Eventually, you get to a point where it starts to work. Each new feature you add has side-effects that ripple through the code base. You begin to evaluate your file system and you realize it is slow. So you go through some cycles of iterative tuning. These introduce performance at the cost of complexity.

You find out about failure cases you hadn't really understood before; maybe you read about them. You experience failures that you'd never heard of before - only to realize when you're reading some _other_ paper that they're describing the same problem. That's happened to me - the other paper said "we had these weird deadlocks, so we just increased the number of buffers we used and it went away." We actually built a robust reservation scheme to ensure we'd never hit that deadlock.

Deadlocks in file systems are just part of life. You wanted performance so you added fine-grained data structure locking. Then you realized you had special cases where you had _re-entrant_ calls. You find that you can have a thread moving file _a_ to _b_ at the same time that some _other_ thread is moving file _b_**** to _a_. How do you lock _that_ properly? In the past, I've built entire mechanisms for tracking and enforcing lock hierarchies, dealing with re-entrant calls, and ensuring we don't deadlock.

So you performance tune, find and fix bugs, increase your parallelism, and continue your relentless march to victory. You learn about reference counting bugs (the **[ABA](https://en.wikipedia.org/wiki/ABA_problem)**[ problem](https://en.wikipedia.org/wiki/ABA_problem), for example, which I've seen in practice when trying to decrement and delete the reference count). You create interesting solutions that allow parallelism in all but the cases where it _really_ matters.

You get old and grey in the process. You learn how to look at a damaged meta-data structure on disk and _in your head_ theorize how that might happen, then you go look at the code and see if you can find that path.

All you wanted to do was build a file system. Moving a file system into user space is a very micro-kernel like thing to do; I've worked on micro-kernels where the file system _was_ in user space. If it crashes, it doesn't bring the machine down. The only threads it has to really worry about are those it creates. _Maybe_ it isn't as fast. _Maybe_ it isn't as challenging to build.

File Systems in User Space (**FUSE**) is a framework in which a kernel component interacts with an application program - the user-mode file system - and presents it to applications so that it looks much like a file system.

FUSE doesn't fix _all_ the challenges of building file systems, but it does address some of them. Security is addressed by restricting the file system process and the applications to belonging to the same security entity ("user"). The tools available are often easier for the debugging process; testing in user space is simpler due to the availability of test harnesses (kernel file systems can be run for testing purposes in user space as well, as I've done it before. Most of the file system logic isn't tied to any specific operating mode.)

FUSE is a wildly popular interface. The last time I looked on Github.com the number of FUSE file systems numbered in the _hundreds_. At one point I was working on cataloguing them, more out of curiosity than anything else. Indeed, that might make a good write-up for some future post

Applications transparently use a FUSE file system because the file system _supports the standard file systems interfaces_. To the applications, it really does just look like another file system, mounted somewhere in the name space of the operating system itself, such as mounted on a directory in Linux or UNIX. Windows uses mount points and symbolic links to make file systems visible to applications. In either case, applications are oblivious to the fact that these file systems are implemented in user space.

The biggest advantage of this model is that building a new file system via FUSE is _simple_ r. It isn't going to win any performance records, it won't be bootable, and its usage model is much more limited than a "general purpose" file system, but often that's all that is required. For example, there are multiple implementations of a file system on top of[ Amazon's Simple Storage Service (S3) ](https://aws.amazon.com/s3/) \- mostly because it provides a simple-to-use interface that works with existing tools. It certainly is not a _performance-oriented_ approach, but often performance is not actually that important for a specialized service.

I will discuss some of the issues with fuse, and some potential solutions, in a future post.

<https://github.com/libfuse/libfuse>  
<https://github.com/osxfuse>  
[<https://github.com/billziss-gh/winfsp>](https://github.com/billziss-gh/winfsp)
