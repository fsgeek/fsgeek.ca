# Guest Lecture: Modeling & Formal Verification

2023-09-14 · https://fsgeek.ca/teaching/cpsc-416-winter-2023-term-1/guest-lecture-modeling-formal-verification/

Finn Hackett

Here is a video that Finn has put together about the topic and this will drive his discussion on Tuesday, September 19, 2023.

https://www.youtube.com/watch?v=NylSI56JPvc 

Finn Hackett: Modeling and Formal Verification of Distributed Systems

The materials described here relate to Finn's guest lecture. While you are not required to have read all of this material, you may wish to review it before and/or after the lecture to expand on your knowledge and understanding of the techniques he will discuss in class.

## Fuzzing and Random Testing

QuickCheck: <https://doi.org/10.1145/351240.351266>   
AFL: <https://lcamtuf.coredump.cx/afl/>

## Exploring Distributed Systems Implementations

Coyote <https://doi.org/10.1145/3472883.3486983> MODIST <https://www.usenix.org/legacy/event/nsdi09/tech/full_papers/yang/yang.pdf>

## Modeling Languages

StateRight (sorta) <https://docs.rs/stateright/latest/stateright/>   
Ivy <https://doi.org/10.1007/978-3-030-53291-8_12>   
PGo <https://doi.org/10.1145/3575693.3575695>   
Dafny <https://doi.org/10.1007/978-3-642-17511-4_20>  
IronFleet <https://doi.org/10.1145/2815400.2815428>

## More Abstract Modeling Languages

  * TLA+ 
    * <https://doi.org/10.1007/3-540-48153-2_6>
    * <https://doi.org/10.1007/978-3-662-43652-3_3>
    * <https://doi.org/10.1109/ICSE-SEIP58684.2023.00006>
  * Alloy 
    * <https://doi.org/10.1109/ICECCS.2005.48>
    * <https://doi.org/10.1109/CSNT.2011.141>



## Proof systems (Based on Coq)

  * Coq: <https://coq.inria.fr/>
  * Verdi <https://doi.org/10.1145/2737924.2737958>
  * Disel <https://doi.org/10.1145/3158116>



## The Dark Side

Bugs that happen anyway. <https://doi.org/10.1145/3064176.3064183>

## Stateright - Rust

A library for model checking systems, with an emphasis on distributed systems: [stateright - Rust](https://docs.rs/stateright/latest/stateright/)
