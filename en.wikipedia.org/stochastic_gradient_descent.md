Stochastic gradient descent (often abbreviated SGD) is an iterative
method for optimizing an objective function with suitable smoothness
properties (e.g. differentiable or subdifferentiable). It can be
regarded as a stochastic approximation of gradient descent optimization,
since it replaces the actual gradient (calculated from the entire data
set) by an estimate thereof (calculated from a randomly selected subset
of the data). Especially in high-dimensional optimization problems this
reduces the very high computational burden, achieving faster iterations
in exchange for a lower convergence rate.While the basic idea behind
stochastic approximation can be traced back to the Robbins--Monro
algorithm of the 1950s, stochastic gradient descent has become an
important optimization method in machine learning. Background Both
statistical estimation and machine learning consider the problem of
minimizing an objective function that has the form of a sum: Q ( w ) = 1
n ∑ i = 1 n Q i ( w ) , {\\displaystyle Q(w)={\\frac {1}{n}}\\sum
\_{i=1}\^{n}Q\_{i}(w),} where the parameter w {\\displaystyle w} that
minimizes Q ( w ) {\\displaystyle Q(w)} is to be estimated. Each summand
function Q i {\\displaystyle Q\_{i}} is typically associated with the i
{\\displaystyle i} -th observation in the data set (used for training).
In classical statistics, sum-minimization problems arise in least
squares and in maximum-likelihood estimation (for independent
observations). The general class of estimators that arise as minimizers
of sums are called M-estimators. However, in statistics, it has been
long recognized that requiring even local minimization is too
restrictive for some problems of maximum-likelihood estimation.
Therefore, contemporary statistical theorists often consider stationary
points of the likelihood function (or zeros of its derivative, the score
function, and other estimating equations). The sum-minimization problem
also arises for empirical risk minimization. In this case, Q i ( w )
{\\displaystyle Q\_{i}(w)} is the value of the loss function at i
{\\displaystyle i} -th example, and Q ( w ) {\\displaystyle Q(w)} is the
empirical risk. When used to minimize the above function, a standard (or
\"batch\") gradient descent method would perform the following
iterations: w := w − η ∇ Q ( w ) = w − η n ∑ i = 1 n ∇ Q i ( w ) ,
{\\displaystyle w:=w-\\eta \\nabla Q(w)=w-{\\frac {\\eta }{n}}\\sum
\_{i=1}\^{n}\\nabla Q\_{i}(w),} where η {\\displaystyle \\eta } is a
step size (sometimes called the learning rate in machine learning). In
many cases, the summand functions have a simple form that enables
inexpensive evaluations of the sum-function and the sum gradient. For
example, in statistics, one-parameter exponential families allow
economical function-evaluations and gradient-evaluations. However, in
other cases, evaluating the sum-gradient may require expensive
evaluations of the gradients from all summand functions. When the
training set is enormous and no simple formulas exist, evaluating the
sums of gradients becomes very expensive, because evaluating the
gradient requires evaluating all the summand functions\' gradients. To
economize on the computational cost at every iteration, stochastic
gradient descent samples a subset of summand functions at every step.
This is very effective in the case of large-scale machine learning
problems. Iterative method In stochastic (or \"on-line\") gradient
descent, the true gradient of Q ( w ) {\\displaystyle Q(w)} is
approximated by a gradient at a single sample: w := w − η ∇ Q i ( w ) .
{\\displaystyle w:=w-\\eta \\nabla Q\_{i}(w).} As the algorithm sweeps
through the training set, it performs the above update for each training
sample. Several passes can be made over the training set until the
algorithm converges. If this is done, the data can be shuffled for each
pass to prevent cycles. Typical implementations may use an adaptive
learning rate so that the algorithm converges.In pseudocode, stochastic
gradient descent can be presented as : A compromise between computing
the true gradient and the gradient at a single sample is to compute the
gradient against more than one training sample (called a \"mini-batch\")
at each step. This can perform significantly better than \"true\"
stochastic gradient descent described, because the code can make use of
vectorization libraries rather than computing each step separately as
was first shown in where it was called \"the bunch-mode back-propagation
algorithm\". It may also result in smoother convergence, as the gradient
computed at each step is averaged over more training sample. The
convergence of stochastic gradient descent has been analyzed using the
theories of convex minimization and of stochastic approximation.
Briefly, when the learning rates η {\\displaystyle \\eta } decrease with
an appropriate rate, and subject to relatively mild assumptions,
stochastic gradient descent converges almost surely to a global minimum
when the objective function is convex or pseudoconvex, and otherwise
converges almost surely to a local minimum. This is in fact a
consequence of the Robbins--Siegmund theorem. Example Suppose we want to
fit a straight line y \^ = w 1 + w 2 x {\\displaystyle {\\hat
{y}}=\\!w\_{1}+w\_{2}x} to a training set with observations ( x 1 , x 2
, ... , x n ) {\\displaystyle (x\_{1},x\_{2},\\ldots ,x\_{n})} and
corresponding estimated responses ( y 1 \^ , y 2 \^ , ... , y n \^ )
{\\displaystyle ({\\hat {y\_{1}}},{\\hat {y\_{2}}},\\ldots ,{\\hat
{y\_{n}}})} using least squares. The objective function to be minimized
is: Q ( w ) = ∑ i = 1 n Q i ( w ) = ∑ i = 1 n ( y i \^ − y i ) 2 = ∑ i =
1 n ( w 1 + w 2 x i − y i ) 2 . {\\displaystyle Q(w)=\\sum
\_{i=1}\^{n}Q\_{i}(w)=\\sum \_{i=1}\^{n}\\left({\\hat
{y\_{i}}}-y\_{i}\\right)\^{2}=\\sum
\_{i=1}\^{n}\\left(w\_{1}+w\_{2}x\_{i}-y\_{i}\\right)\^{2}.} The last
line in the above pseudocode for this specific problem will become: \[ w
1 w 2 \] := \[ w 1 w 2 \] − η \[ ∂ ∂ w 1 ( w 1 + w 2 x i − y i ) 2 ∂ ∂ w
2 ( w 1 + w 2 x i − y i ) 2 \] = \[ w 1 w 2 \] − η \[ 2 ( w 1 + w 2 x i
− y i ) 2 x i ( w 1 + w 2 x i − y i ) \] . {\\displaystyle
{\\begin{bmatrix}w\_{1}\\\\w\_{2}\\end{bmatrix}}:={\\begin{bmatrix}w\_{1}\\\\w\_{2}\\end{bmatrix}}-\\eta
{\\begin{bmatrix}{\\frac {\\partial }{\\partial
w\_{1}}}(w\_{1}+w\_{2}x\_{i}-y\_{i})\^{2}\\\\{\\frac {\\partial
}{\\partial
w\_{2}}}(w\_{1}+w\_{2}x\_{i}-y\_{i})\^{2}\\end{bmatrix}}={\\begin{bmatrix}w\_{1}\\\\w\_{2}\\end{bmatrix}}-\\eta
{\\begin{bmatrix}2(w\_{1}+w\_{2}x\_{i}-y\_{i})\\\\2x\_{i}(w\_{1}+w\_{2}x\_{i}-y\_{i})\\end{bmatrix}}.}
Note that in each iteration (also called update), the gradient is only
evaluated at a single point x i {\\displaystyle x\_{i}} instead of at
the set of all samples. The key difference compared to standard (Batch)
Gradient Descent is that only one piece of data from the dataset is used
to calculate the step, and the piece of data is picked randomly at each
step. Notable applications Stochastic gradient descent is a popular
algorithm for training a wide range of models in machine learning,
including (linear) support vector machines, logistic regression (see,
e.g., Vowpal Wabbit) and graphical models. When combined with the
backpropagation algorithm, it is the de facto standard algorithm for
training artificial neural networks. Its use has been also reported in
the Geophysics community, specifically to applications of Full Waveform
Inversion (FWI).Stochastic gradient descent competes with the L-BFGS
algorithm, which is also widely used. Stochastic gradient descent has
been used since at least 1960 for training linear regression models,
originally under the name ADALINE.Another stochastic gradient descent
algorithm is the least mean squares (LMS) adaptive filter. Extensions
and variants Many improvements on the basic stochastic gradient descent
algorithm have been proposed and used. In particular, in machine
learning, the need to set a learning rate (step size) has been
recognized as problematic. Setting this parameter too high can cause the
algorithm to diverge; setting it too low makes it slow to converge. A
conceptually simple extension of stochastic gradient descent makes the
learning rate a decreasing function ηt of the iteration number t, giving
a learning rate schedule, so that the first iterations cause large
changes in the parameters, while the later ones do only fine-tuning.
Such schedules have been known since the work of MacQueen on k-means
clustering. Practical guidance on choosing the step size in several
variants of SGD is given by Spall. Implicit updates (ISGD) As mentioned
earlier, classical stochastic gradient descent is generally sensitive to
learning rate η. Fast convergence requires large learning rates but this
may induce numerical instability. The problem can be largely solved by
considering implicit updates whereby the stochastic gradient is
evaluated at the next iterate rather than the current one: w n e w := w
o l d − η ∇ Q i ( w n e w ) . {\\displaystyle w\^{\\rm {new}}:=w\^{\\rm
{old}}-\\eta \\nabla Q\_{i}(w\^{\\rm {new}}).} This equation is implicit
since w n e w {\\displaystyle w\^{\\rm {new}}} appears on both sides of
the equation. It is a stochastic form of the proximal gradient method
since the update can also be written as: w n e w := arg ⁡ min w { Q i ( w
) + 1 2 η \| \| w − w o l d \| \| 2 } . {\\displaystyle w\^{\\rm
{new}}:=\\arg \\min \_{w}\\{Q\_{i}(w)+{\\frac {1}{2\\eta
}}\|\|w-w\^{\\rm {old}}\|\|\^{2}\\}.} As an example, consider least
squares with features x 1 , ... , x n ∈ R p {\\displaystyle
x\_{1},\\ldots ,x\_{n}\\in \\mathbb {R} \^{p}} and observations y 1 ,
... , y n ∈ R {\\displaystyle y\_{1},\\ldots ,y\_{n}\\in \\mathbb {R} }
. We wish to solve: min w ∑ j = 1 n ( y j − x j ′ w ) 2 ,
{\\displaystyle \\min \_{w}\\sum \_{j=1}\^{n}(y\_{j}-x\_{j}\'w)\^{2},}
where x j ′ w = x j 1 w 1 + x j , 2 w 2 + . . . + x j , p w p
{\\displaystyle
x\_{j}\'w=x\_{j1}w\_{1}+x\_{j,2}w\_{2}+\...+x\_{j,p}w\_{p}} indicates
the inner product. Note that x {\\displaystyle x} could have \"1\" as
the first element to include an intercept. Classical stochastic gradient
descent proceeds as follows: w n e w = w o l d + η ( y i − x i ′ w o l d
) x i {\\displaystyle w\^{\\rm {new}}=w\^{\\rm {old}}+\\eta
(y\_{i}-x\_{i}\'w\^{\\rm {old}})x\_{i}} where i {\\displaystyle i} is
uniformly sampled between 1 and n {\\displaystyle n} . Although
theoretical convergence of this procedure happens under relatively mild
assumptions, in practice the procedure can be quite unstable. In
particular, when η {\\displaystyle \\eta } is misspecified so that I − η
x i x i ′ {\\displaystyle I-\\eta x\_{i}x\_{i}\'} has large absolute
eigenvalues with high probability, the procedure may diverge numerically
within a few iterations. In contrast, implicit stochastic gradient
descent (shortened as ISGD) can be solved in closed-form as: w n e w = w
o l d + η 1 + η \| \| x i \| \| 2 ( y i − x i ′ w o l d ) x i .
{\\displaystyle w\^{\\rm {new}}=w\^{\\rm {old}}+{\\frac {\\eta }{1+\\eta
\|\|x\_{i}\|\|\^{2}}}(y\_{i}-x\_{i}\'w\^{\\rm {old}})x\_{i}.} This
procedure will remain numerically stable virtually for all η
{\\displaystyle \\eta } as the learning rate is now normalized. Such
comparison between classical and implicit stochastic gradient descent in
the least squares problem is very similar to the comparison between
least mean squares (LMS) and normalized least mean squares filter
(NLMS). Even though a closed-form solution for ISGD is only possible in
least squares, the procedure can be efficiently implemented in a wide
range of models. Specifically, suppose that Q i ( w ) {\\displaystyle
Q\_{i}(w)} depends on w {\\displaystyle w} only through a linear
combination with features x i {\\displaystyle x\_{i}} , so that we can
write ∇ w Q i ( w ) = − q ( x i ′ w ) x i {\\displaystyle \\nabla
\_{w}Q\_{i}(w)=-q(x\_{i}\'w)x\_{i}} , where q ( ) ∈ R {\\displaystyle
q()\\in \\mathbb {R} } may depend on x i , y i {\\displaystyle
x\_{i},y\_{i}} as well but not on w {\\displaystyle w} except through x
i ′ w {\\displaystyle x\_{i}\'w} . Least squares obeys this rule, and so
does logistic regression, and most generalized linear models. For
instance, in least squares, q ( x i ′ w ) = y i − x i ′ w
{\\displaystyle q(x\_{i}\'w)=y\_{i}-x\_{i}\'w} , and in logistic
regression q ( x i ′ w ) = y i − S ( x i ′ w ) {\\displaystyle
q(x\_{i}\'w)=y\_{i}-S(x\_{i}\'w)} , where S ( u ) = e u / ( 1 + e u )
{\\displaystyle S(u)=e\^{u}/(1+e\^{u})} is the logistic function. In
Poisson regression, q ( x i ′ w ) = y i − e x i ′ w {\\displaystyle
q(x\_{i}\'w)=y\_{i}-e\^{x\_{i}\'w}} , and so on. In such settings, ISGD
is simply implemented as follows. Let f ( ξ ) = η q ( x i ′ w o l d + ξ
\| \| x i \| \| 2 ) {\\displaystyle f(\\xi )=\\eta
q(x\_{i}\'w\^{old}+\\xi \|\|x\_{i}\|\|\^{2})} , where ξ {\\displaystyle
\\xi } is scalar. Then, ISGD is equivalent to: w n e w = w o l d + ξ ∗ x
i , where ξ ∗ = f ( ξ ∗ ) . {\\displaystyle w\^{\\rm {new}}=w\^{\\rm
{old}}+\\xi \^{\\ast }x\_{i},\~{\\text{where}}\~\\xi \^{\\ast }=f(\\xi
\^{\\ast }).} The scaling factor ξ ∗ ∈ R {\\displaystyle \\xi \^{\\ast
}\\in \\mathbb {R} } can be found through the bisection method since in
most regular models, such as the aforementioned generalized linear
models, function q ( ) {\\displaystyle q()} is decreasing, and thus the
search bounds for ξ ∗ {\\displaystyle \\xi \^{\\ast }} are \[ min ( 0 ,
f ( 0 ) ) , max ( 0 , f ( 0 ) ) \] {\\displaystyle
\[\\min(0,f(0)),\\max(0,f(0))\]} . Momentum Further proposals include
the momentum method or the heavy ball method, which in ML context
appeared in Rumelhart, Hinton and Williams\' paper on backpropagation
learning and borrowed the idea from Soviet mathematician Boris Polyak\'s
1964 article on solving functional equations. Stochastic gradient
descent with momentum remembers the update Δw at each iteration, and
determines the next update as a linear combination of the gradient and
the previous update: Δ w := α Δ w − η ∇ Q i ( w ) {\\displaystyle
\\Delta w:=\\alpha \\Delta w-\\eta \\nabla Q\_{i}(w)} w := w + Δ w
{\\displaystyle w:=w+\\Delta w} that leads to: w := w − η ∇ Q i ( w ) +
α Δ w {\\displaystyle w:=w-\\eta \\nabla Q\_{i}(w)+\\alpha \\Delta w}
where the parameter w {\\displaystyle w} which minimizes Q ( w )
{\\displaystyle Q(w)} is to be estimated, η {\\displaystyle \\eta } is a
step size (sometimes called the learning rate in machine learning) and α
{\\displaystyle \\alpha } is an exponential decay factor between 0 and 1
that determines the relative contribution of the current gradient and
earlier gradients to the weight change. The name momentum stems from an
analogy to momentum in physics: the weight vector w {\\displaystyle w} ,
thought of as a particle traveling through parameter space, incurs
acceleration from the gradient of the loss (\"force\"). Unlike in
classical stochastic gradient descent, it tends to keep traveling in the
same direction, preventing oscillations. Momentum has been used
successfully by computer scientists in the training of artificial neural
networks for several decades. The momentum method is closely related to
underdamped Langevin dynamics, and may be combined with Simulated
Annealing. In mid-1980s the method was modified by Yurii Nesterov to use
the gradient predicted at the next point, and the resulting so-called
Nesterov Accelerated Gradient was sometimes used in ML in the 2010s.
Averaging Averaged stochastic gradient descent, invented independently
by Ruppert and Polyak in the late 1980s, is ordinary stochastic gradient
descent that records an average of its parameter vector over time. That
is, the update is the same as for ordinary stochastic gradient descent,
but the algorithm also keeps track of w ¯ = 1 t ∑ i = 0 t − 1 w i
{\\displaystyle {\\bar {w}}={\\frac {1}{t}}\\sum \_{i=0}\^{t-1}w\_{i}}
.When optimization is done, this averaged parameter vector takes the
place of w. AdaGrad AdaGrad (for adaptive gradient algorithm) is a
modified stochastic gradient descent algorithm with per-parameter
learning rate, first published in 2011. Informally, this increases the
learning rate for sparser parameters and decreases the learning rate for
ones that are less sparse. This strategy often improves convergence
performance over standard stochastic gradient descent in settings where
data is sparse and sparse parameters are more informative. Examples of
such applications include natural language processing and image
recognition.It still has a base learning rate η, but this is multiplied
with the elements of a vector {Gj,j} which is the diagonal of the outer
product matrix G = ∑ τ = 1 t g τ g τ T {\\displaystyle G=\\sum \_{\\tau
=1}\^{t}g\_{\\tau }g\_{\\tau }\^{\\mathsf {T}}} where g τ = ∇ Q i ( w )
{\\displaystyle g\_{\\tau }=\\nabla Q\_{i}(w)} , the gradient, at
iteration τ. The diagonal is given by G j , j = ∑ τ = 1 t g τ , j 2
{\\displaystyle G\_{j,j}=\\sum \_{\\tau =1}\^{t}g\_{\\tau ,j}\^{2}}
.This vector essentially stores a historical sum of gradient squares by
dimension and is updated after every iteration. The formula for an
update is now w := w − η d i a g ( G ) − 1 2 ⊙ g {\\displaystyle
w:=w-\\eta \\,\\mathrm {diag} (G)\^{-{\\frac {1}{2}}}\\odot g} or,
written as per-parameter updates, w j := w j − η G j , j g j .
{\\displaystyle w\_{j}:=w\_{j}-{\\frac {\\eta }{\\sqrt
{G\_{j,j}}}}g\_{j}.} Each {G(i,i)} gives rise to a scaling factor for
the learning rate that applies to a single parameter wi. Since the
denominator in this factor, G i = ∑ τ = 1 t g τ 2 {\\displaystyle
{\\sqrt {G\_{i}}}={\\sqrt {\\sum \_{\\tau =1}\^{t}g\_{\\tau }\^{2}}}} is
the ℓ2 norm of previous derivatives, extreme parameter updates get
dampened, while parameters that get few or small updates receive higher
learning rates.While designed for convex problems, AdaGrad has been
successfully applied to non-convex optimization. RMSProp RMSProp (for
Root Mean Square Propagation) is a method invented by Geoffrey Hinton in
2012 in which the learning rate is, like in Adagrad, adapted for each of
the parameters. The idea is to divide the learning rate for a weight by
a running average of the magnitudes of recent gradients for that weight.
Unusually, it was not published in an article but merely described in a
Coursera lecture. So, first the running average is calculated in terms
of means square, v ( w , t ) := γ v ( w , t − 1 ) + ( 1 − γ ) ( ∇ Q i (
w ) ) 2 {\\displaystyle v(w,t):=\\gamma v(w,t-1)+(1-\\gamma )(\\nabla
Q\_{i}(w))\^{2}} where, γ {\\displaystyle \\gamma } is the forgetting
factor. The concept of storing the historical gradient as sum of squares
is borrowed from Adagrad, but \"forgetting\" is introduced to solve
Adagrad\'s diminishing learning rates in non-convex problems by
gradually decreasing the influence of old data.And the parameters are
updated as, w := w − η v ( w , t ) ∇ Q i ( w ) {\\displaystyle
w:=w-{\\frac {\\eta }{\\sqrt {v(w,t)}}}\\nabla Q\_{i}(w)} RMSProp has
shown good adaptation of learning rate in different applications.
RMSProp can be seen as a generalization of Rprop and is capable to work
with mini-batches as well opposed to only full-batches. Adam Adam (short
for Adaptive Moment Estimation) is a 2014 update to the RMSProp
optimizer combining it with the main feature of the Momentum method. In
this optimization algorithm, running averages with exponential
forgetting of both the gradients and the second moments of the gradients
are used. Given parameters w ( t ) {\\displaystyle w\^{(t)}} and a loss
function L ( t ) {\\displaystyle L\^{(t)}} , where t {\\displaystyle t}
indexes the current training iteration (indexed at 0 {\\displaystyle 0}
), Adam\'s parameter update is given by: m w ( t + 1 ) ← β 1 m w ( t ) +
( 1 − β 1 ) ∇ w L ( t ) {\\displaystyle m\_{w}\^{(t+1)}\\leftarrow
\\beta \_{1}m\_{w}\^{(t)}+(1-\\beta \_{1})\\nabla \_{w}L\^{(t)}} v w (
t + 1 ) ← β 2 v w ( t ) + ( 1 − β 2 ) ( ∇ w L ( t ) ) 2 {\\displaystyle
v\_{w}\^{(t+1)}\\leftarrow \\beta \_{2}v\_{w}\^{(t)}+(1-\\beta
\_{2})(\\nabla \_{w}L\^{(t)})\^{2}} m \^ w = m w ( t + 1 ) 1 − β 1 t
{\\displaystyle {\\hat {m}}\_{w}={\\frac {m\_{w}\^{(t+1)}}{1-\\beta
\_{1}\^{t}}}} v \^ w = v w ( t + 1 ) 1 − β 2 t {\\displaystyle {\\hat
{v}}\_{w}={\\frac {v\_{w}\^{(t+1)}}{1-\\beta \_{2}\^{t}}}} w ( t + 1 ) ←
w ( t ) − η m \^ w v \^ w + ϵ {\\displaystyle w\^{(t+1)}\\leftarrow
w\^{(t)}-\\eta {\\frac {{\\hat {m}}\_{w}}{{\\sqrt {{\\hat
{v}}\_{w}}}+\\epsilon }}} where ϵ {\\displaystyle \\epsilon } is a small
scalar (e.g. 10 − 8 {\\displaystyle 10\^{-8}} ) used to prevent division
by 0, and β 1 {\\displaystyle \\beta \_{1}} (e.g. 0.9) and β 2
{\\displaystyle \\beta \_{2}} (e.g. 0.999) are the forgetting factors
for gradients and second moments of gradients, respectively. Squaring
and square-rooting is done element-wise. The profound influence of this
algorithm inspired multiple newer, less well-known momentum-based
optimization schemes using Nesterov-enhanced gradients (eg: NAdam and
FASFA) and varying interpretations of second-order information (eg:
Powerpropagation and AdaSqrt). However, the most commonly used variants
are AdaMax, which generalizes Adam using the infinity norm, and AMSGrad,
which addresses convergence problems from Adam by using maximum of past
squared gradients instead of the exponential average.AdamW is a later
update which mitigates an unoptimal choice of the weight decay algorithm
in Adam. Backtracking line search Backtracking line search is another
variant of gradient descent. All of the below are sourced from the
mentioned link. It is based on a condition known as the
Armijo--Goldstein condition. Both methods allow learning rates to change
at each iteration; however, the manner of the change is different.
Backtracking line search uses function evaluations to check Armijo\'s
condition, and in principle the loop in the algorithm for determining
the learning rates can be long and unknown in advance. Adaptive SGD does
not need a loop in determining learning rates. On the other hand,
adaptive SGD does not guarantee the \"descent property\" -- which
Backtracking line search enjoys -- which is that f ( x n + 1 ) ≤ f ( x n
) {\\displaystyle f(x\_{n+1})\\leq f(x\_{n})} for all n. If the gradient
of the cost function is globally Lipschitz continuous, with Lipschitz
constant L, and learning rate is chosen of the order 1/L, then the
standard version of SGD is a special case of backtracking line search.
Second-order methods A stochastic analogue of the standard
(deterministic) Newton--Raphson algorithm (a \"second-order\" method)
provides an asymptotically optimal or near-optimal form of iterative
optimization in the setting of stochastic approximation. A method that
uses direct measurements of the Hessian matrices of the summands in the
empirical risk function was developed by Byrd, Hansen, Nocedal, and
Singer. However, directly determining the required Hessian matrices for
optimization may not be possible in practice. Practical and
theoretically sound methods for second-order versions of SGD that do not
require direct Hessian information are given by Spall and others. (A
less efficient method based on finite differences, instead of
simultaneous perturbations, is given by Ruppert.) Another approach to
the approximation Hessian matrix is replacing it with the Fisher
information matrix, which transforms usual gradient to natural. These
methods not requiring direct Hessian information are based on either
values of the summands in the above empirical risk function or values of
the gradients of the summands (i.e., the SGD inputs). In particular,
second-order optimality is asymptotically achievable without direct
calculation of the Hessian matrices of the summands in the empirical
risk function. History SGD was gradually developed by several
collectives during the 1950s. Notes See also Backtracking line search
Coordinate descent -- changes one coordinate at a time, rather than one
example Linear classifier Online machine learning Stochastic hill
climbing Stochastic variance reduction References Further reading
Bottou, Léon (2004), \"Stochastic Learning\", Advanced Lectures on
Machine Learning, LNAI, vol. 3176, Springer, pp. 146--168, ISBN
978-3-540-23122-6 Buduma, Nikhil; Locascio, Nicholas (2017), \"Beyond
Gradient Descent\", Fundamentals of Deep Learning : Designing
Next-Generation Machine Intelligence Algorithms, O\'Reilly, ISBN
9781491925584 LeCun, Yann A.; Bottou, Léon; Orr, Genevieve B.; Müller,
Klaus-Robert (2012), \"Efficient BackProp\", Neural Networks: Tricks of
the Trade, Springer, pp. 9--48, ISBN 978-3-642-35288-1 Spall, James C.
(2003), Introduction to Stochastic Search and Optimization, Wiley, ISBN
978-0-471-33052-3 External links Using stochastic gradient descent in
C++, Boost, Ublas for linear regression Machine Learning Algorithms
\"Gradient Descent, How Neural Networks Learn\". 3Blue1Brown. October
16, 2017. Archived from the original on 2021-12-22 -- via YouTube. Goh
(April 4, 2017). \"Why Momentum Really Works\". Distill. 2 (4).
doi:10.23915/distill.00006. Interactive paper explaining momentum.
