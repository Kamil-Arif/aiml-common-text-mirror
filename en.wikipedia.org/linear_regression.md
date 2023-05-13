In statistics, linear regression is a linear approach for modelling the
relationship between a scalar response and one or more explanatory
variables (also known as dependent and independent variables). The case
of one explanatory variable is called simple linear regression; for more
than one, the process is called multiple linear regression. This term is
distinct from multivariate linear regression, where multiple correlated
dependent variables are predicted, rather than a single scalar
variable.In linear regression, the relationships are modeled using
linear predictor functions whose unknown model parameters are estimated
from the data. Such models are called linear models. Most commonly, the
conditional mean of the response given the values of the explanatory
variables (or predictors) is assumed to be an affine function of those
values; less commonly, the conditional median or some other quantile is
used. Like all forms of regression analysis, linear regression focuses
on the conditional probability distribution of the response given the
values of the predictors, rather than on the joint probability
distribution of all of these variables, which is the domain of
multivariate analysis. Linear regression was the first type of
regression analysis to be studied rigorously, and to be used extensively
in practical applications. This is because models which depend linearly
on their unknown parameters are easier to fit than models which are
non-linearly related to their parameters and because the statistical
properties of the resulting estimators are easier to determine. Linear
regression has many practical uses. Most applications fall into one of
the following two broad categories: If the goal is error reduction in
prediction or forecasting, linear regression can be used to fit a
predictive model to an observed data set of values of the response and
explanatory variables. After developing such a model, if additional
values of the explanatory variables are collected without an
accompanying response value, the fitted model can be used to make a
prediction of the response. If the goal is to explain variation in the
response variable that can be attributed to variation in the explanatory
variables, linear regression analysis can be applied to quantify the
strength of the relationship between the response and the explanatory
variables, and in particular to determine whether some explanatory
variables may have no linear relationship with the response at all, or
to identify which subsets of explanatory variables may contain redundant
information about the response.Linear regression models are often fitted
using the least squares approach, but they may also be fitted in other
ways, such as by minimizing the \"lack of fit\" in some other norm (as
with least absolute deviations regression), or by minimizing a penalized
version of the least squares cost function as in ridge regression
(L2-norm penalty) and lasso (L1-norm penalty). Conversely, the least
squares approach can be used to fit models that are not linear models.
Thus, although the terms \"least squares\" and \"linear model\" are
closely linked, they are not synonymous. Formulation Given a data set {
y i , x i 1 , ... , x i p } i = 1 n {\\displaystyle
\\{y\_{i},\\,x\_{i1},\\ldots ,x\_{ip}\\}\_{i=1}\^{n}} of n statistical
units, a linear regression model assumes that the relationship between
the dependent variable y and the vector of regressors x is linear. This
relationship is modeled through a disturbance term or error variable ε
--- an unobserved random variable that adds \"noise\" to the linear
relationship between the dependent variable and regressors. Thus the
model takes the form where T denotes the transpose, so that xiTβ is the
inner product between vectors xi and β. Often these n equations are
stacked together and written in matrix notation as y = X β + ε ,
{\\displaystyle \\mathbf {y} =\\mathbf {X} {\\boldsymbol {\\beta
}}+{\\boldsymbol {\\varepsilon }},\\,} where y = \[ y 1 y 2 ⋮ y n \] ,
{\\displaystyle \\mathbf {y}
={\\begin{bmatrix}y\_{1}\\\\y\_{2}\\\\\\vdots
\\\\y\_{n}\\end{bmatrix}},\\quad } X = \[ x 1 T x 2 T ⋮ x n T \] = \[ 1
x 11 ⋯ x 1 p 1 x 21 ⋯ x 2 p ⋮ ⋮ ⋱ ⋮ 1 x n 1 ⋯ x n p \] , {\\displaystyle
\\mathbf {X} ={\\begin{bmatrix}\\mathbf {x} \_{1}\^{\\mathsf
{T}}\\\\\\mathbf {x} \_{2}\^{\\mathsf {T}}\\\\\\vdots \\\\\\mathbf {x}
\_{n}\^{\\mathsf {T}}\\end{bmatrix}}={\\begin{bmatrix}1&x\_{11}&\\cdots
&x\_{1p}\\\\1&x\_{21}&\\cdots &x\_{2p}\\\\\\vdots &\\vdots &\\ddots
&\\vdots \\\\1&x\_{n1}&\\cdots &x\_{np}\\end{bmatrix}},} β = \[ β 0 β 1
β 2 ⋮ β p \] , ε = \[ ε 1 ε 2 ⋮ ε n \] . {\\displaystyle {\\boldsymbol
{\\beta }}={\\begin{bmatrix}\\beta \_{0}\\\\\\beta \_{1}\\\\\\beta
\_{2}\\\\\\vdots \\\\\\beta \_{p}\\end{bmatrix}},\\quad {\\boldsymbol
{\\varepsilon }}={\\begin{bmatrix}\\varepsilon \_{1}\\\\\\varepsilon
\_{2}\\\\\\vdots \\\\\\varepsilon \_{n}\\end{bmatrix}}.} Notation and
terminology y {\\displaystyle \\mathbf {y} } is a vector of observed
values y i ( i = 1 , ... , n ) {\\displaystyle y\_{i}\\ (i=1,\\ldots
,n)} of the variable called the regressand, endogenous variable,
response variable, measured variable, criterion variable, or dependent
variable. This variable is also sometimes known as the predicted
variable, but this should not be confused with predicted values, which
are denoted y \^ {\\displaystyle {\\hat {y}}} . The decision as to which
variable in a data set is modeled as the dependent variable and which
are modeled as the independent variables may be based on a presumption
that the value of one of the variables is caused by, or directly
influenced by the other variables. Alternatively, there may be an
operational reason to model one of the variables in terms of the others,
in which case there need be no presumption of causality. X
{\\displaystyle \\mathbf {X} } may be seen as a matrix of row-vectors x
i ⋅ {\\displaystyle \\mathbf {x} \_{i\\cdot }} or of n-dimensional
column-vectors x ⋅ j {\\displaystyle \\mathbf {x} \_{\\cdot j}} , which
are known as regressors, exogenous variables, explanatory variables,
covariates, input variables, predictor variables, or independent
variables (not to be confused with the concept of independent random
variables). The matrix X {\\displaystyle \\mathbf {X} } is sometimes
called the design matrix. Usually a constant is included as one of the
regressors. In particular, x i 0 = 1 {\\displaystyle x\_{i0}=1} for i =
1 , ... , n {\\displaystyle i=1,\\ldots ,n} . The corresponding element
of β is called the intercept. Many statistical inference procedures for
linear models require an intercept to be present, so it is often
included even if theoretical considerations suggest that its value
should be zero. Sometimes one of the regressors can be a non-linear
function of another regressor or of the data, as in polynomial
regression and segmented regression. The model remains linear as long as
it is linear in the parameter vector β. The values xij may be viewed as
either observed values of random variables Xj or as fixed values chosen
prior to observing the dependent variable. Both interpretations may be
appropriate in different cases, and they generally lead to the same
estimation procedures; however different approaches to asymptotic
analysis are used in these two situations. β {\\displaystyle
{\\boldsymbol {\\beta }}} is a ( p + 1 ) {\\displaystyle (p+1)}
-dimensional parameter vector, where β 0 {\\displaystyle \\beta \_{0}}
is the intercept term (if one is included in the model---otherwise β
{\\displaystyle {\\boldsymbol {\\beta }}} is p-dimensional). Its
elements are known as effects or regression coefficients (although the
latter term is sometimes reserved for the estimated effects). In simple
linear regression, p=1, and the coefficient is known as regression
slope. Statistical estimation and inference in linear regression focuses
on β. The elements of this parameter vector are interpreted as the
partial derivatives of the dependent variable with respect to the
various independent variables. ε {\\displaystyle {\\boldsymbol
{\\varepsilon }}} is a vector of values ε i {\\displaystyle \\varepsilon
\_{i}} . This part of the model is called the error term, disturbance
term, or sometimes noise (in contrast with the \"signal\" provided by
the rest of the model). This variable captures all other factors which
influence the dependent variable y other than the regressors x. The
relationship between the error term and the regressors, for example
their correlation, is a crucial consideration in formulating a linear
regression model, as it will determine the appropriate estimation
method.Fitting a linear model to a given data set usually requires
estimating the regression coefficients β {\\displaystyle {\\boldsymbol
{\\beta }}} such that the error term ε = y − X β {\\displaystyle
{\\boldsymbol {\\varepsilon }}=\\mathbf {y} -\\mathbf {X} {\\boldsymbol
{\\beta }}} is minimized. For example, it is common to use the sum of
squared errors ‖ ε ‖ 2 2 {\\displaystyle \\\|{\\boldsymbol {\\varepsilon
}}\\\|\_{2}\^{2}} as a measure of ε {\\displaystyle {\\boldsymbol
{\\varepsilon }}} for minimization. Example Consider a situation where a
small ball is being tossed up in the air and then we measure its heights
of ascent hi at various moments in time ti. Physics tells us that,
ignoring the drag, the relationship can be modeled as h i = β 1 t i + β
2 t i 2 + ε i , {\\displaystyle h\_{i}=\\beta \_{1}t\_{i}+\\beta
\_{2}t\_{i}\^{2}+\\varepsilon \_{i},} where β1 determines the initial
velocity of the ball, β2 is proportional to the standard gravity, and εi
is due to measurement errors. Linear regression can be used to estimate
the values of β1 and β2 from the measured data. This model is non-linear
in the time variable, but it is linear in the parameters β1 and β2; if
we take regressors xi = (xi1, xi2) = (ti, ti2), the model takes on the
standard form h i = x i T β + ε i . {\\displaystyle h\_{i}=\\mathbf {x}
\_{i}\^{\\mathsf {T}}{\\boldsymbol {\\beta }}+\\varepsilon \_{i}.}
Assumptions Standard linear regression models with standard estimation
techniques make a number of assumptions about the predictor variables,
the response variables and their relationship. Numerous extensions have
been developed that allow each of these assumptions to be relaxed (i.e.
reduced to a weaker form), and in some cases eliminated entirely.
Generally these extensions make the estimation procedure more complex
and time-consuming, and may also require more data in order to produce
an equally precise model. The following are the major assumptions made
by standard linear regression models with standard estimation techniques
(e.g. ordinary least squares): Weak exogeneity. This essentially means
that the predictor variables x can be treated as fixed values, rather
than random variables. This means, for example, that the predictor
variables are assumed to be error-free---that is, not contaminated with
measurement errors. Although this assumption is not realistic in many
settings, dropping it leads to significantly more difficult
errors-in-variables models. Linearity. This means that the mean of the
response variable is a linear combination of the parameters (regression
coefficients) and the predictor variables. Note that this assumption is
much less restrictive than it may at first seem. Because the predictor
variables are treated as fixed values (see above), linearity is really
only a restriction on the parameters. The predictor variables themselves
can be arbitrarily transformed, and in fact multiple copies of the same
underlying predictor variable can be added, each one transformed
differently. This technique is used, for example, in polynomial
regression, which uses linear regression to fit the response variable as
an arbitrary polynomial function (up to a given degree) of a predictor
variable. With this much flexibility, models such as polynomial
regression often have \"too much power\", in that they tend to overfit
the data. As a result, some kind of regularization must typically be
used to prevent unreasonable solutions coming out of the estimation
process. Common examples are ridge regression and lasso regression.
Bayesian linear regression can also be used, which by its nature is more
or less immune to the problem of overfitting. (In fact, ridge regression
and lasso regression can both be viewed as special cases of Bayesian
linear regression, with particular types of prior distributions placed
on the regression coefficients.) Constant variance (a.k.a.
homoscedasticity). This means that the variance of the errors does not
depend on the values of the predictor variables. Thus the variability of
the responses for given fixed values of the predictors is the same
regardless of how large or small the responses are. This is often not
the case, as a variable whose mean is large will typically have a
greater variance than one whose mean is small. For example, a person
whose income is predicted to be \$100,000 may easily have an actual
income of \$80,000 or \$120,000---i.e., a standard deviation of around
\$20,000---while another person with a predicted income of \$10,000 is
unlikely to have the same \$20,000 standard deviation, since that would
imply their actual income could vary anywhere between −\$10,000 and
\$30,000. (In fact, as this shows, in many cases---often the same cases
where the assumption of normally distributed errors fails---the variance
or standard deviation should be predicted to be proportional to the
mean, rather than constant.) The absence of homoscedasticity is called
heteroscedasticity. In order to check this assumption, a plot of
residuals versus predicted values (or the values of each individual
predictor) can be examined for a \"fanning effect\" (i.e., increasing or
decreasing vertical spread as one moves left to right on the plot). A
plot of the absolute or squared residuals versus the predicted values
(or each predictor) can also be examined for a trend or curvature.
Formal tests can also be used; see Heteroscedasticity. The presence of
heteroscedasticity will result in an overall \"average\" estimate of
variance being used instead of one that takes into account the true
variance structure. This leads to less precise (but in the case of
ordinary least squares, not biased) parameter estimates and biased
standard errors, resulting in misleading tests and interval estimates.
The mean squared error for the model will also be wrong. Various
estimation techniques including weighted least squares and the use of
heteroscedasticity-consistent standard errors can handle
heteroscedasticity in a quite general way. Bayesian linear regression
techniques can also be used when the variance is assumed to be a
function of the mean. It is also possible in some cases to fix the
problem by applying a transformation to the response variable (e.g.,
fitting the logarithm of the response variable using a linear regression
model, which implies that the response variable itself has a log-normal
distribution rather than a normal distribution). Independence of errors.
This assumes that the errors of the response variables are uncorrelated
with each other. (Actual statistical independence is a stronger
condition than mere lack of correlation and is often not needed,
although it can be exploited if it is known to hold.) Some methods such
as generalized least squares are capable of handling correlated errors,
although they typically require significantly more data unless some sort
of regularization is used to bias the model towards assuming
uncorrelated errors. Bayesian linear regression is a general way of
handling this issue. Lack of perfect multicollinearity in the
predictors. For standard least squares estimation methods, the design
matrix X must have full column rank p; otherwise perfect
multicollinearity exists in the predictor variables, meaning a linear
relationship exists between two or more predictor variables. This can be
caused by accidentally duplicating a variable in the data, using a
linear transformation of a variable along with the original (e.g., the
same temperature measurements expressed in Fahrenheit and Celsius), or
including a linear combination of multiple variables in the model, such
as their mean. It can also happen if there is too little data available
compared to the number of parameters to be estimated (e.g., fewer data
points than regression coefficients). Near violations of this
assumption, where predictors are highly but not perfectly correlated,
can reduce the precision of parameter estimates (see Variance inflation
factor). In the case of perfect multicollinearity, the parameter vector
β will be non-identifiable---it has no unique solution. In such a case,
only some of the parameters can be identified (i.e., their values can
only be estimated within some linear subspace of the full parameter
space Rp). See partial least squares regression. Methods for fitting
linear models with multicollinearity have been developed, some of which
require additional assumptions such as \"effect sparsity\"---that a
large fraction of the effects are exactly zero. Note that the more
computationally expensive iterated algorithms for parameter estimation,
such as those used in generalized linear models, do not suffer from this
problem.Beyond these assumptions, several other statistical properties
of the data strongly influence the performance of different estimation
methods: The statistical relationship between the error terms and the
regressors plays an important role in determining whether an estimation
procedure has desirable sampling properties such as being unbiased and
consistent. The arrangement, or probability distribution of the
predictor variables x has a major influence on the precision of
estimates of β. Sampling and design of experiments are highly developed
subfields of statistics that provide guidance for collecting data in
such a way to achieve a precise estimate of β. Interpretation A fitted
linear regression model can be used to identify the relationship between
a single predictor variable xj and the response variable y when all the
other predictor variables in the model are \"held fixed\". Specifically,
the interpretation of βj is the expected change in y for a one-unit
change in xj when the other covariates are held fixed---that is, the
expected value of the partial derivative of y with respect to xj. This
is sometimes called the unique effect of xj on y. In contrast, the
marginal effect of xj on y can be assessed using a correlation
coefficient or simple linear regression model relating only xj to y;
this effect is the total derivative of y with respect to xj. Care must
be taken when interpreting regression results, as some of the regressors
may not allow for marginal changes (such as dummy variables, or the
intercept term), while others cannot be held fixed (recall the example
from the introduction: it would be impossible to \"hold ti fixed\" and
at the same time change the value of ti2). It is possible that the
unique effect can be nearly zero even when the marginal effect is large.
This may imply that some other covariate captures all the information in
xj, so that once that variable is in the model, there is no contribution
of xj to the variation in y. Conversely, the unique effect of xj can be
large while its marginal effect is nearly zero. This would happen if the
other covariates explained a great deal of the variation of y, but they
mainly explain variation in a way that is complementary to what is
captured by xj. In this case, including the other variables in the model
reduces the part of the variability of y that is unrelated to xj,
thereby strengthening the apparent relationship with xj. The meaning of
the expression \"held fixed\" may depend on how the values of the
predictor variables arise. If the experimenter directly sets the values
of the predictor variables according to a study design, the comparisons
of interest may literally correspond to comparisons among units whose
predictor variables have been \"held fixed\" by the experimenter.
Alternatively, the expression \"held fixed\" can refer to a selection
that takes place in the context of data analysis. In this case, we
\"hold a variable fixed\" by restricting our attention to the subsets of
the data that happen to have a common value for the given predictor
variable. This is the only interpretation of \"held fixed\" that can be
used in an observational study. The notion of a \"unique effect\" is
appealing when studying a complex system where multiple interrelated
components influence the response variable. In some cases, it can
literally be interpreted as the causal effect of an intervention that is
linked to the value of a predictor variable. However, it has been argued
that in many cases multiple regression analysis fails to clarify the
relationships between the predictor variables and the response variable
when the predictors are correlated with each other and are not assigned
following a study design. Group effects In a multiple linear regression
model y = β 0 + β 1 x 1 + ⋯ + β p x p + ε , {\\displaystyle y=\\beta
\_{0}+\\beta \_{1}x\_{1}+\\cdots +\\beta \_{p}x\_{p}+\\varepsilon ,}
parameter β j {\\displaystyle \\beta \_{j}} of predictor variable x j
{\\displaystyle x\_{j}} represents the individual effect of x j
{\\displaystyle x\_{j}} . It has an interpretation as the expected
change in the response variable y {\\displaystyle y} when x j
{\\displaystyle x\_{j}} increases by one unit with other predictor
variables held constant. When x j {\\displaystyle x\_{j}} is strongly
correlated with other predictor variables, it is improbable that x j
{\\displaystyle x\_{j}} can increase by one unit with other variables
held constant. In this case, the interpretation of β j {\\displaystyle
\\beta \_{j}} becomes problematic as it is based on an improbable
condition, and the effect of x j {\\displaystyle x\_{j}} cannot be
evaluated in isolation. For a group of predictor variables, say, { x 1 ,
x 2 , ... , x q } {\\displaystyle \\{x\_{1},x\_{2},\\dots ,x\_{q}\\}} ,
a group effect ξ ( w ) {\\displaystyle \\xi (\\mathbf {w} )} is defined
as a linear combination of their parameters ξ ( w ) = w 1 β 1 + w 2 β
2 + ⋯ + w q β q , {\\displaystyle \\xi (\\mathbf {w} )=w\_{1}\\beta
\_{1}+w\_{2}\\beta \_{2}+\\dots +w\_{q}\\beta \_{q},} where w = ( w 1 ,
w 2 , ... , w q ) ⊺ {\\displaystyle \\mathbf {w} =(w\_{1},w\_{2},\\dots
,w\_{q})\^{\\intercal }} is a weight vector satisfying ∑ j = 1 q \| w j
\| = 1 {\\textstyle \\sum \_{j=1}\^{q}\|w\_{j}\|=1} . Because of the
constraint on w j {\\displaystyle {w\_{j}}} , ξ ( w ) {\\displaystyle
\\xi (\\mathbf {w} )} is also referred to as a normalized group effect.
A group effect ξ ( w ) {\\displaystyle \\xi (\\mathbf {w} )} has an
interpretation as the expected change in y {\\displaystyle y} when
variables in the group x 1 , x 2 , ... , x q {\\displaystyle
x\_{1},x\_{2},\\dots ,x\_{q}} change by the amount w 1 , w 2 , ... , w q
{\\displaystyle w\_{1},w\_{2},\\dots ,w\_{q}} , respectively, at the
same time with variables not in the group held constant. It generalizes
the individual effect of a variable to a group of variables in that ( i
{\\displaystyle i} ) if q = 1 {\\displaystyle q=1} , then the group
effect reduces to an individual effect, and ( i i {\\displaystyle ii} )
if w i = 1 {\\displaystyle w\_{i}=1} and w j = 0 {\\displaystyle
w\_{j}=0} for j ≠ i {\\displaystyle j\\neq i} , then the group effect
also reduces to an individual effect. A group effect ξ ( w )
{\\displaystyle \\xi (\\mathbf {w} )} is said to be meaningful if the
underlying simultaneous changes of the q {\\displaystyle q} variables (
w 1 , w 2 , ... , w q ) ⊺ {\\displaystyle (w\_{1},w\_{2},\\dots
,w\_{q})\^{\\intercal }} is probable. Group effects provide a means to
study the collective impact of strongly correlated predictor variables
in linear regression models. Individual effects of such variables are
not well-defined as their parameters do not have good interpretations.
Furthermore, when the sample size is not large, none of their parameters
can be accurately estimated by the least squares regression due to the
multicollinearity problem. Nevertheless, there are meaningful group
effects that have good interpretations and can be accurately estimated
by the least squares regression. A simple way to identify these
meaningful group effects is to use an all positive correlations (APC)
arrangement of the strongly correlated variables under which pairwise
correlations among these variables are all positive, and standardize all
p {\\displaystyle p} predictor variables in the model so that they all
have mean zero and length one. To illustrate this, suppose that { x 1 ,
x 2 , ... , x q } {\\displaystyle \\{x\_{1},x\_{2},\\dots ,x\_{q}\\}} is
a group of strongly correlated variables in an APC arrangement and that
they are not strongly correlated with predictor variables outside the
group. Let y ′ {\\displaystyle y\'} be the centred y {\\displaystyle y}
and x j ′ {\\displaystyle x\_{j}\'} be the standardized x j
{\\displaystyle x\_{j}} . Then, the standardized linear regression model
is y ′ = β 1 ′ x 1 ′ + ⋯ + β p ′ x p ′ + ε . {\\displaystyle y\'=\\beta
\_{1}\'x\_{1}\'+\\cdots +\\beta \_{p}\'x\_{p}\'+\\varepsilon .}
Parameters β j {\\displaystyle \\beta \_{j}} in the original model,
including β 0 {\\displaystyle \\beta \_{0}} , are simple functions of β
j ′ {\\displaystyle \\beta \_{j}\'} in the standardized model. The
standardization of variables does not change their correlations, so { x
1 ′ , x 2 ′ , ... , x q ′ } {\\displaystyle \\{x\_{1}\',x\_{2}\',\\dots
,x\_{q}\'\\}} is a group of strongly correlated variables in an APC
arrangement and they are not strongly correlated with other predictor
variables in the standardized model. A group effect of { x 1 ′ , x 2 ′ ,
... , x q ′ } {\\displaystyle \\{x\_{1}\',x\_{2}\',\\dots ,x\_{q}\'\\}}
is ξ ′ ( w ) = w 1 β 1 ′ + w 2 β 2 ′ + ⋯ + w q β q ′ , {\\displaystyle
\\xi \'(\\mathbf {w} )=w\_{1}\\beta \_{1}\'+w\_{2}\\beta \_{2}\'+\\dots
+w\_{q}\\beta \_{q}\',} and its minimum-variance unbiased linear
estimator is ξ \^ ′ ( w ) = w 1 β \^ 1 ′ + w 2 β \^ 2 ′ + ⋯ + w q β \^ q
′ , {\\displaystyle {\\hat {\\xi }}\'(\\mathbf {w} )=w\_{1}{\\hat
{\\beta }}\_{1}\'+w\_{2}{\\hat {\\beta }}\_{2}\'+\\dots +w\_{q}{\\hat
{\\beta }}\_{q}\',} where β \^ j ′ {\\displaystyle {\\hat {\\beta
}}\_{j}\'} is the least squares estimator of β j ′ {\\displaystyle
\\beta \_{j}\'} . In particular, the average group effect of the q
{\\displaystyle q} standardized variables is ξ A = 1 q ( β 1 ′ + β 2 ′ +
⋯ + β q ′ ) , {\\displaystyle \\xi \_{A}={\\frac {1}{q}}(\\beta
\_{1}\'+\\beta \_{2}\'+\\dots +\\beta \_{q}\'),} which has an
interpretation as the expected change in y ′ {\\displaystyle y\'} when
all x j ′ {\\displaystyle x\_{j}\'} in the strongly correlated group
increase by ( 1 / q ) {\\displaystyle (1/q)} th of a unit at the same
time with variables outside the group held constant. With strong
positive correlations and in standardized units, variables in the group
are approximately equal, so they are likely to increase at the same time
and in similar amount. Thus, the average group effect ξ A
{\\displaystyle \\xi \_{A}} is a meaningful effect. It can be accurately
estimated by its minimum-variance unbiased linear estimator ξ \^ A = 1 q
( β \^ 1 ′ + β \^ 2 ′ + ⋯ + β \^ q ′ ) {\\textstyle {\\hat {\\xi
}}\_{A}={\\frac {1}{q}}({\\hat {\\beta }}\_{1}\'+{\\hat {\\beta
}}\_{2}\'+\\dots +{\\hat {\\beta }}\_{q}\')} , even when individually
none of the β j ′ {\\displaystyle \\beta \_{j}\'} can be accurately
estimated by β \^ j ′ {\\displaystyle {\\hat {\\beta }}\_{j}\'} . Not
all group effects are meaningful or can be accurately estimated. For
example, β 1 ′ {\\displaystyle \\beta \_{1}\'} is a special group effect
with weights w 1 = 1 {\\displaystyle w\_{1}=1} and w j = 0
{\\displaystyle w\_{j}=0} for j ≠ 1 {\\displaystyle j\\neq 1} , but it
cannot be accurately estimated by β \^ 1 ′ {\\displaystyle {\\hat
{\\beta }}\'\_{1}} . It is also not a meaningful effect. In general, for
a group of q {\\displaystyle q} strongly correlated predictor variables
in an APC arrangement in the standardized model, group effects whose
weight vectors w {\\displaystyle \\mathbf {w} } are at or near the
centre of the simplex ∑ j = 1 q w j = 1 {\\textstyle \\sum
\_{j=1}\^{q}w\_{j}=1} ( w j ≥ 0 {\\displaystyle w\_{j}\\geq 0} ) are
meaningful and can be accurately estimated by their minimum-variance
unbiased linear estimators. Effects with weight vectors far away from
the centre are not meaningful as such weight vectors represent
simultaneous changes of the variables that violate the strong positive
correlations of the standardized variables in an APC arrangement. As
such, they are not probable. These effects also cannot be accurately
estimated. Applications of the group effects include (1) estimation and
inference for meaningful group effects on the response variable, (2)
testing for \"group significance\" of the q {\\displaystyle q} variables
via testing H 0 : ξ A = 0 {\\displaystyle H\_{0}:\\xi \_{A}=0} versus H
1 : ξ A ≠ 0 {\\displaystyle H\_{1}:\\xi \_{A}\\neq 0} , and (3)
characterizing the region of the predictor variable space over which
predictions by the least squares estimated model are accurate. A group
effect of the original variables { x 1 , x 2 , ... , x q }
{\\displaystyle \\{x\_{1},x\_{2},\\dots ,x\_{q}\\}} can be expressed as
a constant times a group effect of the standardized variables { x 1 ′ ,
x 2 ′ , ... , x q ′ } {\\displaystyle \\{x\_{1}\',x\_{2}\',\\dots
,x\_{q}\'\\}} . The former is meaningful when the latter is. Thus
meaningful group effects of the original variables can be found through
meaningful group effects of the standardized variables. Extensions
Numerous extensions of linear regression have been developed, which
allow some or all of the assumptions underlying the basic model to be
relaxed. Simple and multiple linear regression The very simplest case of
a single scalar predictor variable x and a single scalar response
variable y is known as simple linear regression. The extension to
multiple and/or vector-valued predictor variables (denoted with a
capital X) is known as multiple linear regression, also known as
multivariable linear regression (not to be confused with multivariate
linear regression). Multiple linear regression is a generalization of
simple linear regression to the case of more than one independent
variable, and a special case of general linear models, restricted to one
dependent variable. The basic model for multiple linear regression is Y
i = β 0 + β 1 X i 1 + β 2 X i 2 + ... + β p X i p + ϵ i {\\displaystyle
Y\_{i}=\\beta \_{0}+\\beta \_{1}X\_{i1}+\\beta \_{2}X\_{i2}+\\ldots
+\\beta \_{p}X\_{ip}+\\epsilon \_{i}} for each observation i = 1, \... ,
n. In the formula above we consider n observations of one dependent
variable and p independent variables. Thus, Yi is the ith observation of
the dependent variable, Xij is ith observation of the jth independent
variable, j = 1, 2, \..., p. The values βj represent parameters to be
estimated, and εi is the ith independent identically distributed normal
error. In the more general multivariate linear regression, there is one
equation of the above form for each of m \> 1 dependent variables that
share the same set of explanatory variables and hence are estimated
simultaneously with each other: Y i j = β 0 j + β 1 j X i 1 + β 2 j X i
2 + ... + β p j X i p + ϵ i j {\\displaystyle Y\_{ij}=\\beta
\_{0j}+\\beta \_{1j}X\_{i1}+\\beta \_{2j}X\_{i2}+\\ldots +\\beta
\_{pj}X\_{ip}+\\epsilon \_{ij}} for all observations indexed as i = 1,
\... , n and for all dependent variables indexed as j = 1, \... , m.
Nearly all real-world regression models involve multiple predictors, and
basic descriptions of linear regression are often phrased in terms of
the multiple regression model. Note, however, that in these cases the
response variable y is still a scalar. Another term, multivariate linear
regression, refers to cases where y is a vector, i.e., the same as
general linear regression. General linear models The general linear
model considers the situation when the response variable is not a scalar
(for each observation) but a vector, yi. Conditional linearity of E ( y
∣ x i ) = x i T B {\\displaystyle E(\\mathbf {y} \\mid \\mathbf {x}
\_{i})=\\mathbf {x} \_{i}\^{\\mathsf {T}}B} is still assumed, with a
matrix B replacing the vector β of the classical linear regression
model. Multivariate analogues of ordinary least squares (OLS) and
generalized least squares (GLS) have been developed. \"General linear
models\" are also called \"multivariate linear models\". These are not
the same as multivariable linear models (also called \"multiple linear
models\"). Heteroscedastic models Various models have been created that
allow for heteroscedasticity, i.e. the errors for different response
variables may have different variances. For example, weighted least
squares is a method for estimating linear regression models when the
response variables may have different error variances, possibly with
correlated errors. (See also Weighted linear least squares, and
Generalized least squares.) Heteroscedasticity-consistent standard
errors is an improved method for use with uncorrelated but potentially
heteroscedastic errors. Generalized linear models Generalized linear
models (GLMs) are a framework for modeling response variables that are
bounded or discrete. This is used, for example: when modeling positive
quantities (e.g. prices or populations) that vary over a large
scale---which are better described using a skewed distribution such as
the log-normal distribution or Poisson distribution (although GLMs are
not used for log-normal data, instead the response variable is simply
transformed using the logarithm function); when modeling categorical
data, such as the choice of a given candidate in an election (which is
better described using a Bernoulli distribution/binomial distribution
for binary choices, or a categorical distribution/multinomial
distribution for multi-way choices), where there are a fixed number of
choices that cannot be meaningfully ordered; when modeling ordinal data,
e.g. ratings on a scale from 0 to 5, where the different outcomes can be
ordered but where the quantity itself may not have any absolute meaning
(e.g. a rating of 4 may not be \"twice as good\" in any objective sense
as a rating of 2, but simply indicates that it is better than 2 or 3 but
not as good as 5).Generalized linear models allow for an arbitrary link
function, g, that relates the mean of the response variable(s) to the
predictors: E ( Y ) = g − 1 ( X B ) {\\displaystyle E(Y)=g\^{-1}(XB)} .
The link function is often related to the distribution of the response,
and in particular it typically has the effect of transforming between
the ( − ∞ , ∞ ) {\\displaystyle (-\\infty ,\\infty )} range of the
linear predictor and the range of the response variable. Some common
examples of GLMs are: Poisson regression for count data. Logistic
regression and probit regression for binary data. Multinomial logistic
regression and multinomial probit regression for categorical data.
Ordered logit and ordered probit regression for ordinal data.Single
index models allow some degree of nonlinearity in the relationship
between x and y, while preserving the central role of the linear
predictor β′x as in the classical linear regression model. Under certain
conditions, simply applying OLS to data from a single-index model will
consistently estimate β up to a proportionality constant. Hierarchical
linear models Hierarchical linear models (or multilevel regression)
organizes the data into a hierarchy of regressions, for example where A
is regressed on B, and B is regressed on C. It is often used where the
variables of interest have a natural hierarchical structure such as in
educational statistics, where students are nested in classrooms,
classrooms are nested in schools, and schools are nested in some
administrative grouping, such as a school district. The response
variable might be a measure of student achievement such as a test score,
and different covariates would be collected at the classroom, school,
and school district levels. Errors-in-variables Errors-in-variables
models (or \"measurement error models\") extend the traditional linear
regression model to allow the predictor variables X to be observed with
error. This error causes standard estimators of β to become biased.
Generally, the form of bias is an attenuation, meaning that the effects
are biased toward zero. Others In Dempster--Shafer theory, or a linear
belief function in particular, a linear regression model may be
represented as a partially swept matrix, which can be combined with
similar matrices representing observations and other assumed normal
distributions and state equations. The combination of swept or unswept
matrices provides an alternative method for estimating linear regression
models. Estimation methods A large number of procedures have been
developed for parameter estimation and inference in linear regression.
These methods differ in computational simplicity of algorithms, presence
of a closed-form solution, robustness with respect to heavy-tailed
distributions, and theoretical assumptions needed to validate desirable
statistical properties such as consistency and asymptotic efficiency.
Some of the more common estimation techniques for linear regression are
summarized below. Least-squares estimation and related techniques
Assuming that the independent variable is x i → = \[ x 1 i , x 2 i , ...
, x m i \] {\\displaystyle {\\vec
{x\_{i}}}=\\left\[x\_{1}\^{i},x\_{2}\^{i},\\ldots ,x\_{m}\^{i}\\right\]}
and the model\'s parameters are β → = \[ β 0 , β 1 , ... , β m \]
{\\displaystyle {\\vec {\\beta }}=\\left\[\\beta \_{0},\\beta
\_{1},\\ldots ,\\beta \_{m}\\right\]} , then the model\'s prediction
would be y i ≈ β 0 + ∑ j = 1 m β j × x j i {\\displaystyle
y\_{i}\\approx \\beta \_{0}+\\sum \_{j=1}\^{m}\\beta \_{j}\\times
x\_{j}\^{i}} .If x i → {\\displaystyle {\\vec {x\_{i}}}} is extended to
x i → = \[ 1 , x 1 i , x 2 i , ... , x m i \] {\\displaystyle {\\vec
{x\_{i}}}=\\left\[1,x\_{1}\^{i},x\_{2}\^{i},\\ldots
,x\_{m}\^{i}\\right\]} then y i {\\displaystyle y\_{i}} would become a
dot product of the parameter and the independent variable, i.e. y i ≈ ∑
j = 0 m β j × x j i = β → ⋅ x i → {\\displaystyle y\_{i}\\approx \\sum
\_{j=0}\^{m}\\beta \_{j}\\times x\_{j}\^{i}={\\vec {\\beta }}\\cdot
{\\vec {x\_{i}}}} .In the least-squares setting, the optimum parameter
is defined as such that minimizes the sum of mean squared loss: β \^ → =
arg min β → L ( D , β → ) = arg min β → ∑ i = 1 n ( β → ⋅ x i → − y i )
2 {\\displaystyle {\\vec {\\hat {\\beta }}}={\\underset {\\vec {\\beta
}}{\\mbox{arg min}}}\\,L\\left(D,{\\vec {\\beta }}\\right)={\\underset
{\\vec {\\beta }}{\\mbox{arg min}}}\\sum \_{i=1}\^{n}\\left({\\vec
{\\beta }}\\cdot {\\vec {x\_{i}}}-y\_{i}\\right)\^{2}} Now putting the
independent and dependent variables in matrices X {\\displaystyle X} and
Y {\\displaystyle Y} respectively, the loss function can be rewritten
as: L ( D , β → ) = ‖ X β → − Y ‖ 2 = ( X β → − Y ) T ( X β → − Y ) = Y
T Y − Y T X β → − β → T X T Y + β → T X T X β → {\\displaystyle
{\\begin{aligned}L\\left(D,{\\vec {\\beta }}\\right)&=\\\|X{\\vec
{\\beta }}-Y\\\|\^{2}\\\\&=\\left(X{\\vec {\\beta
}}-Y\\right)\^{\\textsf {T}}\\left(X{\\vec {\\beta
}}-Y\\right)\\\\&=Y\^{\\textsf {T}}Y-Y\^{\\textsf {T}}X{\\vec {\\beta
}}-{\\vec {\\beta }}\^{\\textsf {T}}X\^{\\textsf {T}}Y+{\\vec {\\beta
}}\^{\\textsf {T}}X\^{\\textsf {T}}X{\\vec {\\beta }}\\end{aligned}}} As
the loss is convex the optimum solution lies at gradient zero. The
gradient of the loss function is (using Denominator layout convention):
∂ L ( D , β → ) ∂ β → = ∂ ( Y T Y − Y T X β → − β → T X T Y + β → T X T
X β → ) ∂ β → = − 2 X T Y + 2 X T X β → {\\displaystyle
{\\begin{aligned}{\\frac {\\partial L\\left(D,{\\vec {\\beta
}}\\right)}{\\partial {\\vec {\\beta }}}}&={\\frac {\\partial
\\left(Y\^{\\textsf {T}}Y-Y\^{\\textsf {T}}X{\\vec {\\beta }}-{\\vec
{\\beta }}\^{\\textsf {T}}X\^{\\textsf {T}}Y+{\\vec {\\beta
}}\^{\\textsf {T}}X\^{\\textsf {T}}X{\\vec {\\beta }}\\right)}{\\partial
{\\vec {\\beta }}}}\\\\&=-2X\^{\\textsf {T}}Y+2X\^{\\textsf {T}}X{\\vec
{\\beta }}\\end{aligned}}} Setting the gradient to zero produces the
optimum parameter: − 2 X T Y + 2 X T X β → = 0 ⇒ X T X β → = X T Y ⇒ β
\^ → = ( X T X ) − 1 X T Y {\\displaystyle
{\\begin{aligned}-2X\^{\\textsf {T}}Y+2X\^{\\textsf {T}}X{\\vec {\\beta
}}&=0\\\\\\Rightarrow X\^{\\textsf {T}}X{\\vec {\\beta }}&=X\^{\\textsf
{T}}Y\\\\\\Rightarrow {\\vec {\\hat {\\beta }}}&=\\left(X\^{\\textsf
{T}}X\\right)\^{-1}X\^{\\textsf {T}}Y\\end{aligned}}} Note: To prove
that the β \^ {\\displaystyle {\\hat {\\beta }}} obtained is indeed the
local minimum, one needs to differentiate once more to obtain the
Hessian matrix and show that it is positive definite. This is provided
by the Gauss--Markov theorem. Linear least squares methods include
mainly: Ordinary least squares Weighted least squares Generalized least
squares Maximum-likelihood estimation and related techniques Maximum
likelihood estimation can be performed when the distribution of the
error terms is known to belong to a certain parametric family ƒθ of
probability distributions. When fθ is a normal distribution with zero
mean and variance θ, the resulting estimate is identical to the OLS
estimate. GLS estimates are maximum likelihood estimates when ε follows
a multivariate normal distribution with a known covariance matrix. Ridge
regression and other forms of penalized estimation, such as Lasso
regression, deliberately introduce bias into the estimation of β in
order to reduce the variability of the estimate. The resulting estimates
generally have lower mean squared error than the OLS estimates,
particularly when multicollinearity is present or when overfitting is a
problem. They are generally used when the goal is to predict the value
of the response variable y for values of the predictors x that have not
yet been observed. These methods are not as commonly used when the goal
is inference, since it is difficult to account for the bias. Least
absolute deviation (LAD) regression is a robust estimation technique in
that it is less sensitive to the presence of outliers than OLS (but is
less efficient than OLS when no outliers are present). It is equivalent
to maximum likelihood estimation under a Laplace distribution model for
ε. Adaptive estimation. If we assume that error terms are independent of
the regressors, ε i ⊥ x i {\\displaystyle \\varepsilon \_{i}\\perp
\\mathbf {x} \_{i}} , then the optimal estimator is the 2-step MLE,
where the first step is used to non-parametrically estimate the
distribution of the error term. Other estimation techniques Bayesian
linear regression applies the framework of Bayesian statistics to linear
regression. (See also Bayesian multivariate linear regression.) In
particular, the regression coefficients β are assumed to be random
variables with a specified prior distribution. The prior distribution
can bias the solutions for the regression coefficients, in a way similar
to (but more general than) ridge regression or lasso regression. In
addition, the Bayesian estimation process produces not a single point
estimate for the \"best\" values of the regression coefficients but an
entire posterior distribution, completely describing the uncertainty
surrounding the quantity. This can be used to estimate the \"best\"
coefficients using the mean, mode, median, any quantile (see quantile
regression), or any other function of the posterior distribution.
Quantile regression focuses on the conditional quantiles of y given X
rather than the conditional mean of y given X. Linear quantile
regression models a particular conditional quantile, for example the
conditional median, as a linear function βTx of the predictors. Mixed
models are widely used to analyze linear regression relationships
involving dependent data when the dependencies have a known structure.
Common applications of mixed models include analysis of data involving
repeated measurements, such as longitudinal data, or data obtained from
cluster sampling. They are generally fit as parametric models, using
maximum likelihood or Bayesian estimation. In the case where the errors
are modeled as normal random variables, there is a close connection
between mixed models and generalized least squares. Fixed effects
estimation is an alternative approach to analyzing this type of data.
Principal component regression (PCR) is used when the number of
predictor variables is large, or when strong correlations exist among
the predictor variables. This two-stage procedure first reduces the
predictor variables using principal component analysis, and then uses
the reduced variables in an OLS regression fit. While it often works
well in practice, there is no general theoretical reason that the most
informative linear function of the predictor variables should lie among
the dominant principal components of the multivariate distribution of
the predictor variables. The partial least squares regression is the
extension of the PCR method which does not suffer from the mentioned
deficiency. Least-angle regression is an estimation procedure for linear
regression models that was developed to handle high-dimensional
covariate vectors, potentially with more covariates than observations.
The Theil--Sen estimator is a simple robust estimation technique that
chooses the slope of the fit line to be the median of the slopes of the
lines through pairs of sample points. It has similar statistical
efficiency properties to simple linear regression but is much less
sensitive to outliers. Other robust estimation techniques, including the
α-trimmed mean approach, and L-, M-, S-, and R-estimators have been
introduced. Applications Linear regression is widely used in biological,
behavioral and social sciences to describe possible relationships
between variables. It ranks as one of the most important tools used in
these disciplines. Trend line A trend line represents a trend, the
long-term movement in time series data after other components have been
accounted for. It tells whether a particular data set (say GDP, oil
prices or stock prices) have increased or decreased over the period of
time. A trend line could simply be drawn by eye through a set of data
points, but more properly their position and slope is calculated using
statistical techniques like linear regression. Trend lines typically are
straight lines, although some variations use higher degree polynomials
depending on the degree of curvature desired in the line. Trend lines
are sometimes used in business analytics to show changes in data over
time. This has the advantage of being simple. Trend lines are often used
to argue that a particular action or event (such as training, or an
advertising campaign) caused observed changes at a point in time. This
is a simple technique, and does not require a control group,
experimental design, or a sophisticated analysis technique. However, it
suffers from a lack of scientific validity in cases where other
potential changes can affect the data. Epidemiology Early evidence
relating tobacco smoking to mortality and morbidity came from
observational studies employing regression analysis. In order to reduce
spurious correlations when analyzing observational data, researchers
usually include several variables in their regression models in addition
to the variable of primary interest. For example, in a regression model
in which cigarette smoking is the independent variable of primary
interest and the dependent variable is lifespan measured in years,
researchers might include education and income as additional independent
variables, to ensure that any observed effect of smoking on lifespan is
not due to those other socio-economic factors. However, it is never
possible to include all possible confounding variables in an empirical
analysis. For example, a hypothetical gene might increase mortality and
also cause people to smoke more. For this reason, randomized controlled
trials are often able to generate more compelling evidence of causal
relationships than can be obtained using regression analyses of
observational data. When controlled experiments are not feasible,
variants of regression analysis such as instrumental variables
regression may be used to attempt to estimate causal relationships from
observational data. Finance The capital asset pricing model uses linear
regression as well as the concept of beta for analyzing and quantifying
the systematic risk of an investment. This comes directly from the beta
coefficient of the linear regression model that relates the return on
the investment to the return on all risky assets. Economics Linear
regression is the predominant empirical tool in economics. For example,
it is used to predict consumption spending, fixed investment spending,
inventory investment, purchases of a country\'s exports, spending on
imports, the demand to hold liquid assets, labor demand, and labor
supply. Environmental science Linear regression finds application in a
wide range of environmental science applications. In Canada, the
Environmental Effects Monitoring Program uses statistical analyses on
fish and benthic surveys to measure the effects of pulp mill or metal
mine effluent on the aquatic ecosystem. Machine learning Linear
regression plays an important role in the subfield of artificial
intelligence known as machine learning. The linear regression algorithm
is one of the fundamental supervised machine-learning algorithms due to
its relative simplicity and well-known properties. History Least squares
linear regression, as a means of finding a good rough linear fit to a
set of points was performed by Legendre (1805) and Gauss (1809) for the
prediction of planetary movement. Quetelet was responsible for making
the procedure well-known and for using it extensively in the social
sciences. See also References Citations Sources Further reading
Pedhazur, Elazar J (1982). Multiple regression in behavioral research:
Explanation and prediction (2nd ed.). New York: Holt, Rinehart and
Winston. ISBN 978-0-03-041760-3. Mathieu Rouaud, 2013: Probability,
Statistics and Estimation Chapter 2: Linear Regression, Linear
Regression with Error Bars and Nonlinear Regression. National Physical
Laboratory (1961). \"Chapter 1: Linear Equations and Matrices: Direct
Methods\". Modern Computing Methods. Notes on Applied Science. Vol. 16
(2nd ed.). Her Majesty\'s Stationery Office. External links
Least-Squares Regression, PhET Interactive simulations, University of
Colorado at Boulder DIY Linear Fit
