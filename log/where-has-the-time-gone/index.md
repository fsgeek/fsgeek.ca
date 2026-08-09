# Where has the time gone?

2020-08-05 · https://fsgeek.ca/log/where-has-the-time-gone/

It's been more than a year since I last posted; it's not that I haven't been busy, but rather that I've been trying to do too many things and have been (more slowly than I'd like) cutting back on some of my activities. 

Still, I miss using this as a (one way) discussion about my own work. In the past year I've managed to publish _one_ new (short) paper, though the amount of work that I put into it was substantial (it was just published in _Computer Architecture Letters_). This short article (letter) journal normally provides at most one revise and resubmit opportunity, but they gave me _two_ such opportunities, then accepted the paper, albeit begrudgingly over the objections of Reviewer # 2 (who agreed to accept it, but didn't change their comments).

Despite the lack of clear publications to demonstrate forward progress, I've been working on a couple of projects to push them along. Both were presented, in some form, at [Eurosys as posters](https://www.eurosys2020.org/poster-session/). 

Since I got back from a three month stint at Microsoft Research (in the UK) I've been working on one of those, evolving the idea of kernel bypasses and really analyzing _why_ we keep doing these things; this time through the lens of building user mode file systems. I really should write more about it, since that's on the drawing board for submission this fall.

The second idea is one that stemmed from my attendance at [SOSP 2019.](https://sosp19.rcs.uwaterloo.ca/) There were three papers that spoke directly to file systems: 

  * [File Systems Unfit as Distributed Storage Backends](https://dl.acm.org/authorize?N695037)
  * **[Performance](https://dl.acm.org/authorize?N695045)[and Protection in the ZoFS User-space NVM File System](https://dl.acm.org/authorize?N695045)**
  * **[SplitFS: Reducing Software Overhead in File Systems for Persistent Memory](https://dl.acm.org/authorize?N695046)**



Each of these had important insights into the crossover between file systems and persistent memory. One of the _struggles_ I had with that short paper was explaining to people "why file systems are necessary for using persistent memory". I was still able to capture some of what I'd learned, but a fair bit of it was sacrificed to adding background information.

One key observation was around the size of memory pages and their impact on performance; it convinced me that we'd benefit from using ever larger page sizes for PMEM. Some of this is because persistent memory is, well, _persistent_ and thus we don't need to "load the contents from storage". Instead, it _is_ storage. So, we're off testing out some ideas in this area to see if we can contribute some additional insight.

The other area - the one that I have been ignoring too long - is the thesis of this PhD work in the first place. Part of the challenge is to reduce the problem down to something that is tractable and can be finished in a reasonable amount of time.

![](/media/2020/08/AdobeStock_335005616-scaled.jpeg)Memex

One of the questions (and the one I wanted to explore when I started writing this) is a rather famous article from 1945 entitled [As We May Think](https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/). Vannevar Bush described something quite understandable, yet we have not achieve this, though we have been trying - one could argue that hypertext stems from these ideas, but I would argue that hypertext links are a pale imitation of the rich assistive model Bush lays out when he describes the Memex.

Thus, to the question, which I will reserve for another day: why have we not achieved this yet? What prevents us from having this, or something better, and how can I move us towards this goal?

I suspect, but am not certain, that one culprit may be the fact we decided to stick with an existing and well-understood model of organization:

![](/media/2020/08/AdobeStock_340519156-1024x439.jpeg)Maybe the model is wrong when the data doesn't fit?
