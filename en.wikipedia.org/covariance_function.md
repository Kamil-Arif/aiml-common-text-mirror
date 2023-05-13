In probability theory and statistics, the covariance function describes
how much two random variables change together (their covariance) with
varying spatial or temporal separation. For a random field or stochastic
process Z(x) on a domain D, a covariance function C(x, y) gives the
covariance of the values of the random field at the two locations x and
y: C ( x , y ) := cov ⁡ ( Z ( x ) , Z ( y ) ) = E \[ { Z ( x ) − E \[ Z (
x ) \] } ⋅ { Z ( y ) − E \[ Z ( y ) \] } \] . {\\displaystyle
C(x,y):=\\operatorname {cov} (Z(x),Z(y))=\\mathbb {E}
\\left\[\\{Z(x)-\\mathbb {E} \[Z(x)\]\\}\\cdot \\{Z(y)-\\mathbb {E}
\[Z(y)\]\\}\\right\].\\,} The same C(x, y) is called the autocovariance
function in two instances: in time series (to denote exactly the same
concept except that x and y refer to locations in time rather than in
space), and in multivariate random fields (to refer to the covariance of
a variable with itself, as opposed to the cross covariance between two
different variables at different locations, Cov(Z(x1), Y(x2))).
Admissibility For locations x1, x2, ..., xN ∈ D the variance of every
linear combination X = ∑ i = 1 N w i Z ( x i ) {\\displaystyle X=\\sum
\_{i=1}\^{N}w\_{i}Z(x\_{i})} can be computed as var ⁡ ( X ) = ∑ i = 1 N ∑
j = 1 N w i C ( x i , x j ) w j . {\\displaystyle \\operatorname {var}
(X)=\\sum \_{i=1}\^{N}\\sum \_{j=1}\^{N}w\_{i}C(x\_{i},x\_{j})w\_{j}.} A
function is a valid covariance function if and only if this variance is
non-negative for all possible choices of N and weights w1, ..., wN. A
function with this property is called positive semidefinite.
Simplifications with stationarity In case of a weakly stationary random
field, where C ( x i , x j ) = C ( x i + h , x j + h ) {\\displaystyle
C(x\_{i},x\_{j})=C(x\_{i}+h,x\_{j}+h)\\,} for any lag h, the covariance
function can be represented by a one-parameter function C s ( h ) = C (
0 , h ) = C ( x , x + h ) {\\displaystyle C\_{s}(h)=C(0,h)=C(x,x+h)\\,}
which is called a covariogram and also a covariance function. Implicitly
the C(xi, xj) can be computed from Cs(h) by: C ( x , y ) = C s ( y − x )
. {\\displaystyle C(x,y)=C\_{s}(y-x).\\,} The positive definiteness of
this single-argument version of the covariance function can be checked
by Bochner\'s theorem. Parametric families of covariance functions For a
given variance σ 2 {\\displaystyle \\sigma \^{2}} , a simple stationary
parametric covariance function is the \"exponential covariance
function\" C ( d ) = σ 2 exp ⁡ ( − d / V ) {\\displaystyle C(d)=\\sigma
\^{2}\\exp(-d/V)} where V is a scaling parameter (correlation length),
and d = d(x,y) is the distance between two points. Sample paths of a
Gaussian process with the exponential covariance function are not
smooth. The \"squared exponential\" (or \"Gaussian\") covariance
function: C ( d ) = σ 2 exp ⁡ ( − ( d / V ) 2 ) {\\displaystyle
C(d)=\\sigma \^{2}\\exp(-(d/V)\^{2})} is a stationary covariance
function with smooth sample paths. The Matérn covariance function and
rational quadratic covariance function are two parametric families of
stationary covariance functions. The Matérn family includes the
exponential and squared exponential covariance functions as special
cases. See also Autocorrelation function Correlation function Covariance
matrix Covariance operator -- Operator in probability theory Kriging
Positive-definite kernel Random field Stochastic process Variogram ==
References ==
