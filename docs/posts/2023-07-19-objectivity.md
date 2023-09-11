---
draft: true
date: 2023-07-19
categories:
  - General
tags:
  - Data Science
  - Teams
  - Social Interaction
authors: [ingo]
cover_image: /images/2023-07-19-objectivity.jpg
---
# Rethink objectivity!

We like to think of our ideas and opionions to be "objectively true". Often we use this term kind of loosely as synonymous to "beyond doubt" or "it can not be wrong". This notion of objectivity is not entirely correct. Moreover, I will sketch below how it can hinder productive social interactions.

<!-- more -->

In this post, I will start by elaborating a little more about the role of objectivity in the scientific process and I will then argue that there is almost no place for objectivity in our daily lifes that are filled with social interaction but not so much with scientific knowledge seeking.

My first systematic encouter with the concept objectivity was as part of a course on psychometrics.
Measuring psychological concepts like personality, attention, or intelligence is extremely difficult and as a result, many of the core problems with measuring anything in general become pretty explicit.
There are three classicial dimensions along which the quality of a measurement procedure can be judged (there are a couple of others too, but these three classical ones will suffice here). First, there is objectivity, which refers to *independence of the measurement outcome from the subject performing the measurement*. Second, there is reliability which describes other "unsystematic" measurement noise. The lower that measurement noise, the more reliable the measurement procedure. Finally, there is validity which is often loosely summarized as "does the measurement procedure actually measure what it is supposed to measure". I will here first discuss objectivity and I will later also touch upon validity. This post will however skip all further discussion of reliability&mdash;it's likely the concept most familiar for most data scientists anyway (although likely under different names).

We tend to take objectivity for granted when thinking of measurements of concepts like e.g. length. However, it is easy to also identify more and less objective length measurement procedures: Measuring the length of&mdash;for example&mdash;a table by using one's own hand span is less objective than using normed measuring tape. However, comparing these cases illustrates that objectivity is not a yes or now thing, but is rather gradual. For example, eye-balling a table's length is likely even less objective than using the hand span.

I tend to think of objectivity as a quality of data collection: A dataset would be "objective" if it is statistically indistinguishable from another dataset (real or imaginary) that was collected by somebody else but with the same question in mind.
In fact, most datasets that we deal with in machine learning are *not objective* in this sense.
For example, the recent discussion about racial biases in machine learning illustrated that&mdash;a facial recognition dataset collected by a typical central-european institution tends to look different and include a different range of faces and facial features than a dataset collected by an central-african institution.
Of course, in both cases, reflecting on these biases will help reduce them.

Many of today's datasets&mdash;in particular many proprietary ones&mdash;are not collected by humans who manually enter numbers into an excel sheet, but they are collected by machines that are programmed to store interactions with a large automatic system. It might appear that these datasets are by nature independent of the person who is collecting the data&mdash;after all, there isn't even a person, is there?
I believe that this perspective is misleading.
In almost all cases, there are humans involved in programming the machines that collect data and non-objective decisions enter the design of the system with which people interact.
Often these decisions are driven by business demands and that's fine, but it's important to keep in mind that these decisions are rarely driven by an attempt to collect clean and unbiased data.

You might now think that putting in the effort of collecting such an "objective dataset" would guarantee that any insight derived from such a dataset would be true for anyone and anywhere.
As I mentioned above, there are other dimensions along which the quality of a measurement could be judged.
More importantly, the process of deriving these conclusions is inherently subjective: Which statistical/machine learning method do I pick? What are the questions I ask? How do I break these questions down? What hypotheses do I test? These steps involve many small decisions that leave a lot of room for subjectivity.
However, the advantage of an objective dataset is, that we can focus our attention on judging if the analysis process is sound, rather than having to also constantly question the underlying data.

In almost all social contexts, we argue on the basis of almost no data.
The little data we take into account usually is further filtered by our senses&mdash;our eyes, our ears, …
Even if that data was objective, we would typically care about the conclusions we draw from this little data: Feline likes to help others, Carlo is reliable, Martha is angry, Tim is unfit for the job, but Tyron is not, …
Pretending that any of these was true independent of my own perspective is false, but claiming that "Martha is objectively angry" or worse yet "Tim is objectively unfit for the job" is unfair for Martha and Tim and will also kill any discussion.
Yet, good team work is fundamentally about discussion and killing that discussion by claiming objective truth will often hurt overall performance of the team.

> The social dimension of the post was inspired by a chapter about "rational" argumentation in M. Amjahid's book "Der Weiße Fleck".
