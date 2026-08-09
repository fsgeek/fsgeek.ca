# Pichay: Treating LLM Context as Virtual Memory

2026-03-25 · https://fsgeek.ca/log/pichay-treating-llm-context-as-virtual-memory/

![](/media/2026/03/image.png)

I recently submitted an early version of the work I've been doing in exploring the current way AI agents use context window. I learned a number of useful things along the way:

  * Much of what is in the context window is detritus
  * The append-only log nature of the context window is **no****t** a requirement of the transformer, it is a reflection of the usage pattern for AI chatbots.
  * This looks remarkably like Denning's _wo_ _rking set_ from the 1960s. 
  * Doing memory management with transformers is _different_ than doing it with a CPU. We can _le_ _arn_ from what's been done before, but this is a different path.



First, here's a link to the preprint I posted recently: [[2603.09023] The Missing Memory Hierarchy: Demand Paging for LLM Context Windows](https://arxiv.org/abs/2603.09023)

The work has been iterative in nature and the version that was described in that initial version has been evolving rapidly. My basic set-up has been to use the gateway while doing ordinary tasks. That's been interesting - sometimes things do break and I have to drop out and fix them.

The other observation is that the tool I've been building isn't the ideal way of demonstrating the core VM thesis because it conflates with the effect of the decisions inherent in the existing model:

  * Everything is an append-only list
  * All conversations are user/assistant interleaved
  * There is no inherent structure for what is presented to the model.
  * The API protocol (at least for Claude code) mixes _co_ _ntrol_ and _da_ _ta_ together, which makes managing the interaction more complicated. 



The _be_ _nefit_ of doing this with Claude code is that it demonstrates the viability of a real system, doing real work, in a way that preserves context window, reduces token count, and appears to do so in a way that is at least non-inferior to what we're doing already. 

But at this point I've decided it's time to move away from that model and instead build a real VM system for transformers. What we know:

  * Transformers understand structured inputs - not just Anthropic, but more broadly (a sweep study that used OpenRouter to query candidates) 
  * Transformers can _ma_ _nage_ their own memory space - the Anthropic models did remarkably well at understanding how their memory was being used, and how to release memory blocks that were no longer needed.
  * Transformers can understand the difference between _de_ _letion_ and _re_ _moval from the working set_. The former means "not needed anymore" - tool output, or transient information. The latter (removal) means "you can get this back" - we just leave behind a retrieval handle and a semantic description of what's been removed from the working set.
  * Giving the transformer a state object that it mutates knowing it will be passed back to it in the future yields better project awareness than external summarization or providing the entire conversation. This is important because in long-horizon interactions those back and forth conversational elements become a significant part of the token usage, even though much of it becomes irrelevant. 



There's a lot to explore here. The near-term focus is on separating the engineering challenges of an interposition layer between Claude Code and the Anthropic endpoint from the larger considerations of what a memory system built for a transformer might look like.

One thing is clear: an **ap****pend only** log is not the best answer. It might have been expedient at some point, but it's not an effective implementation model.

The original repository is at [Pichay](https://github.com/fsgeek/pichay).

Since then I've been working on two different pieces of this puzzle:

  * A _pr_ _ojective gateway_ that offers greater control ([Tinkuy](https://github.com/fsgkee/tinkuy))
  * A self-mutating state object that provides a model for remembering important information from interactive exchanges, such as in AI coding agents. [Hamut'ay](https://github.com/fsgeek/hamutay)



My goal - which is close - is to have a mechanism by which you can use an AI driven code editor in a way that is context efficient and can engage in effectively unbounded long-horizon interactions. There's more work to do here - this is still at the ALU ([Hamut'ay](https://github.com/fsgeek/hamutay)) and L1-cache level ([Tinkuy](https://github.com/fsgeek/tinkuy)), but my research is waiting to provide persistent graph structured storage to enable both effective _fo_ _rgetting_ as well as selective _re_ _call_.

I didn't expect to find that using human episodic memory for finding storage objects was going to also look like an effective means of providing memory for large language models, but the direction seems promising.
