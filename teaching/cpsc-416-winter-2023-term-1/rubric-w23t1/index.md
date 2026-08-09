# Rubric (Winter 2023 Term 1)

2023-08-17 · https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/rubric-w23t1/

**Learning Objective****s** : There are a handful of learning objectives for this course.

  * Understanding of persistent storage (databases and file systems, primarily) with particular emphasis on the most common core storage paradigm, the "key value store."
  * Understanding of distributed transaction processing. This is the idea that we need to change persistent information in two different databases when the data being changed is related. Thus, to ensure correctness, you need to coordinate the change so it happens atomically.
  * Understanding of distributed consensus. This is the idea that we need to _replicat_ _e_ our data in order to protect against certain types of failures, including network failures, storage failures, power failures, etc.
  * Understanding the critical tools we use for _implementin_ _g_ systems that provide both distributed transactions and distributed consensus. Key to this is the concept of a _journa_ _l_ or a _lo_ _g_. There are other aspects of this, including state machines, snapshots, clocks (Lamport, vector, and matrix,) which we use for building these systems.
  * Learning that _desig_ _n_ is an integral part of this process. Robust distributed systems are built on the base of a well-considered software architecture, a design that addresses key issues for the specific system being constructed, and an implementation that can be validated and includes detailed instrumentation to ascertain the root cause of failures.



**Evaluation** : The primary student concern usually seems to be focused on grade maximization; this is a constant struggle in education, because in general no one will care about your grades six months after you graduate. They _wil_ _l_ care about your ability to reliably solve problems and there are few more difficult problems than those we face in distributed systems. However, we do have to have some sort of assessment, so here is what I will be using this term:

**Assessment Description**| **Evaluation Criteria**| **Grade Contribution**  
---|---|---  
Post-class Self-assessment| Did you complete it?| 10  
Design Project 1| Design Document  
Peer Feedback  
Implementation Report  
Peer Feedback| 15  
Design Project 2| Design Document  
Peer Feedback  
Implementation Report  
Peer Feedback| 15  
Design Project 3| Design Document  
Peer Feedback  
Implementation Report  
Peer Feedback| 15  
Capstone Project| Design Document  
Implementation  
Status Reports  
Final Report  
Final Presentation| 25  
Final Exam| Multi-question exam| 20  
**Course Grading Scheme**

**Self-Assessmen****t** will be a quiz, on Canvas, that you take when you want. It will consist of a handful of questions about the reading for the individual lecture. Note that nobody will be grading you on this - it's a **self-assessmen****t** tool, so that you can determine how you did in understanding the material. The quiz will open after the lecture is done and close when the next lecture begins. The idea here then is to encourage you to keep up with the material. The one exception here is that while registration is open the self-assessment quiz will be open (it will be set up for late submission, but you won't be penalized for late submission.) If you just want to click some buttons and get a score, you can do that, I won't care.

**Design Projects** will consist of three different projects. Each project will involve one of the non-trivial DSLabs projects but the emphasis will be on learning how to design solutions to distributed systems. In the first part, you will be asked to write a design for the project. The _goa_ _l_ of this design is for you to describe your vision of how to implement the project. You will not be asked to implement your own design. Once you have submitted your design, you will then be asked to review the designs of three other students and provide feedback. A suggested rubric will be provided for your review. Once you are done, you will select one of the three designs that you reviewed and attempt to implement it. You will then submit your code, via Gradescope, and your implementation report, reflecting upon the strengths and weaknesses of the design. Finally, you will be asked to peer review three other students implementation reports and provide feedback on them. The learning objective is to help you understand good design as seen through the lens of distributed systems. **All designs will be shared with the clas****s**. You will not be expected to include your name on the document, and you need not tell people which design you implemented. There are three of these so you have time to reinforce your skills in designing solutions to increasingly complex projects, reflect upon what works, and then sharpen your skills by using them again. Note that _gradin_ _g_ for these is strictly based upon whether or not you submitted something. Your code doesn't need to run. Your report could be as minimal as you would like.

The **Capstone Project** will be your **own** design and implementation of your own project. The specific options will be discussed later, but the range of options will relate to distributed systems: key value stores, distributed transactions, log/journal systems, consensus systems, replicated data types (CRDTs or MRDTs,) etc. Unlike the other assessments, **these will be reviewed by the instructional team** and awarded a grade. Note that your work product will be shared (again, you can remain anonymous) with the rest of the class. You may work in groups for a capstone project, with a limit of no more than 5 people in a group, but you are not **required** to work in a group if you prefer to work solo. Your final submission will consist of your (revised) design, test methodology, code, and a recorded presentation of the system that you have built. Note thereare no restrictions on the programming language or system that you use. Details of the rubric for the capstone will be provided later in the term. 

The **Final Exam** will be a proctored, timed, final examination consisting of multiple choice and true/false questions. The questions will be drawn from the course concepts and materials. 

My goal is to try and make this the most useful course you take in your undergraduate program, both because it combines _theor_ _y_ with _practic_ _e_ as well as helps you develop skills you will find are important afterward. Thus, the difficulty of the course will, hopefully, justify the benefits you receive from it.
