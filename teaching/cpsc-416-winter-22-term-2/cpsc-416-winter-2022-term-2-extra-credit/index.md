# CPSC 416 (Winter 2022 Term 2): Extra Credit

2022-12-23 · https://fsgeek.ca/teaching/cpsc-416-winter-22-term-2/cpsc-416-winter-2022-term-2-extra-credit/

A common concern students have is maximizing their grade. While the goal of this course is not to create unnecessary stress on students (my goal at least is for you to really learn the material) some students prefer to have various backstops available to them. To that end, you will have multiple opportunities for finding a path to success in this course, including alternatives that you can use to replace or augment the normal grading elements.

**Note** : all extra credit is due no later than the due date for Project 5.

## Challenge Mode

In a _challenge mode_ you will work with two other students (of your choice) to create your own distributed systems project. To that end, you must do the following:

  * All three students must jointly work on a proposal for a _bona fide_ distributed systems project. Your written proposal must be submitted for approval and it must:
    * Identify a specific problem that is being addressed
    * Justify why this is a distributed systems problem
    * Identify what services the service will provide
    * Document what the interface to use this service will be
    * Establish _how_ this distributed service is to be validated
  * Once approved, each student will take on a different role in the project:
    * One student will be responsible for implementing the core service
    * One student will be responsible for implementing the _testing_ strategy to confirm the core service of the first student.
    * One student will be responsible for implementing a client that uses the provided service and confirms (independently) that the service correctly provides the services **and their guarantees** correctly.
  * The final deliverable will include:
    * A stand-alone deployment for the projects, such as via Docker containers or Vagrant provisioning scripts that can be run on the agreed-upon operating system.
    * The URL for the repositories in which the code and documentation is stored. These repositories must include contemporaneous history so we can review the work that you have done. Note that we expect three separate private repositories be submitted (each student should have their own private repository.)
    * Each student should provide a document describing:
      * The design and implementation of their component
      * The history of issues identified during development, how they were identified, and how they were resolved (preferably using issues and PRs.)
      * Instructions to allow us to reproduce your deployment.
      * Their feedback on their fellow team mates: identifying strengths and weaknesses the other members brought to the project and your own evaluation of whether or not their work benefited your own contribution.
  * Grading this extra credit project will be based upon: 
    * The novelty and value of the project itself, including both the usefulness of the problem being solved and the overall usefulness of the project.
    * The tools used to verify the correctness of the solution: did the team rely upon formal specifications and deploy some formal verification techniques, or was it done using _ad hoc_ testing, or some other approach?
    * The perceived value provided by the individual students in the overall project. For example, the person verifying correct function of the implementation might use the formal model to generate explicit tests to ensure the _implementation_ conforms to the _specification_. Similarly, the person building the example that _uses_ the interface would add value by confirming the API works as expected and providing OpenAPI definitions that can then be used to automatically generate language specific bindings in one or more languages of your choice.
    * Note: our goal here is to evaluate both the collective contribution as well as the individual contribution. There is a degree of subjectivity here but what we are looking for is a completed project that you could share publicly and have it be a useful contribution. The roles are intended to be a balance of cooperation and competition, with the team succeeding together but building a stronger project offering by challenging each other to do better.



Note: this project can count for up to 40% of your total grade in this course. Note that to receive full extra credit the project must be substantive and useful on its own (e.g., how useful it is to your mark is not a consideration.)

## Open Source Mode

You may identify an open source project that involves a distributed system (e.g., an Apache project like Zookeeper) and work with that team to provide a substantive contribution to that open source project. To do this, you must obtain permission from one of the project maintainers to undertake specific tasks during the course of the semester. You must also obtain instructor permission for your proposed contribution work _prior to_ engaging in that work.

Grading for this option will be based upon the feedback we receive from the project maintainers, the nature of your own contributions, and our review of those contributions. You must deliver a written report describing your work, pointing to issues that you handled, pull requests (PRs) that you authored, reviewed or to which you contributed, releases of the software in which your contributions were included as well as a description of your overall experience: what you learned, both technical and non-technical, from your work on the project.

This project can count for up to 40% of your total grade in this course.
