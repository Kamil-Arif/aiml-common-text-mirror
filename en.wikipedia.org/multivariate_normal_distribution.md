In probability theory and statistics, the multivariate normal
distribution, multivariate Gaussian distribution, or joint normal
distribution is a generalization of the one-dimensional (univariate)
normal distribution to higher dimensions. One definition is that a
random vector is said to be k-variate normally distributed if every
linear combination of its k components has a univariate normal
distribution. Its importance derives mainly from the multivariate
central limit theorem. The multivariate normal distribution is often
used to describe, at least approximately, any set of (possibly)
correlated real-valued random variables each of which clusters around a
mean value. Definitions Notation and parameterization The multivariate
normal distribution of a k-dimensional random vector X = ( X 1 , ... , X
k ) T {\\displaystyle \\mathbf {X} =(X\_{1},\\ldots ,X\_{k})\^{\\mathrm
{T} }} can be written in the following notation: X ∼ N ( μ , Σ ) ,
{\\displaystyle \\mathbf {X} \\ \\sim \\ {\\mathcal {N}}({\\boldsymbol
{\\mu }},\\,{\\boldsymbol {\\Sigma }}),} or to make it explicitly known
that X is k-dimensional, X ∼ N k ( μ , Σ ) , {\\displaystyle \\mathbf
{X} \\ \\sim \\ {\\mathcal {N}}\_{k}({\\boldsymbol {\\mu
}},\\,{\\boldsymbol {\\Sigma }}),} with k-dimensional mean vector μ = E ⁡
\[ X \] = ( E ⁡ \[ X 1 \] , E ⁡ \[ X 2 \] , ... , E ⁡ \[ X k \] ) T ,
{\\displaystyle {\\boldsymbol {\\mu }}=\\operatorname {E} \[\\mathbf {X}
\]=(\\operatorname {E} \[X\_{1}\],\\operatorname {E} \[X\_{2}\],\\ldots
,\\operatorname {E} \[X\_{k}\])\^{\\textbf {T}},} and k × k
{\\displaystyle k\\times k} covariance matrix Σ i , j = E ⁡ \[ ( X i − μ
i ) ( X j − μ j ) \] = Cov ⁡ \[ X i , X j \] {\\displaystyle \\Sigma
\_{i,j}=\\operatorname {E} \[(X\_{i}-\\mu \_{i})(X\_{j}-\\mu
\_{j})\]=\\operatorname {Cov} \[X\_{i},X\_{j}\]} such that 1 ≤ i ≤ k
{\\displaystyle 1\\leq i\\leq k} and 1 ≤ j ≤ k {\\displaystyle 1\\leq
j\\leq k} . The inverse of the covariance matrix is called the precision
matrix, denoted by Q = Σ − 1 {\\displaystyle {\\boldsymbol
{Q}}={\\boldsymbol {\\Sigma }}\^{-1}} . Standard normal random vector A
real random vector X = ( X 1 , ... , X k ) T {\\displaystyle \\mathbf
{X} =(X\_{1},\\ldots ,X\_{k})\^{\\mathrm {T} }} is called a standard
normal random vector if all of its components X i {\\displaystyle
X\_{i}} are independent and each is a zero-mean unit-variance normally
distributed random variable, i.e. if X i ∼ N ( 0 , 1 ) {\\displaystyle
X\_{i}\\sim \\ {\\mathcal {N}}(0,1)} for all i = 1 ... k {\\displaystyle
i=1\\ldots k} .: p. 454 Centered normal random vector A real random
vector X = ( X 1 , ... , X k ) T {\\displaystyle \\mathbf {X}
=(X\_{1},\\ldots ,X\_{k})\^{\\mathrm {T} }} is called a centered normal
random vector if there exists a deterministic k × ℓ {\\displaystyle
k\\times \\ell } matrix A {\\displaystyle {\\boldsymbol {A}}} such that
A Z {\\displaystyle {\\boldsymbol {A}}\\mathbf {Z} } has the same
distribution as X {\\displaystyle \\mathbf {X} } where Z {\\displaystyle
\\mathbf {Z} } is a standard normal random vector with ℓ {\\displaystyle
\\ell } components.: p. 454 Normal random vector A real random vector X
= ( X 1 , ... , X k ) T {\\displaystyle \\mathbf {X} =(X\_{1},\\ldots
,X\_{k})\^{\\mathrm {T} }} is called a normal random vector if there
exists a random ℓ {\\displaystyle \\ell } -vector Z {\\displaystyle
\\mathbf {Z} } , which is a standard normal random vector, a k
{\\displaystyle k} -vector μ {\\displaystyle \\mathbf {\\mu } } , and a
k × ℓ {\\displaystyle k\\times \\ell } matrix A {\\displaystyle
{\\boldsymbol {A}}} , such that X = A Z + μ {\\displaystyle \\mathbf {X}
={\\boldsymbol {A}}\\mathbf {Z} +\\mathbf {\\mu } } .: p. 454 : p.
455 Formally: Here the covariance matrix is Σ = A A T {\\displaystyle
{\\boldsymbol {\\Sigma }}={\\boldsymbol {A}}{\\boldsymbol
{A}}\^{\\mathrm {T} }} . In the degenerate case where the covariance
matrix is singular, the corresponding distribution has no density; see
the section below for details. This case arises frequently in
statistics; for example, in the distribution of the vector of residuals
in the ordinary least squares regression. The X i {\\displaystyle
X\_{i}} are in general not independent; they can be seen as the result
of applying the matrix A {\\displaystyle {\\boldsymbol {A}}} to a
collection of independent Gaussian variables Z {\\displaystyle \\mathbf
{Z} } . Equivalent definitions The following definitions are equivalent
to the definition given above. A random vector X = ( X 1 , ... , X k ) T
{\\displaystyle \\mathbf {X} =(X\_{1},\\ldots ,X\_{k})\^{T}} has a
multivariate normal distribution if it satisfies one of the following
equivalent conditions. Every linear combination Y = a 1 X 1 + ⋯ + a k X
k {\\displaystyle Y=a\_{1}X\_{1}+\\cdots +a\_{k}X\_{k}} of its
components is normally distributed. That is, for any constant vector a ∈
R k {\\displaystyle \\mathbf {a} \\in \\mathbb {R} \^{k}} , the random
variable Y = a T X {\\displaystyle Y=\\mathbf {a} \^{\\mathrm {T}
}\\mathbf {X} } has a univariate normal distribution, where a univariate
normal distribution with zero variance is a point mass on its mean.
There is a k-vector μ {\\displaystyle \\mathbf {\\mu } } and a
symmetric, positive semidefinite k × k {\\displaystyle k\\times k}
matrix Σ {\\displaystyle {\\boldsymbol {\\Sigma }}} , such that the
characteristic function of X {\\displaystyle \\mathbf {X} } is The
spherical normal distribution can be characterised as the unique
distribution where components are independent in any orthogonal
coordinate system. Density function Non-degenerate case The multivariate
normal distribution is said to be \"non-degenerate\" when the symmetric
covariance matrix Σ {\\displaystyle {\\boldsymbol {\\Sigma }}} is
positive definite. In this case the distribution has density where x
{\\displaystyle {\\mathbf {x} }} is a real k-dimensional column vector
and \| Σ \| ≡ det Σ {\\displaystyle \|{\\boldsymbol {\\Sigma }}\|\\equiv
\\det {\\boldsymbol {\\Sigma }}} is the determinant of Σ {\\displaystyle
{\\boldsymbol {\\Sigma }}} , also known as the generalized variance. The
equation above reduces to that of the univariate normal distribution if
Σ {\\displaystyle {\\boldsymbol {\\Sigma }}} is a 1 × 1 {\\displaystyle
1\\times 1} matrix (i.e. a single real number). The circularly symmetric
version of the complex normal distribution has a slightly different
form. Each iso-density locus --- the locus of points in k-dimensional
space each of which gives the same particular value of the density ---
is an ellipse or its higher-dimensional generalization; hence the
multivariate normal is a special case of the elliptical distributions.
The quantity ( x − μ ) T Σ − 1 ( x − μ ) {\\displaystyle {\\sqrt
{({\\mathbf {x} }-{\\boldsymbol {\\mu }})\^{\\mathrm {T} }{\\boldsymbol
{\\Sigma }}\^{-1}({\\mathbf {x} }-{\\boldsymbol {\\mu }})}}} is known as
the Mahalanobis distance, which represents the distance of the test
point x {\\displaystyle {\\mathbf {x} }} from the mean μ {\\displaystyle
{\\boldsymbol {\\mu }}} . Note that in the case when k = 1
{\\displaystyle k=1} , the distribution reduces to a univariate normal
distribution and the Mahalanobis distance reduces to the absolute value
of the standard score. See also Interval below. Bivariate case In the
2-dimensional nonsingular case ( k = rank ⁡ ( Σ ) = 2 {\\displaystyle
k=\\operatorname {rank} \\left(\\Sigma \\right)=2} ), the probability
density function of a vector \[XY\]′ {\\displaystyle {\\text{\[XY\]′}}}
is: where ρ {\\displaystyle \\rho } is the correlation between X
{\\displaystyle X} and Y {\\displaystyle Y} and where σ X \> 0
{\\displaystyle \\sigma \_{X}\>0} and σ Y \> 0 {\\displaystyle \\sigma
\_{Y}\>0} . In this case, μ = ( μ X μ Y ) , Σ = ( σ X 2 ρ σ X σ Y ρ σ X
σ Y σ Y 2 ) . {\\displaystyle {\\boldsymbol {\\mu
}}={\\begin{pmatrix}\\mu \_{X}\\\\\\mu \_{Y}\\end{pmatrix}},\\quad
{\\boldsymbol {\\Sigma }}={\\begin{pmatrix}\\sigma \_{X}\^{2}&\\rho
\\sigma \_{X}\\sigma \_{Y}\\\\\\rho \\sigma \_{X}\\sigma \_{Y}&\\sigma
\_{Y}\^{2}\\end{pmatrix}}.} In the bivariate case, the first equivalent
condition for multivariate reconstruction of normality can be made less
restrictive as it is sufficient to verify that countably many distinct
linear combinations of X {\\displaystyle X} and Y {\\displaystyle Y} are
normal in order to conclude that the vector of \[XY\]′ {\\displaystyle
{\\text{\[XY\]′}}} is bivariate normal.The bivariate iso-density loci
plotted in the x , y {\\displaystyle x,y} -plane are ellipses, whose
principal axes are defined by the eigenvectors of the covariance matrix
Σ {\\displaystyle {\\boldsymbol {\\Sigma }}} (the major and minor
semidiameters of the ellipse equal the square-root of the ordered
eigenvalues). As the absolute value of the correlation parameter ρ
{\\displaystyle \\rho } increases, these loci are squeezed toward the
following line : y ( x ) = sgn ⁡ ( ρ ) σ Y σ X ( x − μ X ) + μ Y .
{\\displaystyle y(x)=\\operatorname {sgn}(\\rho ){\\frac {\\sigma
\_{Y}}{\\sigma \_{X}}}(x-\\mu \_{X})+\\mu \_{Y}.} This is because this
expression, with sgn ⁡ ( ρ ) {\\displaystyle \\operatorname {sgn}(\\rho
)} (where sgn is the Sign function) replaced by ρ {\\displaystyle \\rho
} , is the best linear unbiased prediction of Y {\\displaystyle Y} given
a value of X {\\displaystyle X} . Degenerate case If the covariance
matrix Σ {\\displaystyle {\\boldsymbol {\\Sigma }}} is not full rank,
then the multivariate normal distribution is degenerate and does not
have a density. More precisely, it does not have a density with respect
to k-dimensional Lebesgue measure (which is the usual measure assumed in
calculus-level probability courses). Only random vectors whose
distributions are absolutely continuous with respect to a measure are
said to have densities (with respect to that measure). To talk about
densities but avoid dealing with measure-theoretic complications it can
be simpler to restrict attention to a subset of rank ⁡ ( Σ )
{\\displaystyle \\operatorname {rank} ({\\boldsymbol {\\Sigma }})} of
the coordinates of x {\\displaystyle \\mathbf {x} } such that the
covariance matrix for this subset is positive definite; then the other
coordinates may be thought of as an affine function of these selected
coordinates.To talk about densities meaningfully in singular cases,
then, we must select a different base measure. Using the disintegration
theorem we can define a restriction of Lebesgue measure to the rank ⁡ ( Σ
) {\\displaystyle \\operatorname {rank} ({\\boldsymbol {\\Sigma }})}
-dimensional affine subspace of R k {\\displaystyle \\mathbb {R} \^{k}}
where the Gaussian distribution is supported, i.e. { μ + Σ 1 / 2 v : v ∈
R k } {\\displaystyle \\{{\\boldsymbol {\\mu }}+{\\boldsymbol {\\Sigma
\^{1/2}}}\\mathbf {v} :\\mathbf {v} \\in \\mathbb {R} \^{k}\\}} . With
respect to this measure the distribution has the density of the
following motif: f ( x ) = e − 1 2 ( x − μ ) T Σ + ( x − μ ) ( 2 π ) k
det ∗ ( Σ ) {\\displaystyle f(\\mathbf {x} )={\\frac {e\^{-{\\frac
{1}{2}}(\\mathbf {x} -{\\boldsymbol {\\mu }})\^{\\!{\\mathsf
{T}}}{\\boldsymbol {\\Sigma }}\^{+}(\\mathbf {x} -{\\boldsymbol {\\mu
}})}}{\\sqrt {(2\\pi )\^{k}\\det \\nolimits \^{\*}({\\boldsymbol
{\\Sigma }})}}}} where Σ + {\\displaystyle {\\boldsymbol {\\Sigma
}}\^{+}} is the generalized inverse, k {\\displaystyle k} is the rank of
Σ {\\displaystyle {\\boldsymbol {\\Sigma }}} and det ∗ {\\displaystyle
\\det \\nolimits \^{\*}} is the pseudo-determinant. Cumulative
distribution function The notion of cumulative distribution function
(cdf) in dimension 1 can be extended in two ways to the multidimensional
case, based on rectangular and ellipsoidal regions. The first way is to
define the cdf F ( x ) {\\displaystyle F(\\mathbf {x} )} of a random
vector X {\\displaystyle \\mathbf {X} } as the probability that all
components of X {\\displaystyle \\mathbf {X} } are less than or equal to
the corresponding values in the vector x {\\displaystyle \\mathbf {x} }
: F ( x ) = P ( X ≤ x ) , where X ∼ N ( μ , Σ ) . {\\displaystyle
F(\\mathbf {x} )=\\mathbb {P} (\\mathbf {X} \\leq \\mathbf {x} ),\\quad
{\\text{where }}\\mathbf {X} \\sim {\\mathcal {N}}({\\boldsymbol {\\mu
}},\\,{\\boldsymbol {\\Sigma }}).} Though there is no closed form for F
( x ) {\\displaystyle F(\\mathbf {x} )} , there are a number of
algorithms that estimate it numerically.Another way is to define the cdf
F ( r ) {\\displaystyle F(r)} as the probability that a sample lies
inside the ellipsoid determined by its Mahalanobis distance r
{\\displaystyle r} from the Gaussian, a direct generalization of the
standard deviation. In order to compute the values of this function,
closed analytic formulae exist, as follows. Interval The interval for
the multivariate normal distribution yields a region consisting of those
vectors x satisfying ( x − μ ) T Σ − 1 ( x − μ ) ≤ χ k 2 ( p ) .
{\\displaystyle ({\\mathbf {x} }-{\\boldsymbol {\\mu
}})\^{T}{\\boldsymbol {\\Sigma }}\^{-1}({\\mathbf {x} }-{\\boldsymbol
{\\mu }})\\leq \\chi \_{k}\^{2}(p).} Here x {\\displaystyle {\\mathbf
{x} }} is a k {\\displaystyle k} -dimensional vector, μ {\\displaystyle
{\\boldsymbol {\\mu }}} is the known k {\\displaystyle k} -dimensional
mean vector, Σ {\\displaystyle {\\boldsymbol {\\Sigma }}} is the known
covariance matrix and χ k 2 ( p ) {\\displaystyle \\chi \_{k}\^{2}(p)}
is the quantile function for probability p {\\displaystyle p} of the
chi-squared distribution with k {\\displaystyle k} degrees of freedom.
When k = 2 , {\\displaystyle k=2,} the expression defines the interior
of an ellipse and the chi-squared distribution simplifies to an
exponential distribution with mean equal to two (rate equal to half).
Complementary cumulative distribution function (tail distribution) The
complementary cumulative distribution function (ccdf) or the tail
distribution is defined as F ¯ ( x ) = 1 − P ( X ≤ x ) {\\displaystyle
{\\overline {F}}(\\mathbf {x} )=1-\\mathbb {P} (\\mathbf {X} \\leq
\\mathbf {x} )} . When X ∼ N ( μ , Σ ) {\\displaystyle \\mathbf {X}
\\sim {\\mathcal {N}}({\\boldsymbol {\\mu }},\\,{\\boldsymbol {\\Sigma
}})} , then the ccdf can be written as a probability the maximum of
dependent Gaussian variables: F ¯ ( x ) = P ( ⋃ i { X i ≥ x i } ) = P (
max i Y i ≥ 0 ) , where Y ∼ N ( μ − x , Σ ) . {\\displaystyle
{\\overline {F}}(\\mathbf {x} )=\\mathbb {P} \\left(\\bigcup
\_{i}\\{X\_{i}\\geq x\_{i}\\}\\right)=\\mathbb {P} (\\max
\_{i}Y\_{i}\\geq 0),\\quad {\\text{where }}\\mathbf {Y} \\sim {\\mathcal
{N}}({\\boldsymbol {\\mu }}-\\mathbf {x} ,\\,{\\boldsymbol {\\Sigma
}}).} While no simple closed formula exists for computing the ccdf, the
maximum of dependent Gaussian variables can be estimated accurately via
the Monte Carlo method. Properties Probability in different domains The
probability content of the multivariate normal in a quadratic domain
defined by q ( x ) = x ′ Q 2 x + q 1 ′ x + q 0 \> 0 {\\displaystyle
q({\\boldsymbol {x}})={\\boldsymbol {x}}\'\\mathbf {Q\_{2}}
{\\boldsymbol {x}}+{\\boldsymbol {q\_{1}}}\'{\\boldsymbol
{x}}+q\_{0}\>0} (where Q 2 {\\displaystyle \\mathbf {Q\_{2}} } is a
matrix, q 1 {\\displaystyle {\\boldsymbol {q\_{1}}}} is a vector, and q
0 {\\displaystyle q\_{0}} is a scalar), which is relevant for Bayesian
classification/decision theory using Gaussian discriminant analysis, is
given by the generalized chi-squared distribution. The probability
content within any general domain defined by f ( x ) \> 0
{\\displaystyle f({\\boldsymbol {x}})\>0} (where f ( x ) {\\displaystyle
f({\\boldsymbol {x}})} is a general function) can be computed using the
numerical method of ray-tracing (Matlab code). Higher moments The
kth-order moments of x are given by μ 1 , ... , N ( x ) = d e f μ r 1 ,
... , r N ( x ) = d e f E ⁡ \[ ∏ j = 1 N X j r j \] {\\displaystyle \\mu
\_{1,\\ldots ,N}(\\mathbf {x} )\\ {\\stackrel {\\mathrm {def} }{=}}\\
\\mu \_{r\_{1},\\ldots ,r\_{N}}(\\mathbf {x} )\\ {\\stackrel {\\mathrm
{def} }{=}}\\operatorname {E} \\left\[\\prod
\_{j=1}\^{N}X\_{j}\^{r\_{j}}\\right\]} where r1 + r2 + ⋯ + rN = k. The
kth-order central moments are as follows where the sum is taken over all
allocations of the set { 1 , ... , 2 λ } {\\displaystyle
\\left\\{1,\\ldots ,2\\lambda \\right\\}} into λ (unordered) pairs. That
is, for a kth (= 2λ = 6) central moment, one sums the products of λ = 3
covariances (the expected value μ is taken to be 0 in the interests of
parsimony): E ⁡ \[ X 1 X 2 X 3 X 4 X 5 X 6 \] = E ⁡ \[ X 1 X 2 \] E ⁡ \[ X
3 X 4 \] E ⁡ \[ X 5 X 6 \] + E ⁡ \[ X 1 X 2 \] E ⁡ \[ X 3 X 5 \] E ⁡ \[ X 4
X 6 \] + E ⁡ \[ X 1 X 2 \] E ⁡ \[ X 3 X 6 \] E ⁡ \[ X 4 X 5 \] + E ⁡ \[ X 1
X 3 \] E ⁡ \[ X 2 X 4 \] E ⁡ \[ X 5 X 6 \] + E ⁡ \[ X 1 X 3 \] E ⁡ \[ X 2 X
5 \] E ⁡ \[ X 4 X 6 \] + E ⁡ \[ X 1 X 3 \] E ⁡ \[ X 2 X 6 \] E ⁡ \[ X 4 X 5
\] + E ⁡ \[ X 1 X 4 \] E ⁡ \[ X 2 X 3 \] E ⁡ \[ X 5 X 6 \] + E ⁡ \[ X 1 X 4
\] E ⁡ \[ X 2 X 5 \] E ⁡ \[ X 3 X 6 \] + E ⁡ \[ X 1 X 4 \] E ⁡ \[ X 2 X 6 \]
E ⁡ \[ X 3 X 5 \] + E ⁡ \[ X 1 X 5 \] E ⁡ \[ X 2 X 3 \] E ⁡ \[ X 4 X 6 \] +
E ⁡ \[ X 1 X 5 \] E ⁡ \[ X 2 X 4 \] E ⁡ \[ X 3 X 6 \] + E ⁡ \[ X 1 X 5 \] E ⁡
\[ X 2 X 6 \] E ⁡ \[ X 3 X 4 \] + E ⁡ \[ X 1 X 6 \] E ⁡ \[ X 2 X 3 \] E ⁡ \[
X 4 X 5 \] + E ⁡ \[ X 1 X 6 \] E ⁡ \[ X 2 X 4 \] E ⁡ \[ X 3 X 5 \] + E ⁡ \[
X 1 X 6 \] E ⁡ \[ X 2 X 5 \] E ⁡ \[ X 3 X 4 \] . {\\displaystyle
{\\begin{aligned}&\\operatorname {E}
\[X\_{1}X\_{2}X\_{3}X\_{4}X\_{5}X\_{6}\]\\\\\[8pt\]={}&\\operatorname
{E} \[X\_{1}X\_{2}\]\\operatorname {E} \[X\_{3}X\_{4}\]\\operatorname
{E} \[X\_{5}X\_{6}\]+\\operatorname {E} \[X\_{1}X\_{2}\]\\operatorname
{E} \[X\_{3}X\_{5}\]\\operatorname {E} \[X\_{4}X\_{6}\]+\\operatorname
{E} \[X\_{1}X\_{2}\]\\operatorname {E} \[X\_{3}X\_{6}\]\\operatorname
{E} \[X\_{4}X\_{5}\]\\\\\[4pt\]&{}+\\operatorname {E}
\[X\_{1}X\_{3}\]\\operatorname {E} \[X\_{2}X\_{4}\]\\operatorname {E}
\[X\_{5}X\_{6}\]+\\operatorname {E} \[X\_{1}X\_{3}\]\\operatorname {E}
\[X\_{2}X\_{5}\]\\operatorname {E} \[X\_{4}X\_{6}\]+\\operatorname {E}
\[X\_{1}X\_{3}\]\\operatorname {E} \[X\_{2}X\_{6}\]\\operatorname {E}
\[X\_{4}X\_{5}\]\\\\\[4pt\]&{}+\\operatorname {E}
\[X\_{1}X\_{4}\]\\operatorname {E} \[X\_{2}X\_{3}\]\\operatorname {E}
\[X\_{5}X\_{6}\]+\\operatorname {E} \[X\_{1}X\_{4}\]\\operatorname {E}
\[X\_{2}X\_{5}\]\\operatorname {E} \[X\_{3}X\_{6}\]+\\operatorname {E}
\[X\_{1}X\_{4}\]\\operatorname {E} \[X\_{2}X\_{6}\]\\operatorname {E}
\[X\_{3}X\_{5}\]\\\\\[4pt\]&{}+\\operatorname {E}
\[X\_{1}X\_{5}\]\\operatorname {E} \[X\_{2}X\_{3}\]\\operatorname {E}
\[X\_{4}X\_{6}\]+\\operatorname {E} \[X\_{1}X\_{5}\]\\operatorname {E}
\[X\_{2}X\_{4}\]\\operatorname {E} \[X\_{3}X\_{6}\]+\\operatorname {E}
\[X\_{1}X\_{5}\]\\operatorname {E} \[X\_{2}X\_{6}\]\\operatorname {E}
\[X\_{3}X\_{4}\]\\\\\[4pt\]&{}+\\operatorname {E}
\[X\_{1}X\_{6}\]\\operatorname {E} \[X\_{2}X\_{3}\]\\operatorname {E}
\[X\_{4}X\_{5}\]+\\operatorname {E} \[X\_{1}X\_{6}\]\\operatorname {E}
\[X\_{2}X\_{4}\]\\operatorname {E} \[X\_{3}X\_{5}\]+\\operatorname {E}
\[X\_{1}X\_{6}\]\\operatorname {E} \[X\_{2}X\_{5}\]\\operatorname {E}
\[X\_{3}X\_{4}\].\\end{aligned}}} This yields ( 2 λ − 1 ) ! 2 λ − 1 ( λ
− 1 ) ! {\\displaystyle {\\tfrac {(2\\lambda -1)!}{2\^{\\lambda
-1}(\\lambda -1)!}}} terms in the sum (15 in the above case), each being
the product of λ (in this case 3) covariances. For fourth order moments
(four variables) there are three terms. For sixth-order moments there
are 3 × 5 = 15 terms, and for eighth-order moments there are 3 × 5 × 7 =
105 terms. The covariances are then determined by replacing the terms of
the list \[ 1 , ... , 2 λ \] {\\displaystyle \[1,\\ldots ,2\\lambda \]}
by the corresponding terms of the list consisting of r1 ones, then r2
twos, etc.. To illustrate this, examine the following 4th-order central
moment case: E ⁡ \[ X i 4 \] = 3 σ i i 2 E ⁡ \[ X i 3 X j \] = 3 σ i i σ i
j E ⁡ \[ X i 2 X j 2 \] = σ i i σ j j + 2 σ i j 2 E ⁡ \[ X i 2 X j X k \]
= σ i i σ j k + 2 σ i j σ i k E ⁡ \[ X i X j X k X n \] = σ i j σ k n + σ
i k σ j n + σ i n σ j k . {\\displaystyle
{\\begin{aligned}\\operatorname {E}
\\left\[X\_{i}\^{4}\\right\]&=3\\sigma
\_{ii}\^{2}\\\\\[4pt\]\\operatorname {E}
\\left\[X\_{i}\^{3}X\_{j}\\right\]&=3\\sigma \_{ii}\\sigma
\_{ij}\\\\\[4pt\]\\operatorname {E}
\\left\[X\_{i}\^{2}X\_{j}\^{2}\\right\]&=\\sigma \_{ii}\\sigma
\_{jj}+2\\sigma \_{ij}\^{2}\\\\\[4pt\]\\operatorname {E}
\\left\[X\_{i}\^{2}X\_{j}X\_{k}\\right\]&=\\sigma \_{ii}\\sigma
\_{jk}+2\\sigma \_{ij}\\sigma \_{ik}\\\\\[4pt\]\\operatorname {E}
\\left\[X\_{i}X\_{j}X\_{k}X\_{n}\\right\]&=\\sigma \_{ij}\\sigma
\_{kn}+\\sigma \_{ik}\\sigma \_{jn}+\\sigma \_{in}\\sigma
\_{jk}.\\end{aligned}}} where σ i j {\\displaystyle \\sigma \_{ij}} is
the covariance of Xi and Xj. With the above method one first finds the
general case for a kth moment with k different X variables, E \[ X i X j
X k X n \] {\\displaystyle E\\left\[X\_{i}X\_{j}X\_{k}X\_{n}\\right\]} ,
and then one simplifies this accordingly. For example, for E ⁡ \[ X i 2 X
k X n \] {\\displaystyle \\operatorname {E} \[X\_{i}\^{2}X\_{k}X\_{n}\]}
, one lets Xi = Xj and one uses the fact that σ i i = σ i 2
{\\displaystyle \\sigma \_{ii}=\\sigma \_{i}\^{2}} . Functions of a
normal vector A quadratic form of a normal vector x {\\displaystyle
{\\boldsymbol {x}}} , q ( x ) = x ′ Q 2 x + q 1 ′ x + q 0
{\\displaystyle q({\\boldsymbol {x}})={\\boldsymbol {x}}\'\\mathbf
{Q\_{2}} {\\boldsymbol {x}}+{\\boldsymbol {q\_{1}}}\'{\\boldsymbol
{x}}+q\_{0}} (where Q 2 {\\displaystyle \\mathbf {Q\_{2}} } is a matrix,
q 1 {\\displaystyle {\\boldsymbol {q\_{1}}}} is a vector, and q 0
{\\displaystyle q\_{0}} is a scalar), is a generalized chi-squared
variable. If f ( x ) {\\displaystyle f({\\boldsymbol {x}})} is a general
scalar-valued function of a normal vector, its probability density
function, cumulative distribution function, and inverse cumulative
distribution function can be computed with the numerical method of
ray-tracing (Matlab code). Likelihood function If the mean and
covariance matrix are known, the log likelihood of an observed vector x
{\\displaystyle {\\boldsymbol {x}}} is simply the log of the probability
density function: ln ⁡ L ( x ) = − 1 2 \[ ln ⁡ ( \| Σ \| ) + ( x − μ ) ′ Σ
− 1 ( x − μ ) + k ln ⁡ ( 2 π ) \] {\\displaystyle \\ln L({\\boldsymbol
{x}})=-{\\frac {1}{2}}\\left\[\\ln(\|{\\boldsymbol {\\Sigma
}}\|\\,)+({\\boldsymbol {x}}-{\\boldsymbol {\\mu }})\'{\\boldsymbol
{\\Sigma }}\^{-1}({\\boldsymbol {x}}-{\\boldsymbol {\\mu }})+k\\ln(2\\pi
)\\right\]} ,The circularly symmetric version of the noncentral complex
case, where z {\\displaystyle {\\boldsymbol {z}}} is a vector of complex
numbers, would be ln ⁡ L ( z ) = − ln ⁡ ( \| Σ \| ) − ( z − μ ) † Σ − 1 (
z − μ ) − k ln ⁡ ( π ) {\\displaystyle \\ln L({\\boldsymbol
{z}})=-\\ln(\|{\\boldsymbol {\\Sigma }}\|\\,)-({\\boldsymbol
{z}}-{\\boldsymbol {\\mu }})\^{\\dagger }{\\boldsymbol {\\Sigma
}}\^{-1}({\\boldsymbol {z}}-{\\boldsymbol {\\mu }})-k\\ln(\\pi )} i.e.
with the conjugate transpose (indicated by † {\\displaystyle \\dagger }
) replacing the normal transpose (indicated by ′ {\\displaystyle \'} ).
This is slightly different than in the real case, because the circularly
symmetric version of the complex normal distribution has a slightly
different form for the normalization constant. A similar notation is
used for multiple linear regression.Since the log likelihood of a normal
vector is a quadratic form of the normal vector, it is distributed as a
generalized chi-squared variable. Differential entropy The differential
entropy of the multivariate normal distribution is h ( f ) = − ∫ − ∞ ∞ ∫
− ∞ ∞ ⋯ ∫ − ∞ ∞ f ( x ) ln ⁡ f ( x ) d x , = 1 2 ln ⁡ ( \| ( 2 π e ) Σ \|
) = 1 2 ln ⁡ ( ( 2 π e ) k \| Σ \| ) = k 2 ln ⁡ ( 2 π e ) + 1 2 ln ⁡ ( \| Σ
\| ) = k 2 + k 2 ln ⁡ ( 2 π ) + 1 2 ln ⁡ ( \| Σ \| ) {\\displaystyle
{\\begin{aligned}h\\left(f\\right)&=-\\int \_{-\\infty }\^{\\infty
}\\int \_{-\\infty }\^{\\infty }\\cdots \\int \_{-\\infty }\^{\\infty
}f(\\mathbf {x} )\\ln f(\\mathbf {x} )\\,d\\mathbf {x} ,\\\\&={\\frac
{1}{2}}\\ln \\left(\\left\|\\left(2\\pi e\\right){\\boldsymbol {\\Sigma
}}\\right\|\\right)={\\frac {1}{2}}\\ln \\left(\\left(2\\pi
e\\right)\^{k}\\left\|{\\boldsymbol {\\Sigma }}\\right\|\\right)={\\frac
{k}{2}}\\ln \\left(2\\pi e\\right)+{\\frac {1}{2}}\\ln
\\left(\\left\|{\\boldsymbol {\\Sigma }}\\right\|\\right)={\\frac
{k}{2}}+{\\frac {k}{2}}\\ln \\left(2\\pi \\right)+{\\frac {1}{2}}\\ln
\\left(\\left\|{\\boldsymbol {\\Sigma
}}\\right\|\\right)\\\\\\end{aligned}}} where the bars denote the matrix
determinant and k is the dimensionality of the vector space.
Kullback--Leibler divergence The Kullback--Leibler divergence from N 1 (
μ 1 , Σ 1 ) {\\displaystyle {\\mathcal {N}}\_{1}({\\boldsymbol {\\mu
}}\_{1},{\\boldsymbol {\\Sigma }}\_{1})} to N 0 ( μ 0 , Σ 0 )
{\\displaystyle {\\mathcal {N}}\_{0}({\\boldsymbol {\\mu
}}\_{0},{\\boldsymbol {\\Sigma }}\_{0})} , for non-singular matrices Σ1
and Σ0, is: D KL ( N 0 ∥ N 1 ) = 1 2 { tr ⁡ ( Σ 1 − 1 Σ 0 ) + ( μ 1 − μ 0
) T Σ 1 − 1 ( μ 1 − μ 0 ) − k + ln ⁡ \| Σ 1 \| \| Σ 0 \| } ,
{\\displaystyle D\_{\\text{KL}}({\\mathcal {N}}\_{0}\\parallel
{\\mathcal {N}}\_{1})={1 \\over 2}\\left\\{\\operatorname {tr}
\\left({\\boldsymbol {\\Sigma }}\_{1}\^{-1}{\\boldsymbol {\\Sigma
}}\_{0}\\right)+\\left({\\boldsymbol {\\mu }}\_{1}-{\\boldsymbol {\\mu
}}\_{0}\\right)\^{\\rm {T}}{\\boldsymbol {\\Sigma
}}\_{1}\^{-1}({\\boldsymbol {\\mu }}\_{1}-{\\boldsymbol {\\mu
}}\_{0})-k+\\ln {\|{\\boldsymbol {\\Sigma }}\_{1}\| \\over
\|{\\boldsymbol {\\Sigma }}\_{0}\|}\\right\\},} where k {\\displaystyle
k} is the dimension of the vector space. The logarithm must be taken to
base e since the two terms following the logarithm are themselves base-e
logarithms of expressions that are either factors of the density
function or otherwise arise naturally. The equation therefore gives a
result measured in nats. Dividing the entire expression above by loge 2
yields the divergence in bits. When μ 1 = μ 0 {\\displaystyle
{\\boldsymbol {\\mu }}\_{1}={\\boldsymbol {\\mu }}\_{0}} , D KL ( N 0 ∥
N 1 ) = 1 2 { tr ⁡ ( Σ 1 − 1 Σ 0 ) − k + ln ⁡ \| Σ 1 \| \| Σ 0 \| } .
{\\displaystyle D\_{\\text{KL}}({\\mathcal {N}}\_{0}\\parallel
{\\mathcal {N}}\_{1})={1 \\over 2}\\left\\{\\operatorname {tr}
\\left({\\boldsymbol {\\Sigma }}\_{1}\^{-1}{\\boldsymbol {\\Sigma
}}\_{0}\\right)-k+\\ln {\|{\\boldsymbol {\\Sigma }}\_{1}\| \\over
\|{\\boldsymbol {\\Sigma }}\_{0}\|}\\right\\}.} Mutual information The
mutual information of a distribution is a special case of the
Kullback--Leibler divergence in which P {\\displaystyle P} is the full
multivariate distribution and Q {\\displaystyle Q} is the product of the
1-dimensional marginal distributions. In the notation of the
Kullback--Leibler divergence section of this article, Σ 1
{\\displaystyle {\\boldsymbol {\\Sigma }}\_{1}} is a diagonal matrix
with the diagonal entries of Σ 0 {\\displaystyle {\\boldsymbol {\\Sigma
}}\_{0}} , and μ 1 = μ 0 {\\displaystyle {\\boldsymbol {\\mu
}}\_{1}={\\boldsymbol {\\mu }}\_{0}} . The resulting formula for mutual
information is: I ( X ) = − 1 2 ln ⁡ \| ρ 0 \| , {\\displaystyle
I({\\boldsymbol {X}})=-{1 \\over 2}\\ln \|{\\boldsymbol {\\rho
}}\_{0}\|,} where ρ 0 {\\displaystyle {\\boldsymbol {\\rho }}\_{0}} is
the correlation matrix constructed from Σ 0 {\\displaystyle
{\\boldsymbol {\\Sigma }}\_{0}} .In the bivariate case the expression
for the mutual information is: I ( x ; y ) = − 1 2 ln ⁡ ( 1 − ρ 2 ) .
{\\displaystyle I(x;y)=-{1 \\over 2}\\ln(1-\\rho \^{2}).} Joint
normality Normally distributed and independent If X {\\displaystyle X}
and Y {\\displaystyle Y} are normally distributed and independent, this
implies they are \"jointly normally distributed\", i.e., the pair ( X ,
Y ) {\\displaystyle (X,Y)} must have multivariate normal distribution.
However, a pair of jointly normally distributed variables need not be
independent (would only be so if uncorrelated, ρ = 0 {\\displaystyle
\\rho =0} ). Two normally distributed random variables need not be
jointly bivariate normal The fact that two random variables X
{\\displaystyle X} and Y {\\displaystyle Y} both have a normal
distribution does not imply that the pair ( X , Y ) {\\displaystyle
(X,Y)} has a joint normal distribution. A simple example is one in which
X has a normal distribution with expected value 0 and variance 1, and Y
= X {\\displaystyle Y=X} if \| X \| \> c {\\displaystyle \|X\|\>c} and Y
= − X {\\displaystyle Y=-X} if \| X \| \< c {\\displaystyle \|X\| 0
{\\displaystyle c\>0} . There are similar counterexamples for more than
two random variables. In general, they sum to a mixture model.
Correlations and independence In general, random variables may be
uncorrelated but statistically dependent. But if a random vector has a
multivariate normal distribution then any two or more of its components
that are uncorrelated are independent. This implies that any two or more
of its components that are pairwise independent are independent. But, as
pointed out just above, it is not true that two random variables that
are (separately, marginally) normally distributed and uncorrelated are
independent. Conditional distributions If N-dimensional x is partitioned
as follows x = \[ x 1 x 2 \] with sizes \[ q × 1 ( N − q ) × 1 \]
{\\displaystyle \\mathbf {x} ={\\begin{bmatrix}\\mathbf {x}
\_{1}\\\\\\mathbf {x} \_{2}\\end{bmatrix}}{\\text{ with sizes
}}{\\begin{bmatrix}q\\times 1\\\\(N-q)\\times 1\\end{bmatrix}}} and
accordingly μ and Σ are partitioned as follows μ = \[ μ 1 μ 2 \] with
sizes \[ q × 1 ( N − q ) × 1 \] {\\displaystyle {\\boldsymbol {\\mu
}}={\\begin{bmatrix}{\\boldsymbol {\\mu }}\_{1}\\\\{\\boldsymbol {\\mu
}}\_{2}\\end{bmatrix}}{\\text{ with sizes }}{\\begin{bmatrix}q\\times
1\\\\(N-q)\\times 1\\end{bmatrix}}} Σ = \[ Σ 11 Σ 12 Σ 21 Σ 22 \] with
sizes \[ q × q q × ( N − q ) ( N − q ) × q ( N − q ) × ( N − q ) \]
{\\displaystyle {\\boldsymbol {\\Sigma }}={\\begin{bmatrix}{\\boldsymbol
{\\Sigma }}\_{11}&{\\boldsymbol {\\Sigma }}\_{12}\\\\{\\boldsymbol
{\\Sigma }}\_{21}&{\\boldsymbol {\\Sigma }}\_{22}\\end{bmatrix}}{\\text{
with sizes }}{\\begin{bmatrix}q\\times q&q\\times (N-q)\\\\(N-q)\\times
q&(N-q)\\times (N-q)\\end{bmatrix}}} then the distribution of x1
conditional on x2 = a is multivariate normal (x1 \| x2 = a) \~ N(μ, Σ)
where μ ¯ = μ 1 + Σ 12 Σ 22 − 1 ( a − μ 2 ) {\\displaystyle {\\bar
{\\boldsymbol {\\mu }}}={\\boldsymbol {\\mu }}\_{1}+{\\boldsymbol
{\\Sigma }}\_{12}{\\boldsymbol {\\Sigma }}\_{22}\^{-1}\\left(\\mathbf
{a} -{\\boldsymbol {\\mu }}\_{2}\\right)} and covariance matrix Σ ¯ = Σ
11 − Σ 12 Σ 22 − 1 Σ 21 . {\\displaystyle {\\overline {\\boldsymbol
{\\Sigma }}}={\\boldsymbol {\\Sigma }}\_{11}-{\\boldsymbol {\\Sigma
}}\_{12}{\\boldsymbol {\\Sigma }}\_{22}\^{-1}{\\boldsymbol {\\Sigma
}}\_{21}.} Here Σ 22 − 1 {\\displaystyle {\\boldsymbol {\\Sigma
}}\_{22}\^{-1}} is the generalized inverse of Σ 22 {\\displaystyle
{\\boldsymbol {\\Sigma }}\_{22}} . The matrix Σ ¯ {\\displaystyle
{\\overline {\\boldsymbol {\\Sigma }}}} is the Schur complement of Σ22
in Σ. That is, the equation above is equivalent to inverting the overall
covariance matrix, dropping the rows and columns corresponding to the
variables being conditioned upon, and inverting back to get the
conditional covariance matrix. Note that knowing that x2 = a alters the
variance, though the new variance does not depend on the specific value
of a; perhaps more surprisingly, the mean is shifted by Σ 12 Σ 22 − 1 (
a − μ 2 ) {\\displaystyle {\\boldsymbol {\\Sigma }}\_{12}{\\boldsymbol
{\\Sigma }}\_{22}\^{-1}\\left(\\mathbf {a} -{\\boldsymbol {\\mu
}}\_{2}\\right)} ; compare this with the situation of not knowing the
value of a, in which case x1 would have distribution N q ( μ 1 , Σ 11 )
{\\displaystyle {\\mathcal {N}}\_{q}\\left({\\boldsymbol {\\mu
}}\_{1},{\\boldsymbol {\\Sigma }}\_{11}\\right)} . An interesting fact
derived in order to prove this result, is that the random vectors x 2
{\\displaystyle \\mathbf {x} \_{2}} and y 1 = x 1 − Σ 12 Σ 22 − 1 x 2
{\\displaystyle \\mathbf {y} \_{1}=\\mathbf {x} \_{1}-{\\boldsymbol
{\\Sigma }}\_{12}{\\boldsymbol {\\Sigma }}\_{22}\^{-1}\\mathbf {x}
\_{2}} are independent. The matrix Σ12Σ22−1 is known as the matrix of
regression coefficients. Bivariate case In the bivariate case where x is
partitioned into X 1 {\\displaystyle X\_{1}} and X 2 {\\displaystyle
X\_{2}} , the conditional distribution of X 1 {\\displaystyle X\_{1}}
given X 2 {\\displaystyle X\_{2}} is X 1 ∣ X 2 = a ∼ N ( μ 1 + σ 1 σ 2 ρ
( a − μ 2 ) , ( 1 − ρ 2 ) σ 1 2 ) . {\\displaystyle X\_{1}\\mid
X\_{2}=a\\ \\sim \\ {\\mathcal {N}}\\left(\\mu \_{1}+{\\frac {\\sigma
\_{1}}{\\sigma \_{2}}}\\rho (a-\\mu \_{2}),\\,(1-\\rho \^{2})\\sigma
\_{1}\^{2}\\right).} where ρ {\\displaystyle \\rho } is the correlation
coefficient between X 1 {\\displaystyle X\_{1}} and X 2 {\\displaystyle
X\_{2}} . Bivariate conditional expectation In the general case ( X 1 X
2 ) ∼ N ( ( μ 1 μ 2 ) , ( σ 1 2 ρ σ 1 σ 2 ρ σ 1 σ 2 σ 2 2 ) )
{\\displaystyle {\\begin{pmatrix}X\_{1}\\\\X\_{2}\\end{pmatrix}}\\sim
{\\mathcal {N}}\\left({\\begin{pmatrix}\\mu \_{1}\\\\\\mu
\_{2}\\end{pmatrix}},{\\begin{pmatrix}\\sigma \_{1}\^{2}&\\rho \\sigma
\_{1}\\sigma \_{2}\\\\\\rho \\sigma \_{1}\\sigma \_{2}&\\sigma
\_{2}\^{2}\\end{pmatrix}}\\right)} The conditional expectation of X1
given X2 is: E ⁡ ( X 1 ∣ X 2 = x 2 ) = μ 1 + ρ σ 1 σ 2 ( x 2 − μ 2 )
{\\displaystyle \\operatorname {E} (X\_{1}\\mid X\_{2}=x\_{2})=\\mu
\_{1}+\\rho {\\frac {\\sigma \_{1}}{\\sigma \_{2}}}(x\_{2}-\\mu \_{2})}
Proof: the result is obtained by taking the expectation of the
conditional distribution X 1 ∣ X 2 {\\displaystyle X\_{1}\\mid X\_{2}}
above. In the centered case with unit variances ( X 1 X 2 ) ∼ N ( ( 0 0
) , ( 1 ρ ρ 1 ) ) {\\displaystyle
{\\begin{pmatrix}X\_{1}\\\\X\_{2}\\end{pmatrix}}\\sim {\\mathcal
{N}}\\left({\\begin{pmatrix}0\\\\0\\end{pmatrix}},{\\begin{pmatrix}1&\\rho
\\\\\\rho &1\\end{pmatrix}}\\right)} The conditional expectation of X1
given X2 is E ⁡ ( X 1 ∣ X 2 = x 2 ) = ρ x 2 {\\displaystyle
\\operatorname {E} (X\_{1}\\mid X\_{2}=x\_{2})=\\rho x\_{2}} and the
conditional variance is var ⁡ ( X 1 ∣ X 2 = x 2 ) = 1 − ρ 2 ;
{\\displaystyle \\operatorname {var} (X\_{1}\\mid X\_{2}=x\_{2})=1-\\rho
\^{2};} thus the conditional variance does not depend on x2. The
conditional expectation of X1 given that X2 is smaller/bigger than z
is:: 367  E ⁡ ( X 1 ∣ X 2 \< z ) = − ρ φ ( z ) Φ ( z ) , {\\displaystyle
\\operatorname {E} (X\_{1}\\mid X\_{2} z ) = ρ φ ( z ) ( 1 − Φ ( z ) ) ,
{\\displaystyle \\operatorname {E} (X\_{1}\\mid X\_{2}\>z)=\\rho
{\\varphi (z) \\over (1-\\Phi (z))},} where the final ratio here is
called the inverse Mills ratio. Proof: the last two results are obtained
using the result E ⁡ ( X 1 ∣ X 2 = x 2 ) = ρ x 2 {\\displaystyle
\\operatorname {E} (X\_{1}\\mid X\_{2}=x\_{2})=\\rho x\_{2}} , so that E
⁡( X 1 ∣ X 2 \< z ) = ρ E ( X 2 ∣ X 2 \< z ) {\\displaystyle
\\operatorname {E} (X\_{1}\\mid X\_{2}
