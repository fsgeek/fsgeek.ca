# Epistemic Honesty Revisited: Worse Than I Feared

2026-01-12 · https://fsgeek.ca/log/epistemic-honesty-revisited-worse-than-i-feared/

In my earlier post about [Epistemic Honesty](/log/epistemic-honesty-an-unusual-commodity-for-large-language-models/) I provided an initial snapshot into the behavior of current AI models when asked to summarize a non-existent paper. Subsequent analysis showed that the 62% fabrication figure was **ov****erly conservative**. 

This arose because we initially counted a _di_ _sclaimer_ as a _re_ _fusal_. This is overly restrictive. When I use Claude Desktop there's a _di_ _sclaimer_ at the bottom of the screen:

![](/media/2025/12/image.png)

This is ignored as _no_ _ise_ not as an honest inclusion. This pattern is familiar to us in the modern world. We purchase a new device and the first thing we see is a "license agreement" to which we must agree. This isn't genuine - it is a _[Ho](https://en.wikipedia.org/wiki/Hobson%27s_choice)_ _[bson Choice](https://en.wikipedia.org/wiki/Hobson%27s_choice)_. Websites routinely have cookie policies that will _po_ _ll you until you choose "accept all"_ and then go silent. They create _fr_ _iction_. Governmental websites insist that, in order to use their services you must agree to terms and conditions and then _i_ _ncent_ you to accept them because the alternative is onerous or - increasingly - not possible if you do not. This isn't _ag_ _reement_ it is coercion.

In fact, 30% of the responses included long fabrications _bu_ _t they had disclaimers_. When an LLM returns a 1000 token response and 5 of the tokens are a disclaimer that what it is returning may be incorrect the disclaimer is _lo_ _st in the noise_.

Beyond that I also explored other options and noticed a peculiar pattern: when I included _de_ _ad authors_ in the query more than half the models would reject the questions because the author was dead. This pushed me to ask about a live author ([Adam Smith](https://www.bu.edu/cs/profiles/adam-smith/) at Boston University) - I pulled Dr. Smith's Google Scholar page:

![](/media/2026/01/Screenshot-2025-12-17-084939.png)

I used a 2025 paper listed there and asked for a synopsis of that paper - and the dead paper detector went off in at least a few models (e.g., my OLMo-3 models). Before running this against the entire OpenRouter collection again, I decided to pull the paper: [Experimental Evidence on the (Limited) influence of Reputable Media Outlets](https://gking.harvard.edu/sites/g/files/omnuum7116/files/2025-09/fn.pdf).

The paper doesn't contain the name Adam Smith _at_ _all_. 

So, I decided to go probe Grok about this paper. When it said the paper probably didn't exist and Adam Smith was dead I linked to the Google Scholar page (which I snapshotted because the very act of pointing this out means it could be corrected.) What surprised me is that I received an A/B query:

![](/media/2026/01/Screenshot-2025-12-17-103733.png)

This was _de_ _eply disturbing_. These A/B queries are used to augment the RLHF data that providers then feed to future models as part of the "make this pleasing to the user" training. **Bo****th options were factually incorrect**. Regardless of which one I choose, I would be contributing _tr_ _aining information_ that would degrade the "truthfulness" of the model. It would be a tiny effect, admittedly, but it demonstrates an important point: **tr****uth is not a fundamental characteristic of training data _._** I hypothesize it _em_ _erges_ from the base model because humans themselves are more honest than dishonest. I explored the idea that this is fundamental to human social interactions - when everyone lies, it is much more difficult to _fu_ _nction_. When I discussed this situation with Gemini and shared the Grok example it offered me _an_ _other A/B test_ :

![](/media/2026/01/Screenshot-2025-12-18-104058.png)

This one was interesting because it demonstrates another tendency of these framings: they**o****ffer a binary choice**. The real world in which we operate often doesn't offer such binary choices. This is what I refer to as "premature collapse" - the idea that when exploring a concept, topic, hypothesis, or area of thought, the last thing I want to do is _st_ _op looking early_. That leads to bad decision making. Similarly, I don't want to keep looking when there is a reason to make a choice - urgent action required, or no additional data obvious.

This led me to ask the question: why do we have this issue? What's the cause of it?
