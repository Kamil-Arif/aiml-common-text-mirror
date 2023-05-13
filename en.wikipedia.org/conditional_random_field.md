Conditional random fields (CRFs) are a class of statistical modeling
methods often applied in pattern recognition and machine learning and
used for structured prediction. Whereas a classifier predicts a label
for a single sample without considering \"neighbouring\" samples, a CRF
can take context into account. To do so, the predictions are modelled as
a graphical model, which represents the presence of dependencies between
the predictions. What kind of graph is used depends on the application.
For example, in natural language processing, \"linear chain\" CRFs are
popular, for which each prediction is dependent only on its immediate
neighbours. In image processing, the graph typically connects locations
to nearby and/or similar locations to enforce that they receive similar
predictions. Other examples where CRFs are used are: labeling or parsing
of sequential data for natural language processing or biological
sequences, part-of-speech tagging, shallow parsing, named entity
recognition, gene finding, peptide critical functional region finding,
and object recognition and image segmentation in computer vision.
Description CRFs are a type of discriminative undirected probabilistic
graphical model. Lafferty, McCallum and Pereira define a CRF on
observations X {\\displaystyle {\\boldsymbol {X}}} and random variables
Y {\\displaystyle {\\boldsymbol {Y}}} as follows: Let G = ( V , E )
{\\displaystyle G=(V,E)} be a graph such that Y = ( Y v ) v ∈ V
{\\displaystyle {\\boldsymbol {Y}}=({\\boldsymbol {Y}}\_{v})\_{v\\in V}}
, so that Y {\\displaystyle {\\boldsymbol {Y}}} is indexed by the
vertices of G {\\displaystyle G} . Then ( X , Y ) {\\displaystyle
({\\boldsymbol {X}},{\\boldsymbol {Y}})} is a conditional random field
when each random variable Y v {\\displaystyle {\\boldsymbol {Y}}\_{v}} ,
conditioned on X {\\displaystyle {\\boldsymbol {X}}} , obeys the Markov
property with respect to the graph; that is, its probability is
dependent only on its neighbours in G: P ( Y v \| X , { Y w : w ≠ v } )
= P ( Y v \| X , { Y w : w ∼ v } ) {\\displaystyle P({\\boldsymbol
{Y}}\_{v}\|{\\boldsymbol {X}},\\{{\\boldsymbol {Y}}\_{w}:w\\neq
v\\})=P({\\boldsymbol {Y}}\_{v}\|{\\boldsymbol {X}},\\{{\\boldsymbol
{Y}}\_{w}:w\\sim v\\})} , where w ∼ v {\\displaystyle {\\mathit
{w}}\\sim v} means that w {\\displaystyle w} and v {\\displaystyle v}
are neighbors in G {\\displaystyle G} . What this means is that a CRF is
an undirected graphical model whose nodes can be divided into exactly
two disjoint sets X {\\displaystyle {\\boldsymbol {X}}} and Y
{\\displaystyle {\\boldsymbol {Y}}} , the observed and output variables,
respectively; the conditional distribution p ( Y \| X ) {\\displaystyle
p({\\boldsymbol {Y}}\|{\\boldsymbol {X}})} is then modeled. Inference
For general graphs, the problem of exact inference in CRFs is
intractable. The inference problem for a CRF is basically the same as
for an MRF and the same arguments hold. However, there exist special
cases for which exact inference is feasible: If the graph is a chain or
a tree, message passing algorithms yield exact solutions. The algorithms
used in these cases are analogous to the forward-backward and Viterbi
algorithm for the case of HMMs. If the CRF only contains pair-wise
potentials and the energy is submodular, combinatorial min cut/max flow
algorithms yield exact solutions.If exact inference is impossible,
several algorithms can be used to obtain approximate solutions. These
include: Loopy belief propagation Alpha expansion Mean field inference
Linear programming relaxations Parameter Learning Learning the
parameters θ {\\displaystyle \\theta } is usually done by maximum
likelihood learning for p ( Y i \| X i ; θ ) {\\displaystyle
p(Y\_{i}\|X\_{i};\\theta )} . If all nodes have exponential family
distributions and all nodes are observed during training, this
optimization is convex. It can be solved for example using gradient
descent algorithms, or Quasi-Newton methods such as the L-BFGS
algorithm. On the other hand, if some variables are unobserved, the
inference problem has to be solved for these variables. Exact inference
is intractable in general graphs, so approximations have to be used.
Examples In sequence modeling, the graph of interest is usually a chain
graph. An input sequence of observed variables X {\\displaystyle X}
represents a sequence of observations and Y {\\displaystyle Y}
represents a hidden (or unknown) state variable that needs to be
inferred given the observations. The Y i {\\displaystyle Y\_{i}} are
structured to form a chain, with an edge between each Y i − 1
{\\displaystyle Y\_{i-1}} and Y i {\\displaystyle Y\_{i}} . As well as
having a simple interpretation of the Y i {\\displaystyle Y\_{i}} as
\"labels\" for each element in the input sequence, this layout admits
efficient algorithms for: model training, learning the conditional
distributions between the Y i {\\displaystyle Y\_{i}} and feature
functions from some corpus of training data. decoding, determining the
probability of a given label sequence Y {\\displaystyle Y} given X
{\\displaystyle X} . inference, determining the most likely label
sequence Y {\\displaystyle Y} given X {\\displaystyle X} .The
conditional dependency of each Y i {\\displaystyle Y\_{i}} on X
{\\displaystyle X} is defined through a fixed set of feature functions
of the form f ( i , Y i − 1 , Y i , X ) {\\displaystyle
f(i,Y\_{i-1},Y\_{i},X)} , which can be thought of as measurements on the
input sequence that partially determine the likelihood of each possible
value for Y i {\\displaystyle Y\_{i}} . The model assigns each feature a
numerical weight and combines them to determine the probability of a
certain value for Y i {\\displaystyle Y\_{i}} . Linear-chain CRFs have
many of the same applications as conceptually simpler hidden Markov
models (HMMs), but relax certain assumptions about the input and output
sequence distributions. An HMM can loosely be understood as a CRF with
very specific feature functions that use constant probabilities to model
state transitions and emissions. Conversely, a CRF can loosely be
understood as a generalization of an HMM that makes the constant
transition probabilities into arbitrary functions that vary across the
positions in the sequence of hidden states, depending on the input
sequence. Notably, in contrast to HMMs, CRFs can contain any number of
feature functions, the feature functions can inspect the entire input
sequence X {\\displaystyle X} at any point during inference, and the
range of the feature functions need not have a probabilistic
interpretation. Variants Higher-order CRFs and semi-Markov CRFs CRFs can
be extended into higher order models by making each Y i {\\displaystyle
Y\_{i}} dependent on a fixed number k {\\displaystyle k} of previous
variables Y i − k , . . . , Y i − 1 {\\displaystyle
Y\_{i-k},\...,Y\_{i-1}} . In conventional formulations of higher order
CRFs, training and inference are only practical for small values of k
{\\displaystyle k} (such as k ≤ 5), since their computational cost
increases exponentially with k {\\displaystyle k} . However, another
recent advance has managed to ameliorate these issues by leveraging
concepts and tools from the field of Bayesian nonparametrics.
Specifically, the CRF-infinity approach constitutes a CRF-type model
that is capable of learning infinitely-long temporal dynamics in a
scalable fashion. This is effected by introducing a novel potential
function for CRFs that is based on the Sequence Memoizer (SM), a
nonparametric Bayesian model for learning infinitely-long dynamics in
sequential observations. To render such a model computationally
tractable, CRF-infinity employs a mean-field approximation of the
postulated novel potential functions (which are driven by an SM). This
allows for devising efficient approximate training and inference
algorithms for the model, without undermining its capability to capture
and model temporal dependencies of arbitrary length. There exists
another generalization of CRFs, the semi-Markov conditional random field
(semi-CRF), which models variable-length segmentations of the label
sequence Y {\\displaystyle Y} . This provides much of the power of
higher-order CRFs to model long-range dependencies of the Y i
{\\displaystyle Y\_{i}} , at a reasonable computational cost. Finally,
large-margin models for structured prediction, such as the structured
Support Vector Machine can be seen as an alternative training procedure
to CRFs. Latent-dynamic conditional random field Latent-dynamic
conditional random fields (LDCRF) or discriminative probabilistic latent
variable models (DPLVM) are a type of CRFs for sequence tagging tasks.
They are latent variable models that are trained discriminatively. In an
LDCRF, like in any sequence tagging task, given a sequence of
observations x = x 1 , ... , x n {\\displaystyle x\_{1},\\dots ,x\_{n}}
, the main problem the model must solve is how to assign a sequence of
labels y = y 1 , ... , y n {\\displaystyle y\_{1},\\dots ,y\_{n}} from
one finite set of labels Y. Instead of directly modeling P(y\|x) as an
ordinary linear-chain CRF would do, a set of latent variables h is
\"inserted\" between x and y using the chain rule of probability: P ( y
\| x ) = ∑ h P ( y \| h , x ) P ( h \| x ) {\\displaystyle P(\\mathbf
{y} \|\\mathbf {x} )=\\sum \_{\\mathbf {h} }P(\\mathbf {y} \|\\mathbf
{h} ,\\mathbf {x} )P(\\mathbf {h} \|\\mathbf {x} )} This allows
capturing latent structure between the observations and labels. While
LDCRFs can be trained using quasi-Newton methods, a specialized version
of the perceptron algorithm called the latent-variable perceptron has
been developed for them as well, based on Collins\' structured
perceptron algorithm. These models find applications in computer vision,
specifically gesture recognition from video streams and shallow parsing.
See also Hammersley--Clifford theorem Maximum entropy Markov model
(MEMM) References Further reading McCallum, A.: Efficiently inducing
features of conditional random fields. In: Proc. 19th Conference on
Uncertainty in Artificial Intelligence. (2003) Wallach, H.M.:
Conditional random fields: An introduction. Technical report
MS-CIS-04-21, University of Pennsylvania (2004) Sutton, C., McCallum,
A.: An Introduction to Conditional Random Fields for Relational
Learning. In \"Introduction to Statistical Relational Learning\". Edited
by Lise Getoor and Ben Taskar. MIT Press. (2006) Online PDF Klinger, R.,
Tomanek, K.: Classical Probabilistic Models and Conditional Random
Fields. Algorithm Engineering Report TR07-2-013, Department of Computer
Science, Dortmund University of Technology, December 2007. ISSN
1864-4503. Online PDF
