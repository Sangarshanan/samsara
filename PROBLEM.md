### Scheduler

Stupid scheduler with queues

----

It has gotten to a point where I am writing problems for myself

You are playing a game with 3 people in a universe where you are omniscient
i.e you take negligible time to make a move

- Person A takes 4 seconds to respond to your move (pov: you are normal)
- Person B takes 3 seconds to respond (clever chap)
- Person C takes 6 seconds to respond (Unirinonically uses TikTok)

The Game is infinite unless a player withdraws from the game and
here is what happens

Initially `A=0 B=0 C=0` and `time=0`

So everyone can play and we are following a sorted order

- You play with Person A and have to wait for 3 seconds to play with A again

`B=0 C=0 A=3 time=1`

- A should wait till the time is 3 to be ready again, so we run B which will run
  after current_time + 3

`C=0 A=3 B=4 time=2`

- C now runs adding itself to the queue with a `wait-time` of 6 seconds

`A=4 B=4 C=8 time=3`

And so on ....

we push the task that needs to run to the ready queue, and tasks that need to sleep are inside a priority queue when the elements at the top of the priority queue are ready or it's time_to_run = current_time we pop it into the ready queue. The ready queue is just a list of functions running one by one

**Footnotes eh**

Tasks pending in the ready queue might not be tended to immediately so we might be lagging in executing tasks

Persist the queues with Redis !?

And maybe instead of running the tasks I can just act as a message bus !?

Based on black magic as seen on https://www.youtube.com/watch?v=Y4Gt3Xjd7G8
