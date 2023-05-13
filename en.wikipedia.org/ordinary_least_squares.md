In statistics, ordinary least squares (OLS) is a type of linear least
squares method for choosing the unknown parameters in a linear
regression model (with fixed level-one effects of a linear function of a
set of explanatory variables) by the principle of least squares:
minimizing the sum of the squares of the differences between the
observed dependent variable (values of the variable being observed) in
the input dataset and the output of the (linear) function of the
independent variable. Geometrically, this is seen as the sum of the
squared distances, parallel to the axis of the dependent variable,
between each data point in the set and the corresponding point on the
regression surface---the smaller the differences, the better the model
fits the data. The resulting estimator can be expressed by a simple
formula, especially in the case of a simple linear regression, in which
there is a single regressor on the right side of the regression
equation. The OLS estimator is consistent for the level-one fixed
effects when the regressors are exogenous and forms perfect colinearity
(rank condition), consistent for the variance estimate of the residuals
when regressors have finite fourth moments and---by the Gauss--Markov
theorem---optimal in the class of linear unbiased estimators when the
errors are homoscedastic and serially uncorrelated. Under these
conditions, the method of OLS provides minimum-variance mean-unbiased
estimation when the errors have finite variances. Under the additional
assumption that the errors are normally distributed with zero mean, OLS
is the maximum likelihood estimator that outperforms any non-linear
unbiased estimator. Linear model Suppose the data consists of n
{\\displaystyle n} observations { x i , y i } i = 1 n {\\displaystyle
\\left\\{\\mathbf {x} \_{i},y\_{i}\\right\\}\_{i=1}\^{n}} . Each
observation i {\\displaystyle i} includes a scalar response y i
{\\displaystyle y\_{i}} and a column vector x i {\\displaystyle \\mathbf
{x} \_{i}} of p {\\displaystyle p} parameters (regressors), i.e., x i =
\[ x i 1 , x i 2 , ... , x i p \] T {\\displaystyle \\mathbf {x}
\_{i}=\\left\[x\_{i1},x\_{i2},\\dots ,x\_{ip}\\right\]\^{\\mathsf {T}}}
. In a linear regression model, the response variable, y i
{\\displaystyle y\_{i}} , is a linear function of the regressors: y i =
β 1 x i 1 + β 2 x i 2 + ⋯ + β p x i p + ε i , {\\displaystyle
y\_{i}=\\beta \_{1}\\ x\_{i1}+\\beta \_{2}\\ x\_{i2}+\\cdots +\\beta
\_{p}\\ x\_{ip}+\\varepsilon \_{i},} or in vector form, y i = x i T β +
ε i , {\\displaystyle y\_{i}=\\mathbf {x} \_{i}\^{\\mathsf
{T}}{\\boldsymbol {\\beta }}+\\varepsilon \_{i},\\,} where x i
{\\displaystyle \\mathbf {x} \_{i}} , as introduced previously, is a
column vector of the i {\\displaystyle i} -th observation of all the
explanatory variables; β {\\displaystyle {\\boldsymbol {\\beta }}} is a
p × 1 {\\displaystyle p\\times 1} vector of unknown parameters; and the
scalar ε i {\\displaystyle \\varepsilon \_{i}} represents unobserved
random variables (errors) of the i {\\displaystyle i} -th observation. ε
i {\\displaystyle \\varepsilon \_{i}} accounts for the influences upon
the responses y i {\\displaystyle y\_{i}} from sources other than the
explanatory variables x i {\\displaystyle \\mathbf {x} \_{i}} . This
model can also be written in matrix notation as y = X β + ε ,
{\\displaystyle \\mathbf {y} =\\mathbf {X} {\\boldsymbol {\\beta
}}+{\\boldsymbol {\\varepsilon }},\\,} where y {\\displaystyle \\mathbf
{y} } and ε {\\displaystyle {\\boldsymbol {\\varepsilon }}} are n × 1
{\\displaystyle n\\times 1} vectors of the response variables and the
errors of the n {\\displaystyle n} observations, and X {\\displaystyle
\\mathbf {X} } is an n × p {\\displaystyle n\\times p} matrix of
regressors, also sometimes called the design matrix, whose row i
{\\displaystyle i} is x i T {\\displaystyle \\mathbf {x}
\_{i}\^{\\mathsf {T}}} and contains the i {\\displaystyle i} -th
observations on all the explanatory variables. Typically, a constant
term is included in the set of regressors X {\\displaystyle \\mathbf {X}
} , say, by taking x i 1 = 1 {\\displaystyle x\_{i1}=1} for all i = 1 ,
... , n {\\displaystyle i=1,\\dots ,n} . The coefficient β 1
{\\displaystyle \\beta \_{1}} corresponding to this regressor is called
the intercept. Without the intercept, the fitted line is forced to cross
the origin when x i = 0 → {\\displaystyle x\_{i}={\\vec {0}}} .
Regressors do not have to be independent: there can be any desired
relationship between the regressors (so long as it is not a linear
relationship). For instance, we might suspect the response depends
linearly both on a value and its square; in which case we would include
one regressor whose value is just the square of another regressor. In
that case, the model would be quadratic in the second regressor, but
none-the-less is still considered a linear model because the model is
still linear in the parameters ( β {\\displaystyle {\\boldsymbol {\\beta
}}} ). Matrix/vector formulation Consider an overdetermined system ∑ j =
1 p x i j β j = y i , ( i = 1 , 2 , ... , n ) , {\\displaystyle \\sum
\_{j=1}\^{p}x\_{ij}\\beta \_{j}=y\_{i},\\ (i=1,2,\\dots ,n),} of n
{\\displaystyle n} linear equations in p {\\displaystyle p} unknown
coefficients, β 1 , β 2 , ... , β p {\\displaystyle \\beta \_{1},\\beta
\_{2},\\dots ,\\beta \_{p}} , with n \> p {\\displaystyle n\>p} . This
can be written in matrix form as X β = y , {\\displaystyle \\mathbf {X}
{\\boldsymbol {\\beta }}=\\mathbf {y} ,} where X = \[ X 11 X 12 ⋯ X 1 p
X 21 X 22 ⋯ X 2 p ⋮ ⋮ ⋱ ⋮ X n 1 X n 2 ⋯ X n p \] , β = \[ β 1 β 2 ⋮ β p
\] , y = \[ y 1 y 2 ⋮ y n \] . {\\displaystyle \\mathbf {X}
={\\begin{bmatrix}X\_{11}&X\_{12}&\\cdots
&X\_{1p}\\\\X\_{21}&X\_{22}&\\cdots &X\_{2p}\\\\\\vdots &\\vdots
&\\ddots &\\vdots \\\\X\_{n1}&X\_{n2}&\\cdots
&X\_{np}\\end{bmatrix}},\\qquad {\\boldsymbol {\\beta
}}={\\begin{bmatrix}\\beta \_{1}\\\\\\beta \_{2}\\\\\\vdots \\\\\\beta
\_{p}\\end{bmatrix}},\\qquad \\mathbf {y}
={\\begin{bmatrix}y\_{1}\\\\y\_{2}\\\\\\vdots
\\\\y\_{n}\\end{bmatrix}}.} (Note: for a linear model as above, not all
elements in X {\\displaystyle \\mathbf {X} } contains information on the
data points. The first column is populated with ones, X i 1 = 1
{\\displaystyle X\_{i1}=1} . Only the other columns contain actual data.
So here p {\\displaystyle p} is equal to the number of regressors plus
one). Such a system usually has no exact solution, so the goal is
instead to find the coefficients β {\\displaystyle {\\boldsymbol {\\beta
}}} which fit the equations \"best\", in the sense of solving the
quadratic minimization problem β \^ = a r g m i n β S ( β ) ,
{\\displaystyle {\\hat {\\boldsymbol {\\beta }}}={\\underset
{\\boldsymbol {\\beta }}{\\operatorname {arg\\,min} }}\\,S({\\boldsymbol
{\\beta }}),} where the objective function S {\\displaystyle S} is given
by S ( β ) = ∑ i = 1 n \| y i − ∑ j = 1 p X i j β j \| 2 = ‖ y − X β ‖ 2
. {\\displaystyle S({\\boldsymbol {\\beta }})=\\sum
\_{i=1}\^{n}\\left\|y\_{i}-\\sum \_{j=1}\^{p}X\_{ij}\\beta
\_{j}\\right\|\^{2}=\\left\\\|\\mathbf {y} -\\mathbf {X} {\\boldsymbol
{\\beta }}\\right\\\|\^{2}.} A justification for choosing this criterion
is given in Properties below. This minimization problem has a unique
solution, provided that the p {\\displaystyle p} columns of the matrix X
{\\displaystyle \\mathbf {X} } are linearly independent, given by
solving the so-called normal equations: ( X T X ) β \^ = X T y .
{\\displaystyle \\left(\\mathbf {X} \^{\\mathsf {T}}\\mathbf {X}
\\right){\\hat {\\boldsymbol {\\beta }}}=\\mathbf {X} \^{\\mathsf
{T}}\\mathbf {y} \\ .} The matrix X T X {\\displaystyle \\mathbf {X}
\^{\\mathsf {T}}\\mathbf {X} } is known as the normal matrix or Gram
matrix and the matrix X T y {\\displaystyle \\mathbf {X} \^{\\mathsf
{T}}\\mathbf {y} } is known as the moment matrix of regressand by
regressors. Finally, β \^ {\\displaystyle {\\hat {\\boldsymbol {\\beta
}}}} is the coefficient vector of the least-squares hyperplane,
expressed as β \^ = ( X T X ) − 1 X T y . {\\displaystyle {\\hat
{\\boldsymbol {\\beta }}}=\\left(\\mathbf {X} \^{\\mathsf {T}}\\mathbf
{X} \\right)\^{-1}\\mathbf {X} \^{\\mathsf {T}}\\mathbf {y} .} or β \^ =
β + ( X T X ) − 1 X T ε . {\\displaystyle {\\hat {\\boldsymbol {\\beta
}}}={\\boldsymbol {\\beta }}+\\left(\\mathbf {X} \^{\\mathsf
{T}}\\mathbf {X} \\right)\^{-1}\\mathbf {X} \^{\\mathsf
{T}}{\\boldsymbol {\\varepsilon }}.} Estimation Suppose b is a
\"candidate\" value for the parameter vector β. The quantity yi − xiTb,
called the residual for the i-th observation, measures the vertical
distance between the data point (xi, yi) and the hyperplane y = xTb, and
thus assesses the degree of fit between the actual data and the model.
The sum of squared residuals (SSR) (also called the error sum of squares
(ESS) or residual sum of squares (RSS)) is a measure of the overall
model fit: S ( b ) = ∑ i = 1 n ( y i − x i T b ) 2 = ( y − X b ) T ( y −
X b ) , {\\displaystyle S(b)=\\sum \_{i=1}\^{n}(y\_{i}-x\_{i}\^{\\mathrm
{T} }b)\^{2}=(y-Xb)\^{\\mathrm {T} }(y-Xb),} where T denotes the matrix
transpose, and the rows of X, denoting the values of all the independent
variables associated with a particular value of the dependent variable,
are Xi = xiT. The value of b which minimizes this sum is called the OLS
estimator for β. The function S(b) is quadratic in b with
positive-definite Hessian, and therefore this function possesses a
unique global minimum at b = β \^ {\\displaystyle b={\\hat {\\beta }}} ,
which can be given by the explicit formula:\[proof\] β \^ = argmin b ∈ R
p ⁡ S ( b ) = ( X T X ) − 1 X T y . {\\displaystyle {\\hat {\\beta
}}=\\operatorname {argmin} \_{b\\in \\mathbb {R}
\^{p}}S(b)=(X\^{\\mathrm {T} }X)\^{-1}X\^{\\mathrm {T} }y\\ .} The
product N=XT X is a Gram matrix and its inverse, Q=N--1, is the cofactor
matrix of β, closely related to its covariance matrix, Cβ. The matrix
(XT X)--1 XT=Q XT is called the Moore--Penrose pseudoinverse matrix of
X. This formulation highlights the point that estimation can be carried
out if, and only if, there is no perfect multicollinearity between the
explanatory variables (which would cause the gram matrix to have no
inverse). After we have estimated β, the fitted values (or predicted
values) from the regression will be y \^ = X β \^ = P y ,
{\\displaystyle {\\hat {y}}=X{\\hat {\\beta }}=Py,} where P = X(XTX)−1XT
is the projection matrix onto the space V spanned by the columns of X.
This matrix P is also sometimes called the hat matrix because it \"puts
a hat\" onto the variable y. Another matrix, closely related to P is the
annihilator matrix M = In − P; this is a projection matrix onto the
space orthogonal to V. Both matrices P and M are symmetric and
idempotent (meaning that P2 = P and M2 = M), and relate to the data
matrix X via identities PX = X and MX = 0. Matrix M creates the
residuals from the regression: ε \^ = y − y \^ = y − X β \^ = M y = M (
X β + ε ) = ( M X ) β + M ε = M ε . {\\displaystyle {\\hat {\\varepsilon
}}=y-{\\hat {y}}=y-X{\\hat {\\beta }}=My=M(X\\beta +\\varepsilon
)=(MX)\\beta +M\\varepsilon =M\\varepsilon .} Using these residuals we
can estimate the value of σ 2 using the reduced chi-squared statistic: s
2 = ε \^ T ε \^ n − p = ( M y ) T M y n − p = y T M T M y n − p = y T M
y n − p = S ( β \^ ) n − p , σ \^ 2 = n − p n s 2 {\\displaystyle
s\^{2}={\\frac {{\\hat {\\varepsilon }}\^{\\mathrm {T} }{\\hat
{\\varepsilon }}}{n-p}}={\\frac {(My)\^{\\mathrm {T} }My}{n-p}}={\\frac
{y\^{\\mathrm {T} }M\^{\\mathrm {T} }My}{n-p}}={\\frac {y\^{\\mathrm {T}
}My}{n-p}}={\\frac {S({\\hat {\\beta }})}{n-p}},\\qquad {\\hat {\\sigma
}}\^{2}={\\frac {n-p}{n}}\\;s\^{2}} The denominator, n−p, is the
statistical degrees of freedom. The first quantity, s2, is the OLS
estimate for σ2, whereas the second, σ \^ 2 {\\displaystyle
\\scriptstyle {\\hat {\\sigma }}\^{2}} , is the MLE estimate for σ2. The
two estimators are quite similar in large samples; the first estimator
is always unbiased, while the second estimator is biased but has a
smaller mean squared error. In practice s2 is used more often, since it
is more convenient for the hypothesis testing. The square root of s2 is
called the regression standard error, standard error of the regression,
or standard error of the equation.It is common to assess the
goodness-of-fit of the OLS regression by comparing how much the initial
variation in the sample can be reduced by regressing onto X. The
coefficient of determination R2 is defined as a ratio of \"explained\"
variance to the \"total\" variance of the dependent variable y, in the
cases where the regression sum of squares equals the sum of squares of
residuals: R 2 = ∑ ( y \^ i − y ¯ ) 2 ∑ ( y i − y ¯ ) 2 = y T P T L P y
y T L y = 1 − y T M y y T L y = 1 − R S S T S S {\\displaystyle
R\^{2}={\\frac {\\sum ({\\hat {y}}\_{i}-{\\overline {y}})\^{2}}{\\sum
(y\_{i}-{\\overline {y}})\^{2}}}={\\frac {y\^{\\mathrm {T} }P\^{\\mathrm
{T} }LPy}{y\^{\\mathrm {T} }Ly}}=1-{\\frac {y\^{\\mathrm {T}
}My}{y\^{\\mathrm {T} }Ly}}=1-{\\frac {\\rm {RSS}}{\\rm {TSS}}}} where
TSS is the total sum of squares for the dependent variable, L = I n − 1
n J n {\\textstyle L=I\_{n}-{\\frac {1}{n}}J\_{n}} , and J n
{\\textstyle J\_{n}} is an n×n matrix of ones. ( L {\\displaystyle L} is
a centering matrix which is equivalent to regression on a constant; it
simply subtracts the mean from a variable.) In order for R2 to be
meaningful, the matrix X of data on regressors must contain a column
vector of ones to represent the constant whose coefficient is the
regression intercept. In that case, R2 will always be a number between 0
and 1, with values close to 1 indicating a good degree of fit. The
variance in the prediction of the independent variable as a function of
the dependent variable is given in the article Polynomial least squares.
Simple linear regression model If the data matrix X contains only two
variables, a constant and a scalar regressor xi, then this is called the
\"simple regression model\". This case is often considered in the
beginner statistics classes, as it provides much simpler formulas even
suitable for manual calculation. The parameters are commonly denoted as
(α, β): y i = α + β x i + ε i . {\\displaystyle y\_{i}=\\alpha +\\beta
x\_{i}+\\varepsilon \_{i}.} The least squares estimates in this case are
given by simple formulas β \^ = ∑ i = 1 n ( x i − x ¯ ) ( y i − y ¯ ) ∑
i = 1 n ( x i − x ¯ ) 2 α \^ = y ¯ − β \^ x ¯ , {\\displaystyle
{\\begin{aligned}{\\widehat {\\beta }}&={\\frac {\\sum
\_{i=1}\^{n}{(x\_{i}-{\\bar {x}})(y\_{i}-{\\bar {y}})}}{\\sum
\_{i=1}\^{n}{(x\_{i}-{\\bar {x}})\^{2}}}}\\\\\[2pt\]{\\widehat {\\alpha
}}&={\\bar {y}}-{\\widehat {\\beta }}\\,{\\bar {x}}\\ ,\\end{aligned}}}
Alternative derivations In the previous section the least squares
estimator β \^ {\\displaystyle {\\hat {\\beta }}} was obtained as a
value that minimizes the sum of squared residuals of the model. However
it is also possible to derive the same estimator from other approaches.
In all cases the formula for OLS estimator remains the same: \^β =
(XTX)−1XTy; the only difference is in how we interpret this result.
Projection For mathematicians, OLS is an approximate solution to an
overdetermined system of linear equations Xβ ≈ y, where β is the
unknown. Assuming the system cannot be solved exactly (the number of
equations n is much larger than the number of unknowns p), we are
looking for a solution that could provide the smallest discrepancy
between the right- and left- hand sides. In other words, we are looking
for the solution that satisfies β \^ = a r g min β ‖ y − X β ‖ ,
{\\displaystyle {\\hat {\\beta }}={\\rm {arg}}\\min \_{\\beta
}\\,\\lVert \\mathbf {y} -\\mathbf {X} {\\boldsymbol {\\beta }}\\rVert
,} where ‖·‖ is the standard L2 norm in the n-dimensional Euclidean
space Rn. The predicted quantity Xβ is just a certain linear combination
of the vectors of regressors. Thus, the residual vector y − Xβ will have
the smallest length when y is projected orthogonally onto the linear
subspace spanned by the columns of X. The OLS estimator β \^
{\\displaystyle {\\hat {\\beta }}} in this case can be interpreted as
the coefficients of vector decomposition of \^y = Py along the basis of
X. In other words, the gradient equations at the minimum can be written
as: ( y − X β \^ ) ⊤ X = 0. {\\displaystyle (\\mathbf {y} -\\mathbf {X}
{\\hat {\\boldsymbol {\\beta }}})\^{\\top }\\mathbf {X} =0.} A
geometrical interpretation of these equations is that the vector of
residuals, y − X β \^ {\\displaystyle \\mathbf {y} -X{\\hat
{\\boldsymbol {\\beta }}}} is orthogonal to the column space of X, since
the dot product ( y − X β \^ ) ⋅ X v {\\displaystyle (\\mathbf {y}
-\\mathbf {X} {\\hat {\\boldsymbol {\\beta }}})\\cdot \\mathbf {X}
\\mathbf {v} } is equal to zero for any conformal vector, v. This means
that y − X β \^ {\\displaystyle \\mathbf {y} -\\mathbf {X} {\\boldsymbol
{\\hat {\\beta }}}} is the shortest of all possible vectors y − X β
{\\displaystyle \\mathbf {y} -\\mathbf {X} {\\boldsymbol {\\beta }}} ,
that is, the variance of the residuals is the minimum possible. This is
illustrated at the right. Introducing γ \^ {\\displaystyle {\\hat
{\\boldsymbol {\\gamma }}}} and a matrix K with the assumption that a
matrix \[ X K \] {\\displaystyle \[\\mathbf {X} \\ \\mathbf {K} \]} is
non-singular and KT X = 0 (cf. Orthogonal projections), the residual
vector should satisfy the following equation: r \^ := y − X β \^ = K γ
\^ . {\\displaystyle {\\hat {\\mathbf {r} }}:=\\mathbf {y} -\\mathbf {X}
{\\hat {\\boldsymbol {\\beta }}}=\\mathbf {K} {\\hat {\\boldsymbol
{\\gamma }}}.} The equation and solution of linear least squares are
thus described as follows: y = \[ X K \] \[ β \^ γ \^ \] , ⇒ \[ β \^ γ
\^ \] = \[ X K \] − 1 y = \[ ( X ⊤ X ) − 1 X ⊤ ( K ⊤ K ) − 1 K ⊤ \] y .
{\\displaystyle {\\begin{aligned}\\mathbf {y}
&={\\begin{bmatrix}\\mathbf {X} &\\mathbf {K}
\\end{bmatrix}}{\\begin{bmatrix}{\\hat {\\boldsymbol {\\beta
}}}\\\\{\\hat {\\boldsymbol {\\gamma
}}}\\end{bmatrix}},\\\\{}\\Rightarrow {\\begin{bmatrix}{\\hat
{\\boldsymbol {\\beta }}}\\\\{\\hat {\\boldsymbol {\\gamma
}}}\\end{bmatrix}}&={\\begin{bmatrix}\\mathbf {X} &\\mathbf {K}
\\end{bmatrix}}\^{-1}\\mathbf {y} ={\\begin{bmatrix}\\left(\\mathbf {X}
\^{\\top }\\mathbf {X} \\right)\^{-1}\\mathbf {X} \^{\\top
}\\\\\\left(\\mathbf {K} \^{\\top }\\mathbf {K} \\right)\^{-1}\\mathbf
{K} \^{\\top }\\end{bmatrix}}\\mathbf {y} .\\end{aligned}}} Another way
of looking at it is to consider the regression line to be a weighted
average of the lines passing through the combination of any two points
in the dataset. Although this way of calculation is more computationally
expensive, it provides a better intuition on OLS. Maximum likelihood The
OLS estimator is identical to the maximum likelihood estimator (MLE)
under the normality assumption for the error terms.\[proof\] This
normality assumption has historical importance, as it provided the basis
for the early work in linear regression analysis by Yule and Pearson.
From the properties of MLE, we can infer that the OLS estimator is
asymptotically efficient (in the sense of attaining the Cramér--Rao
bound for variance) if the normality assumption is satisfied.
Generalized method of moments In iid case the OLS estimator can also be
viewed as a GMM estimator arising from the moment conditions E \[ x i (
y i − x i T β ) \] = 0. {\\displaystyle \\mathrm {E} {\\big
\[}\\,x\_{i}\\left(y\_{i}-x\_{i}\^{\\mathsf {T}}\\beta \\right)\\,{\\big
\]}=0.} These moment conditions state that the regressors should be
uncorrelated with the errors. Since xi is a p-vector, the number of
moment conditions is equal to the dimension of the parameter vector β,
and thus the system is exactly identified. This is the so-called
classical GMM case, when the estimator does not depend on the choice of
the weighting matrix. Note that the original strict exogeneity
assumption E\[εi \| xi\] = 0 implies a far richer set of moment
conditions than stated above. In particular, this assumption implies
that for any vector-function ƒ, the moment condition E\[ƒ(xi)·εi\] = 0
will hold. However it can be shown using the Gauss--Markov theorem that
the optimal choice of function ƒ is to take ƒ(x) = x, which results in
the moment equation posted above. Properties Assumptions There are
several different frameworks in which the linear regression model can be
cast in order to make the OLS technique applicable. Each of these
settings produces the same formulas and same results. The only
difference is the interpretation and the assumptions which have to be
imposed in order for the method to give meaningful results. The choice
of the applicable framework depends mostly on the nature of data in
hand, and on the inference task which has to be performed. One of the
lines of difference in interpretation is whether to treat the regressors
as random variables, or as predefined constants. In the first case
(random design) the regressors xi are random and sampled together with
the yi\'s from some population, as in an observational study. This
approach allows for more natural study of the asymptotic properties of
the estimators. In the other interpretation (fixed design), the
regressors X are treated as known constants set by a design, and y is
sampled conditionally on the values of X as in an experiment. For
practical purposes, this distinction is often unimportant, since
estimation and inference is carried out while conditioning on X. All
results stated in this article are within the random design framework.
Classical linear regression model The classical model focuses on the
\"finite sample\" estimation and inference, meaning that the number of
observations n is fixed. This contrasts with the other approaches, which
study the asymptotic behavior of OLS, and in which the number of
observations is allowed to grow to infinity. Correct specification. The
linear functional form must coincide with the form of the actual
data-generating process. Strict exogeneity. The errors in the regression
should have conditional mean zero: The immediate consequence of the
exogeneity assumption is that the errors have mean zero: E\[ε\] = 0 (for
the law of total expectation), and that the regressors are uncorrelated
with the errors: E\[XTε\] = 0. The exogeneity assumption is critical for
the OLS theory. If it holds then the regressor variables are called
exogenous. If it doesn\'t, then those regressors that are correlated
with the error term are called endogenous, and the OLS estimator becomes
biased. In such case the method of instrumental variables may be used to
carry out inference. No linear dependence. The regressors in X must all
be linearly independent. Mathematically, this means that the matrix X
must have full column rank almost surely: Usually, it is also assumed
that the regressors have finite moments up to at least the second
moment. Then the matrix Qxx = E\[XTX / n\] is finite and positive
semi-definite. When this assumption is violated the regressors are
called linearly dependent or perfectly multicollinear. In such case the
value of the regression coefficient β cannot be learned, although
prediction of y values is still possible for new values of the
regressors that lie in the same linearly dependent subspace. Spherical
errors: where In is the identity matrix in dimension n, and σ2 is a
parameter which determines the variance of each observation. This σ2 is
considered a nuisance parameter in the model, although usually it is
also estimated. If this assumption is violated then the OLS estimates
are still valid, but no longer efficient. It is customary to split this
assumption into two parts: Homoscedasticity: E\[ εi2 \| X \] = σ2, which
means that the error term has the same variance σ2 in each observation.
When this requirement is violated this is called heteroscedasticity, in
such case a more efficient estimator would be weighted least squares. If
the errors have infinite variance then the OLS estimates will also have
infinite variance (although by the law of large numbers they will
nonetheless tend toward the true values so long as the errors have zero
mean). In this case, robust estimation techniques are recommended. No
autocorrelation: the errors are uncorrelated between observations:
E\[ εiεj \| X \] = 0 for i ≠ j. This assumption may be violated in the
context of time series data, panel data, cluster samples, hierarchical
data, repeated measures data, longitudinal data, and other data with
dependencies. In such cases generalized least squares provides a better
alternative than the OLS. Another expression for autocorrelation is
serial correlation. Normality. It is sometimes additionally assumed that
the errors have normal distribution conditional on the regressors:This
assumption is not needed for the validity of the OLS method, although
certain additional finite-sample properties can be established in case
when it does (especially in the area of hypotheses testing). Also when
the errors are normal, the OLS estimator is equivalent to the maximum
likelihood estimator (MLE), and therefore it is asymptotically efficient
in the class of all regular estimators. Importantly, the normality
assumption applies only to the error terms; contrary to a popular
misconception, the response (dependent) variable is not required to be
normally distributed. Independent and identically distributed (iid) In
some applications, especially with cross-sectional data, an additional
assumption is imposed --- that all observations are independent and
identically distributed. This means that all observations are taken from
a random sample which makes all the assumptions listed earlier simpler
and easier to interpret. Also this framework allows one to state
asymptotic results (as the sample size n → ∞), which are understood as a
theoretical possibility of fetching new independent observations from
the data generating process. The list of assumptions in this case is:
iid observations: (xi, yi) is independent from, and has the same
distribution as, (xj, yj) for all i ≠ j; no perfect multicollinearity:
Qxx = E\[ xi xiT \] is a positive-definite matrix; exogeneity:
E\[ εi \| xi \] = 0; homoscedasticity: Var\[ εi \| xi \] = σ2. Time
series model The stochastic process {xi, yi} is stationary and ergodic;
if {xi, yi} is nonstationary, OLS results are often spurious unless {xi,
yi} is co-integrating. The regressors are predetermined: E\[xiεi\] = 0
for all i = 1, \..., n; The p×p matrix Qxx = E\[ xi xiT \] is of full
rank, and hence positive-definite; {xiεi} is a martingale difference
sequence, with a finite matrix of second moments Qxxε² =
E\[ εi2xi xiT \]. Finite sample properties First of all, under the
strict exogeneity assumption the OLS estimators β \^ {\\displaystyle
\\scriptstyle {\\hat {\\beta }}} and s2 are unbiased, meaning that their
expected values coincide with the true values of the
parameters:\[proof\] E ⁡ \[ β \^ ∣ X \] = β , E ⁡ \[ s 2 ∣ X \] = σ 2 .
{\\displaystyle \\operatorname {E} \[\\,{\\hat {\\beta }}\\mid
X\\,\]=\\beta ,\\quad \\operatorname {E} \[\\,s\^{2}\\mid X\\,\]=\\sigma
\^{2}.} If the strict exogeneity does not hold (as is the case with many
time series models, where exogeneity is assumed only with respect to the
past shocks but not the future ones), then these estimators will be
biased in finite samples. The variance-covariance matrix (or simply
covariance matrix) of β \^ {\\displaystyle \\scriptstyle {\\hat {\\beta
}}} is equal to Var ⁡ \[ β \^ ∣ X \] = σ 2 ( X T X ) − 1 = σ 2 Q .
{\\displaystyle \\operatorname {Var} \[\\,{\\hat {\\beta }}\\mid
X\\,\]=\\sigma \^{2}\\left(X\^{\\mathsf {T}}X\\right)\^{-1}=\\sigma
\^{2}Q.} In particular, the standard error of each coefficient β \^ j
{\\displaystyle \\scriptstyle {\\hat {\\beta }}\_{j}} is equal to square
root of the j-th diagonal element of this matrix. The estimate of this
standard error is obtained by replacing the unknown quantity σ2 with its
estimate s2. Thus, s . e . \^ ( β \^ j ) = s 2 ( X T X ) j j − 1
{\\displaystyle {\\widehat {\\operatorname {s.\\!e.} }}({\\hat {\\beta
}}\_{j})={\\sqrt {s\^{2}\\left(X\^{\\mathsf {T}}X\\right)\_{jj}\^{-1}}}}
It can also be easily shown that the estimator β \^ {\\displaystyle
\\scriptstyle {\\hat {\\beta }}} is uncorrelated with the residuals from
the model: Cov ⁡ \[ β \^ , ε \^ ∣ X \] = 0. {\\displaystyle
\\operatorname {Cov} \[\\,{\\hat {\\beta }},{\\hat {\\varepsilon }}\\mid
X\\,\]=0.} The Gauss--Markov theorem states that under the spherical
errors assumption (that is, the errors should be uncorrelated and
homoscedastic) the estimator β \^ {\\displaystyle \\scriptstyle {\\hat
{\\beta }}} is efficient in the class of linear unbiased estimators.
This is called the best linear unbiased estimator (BLUE). Efficiency
should be understood as if we were to find some other estimator β \~
{\\displaystyle \\scriptstyle {\\tilde {\\beta }}} which would be linear
in y and unbiased, then Var ⁡ \[ β \~ ∣ X \] − Var ⁡ \[ β \^ ∣ X \] ≥ 0
{\\displaystyle \\operatorname {Var} \[\\,{\\tilde {\\beta }}\\mid
X\\,\]-\\operatorname {Var} \[\\,{\\hat {\\beta }}\\mid X\\,\]\\geq 0}
in the sense that this is a nonnegative-definite matrix. This theorem
establishes optimality only in the class of linear unbiased estimators,
which is quite restrictive. Depending on the distribution of the error
terms ε, other, non-linear estimators may provide better results than
OLS. Assuming normality The properties listed so far are all valid
regardless of the underlying distribution of the error terms. However,
if you are willing to assume that the normality assumption holds (that
is, that ε \~ N(0, σ2In)), then additional properties of the OLS
estimators can be stated. The estimator β \^ {\\displaystyle
\\scriptstyle {\\hat {\\beta }}} is normally distributed, with mean and
variance as given before: β \^ ∼ N ( β , σ 2 ( X T X ) − 1 ) .
{\\displaystyle {\\hat {\\beta }}\\ \\sim \\ {\\mathcal {N}}{\\big
(}\\beta ,\\ \\sigma \^{2}(X\^{\\mathrm {T} }X)\^{-1}{\\big )}.} This
estimator reaches the Cramér--Rao bound for the model, and thus is
optimal in the class of all unbiased estimators. Note that unlike the
Gauss--Markov theorem, this result establishes optimality among both
linear and non-linear estimators, but only in the case of normally
distributed error terms. The estimator s2 will be proportional to the
chi-squared distribution: s 2 ∼ σ 2 n − p ⋅ χ n − p 2 {\\displaystyle
s\^{2}\\ \\sim \\ {\\frac {\\sigma \^{2}}{n-p}}\\cdot \\chi
\_{n-p}\^{2}} The variance of this estimator is equal to 2σ4/(n − p),
which does not attain the Cramér--Rao bound of 2σ4/n. However it was
shown that there are no unbiased estimators of σ2 with variance smaller
than that of the estimator s2. If we are willing to allow biased
estimators, and consider the class of estimators that are proportional
to the sum of squared residuals (SSR) of the model, then the best (in
the sense of the mean squared error) estimator in this class will be
\~σ2 = SSR / (n − p + 2), which even beats the Cramér--Rao bound in case
when there is only one regressor (p = 1).Moreover, the estimators β \^
{\\displaystyle \\scriptstyle {\\hat {\\beta }}} and s2 are independent,
the fact which comes in useful when constructing the t- and F-tests for
the regression. Influential observations As was mentioned before, the
estimator β \^ {\\displaystyle {\\hat {\\beta }}} is linear in y,
meaning that it represents a linear combination of the dependent
variables yi. The weights in this linear combination are functions of
the regressors X, and generally are unequal. The observations with high
weights are called influential because they have a more pronounced
effect on the value of the estimator. To analyze which observations are
influential we remove a specific j-th observation and consider how much
the estimated quantities are going to change (similarly to the jackknife
method). It can be shown that the change in the OLS estimator for β will
be equal to β \^ ( j ) − β \^ = − 1 1 − h j ( X T X ) − 1 x j T ε \^ j ,
{\\displaystyle {\\hat {\\beta }}\^{(j)}-{\\hat {\\beta }}=-{\\frac
{1}{1-h\_{j}}}(X\^{\\mathrm {T} }X)\^{-1}x\_{j}\^{\\mathrm {T} }{\\hat
{\\varepsilon }}\_{j}\\,,} where hj = xjT (XTX)−1xj is the j-th diagonal
element of the hat matrix P, and xj is the vector of regressors
corresponding to the j-th observation. Similarly, the change in the
predicted value for j-th observation resulting from omitting that
observation from the dataset will be equal to y \^ j ( j ) − y \^ j = x
j T β \^ ( j ) − x j T β \^ = − h j 1 − h j ε \^ j {\\displaystyle
{\\hat {y}}\_{j}\^{(j)}-{\\hat {y}}\_{j}=x\_{j}\^{\\mathrm {T} }{\\hat
{\\beta }}\^{(j)}-x\_{j}\^{T}{\\hat {\\beta }}=-{\\frac
{h\_{j}}{1-h\_{j}}}\\,{\\hat {\\varepsilon }}\_{j}} From the properties
of the hat matrix, 0 ≤ hj ≤ 1, and they sum up to p, so that on average
hj ≈ p/n. These quantities hj are called the leverages, and observations
with high hj are called leverage points. Usually the observations with
high leverage ought to be scrutinized more carefully, in case they are
erroneous, or outliers, or in some other way atypical of the rest of the
dataset. Partitioned regression Sometimes the variables and
corresponding parameters in the regression can be logically split into
two groups, so that the regression takes form y = X 1 β 1 + X 2 β 2 + ε
, {\\displaystyle y=X\_{1}\\beta \_{1}+X\_{2}\\beta \_{2}+\\varepsilon
,} where X1 and X2 have dimensions n×p1, n×p2, and β1, β2 are p1×1 and
p2×1 vectors, with p1 + p2 = p. The Frisch--Waugh--Lovell theorem states
that in this regression the residuals ε \^ {\\displaystyle {\\hat
{\\varepsilon }}} and the OLS estimate β \^ 2 {\\displaystyle
\\scriptstyle {\\hat {\\beta }}\_{2}} will be numerically identical to
the residuals and the OLS estimate for β2 in the following regression: M
1 y = M 1 X 2 β 2 + η , {\\displaystyle M\_{1}y=M\_{1}X\_{2}\\beta
\_{2}+\\eta \\,,} where M1 is the annihilator matrix for regressors X1.
The theorem can be used to establish a number of theoretical results.
For example, having a regression with a constant and another regressor
is equivalent to subtracting the means from the dependent variable and
the regressor and then running the regression for the de-meaned
variables but without the constant term. Constrained estimation Suppose
it is known that the coefficients in the regression satisfy a system of
linear equations A : Q T β = c , {\\displaystyle A\\colon \\quad
Q\^{T}\\beta =c,\\,} where Q is a p×q matrix of full rank, and c is a
q×1 vector of known constants, where q \< p. In this case least squares
estimation is equivalent to minimizing the sum of squared residuals of
the model subject to the constraint A. The constrained least squares
(CLS) estimator can be given by an explicit formula: β \^ c = β \^ − ( X
T X ) − 1 Q ( Q T ( X T X ) − 1 Q ) − 1 ( Q T β \^ − c ) .
{\\displaystyle {\\hat {\\beta }}\^{c}={\\hat {\\beta
}}-(X\^{T}X)\^{-1}Q{\\Big (}Q\^{T}(X\^{T}X)\^{-1}Q{\\Big
)}\^{-1}(Q\^{T}{\\hat {\\beta }}-c).} This expression for the
constrained estimator is valid as long as the matrix XTX is invertible.
It was assumed from the beginning of this article that this matrix is of
full rank, and it was noted that when the rank condition fails, β will
not be identifiable. However it may happen that adding the restriction A
makes β identifiable, in which case one would like to find the formula
for the estimator. The estimator is equal to β \^ c = R ( R T X T X R )
− 1 R T X T y + ( I p − R ( R T X T X R ) − 1 R T X T X ) Q ( Q T Q ) −
1 c , {\\displaystyle {\\hat {\\beta
}}\^{c}=R(R\^{T}X\^{T}XR)\^{-1}R\^{T}X\^{T}y+{\\Big
(}I\_{p}-R(R\^{T}X\^{T}XR)\^{-1}R\^{T}X\^{T}X{\\Big
)}Q(Q\^{T}Q)\^{-1}c,} where R is a p×(p − q) matrix such that the matrix
\[Q R\] is non-singular, and RTQ = 0. Such a matrix can always be found,
although generally it is not unique. The second formula coincides with
the first in case when XTX is invertible. Large sample properties The
least squares estimators are point estimates of the linear regression
model parameters β. However, generally we also want to know how close
those estimates might be to the true values of parameters. In other
words, we want to construct the interval estimates. Since we haven\'t
made any assumption about the distribution of error term εi, it is
impossible to infer the distribution of the estimators β \^
{\\displaystyle {\\hat {\\beta }}} and σ \^ 2 {\\displaystyle {\\hat
{\\sigma }}\^{2}} . Nevertheless, we can apply the central limit theorem
to derive their asymptotic properties as sample size n goes to infinity.
While the sample size is necessarily finite, it is customary to assume
that n is \"large enough\" so that the true distribution of the OLS
estimator is close to its asymptotic limit. We can show that under the
model assumptions, the least squares estimator for β is consistent (that
is β \^ {\\displaystyle {\\hat {\\beta }}} converges in probability to
β) and asymptotically normal:\[proof\] ( β \^ − β ) → d N ( 0 , σ 2 Q x
x − 1 ) , {\\displaystyle ({\\hat {\\beta }}-\\beta )\\ {\\xrightarrow
{d}}\\ {\\mathcal {N}}{\\big (}0,\\;\\sigma \^{2}Q\_{xx}\^{-1}{\\big
)},} where Q x x = X T X . {\\displaystyle Q\_{xx}=X\^{T}X.} Intervals
Using this asymptotic distribution, approximate two-sided confidence
intervals for the j-th component of the vector β \^ {\\displaystyle
{\\hat {\\beta }}} can be constructed as β j ∈ \[ β \^ j ± q 1 − α 2 N (
0 , 1 ) σ \^ 2 \[ Q x x − 1 \] j j \] {\\displaystyle \\beta \_{j}\\in
{\\bigg \[}\\ {\\hat {\\beta }}\_{j}\\pm q\_{1-{\\frac {\\alpha
}{2}}}\^{{\\mathcal {N}}(0,1)}\\!{\\sqrt {{\\hat {\\sigma
}}\^{2}\\left\[Q\_{xx}\^{-1}\\right\]\_{jj}}}\\ {\\bigg \]}} at the 1 −
α confidence level,where q denotes the quantile function of standard
normal distribution, and \[·\]jj is the j-th diagonal element of a
matrix. Similarly, the least squares estimator for σ2 is also consistent
and asymptotically normal (provided that the fourth moment of εi exists)
with limiting distribution ( σ \^ 2 − σ 2 ) → d N ( 0 , E ⁡ \[ ε i 4 \] −
σ 4 ) . {\\displaystyle ({\\hat {\\sigma }}\^{2}-\\sigma \^{2})\\
{\\xrightarrow {d}}\\ {\\mathcal {N}}\\left(0,\\;\\operatorname {E}
\\left\[\\varepsilon \_{i}\^{4}\\right\]-\\sigma \^{4}\\right).} These
asymptotic distributions can be used for prediction, testing hypotheses,
constructing other estimators, etc.. As an example consider the problem
of prediction. Suppose x 0 {\\displaystyle x\_{0}} is some point within
the domain of distribution of the regressors, and one wants to know what
the response variable would have been at that point. The mean response
is the quantity y 0 = x 0 T β {\\displaystyle y\_{0}=x\_{0}\^{\\mathrm
{T} }\\beta } , whereas the predicted response is y \^ 0 = x 0 T β \^
{\\displaystyle {\\hat {y}}\_{0}=x\_{0}\^{\\mathrm {T} }{\\hat {\\beta
}}} . Clearly the predicted response is a random variable, its
distribution can be derived from that of β \^ {\\displaystyle {\\hat
{\\beta }}} : ( y \^ 0 − y 0 ) → d N ( 0 , σ 2 x 0 T Q x x − 1 x 0 ) ,
{\\displaystyle \\left({\\hat {y}}\_{0}-y\_{0}\\right)\\ {\\xrightarrow
{d}}\\ {\\mathcal {N}}\\left(0,\\;\\sigma \^{2}x\_{0}\^{\\mathrm {T}
}Q\_{xx}\^{-1}x\_{0}\\right),} which allows construct confidence
intervals for mean response y 0 {\\displaystyle y\_{0}} to be
constructed: y 0 ∈ \[ x 0 T β \^ ± q 1 − α 2 N ( 0 , 1 ) σ \^ 2 x 0 T Q
x x − 1 x 0 \] {\\displaystyle y\_{0}\\in \\left\[\\ x\_{0}\^{\\mathrm
{T} }{\\hat {\\beta }}\\pm q\_{1-{\\frac {\\alpha }{2}}}\^{{\\mathcal
{N}}(0,1)}\\!{\\sqrt {{\\hat {\\sigma }}\^{2}x\_{0}\^{\\mathrm {T}
}Q\_{xx}\^{-1}x\_{0}}}\\ \\right\]} at the 1 − α confidence level.
Hypothesis testing Two hypothesis tests are particularly widely used.
First, one wants to know if the estimated regression equation is any
better than simply predicting that all values of the response variable
equal its sample mean (if not, it is said to have no explanatory power).
The null hypothesis of no explanatory value of the estimated regression
is tested using an F-test. If the calculated F-value is found to be
large enough to exceed its critical value for the pre-chosen level of
significance, the null hypothesis is rejected and the alternative
hypothesis, that the regression has explanatory power, is accepted.
Otherwise, the null hypothesis of no explanatory power is accepted.
Second, for each explanatory variable of interest, one wants to know
whether its estimated coefficient differs significantly from zero---that
is, whether this particular explanatory variable in fact has explanatory
power in predicting the response variable. Here the null hypothesis is
that the true coefficient is zero. This hypothesis is tested by
computing the coefficient\'s t-statistic, as the ratio of the
coefficient estimate to its standard error. If the t-statistic is larger
than a predetermined value, the null hypothesis is rejected and the
variable is found to have explanatory power, with its coefficient
significantly different from zero. Otherwise, the null hypothesis of a
zero value of the true coefficient is accepted. In addition, the Chow
test is used to test whether two subsamples both have the same
underlying true coefficient values. The sum of squared residuals of
regressions on each of the subsets and on the combined data set are
compared by computing an F-statistic; if this exceeds a critical value,
the null hypothesis of no difference between the two subsets is
rejected; otherwise, it is accepted. Example with real data The
following data set gives average heights and weights for American women
aged 30--39 (source: The World Almanac and Book of Facts, 1975). When
only one dependent variable is being modeled, a scatterplot will suggest
the form and strength of the relationship between the dependent variable
and regressors. It might also reveal outliers, heteroscedasticity, and
other aspects of the data that may complicate the interpretation of a
fitted regression model. The scatterplot suggests that the relationship
is strong and can be approximated as a quadratic function. OLS can
handle non-linear relationships by introducing the regressor HEIGHT2.
The regression model then becomes a multiple linear model: w i = β 1 + β
2 h i + β 3 h i 2 + ε i . {\\displaystyle w\_{i}=\\beta \_{1}+\\beta
\_{2}h\_{i}+\\beta \_{3}h\_{i}\^{2}+\\varepsilon \_{i}.} The output from
most popular statistical packages will look similar to this: In this
table: The Value column gives the least squares estimates of parameters
βj The Std error column shows standard errors of each coefficient
estimate: σ \^ j = ( σ \^ 2 \[ Q x x − 1 \] j j ) 1 2 {\\displaystyle
{\\hat {\\sigma }}\_{j}=\\left({\\hat {\\sigma
}}\^{2}\\left\[Q\_{xx}\^{-1}\\right\]\_{jj}\\right)\^{\\frac {1}{2}}}
The t-statistic and p-value columns are testing whether any of the
coefficients might be equal to zero. The t-statistic is calculated
simply as t = β \^ j / σ \^ j {\\displaystyle t={\\hat {\\beta
}}\_{j}/{\\hat {\\sigma }}\_{j}} . If the errors ε follow a normal
distribution, t follows a Student-t distribution. Under weaker
conditions, t is asymptotically normal. Large values of t indicate that
the null hypothesis can be rejected and that the corresponding
coefficient is not zero. The second column, p-value, expresses the
results of the hypothesis test as a significance level. Conventionally,
p-values smaller than 0.05 are taken as evidence that the population
coefficient is nonzero. R-squared is the coefficient of determination
indicating goodness-of-fit of the regression. This statistic will be
equal to one if fit is perfect, and to zero when regressors X have no
explanatory power whatsoever. This is a biased estimate of the
population R-squared, and will never decrease if additional regressors
are added, even if they are irrelevant. Adjusted R-squared is a slightly
modified version of R 2 {\\displaystyle R\^{2}} , designed to penalize
for the excess number of regressors which do not add to the explanatory
power of the regression. This statistic is always smaller than R 2
{\\displaystyle R\^{2}} , can decrease as new regressors are added, and
even be negative for poorly fitting models: R ¯ 2 = 1 − n − 1 n − p ( 1
− R 2 ) {\\displaystyle {\\overline {R}}\^{2}=1-{\\frac
{n-1}{n-p}}(1-R\^{2})} Log-likelihood is calculated under the assumption
that errors follow normal distribution. Even though the assumption is
not very reasonable, this statistic may still find its use in conducting
LR tests. Durbin--Watson statistic tests whether there is any evidence
of serial correlation between the residuals. As a rule of thumb, the
value smaller than 2 will be an evidence of positive correlation. Akaike
information criterion and Schwarz criterion are both used for model
selection. Generally when comparing two alternative models, smaller
values of one of these criteria will indicate a better model. Standard
error of regression is an estimate of σ, standard error of the error
term. Total sum of squares, model sum of squared, and residual sum of
squares tell us how much of the initial variation in the sample were
explained by the regression. F-statistic tries to test the hypothesis
that all coefficients (except the intercept) are equal to zero. This
statistic has F(p--1,n--p) distribution under the null hypothesis and
normality assumption, and its p-value indicates probability that the
hypothesis is indeed true. Note that when errors are not normal this
statistic becomes invalid, and other tests such as Wald test or LR test
should be used. Ordinary least squares analysis often includes the use
of diagnostic plots designed to detect departures of the data from the
assumed form of the model. These are some of the common diagnostic
plots: Residuals against the explanatory variables in the model. A
non-linear relation between these variables suggests that the linearity
of the conditional mean function may not hold. Different levels of
variability in the residuals for different levels of the explanatory
variables suggests possible heteroscedasticity. Residuals against
explanatory variables not in the model. Any relation of the residuals to
these variables would suggest considering these variables for inclusion
in the model. Residuals against the fitted values, y \^ {\\displaystyle
{\\hat {y}}} . Residuals against the preceding residual. This plot may
identify serial correlations in the residuals.An important consideration
when carrying out statistical inference using regression models is how
the data were sampled. In this example, the data are averages rather
than measurements on individual women. The fit of the model is very
good, but this does not imply that the weight of an individual woman can
be predicted with high accuracy based only on her height. Sensitivity to
rounding This example also demonstrates that coefficients determined by
these calculations are sensitive to how the data is prepared. The
heights were originally given rounded to the nearest inch and have been
converted and rounded to the nearest centimetre. Since the conversion
factor is one inch to 2.54 cm this is not an exact conversion. The
original inches can be recovered by Round(x/0.0254) and then
re-converted to metric without rounding. If this is done the results
become: Using either of these equations to predict the weight of a 5\'
6\" (1.6764 m) woman gives similar values: 62.94 kg with rounding vs.
62.98 kg without rounding. Thus a seemingly small variation in the data
has a real effect on the coefficients but a small effect on the results
of the equation. While this may look innocuous in the middle of the data
range it could become significant at the extremes or in the case where
the fitted model is used to project outside the data range
(extrapolation). This highlights a common error: this example is an
abuse of OLS which inherently requires that the errors in the
independent variable (in this case height) are zero or at least
negligible. The initial rounding to nearest inch plus any actual
measurement errors constitute a finite and non-negligible error. As a
result, the fitted parameters are not the best estimates they are
presumed to be. Though not totally spurious the error in the estimation
will depend upon relative size of the x and y errors. Another example
with less real data Problem statement We can use the least square
mechanism to figure out the equation of a two body orbit in polar base
co-ordinates. The equation typically used is r ( θ ) = p 1 − e cos ⁡ ( θ
) {\\displaystyle r(\\theta )={\\frac {p}{1-e\\cos(\\theta )}}} where r
( θ ) {\\displaystyle r(\\theta )} is the radius of how far the object
is from one of the bodies. In the equation the parameters p
{\\displaystyle p} and e {\\displaystyle e} are used to determine the
path of the orbit. We have measured the following data. We need to find
the least-squares approximation of e {\\displaystyle e} and p
{\\displaystyle p} for the given data. Solution First we need to
represent e and p in a linear form. So we are going to rewrite the
equation r ( θ ) {\\displaystyle r(\\theta )} as 1 r ( θ ) = 1 p − e p
cos ⁡ ( θ ) {\\displaystyle {\\frac {1}{r(\\theta )}}={\\frac
{1}{p}}-{\\frac {e}{p}}\\cos(\\theta )} . Now we can use this form to
represent our observational data as: A T A ( x y ) = A T b
{\\displaystyle A\^{T}A{\\binom {x}{y}}=A\^{T}b} where x {\\displaystyle
x} is 1 p {\\displaystyle {\\frac {1}{p}}} and y {\\displaystyle y} is e
p {\\displaystyle {\\frac {e}{p}}} and A {\\displaystyle A} is
constructed by the first column being the coefficient of 1 p
{\\displaystyle {\\frac {1}{p}}} and the second column being the
coefficient of e p {\\displaystyle {\\frac {e}{p}}} and b
{\\displaystyle b} is the values for the respective 1 r ( θ )
{\\displaystyle {\\frac {1}{r(\\theta )}}} so A = \[ 1 − 0.731354 1 −
0.707107 1 − 0.615661 1 0.052336 1 0.309017 1 0.438371 \]
{\\displaystyle
A={\\begin{bmatrix}1&-0.731354\\\\1&-0.707107\\\\1&-0.615661\\\\1&\\
0.052336\\\\1&0.309017\\\\1&0.438371\\end{bmatrix}}} and b = \[ 0.21220
0.21958 0.24741 0.45071 0.52883 0.56820 \] . {\\displaystyle
b={\\begin{bmatrix}0.21220\\\\0.21958\\\\0.24741\\\\0.45071\\\\0.52883\\\\0.56820\\end{bmatrix}}.}
On solving we get ( x y ) = ( 0.43478 0.30435 ) {\\displaystyle {\\binom
{x}{y}}={\\binom {0.43478}{0.30435}}} so p = 1 x = 2.3000
{\\displaystyle p={\\frac {1}{x}}=2.3000} and e = p ⋅ y = 0.70001
{\\displaystyle e=p\\cdot y=0.70001} See also Bayesian least squares
Fama--MacBeth regression Nonlinear least squares Numerical methods for
linear least squares Nonlinear system identification References Further
reading Dougherty, Christopher (2002). Introduction to Econometrics (2nd
ed.). New York: Oxford University Press. pp. 48--113. ISBN
0-19-877643-8. Gujarati, Damodar N.; Porter, Dawn C. (2009). Basic
Econometics (Fifth ed.). Boston: McGraw-Hill Irwin. pp. 55--96. ISBN
978-0-07-337577-9. Heij, Christiaan; Boer, Paul; Franses, Philip H.;
Kloek, Teun; van Dijk, Herman K. (2004). Econometric Methods with
Applications in Business and Economics (1st ed.). Oxford: Oxford
University Press. pp. 76--115. ISBN 978-0-19-926801-6. Hill, R. Carter;
Griffiths, William E.; Lim, Guay C. (2008). Principles of Econometrics
(3rd ed.). Hoboken, NJ: John Wiley & Sons. pp. 8--47. ISBN
978-0-471-72360-8. Wooldridge, Jeffrey (2008). \"The Simple Regression
Model\". Introductory Econometrics: A Modern Approach (4th ed.). Mason,
OH: Cengage Learning. pp. 22--67. ISBN 978-0-324-58162-1.
