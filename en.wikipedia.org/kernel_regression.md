In statistics, kernel regression is a non-parametric technique to
estimate the conditional expectation of a random variable. The objective
is to find a non-linear relation between a pair of random variables X
and Y. In any nonparametric regression, the conditional expectation of a
variable Y {\\displaystyle Y} relative to a variable X {\\displaystyle
X} may be written: E ⁡ ( Y ∣ X ) = m ( X ) {\\displaystyle \\operatorname
{E} (Y\\mid X)=m(X)} where m {\\displaystyle m} is an unknown function.
Nadaraya--Watson kernel regression Nadaraya and Watson, both in 1964,
proposed to estimate m {\\displaystyle m} as a locally weighted average,
using a kernel as a weighting function. The Nadaraya--Watson estimator
is: m \^ h ( x ) = ∑ i = 1 n K h ( x − x i ) y i ∑ i = 1 n K h ( x − x i
) {\\displaystyle {\\widehat {m}}\_{h}(x)={\\frac {\\sum
\_{i=1}\^{n}K\_{h}(x-x\_{i})y\_{i}}{\\sum
\_{i=1}\^{n}K\_{h}(x-x\_{i})}}} where K h ( t ) = 1 h K ( t h )
{\\displaystyle K\_{h}(t)={\\frac {1}{h}}K\\left({\\frac
{t}{h}}\\right)} is a kernel with a bandwidth h {\\displaystyle h} such
that K ( ⋅ ) {\\displaystyle K(\\cdot )} is of order at least 1, that is
∫ − ∞ ∞ u K ( u ) d u = 0 {\\displaystyle \\int \_{-\\infty }\^{\\infty
}uK(u)du=0} . Derivation E ⁡ ( Y ∣ X = x ) = ∫ y f ( y ∣ x ) d y = ∫ y f
( x , y ) f ( x ) d y {\\displaystyle \\operatorname {E} (Y\\mid
X=x)=\\int yf(y\\mid x)\\,dy=\\int y{\\frac {f(x,y)}{f(x)}}\\,dy} Using
the kernel density estimation for the joint distribution f(x,y) and f(x)
with a kernel K, f \^ ( x , y ) = 1 n ∑ i = 1 n K h ( x − x i ) K h ( y
− y i ) , {\\displaystyle {\\hat {f}}(x,y)={\\frac {1}{n}}\\sum
\_{i=1}\^{n}K\_{h}(x-x\_{i})K\_{h}(y-y\_{i}),} f \^ ( x ) = 1 n ∑ i = 1
n K h ( x − x i ) , {\\displaystyle {\\hat {f}}(x)={\\frac {1}{n}}\\sum
\_{i=1}\^{n}K\_{h}(x-x\_{i}),} we get E \^ ⁡ ( Y ∣ X = x ) = ∫ y ∑ i = 1
n K h ( x − x i ) K h ( y − y i ) ∑ j = 1 n K h ( x − x j ) d y , = ∑ i
= 1 n K h ( x − x i ) ∫ y K h ( y − y i ) d y ∑ j = 1 n K h ( x − x j )
, = ∑ i = 1 n K h ( x − x i ) y i ∑ j = 1 n K h ( x − x j ) ,
{\\displaystyle {\\begin{aligned}\\operatorname {\\hat {E}} (Y\\mid
X=x)&=\\int {\\frac {y\\sum
\_{i=1}\^{n}K\_{h}(x-x\_{i})K\_{h}(y-y\_{i})}{\\sum
\_{j=1}\^{n}K\_{h}(x-x\_{j})}}\\,dy,\\\\\[6pt\]&={\\frac {\\sum
\_{i=1}\^{n}K\_{h}(x-x\_{i})\\int y\\,K\_{h}(y-y\_{i})\\,dy}{\\sum
\_{j=1}\^{n}K\_{h}(x-x\_{j})}},\\\\\[6pt\]&={\\frac {\\sum
\_{i=1}\^{n}K\_{h}(x-x\_{i})y\_{i}}{\\sum
\_{j=1}\^{n}K\_{h}(x-x\_{j})}},\\end{aligned}}} which is the
Nadaraya--Watson estimator. Priestley--Chao kernel estimator m \^ P C (
x ) = h − 1 ∑ i = 2 n ( x i − x i − 1 ) K ( x − x i h ) y i
{\\displaystyle {\\widehat {m}}\_{PC}(x)=h\^{-1}\\sum
\_{i=2}\^{n}(x\_{i}-x\_{i-1})K\\left({\\frac
{x-x\_{i}}{h}}\\right)y\_{i}} where h {\\displaystyle h} is the
bandwidth (or smoothing parameter). Gasser--Müller kernel estimator m \^
G M ( x ) = h − 1 ∑ i = 1 n \[ ∫ s i − 1 s i K ( x − u h ) d u \] y i
{\\displaystyle {\\widehat {m}}\_{GM}(x)=h\^{-1}\\sum
\_{i=1}\^{n}\\left\[\\int \_{s\_{i-1}}\^{s\_{i}}K\\left({\\frac
{x-u}{h}}\\right)\\,du\\right\]y\_{i}} where s i = x i − 1 + x i 2 .
{\\displaystyle s\_{i}={\\frac {x\_{i-1}+x\_{i}}{2}}.} Example This
example is based upon Canadian cross-section wage data consisting of a
random sample taken from the 1971 Canadian Census Public Use Tapes for
male individuals having common education (grade 13). There are 205
observations in total. The figure to the right shows the estimated
regression function using a second order Gaussian kernel along with
asymptotic variability bounds. Script for example The following commands
of the R programming language use the npreg() function to deliver
optimal smoothing and to create the figure given above. These commands
can be entered at the command prompt via cut and paste. Related
According to David Salsburg, the algorithms used in kernel regression
were independently developed and used in fuzzy systems: \"Coming up with
almost exactly the same computer algorithm, fuzzy systems and kernel
density-based regressions appear to have been developed completely
independently of one another.\" Statistical implementation GNU Octave
mathematical program package Julia: KernelEstimator.jl MATLAB: A free
MATLAB toolbox with implementation of kernel regression, kernel density
estimation, kernel estimation of hazard function and many others is
available on these pages (this toolbox is a part of the book ). Python:
the KernelReg class for mixed data types in the
statsmodels.nonparametric sub-package (includes other kernel density
related classes), the package kernel_regression as an extension of
scikit-learn (inefficient memory-wise, useful only for small datasets)
R: the function npreg of the np package can perform kernel regression.
Stata: npregress, kernreg2 See also Kernel smoother Local regression
References Further reading Henderson, Daniel J.; Parmeter, Christopher
F. (2015). Applied Nonparametric Econometrics. Cambridge University
Press. ISBN 978-1-107-01025-3. Li, Qi; Racine, Jeffrey S. (2007).
Nonparametric Econometrics: Theory and Practice. Princeton University
Press. ISBN 978-0-691-12161-1. Pagan, A.; Ullah, A. (1999).
Nonparametric Econometrics. Cambridge University Press. ISBN
0-521-35564-8. Racine, Jeffrey S. (2019). An Introduction to the
Advanced Theory and Practice of Nonparametric Econometrics: A Replicable
Approach Using R. Cambridge University Press. ISBN 9781108483407.
Simonoff, Jeffrey S. (1996). Smoothing Methods in Statistics. Springer.
ISBN 0-387-94716-7. External links Scale-adaptive kernel regression
(with Matlab software). Tutorial of Kernel regression using spreadsheet
(with Microsoft Excel). An online kernel regression demonstration
Requires .NET 3.0 or later. Kernel regression with automatic bandwidth
selection (with Python)
