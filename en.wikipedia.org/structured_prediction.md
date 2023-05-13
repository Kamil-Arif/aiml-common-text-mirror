Structured prediction or structured (output) learning is an umbrella
term for supervised machine learning techniques that involves predicting
structured objects, rather than scalar discrete or real values.Similar
to commonly used supervised learning techniques, structured prediction
models are typically trained by means of observed data in which the true
prediction value is used to adjust model parameters. Due to the
complexity of the model and the interrelations of predicted variables
the process of prediction using a trained model and of training itself
is often computationally infeasible and approximate inference and
learning methods are used. Applications For example, the problem of
translating a natural language sentence into a syntactic representation
such as a parse tree can be seen as a structured prediction problem in
which the structured output domain is the set of all possible parse
trees. Structured prediction is also used in a wide variety of
application domains including bioinformatics, natural language
processing, speech recognition, and computer vision. Example: sequence
tagging Sequence tagging is a class of problems prevalent in natural
language processing, where input data are often sequences (e.g.
sentences of text). The sequence tagging problem appears in several
guises, e.g. part-of-speech tagging and named entity recognition. In POS
tagging, for example, each word in a sequence must receive a \"tag\"
(class label) that expresses its \"type\" of word: The main challenge of
this problem is to resolve ambiguity: the word \"sentence\" can also be
a verb in English, and so can \"tagged\". While this problem can be
solved by simply performing classification of individual tokens, that
approach does not take into account the empirical fact that tags do not
occur independently; instead, each tag displays a strong conditional
dependence on the tag of the previous word. This fact can be exploited
in a sequence model such as a hidden Markov model or conditional random
field that predicts the entire tag sequence for a sentence, rather than
just individual tags, by means of the Viterbi algorithm. Techniques
Probabilistic graphical models form a large class of structured
prediction models. In particular, Bayesian networks and random fields
are popular. Other algorithms and models for structured prediction
include inductive logic programming, case-based reasoning, structured
SVMs, Markov logic networks, Probabilistic Soft Logic, and constrained
conditional models. Main techniques: Conditional random field Structured
support vector machine Structured k-Nearest Neighbours Recurrent neural
network, in particular Elman network Structured perceptron One of the
easiest ways to understand algorithms for general structured prediction
is the structured perceptron of Collins. This algorithm combines the
perceptron algorithm for learning linear classifiers with an inference
algorithm (classically the Viterbi algorithm when used on sequence data)
and can be described abstractly as follows. First define a \"joint
feature function\" Φ(x, y) that maps a training sample x and a candidate
prediction y to a vector of length n (x and y may have any structure; n
is problem-dependent, but must be fixed for each model). Let GEN be a
function that generates candidate predictions. Then: Let w
{\\displaystyle w} be a weight vector of length nFor a pre-determined
number of iterations:For each sample x {\\displaystyle x} in the
training set with true output t {\\displaystyle t} :Make a prediction y
\^ = a r g m a x { y ∈ G E N ( x ) } ( w T ϕ ( x , y ) ) {\\displaystyle
{\\hat {y}}={\\operatorname {arg\\,max} }\\,\\{{y}\\in
{GEN}({x})\\}\\,({w}\^{T}\\,\\phi ({x},{y}))} Update w {\\displaystyle
w} , from y \^ {\\displaystyle {\\hat {y}}} to t {\\displaystyle t} : w
= w + c ( − ϕ ( x , y \^ ) + ϕ ( x , t ) ) {\\displaystyle
{w}={w}+{c}(-\\phi ({x},{\\hat {y}})+\\phi ({x},{t}))} , c
{\\displaystyle c} is learning rateIn practice, finding the argmax over
G E N ( x ) {\\displaystyle {GEN}({x})} will be done using an algorithm
such as Viterbi or an algorithm such as max-sum, rather than an
exhaustive search through an exponentially large set of candidates. The
idea of learning is similar to multiclass perceptron. References Noah
Smith, Linguistic Structure Prediction, 2011. Michael Collins,
Discriminative Training Methods for Hidden Markov Models, 2002. External
links Implementation of Collins structured perceptron
