# ZUFS

2019-07-16 · https://fsgeek.ca/log/zufs/

After one of my earlier posts on FUSE file system performance, someone mentioned this project to me - the Zero copy Userspace File System project (**ZUFS**) which appears to be a NetApp sponsored project.

![Sometimes Zero is best](https://i1.wp.com/fsgeek.ca/wp-content/uploads/2019/07/AdobeStock_130934292.jpeg?fit=600%2C300&ssl=1)Sometimes Zero is best.

There have been a variety of talks about this project, including the [Linux Plumber's Conference](https://linuxplumbersconf.org/event/2/contributions/87/) (which was held next door to me - I can see the venue from my window as I write this), as well as the [SNIA Persistent Memory Summit in 2018](https://www.snia.org/sites/default/files/PM-Summit/2018/presentations/04_A_PMSummit_18_Golander_Final_Post.pdf). The NetApp repositories on Github.com contain both a file system reflector ([zufs-zuf](https://github.com/NetApp/zufs-zuf)), which appears to be similar to the FUSE kernel driver, as well as the user mode server ([zufs-zus](https://github.com/NetApp/zufs-zus)) which handles dispatching the kernel level requests to the user mode file system implementations.

Their concern appears to be eliminating the copy of **any** data between kernel and user mode, which makes sense given their objective of supporting persistent memory, such as the new [Intel Optane DC Persistent Memory](https://www.intel.com/content/www/us/en/architecture-and-technology/optane-dc-persistent-memory.html) that has recently become commercially available.

Persistent memory __ benefits from a direct access model, in which traditional file data caching is eschewed in favor of direct access. Thus, data is read or written directly from the underlying persistent memory, rather than copied from a buffer cache.

There are a few persistent memory file systems, including UCSD's [NOVA](https://cseweb.ucsd.edu/~swanson/papers/FAST2016NOVA.pdf) file system, though usually they were developed using emulation of persistent memory. In such systems, there is no benefit to copying the data from persistent memory into DRAM and back; indeed, it is a significant performance impediment.

What is not currently present in the NetApp repository is an implementation of a user mode persistent file system (they have a dummy file system implementation, which appears to be the base from which one could build a real file system). This definitely presents an interesting alternative to using traditional FUSE.

![Fuze vs ZUFS](/media/2019/07/FUSE-v-ZUFS-Penalty.png)FUSE vs ZUFS Performance (from NetApp SNIA presentation)

I have not had an opportunity to play with this new system yet, but it certainly does seem to be intriguing - and the performance graph from the SNIA presentation is rather compelling, given the massive improvement in scalable performance.

There sure are quite a few alternatives to traditional FUSE to consider...
