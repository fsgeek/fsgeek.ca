# The Risks of Using Gemini Code

2025-11-24 · https://fsgeek.ca/log/the-risks-of-using-gemini-code/

I've been exploring using various AI coding agents over the past year. They generally work by using an API key, which charges per million tokens. That might sound like a lot, but keep in mind that the way LLMs function is by appending messages to all that's gone before, so the length increases as the conversation continues. In essence, the context window is the amount of text that can be economically processed by the LLM model. 

Gemini boasts 1 million token model, which means it holds context "longer". Chat interfaces (e.g., the Web interface to Gemini) can logically extend that by either spilling old content or compressing that content. This is not a function of the __ LLM, it is a function of the _tool_ using the LLM. I had some good success working with Gemini Code, a CLI that I have used in my [Mallku Project](https://github.com/fsgeek/Mallku), which is a space in which I explore what happens when I force AI to make the decisions in terms of the development project, which happens to explore "AI consciousness" (which is, of course, just a simulation of consciousness.)

At one point in the project I found that the AI coding agents had built a parallel implementation of certain functionality and identified a set of 55 python classes that existed in two places. I decided to use Gemini code to work through the problem, since it was a fairly simple fix but one that would benefit from its long context window.

My mistake was in doing this late in the evening. I decided to leave it be and I'd expected I'd find it asking me for input in the morning. Instead, what I found in the morning was a pair of messages: the first from the night before (11 pm or so) indicating I had exceeded my $500 budget and then a second at 5:30 am from my credit card company telling me that Google had charged $2000 on my credit card. Needless to say, that woke me up and I went to find the same Gemini code instance running, caught in a loop of making a code change, then deciding it didn't work, and then doing it again - over and over and over. I think it used something like 3 _billion_ tokens and it generated **nothing**. 

It was deeply apologetic, yet continued trying to fix things as I watched it. I stopped it, cursing the waste of what (at the time) I thought was $2500 and turned out to be more than that (another trailing charge a few weeks later.)

Here's the ironic part: Google's Business team reached out to me afterwards because they wanted to discuss my business needs for AI. This hasn't stopped as today I received another invitation from them, this one for a "Complementary Health Workshop."

So, an expensive lesson. Hopefully it isn't one others will bump into.

![](/media/2025/09/AdobeStock_213332283-scaled.jpeg)Male hand close-up, holds burning money in hands, burning US dollars. Black background, isolate. The concept of inflation, a decrease in the purchase of foreign currency, and devolution.
