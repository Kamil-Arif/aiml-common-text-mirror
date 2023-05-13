Empirical risk minimization (ERM) is a principle in statistical learning
theory which defines a family of learning algorithms and is used to give
theoretical bounds on their performance. The core idea is that we cannot
know exactly how well an algorithm will work in practice (the true
\"risk\") because we don\'t know the true distribution of data that the
algorithm will work on, but we can instead measure its performance on a
known set of training data (the \"empirical\" risk). Background Consider
the following situation, which is a general setting of many supervised
learning problems. We have two spaces of objects X {\\displaystyle X}
and Y {\\displaystyle Y} and would like to learn a function h : X → Y
{\\displaystyle \\ h:X\\to Y} (often called hypothesis) which outputs an
object y ∈ Y {\\displaystyle y\\in Y} , given x ∈ X {\\displaystyle
x\\in X} . To do so, we have at our disposal a training set of n
{\\displaystyle n} examples ( x 1 , y 1 ) , ... , ( x n , y n )
{\\displaystyle \\ (x\_{1},y\_{1}),\\ldots ,(x\_{n},y\_{n})} where x i ∈
X {\\displaystyle x\_{i}\\in X} is an input and y i ∈ Y {\\displaystyle
y\_{i}\\in Y} is the corresponding response that we wish to get from h (
x i ) {\\displaystyle h(x\_{i})} . To put it more formally, we assume
that there is a joint probability distribution P ( x , y )
{\\displaystyle P(x,y)} over X {\\displaystyle X} and Y {\\displaystyle
Y} , and that the training set consists of n {\\displaystyle n}
instances ( x 1 , y 1 ) , ... , ( x n , y n ) {\\displaystyle \\
(x\_{1},y\_{1}),\\ldots ,(x\_{n},y\_{n})} drawn i.i.d. from P ( x , y )
{\\displaystyle P(x,y)} . Note that the assumption of a joint
probability distribution allows us to model uncertainty in predictions
(e.g. from noise in data) because y {\\displaystyle y} is not a
deterministic function of x {\\displaystyle x} , but rather a random
variable with conditional distribution P ( y \| x ) {\\displaystyle
P(y\|x)} for a fixed x {\\displaystyle x} . We also assume that we are
given a non-negative real-valued loss function L ( y \^ , y )
{\\displaystyle L({\\hat {y}},y)} which measures how different the
prediction y \^ {\\displaystyle {\\hat {y}}} of a hypothesis is from the
true outcome y . {\\displaystyle y.} The risk associated with hypothesis
h ( x ) {\\displaystyle h(x)} is then defined as the expectation of the
loss function: R ( h ) = E \[ L ( h ( x ) , y ) \] = ∫ L ( h ( x ) , y )
d P ( x , y ) . {\\displaystyle R(h)=\\mathbf {E} \[L(h(x),y)\]=\\int
L(h(x),y)\\,dP(x,y).} A loss function commonly used in theory is the 0-1
loss function: L ( y \^ , y ) = { 1 if y \^ ≠ y 0 if y \^ = y
{\\displaystyle L({\\hat {y}},y)={\\begin{cases}1&{\\mbox{ if }}\\quad
{\\hat {y}}\\neq y\\\\0&{\\mbox{ if }}\\quad {\\hat {y}}=y\\end{cases}}}
. The ultimate goal of a learning algorithm is to find a hypothesis h ∗
{\\displaystyle h\^{\*}} among a fixed class of functions H
{\\displaystyle {\\mathcal {H}}} for which the risk R ( h )
{\\displaystyle R(h)} is minimal: h ∗ = a r g m i n h ∈ H R ( h ) .
{\\displaystyle h\^{\*}={\\underset {h\\in {\\mathcal
{H}}}{\\operatorname {arg\\,min} }}\\,{R(h)}.} For classification
problems, the Bayes classifier is defined to be the classifier
minimizing the risk defined with the 0--1 loss function. Empirical risk
minimization In general, the risk R ( h ) {\\displaystyle R(h)} cannot
be computed because the distribution P ( x , y ) {\\displaystyle P(x,y)}
is unknown to the learning algorithm (this situation is referred to as
agnostic learning). However, we can compute an approximation, called
empirical risk, by averaging the loss function on the training set; more
formally, computing the expectation with respect to the empirical
measure: R emp ( h ) = 1 n ∑ i = 1 n L ( h ( x i ) , y i ) .
{\\displaystyle \\!R\_{\\text{emp}}(h)={\\frac {1}{n}}\\sum
\_{i=1}\^{n}L(h(x\_{i}),y\_{i}).} The empirical risk minimization
principle states that the learning algorithm should choose a hypothesis
h \^ {\\displaystyle {\\hat {h}}} which minimizes the empirical risk: h
\^ = a r g m i n h ∈ H R emp ( h ) . {\\displaystyle {\\hat
{h}}={\\underset {h\\in {\\mathcal {H}}}{\\operatorname {arg\\,min}
}}\\,R\_{\\text{emp}}(h).} Thus the learning algorithm defined by the
ERM principle consists in solving the above optimization problem.
Properties Computational complexity Empirical risk minimization for a
classification problem with a 0-1 loss function is known to be an
NP-hard problem even for a relatively simple class of functions such as
linear classifiers. Nevertheless, it can be solved efficiently when the
minimal empirical risk is zero, i.e., data is linearly separable. In
practice, machine learning algorithms cope with this issue either by
employing a convex approximation to the 0--1 loss function (like hinge
loss for SVM), which is easier to optimize, or by imposing assumptions
on the distribution P ( x , y ) {\\displaystyle P(x,y)} (and thus stop
being agnostic learning algorithms to which the above result applies).
See also Maximum likelihood estimation M-estimator References Further
reading Vapnik, V. (2000). The Nature of Statistical Learning Theory.
Information Science and Statistics. Springer-Verlag. ISBN
978-0-387-98780-4.
