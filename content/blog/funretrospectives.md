---
title: "Fun Retrospectives"
date: 2023-03-28
draft: false
---

This first post is an updated version of an article which I have written in January 2021 for an older blog of mine which I have since discontinued. It was the time when we had to prepare our first distributed/online retrospectives during the Corona lockdown. It describes my experience with [Fun Retrospectives](https://www.funretrospectives.com/), a book, website and very helpful online retro tool.

## Introduction

For those who do not know the term “retrospective” (or “retro” for short), I cite the following method-independent definition:

> Another agile practice is the retrospective, in which a team having finished a development iteration takes time off further development
> to reflect on the experience and the lessons learned, with the goal of improving its development process.
>
> –-- [Bertrand Meyer](https://bertrandmeyer.com/): [Agile! The Good, the Hype and the Ugly](https://bertrandmeyer.com/2014/06/02/accurately-analyzing-agility/), pg. 9

Retrospectives are an important agile practice. They facilitate the team’s self-organization and continuous improvement.

The concept was of course not invented by the agile movement. When I started my career in the software industry more than twenty years ago, we used to have a “touch-down” meeting at the end of every project, as we used to have a “kick-off” meeting at the beginning of every project. In other settings, these touch-downs were simply called “lessons-learnt”. And even in the Swiss Army, where I served in the last century, trainings used to be closed with a “debriefing” (or in German: “Manöverkritik”).

The achievement of the agile movement lies in the importance and value it has given to retrospectives. Scrum development teams do a retro after every sprint, which usually means every 2 to 4 weeks.

There are many books on the theory, philosophy and psychology of retrospectives. Far out at the practical end of the spectrum, there is Fun Retrospectives by Paulo Caroli and Tainã Caetano, a book and website which contain a wealth of techniques and activities to “break the ice” in a retro, to get the conversation going and to help uncover the real, hidden issues which bother the team members. Again, the general idea is of course not new: Good moderators have known such games and activities in pre-agile times. But the book is a good starting point for the novice and a great source of inspiration even for the experienced scrum master.

These types of activities were developed for in-person meetings, as agile methods in general were developed for personal interaction, with developers sharing (depending on the method) one room, one desk, one keyboard or even one lunchbox. But some of the activities can easily be performed in a distributed setting. And, fortunately, the authors have built an online tool where they have implemented a few of them. They have, in fact, implemented their full [7-Step Agenda for Effective Retrospectives](https://caroli.org/en/a-7-step-agenda-for-effective-retrospectives/).

Let’s look at how to successfully prepare and execute such an online retrospective.

## Preparation

To prepare a retrospective for your team, just create a [new agenda](https://app.funretrospectives.com/new) and configure the seven steps:

### 1. CONTEXT

Set the context for the meeting, for example “last sprint” or “last delivery” or “last week’s major incident”. This will align the participants’ expectations as to the scope of the retro. As we are nearing the end of the first quarter, we’ll set the context to “Q1/2023” in the example and then click the **NEXT** button:

![1. context](../funretrospectives/images/1_context.png)

### 2. Prime Directive

For retrospectives, this is the well-known

> Regardless of what we discover, we understand and truly believe that everyone did the best job they could, given what they knew at the time,
> their skills and abilities, the resources available, and the situation at hand. 
>
> --- Norm Kerth: Project Retrospectives: A Handbook for Team Reviews

There are similar prime directives for futurespectives and team building meetings. As we’ll do a normal retrospective in the example, we'll choose "Retrospective" and then click the **NEXT** button again:

![2. prime directive](../funretrospectives/images/2_prime_directive.png)

### 3. Energizer

Choose a first activity to break the ice and get the participants engaged. At the time of this writing, three activities are available: [Guess who likes it](https://www.funretrospectives.com/guess-my-favorite-song/), [The roulette asks](https://www.funretrospectives.com/the-roulette-asks/) and [Fun Fact](https://www.funretrospectives.com/fun-fact/). Alternatively, a custom table can be created or the activity can be skipped by choosing "None". We’ll choose “Guess who likes it” in the example and then click the **NEXT** button again:

![3. prime directive](../funretrospectives/images/3_energizer.png)

### 4. Check-in

Choose an activity which allows the participants to reflect and communicate their mood and feelings about the retrospective and the group of participants. At the time of this writing, four activities are available: [Safety Check](https://www.funretrospectives.com/safety-check/), [Explorer, Shopper, Vacationer, Prisoner](https://www.funretrospectives.com/esvp-explorer-shopper-vacationer-prisoner/), [Happiness Radar](https://www.funretrospectives.com/happiness-radar/) and [One Word](https://www.funretrospectives.com/one-word/). Alternatively, a custom table can be created or the activity can be skipped by choosing "None". We’ll choose “Safety Check” in the example and then click the **NEXT** button again:

![4. check-in](../funretrospectives/images/4_check_in.png)

### 5. Main Course

Choose an activity for the main part of the retrospective where you want to collect feedback about the iteration (or whatever context you have chosen). At the time of this writing, four activities are available: [WWW: Worked well, kinda Worked, didn’t Work](https://www.funretrospectives.com/www-activity-worked-well-kinda-worked-didnt-work/), [The 3 Ls: Liked, Learned, Lacked](https://www.funretrospectives.com/the-3-ls-liked-learned-lacked/), [Open the Box: Add, Remove, Recycle](https://www.funretrospectives.com/open-the-box/) and [Hopes & Concerns](https://www.funretrospectives.com/hopes-and-concerns/). Alternatively, a custom table can be created. We’ll choose “Open the Box: Add, Remove, Recycle” in the example:

![5. main course](../funretrospectives/images/5_main_course.png)

All the main course activities allow the participants to post cards with items to be discussed. The cards can be colored for categorization. The default colors are yellow (for category “People”), blue (for category “Process”) and red (for category “Tools”):
 
![5.a. main course config](../funretrospectives/images/5a_main_course_config.png)

You can change the colors (by clicking on them) or change the labels (by clicking on the **pen** icons) to group the items along different categories. We'll leave the default configuration unchanged and click the **NEXT** button again.

### 6. Filtering

Define the voting scheme on the items collected in the main course. [Dot Voting](https://www.funretrospectives.com/dot-voting/) provides feedback about the relative importance of the items to the majority of the participants whereas [Select one and talk](https://www.funretrospectives.com/select-one-and-talk/) allows every participant to discuss the item most important to them. The other voting schemes do not seem to be enabled yet at the time of this writing. We’ll choose Dot Voting in the example and then click the **NEXT** button again:

![6. filtering](../funretrospectives/images/6_filtering.png)

### 7. Check-out

Choose an activity to close the meeting. At the time of this writing, three very different activities are available: While [One word before leaving](https://www.funretrospectives.com/one-word-before-leaving/) allows each participant to communicate their feelings at the end of the meeting and [Token of appreciation](https://www.funretrospectives.com/token-of-appreciation/) fosters appreciation and acknowlegement between team members, [Who-What-When Steps to Action](https://www.funretrospectives.com/the-who-what-when-steps-to-action/) helps to define follow-up actions, deadlines and accountabilities. Alternatively, a custom table can be created or the activity can be skipped by choosing "None".  We’ll choose “Who-What-When Steps to Action” in the example and then click the **COMPLETE** button and then the **CREATE RETROSPECTIVE** button:

![7. check-out](../funretrospectives/images/7_check_out.png)

*more content will be added here*


## Execution

*more content will be added here*

## Caveats

*more content will be added here*

![pilgrims](/images/pilgrims.png)
