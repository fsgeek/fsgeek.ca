# The Newest Memory Dies First

2026-06-29 · https://fsgeek.ca/log/the-newest-memory-dies-first/

TL;DR version - I've released a new tool for Claude Code that prevents the **MEMORY.md** file from being truncated based on length. 

## Background

Like many people doing software development with AI tools, I use **[Claude Code](https://claude.com/product/claude-code)**. This tool changes frequently, sometimes more than once in a day, but often daily. Thus, the functionality landscape is constantly shifting. When I built [Pichay](/log/pichay-treating-llm-context-as-virtual-memory/) and its follow-up project, [Tinkuy](https://github.com/fsgeek/tinkuy) my primary focus was on reducing the use of the context window. It's where I learned that one of the real confounds was the _key-value cache_ , which is used to speed up inference by saving the machine weights for a known prefix (e.g., the "append only log of all prior conversations") and I designed around it while still preserving the benefits of removing detritus from the context window. Eventually I realized the _conversation_ (back and forth between me and Claude) had become the impediment to further reduction in context window usage

[Anthropic](https://www.anthropic.com/) continues to struggle with memory as much as I do:

  * With Opus 4.6 they added an optional, higher cost, 1 million [token](https://www.youtube.com/watch?v=ZUCVRppXPSc) context window - context window usage between 200k tokens and 1 million tokens was charged at 2x the cost (note, they have since gone to a flat price for the full 1 million token context window.)
  * With Opus 4.7 they changed their tokenizer (the bit that converts the _input text_ into the **tokens**) in a way that _increased_ the number of tokens produced. My experience was that context filled up noticeably faster, which was consistent with [report that this increased token usage by about 30](https://www.computeunion.net/blog/claude-opus-tokenizer-hidden-cost-increase-2026)% (Note: actual reports varied up to about 50% so I picked an example in the lower end of the range.)
  * Anthropic introduced a [new memory system](https://medium.com/ai-simplified-in-plain-english/claude-codes-auto-memory-the-end-of-amnesiac-ai-sessions-has-started-62ccfc37d7c8) in late February 2026. The idea was to provide continuity across a project's lifetime. I remember being surprised when I first saw Claude using this as a means of sharing information across instances (a surprising covert channel) that Anthropic made _opt-in_ later. 



That auto memory system they introduced has actually been useful for my projects but I have also found that it suffers from an interesting problem: somewhere around 25,500 _bytes_ , the Claude Code framework truncates the file. Interestingly, Claude Code tells the Claude _instance_ that the limit is 24.4KB, but I found via testing that the number is about 1KB higher. 

> [T]he Claude Code framework truncates the [MEMORY.md] file. [A]nything in the MEMORY.md file after that point [~25,500 bytes] is discarded... which is often the most recent information about the project.

Further testing showed me that it _truncates the file at the boundary_. So, anything in the MEMORY.md file after that point is discarded. This _discards_ the data at the end, which is often the most recent information about the project. I have been working on AI memory systems for over a year now, using **_human_** models for memory as a design model. That human memory model ties into my earlier research around using human episodic memory with activity information (the kind that's already collected by our computers, devices, cameras, sensors, etc.) to improve our ability to find specific things (files) in our storage. This is described in my report about my project, [Indaleko](https://arxiv.org/pdf/2602.20507). Since that time I've been working to build a newer version, and along the way I realized much of what was useful in Indaleko for humans turns out to be useful for AI as well.

For example, when I started addressing that **conversational size** challenge I mentioned earlier (the one that consumes so much of the context window) I asked the question about "what happens if we use the transformer to keep its own rolling summary of the information flow. I described that earlier this month: [Letting the AI Model Keep Its Own Notes](/log/letting-the-ai-model-keep-its-own-notes/). Part of that work involved storing the individual interactions in an [ArangoDB database](https://arango.ai/) (interesting side-note, I see they've now pivoted to pitching this as an AI native database.) That larger memory project is called [Yanantin](https://github.com/fsgeek/yanantin) and I continue to work on that, combining the work on human-friendly storage indexing with AI supporting memory systems. 

When I discovered this MEMORY.md issue in Claude Code, I thought about how I'd incorporate it into Yanantin and realized that could ultimately be a good idea, but I'd like to be able to use it more generally, like in my project around building [explainable governance processes](https://github.com/fsgeek/governance). Requiring a full separate database is a bit of overkill. So what I did instead was build an extension for Claude Code that provides tools to the models using Claude Code allowing it to manage its own memories. 

## Qhaway: a Tool to Watch Over MEMORY.md

I called the project _[qhaway](https://github.com/fsgeek/qhaway)_ (which means "to watch over") and the git repo contains the code. The package is also available via pypi and you can install it using `uvx qhaway init`. The package will reorganize the MEMORY.md file and provide two MCP tools that Claude Code can use for storing and retrieving information. It preserves the original MEMORY.md file and if you uninstall it, it will write a _current_ version of MEMORY.md rather than the original (you can replace the original if you want, but MEMORY.md tends to get stale quickly.)

The infrastructure builds a _projection_ of the complete memory system, an _index_ into what is available, that keeps the size below the maximum. It uses a simple heuristic for doing this and thus far I've found it helps keep my larger projects from losing the important details around the project. Using Claude Code to build and debug its own tools has, itself, been an interesting process, and the tools are working well in the three projects that I had where MEMORY.md was over the limit. I suspect this approach can be used for other files as well (e.g., CLAUDE.md) but that's for future tool work.

When things don't fix, they're declared _and_ you have the tools to find them - just in case. 

![](/media/2026/06/Screenshot-2026-06-29-140024.png)

The project is open source, and I welcome contributions. I hope others find this as useful as I have.
