---
title: "Backtracking algorithms: experiment, inspect and adapt"
date: 2023-06-13
draft: false
---

In this post I tell the story of a beautiful **picture** which represents an interesting mathematical **problem** whose algorithmic **solution** has some **analogy** to the agile way of making progress.

## The picture

My former highschool math teacher [Hansruedi Widmer](https://www.linkedin.com/in/hansruediwidmer/) ("retired as a teacher, not as a mathematician") daily posts mathematical puzzles, bits of history or just "fun facts" on twitter. On March 1{{< super "st" >}}, 2022, which was the 60{{< super "th" >}} day of the year, he tweeted the following (translation from German is mine): 

> As it is day 60: The numbers from 1 to 60 can be paired in such a way that the sum of every pair is one of the sqare numbers 3{{< super "2" >}}, 6{{< super "2" >}}, 7{{< super "2" >}}, 8{{< super "2" >}}, 9{{< super "2" >}}.
>
> ![rainbow squares](/images/blog/backtracking-algorithms/rainbow_squares.jpg)
> 
> — <cite>[tweet](https://twitter.com/HansruediWidmer/status/1498540361827954689) by [Hansruedi Widmer](https://twitter.com/HansruediWidmer) on March 1{{< super "st" >}}, 2022</cite>

I found (and still find) this drawing (figure 1) very beautiful, like a piece of art, and I wanted to know more about the underlying mathematical problem:
1. Is there more than one solution which satisfies the given constraints?
2. And if yes, how can they be found?

## The problem

I asked Hansruedi, but all he could tell me without further investigation was that 93 pairs could be formed with the numbers from 1 to 60 whose sum was an element of the set {9, 36, 49, 64, 81}. The solution was to choose 30 out of these 93 pairs such that every number from 1 to 60 was included exactly once. 

The 93 pairs can easily be found by iterating over all numbers i from 1 to 60 and checking for every number j between (i + 1) and 60 whether the sum of i and j is an element of the above set of square numbers:

- 1 can be paired with 8 (to yield 9), with 35 (to yield 36) and with 48 (to yield 49)
- 2 can be paired with 7 (to yield 9), with 34 (to yield 36) and with 47 (to yield 49)
- 3 can be paired with 6 (to yield 9), with 33 (to yield 36) and with 46 (to yield 49)
- 4 can be paired with 5 (to yield 9), with 32 (to yield 36), with 45 (to yield 49) and with 60 (to yield 64)
- 5 can be paired with 31 (to yield 36), with 44 (to yield 49) and with 59 (to yield 64)
- and so on

Alternatively, of course, the pairs can be found the inverse way, by iterating over all numbers i from 60 down to 1 and checking for every number j between (i - 1) and 1 whether the sum of i and j is an element of the target set.

A table with all pairs sorted in different ways can be found [here](../../materials/blog/backtracking-algorithms/table-pairs).

The difficult part is to find 30 pairs out of these 93 which satisfy the additional constraint that every number from 1 to 60 is included exactly once.

As Hansruedy had not investigated this any further, I had to give it a try myself.

## The solution 

### 1{{< super "st" >}} attempt: a dead end

Maybe pushed a bit into this direction by Hansruedi's very mathematical problem description ("Choose 30 out of these 93 pairs such that ...") I tried exactly that: Somehow generate all possible subsets of 30 pairs out of the whole set of 93 pairs and then apply the additional constraints. None of my experiments worked, and if you look at the sheer dimension of the problem, it becomes obvious that none of them could work, at least not with today's computers:

The number of possible ways to choose 30 pairs out of 93 is 

({{< super "93" >}}{{< sub "30" >}}) = 93! / (30! x (93-30)!) = 93! / (30! x 63!)

which is roughly 2.200 x 10{{< super "24" >}}, i.e. 2.2 septillion, which is an enormous number (22 followed by 23 zeroes). 

A web search led me to the [paper from the Mathematical Association of America( MAA)](https://www.maa.org/sites/default/files/pdf/awards/college.math.j.46.4.264.pdf) from which the above picture must have been taken. I learned that the problem is called "rainbow squares" because of the way in which the pairs with equal sum are marked with the same color, or simply "rainbow pairs" for the more general case where the sums are subject to some constraint different from being square numbers (e.g. polynomials or Fibonacci numbers).

I also learned from this paper that the number of solutions for the numbers from 1 to 60 where the sum is constraint to be *any* square, i.e. {4, 9, 16, 25, 36, 49, 64, 81, 100} is 4,366,714! But how many solutions would there be with the narrower constraint set {9, 36, 49, 64, 81}? And how could they be found?

This was all valuable and interesting background information but did not explain *how* to find the solutions. 

### 2{{< super "nd" >}} attempt: a slow road

As the purely mathematical approach had not worked, I tried to think about the problem more *procedurally*: Not in terms of selecting pairs but in terms of drawing the beautful picture shown in figure 1: If I had a sheet of paper with the circle of numbers from 1 to 60 and five colored pencicls, how would I go about drawing such a picture?

Starting with the empty "circle" (figure 2):

![backtracking 1: empty circle](/images/blog/backtracking-algorithms/backtracking_1_empty.png)

I would begin with the lowest number - 1 - and *tentatively* mark a pair for it. I could use any of the three possible pairs shown in the [reference table](../../materials/blog/backtracking-algorithms/table-pairs), so to do it sistematically, I would just choose the first one from the second column in the table. This is the lowest pairing, which is 8 (figure 3):

![backtracking 2: 1 pair](/images/blog/backtracking-algorithms/backtracking_2_1_pair.png)

I would do the same for the next three numbers 2 to 4 (figure 4):

![backtracking 3: 4 pairs](/images/blog/backtracking-algorithms/backtracking_3_4_pairs.png)

As the numbers 5 to 8 are already paired, I would continue with 9 to 17 (figure 5):

![backtracking 4: 13 pairs](/images/blog/backtracking-algorithms/backtracking_4_13_pairs.png)

And 18 (figure 6):

![backtracking 5: 14 pairs](/images/blog/backtracking-algorithms/backtracking_5_14_pairs.png)

Again, as the numbers 19 to 27 are already paired, I would continue with 28 to 30 (figure 7):

![backtracking 6: 17 pairs](/images/blog/backtracking-algorithms/backtracking_6_17_pairs.png)

And then all the numbers from 32 to 40 which have not already been paired (figure 8):

![backtracking 7: 23 pairs](/images/blog/backtracking-algorithms/backtracking_7_23_pairs.png)

And as numbers 41 to 44 have already been paired, I would now like to continue wth 45, but there is a problem: As can be seen in the [reference table](../../materials/blog/backtracking-algorithms/table-pairs), there is no more pairing possible for 45. What to do now?

As I have said at the beginning, I have just marked the pairs *tentatively*, so I can now trace back and erase the latest pair marked ([40 - 41]) (figure 9): 

![backtracking 8: 22 pairs](/images/blog/backtracking-algorithms/backtracking_8_22_pairs.png)

Unfortunately, this is not enough because at this point I have no alternative for number 40 than the pair 41. So I have to trace further back until I arrive at the number for which there is an alternative path forward. This is number 30 (figure 10):

![backtracking 9: 22 pairs](/images/blog/backtracking-algorithms/backtracking_9_16_pairs.png)

Instead of pairing 30 with 34, I now pair it with 51 (figure 11):

![backtracking 10: 17 pairs](/images/blog/backtracking-algorithms/backtracking_10_17_pairs.png)

And continue forward from there until I run into another dead end, which happens to be at number 45 again (figure 12):

![backtracking 10: 17 pairs](/images/blog/backtracking-algorithms/backtracking_11_24_pairs.png)

So I have to trace back to 30 again, but as there is no third alternative besides 34 and 51 for 30, I have to trace yet another step back to 29 and pair it with 52 instead of 35 (figure 13):

![backtracking 12: 16 pairs](/images/blog/backtracking-algorithms/backtracking_12_16_pairs.png)

And from here I can move forward again. And back and forth and back and forth again... And if there is a solution, I will eventually find it. Not in my lifetime, though, as in this concrete example it will take almost 50,000,000 steps to find the first solution.

Millions of repetions of the same small, simple step? Sounds like the perfect problem to write a program for!

This type of algorithm is called [backtracking algorithm](https://en.wikipedia.org/wiki/Backtracking) as I remembered from the time I had once implemented a Sudoku solver in Ruby some 20 years earlier. [Sudoku](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms) is a very typical application of backtracking, as is the [Eight Queens Problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle) with which the algorithm is usually illustrated in textbooks. But the rainbow squares problem is equally well suited to illustrate backtracking, as I hope to have shown above.

Test [link to a python program](/files/blog/backtracking-algorithms/askpython.py)

[link to my program here!!]

I implemented the algorithm in python. The first version worked exactly as shown in the figures above. It found 5294 solutions but ran more than an hour. That was disappointing and unexpected, because for an average Sudoku, a backtracking algorithm finds the solutions in less than a second. Analysis showed that the algorithm had performed 5.2 billion tentative steps whereas an average Sudoku only requires something between 10,000 and one million steps. The reason is that Sudokus are very highly constraint puzzles where many alternatives can be excluded early on.

### 3{{< super "rd" >}} attempt: fast backward

How could the algorithm for the rainbow squares be improved? I found a hint in the [AMM paper](https://www.maa.org/sites/default/files/pdf/awards/college.math.j.46.4.264.pdf) mentioned above where for a simpler problem (numbers only from 1 to 18, not to 60) they ask whether it would be better to start with small pairs or large ones and answer that "The latter is in fact more efficient since it presents fewer choices early on." That the same holds for our problem with numbers from 1 to 60 can be seen in the [reference table](../../materials/blog/backtracking-algorithms/table-pairs): While the twelve smallest numbers can form three or even four pairs each, the twelve largest numbers can only form two pairs each.

I changed the algorithm to run backwards from 60 to 1 and this reduced the number of tentative steps to from 5.2 billion to 112 million and the execution time from more than an hour to about a minute and 15 seconds!

Conceptually, the algorithm searches a tree of possibilities. Running the algorithm from 60 to 1 instead of from 1 to 60 changes the structure of this tree (figure 14):

![backtracking as tree traversal](/images/blog/backtracking-algorithms/backtracking_tree_structure.png)

Starting with the largest pairs yields a tree which is narrower but deeper as - with a bit of imagination - can already be seen in the [reference table](../../materials/blog/backtracking-algorithms/table-pairs). Or as the [AMM paper](https://www.maa.org/sites/default/files/pdf/awards/college.math.j.46.4.264.pdf) states: "... it presents fewer choices early on."

Another strategy worth exploring might be to run from 1 to 60 but for each number start with the highest-number pairing instead of the lowest one, i.e. pair 1 first with 48, 2 with 47, 3 with 46, 4 with 60 and so on. Thinking in terms of the tree, this means leaving the structure of the tree unchanged but exploring different branches first. I have not tried this.

I was not so interested in exploring this any further because it is highly dependant on the concrete problem. Does the statement "... it presents fewer choices early on..." still hold if the target set is not square numbers but e.g. prime numbers? This would have to be analyzed for every case separately. 

### 4{{< super "th" >}} and final attempt: fast forward

The generic algorithm might benefit from tree optimization techniques, either up-front before starting the traversal, or even at every step of the search. But I have no experience with such techniques and have not explored them any further.

But I was still thinking of ways to improve my first approach of just iterating over the numbers ascending, from 1 to 60. Could I somehow include information from the reverse traversal into the forward search?

Looking at my paper figures again, I suddenly understood the missing bit: In the first version of my algorithm, on the first traversal "down the tree", I would have chosen the 11{{< super "th" >}} pair to be [15 - 21] as shown in figure 5 because that's the first option listed for 15 in the second column of the [reference table](../../materials/blog/backtracking-algorithms/table-pairs) and because the number 21 is not yet used by any other pair which means it is still available (figure 15):

![backtracking 13: 10 pairs](/images/blog/backtracking-algorithms/backtracking_13_10_pairs.png)

But taking also the fourth column of the table into account (for all numbers greater than 15), I see that 60 can only be paired with 4 and 21. As 4 is already paired with 5, I cannot pair 15 with 21 now; I have to leave 21 free to be paired with 60. I will therefore try the second option for 15 right away, which is 34. I thus save myself from taking a wrong turn at this junction and traversing many additional subtrees which would not yield any result. 16 on the other hand can be paired with 20 as in the initial version of the algorithm (figure 16):

![backtracking 14: 12 pairs](/images/blog/backtracking-algorithms/backtracking_14_12_pairs.png)

Taking this effect of the current pairing on potential future pairings into account allows to stop and retrace much earler, i.e. cut off huge subtrees of the search tree which otherwise would have been traversed without any result.

If this additional check is incorporated into the forward-running algorithm which before took more than an hour to run and executed 5.2 billion steps, the program runs even slightly faster than the backward-running algorithm (it takes just about a minute) and uses less than 2 million steps!

[show and explain the python program here.]



## The analogy

try sth, and if it does not work, then throw the partial solution away and try sth different. 
probe and make small controlled changes
be empiric: use all available info
fail at the esrliest possible moment

- show the idea of a tree representation of the problem
- the more information you have (and apply)  early, the more subtrees you can clip off early —> no useless walking down paths which don’t lead to a somutiin 
- closing remark sth like: it’s a bit like the agile way of building products and finding solutions:
— try all possible paths
— consider all feedback available
— on all the paths which wihich are dead ends: fail at the earliest possible moment
