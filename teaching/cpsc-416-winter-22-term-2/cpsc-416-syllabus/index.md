# CPSC 416 (Winter 2022 Term 2): Syllabus

2022-12-23 · https://fsgeek.ca/teaching/cpsc-416-winter-22-term-2/cpsc-416-syllabus/

CPSC 416 Winter 2022 Term 2, Department of Computer Science  
---  
Delivery: In Person, Tuesday and Thursday 8:00-9:30 am (Location TBA)  
Course Dates: January 10, 2023 to April 13, 2023  
  
## Instructor Information

Tony Mason| Office:  
---|---  
| E-mail: fsgeek@cs.ubc.ca  
In-person Office Hours by Appointment| Teaching Assistants: (TBA)  
Online Office Hours:| Tuesday @ 13:00-14:00 via Zoom  
| Thursday @ 16:00-17:00 on Discord  
  
## General Course Information

### Description

_A distributed system is one in which the failure of a computer you didn't even know existed can render your own computer unusable._ \- Leslie Lamport (2013 ACM Turing Machine Award Winner)

This course covers fundamental concepts in distributed computing and how systems can be designed to use those concepts to enable distributed applications. Course objectives are: in-depth understanding of distributed computing concepts and practical techniques, how to build distributed systems using hands-on labs as well as optional projects, as well as an understanding of the current state of the art for several aspects of building distributed systems (Machine Learning, Data Analysis, and Byzantine Fault Tolerance, for example.)

Distributed systems provide substantial benefits that justify their use _despite_ their complexity. Properly executed distributed system implementations are more fault tolerant since there are fewer (or no) single points of failure. In addition, distributed systems provide a highly useful technique for providing scalability, which in turn can improve their ability to handle more work - including brief periods of high demand work. Techniques such as caching provide strong benefits but introduce additional complexities due to the need to manage distributed state. 

Distributed systems have complex failure modes that must be handled properly in order to provide the benefits of those same systems. Thus, much of this material is about handling failures in a fashion that permits forward progress, which is often different than typical programming involves.

The tentative topics are listed in the schedule below. For the most part this will be a lecture-style course. However, distributed system concepts are notoriously challenging to internalize without first-hand experience. The emphasis of this course, therefore, will be on **building** distributed system prototypes, small and large.

### Prerequisites

CPSC 317 (Networks)

CPSC 313 (Computer Hardware and Operating Systems)

### Textbooks

**There are no required textbooks for this course. The following books are optional and may help your understanding of the materials.**

  1. TBD
  2. TBD



### Communications

TBA

### Course Goals and Learning Objectives

## Schedule

Note that this schedule is a work in progress and **is subject to change**.

Date| Topics| Deliverables  
---|---|---  
January 10, 2023| Introduction: Failure  
Readings: TBA| Course Collaboration Policy Quiz Due Monday January 16, 2023.  
January 12, 2023| Networks and Remote Procedure Calls|   
January 17, 2023| Clocks, Time, and Event Ordering.|   
January 19, 2023| Distributed State| Project 1: Intro to DS Labs due Monday January 16, 2023.  
January 23, 2023| Last Day to Drop|   
January 24, 2023| Achieving Consensus|   
January 26, 2023| Replication|   
January 31, 2023| Fault-Tolerance|   
February 2, 2023| Transactions| Project 2: Client-server due Sunday February 5, 2023.  
February 7, 2023| Distributed Logging|   
February 9, 2023| Quorum Replication|   
February 14, 2023| PAXOS| Project 3: Primary-backup replication Due Monday February 13, 2023  
February 16, 2023| Viewstamped Replication|   
February 21, 2023| Reading Break|   
February 23, 2023| Reading Break|   
February 28, 2023| Raft|   
March 2, 2023| PMMC Walk-through|   
March 7, 2023| | Last Day to Withdraw (Extended)  
March 7, 2023| Introduction to Formal Verification (TLA+)|   
March 9, 2023| Consistency and Geo-Distributed Data Stores|   
March 14, 2023| Guest Lecture|   
March 16, 2023| Project 5 Walk-through|   
March 21, 2023| Peer-to-Peer Systems and Mobility| Project 4: Paxos Due Monday, March 20, 2023  
March 23, 2023| Distributed Data Analytics|   
March 28, 2023| Datacenter-based Distributed Computing|   
March 30, 2023| Distributed Machine Learning|   
April 4, 2023| Byzantine Fault Tolerance and Blockchain|   
April 6, 2023| Guest Lecture|   
April 11, 2023| Guest Lecture|   
April 13, 2023| TBA| Project 5: Sharded Fault-Tolerant Key-Value Store due Thursday April 13, 2023.  
TBD| Final Exam|   
  
My goal is to have several guest speakers during the term. I have put time for four such guest lectures at the end of the schedule and will adjust the schedule as I am able to confirm specific dates with guests. If I am not able to get four guest speakers I will provide supplementary presentations in lieu of those guest speakers.
