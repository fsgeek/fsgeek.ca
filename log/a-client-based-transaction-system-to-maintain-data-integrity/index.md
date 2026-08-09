# A Client-Based Transaction System to Maintain Data Integrity

2018-02-15 · https://fsgeek.ca/log/a-client-based-transaction-system-to-maintain-data-integrity/

[A Client-Based Transaction System to Maintain Data Integrity](https://dl.acm.org/citation.cfm?id=806565) William H. Paxton, in  _Proceedings of the seventh ACM Symposium on Operating Systems Principles, 1979, pp 18-23._ Last time I discussed the basis of [consistency and locks](/log/granularity-of-locks-in-a-shared-data-base/). I did so because I thought it would help explain this paper more easily. We now move into the nascent world of sharing data over the network (what today we might call  _distributed systems_). One of the challenges of this world is that it involves coordinating changes to information that involves multiple actors (the client and server) that has some sort of consistency requirement. The authors here use the term **integrity** (rather than consistency) but I would suggest the terms are effectively the same for our purposes: 

> _Integrity is a property of a total collection of data. It cannot be maintained simply by using reliable primitives for reading and writing single units -- the relations between the units are important also._

This latter point is important. Even given atomic primitives, any time we need to update related state, we need to have some mechanism beyond a simple read or write mechanism. The definitions offered by the author is highly consistent with what we saw previously: 

>   1. _The_ consistency property:  _although many clients may be performing transactions simultaneously, each will get a consistent view of the shared data as if the transactions were being executed one at a time_.
>   2. _The_ atomic property:  _for each transaction, either all the writes will be executed or none of them will, independent of crashes in servers or clients._
> 


Prior work had focused on having the server handle these issue. This paper describes how the client can accomplish this task. There were some surprising gems here. For example: 

> _If a locked file is not accessed for a period of time, the server automatically releases the lock so that a crashed client will not leave files permanently unavailable_.

We will see this technique used a number of times in the future and it is a standard technique for handling client-side locks in network file systems. Thus, one novelty to the locks presented here is that they have a **bounded lifetime _._** Thus, one of the services required from the **server** is support for this style of locking. The author then goes on to propose the use of an intention log ("intention file" in the paper). The idea is that the client computer locks files, computes the set of changes, records them in the intention log, and then commits the changes. Then the actual changes are applied. To achieve this, it sets out six operations: 

  * **Begin Transaction** \- this is what reserves the intention file. Note that the author's model only permits a single transaction at a time. Note that the other operations **fail** if a transaction has not been started.
  * **Open** \- this is what opens the actual data file. At this point the file header is read. If that header indicates the file is being used for a transaction, the file is recovered before the open can proceed.
  * **Read** \- as it suggests, this reads data from the file.
  * **Write** \- this  _prepares_ to write data to the file. Since this is a mutation, the new data must be recorded in the the intention file at this point. The actual file is not modified at this point.
  * **Abort Transaction** \- this causes all files to be unlocked and closed. No changes are applied. The transaction becomes "completed".
  * **End Transaction** \- this is how a transaction is recorded and applied. The paper describes how this is handled in some detail. In all successful cases, the changes are applied to the server.

The balance of the paper then describes how crash recovery works. The simplifying assumptions help considerably here - this system only permits a single transaction to proceed at a time. Then the author moves on to a "sketch of correctness proof". I admit I did find that humorous as the attempt at formalism without actually  _invoking_ formalism achieves anything other than warm-fuzzy feelings. He wraps up by discussing some complex cases, such as file creation and the challenge of "cleaning up" partially created file state. Having dealt with this issue over the years, I can assure you that it can be complex to get it implemented correctly. He also discusses that some files might have multi-block meta-data headers and explains how those should be handled as well. He concludes with a discussion about handling media failure conditions, which are a class of failures that this system does not claim to protect against.
