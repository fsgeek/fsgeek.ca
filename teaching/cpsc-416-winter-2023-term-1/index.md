# CPSC 416 Winter 2023 Term 1

2023-06-10 · https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/

**Note****:** This is preliminary and will be changing over the next couple of weeks. The course starts September 5, 2023. The first in-person lecture is September 7, 2023.  
  
The first time that I taught this course ([Distributed Systems (CPSC 416)](https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=CPSC&course=416)) was January to April 2023 (UBC called it Winter 2022 Term 2). This course will differ from my prior offering, so while you are free to review the materials from my prior offering, **do no****t** expect that this offering will be the same.

First: this course is challenging. It is not _gratuitously_  challenging (e.g., I won’t make you suffer because _I  _suffered and think you somehow need to “pay your dues.”) My goal is to help you build a mental model for understanding the field but the field is _difficult_.

Distributed Systems are difficult because:

  * The _primary_  concern for this field is dealing with _failure_. Most of the courses you have taken teach you how to do things. Frequently “failure” means killing the program, rebooting the computer, fixing the bug in the code. In distributed systems we have to figure out how to make things work _in the presence of failure_.
  * A major challenge is that, unlike programs running on a single computer, there is limited [_fate sharing_.](https://en.wikipedia.org/wiki/Fate-sharing) In other words, parts of the system can keep running while other parts have failed. When different parts of the system do not have the same view of reality we lose the ability to know what the “correct” state of the system is.
  * We care about **persistent stat****e**. What this means is that, unlike ephemeral state where we can reboot to recover, any errors we make will be there **after we reboo****t**. That's why this version of the course is organized around the two primary ways we store persistent data: **database****s** and **file system****s**. They're really mostly the same, with different access interfaces. Even databases come in a variety of flavours, depending upon the access model for which they optimize (e.g., SQL, NoSQL, Graph, Vector, etc.)
  * We are primarily interested in just **tw****o** core problems:
    * How do we ensure that changes to two _different_ __ databases that are related to each other are done in a _consisten_ _t_ fashion. In other words, **if and only i****f** the bank machine gives you the cash you requested should your account balance be adjusted. For this we use **transactional consistenc****y** mechanisms.
    * How do we ensure that our databases can recover from the failure of a single copy (or instance) of the database. For this we use **consensus algorithm****s**.
  * We can easily develop working solutions that are not _practically usabl_ _e_ because they are too slow. The complications arise because we must both _optimiz_ _e_ our techniques and _preserv_ _e_ our correctness.



We cannot protect against all possible failures. What we do, instead, is identify failures we **d****o** want to protect against. Over time, we can expand on the failures we can handle. Of course, it turns out that _figuring out if you did it righ_ _t_ is **har****d**. It's like backups: the time you figure out they didn't work is when you need them. Failure at that point often means data loss. There are numerous articles that describe the impact of data loss on organizations. Here's a good quotation from one: "[[M]any companies don't understand what constitutes their most critical data and how to protect it.](https://www.businessdit.com/impact-of-data-loss-on-business/)"

Why do distributed systems matter? Because, while they are not 100% proof against all possible failures they can achieve high – but not absolute – reliability. Cloud compute vendors use the techniques we will discuss in this course to build “high availability systems.” Their failure model extends to protecting against regional level disasters.

During the term I will be updating the materials I have provided here as necessary:

  * [Instructional Team](https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/instructional-team-winter-2023-term-1/)
  * [Books](https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/books-winter-2023-term-1/)
  * [Syllabus](https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/syllabus-winter-2023-term-1/)
  * [Projects](https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/projects-winter-2023-term-1/)
  * [Exams](https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/exams-winter-2023-term-1/)
  * [Rubric](https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/rubric-w23t1/)
  * [Resources](https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/resources-winter-2023-term-2/)

- [Books (Winter 2023 Term 1)](https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/books-winter-2023-term-1/)
- [Exams (Winter 2023 Term 1)](https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/exams-winter-2023-term-1/)
- [Guest Lecture: Modeling & Formal Verification](https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/guest-lecture-modeling-formal-verification/)
- [Instructional Team (Winter 2023 Term 1)](https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/instructional-team-winter-2023-term-1/)
- [Projects (Winter 2023 Term 1)](https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/projects-winter-2023-term-1/)
- [Resources (Winter 2023 Term 1)](https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/resources-winter-2023-term-2/)
- [Rubric (Winter 2023 Term 1)](https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/rubric-w23t1/)
- [Syllabus (Winter 2023 Term 1)](https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/syllabus-winter-2023-term-1/)
