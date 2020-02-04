Title: "What's your favourite machine learning algorithm?"
Date: 2020-02-03 12:08
Category: Machine Learning
Tags: Machine Learning, Algorithm, Kernel, Feature
Slug: favourite-ml-algorithm
Authors: Ingo Fruend
Summary: Is there really anything like that? Rather some really nice ideas.

According to my friend Kyle Becker, this interview question seems to throw off quite a few candidates.
Honestly, it threw me off as well: I don't think I have a "favourite machine learning algorithm", I typically feel that the best solution is largely dictated by the problem to be solved.
However, when thinking a little more about this question, I must admit that there are some ideas that I find very elegant and that certainly had a big impact on the way I think about data.

When presenting these ideas, I will compare them to the approach of using a linear model or bag of features to make predictions from a set of hand-crafted features.
In most application areas of machine learning, this is not state of the art.
However, I believe that it is common practice in many companies that use machine learning to improve their business or provide a better user experience.

## The Kernel-Trick

The kernel trick is a technical term for a method which replaces the standard scalar product by an arbitrary symmetric and positive definite "kernel" function; thus, whenever your algorithm multiplies a row-vector by a column-vector, you instead use the value of the kernel function evaluated at the two vectors.
Using this technique, it is possible to extend linear models to work in highly non-linear and potentially infinite dimensional features spaces.
The kernel trick was really hot some 15 to 20 years ago and researchers created a bunch of fancy methods by simply prepending "Kernel-" to it.
A good reference to learn about kernel methods in more depth is [chapter 6 in the Bishop Book](https://www.springer.com/gp/book/9780387310732).
These kernel methods are now pretty out of fashion; they don't scale well to really big data sets and their performance has clearly been superseeded in almost all domains by deep neural networks.

A looser definition of "the kernel-trick" can be very useful when thinking about data.
We can interprete the kernel as a measure of the similarity between two data points.
Instead of describing data points by a set of more or less meaningful features, kernel methods *describe data points by their similarity to other data points*.
I believe that this can be quite profound when it comes to communicating early model versions with stakeholders.
Stakeholders can often give examples of particularly important or illustrative data points.
Using similarity to these illustrative data points as features can be a good baseline model.
Furthermore, such a baseline model can help build trust with stakeholders &mdash; after all, this model would almost trivially do "the right thing" on the illustrative cases.

## Feature learning

Today's state-of-the-art models differ in one crucial point from the simplified approach that I sketched above: They do not rely on hand-crafted features, but rather learn the best (or good) features to do the task from the data themselves.
This is clearly the case for deep neural networks, but it also applies for additive models or tree based approaches.
Where traditional approaches attempt to select features from a (potentially very large) pool of candidates, these models simply *construct* the right features.
Ultimately, this leads to the idea of training models "end-to-end".

Many recent developments in machine learning &mdash; such as embeddings, attention, transformers &mdash; can be seen as moving from feature selection to feature learning.
Often, these features are far from anything that human feature engineering could have brought about.
They typically work surprisingly well.

## Cool things that almost made it

Obviously there are a ton of other really cool ideas in recent machine learning that could have been in this list.
Close candidates are certainly reinforcement learning, causal inference, adversarial learning, or convolutions on graphs.
Although I acknowledge that these are powerful concepts that really profoundly influenced the way I think about data and about learning from data, they would not be the first thing that comes to my mind in response to the question "What's your favourite machine learning algorithm?".

<!-- acknowledge Kyle -->
<!-- personal perspective and by no means complete -->
<!--  -->
<!-- Strawman: -->
<!-- - Relate to linear models/ bag of features -->
<!-- - Hand-selected features -->
<!-- - This is common practice in most data science jobs -->
<!--  -->
<!-- - Kernel-Trick -->
<!--     - Kernels are out of fashion -->
<!--     - point out elegance of the formal kernel trick (changing scalar product) -->
<!--     - Loose version: Use data to describe data, similarity -->
<!--     - Facilitate Stakeholder communication -->
<!--     - Baseline model ~> build trust -->
<!-- - Feature Learning -->
<!--     - GAM, ANN, Trees -->
<!--     - Ultimately leads to end-to-end trainability -->
<!--     - Embeddings, Transformers, ... are all extensions of this concept -->
<!--  -->
<!-- Not covered: Graph signal processing, Reinforcement learning -->
