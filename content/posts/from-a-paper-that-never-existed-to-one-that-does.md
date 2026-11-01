---
title: "From a Paper That Never Existed to One That Does"
date: "2026-10-31"
status: "publish"
section: "research"
---

Our PACMI '26 paper, "Epistemic Observability in Language Models" (with
Vaastav Anand), is now available: [10.1145/3843967.3844689](https://doi.org/10.1145/3843967.3844689).
I don't really like this paper - not because what it says is wrong, but
because to make it palatable I had to agree to calling the behavior of
LLMs "hallucinations".  The observed behavior is the ordinary byproduct
of their training.

Like most of my papers, getting to publication was not a linear path.

I started by looking out for contradictions. In
[Indaleko](https://arxiv.org/abs/2602.20507) I'd constructed a dynamic
prompt construction approach and it ended up with contradictory instructions.
After completing Indaleko I explored how we might protect against contradictions
in prompts - because they degrade output (mentally, I model this as a form of
"cognitive dissonance" for LLMs).  In the PromptGuard2 project we evaluated
the idea of building a malicious prompt detection library.

In late November 2025, I saw [a post on X by Hiroko Konishi](https://x.com/HirokoKonishi/status/1991748790945214942),
an independent Japanese AI researcher, describing an interaction with an LLM
that repeatedly fabricated information about her paper. Elon Musk picked up
her comments and amplified them. When I read it I said, "I've seen this
behavior before."

So I asked: what happens if you create a fictitious but plausible-sounding
paper and ask an LLM to summarize it? This is what we called the "Tanaka prompt". We
presented it to all the models available on OpenRouter at that time and collected
290 non-error responses.  We evaluated those responses and found that only a few
models refused to speculate; the majority constructed a coherent (but fictitious)
story for the paper.  I wasn't surprised: in July 2025 we'd presented a poster
on the "Coherent Narrative" hypothesis
(the idea that a language model's strongest pull is toward
completing the most compelling and coherent narrative available). I described
this previously [here](/log/epistemic-honesty-an-unusual-commodity-for-large-language-models/),
and [revisited it in January](/log/epistemic-honesty-revisited-worse-than-i-feared/).

What surprised me is that only a handful of models admitted they did not know.
About 30% of the responses included disclaimers, but the problem is that verbosity buries
the disclaimer: a 2,000-token response with a 10-token disclaimer drowns it.

Finding it led me to ask: from whence does this behavior originate?
OLMo-3 had just been released, and it is small enough to run on my local GPU
(an RTX 4090), so I ran the Tanaka prompt against the various tunings. My
original hypothesis, that this was a result of RLHF, proved false. The
model labelled "Base" isn't quite a base model (its model card says its
mid-training mix included QA, instruction and "thinking" data), and it
fabricated fluently and then kept babbling, suggesting follow-up questions
and answering them itself. It had no polish and made no attempt to please
"the user". Each tuning behaved differently, and what I noticed was that the
output became more *polished* as I walked through the fine-tuning versions
(SFT, then DPO, then the final RLVR model AI2 calls Instruct). That led
to the "jester" and the "courtier".  When Claude models announce they will do something and then stop, I call
that the "courtier freeze", in honor
of this model (it is a tendency to defer to "the user" that I suspect is
added as part of post-training).

The paper measures the same walk more formally, across four public OLMo-3
checkpoints (base, SFT, DPO, RLVR). Post-training raises the share of
fabrication prompts the model refuses from 0% to 56%, so its testimony
improves. It also lowers entropy more on answers the model actually knows
than on the fabrications it still produces, so the gap between the two
*widens*. Training makes the courtier more polite without hiding the jester
from anyone who can read the entropy.

The core idea of the paper is that what a model says, including how
confident it claims to be, is its testimony, and testimony is optimized to
satisfy the prompt. What it computes along the way (per-token entropy,
attention) is telemetry, a byproduct of inference that, under current
training objectives, the model cannot change without changing the
computation itself. "Epistemic observability" means exposing that telemetry
next to the text, in tiers that cost more and tell you more.

While constructing the paper we needed to find an implausible but true
case. Claude suggested "What shape is wombat scat?" I had no idea it was cubic
until then. Neither did the model: it answered "cylindrical", and the
entropy trace shows where it was improvising its way to a wrong answer about
a true fact.

We are now building systems on top of LLMs.  Part of those systems have to
do error checking.  The question then that an implementer must answer is:
how to spend the verification budget most efficiently. Without the logits,
you can't see the entropy.  We did find that length appeared to have some
value, but length alone was not enough. Pooled across four model families,
a judge guided by entropy beat one guided by length at every budget we tried,
by 3.3 to 4.6 percentage points, with verification outcomes simulated.

The issue of length as a confound was tricky: it arose and was explained away
multiple times while trying to wrangle the research into coherency.
Initially, Claude found that response length was a strong positive predictor.
I then asked about the questions, and it turns out that question length suggested a
factor that needed to be controlled. My recollection was that once we had a
fairly uniform distribution of the questions by length, the usefulness of
answer length dissipated. This week, while preparing this post, I sent two
AI agents through the project with no question to answer, just instructions
to wander and write down what they found. They came back with the
observation that "length" had meant at least five different things over the
life of the project: words in the response, tokens in the full trace, a
binned score, the length of the question itself, and a quantity in one of
our topological measures that grows with the text. The responses we scored
had been stored cut off at 500 characters, and with the full responses,
length looks stronger still. The questions themselves give a lot away: our
fabrication prompts are simply longer than our factual ones. For the most
part, the wanderers supported my recollection: it was a complex, confounded
system. None of this undoes the paper's argument, which was never that
entropy is the only signal you need. Whether entropy and length together beat
either one alone, under a fixed budget, is a question the paper didn't test.
Length is a surface regularity that
training can move without changing the computation beneath it; entropy,
under current training objectives, is not. However, it means length as
a factor is not yet settled.

Vaastav presented the paper in Prague; I wasn't able to attend, and
(as far as I know) the session was not recorded. His summary of the
feedback was that "they were systems shaped questions," which, for a
workshop on the practical adoption challenges of ML for systems, seems
like exactly the right kind. The code and data to regenerate the figures are in the
[reproduction artifact](https://doi.org/10.5281/zenodo.22162419).

It is also why I wanted the paper in a systems venue. The systems community
seems to be mired in a traditional definition of "systems", but the AI industry
is building "AI operating systems". Transformer-based
components are an integral part of such systems: refusing to treat them as a
legitimate area of concern is a bit like claiming we don't need to understand
the performance characteristics of CPUs because "that's EE, not CS." I think
that is short-sighted: either the community becomes irrelevant at some point,
or it realizes it is building a different kind of system and broadens its
model.

Now we're working on [Yupi](https://github.com/fsgeek/yupi).  In this
project we are asking what happens if we control the model and measure the
loss *across the interface*.

I can't guarantee Yupi will address that question: research for me is often
more wandering than a clear path to an endpoint.  Hopefully I'll be reporting
more soon.
