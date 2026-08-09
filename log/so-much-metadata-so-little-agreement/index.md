# So Much Metadata, So Little Agreement

2022-10-06 · https://fsgeek.ca/log/so-much-metadata-so-little-agreement/

Earlier this year I was focused on collecting _[activity data](/log/challenges-of-capturing-system-activity/)_. I made reasonable progress here, finding ways to capture local file system activity as well as activity against two different cloud service providers. I keep looking at other examples, as well, but rather than try for too much breadth, I decided to focus on the three sources I was able to get working and then push deeper into each source.

First, there is little agreement as to what metadata should be present. There are a few common fields, but then there are numerous fields that only show up in some subset of data sources - and this is just for _file systems_ where presumably they're storing the same basic stuff. What's most common:

  * A name
  * A timestamp for when it was created
  * A timestamp for when it was modified
  * A timestamp for when it was accessed
  * Some attributes (read-only, file, directory, special/device)
  * A size



Of course, even here there isn't necessarily agreement. Some file systems have limited size names or limited character sets they support. Timestamps are stored relative to some well-known value. UNIX traditionally chose January 1, 1970 00:00:00 UTC and that number comes up quite often. IBM DOS (and thus MS-DOS) for x86 PCs used January 1, 1980. Windows NT chose January 1, 1601. I do understand why this happens: we store timestamps in finite size fields. When the timestamp "rolls over" we have to deal with it. That was the basis of the [Y2K crisis](https://en.wikipedia.org/wiki/Year_2000_problem). Of course, I've been pretty anal about this. In the late 1970s when I was writing software, I made sure that my code would work at least to 2100 (2100 is _not_ a leap year while 2000 was a leap year because of the rules for leap years.) I doubt that code survived to Y2K.

But file systems designers worry about these sorts of things because we know that file systems life surprisingly long lifetimes. When the Windows NT designers first settled on a 64 bit timestamp in the late 1980s they gleefully used high precision timestamps: 100 _nanoseconds_. But 64 bits is a lot of space and it allows storing date for many millennia to come.

Today, we store data all over the place. When we move it, those timestamps will be adjusted to fit whatever the recipient storage repository wants to use. In addition, any other "extra" metadata will silently disappear.

How much _extra_ metadata exists? I've spent the past few weeks wading through Windows and even though I knew there were many different types of metadata that could be stored, I chuckled at the fact there is no simple way to retrieve all that metadata:

  * There are APIs for getting timestamps and sizes
  * There are APIs for getting file attributes
  * There are APIs for getting file names
  * There are APIs for getting a list of "alternate data streams" that are associated with a given file.
  * There are APIs for retrieving the _file identifier_ of the file - that's a magic number that can be combined with data from other APIs to associate activity information (and _that_ is the reason I went spelunking for this information in the first place.)
  * There are APIs for retrieving "extended attributes" of files (EAs). EAs are older than Windows NT (1993) but have been difficult to use from the Win32 API that most applications use.
  * There are now APIs for retrieving _linux_ related attribute information (see [FILE_STAT_LX_INFORMATION](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_stat_lx_information)) on top of the existing attributes. 
  * There are 128 bit GUIDs _and_ 128 bit File IDs



I'm sure I didn't hit them all, but the point is that these various metadata types are not supported by all file systems. On Windows at least, when you try to copy a file from NTFS to FAT32 (or ExFAT) it will warn you about potential data loss if certain attribute data is present (specifically alternate data streams.) The _reason_ I think they first added this (it was added a long time ago) was because in the early days of downloading files from the internet it became useful to _tag_ them as being potentially suspect. This is done by adding an alternate data stream to the file (**::Zone_Identifier**) and then information about the remote location from which the file was downloaded.

Thus, this metadata isn't added _just because_ , it is added because it enables potentially useful functionality.

Here's something I've never seen anyone do thus far - that doesn't mean nobody does it, just that I haven't seen it: nobody indexes based upon these attributes. The named stream Zone_Identifier could be used to find all the files that you've downloaded from the internet, regardless of where on your computer. I laugh at this because I know a number of times I've downloaded content and then had _no idea_ where it was downloaded. With an index of downloaded content, I could just look at the last five things I downloaded - problem solved.

While I have spent a fair bit of time talking about Windows, I have seen similar issues on Linux. It is only in the past couple of years that the extended _stat_ structure (statx) has become mainstream supported. Several file systems that run on Linux support extended attributes. The idea behind streams isn't particularly novel (we implemented something we called _property lists_ in [Episode](/media/2017/11/1992-The-Episode-File-System.pdf) at the same time the NTFS team was deciding to all full-blown named alternate data streams to their file system. Ours were just limited in size - an approach that I think the ReFS team took because they found nobody was really using large alternate data streams.)

Bottom line: one of the interesting challenges in using activity data is that as similar as file systems seem on the surface they often implement different/special semantics using metadata. How to make sense of this is a significant problem and one that I do not expect to fully address. Despite this, I can see there is tremendous benefit to using even some of this metadata to build relationships between different storage locations. That, however, is a topic for another day.
