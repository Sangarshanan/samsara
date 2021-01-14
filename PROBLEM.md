### Async Scheduler.

It has gotten to a point where I am writing problems for myself

You are playing a game with 3 people in a universe where you are omniscient
i.e you take negligible time to make a move

- Person A takes 4 seconds to respond to your move (pov: you are normal)
- Person B takes 3 second to respond (clever chap)
- Person C takes 6 seconds to respond (Unirinonically uses tiktok)

The Game is infinite unless a player withdraws from the game and
here is what happens

Initially `A=0 B=0 C=0` and `time=0`

So everyone can play and we are follow a sorted order

- You play with Person A and have to wait for 3 seconds to play with A again

`B=0 C=0 A=3 time=1`

- A should wait till time is 3 to be ready again, so we run B which will run
  after current_time + 3

`C=0 A=3 B=4 time=2`

- C now runs adding itself to the queue with a `wait-time` of 6 seconds

`A=4 B=4 C=8 time=3`

And so on ....

we push the task that need to run to the ready queue, and tasks that need to sleep is inside a priority waiting queue when the elements at the top of the priority queue is ready or its time_to_run = current_time we pop it into the ready queue. Ready queue is just a list of functions running one by one

Issues ....

Tasks pending in the ready queue migth not be tended to immediately so we might be lagging in executing tasks
