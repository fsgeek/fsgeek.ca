# What is a File System?

2019-06-06 · https://fsgeek.ca/log/what-is-a-file-system/

I don't know if I've discussed this previously, but if so, feel free to skip it. I had a meeting with one of my supervisors this morning and he observed that something I pointed out "would make a great HotOS paper..." I'm pretty much off the hook on that one, since there won't be another HotOS for almost two years.

[![Neutron star collision](http://www.skyworksdigital.com/wp-content/uploads/2013/09/info-graphic-960x330.jpg)](http://www.skyworksdigital.com/wp-content/uploads/2013/09/info-graphic-960x330.jpg)Copyright 2016 [Skyworks Digital, Inc](http://www.skyworksdigital.com).

I said "we conflate name spaces and storage in file systems". Or something equivalent. Here's my real question: _why do we mingle storage with indexing?_ I realize that indexing needs to be able to ultimately get us what we're looking for, but traditionally we smash these together and call them a "file system". 

[The Google File System ](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/035fc972c796d33122033a0614bc94cff1527999.pdf)paper certainly annoys me at some level each time I read it. But _why_ does it disturb me? Because what they build isn't a file system, it's a key-value store. Yet over the years I have come back to it, repeatedly, and observed that there is an important insight in it that really does affect the way we build file systems: **applications do not need hierarchical name spaces**. What they need is a way to get the object they want. 

Indeed, Amazon's S3 service really is the same thing: an object store in which the "hierarchical name" is nothing more than an arbitrary key. I don't know how it is organized internally, but the documentation is quite clear that the "hierarchical name space" is really just the way the key is encoded.

> An Amazon S3 bucket has no directory hierarchy such as you would find in a typical computer file system. You can, however, create a logical hierarchy by using object key names that imply a folder structure. For example, instead of naming an object `sample.jpg`, you can name it `photos/2006/February/sample.jpg`. 
> 
> [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html)

For me, this is a useful insight because at one point I considered inverting the traditional directory hierarchy, so that rather than have a directory point to it's children, I would have each file maintain a list of the directories to which it points. Then "enumerating a directory" becomes "finding all the files with a specific attribute". One motivation for considering this approach was to avoid the scaling issues inherent in large directories (which led me to an interesting looking PhD thesis _[Scale and Concurrency of Massive File System Directories](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.1019.5875&rep=rep1&type=pdf)_ \- more for the reading list!) This is an important concern in a world in which I'm suggesting adding multiple different indices.

But back to the more fundamental question: _why_ do we conflate them? Recall that the original thinking around file systems mirrored the physical nature of existing physical filing systems (I discussed that somewhat back when I talked about [my Eurosys presentation](/log/eurosys-2019/)) rather than the more free-flowing linkage present back in the [Memex ](/log/as-we-may-think/)model. In a world where the physical copy is located by using its naming information, this does make sense.

Consider how a modern library is organized (yes, some people still collect books!) The _location_ of the object (book) is important, but the _categories_ of the object are equally important - it's properties. A card catalog could be organized by topic, and would then give you information allowing you to find the work itself.

Applications don't need hierarchical name spaces - those are something that _humans_ use for managing things. Applications need persistent location information. By using a mutable location key with application we create a situation in which _things break just by reorganizing them_.

S3 does not fix this issue, since "moving a file" is equivalent to "changing its key". In that way, it misses my point here. However, I suspect that those keys don't actually change very often. Plus, S3 has other useful concepts, such as versioning.

What you do lose here is the ability to "check directory-wise security". That will likely bother some people, but for the vast majority of situations, it really doesn't matter.

Typical file systems actually do use key-value stores, although local file systems do it with simple keys (e.g., "i-node numbers"). These keys turn out to be useful: NFS looks up files using that i-node number, which is embedded inside the file handle. We did the same thing in AFS, going so far as to add an "open by i-node number" system call so the server could be implemented in user mode. Windows does the same thing with CDFS and NTFS, and I've implemented file systems that support "open by ID" for both file and object IDs.

Thus, my point: we merge the name space and the storage management together because "that's the way we've always done it". The POSIX interface, which codified how things were done in UNIX, embeds this further as there is no open by i-node number and the security model requires a path-wise walk.

Ah, but the failings of POSIX are something that I'll save for another post.
