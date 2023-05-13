A restricted Boltzmann machine (RBM) is a generative stochastic
artificial neural network that can learn a probability distribution over
its set of inputs. RBMs were initially invented under the name Harmonium
by Paul Smolensky in 1986, and rose to prominence after Geoffrey Hinton
and collaborators invented fast learning algorithms for them in the
mid-2000. RBMs have found applications in dimensionality
reduction,classification,collaborative filtering, feature learning,topic
modelling and even many body quantum mechanics. They can be trained in
either supervised or unsupervised ways, depending on the task. As their
name implies, RBMs are a variant of Boltzmann machines, with the
restriction that their neurons must form a bipartite graph: a pair of
nodes from each of the two groups of units (commonly referred to as the
\"visible\" and \"hidden\" units respectively) may have a symmetric
connection between them; and there are no connections between nodes
within a group. By contrast, \"unrestricted\" Boltzmann machines may
have connections between hidden units. This restriction allows for more
efficient training algorithms than are available for the general class
of Boltzmann machines, in particular the gradient-based contrastive
divergence algorithm.Restricted Boltzmann machines can also be used in
deep learning networks. In particular, deep belief networks can be
formed by \"stacking\" RBMs and optionally fine-tuning the resulting
deep network with gradient descent and backpropagation. Structure The
standard type of RBM has binary-valued (Boolean) hidden and visible
units, and consists of a matrix of weights W {\\displaystyle W} of size
m × n {\\displaystyle m\\times n} . Each weight element ( w i , j )
{\\displaystyle (w\_{i,j})} of the matrix is associated with the
connection between the visible (input) unit v i {\\displaystyle v\_{i}}
and the hidden unit h j {\\displaystyle h\_{j}} . In addition, there are
bias weights (offsets) a i {\\displaystyle a\_{i}} for v i
{\\displaystyle v\_{i}} and b j {\\displaystyle b\_{j}} for h j
{\\displaystyle h\_{j}} . Given the weights and biases, the energy of a
configuration (pair of boolean vectors) (v,h) is defined as E ( v , h )
= − ∑ i a i v i − ∑ j b j h j − ∑ i ∑ j v i w i , j h j {\\displaystyle
E(v,h)=-\\sum \_{i}a\_{i}v\_{i}-\\sum \_{j}b\_{j}h\_{j}-\\sum \_{i}\\sum
\_{j}v\_{i}w\_{i,j}h\_{j}} or, in matrix notation, E ( v , h ) = − a T v
− b T h − v T W h . {\\displaystyle E(v,h)=-a\^{\\mathrm {T}
}v-b\^{\\mathrm {T} }h-v\^{\\mathrm {T} }Wh.} This energy function is
analogous to that of a Hopfield network. As with general Boltzmann
machines, the joint probability distribution for the visible and hidden
vectors is defined in terms of the energy function as follows, P ( v , h
) = 1 Z e − E ( v , h ) {\\displaystyle P(v,h)={\\frac
{1}{Z}}e\^{-E(v,h)}} where Z {\\displaystyle Z} is a partition function
defined as the sum of e − E ( v , h ) {\\displaystyle e\^{-E(v,h)}} over
all possible configurations, which can be interpreted as a normalizing
constant to ensure that the probabilities sum to 1. The marginal
probability of a visible vector is the sum of P ( v , h )
{\\displaystyle P(v,h)} over all possible hidden layer configurations, P
( v ) = 1 Z ∑ { h } e − E ( v , h ) {\\displaystyle P(v)={\\frac
{1}{Z}}\\sum \_{\\{h\\}}e\^{-E(v,h)}} ,and vice versa. Since the
underlying graph structure of the RBM is bipartite (meaning there is no
intra-layer connections), the hidden unit activations are mutually
independent given the visible unit activations. Conversely, the visible
unit activations are mutually independent given the hidden unit
activations. That is, for m visible units and n hidden units, the
conditional probability of a configuration of the visible units v, given
a configuration of the hidden units h, is P ( v \| h ) = ∏ i = 1 m P ( v
i \| h ) {\\displaystyle P(v\|h)=\\prod \_{i=1}\^{m}P(v\_{i}\|h)}
.Conversely, the conditional probability of h given v is P ( h \| v ) =
∏ j = 1 n P ( h j \| v ) {\\displaystyle P(h\|v)=\\prod
\_{j=1}\^{n}P(h\_{j}\|v)} .The individual activation probabilities are
given by P ( h j = 1 \| v ) = σ ( b j + ∑ i = 1 m w i , j v i )
{\\displaystyle P(h\_{j}=1\|v)=\\sigma \\left(b\_{j}+\\sum
\_{i=1}\^{m}w\_{i,j}v\_{i}\\right)} and P ( v i = 1 \| h ) = σ ( a i + ∑
j = 1 n w i , j h j ) {\\displaystyle \\,P(v\_{i}=1\|h)=\\sigma
\\left(a\_{i}+\\sum \_{j=1}\^{n}w\_{i,j}h\_{j}\\right)} where σ
{\\displaystyle \\sigma } denotes the logistic sigmoid. The visible
units of Restricted Boltzmann Machine can be multinomial, although the
hidden units are Bernoulli. In this case, the logistic function for
visible units is replaced by the softmax function P ( v i k = 1 \| h ) =
exp ⁡ ( a i k + Σ j W i j k h j ) Σ k ′ = 1 K exp ⁡ ( a i k ′ + Σ j W i j
k ′ h j ) {\\displaystyle P(v\_{i}\^{k}=1\|h)={\\frac
{\\exp(a\_{i}\^{k}+\\Sigma \_{j}W\_{ij}\^{k}h\_{j})}{\\Sigma
\_{k\'=1}\^{K}\\exp(a\_{i}\^{k\'}+\\Sigma \_{j}W\_{ij}\^{k\'}h\_{j})}}}
where K is the number of discrete values that the visible values have.
They are applied in topic modeling, and recommender systems. Relation to
other models Restricted Boltzmann machines are a special case of
Boltzmann machines and Markov random fields. Their graphical model
corresponds to that of factor analysis. Training algorithm Restricted
Boltzmann machines are trained to maximize the product of probabilities
assigned to some training set V {\\displaystyle V} (a matrix, each row
of which is treated as a visible vector v {\\displaystyle v} ), arg ⁡ max
W ∏ v ∈ V P ( v ) {\\displaystyle \\arg \\max \_{W}\\prod \_{v\\in
V}P(v)} or equivalently, to maximize the expected log probability of a
training sample v {\\displaystyle v} selected randomly from V
{\\displaystyle V} : arg ⁡ max W E \[ log ⁡ P ( v ) \] {\\displaystyle
\\arg \\max \_{W}\\mathbb {E} \\left\[\\log P(v)\\right\]} The algorithm
most often used to train RBMs, that is, to optimize the weight matrix W
{\\displaystyle W} , is the contrastive divergence (CD) algorithm due to
Hinton, originally developed to train PoE (product of experts) models.
The algorithm performs Gibbs sampling and is used inside a gradient
descent procedure (similar to the way backpropagation is used inside
such a procedure when training feedforward neural nets) to compute
weight update. The basic, single-step contrastive divergence (CD-1)
procedure for a single sample can be summarized as follows: Take a
training sample v, compute the probabilities of the hidden units and
sample a hidden activation vector h from this probability distribution.
Compute the outer product of v and h and call this the positive
gradient. From h, sample a reconstruction v\' of the visible units, then
resample the hidden activations h\' from this. (Gibbs sampling step)
Compute the outer product of v\' and h\' and call this the negative
gradient. Let the update to the weight matrix W {\\displaystyle W} be
the positive gradient minus the negative gradient, times some learning
rate: Δ W = ϵ ( v h T − v ′ h ′ T ) {\\displaystyle \\Delta W=\\epsilon
(vh\^{\\mathsf {T}}-v\'h\'\^{\\mathsf {T}})} . Update the biases a and b
analogously: Δ a = ϵ ( v − v ′ ) {\\displaystyle \\Delta a=\\epsilon
(v-v\')} , Δ b = ϵ ( h − h ′ ) {\\displaystyle \\Delta b=\\epsilon
(h-h\')} .A Practical Guide to Training RBMs written by Hinton can be
found on his homepage. Stacked Restricted Boltzmann Machine The
difference between the Stacked Restricted Boltzmann Machines and RBM is
that RBM has lateral connections within a layer that are prohibited to
make analysis tractable. On the other hand, the Stacked Boltzmann
consists of a combination of an unsupervised three-layer network with
symmetric weights and a supervised fine-tuned top layer for recognizing
three classes. The usage of Stacked Boltzmann is to understand Natural
languages, retrieve documents, image generation, and classification.
These functions are trained with unsupervised pre-training and/or
supervised fine-tuning. Unlike the undirected symmetric top layer, with
a two-way unsymmetric layer for connection for RBM. The restricted
Boltzmann\'s connection is three-layers with asymmetric weights, and two
networks are combined into one. Stacked Boltzmann does share
similarities with RBM, the neuron for Stacked Boltzmann is a stochastic
binary Hopfield neuron, which is the same as the Restricted Boltzmann
Machine. The energy from both Restricted Boltzmann and RBM is given by
Gibb\'s probability measure: E = − 1 2 ∑ i , j w i j s i s j + ∑ i θ i s
i {\\displaystyle E=-{\\frac {1}{2}}\\sum
\_{i,j}{w\_{ij}{s\_{i}}{s\_{j}}}+\\sum \_{i}{\\theta \_{i}}{s\_{i}}} .
The training process of Restricted Boltzmann is similar to RBM.
Restricted Boltzmann train one layer at a time and approximate
equilibrium state with a 3-segment pass, not performing back
propagation. Restricted Boltzmann uses both supervised and unsupervised
on different RBM for pre-training for classification and recognition.
The training uses contrastive divergence with Gibbs sampling: Δwij =
e\*(pij - p\'ij) The restricted Boltzmann\'s strength is it performs a
non-linear transformation so it\'s easy to expand, and can give a
hierarchical layer of features. The Weakness is that it has complicated
calculations of integer and real-valued neurons. It does not follow the
gradient of any function, so the approximation of Contrastive divergence
to maximum likelihood is improvised. Literature Fischer, Asja; Igel,
Christian (2012), \"An Introduction to Restricted Boltzmann Machines\",
Progress in Pattern Recognition, Image Analysis, Computer Vision, and
Applications, Lecture Notes in Computer Science, Berlin, Heidelberg:
Springer Berlin Heidelberg, vol. 7441, pp. 14--36,
doi:10.1007/978-3-642-33275-3_2, ISBN 978-3-642-33274-6, retrieved
2021-09-19 See also Autoencoder Helmholtz machine References External
links Introduction to Restricted Boltzmann Machines. Edwin Chen\'s blog,
July 18, 2011. \"A Beginner\'s Guide to Restricted Boltzmann Machines\".
Archived from the original on February 11, 2017. Retrieved November 15,
2018.{{cite web}}: CS1 maint: bot: original URL status unknown (link).
Deeplearning4j Documentation \"Understanding RBMs\". Archived from the
original on September 20, 2016. Retrieved December 29, 2014..
Deeplearning4j Documentation Python implementation of Bernoulli RBM and
tutorial SimpleRBM is a very small RBM code (24kB) useful for you to
learn about how RBMs learn and work. Julia implementation of Restricted
Boltzmann machines:
https://github.com/cossio/RestrictedBoltzmannMachines.jl
