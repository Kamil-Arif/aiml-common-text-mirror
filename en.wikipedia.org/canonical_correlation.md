In statistics, canonical-correlation analysis (CCA), also called
canonical variates analysis, is a way of inferring information from
cross-covariance matrices. If we have two vectors X = (X1, \..., Xn) and
Y = (Y1, \..., Ym) of random variables, and there are correlations among
the variables, then canonical-correlation analysis will find linear
combinations of X and Y which have maximum correlation with each other.
T. R. Knapp notes that \"virtually all of the commonly encountered
parametric tests of significance can be treated as special cases of
canonical-correlation analysis, which is the general procedure for
investigating the relationships between two sets of variables.\" The
method was first introduced by Harold Hotelling in 1936, although in the
context of angles between flats the mathematical concept was published
by Jordan in 1875. Definition Given two column vectors X = ( x 1 , ... ,
x n ) T {\\displaystyle X=(x\_{1},\\dots ,x\_{n})\^{T}} and Y = ( y 1 ,
... , y m ) T {\\displaystyle Y=(y\_{1},\\dots ,y\_{m})\^{T}} of random
variables with finite second moments, one may define the
cross-covariance Σ X Y = cov ⁡ ( X , Y ) {\\displaystyle \\Sigma
\_{XY}=\\operatorname {cov} (X,Y)} to be the n × m {\\displaystyle
n\\times m} matrix whose ( i , j ) {\\displaystyle (i,j)} entry is the
covariance cov ⁡ ( x i , y j ) {\\displaystyle \\operatorname {cov}
(x\_{i},y\_{j})} . In practice, we would estimate the covariance matrix
based on sampled data from X {\\displaystyle X} and Y {\\displaystyle Y}
(i.e. from a pair of data matrices). Canonical-correlation analysis
seeks vectors a {\\displaystyle a} ( a ∈ R n {\\displaystyle a\\in
\\mathbb {R} \^{n}} ) and b {\\displaystyle b} ( b ∈ R m {\\displaystyle
b\\in \\mathbb {R} \^{m}} ) such that the random variables a T X
{\\displaystyle a\^{T}X} and b T Y {\\displaystyle b\^{T}Y} maximize the
correlation ρ = corr ⁡ ( a T X , b T Y ) {\\displaystyle \\rho
=\\operatorname {corr} (a\^{T}X,b\^{T}Y)} . The (scalar) random
variables U = a T X {\\displaystyle U=a\^{T}X} and V = b T Y
{\\displaystyle V=b\^{T}Y} are the first pair of canonical variables.
Then one seeks vectors maximizing the same correlation subject to the
constraint that they are to be uncorrelated with the first pair of
canonical variables; this gives the second pair of canonical variables.
This procedure may be continued up to min { m , n } {\\displaystyle
\\min\\{m,n\\}} times. Computation Derivation Let Σ X Y {\\displaystyle
\\Sigma \_{XY}} be the cross-covariance matrix for any pair of
(vector-shaped) random variables X {\\displaystyle X} and Y
{\\displaystyle Y} . The target function to maximize is ρ = a T Σ X Y b
a T Σ X X a b T Σ Y Y b . {\\displaystyle \\rho ={\\frac {a\^{T}\\Sigma
\_{XY}b}{{\\sqrt {a\^{T}\\Sigma \_{XX}a}}{\\sqrt {b\^{T}\\Sigma
\_{YY}b}}}}.} The first step is to define a change of basis and define c
= Σ X X 1 / 2 a , {\\displaystyle c=\\Sigma \_{XX}\^{1/2}a,} d = Σ Y Y 1
/ 2 b . {\\displaystyle d=\\Sigma \_{YY}\^{1/2}b.} And thus we have ρ =
c T Σ X X − 1 / 2 Σ X Y Σ Y Y − 1 / 2 d c T c d T d . {\\displaystyle
\\rho ={\\frac {c\^{T}\\Sigma \_{XX}\^{-1/2}\\Sigma \_{XY}\\Sigma
\_{YY}\^{-1/2}d}{{\\sqrt {c\^{T}c}}{\\sqrt {d\^{T}d}}}}.} By the
Cauchy--Schwarz inequality, we have ( c T Σ X X − 1 / 2 Σ X Y Σ Y Y − 1
/ 2 ) ( d ) ≤ ( c T Σ X X − 1 / 2 Σ X Y Σ Y Y − 1 / 2 Σ Y Y − 1 / 2 Σ Y
X Σ X X − 1 / 2 c ) 1 / 2 ( d T d ) 1 / 2 , {\\displaystyle
\\left(c\^{T}\\Sigma \_{XX}\^{-1/2}\\Sigma \_{XY}\\Sigma
\_{YY}\^{-1/2}\\right)(d)\\leq \\left(c\^{T}\\Sigma
\_{XX}\^{-1/2}\\Sigma \_{XY}\\Sigma \_{YY}\^{-1/2}\\Sigma
\_{YY}\^{-1/2}\\Sigma \_{YX}\\Sigma
\_{XX}\^{-1/2}c\\right)\^{1/2}\\left(d\^{T}d\\right)\^{1/2},} ρ ≤ ( c T
Σ X X − 1 / 2 Σ X Y Σ Y Y − 1 Σ Y X Σ X X − 1 / 2 c ) 1 / 2 ( c T c ) 1
/ 2 . {\\displaystyle \\rho \\leq {\\frac {\\left(c\^{T}\\Sigma
\_{XX}\^{-1/2}\\Sigma \_{XY}\\Sigma \_{YY}\^{-1}\\Sigma \_{YX}\\Sigma
\_{XX}\^{-1/2}c\\right)\^{1/2}}{\\left(c\^{T}c\\right)\^{1/2}}}.} There
is equality if the vectors d {\\displaystyle d} and Σ Y Y − 1 / 2 Σ Y X
Σ X X − 1 / 2 c {\\displaystyle \\Sigma \_{YY}\^{-1/2}\\Sigma
\_{YX}\\Sigma \_{XX}\^{-1/2}c} are collinear. In addition, the maximum
of correlation is attained if c {\\displaystyle c} is the eigenvector
with the maximum eigenvalue for the matrix Σ X X − 1 / 2 Σ X Y Σ Y Y − 1
Σ Y X Σ X X − 1 / 2 {\\displaystyle \\Sigma \_{XX}\^{-1/2}\\Sigma
\_{XY}\\Sigma \_{YY}\^{-1}\\Sigma \_{YX}\\Sigma \_{XX}\^{-1/2}} (see
Rayleigh quotient). The subsequent pairs are found by using eigenvalues
of decreasing magnitudes. Orthogonality is guaranteed by the symmetry of
the correlation matrices. Another way of viewing this computation is
that c {\\displaystyle c} and d {\\displaystyle d} are the left and
right singular vectors of the correlation matrix of X and Y
corresponding to the highest singular value. Solution The solution is
therefore: c {\\displaystyle c} is an eigenvector of Σ X X − 1 / 2 Σ X Y
Σ Y Y − 1 Σ Y X Σ X X − 1 / 2 {\\displaystyle \\Sigma
\_{XX}\^{-1/2}\\Sigma \_{XY}\\Sigma \_{YY}\^{-1}\\Sigma \_{YX}\\Sigma
\_{XX}\^{-1/2}} d {\\displaystyle d} is proportional to Σ Y Y − 1 / 2 Σ
Y X Σ X X − 1 / 2 c {\\displaystyle \\Sigma \_{YY}\^{-1/2}\\Sigma
\_{YX}\\Sigma \_{XX}\^{-1/2}c} Reciprocally, there is also: d
{\\displaystyle d} is an eigenvector of Σ Y Y − 1 / 2 Σ Y X Σ X X − 1 Σ
X Y Σ Y Y − 1 / 2 {\\displaystyle \\Sigma \_{YY}\^{-1/2}\\Sigma
\_{YX}\\Sigma \_{XX}\^{-1}\\Sigma \_{XY}\\Sigma \_{YY}\^{-1/2}} c
{\\displaystyle c} is proportional to Σ X X − 1 / 2 Σ X Y Σ Y Y − 1 / 2
d {\\displaystyle \\Sigma \_{XX}\^{-1/2}\\Sigma \_{XY}\\Sigma
\_{YY}\^{-1/2}d} Reversing the change of coordinates, we have that a
{\\displaystyle a} is an eigenvector of Σ X X − 1 Σ X Y Σ Y Y − 1 Σ Y X
{\\displaystyle \\Sigma \_{XX}\^{-1}\\Sigma \_{XY}\\Sigma
\_{YY}\^{-1}\\Sigma \_{YX}} , b {\\displaystyle b} is proportional to Σ
Y Y − 1 Σ Y X a ; {\\displaystyle \\Sigma \_{YY}\^{-1}\\Sigma \_{YX}a;}
b {\\displaystyle b} is an eigenvector of Σ Y Y − 1 Σ Y X Σ X X − 1 Σ X
Y , {\\displaystyle \\Sigma \_{YY}\^{-1}\\Sigma \_{YX}\\Sigma
\_{XX}\^{-1}\\Sigma \_{XY},} a {\\displaystyle a} is proportional to Σ X
X − 1 Σ X Y b {\\displaystyle \\Sigma \_{XX}\^{-1}\\Sigma \_{XY}b} .The
canonical variables are defined by: U = c T Σ X X − 1 / 2 X = a T X
{\\displaystyle U=c\^{T}\\Sigma \_{XX}\^{-1/2}X=a\^{T}X} V = d T Σ Y Y −
1 / 2 Y = b T Y {\\displaystyle V=d\^{T}\\Sigma \_{YY}\^{-1/2}Y=b\^{T}Y}
Implementation CCA can be computed using singular value decomposition on
a correlation matrix. It is available as a function in MATLAB as
canoncorr (also in Octave) R as the standard function cancor and several
other packages, including CCA and vegan. CCP for statistical hypothesis
testing in canonical correlation analysis. SAS as proc cancorr Python in
the library scikit-learn, as Cross decomposition and in statsmodels, as
CanCorr. SPSS as macro CanCorr shipped with the main software Julia
(programming language) in the MultivariateStats.jl package.CCA
computation using singular value decomposition on a correlation matrix
is related to the cosine of the angles between flats. The cosine
function is ill-conditioned for small angles, leading to very inaccurate
computation of highly correlated principal vectors in finite precision
computer arithmetic. To fix this trouble, alternative algorithms are
available in SciPy as linear-algebra function subspace_angles MATLAB as
FileExchange function subspacea Hypothesis testing Each row can be
tested for significance with the following method. Since the
correlations are sorted, saying that row i {\\displaystyle i} is zero
implies all further correlations are also zero. If we have p
{\\displaystyle p} independent observations in a sample and ρ \^ i
{\\displaystyle {\\widehat {\\rho }}\_{i}} is the estimated correlation
for i = 1 , ... , min { m , n } {\\displaystyle i=1,\\dots
,\\min\\{m,n\\}} . For the i {\\displaystyle i} th row, the test
statistic is: χ 2 = − ( p − 1 − 1 2 ( m + n + 1 ) ) ln ⁡ ∏ j = i min { m
, n } ( 1 − ρ \^ j 2 ) , {\\displaystyle \\chi \^{2}=-\\left(p-1-{\\frac
{1}{2}}(m+n+1)\\right)\\ln \\prod \_{j=i}\^{\\min\\{m,n\\}}(1-{\\widehat
{\\rho }}\_{j}\^{2}),} which is asymptotically distributed as a
chi-squared with ( m − i + 1 ) ( n − i + 1 ) {\\displaystyle
(m-i+1)(n-i+1)} degrees of freedom for large p {\\displaystyle p} .
Since all the correlations from min { m , n } {\\displaystyle
\\min\\{m,n\\}} to p {\\displaystyle p} are logically zero (and
estimated that way also) the product for the terms after this point is
irrelevant. Note that in the small sample size limit with p \< n + m
{\\displaystyle p
