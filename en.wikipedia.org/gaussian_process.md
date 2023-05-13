In probability theory and statistics, a Gaussian process is a stochastic
process (a collection of random variables indexed by time or space),
such that every finite collection of those random variables has a
multivariate normal distribution, i.e. every finite linear combination
of them is normally distributed. The distribution of a Gaussian process
is the joint distribution of all those (infinitely many) random
variables, and as such, it is a distribution over functions with a
continuous domain, e.g. time or space. The concept of Gaussian processes
is named after Carl Friedrich Gauss because it is based on the notion of
the Gaussian distribution (normal distribution). Gaussian processes can
be seen as an infinite-dimensional generalization of multivariate normal
distributions. Gaussian processes are useful in statistical modelling,
benefiting from properties inherited from the normal distribution. For
example, if a random process is modelled as a Gaussian process, the
distributions of various derived quantities can be obtained explicitly.
Such quantities include the average value of the process over a range of
times and the error in estimating the average using sample values at a
small set of times. While exact models often scale poorly as the amount
of data increases, multiple approximation methods have been developed
which often retain good accuracy while drastically reducing computation
time. Definition A time continuous stochastic process { X t ; t ∈ T }
{\\displaystyle \\left\\{X\_{t};t\\in T\\right\\}} is Gaussian if and
only if for every finite set of indices t 1 , ... , t k {\\displaystyle
t\_{1},\\ldots ,t\_{k}} in the index set T {\\displaystyle T} is a
multivariate Gaussian random variable. That is the same as saying every
linear combination of ( X t 1 , ... , X t k ) {\\displaystyle
(X\_{t\_{1}},\\ldots ,X\_{t\_{k}})} has a univariate normal (or
Gaussian) distribution. Using characteristic functions of random
variables, the Gaussian property can be formulated as follows: { X t ; t
∈ T } {\\displaystyle \\left\\{X\_{t};t\\in T\\right\\}} is Gaussian if
and only if, for every finite set of indices t 1 , ... , t k
{\\displaystyle t\_{1},\\ldots ,t\_{k}} , there are real-valued σ ℓ j
{\\displaystyle \\sigma \_{\\ell j}} , μ ℓ {\\displaystyle \\mu \_{\\ell
}} with σ j j \> 0 {\\displaystyle \\sigma \_{jj}\>0} such that the
following equality holds for all s 1 , s 2 , ... , s k ∈ R
{\\displaystyle s\_{1},s\_{2},\\ldots ,s\_{k}\\in \\mathbb {R} } where i
{\\displaystyle i} denotes the imaginary unit such that i 2 = − 1
{\\displaystyle i\^{2}=-1} . The numbers σ ℓ j {\\displaystyle \\sigma
\_{\\ell j}} and μ ℓ {\\displaystyle \\mu \_{\\ell }} can be shown to be
the covariances and means of the variables in the process. Variance The
variance of a Gaussian process is finite at any time t {\\displaystyle
t} , formally: p. 515 Stationarity For general stochastic processes
strict-sense stationarity implies wide-sense stationarity but not every
wide-sense stationary stochastic process is strict-sense stationary.
However, for a Gaussian stochastic process the two concepts are
equivalent.: p. 518 A Gaussian stochastic process is strict-sense
stationary if, and only if, it is wide-sense stationary. Example There
is an explicit representation for stationary Gaussian processes. A
simple example of this representation is where ξ 1 {\\displaystyle \\xi
\_{1}} and ξ 2 {\\displaystyle \\xi \_{2}} are independent random
variables with the standard normal distribution. Covariance functions A
key fact of Gaussian processes is that they can be completely defined by
their second-order statistics. Thus, if a Gaussian process is assumed to
have mean zero, defining the covariance function completely defines the
process\' behaviour. Importantly the non-negative definiteness of this
function enables its spectral decomposition using the Karhunen--Loève
expansion. Basic aspects that can be defined through the covariance
function are the process\' stationarity, isotropy, smoothness and
periodicity.Stationarity refers to the process\' behaviour regarding the
separation of any two points x {\\displaystyle x} and x ′
{\\displaystyle x\'} . If the process is stationary, the covariance
function depends only on x − x ′ {\\displaystyle x-x\'} . For example,
the Ornstein--Uhlenbeck process is stationary. If the process depends
only on \| x − x ′ \| {\\displaystyle \|x-x\'\|} , the Euclidean
distance (not the direction) between x {\\displaystyle x} and x ′
{\\displaystyle x\'} , then the process is considered isotropic. A
process that is concurrently stationary and isotropic is considered to
be homogeneous; in practice these properties reflect the differences (or
rather the lack of them) in the behaviour of the process given the
location of the observer. Ultimately Gaussian processes translate as
taking priors on functions and the smoothness of these priors can be
induced by the covariance function. If we expect that for \"near-by\"
input points x {\\displaystyle x} and x ′ {\\displaystyle x\'} their
corresponding output points y {\\displaystyle y} and y ′ {\\displaystyle
y\'} to be \"near-by\" also, then the assumption of continuity is
present. If we wish to allow for significant displacement then we might
choose a rougher covariance function. Extreme examples of the behaviour
is the Ornstein--Uhlenbeck covariance function and the squared
exponential where the former is never differentiable and the latter
infinitely differentiable. Periodicity refers to inducing periodic
patterns within the behaviour of the process. Formally, this is achieved
by mapping the input x {\\displaystyle x} to a two dimensional vector u
( x ) = ( cos ⁡ ( x ) , sin ⁡ ( x ) ) {\\displaystyle
u(x)=\\left(\\cos(x),\\sin(x)\\right)} . Usual covariance functions
There are a number of common covariance functions: Constant : K C ( x ,
x ′ ) = C {\\displaystyle K\_{\\operatorname {C} }(x,x\')=C} Linear: K L
( x , x ′ ) = x T x ′ {\\displaystyle K\_{\\operatorname {L}
}(x,x\')=x\^{\\mathsf {T}}x\'} white Gaussian noise: K GN ( x , x ′ ) =
σ 2 δ x , x ′ {\\displaystyle K\_{\\operatorname {GN} }(x,x\')=\\sigma
\^{2}\\delta \_{x,x\'}} Squared exponential: K SE ( x , x ′ ) = exp ⁡ ( −
\| d \| 2 2 ℓ 2 ) {\\displaystyle K\_{\\operatorname {SE} }(x,x\')=\\exp
\\left(-{\\frac {\|d\|\^{2}}{2\\ell \^{2}}}\\right)}
Ornstein--Uhlenbeck: K OU ( x , x ′ ) = exp ⁡ ( − \| d \| ℓ )
{\\displaystyle K\_{\\operatorname {OU} }(x,x\')=\\exp \\left(-{\\frac
{\|d\|}{\\ell }}\\right)} Matérn: K Matern ( x , x ′ ) = 2 1 − ν Γ ( ν )
( 2 ν \| d \| ℓ ) ν K ν ( 2 ν \| d \| ℓ ) {\\displaystyle
K\_{\\operatorname {Matern} }(x,x\')={\\frac {2\^{1-\\nu }}{\\Gamma
(\\nu )}}\\left({\\frac {{\\sqrt {2\\nu }}\|d\|}{\\ell }}\\right)\^{\\nu
}K\_{\\nu }\\left({\\frac {{\\sqrt {2\\nu }}\|d\|}{\\ell }}\\right)}
Periodic: K P ( x , x ′ ) = exp ⁡ ( − 2 sin 2 ⁡ ( d 2 ) ℓ 2 )
{\\displaystyle K\_{\\operatorname {P} }(x,x\')=\\exp \\left(-{\\frac
{2\\sin \^{2}\\left({\\frac {d}{2}}\\right)}{\\ell \^{2}}}\\right)}
Rational quadratic: K RQ ( x , x ′ ) = ( 1 + \| d \| 2 ) − α , α ≥ 0
{\\displaystyle K\_{\\operatorname {RQ}
}(x,x\')=\\left(1+\|d\|\^{2}\\right)\^{-\\alpha },\\quad \\alpha \\geq
0} Here d = x − x ′ {\\displaystyle d=x-x\'} . The parameter ℓ
{\\displaystyle \\ell } is the characteristic length-scale of the
process (practically, \"how close\" two points x {\\displaystyle x} and
x ′ {\\displaystyle x\'} have to be to influence each other
significantly), δ {\\displaystyle \\delta } is the Kronecker delta and σ
{\\displaystyle \\sigma } the standard deviation of the noise
fluctuations. Moreover, K ν {\\displaystyle K\_{\\nu }} is the modified
Bessel function of order ν {\\displaystyle \\nu } and Γ ( ν )
{\\displaystyle \\Gamma (\\nu )} is the gamma function evaluated at ν
{\\displaystyle \\nu } . Importantly, a complicated covariance function
can be defined as a linear combination of other simpler covariance
functions in order to incorporate different insights about the data-set
at hand. The inferential results are dependent on the values of the
hyperparameters θ {\\displaystyle \\theta } (e.g. ℓ {\\displaystyle
\\ell } and σ {\\displaystyle \\sigma } ) defining the model\'s
behaviour. A popular choice for θ {\\displaystyle \\theta } is to
provide maximum a posteriori (MAP) estimates of it with some chosen
prior. If the prior is very near uniform, this is the same as maximizing
the marginal likelihood of the process; the marginalization being done
over the observed process values y {\\displaystyle y} . This approach is
also known as maximum likelihood II, evidence maximization, or empirical
Bayes. Continuity For a Gaussian process, continuity in probability is
equivalent to mean-square continuity,: 145  and continuity with
probability one is equivalent to sample continuity.: 91 \"Gaussian
processes are discontinuous at fixed points.\"  The latter implies, but
is not implied by, continuity in probability. Continuity in probability
holds if and only if the mean and autocovariance are continuous
functions. In contrast, sample continuity was challenging even for
stationary Gaussian processes (as probably noted first by Andrey
Kolmogorov), and more challenging for more general processes.: Sect.
2.8 : 69, 81 : 80  As usual, by a sample continuous process one means a
process that admits a sample continuous modification. : 292 : 424
Stationary case For a stationary Gaussian process X = ( X t ) t ∈ R ,
{\\displaystyle X=(X\_{t})\_{t\\in \\mathbb {R} },} some conditions on
its spectrum are sufficient for sample continuity, but fail to be
necessary. A necessary and sufficient condition, sometimes called
Dudley--Fernique theorem, involves the function σ {\\displaystyle
\\sigma } defined by (the right-hand side does not depend on t
{\\displaystyle t} due to stationarity). Continuity of X {\\displaystyle
X} in probability is equivalent to continuity of σ {\\displaystyle
\\sigma } at 0. {\\displaystyle 0.} When convergence of σ ( h )
{\\displaystyle \\sigma (h)} to 0 {\\displaystyle 0} (as h → 0
{\\displaystyle h\\to 0} ) is too slow, sample continuity of X
{\\displaystyle X} may fail. Convergence of the following integrals
matters: these two integrals being equal according to integration by
substitution h = e − x 2 , {\\textstyle h=e\^{-x\^{2}},} x = log ⁡ ( 1 /
h ) . {\\textstyle x={\\sqrt {\\log(1/h)}}.} The first integrand need
not be bounded as h → 0 + , {\\displaystyle h\\to 0+,} thus the integral
may converge ( I ( σ ) \< ∞ {\\displaystyle I(\\sigma )\<\\infty } ) or
diverge ( I ( σ ) = ∞ {\\displaystyle I(\\sigma )=\\infty } ). Taking
for example σ ( e − x 2 ) = 1 x a {\\textstyle \\sigma
(e\^{-x\^{2}})={\\tfrac {1}{x\^{a}}}} for large x , {\\displaystyle x,}
that is, σ ( h ) = ( log ⁡ ( 1 / h ) ) − a / 2 {\\textstyle \\sigma
(h)=(\\log(1/h))\^{-a/2}} for small h , {\\displaystyle h,} one obtains
I ( σ ) \< ∞ {\\displaystyle I(\\sigma )\<\\infty } when a \> 1 ,
{\\displaystyle a\>1,} and I ( σ ) = ∞ {\\displaystyle I(\\sigma
)=\\infty } when 0 \< a ≤ 1. {\\displaystyle 0 0 {\\displaystyle
c\_{n}\>0} satisfy ∑ n c n \< ∞ . {\\textstyle \\sum
\_{n}c\_{n}\<\\infty .} The latter relation implies E ∑ n c n ( \| ξ n
\| + \| η n \| ) = ∑ n c n E ( \| ξ n \| + \| η n \| ) = const ⋅ ∑ n c n
\< ∞ , {\\textstyle \\mathbb {E} \\sum \_{n}c\_{n}(\|\\xi
\_{n}\|+\|\\eta \_{n}\|)=\\sum \_{n}c\_{n}\\mathbb {E} (\|\\xi
\_{n}\|+\|\\eta \_{n}\|)={\\text{const}}\\cdot \\sum
\_{n}c\_{n}\<\\infty ,} whence ∑ n c n ( \| ξ n \| + \| η n \| ) \< ∞
{\\textstyle \\sum \_{n}c\_{n}(\|\\xi \_{n}\|+\|\\eta \_{n}\|)\<\\infty
} almost surely, which ensures uniform convergence of the Fourier series
almost surely, and sample continuity of X . {\\displaystyle X.} Its
autocovariation function is nowhere monotone (see the picture), as well
as the corresponding function σ , {\\displaystyle \\sigma ,} Brownian
motion as the integral of Gaussian processes A Wiener process (also
known as Brownian motion) is the integral of a white noise generalized
Gaussian process. It is not stationary, but it has stationary
increments. The Ornstein--Uhlenbeck process is a stationary Gaussian
process. The Brownian bridge is (like the Ornstein--Uhlenbeck process)
an example of a Gaussian process whose increments are not independent.
The fractional Brownian motion is a Gaussian process whose covariance
function is a generalisation of that of the Wiener process. Driscoll\'s
zero-one law Driscoll\'s zero-one law is a result characterizing the
sample functions generated by a Gaussian process. Let f {\\displaystyle
f} be a mean-zero Gaussian process { X t ; t ∈ T } {\\displaystyle
\\left\\{X\_{t};t\\in T\\right\\}} with non-negative definite covariance
function K {\\displaystyle K} . Let H ( R ) {\\displaystyle {\\mathcal
{H}}(R)} be a Reproducing kernel Hilbert space with positive definite
kernel R {\\displaystyle R} . Then where K n {\\displaystyle K\_{n}} and
R n {\\displaystyle R\_{n}} are the covariance matrices of all possible
pairs of n {\\displaystyle n} points, implies Moreover, implies This has
significant implications when K = R {\\displaystyle K=R} , as As such,
almost all sample paths of a mean-zero Gaussian process with positive
definite kernel K {\\displaystyle K} will lie outside of the Hilbert
space H ( K ) {\\displaystyle {\\mathcal {H}}(K)} . Linearly constrained
Gaussian processes For many applications of interest some pre-existing
knowledge about the system at hand is already given. Consider e.g. the
case where the output of the Gaussian process corresponds to a magnetic
field; here, the real magnetic field is bound by Maxwell\'s equations
and a way to incorporate this constraint into the Gaussian process
formalism would be desirable as this would likely improve the accuracy
of the algorithm. A method on how to incorporate linear constraints into
Gaussian processes already exists:Consider the (vector valued) output
function f ( x ) {\\displaystyle f(x)} which is known to obey the linear
constraint (i.e. F X {\\displaystyle {\\mathcal {F}}\_{X}} is a linear
operator) Then the constraint F X {\\displaystyle {\\mathcal {F}}\_{X}}
can be fulfilled by choosing f ( x ) = G X ( g ( x ) ) {\\displaystyle
f(x)={\\mathcal {G}}\_{X}(g(x))} , where g ( x ) ∼ G P ( μ g , K g )
{\\displaystyle g(x)\\sim {\\mathcal {GP}}(\\mu \_{g},K\_{g})} is
modelled as a Gaussian process, and finding G X {\\displaystyle
{\\mathcal {G}}\_{X}} such that Given G X {\\displaystyle {\\mathcal
{G}}\_{X}} and using the fact that Gaussian processes are closed under
linear transformations, the Gaussian process for f {\\displaystyle f}
obeying constraint F X {\\displaystyle {\\mathcal {F}}\_{X}} becomes
Hence, linear constraints can be encoded into the mean and covariance
function of a Gaussian process. Applications A Gaussian process can be
used as a prior probability distribution over functions in Bayesian
inference. Given any set of N points in the desired domain of your
functions, take a multivariate Gaussian whose covariance matrix
parameter is the Gram matrix of your N points with some desired kernel,
and sample from that Gaussian. For solution of the multi-output
prediction problem, Gaussian process regression for vector-valued
function was developed. In this method, a \'big\' covariance is
constructed, which describes the correlations between all the input and
output variables taken in N points in the desired domain. This approach
was elaborated in detail for the matrix-valued Gaussian processes and
generalised to processes with \'heavier tails\' like Student-t
processes.Inference of continuous values with a Gaussian process prior
is known as Gaussian process regression, or kriging; extending Gaussian
process regression to multiple target variables is known as cokriging.
Gaussian processes are thus useful as a powerful non-linear multivariate
interpolation tool. Gaussian processes are also commonly used to tackle
numerical analysis problems such as numerical integration, solving
differential equations, or optimisation in the field of probabilistic
numerics. Gaussian processes can also be used in the context of mixture
of experts models, for example. The underlying rationale of such a
learning framework consists in the assumption that a given mapping
cannot be well captured by a single Gaussian process model. Instead, the
observation space is divided into subsets, each of which is
characterized by a different mapping function; each of these is learned
via a different Gaussian process component in the postulated mixture. In
the natural sciences, Gaussian processes have found use as probabilistic
models of astronomical time series and as predictors of molecular
properties. Gaussian process prediction, or Kriging When concerned with
a general Gaussian process regression problem (Kriging), it is assumed
that for a Gaussian process f {\\displaystyle f} observed at coordinates
x {\\displaystyle x} , the vector of values f ( x ) {\\displaystyle
f(x)} is just one sample from a multivariate Gaussian distribution of
dimension equal to number of observed coordinates n {\\displaystyle n} .
Therefore, under the assumption of a zero-mean distribution, f ( x ′ ) ∼
N ( 0 , K ( θ , x , x ′ ) ) {\\displaystyle f(x\')\\sim N(0,K(\\theta
,x,x\'))} , where K ( θ , x , x ′ ) {\\displaystyle K(\\theta ,x,x\')}
is the covariance matrix between all possible pairs ( x , x ′ )
{\\displaystyle (x,x\')} for a given set of hyperparameters θ. As such
the log marginal likelihood is: and maximizing this marginal likelihood
towards θ provides the complete specification of the Gaussian process f.
One can briefly note at this point that the first term corresponds to a
penalty term for a model\'s failure to fit observed values and the
second term to a penalty term that increases proportionally to a
model\'s complexity. Having specified θ, making predictions about
unobserved values f ( x ∗ ) {\\displaystyle f(x\^{\*})} at coordinates
x\* is then only a matter of drawing samples from the predictive
distribution p ( y ∗ ∣ x ∗ , f ( x ) , x ) = N ( y ∗ ∣ A , B )
{\\displaystyle p(y\^{\*}\\mid x\^{\*},f(x),x)=N(y\^{\*}\\mid A,B)}
where the posterior mean estimate A is defined as and the posterior
variance estimate B is defined as: where K ( θ , x ∗ , x )
{\\displaystyle K(\\theta ,x\^{\*},x)} is the covariance between the new
coordinate of estimation x\* and all other observed coordinates x for a
given hyperparameter vector θ, K ( θ , x , x ′ ) {\\displaystyle
K(\\theta ,x,x\')} and f ( x ) {\\displaystyle f(x)} are defined as
before and K ( θ , x ∗ , x ∗ ) {\\displaystyle K(\\theta
,x\^{\*},x\^{\*})} is the variance at point x\* as dictated by θ. It is
important to note that practically the posterior mean estimate of f ( x
∗ ) {\\displaystyle f(x\^{\*})} (the \"point estimate\") is just a
linear combination of the observations f ( x ) {\\displaystyle f(x)} ;
in a similar manner the variance of f ( x ∗ ) {\\displaystyle
f(x\^{\*})} is actually independent of the observations f ( x )
{\\displaystyle f(x)} . A known bottleneck in Gaussian process
prediction is that the computational complexity of inference and
likelihood evaluation is cubic in the number of points \|x\|, and as
such can become unfeasible for larger data sets. Works on sparse
Gaussian processes, that usually are based on the idea of building a
representative set for the given process f, try to circumvent this
issue. The kriging method can be used in the latent level of a nonlinear
mixed-effects model for a spatial functional prediction: this technique
is called the latent kriging.Often, the covariance has the form K ( θ ,
x , x ′ ) = 1 σ 2 K \~ ( θ , x , x ′ ) {\\textstyle K(\\theta
,x,x\')={\\frac {1}{\\sigma \^{2}}}{\\tilde {K}}(\\theta ,x,x\')} ,
where σ 2 {\\displaystyle \\sigma \^{2}} is a scaling parameter.
Examples are the Matérn class covariance functions. If this scaling
parameter σ 2 {\\displaystyle \\sigma \^{2}} is either known or unknown
(i.e. must be marginalized), then the posterior probability, p ( θ ∣ D )
{\\displaystyle p(\\theta \\mid D)} , i.e. the probability for the
hyperparameters θ {\\displaystyle \\theta } given a set of data pairs D
{\\displaystyle D} of observations of x {\\displaystyle x} and f ( x )
{\\displaystyle f(x)} , admits an analytical expression. Bayesian neural
networks as Gaussian processes Bayesian neural networks are a particular
type of Bayesian network that results from treating deep learning and
artificial neural network models probabilistically, and assigning a
prior distribution to their parameters. Computation in artificial neural
networks is usually organized into sequential layers of artificial
neurons. The number of neurons in a layer is called the layer width. As
layer width grows large, many Bayesian neural networks reduce to a
Gaussian process with a closed form compositional kernel. This Gaussian
process is called the Neural Network Gaussian Process (NNGP). It allows
predictions from Bayesian neural networks to be more efficiently
evaluated, and provides an analytic tool to understand deep learning
models. Computational issues In practical applications, Gaussian process
models are often evaluated on a grid leading to multivariate normal
distributions. Using these models for prediction or parameter estimation
using maximum likelihood requires evaluating a multivariate Gaussian
density, which involves calculating the determinant and the inverse of
the covariance matrix. Both of these operations have cubic computational
complexity which means that even for grids of modest sizes, both
operations can have a prohibitive computational cost. This drawback led
to the development of multiple approximation methods. See also Bayes
linear statistics Bayesian interpretation of regularization Kriging
Gaussian free field Gauss--Markov process Gradient-enhanced kriging
(GEK) Student\'s t-process References External links Literature The
Gaussian Processes Web Site, including the text of Rasmussen and
Williams\' Gaussian Processes for Machine Learning A gentle introduction
to Gaussian processes A Review of Gaussian Random Fields and Correlation
Functions Efficient Reinforcement Learning using Gaussian Processes
Software GPML: A comprehensive Matlab toolbox for GP regression and
classification STK: a Small (Matlab/Octave) Toolbox for Kriging and GP
modeling Kriging module in UQLab framework (Matlab) Matlab/Octave
function for stationary Gaussian fields Yelp MOE -- A black box
optimization engine using Gaussian process learning ooDACE -- A flexible
object-oriented Kriging Matlab toolbox. GPstuff -- Gaussian process
toolbox for Matlab and Octave GPy -- A Gaussian processes framework in
Python GSTools - A geostatistical toolbox, including Gaussian process
regression, written in Python Interactive Gaussian process regression
demo Basic Gaussian process library written in C++11 scikit-learn -- A
machine learning library for Python which includes Gaussian process
regression and classification \[1\] - The Kriging toolKit (KriKit) is
developed at the Institute of Bio- and Geosciences 1 (IBG-1) of
Forschungszentrum Jülich (FZJ) Video tutorials Gaussian Process Basics
by David MacKay Learning with Gaussian Processes by Carl Edward
Rasmussen Bayesian inference and Gaussian processes by Carl Edward
Rasmussen
