In statistics, polynomial regression is a form of regression analysis in
which the relationship between the independent variable x and the
dependent variable y is modelled as an nth degree polynomial in x.
Polynomial regression fits a nonlinear relationship between the value of
x and the corresponding conditional mean of y, denoted E(y \|x).
Although polynomial regression fits a nonlinear model to the data, as a
statistical estimation problem it is linear, in the sense that the
regression function E(y \| x) is linear in the unknown parameters that
are estimated from the data. For this reason, polynomial regression is
considered to be a special case of multiple linear regression. The
explanatory (independent) variables resulting from the polynomial
expansion of the \"baseline\" variables are known as higher-degree
terms. Such variables are also used in classification settings. History
Polynomial regression models are usually fit using the method of least
squares. The least-squares method minimizes the variance of the unbiased
estimators of the coefficients, under the conditions of the
Gauss--Markov theorem. The least-squares method was published in 1805 by
Legendre and in 1809 by Gauss. The first design of an experiment for
polynomial regression appeared in an 1815 paper of Gergonne. In the
twentieth century, polynomial regression played an important role in the
development of regression analysis, with a greater emphasis on issues of
design and inference. More recently, the use of polynomial models has
been complemented by other methods, with non-polynomial models having
advantages for some classes of problems. Definition and example The goal
of regression analysis is to model the expected value of a dependent
variable y in terms of the value of an independent variable (or vector
of independent variables) x. In simple linear regression, the model y =
β 0 + β 1 x + ε , {\\displaystyle y=\\beta \_{0}+\\beta
\_{1}x+\\varepsilon ,\\,} is used, where ε is an unobserved random error
with mean zero conditioned on a scalar variable x. In this model, for
each unit increase in the value of x, the conditional expectation of y
increases by β1 units. In many settings, such a linear relationship may
not hold. For example, if we are modeling the yield of a chemical
synthesis in terms of the temperature at which the synthesis takes
place, we may find that the yield improves by increasing amounts for
each unit increase in temperature. In this case, we might propose a
quadratic model of the form y = β 0 + β 1 x + β 2 x 2 + ε .
{\\displaystyle y=\\beta \_{0}+\\beta \_{1}x+\\beta
\_{2}x\^{2}+\\varepsilon .\\,} In this model, when the temperature is
increased from x to x + 1 units, the expected yield changes by β 1 + β 2
( 2 x + 1 ) . {\\displaystyle \\beta \_{1}+\\beta \_{2}(2x+1).} (This
can be seen by replacing x in this equation with x+1 and subtracting the
equation in x from the equation in x+1.) For infinitesimal changes in x,
the effect on y is given by the total derivative with respect to x: β
1 + 2 β 2 x . {\\displaystyle \\beta \_{1}+2\\beta \_{2}x.} The fact
that the change in yield depends on x is what makes the relationship
between x and y nonlinear even though the model is linear in the
parameters to be estimated. In general, we can model the expected value
of y as an nth degree polynomial, yielding the general polynomial
regression model y = β 0 + β 1 x + β 2 x 2 + β 3 x 3 + ⋯ + β n x n + ε .
{\\displaystyle y=\\beta \_{0}+\\beta \_{1}x+\\beta \_{2}x\^{2}+\\beta
\_{3}x\^{3}+\\cdots +\\beta \_{n}x\^{n}+\\varepsilon .\\,} Conveniently,
these models are all linear from the point of view of estimation, since
the regression function is linear in terms of the unknown parameters β0,
β1, \.... Therefore, for least squares analysis, the computational and
inferential problems of polynomial regression can be completely
addressed using the techniques of multiple regression. This is done by
treating x, x2, \... as being distinct independent variables in a
multiple regression model. Matrix form and calculation of estimates The
polynomial regression model y i = β 0 + β 1 x i + β 2 x i 2 + ⋯ + β m x
i m + ε i ( i = 1 , 2 , ... , n ) {\\displaystyle y\_{i}\\,=\\,\\beta
\_{0}+\\beta \_{1}x\_{i}+\\beta \_{2}x\_{i}\^{2}+\\cdots +\\beta
\_{m}x\_{i}\^{m}+\\varepsilon \_{i}\\ (i=1,2,\\dots ,n)} can be
expressed in matrix form in terms of a design matrix X {\\displaystyle
\\mathbf {X} } , a response vector y → {\\displaystyle {\\vec {y}}} , a
parameter vector β → {\\displaystyle {\\vec {\\beta }}} , and a vector ε
→ {\\displaystyle {\\vec {\\varepsilon }}} of random errors. The i-th
row of X {\\displaystyle \\mathbf {X} } and y → {\\displaystyle {\\vec
{y}}} will contain the x and y value for the i-th data sample. Then the
model can be written as a system of linear equations: \[ y 1 y 2 y 3 ⋮ y
n \] = \[ 1 x 1 x 1 2 ... x 1 m 1 x 2 x 2 2 ... x 2 m 1 x 3 x 3 2 ... x
3 m ⋮ ⋮ ⋮ ⋱ ⋮ 1 x n x n 2 ... x n m \] \[ β 0 β 1 β 2 ⋮ β m \] + \[ ε 1
ε 2 ε 3 ⋮ ε n \] , {\\displaystyle
{\\begin{bmatrix}y\_{1}\\\\y\_{2}\\\\y\_{3}\\\\\\vdots
\\\\y\_{n}\\end{bmatrix}}={\\begin{bmatrix}1&x\_{1}&x\_{1}\^{2}&\\dots
&x\_{1}\^{m}\\\\1&x\_{2}&x\_{2}\^{2}&\\dots
&x\_{2}\^{m}\\\\1&x\_{3}&x\_{3}\^{2}&\\dots &x\_{3}\^{m}\\\\\\vdots
&\\vdots &\\vdots &\\ddots &\\vdots \\\\1&x\_{n}&x\_{n}\^{2}&\\dots
&x\_{n}\^{m}\\end{bmatrix}}{\\begin{bmatrix}\\beta \_{0}\\\\\\beta
\_{1}\\\\\\beta \_{2}\\\\\\vdots \\\\\\beta
\_{m}\\end{bmatrix}}+{\\begin{bmatrix}\\varepsilon \_{1}\\\\\\varepsilon
\_{2}\\\\\\varepsilon \_{3}\\\\\\vdots \\\\\\varepsilon
\_{n}\\end{bmatrix}},} which when using pure matrix notation is written
as y → = X β → + ε → . {\\displaystyle {\\vec {y}}=\\mathbf {X} {\\vec
{\\beta }}+{\\vec {\\varepsilon }}.\\,} The vector of estimated
polynomial regression coefficients (using ordinary least squares
estimation) is β → \^ = ( X T X ) − 1 X T y → , {\\displaystyle
{\\widehat {\\vec {\\beta }}}=(\\mathbf {X} \^{\\mathsf {T}}\\mathbf {X}
)\^{-1}\\;\\mathbf {X} \^{\\mathsf {T}}{\\vec {y}},\\,} assuming m \< n
which is required for the matrix to be invertible; then since X
{\\displaystyle \\mathbf {X} } is a Vandermonde matrix, the
invertibility condition is guaranteed to hold if all the x i
{\\displaystyle x\_{i}} values are distinct. This is the unique
least-squares solution. Interpretation Although polynomial regression is
technically a special case of multiple linear regression, the
interpretation of a fitted polynomial regression model requires a
somewhat different perspective. It is often difficult to interpret the
individual coefficients in a polynomial regression fit, since the
underlying monomials can be highly correlated. For example, x and x2
have correlation around 0.97 when x is uniformly distributed on the
interval (0, 1). Although the correlation can be reduced by using
orthogonal polynomials, it is generally more informative to consider the
fitted regression function as a whole. Point-wise or simultaneous
confidence bands can then be used to provide a sense of the uncertainty
in the estimate of the regression function. Alternative approaches
Polynomial regression is one example of regression analysis using basis
functions to model a functional relationship between two quantities.
More specifically, it replaces x ∈ R d x {\\displaystyle x\\in \\mathbb
{R} \^{d\_{x}}} in linear regression with polynomial basis φ ( x ) ∈ R d
φ {\\displaystyle \\varphi (x)\\in \\mathbb {R} \^{d\_{\\varphi }}} ,
e.g. \[ 1 , x \] → φ \[ 1 , x , x 2 , ... , x d \] {\\displaystyle
\[1,x\]{\\mathbin {\\stackrel {\\varphi }{\\rightarrow
}}}\[1,x,x\^{2},\\ldots ,x\^{d}\]} . A drawback of polynomial bases is
that the basis functions are \"non-local\", meaning that the fitted
value of y at a given value x = x0 depends strongly on data values with
x far from x0. In modern statistics, polynomial basis-functions are used
along with new basis functions, such as splines, radial basis functions,
and wavelets. These families of basis functions offer a more
parsimonious fit for many types of data. The goal of polynomial
regression is to model a non-linear relationship between the independent
and dependent variables (technically, between the independent variable
and the conditional mean of the dependent variable). This is similar to
the goal of nonparametric regression, which aims to capture non-linear
regression relationships. Therefore, non-parametric regression
approaches such as smoothing can be useful alternatives to polynomial
regression. Some of these methods make use of a localized form of
classical polynomial regression. An advantage of traditional polynomial
regression is that the inferential framework of multiple regression can
be used (this also holds when using other families of basis functions
such as splines). A final alternative is to use kernelized models such
as support vector regression with a polynomial kernel. If residuals have
unequal variance, a weighted least squares estimator may be used to
account for that. See also Curve fitting Line regression Local
polynomial regression Polynomial and rational function modeling
Polynomial interpolation Response surface methodology Smoothing spline
Notes Microsoft Excel makes use of polynomial regression when fitting a
trendline to data points on an X Y scatter plot. References External
links Curve Fitting, PhET Interactive simulations, University of
Colorado at Boulder
