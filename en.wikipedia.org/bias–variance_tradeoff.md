In statistics and machine learning, the bias--variance tradeoff is the
property of a model that the variance of the parameter estimated across
samples can be reduced by increasing the bias in the estimated
parameters. The bias--variance dilemma or bias--variance problem is the
conflict in trying to simultaneously minimize these two sources of error
that prevent supervised learning algorithms from generalizing beyond
their training set: The bias error is an error from erroneous
assumptions in the learning algorithm. High bias can cause an algorithm
to miss the relevant relations between features and target outputs
(underfitting). The variance is an error from sensitivity to small
fluctuations in the training set. High variance may result from an
algorithm modeling the random noise in the training data
(overfitting).The bias--variance decomposition is a way of analyzing a
learning algorithm\'s expected generalization error with respect to a
particular problem as a sum of three terms, the bias, variance, and a
quantity called the irreducible error, resulting from noise in the
problem itself. Motivation The bias--variance tradeoff is a central
problem in supervised learning. Ideally, one wants to choose a model
that both accurately captures the regularities in its training data, but
also generalizes well to unseen data. Unfortunately, it is typically
impossible to do both simultaneously. High-variance learning methods may
be able to represent their training set well but are at risk of
overfitting to noisy or unrepresentative training data. In contrast,
algorithms with high bias typically produce simpler models that may fail
to capture important regularities (i.e. underfit) in the data. It is an
often made fallacy to assume that complex models must have high
variance; High variance models are \'complex\' in some sense, but the
reverse needs not be true. In addition, one has to be careful how to
define complexity: In particular, the number of parameters used to
describe the model is a poor measure of complexity. This is illustrated
by an example adapted from: The model f a , b ( x ) = a sin ⁡ ( b x )
{\\displaystyle f\_{a,b}(x)=a\\sin(bx)} has only two parameters ( a , b
{\\displaystyle a,b} ) but it can interpolate any number of points by
oscillating with a high enough frequency, resulting in both a high bias
and high variance. An analogy can be made to the relationship between
accuracy and precision. Accuracy is a description of bias and can
intuitively be improved by selecting from only local information.
Consequently, a sample will appear accurate (i.e. have low bias) under
the aforementioned selection conditions, but may result in underfitting.
In other words, test data may not agree as closely with training data,
which would indicate imprecision and therefore inflated variance. A
graphical example would be a straight line fit to data exhibiting
quadratic behavior overall. Precision is a description of variance and
generally can only be improved by selecting information from a
comparatively larger space. The option to select many data points over a
broad sample space is the ideal condition for any analysis. However,
intrinsic constraints (whether physical, theoretical, computational,
etc.) will always play a limiting role. The limiting case where only a
finite number of data points are selected over a broad sample space may
result in improved precision and lower variance overall, but may also
result in an overreliance on the training data (overfitting). This means
that test data would also not agree as closely with the training data,
but in this case the reason is due to inaccuracy or high bias. To borrow
from the previous example, the graphical representation would appear as
a high-order polynomial fit to the same data exhibiting quadratic
behavior. Note that error in each case is measured the same way, but the
reason ascribed to the error is different depending on the balance
between bias and variance. To mitigate how much information is used from
neighboring observations, a model can be smoothed via explicit
regularization, such as shrinkage. Bias--variance decomposition of mean
squared error Suppose that we have a training set consisting of a set of
points x 1 , ... , x n {\\displaystyle x\_{1},\\dots ,x\_{n}} and real
values y i {\\displaystyle y\_{i}} associated with each point x i
{\\displaystyle x\_{i}} . We assume that there is a function f(x) such
as y = f ( x ) + ε {\\displaystyle y=f(x)+\\varepsilon } , where the
noise, ε {\\displaystyle \\varepsilon } , has zero mean and variance σ 2
{\\displaystyle \\sigma \^{2}} . We want to find a function f \^ ( x ; D
) {\\displaystyle {\\hat {f}}(x;D)} , that approximates the true
function f ( x ) {\\displaystyle f(x)} as well as possible, by means of
some learning algorithm based on a training dataset (sample) D = { ( x 1
, y 1 ) ... , ( x n , y n ) } {\\displaystyle D=\\{(x\_{1},y\_{1})\\dots
,(x\_{n},y\_{n})\\}} . We make \"as well as possible\" precise by
measuring the mean squared error between y {\\displaystyle y} and f \^ (
x ; D ) {\\displaystyle {\\hat {f}}(x;D)} : we want ( y − f \^ ( x ; D )
) 2 {\\displaystyle (y-{\\hat {f}}(x;D))\^{2}} to be minimal, both for x
1 , ... , x n {\\displaystyle x\_{1},\\dots ,x\_{n}} and for points
outside of our sample. Of course, we cannot hope to do so perfectly,
since the y i {\\displaystyle y\_{i}} contain noise ε {\\displaystyle
\\varepsilon } ; this means we must be prepared to accept an irreducible
error in any function we come up with. Finding an f \^ {\\displaystyle
{\\hat {f}}} that generalizes to points outside of the training set can
be done with any of the countless algorithms used for supervised
learning. It turns out that whichever function f \^ {\\displaystyle
{\\hat {f}}} we select, we can decompose its expected error on an unseen
sample x {\\displaystyle x} as follows:: 34 : 223  E D , ε ⁡ \[ ( y − f
\^ ( x ; D ) ) 2 \] = ( Bias D ⁡ \[ f \^ ( x ; D ) \] ) 2 + Var D ⁡ \[ f
\^ ( x ; D ) \] + σ 2 {\\displaystyle \\operatorname {E}
\_{D,\\varepsilon }{\\Big \[}{\\big (}y-{\\hat {f}}(x;D){\\big
)}\^{2}{\\Big \]}={\\Big (}\\operatorname {Bias} \_{D}{\\big \[}{\\hat
{f}}(x;D){\\big \]}{\\Big )}\^{2}+\\operatorname {Var} \_{D}{\\big
\[}{\\hat {f}}(x;D){\\big \]}+\\sigma \^{2}} where Bias D ⁡ \[ f \^ ( x ;
D ) \] = E D ⁡ \[ f \^ ( x ; D ) − f ( x ) \] = E D ⁡ \[ f \^ ( x ; D ) \]
− E ⁡ \[ y ( x ) \] {\\displaystyle \\operatorname {Bias} \_{D}{\\big
\[}{\\hat {f}}(x;D){\\big \]}=\\operatorname {E} \_{D}{\\big \[}{\\hat
{f}}(x;D)-f(x){\\big \]}=\\operatorname {E} \_{D}{\\big \[}{\\hat
{f}}(x;D){\\big \]}-\\operatorname {E} {\\big \[}y(x){\\big \]}} and Var
D ⁡ \[ f \^ ( x ; D ) \] = E D ⁡ \[ ( E D ⁡ \[ f \^ ( x ; D ) \] − f \^ ( x
; D ) ) 2 \] . {\\displaystyle \\operatorname {Var} \_{D}{\\big
\[}{\\hat {f}}(x;D){\\big \]}=\\operatorname {E} \_{D}\[{\\big
(}\\operatorname {E} \_{D}\[{\\hat {f}}(x;D)\]-{\\hat {f}}(x;D){\\big
)}\^{2}\].} The expectation ranges over different choices of the
training set D = { ( x 1 , y 1 ) ... , ( x n , y n ) } {\\displaystyle
D=\\{(x\_{1},y\_{1})\\dots ,(x\_{n},y\_{n})\\}} , all sampled from the
same joint distribution P ( x , y ) {\\displaystyle P(x,y)} which can
for example be done via bootstrapping. The three terms represent: the
square of the bias of the learning method, which can be thought of as
the error caused by the simplifying assumptions built into the method.
E.g., when approximating a non-linear function f ( x ) {\\displaystyle
f(x)} using a learning method for linear models, there will be error in
the estimates f \^ ( x ) {\\displaystyle {\\hat {f}}(x)} due to this
assumption; the variance of the learning method, or, intuitively, how
much the learning method f \^ ( x ) {\\displaystyle {\\hat {f}}(x)} will
move around its mean; the irreducible error σ 2 {\\displaystyle \\sigma
\^{2}} .Since all three terms are non-negative, the irreducible error
forms a lower bound on the expected error on unseen samples.: 34 The
more complex the model f \^ ( x ) {\\displaystyle {\\hat {f}}(x)} is,
the more data points it will capture, and the lower the bias will be.
However, complexity will make the model \"move\" more to capture the
data points, and hence its variance will be larger. Derivation The
derivation of the bias--variance decomposition for squared error
proceeds as follows. For notational convenience, we abbreviate f = f ( x
) {\\displaystyle f=f(x)} , f \^ = f \^ ( x ; D ) {\\displaystyle {\\hat
{f}}={\\hat {f}}(x;D)} and we drop the D {\\displaystyle D} subscript on
our expectation operators. Let us write the mean-squared error of our
model: MSE ≜ E ⁡ \[ ( y − f \^ ) 2 \] = E ⁡ \[ y 2 − 2 y f \^ + f \^ 2 \]
= E ⁡ \[ y 2 \] − 2 E ⁡ \[ y f \^ \] + E ⁡ \[ f \^ 2 \] {\\displaystyle
{\\text{MSE}}\\triangleq \\operatorname {E} {\\big \[}(y-{\\hat
{f}})\^{2}{\\big \]}=\\operatorname {E} {\\big \[}y\^{2}-2y{\\hat
{f}}+{\\hat {f}}\^{2}{\\big \]}=\\operatorname {E} {\\big
\[}y\^{2}{\\big \]}-2\\operatorname {E} {\\big \[}y{\\hat {f}}{\\big
\]}+\\operatorname {E} {\\big \[}{\\hat {f}}\^{2}{\\big \]}} First, E ⁡
\[ f \^ 2 \] = Var ⁡ ( f \^ ) + E ⁡ \[ f \^ \] 2 since Var ⁡ \[ X \] ≜ E ⁡
\[ ( X − E ⁡ \[ X \] ) 2 \] = E ⁡ \[ X 2 \] − E ⁡ \[ X \] 2 for any random
variable X {\\displaystyle {\\begin{aligned}\\operatorname {E} {\\big
\[}{\\hat {f}}\^{2}{\\big \]}&=\\operatorname {Var} ({\\hat
{f}})+\\operatorname {E} \[{\\hat {f}}\]\^{2}&&{\\text{since
}}\\operatorname {Var} \[X\]\\triangleq \\operatorname {E} {\\Big
\[}(X-\\operatorname {E} \[X\])\^{2}{\\Big \]}=\\operatorname {E}
\[X\^{2}\]-\\operatorname {E} \[X\]\^{2}{\\text{ for any random variable
}}X\\end{aligned}}} Secondly, since we model y = f + ε {\\displaystyle
y=f+\\varepsilon } , we show that E ⁡ \[ y 2 \] = E ⁡ \[ ( f + ε ) 2 \] =
E ⁡ \[ f 2 \] + 2 E ⁡ \[ f ε \] + E ⁡ \[ ε 2 \] by linearity of E = f 2 + 2
f E ⁡ \[ ε \] + E ⁡ \[ ε 2 \] since f does not depend on the data = f 2 +
2 f ⋅ 0 + σ 2 since ε has zero mean and variance σ 2 {\\displaystyle
{\\begin{aligned}\\operatorname {E} {\\big \[}y\^{2}{\\big
\]}&=\\operatorname {E} {\\big \[}(f+\\varepsilon )\^{2}{\\big
\]}\\\\&=\\operatorname {E} \[f\^{2}\]+2\\operatorname {E}
\[f\\varepsilon \]+\\operatorname {E} \[\\varepsilon \^{2}\]&&{\\text{by
linearity of }}\\operatorname {E} \\\\&=f\^{2}+2f\\operatorname {E}
\[\\varepsilon \]+\\operatorname {E} \[\\varepsilon
\^{2}\]&&{\\text{since }}f{\\text{ does not depend on the
data}}\\\\&=f\^{2}+2f\\cdot 0+\\sigma \^{2}&&{\\text{since
}}\\varepsilon {\\text{ has zero mean and variance }}\\sigma
\^{2}\\end{aligned}}} Lastly, E ⁡ \[ y f \^ \] = E ⁡ \[ ( f + ε ) f \^ \]
= E ⁡ \[ f f \^ \] + E ⁡ \[ ε f \^ \] by linearity of E = E ⁡ \[ f f \^
\] + E ⁡ \[ ε \] E ⁡ \[ f \^ \] since f \^ and ε are independent = f E ⁡ \[
f \^ \] since E ⁡ \[ ε \] = 0 {\\displaystyle
{\\begin{aligned}\\operatorname {E} {\\big \[}y{\\hat {f}}{\\big
\]}&=\\operatorname {E} {\\big \[}(f+\\varepsilon ){\\hat {f}}{\\big
\]}\\\\&=\\operatorname {E} \[f{\\hat {f}}\]+\\operatorname {E}
\[\\varepsilon {\\hat {f}}\]&&{\\text{by linearity of }}\\operatorname
{E} \\\\&=\\operatorname {E} \[f{\\hat {f}}\]+\\operatorname {E}
\[\\varepsilon \]\\operatorname {E} \[{\\hat {f}}\]&&{\\text{since
}}{\\hat {f}}{\\text{ and }}\\varepsilon {\\text{ are
independent}}\\\\&=f\\operatorname {E} \[{\\hat {f}}\]&&{\\text{since
}}\\operatorname {E} \[\\varepsilon \]=0\\end{aligned}}} Eventually, we
plug these 3 formulas in our previous derivation of MSE {\\displaystyle
{\\text{MSE}}} and thus show that: MSE = f 2 + σ 2 − 2 f E ⁡ \[ f \^ \] +
Var ⁡ \[ f \^ \] + E ⁡ \[ f \^ \] 2 = ( f − E ⁡ \[ f \^ \] ) 2 + σ 2 + Var ⁡
\[ f \^ \] = Bias ⁡ \[ f \^ \] 2 + σ 2 + Var ⁡ \[ f \^ \] {\\displaystyle
{\\begin{aligned}{\\text{MSE}}&=f\^{2}+\\sigma \^{2}-2f\\operatorname
{E} \[{\\hat {f}}\]+\\operatorname {Var} \[{\\hat {f}}\]+\\operatorname
{E} \[{\\hat {f}}\]\^{2}\\\\&=(f-\\operatorname {E} \[{\\hat
{f}}\])\^{2}+\\sigma \^{2}+\\operatorname {Var} {\\big \[}{\\hat
{f}}{\\big \]}\\\\\[5pt\]&=\\operatorname {Bias} \[{\\hat
{f}}\]\^{2}+\\sigma \^{2}+\\operatorname {Var} {\\big \[}{\\hat
{f}}{\\big \]}\\end{aligned}}} Finally, MSE loss function (or negative
log-likelihood) is obtained by taking the expectation value over x ∼ P
{\\displaystyle x\\sim P} : MSE = E x ⁡ { Bias D ⁡ \[ f \^ ( x ; D ) \]
2 + Var D ⁡ \[ f \^ ( x ; D ) \] } + σ 2 . {\\displaystyle
{\\text{MSE}}=\\operatorname {E} \_{x}{\\bigg \\{}\\operatorname {Bias}
\_{D}\[{\\hat {f}}(x;D)\]\^{2}+\\operatorname {Var} \_{D}{\\big
\[}{\\hat {f}}(x;D){\\big \]}{\\bigg \\}}+\\sigma \^{2}.} Approaches
Dimensionality reduction and feature selection can decrease variance by
simplifying models. Similarly, a larger training set tends to decrease
variance. Adding features (predictors) tends to decrease bias, at the
expense of introducing additional variance. Learning algorithms
typically have some tunable parameters that control bias and variance;
for example, linear and Generalized linear models can be regularized to
decrease their variance at the cost of increasing their bias. In
artificial neural networks, the variance increases and the bias
decreases as the number of hidden units increase, although this
classical assumption has been the subject of recent debate. Like in
GLMs, regularization is typically applied. In k-nearest neighbor models,
a high value of k leads to high bias and low variance (see below). In
instance-based learning, regularization can be achieved varying the
mixture of prototypes and exemplars. In decision trees, the depth of the
tree determines the variance. Decision trees are commonly pruned to
control variance.: 307 One way of resolving the trade-off is to use
mixture models and ensemble learning. For example, boosting combines
many \"weak\" (high bias) models in an ensemble that has lower bias than
the individual models, while bagging combines \"strong\" learners in a
way that reduces their variance. Model validation methods such as
cross-validation (statistics) can be used to tune models so as to
optimize the trade-off. k-nearest neighbors In the case of k-nearest
neighbors regression, when the expectation is taken over the possible
labeling of a fixed training set, a closed-form expression exists that
relates the bias--variance decomposition to the parameter k:: 37, 223  E
⁡\[ ( y − f \^ ( x ) ) 2 ∣ X = x \] = ( f ( x ) − 1 k ∑ i = 1 k f ( N i (
x ) ) ) 2 + σ 2 k + σ 2 {\\displaystyle \\operatorname {E} \[(y-{\\hat
{f}}(x))\^{2}\\mid X=x\]=\\left(f(x)-{\\frac {1}{k}}\\sum
\_{i=1}\^{k}f(N\_{i}(x))\\right)\^{2}+{\\frac {\\sigma
\^{2}}{k}}+\\sigma \^{2}} where N 1 ( x ) , ... , N k ( x )
{\\displaystyle N\_{1}(x),\\dots ,N\_{k}(x)} are the k nearest neighbors
of x in the training set. The bias (first term) is a monotone rising
function of k, while the variance (second term) drops off as k is
increased. In fact, under \"reasonable assumptions\" the bias of the
first-nearest neighbor (1-NN) estimator vanishes entirely as the size of
the training set approaches infinity. Applications In regression The
bias--variance decomposition forms the conceptual basis for regression
regularization methods such as Lasso and ridge regression.
Regularization methods introduce bias into the regression solution that
can reduce variance considerably relative to the ordinary least squares
(OLS) solution. Although the OLS solution provides non-biased regression
estimates, the lower variance solutions produced by regularization
techniques provide superior MSE performance. In classification The
bias--variance decomposition was originally formulated for least-squares
regression. For the case of classification under the 0-1 loss
(misclassification rate), it is possible to find a similar
decomposition. Alternatively, if the classification problem can be
phrased as probabilistic classification, then the expected squared error
of the predicted probabilities with respect to the true probabilities
can be decomposed as before.It has been argued that as training data
increases, the variance of learned models will tend to decrease, and
hence that as training data quantity increases, error is minimized by
methods that learn models with lesser bias, and that conversely, for
smaller training data quantities it is ever more important to minimize
variance. In reinforcement learning Even though the bias--variance
decomposition does not directly apply in reinforcement learning, a
similar tradeoff can also characterize generalization. When an agent has
limited information on its environment, the suboptimality of an RL
algorithm can be decomposed into the sum of two terms: a term related to
an asymptotic bias and a term due to overfitting. The asymptotic bias is
directly related to the learning algorithm (independently of the
quantity of data) while the overfitting term comes from the fact that
the amount of data is limited. In human learning While widely discussed
in the context of machine learning, the bias--variance dilemma has been
examined in the context of human cognition, most notably by Gerd
Gigerenzer and co-workers in the context of learned heuristics. They
have argued (see references below) that the human brain resolves the
dilemma in the case of the typically sparse, poorly-characterised
training-sets provided by experience by adopting high-bias/low variance
heuristics. This reflects the fact that a zero-bias approach has poor
generalisability to new situations, and also unreasonably presumes
precise knowledge of the true state of the world. The resulting
heuristics are relatively simple, but produce better inferences in a
wider variety of situations.Geman et al. argue that the bias--variance
dilemma implies that abilities such as generic object recognition cannot
be learned from scratch, but require a certain degree of \"hard wiring\"
that is later tuned by experience. This is because model-free approaches
to inference require impractically large training sets if they are to
avoid high variance. See also References External links MLU-Explain: The
Bias Variance Tradeoff --- An interactive visualization of the
bias-variance tradeoff in LOESS Regression and K-Nearest Neighbors.
