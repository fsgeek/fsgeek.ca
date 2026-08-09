# CPSC 416 (Winter 22 Term 2)

2022-12-23 · https://fsgeek.ca/teaching/cpsc-416-winter-22-term-2/

Starting in January 2023 I will be teaching the Computer Science Department's course in [Distributed Systems (CPSC 416)](https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=CPSC&course=416). This course has been taught by [Ivan Bestchastnikh ](https://www.cs.ubc.ca/~bestchai/)and it means I have an interesting challenge ahead in filling his shoes. The course I am teaching will be based upon his prior course, albeit with some modifications that I bring from my own experience as part of the instructional team for [Georgia Tech's CS 7210 course](https://omscs.gatech.edu/cs-7210-distributed-computing).

First: this course is challenging. It is not _gratuitously_ challenging (e.g., I won't make you suffer because _I_ suffered and think you somehow need to "pay your dues." My goal is to help you build a mental model for understanding the field but the field is _difficult_.

Distributed Systems are difficult because:

  * The _primary_ concern for this field is _failure_. Most of the courses you have taken teach you how to do things. Frequently "failure" means killing the program, rebooting the computer, fixing the bug in the code. In distributed systems we have to figure out how to make things work _in the presence of failure_.
  * A major challenge is that, unlike programs running on a single computer, there is limited [_fate sharing_.](https://en.wikipedia.org/wiki/Fate-sharing) In other words, parts of the system can keep running while other parts have failed. When different parts of the system do not have the same view of reality we lose the ability to know what the "correct" state of the system is.
  * The most common technique we use is to construct _consensus_ mechanisms - getting different independent parts of the system to agree on how to handle failures. The benefit of this is that _if we do it right_ we can project the aura of a single, coherent system capable of providing concrete guarantees to our "customers."



The dirty secret is that, in fact, we cannot guarantee the ability to handle _all possible failures_. A concrete example of this is the _[Two Generals Problem](https://en.wikipedia.org/wiki/Two_Generals%27_Problem)_. Thus, what we do in distributed systems is provide specific guarantees _within some defined set of failures_.

Why do distributed systems matter? Because, while they are not 100% proof against all possible failures they can achieve high - but not absolute - reliability. Cloud compute vendors use the techniques we will discuss in this course to build "high availability systems." Their failure model extends to protecting against regional level disasters.

Over the term I will be updating the materials I have provided here as necessary:

  * [Syllabus](https://fsgeek.ca/cpsc-416-winter-22-term-2/cpsc-416-syllabus/)
  * [Projects](https://fsgeek.ca/cpsc-416-winter-22-term-2/cpsc-416-winter-2022-term-2-projects/)
  * [Extra Credit](https://fsgeek.ca/cpsc-416-winter-22-term-2/cpsc-416-winter-2022-term-2-extra-credit/)
  * [Exams](https://fsgeek.ca/cpsc-416-winter-22-term-2/cpsc-416-winter-2022-term-2-exams/)
  * [Rubric](https://fsgeek.ca/cpsc-416-winter-22-term-2/cpsc-416-winter-2022-term-2-rubric/)
  * [Resources ](https://fsgeek.ca/cpsc-416-winter-22-term-2/cpsc-416-winter-2022-term-2-resources/)(Canvas, Discussion (TBD), Discord, Twitch, TAs, Office Hours)
  * [Lectures ](https://fsgeek.ca/cpsc-416-winter-22-term-2/lectures/)(Slides, Videos - if available)

- [CPSC 416 (Winter 2022 Term 2): Class Grading Rubric](https://fsgeek.ca/teaching/cpsc-416-winter-22-term-2/cpsc-416-winter-2022-term-2-rubric/)
- [CPSC 416 (Winter 2022 Term 2): Exams](https://fsgeek.ca/teaching/cpsc-416-winter-22-term-2/cpsc-416-winter-2022-term-2-exams/)
- [CPSC 416 (Winter 2022 Term 2): Extra Credit](https://fsgeek.ca/teaching/cpsc-416-winter-22-term-2/cpsc-416-winter-2022-term-2-extra-credit/)
- [CPSC 416 (Winter 2022 Term 2): Lectures](https://fsgeek.ca/teaching/cpsc-416-winter-22-term-2/lectures/)
- [CPSC 416 (Winter 2022 Term 2): Projects](https://fsgeek.ca/teaching/cpsc-416-winter-22-term-2/cpsc-416-winter-2022-term-2-projects/)
- [CPSC 416 (Winter 2022 Term 2): Resources](https://fsgeek.ca/teaching/cpsc-416-winter-22-term-2/cpsc-416-winter-2022-term-2-resources/)
- [CPSC 416 (Winter 2022 Term 2): Syllabus](https://fsgeek.ca/teaching/cpsc-416-winter-22-term-2/cpsc-416-syllabus/)
