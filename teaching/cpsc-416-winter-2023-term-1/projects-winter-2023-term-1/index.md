# Projects (Winter 2023 Term 1)

2023-08-17 · https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/projects-winter-2023-term-1/

There will be **fou****r** projects this term. Three of these projects are what I call _design project_ _s_ because they emphasize the planning and design of a potential solution to a DSLabs project. You will implement the design, but because the implementation is used as a tool to improve your design understanding and hone your skills of critical review and self-reflection **your code is not directly grade****d**. You will submit your code, but as long as it compiles, you will receive credit for your submission. 

The fourth project is the **Capstone Projec****t**. This is your opportunity to use your now enhanced design skills to build a system that incorporates concepts of distributed systems into your software solution. 

I'll describe each of these in greater detail below.

## Design Projects (3)

There will be three design projects:

  * Primary/Backup Design Project - this is based upon the DSLabs first substantive project, which is to implement a system with three functional components to provide reliable replicated data services. **This project will be a solo projec****t**. 
  * Paxos Design Project - this is based on the DSLabs second substantive project, which is to implement a system with multiple functional components that implement a specific optimized variant of the Paxos protocol, as described in the **[PMM](https://paxos.systems/)****[C](https://paxos.systems/)** paper. Interestingly enough, while this lab focuses on Paxos, in the past students have implemented other similar protocols (e.g., Raft) within that framework. **This project may be done in a group of up to three student****s**. Note: the default will be that you do it on your own unless you declare your group to us by the deadline.
  * Sharded Key-Value Store Project - this is based on the final DSLabs project, which is to implement a system using two-phase commit (2PC) transactions and shard rebalancing, combined with a Paxos implementation for replication of the individual shard groups. Two relevant papers you will want to read as part of this project are [Chord](https://pdos.csail.mit.edu/papers/chord:sigcomm01/chord_sigcomm.pdf) and [Dynamo](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf). **This project may be done in a group of up to four student****s _._** Note: the default will be that you do it on your own unless you declare your group to us by the deadline.



You have several deliverables for these projects:

  * You will provide your best effort design of a solution. In doing so, you need to think about the components, their role in the project, and what the issues are that need to be addressed in the implementation. **Grading for this is just for submissio****n**. The goal here is to help you learn better design skills.
  * You will be given **thre****e** designs by other students to review. You will then review those designs, providing feedback on them. **Grading for this is just for submissio****n**. The goal here is to help you provide critical review. By _critical revie_ _w_ I mean "feedback that strives to improve the original design through actionable suggestions." None of your feedback should be _ad hominem_ or offensive.
  * You will choose **on****e** of the three designs and implement it using the DSLabs framework on Gradescope. **Grading for this is just for submissio****n**. The purpose of the code isn't to make the best possible implementation (or one that gets 100% on the grader) and instead is focused on learning what issues you might have overlooked in your own review of the design, as well as additional flaws in the design.
  * You will write an **implementation repor****t** that builds on your previous review by expanding that original design. The purpose of this is not to criticize the original author, but to reflect upon the issues that _yo_ _u_ may have overlooked and should demonstrate your abilities of self-reflection to think about how you can improve your future design work. **Grading for this is just for submissio****n**.
  * You will be asked to review **thre****e** implementation reports by other students. You will review those reports and provide feedback on them. **Grading is just for submissio****n**. The goal here is for you to see how others enhanced their understanding through self-reflection. Since everyone is designing, implementing, and reflecting on the **sam****e** project, the goal is to help you increase your depth of understanding.



Note that there's no explicit grade or review of your work. However, the instructional team will attempt to identify a handful of exemplary reports to showcase.

## Capstone Project

In the Capstone Project, _yo_ _u_ get to utilize your design skills to demonstrate your understanding of the distributed systems principles we will have been discussing in the class. **This project will be graded****.** **You may work in a team of up to five****.** Unless you declare your group up front we will expect you to provide an individual submission.

There are five distinct deliverables as part of your Capstone Project:

  * Design Document - this is where you describe your project: what problem is it solving, what are the goals for your problem, what is the architecture of your solution, what design did you choose to guide your implementation of your project.
  * Implementation - this is your implementation. It is in the language of your choice, with the tests of your choice. Your code will be submitted via GitHub.
  * Status Reports - each week throughout the project, you will be responsible for submitting a written status report. **This is an individual activit****y** ; that is, each of you must submit a status report.
  * Final Report - This will be your final document in which you review what you did and how it compares to your original design. Our primary review here will be to ensure you demonstrate understanding and beneficial self-reflection, so we will be looking to see how effective you are at identifying the strengths and weaknesses of your work.
  * Final Presentation - This will be a video presentation demonstrating your project. Criteria for grading will be the quality of the presentation, and clarity of your goals.



Note that for **AL****L** projects and reports, the material will be included in a library that is visible to other students in the class. **Do not include personally identifiable information in your submission if you wish to remain anonymous****.**

The instructional team will highlight the capstone projects we thought were the best overall by the end of the term. Our goal here is to help those taking the class see the range of work that others have done and (hopefully) learn from the experience. In this way you will leave the course with a solid understanding of distributed systems _an_ _d_ good design.
