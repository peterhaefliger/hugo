---
title: "More Fun with Retrospectives: Check your rearview mirror!"
date: 2023-12-15
draft: false
tags: ["agilepractices"]
---

_This is the translation of [my blog post written in German](https://blog.hslu.ch/informatik-wb/2023/11/08/voll-retro/) as an assignment for the [CAS DevOps Leadership and Agile Methods](https://www.hslu.ch/en/lucerne-school-of-information-technology/continuing-education/technologies-and-methods/cas-devops-and-cloud-transformation/) which I am currently doing at the [Lucerne University of Applied Sciences and Arts](https://www.hslu.ch/en/). The translation is rather free, as self-translations usually are, because the author can allow themself full liberties. But let me first explain the context of the course assignment:_

_During the course, a colleague brought up the question of how shy team members can be encouraged to speak up in a retro. I answered that there are techniques  and tools like [Fun Retrospectives](https://www.funretrospectives.com/) which I had described in [my very first post on this blog](/blog/funretrospectives). The teacher then mentioned [Retromat](https://retromat.org/en/) and I decided to compare the two and give a general introduction to retrospectives in my blog post assignment._

_Contrary to the more technical text-based theme I use here, the university's wordpress theme asked for a "featured image" to be displayed not only at the top of the post itself but also as a thumbnail in the list of posts. So the first challenge was to find a picture (in the public domain) which would somehow illustrate my topic of retrospectives and get the site's visitor interested enough to click and read the article._

_How can a retrospective be visualized in a catchy image? Over the course of the article's evolution, I chose three different pictures:_

### 1. Flashlight

_My first idea was a flashlight because the goal of a retro is to_ uncover _obstacles or_ bring _challenges from dark hidden corners_ into full light:

![Featured image "Flashlight"](/images/blog/more-fun-with-retrospectives/1_Fenix_P1D_LED_flashlight.jpg)

(Source: [Fenix P1D LED flashlight](https://commons.wikimedia.org/wiki/File:Fenix_P1D_LED_flashlight_(2739718566).jpg))

### 2. Antenna

_My second idea was an antenna because the goal of the retro can only be reached if every voice is_ heard:

![Featured image "Antenna"](/images/blog/more-fun-with-retrospectives/2_apex_antenna.jpg)

(Source: [APEX Antenna](https://commons.wikimedia.org/wiki/File:APEX_Antenna.jpg))

### 3. Retro car with rearview mirror

_My third idea was a "retro" car's rearview mirror because in a retro the team reflects on the_ past _course to make adjustments to the_ future _course:_

![Featured image "Retro car"](/images/blog/more-fun-with-retrospectives/3_retro_car_rearview_mirror.jpg)

(Source: [Look back again](https://commons.wikimedia.org/wiki/File:Look_back_again_(7664606152).jpg))

_The third idea is the one I stayed with. I simply like the tone of the picture the most and I like the "retro" pun._ 

_Which one would you have chosen?_

_Congratulations! You have chosen well and the reader has clicked. So here is the translated article:_

# Retrospectives: Don't forget to check your rearview mirror!

**Agile teams do regular retrospectives or "retros" to reflect on the development process and their collaboration and to identify possibilities for improvement. Structures, techniques and tools like Fun Retrospectives or Retromat can help to evaluate the current course and change the lane or take the appropriate turn.**

A question for starters: How do you feel right now that you have decided to read this article? In one word: Interested? Curious? Impatient?

The question is a check-in activity called [One Word](https://www.funretrospectives.com/one-word/). It is described in Fun Retrospectives. [Fun Retrospectives](https://www.funretrospectives.com/) describes a [7-Step Agenda for Effective Retrospectives](https://caroli.org/en/a-7-step-agenda-for-effective-retrospectives/) while [Retromat](https://retromat.org/en/) builds retrospectives from the 5 steps described in the [Pragmatic Programmers](https://pragprog.com/) book [Agile Retrospectives](https://pragprog.com/titles/dlret/agile-retrospectives/). They are compared in the following table:

![Comparision Fun Retrospectives and Retromat](/images/blog/more-fun-with-retrospectives/4_Table_steps_funretrospectives_retromat.png)

The following three phases are the common denominator of the two structures:

* Set the Stage (Engergizer / Check-in)
* Main Course (Gather Data / Generate Insights / Decide what to do)
* Closing / Check-out

Both platforms offer a variety of activities for each step. A few examples are described in the following sections.

## Set the Stage

Fun Retrospectives divides this phase into four smaller steps. For "Set the Context" and "Prime Directive" see [my earlier post](/blog/funretrospectives) or [this article](https://caroli.org/en/a-7-step-agenda-for-effective-retrospectives) by Fun Retrospectives' co-author [Paulo Caroli](https://caroli.org/en). An Energizer is an icebreaker to wake the participants up and to loosen any initial tension. One example is [Fun Fact](https://www.funretrospectives.com/fun-fact) for a newly-formed team whose members do not yet know much about each other: Every member writes something about themself on a sticky note, for example a hobby or a favourite song. The group then tries to guess which fun fact is about which member. This can be very surprising and much fun!

Check-in activities, on the other hand, are needed to feel the mood in the room and gauge the engagement level of the participants. [One Word](https://www.funretrospectives.com/one-word/) has already been mentioned. Another frequently described activity is ESVP - Explorer, Shopper, Vacationer, Prisoner - (see for example [here](https://retromat.org/en/?id=1) or [here](https://www.funretrospectives.com/esvp-explorer-shopper-vacationer-prisoner)) where every participant classifies themself as one of the following:

* **Explorers**: Are eager to discover new ideas and insights. They want to learn everything they can about the iteration/release/project.
* **Shoppers**: Will look over all the available information and be happy to go home with one useful new idea.
* **Vacationers**: Aren't interested in the work of the retrospective but are happy to be away from the daily grind.
* **Prisoners**: Feel they have been forced to attend and would rather be doing something else.

The following screenshot shows the real-world example of a highly motivated team with which I facilitated a retro last year:

![Screenshot ESVP](/images/blog/more-fun-with-retrospectives/5_ESVP.png)

Nice! With this group, the main course can start! If, on the other hand, a larger part of the team felt like vacationers or even prisoners, then the facilitator would have to consider stopping and canceling the event. There is no point in a retro if the participants are either not interested in learning anything or lack the psychological safety to address their problems and pain points.

## Main Course

In the main course phase, information is gathered first: What went well in the defined context, what did not? There are numerous templates for this. Most are simply used to group topics into two, three or four categories. The activities' names speak for themselves: [WWW: Worked Well, kinda Worked, didn’t Work](https://www.funretrospectives.com/www-activity-worked-well-kinda-worked-didnt-work), [3Ls: Liked, Learned, Lacked](https://www.funretrospectives.com/the-3-ls-liked-learned-lacked) oder [Add, Remove, Recycle](https://www.funretrospectives.com/open-the-box). Another activity described in several places (for example [here](https://retromat.org/en/?id=19) or [here](https://www.funretrospectives.com/anchors-and-engine)) is Engines & Anchors where topics are grouped by what drives the team forward and what holds the team back:

![Screenshot Engines & Anchors](/images/blog/more-fun-with-retrospectives/6_engines_and_anchors.png)

The screenshot shows a real-world example, anonymized. The underlying drawing by [Héctor Horacio Jure](https://www.linkedin.com/in/h%C3%A9ctorhjure/) has been taken with his permission from this [medium article](https://medium.com/@hectorhjure/scrum-toolkit-retrospective-1a8d7334d97a).

Fun Retrospectives seems to assume that the action items follow more or less automatically from these topics. Just rev the engines and cut the anchors! Templates with category names like "Add, Remove, Recycle" do indeed imply the corresponding actions. Retromat, on the other hand, describes activities like [5 Whys](https://retromat.org/en/?id=8) or [Speed Dating](https://retromat.org/en/?id=26) to generate further insights. If the collected topics only describe symptoms, these additional activities can help to find the underlying causes. More inspiration can be found in [Liberating Structures](https://www.liberatingstructures.com/).

## Closing

For closing, both platforms offer check-out activities. They allow the team to express mutual [appreciation](https://retromat.org/en/?id=15) or the facilitator to feel the mood again with [one word](https://www.funretrospectives.com/one-word-before-leaving). Therefore, I ask the starter question again before leaving: How do you feel now that you have read my article? Again in one word: Bored or disappointed? I hope not! Still interested? Informed? Or even inspired?