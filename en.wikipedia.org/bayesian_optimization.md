Bayesian optimization is a sequential design strategy for global
optimization of black-box functions that does not assume any functional
forms. It is usually employed to optimize expensive-to-evaluate
functions. History The term is generally attributed to Jonas Mockus and
is coined in his work from a series of publications on global
optimization in the 1970s and 1980s. Strategy Bayesian optimization is
typically used on problems of the form max x ∈ A f ( x ) {\\textstyle
\\max \_{x\\in A}f(x)} , where A {\\textstyle A} is a set of points, x
{\\textstyle x} , which rely upon less than 20 dimensions ( R d , d ≤ 20
{\\textstyle \\mathbb {R} \^{d},d\\leq 20} ), and whose membership can
easily be evaluated. Bayesian optimization is particularly advantageous
for problems where f ( x ) {\\textstyle f(x)} is difficult to evaluate
due to its computational cost. The objective function, f {\\textstyle f}
, is continuous and takes the form of some unknown structure, referred
to as a \"black box\". Upon its evaluation, only f ( x ) {\\textstyle
f(x)} is observed and its derivatives are not evaluated.Since the
objective function is unknown, the Bayesian strategy is to treat it as a
random function and place a prior over it. The prior captures beliefs
about the behavior of the function. After gathering the function
evaluations, which are treated as data, the prior is updated to form the
posterior distribution over the objective function. The posterior
distribution, in turn, is used to construct an acquisition function
(often also referred to as infill sampling criteria) that determines the
next query point. There are several methods used to define the
prior/posterior distribution over the objective function. The most
common two methods use Gaussian processes in a method called kriging.
Another less expensive method uses the Parzen-Tree Estimator to
construct two distributions for \'high\' and \'low\' points, and then
finds the location that maximizes the expected improvement.Standard
Bayesian optimization relies upon each x ∈ A {\\displaystyle x\\in A}
being easy to evaluate, and problems that deviate from this assumption
are known as exotic Bayesian optimization problems. Optimization
problems can become exotic if it is known that there is noise, the
evaluations are being done in parallel, the quality of evaluations
relies upon a tradeoff between difficulty and accuracy, the presence of
random environmental conditions, or if the evaluation involves
derivatives. Acquisition functions Examples of acquisition functions
include probability of improvement expected improvement Bayesian
expected losses upper confidence bounds (UCB) or lower confidence bounds
Thompson samplingand hybrids of these. They all trade-off exploration
and exploitation so as to minimize the number of function queries. As
such, Bayesian optimization is well suited for functions that are
expensive to evaluate. Solution methods The maximum of the acquisition
function is typically found by resorting to discretization or by means
of an auxiliary optimizer. Acquisition functions are typically
well-behaved and are maximized using a numerical optimization technique,
such as Newton\'s Method or quasi-Newton methods like the
Broyden--Fletcher--Goldfarb--Shanno algorithm. Applications The approach
has been applied to solve a wide range of problems, including learning
to rank, computer graphics and visual design, robotics, sensor networks,
automatic algorithm configuration, automatic machine learning toolboxes,
reinforcement learning, planning, visual attention, architecture
configuration in deep learning, static program analysis, experimental
particle physics, chemistry, material design, and drug development. See
also Multi-armed bandit Kriging Thompson sampling Global optimization
Bayesian experimental design Probabilistic numerics Pareto optimum ==
References ==
