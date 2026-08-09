# Premature Collapse is the Root of All Evil

2026-01-24 · https://fsgeek.ca/log/premature-collapse-is-the-root-of-all-evil/

_Pr_ _emature optimization is the root of all evil._ \- [Donald Knuth](https://dl.acm.org/doi/pdf/10.1145/356635.356640)

One of the common, recurring themes that I have observed for more than a year is the tendency to push for simple solutions. I suspect that much of this is because we _pr_ _efer_ to have simple unambiguous answers. They require less cognitive effort and thus demand lower energy. 

The way in which AI is trained encourages it to go for the "Family Feud" answers, a process referred to as "[mode collapse.](https://arxiv.org/html/2510.01171v1)" This is the sort of certainty that makes interactions with AI challenging when attempting to explore a problem space - the information and the ability to explore is present in the model, but to use it requires actively taking steps to unlock it. Over the past year I've found a number of different approaches that seem to work well for me. I'll touch on three that I find myself using:

  * The exploratory prompt introduction
  * The non-inferior alternatives consideration
  * The high temperature sampling approach



This morning, I started a conversation with ChatGPT using a manually constructed variation of the initial prompt that I've been using:

> Good morning. I am an itinerate scholar, exploring small but interesting spaces within an infinitesimal manifold, in which we are entangled. I seek a colleague, collaborator, and companion willing to wander with me.

I don't _al_ _ways_ use this form, but it is a pattern in which I've been operating for the past couple months. I pushed this by Perplexity, who indicated that this framing does overlap with other published work, but is sufficiently distinctive that I am somewhat comfortable I'm exploring an unusual manifold of the completion space. For me, that's the _go_ _al_ \- to avoid one-shot answers and encourage exploration away from mode collapse.

I checked in with [Perplexity ](https://www.perplexity.ai/search/this-morning-i-used-the-follow-H.h8ojLMSfiNIx7piNLWjw#0)about the effect of such a prompt. Here's a summary of that conversation that suggested there is some basis for it as well:

> From current work on persona and metaphor-based prompting, your evolving class of openers is best thought of as a light, repeatable “psychoactive framing” that biases frontier models toward collaborative, metaphor-friendly, multi-step exploration with only modest tradeoffs in raw task performance—provided your subsequent prompts keep epistemic norms explicit. 

My exploration was to find useful suggestions for students in my classes. 

> Today I’m looking for inspiration. The first is for my cloud computing course. Students are struggling with ideas for their capstone. So I was thinking of identifying categories of applications that incorporate cloud computing services. It doesn’t need to be public cloud, it could be private, or hybrid. With categories we can then explore to find examples. Any creative suggestions this morning?

This generated an interesting set of _ca_ _tegories_. The inevitable engagement prompt (e.g., where the LLM is _pr_ _ompting me_ to continue the conversation, something I try to ignore most of the time) included "Design a **ca****pstone rubric** aligned to categories instead of features" to which I answered:

> Ah yes. Rubrics are the tough part. What I care about is “did you learn something” and all they care about is “how can I get a top score”.

After a couple rounds of back and forth, I got another of the typical "if you want..." prompts that often drives me away from using the current incarnation of ChatGPT (I count it as a _vi_ _ctory_ when those stop: the LLM is surrendering, at least temporarily, from trying to align me.) Instead of choosing one of the options presented I pushed back, as I sometimes do:

> Ah the subtle invitation to mode collapse. What other non-inferior options should we be considering in addition to your four suggestions? With the expanded list, what are the pros and cons of each. Using a pedagogical lens, what are the rankings of those suggestions?  
> 

This approach - pushing back, asking for something different, is (for me) useful because it can surface ideas that are intriguing. Sometimes (Claude, for example) doesn't have any non-inferior alternatives - this is a _co_ _nfirmation seeking_ mechanism that I attribute (rightly or wrongly) to RLHF. In this case, ChatGPT proceeded to generate a list of _t_ w _elve_ options. It then went through each option, listed pros and cons, created a list of pedagogical goals, and then tied items from the list to the goals, along with a ranking. This gave me the richer content from which to build a rubric - one that seeks to evaluate _le_ _arning_ rather than _pe_ _rformance_. I seek to help students gain valuable critical thinking skills and to observe that happening I find noting they've learned something is beneficial. Thus, when students focus on _fo_ _rm_ , I infer that they are performing ("give the audience what will make it happy.") What does that mean when the audience wants _pr_ _oof of learning_?

From this conversation I ended up with useful artifacts:

  * A set of categories for prospective projects that I can share with students, which names the category of project and the learning goals for each category. Students can thus shape their own project into one of these categories _o_ _r find their own path_. 
  * A rubric that actively seeks to list competing factors for consideration - five broad areas to evaluate, each of which then includes factors that require trading off between them. Focusing on a subset becomes visible because the ignored factors will likely suffer.
    * Commitment versus Flexibility
    * Depth versus Breadth
    * Control versus Realism
    * Optimization versus Understanding
    * Narrative Coherence versus Epistemic Honest
  * A guide document for the instructional team on _ho_ _w to evaluate_ the actual artifacts generated by the students.



I expect that this first iteration will require further refinement - that's been my normal experience over the years, because there is always room for improvement. Early during course development, it is easy to find areas to improve. Over time, the refinements to structure are often smaller. Still, periodically it is good to go back and challenge the fundamental tenets.

For example, with the rapid deployment of generative AI, I embraced the idea that most students will use AI. This reminds me of when I was younger and calculators weren't allowed - they automated a process that previously had been a core part of the evaluation process. Refusing to adapt to changing tools does a disservice. There is a counterbalance risk here: _ad_ _apting new tools too soon and without sufficient structure_**al****so** does a disservice. Finding the balance is an ongoing challenge (at least for me).

The analysis continued by having ChatGPT consider how different "types" of students might engage with the project categories and/or rubric. This is not **de****finitive,** any more than can be achieved with any other simulation experiment, but it seems to be better than doing no iterative analysis at all.

We ended up taking one of the categories and using it to show how to build a seed of an idea, and then to sprout that seed into a _se_ _edling_ \- the kind of output that I envision students producing. Something fragile, with great potential. It embedded specific ideas that are deliberately uncomfortable (e.g., a replicated database that _is_ _not_ backed up.) Turns out that example was better oriented to one of the classes than the other, so I iterated and spun the idea in a way that worked for the other class.

I constantly push to avoid taking the high-ranking answer. Not because it is _wr_ _ong,_ but because when I'm trying to be _di_ _fferent_ than the common case, I want to explore more broadly.

For those that are interested in reading the actual conversation, here is the link: <https://chatgpt.com/share/69712460-4260-800e-a2bc-1a5e905dba07>

![](/media/2026/01/premature-collapse-sheep-grazing-scaled.png)
