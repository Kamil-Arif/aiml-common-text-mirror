In statistics, the logistic model (or logit model) is a statistical
model that models the probability of an event taking place by having the
log-odds for the event be a linear combination of one or more
independent variables. In regression analysis, logistic regression (or
logit regression) is estimating the parameters of a logistic model (the
coefficients in the linear combination). Formally, in binary logistic
regression there is a single binary dependent variable, coded by an
indicator variable, where the two values are labeled \"0\" and \"1\",
while the independent variables can each be a binary variable (two
classes, coded by an indicator variable) or a continuous variable (any
real value). The corresponding probability of the value labeled \"1\"
can vary between 0 (certainly the value \"0\") and 1 (certainly the
value \"1\"), hence the labeling; the function that converts log-odds to
probability is the logistic function, hence the name. The unit of
measurement for the log-odds scale is called a logit, from logistic
unit, hence the alternative names. See § Background and § Definition for
formal mathematics, and § Example for a worked example. Binary variables
are widely used in statistics to model the probability of a certain
class or event taking place, such as the probability of a team winning,
of a patient being healthy, etc. (see § Applications), and the logistic
model has been the most commonly used model for binary regression since
about 1970. Binary variables can be generalized to categorical variables
when there are more than two possible values (e.g. whether an image is
of a cat, dog, lion, etc.), and the binary logistic regression
generalized to multinomial logistic regression. If the multiple
categories are ordered, one can use the ordinal logistic regression (for
example the proportional odds ordinal logistic model). See § Extensions
for further extensions. The logistic regression model itself simply
models probability of output in terms of input and does not perform
statistical classification (it is not a classifier), though it can be
used to make a classifier, for instance by choosing a cutoff value and
classifying inputs with probability greater than the cutoff as one
class, below the cutoff as the other; this is a common way to make a
binary classifier. Analogous linear models for binary variables with a
different sigmoid function instead of the logistic function (to convert
the linear combination to a probability) can also be used, most notably
the probit model; see § Alternatives. The defining characteristic of the
logistic model is that increasing one of the independent variables
multiplicatively scales the odds of the given outcome at a constant
rate, with each independent variable having its own parameter; for a
binary dependent variable this generalizes the odds ratio. More
abstractly, the logistic function is the natural parameter for the
Bernoulli distribution, and in this sense is the \"simplest\" way to
convert a real number to a probability. In particular, it maximizes
entropy (minimizes added information), and in this sense makes the
fewest assumptions of the data being modeled; see § Maximum entropy. The
parameters of a logistic regression are most commonly estimated by
maximum-likelihood estimation (MLE). This does not have a closed-form
expression, unlike linear least squares; see § Model fitting. Logistic
regression by MLE plays a similarly basic role for binary or categorical
responses as linear regression by ordinary least squares (OLS) plays for
scalar responses: it is a simple, well-analyzed baseline model; see §
Comparison with linear regression for discussion. The logistic
regression as a general statistical model was originally developed and
popularized primarily by Joseph Berkson, beginning in Berkson (1944),
where he coined \"logit\"; see § History. Applications Logistic
regression is used in various fields, including machine learning, most
medical fields, and social sciences. For example, the Trauma and Injury
Severity Score (TRISS), which is widely used to predict mortality in
injured patients, was originally developed by Boyd et al. using logistic
regression. Many other medical scales used to assess severity of a
patient have been developed using logistic regression. Logistic
regression may be used to predict the risk of developing a given disease
(e.g. diabetes; coronary heart disease), based on observed
characteristics of the patient (age, sex, body mass index, results of
various blood tests, etc.). Another example might be to predict whether
a Nepalese voter will vote Nepali Congress or Communist Party of Nepal
or Any Other Party, based on age, income, sex, race, state of residence,
votes in previous elections, etc. The technique can also be used in
engineering, especially for predicting the probability of failure of a
given process, system or product. It is also used in marketing
applications such as prediction of a customer\'s propensity to purchase
a product or halt a subscription, etc. In economics, it can be used to
predict the likelihood of a person ending up in the labor force, and a
business application would be to predict the likelihood of a homeowner
defaulting on a mortgage. Conditional random fields, an extension of
logistic regression to sequential data, are used in natural language
processing. Example Problem As a simple example, we can use a logistic
regression with one explanatory variable and two categories to answer
the following question: A group of 20 students spends between 0 and 6
hours studying for an exam. How does the number of hours spent studying
affect the probability of the student passing the exam? The reason for
using logistic regression for this problem is that the values of the
dependent variable, pass and fail, while represented by \"1\" and \"0\",
are not cardinal numbers. If the problem was changed so that pass/fail
was replaced with the grade 0--100 (cardinal numbers), then simple
regression analysis could be used. The table shows the number of hours
each student spent studying, and whether they passed (1) or failed (0).
We wish to fit a logistic function to the data consisting of the hours
studied (xk) and the outcome of the test (yk =1 for pass, 0 for fail).
The data points are indexed by the subscript k which runs from k = 1
{\\displaystyle k=1} to k = K = 20 {\\displaystyle k=K=20} . The x
variable is called the \"explanatory variable\", and the y variable is
called the \"categorical variable\" consisting of two categories:
\"pass\" or \"fail\" corresponding to the categorical values 1 and 0
respectively. Model The logistic function is of the form: p ( x ) = 1
1 + e − ( x − μ ) / s {\\displaystyle p(x)={\\frac {1}{1+e\^{-(x-\\mu
)/s}}}} where μ is a location parameter (the midpoint of the curve,
where p ( μ ) = 1 / 2 {\\displaystyle p(\\mu )=1/2} ) and s is a scale
parameter. This expression may be rewritten as: p ( x ) = 1 1 + e − ( β
0 + β 1 x ) {\\displaystyle p(x)={\\frac {1}{1+e\^{-(\\beta \_{0}+\\beta
\_{1}x)}}}} where β 0 = − μ / s {\\displaystyle \\beta \_{0}=-\\mu /s}
and is known as the intercept (it is the vertical intercept or
y-intercept of the line y = β 0 + β 1 x {\\displaystyle y=\\beta
\_{0}+\\beta \_{1}x} ), and β 1 = 1 / s {\\displaystyle \\beta
\_{1}=1/s} (inverse scale parameter or rate parameter): these are the
y-intercept and slope of the log-odds as a function of x. Conversely, μ
= − β 0 / β 1 {\\displaystyle \\mu =-\\beta \_{0}/\\beta \_{1}} and s =
1 / β 1 {\\displaystyle s=1/\\beta \_{1}} . Fit The usual measure of
goodness of fit for a logistic regression uses logistic loss (or log
loss), the negative log-likelihood. For a given xk and yk, write p k = p
( x k ) {\\displaystyle p\_{k}=p(x\_{k})} . The p k {\\displaystyle
p\_{k}} are the probabilities that the corresponding y k {\\displaystyle
y\_{k}} will be unity and 1 − p k {\\displaystyle 1-p\_{k}} are the
probabilities that they will be zero (see Bernoulli distribution). We
wish to find the values of β 0 {\\displaystyle \\beta \_{0}} and β 1
{\\displaystyle \\beta \_{1}} which give the \"best fit\" to the data.
In the case of linear regression, the sum of the squared deviations of
the fit from the data points (yk), the squared error loss, is taken as a
measure of the goodness of fit, and the best fit is obtained when that
function is minimized. The log loss for the k-th point is: { − ln ⁡ p k
if y k = 1 , − ln ⁡ ( 1 − p k ) if y k = 0. {\\displaystyle
{\\begin{cases}-\\ln p\_{k}&{\\text{ if
}}y\_{k}=1,\\\\-\\ln(1-p\_{k})&{\\text{ if }}y\_{k}=0.\\end{cases}}} The
log loss can be interpreted as the \"surprisal\" of the actual outcome y
k {\\displaystyle y\_{k}} relative to the prediction p k {\\displaystyle
p\_{k}} , and is a measure of information content. Note that log loss is
always greater than or equal to 0, equals 0 only in case of a perfect
prediction (i.e., when p k = 1 {\\displaystyle p\_{k}=1} and y k = 1
{\\displaystyle y\_{k}=1} , or p k = 0 {\\displaystyle p\_{k}=0} and y k
= 0 {\\displaystyle y\_{k}=0} ), and approaches infinity as the
prediction gets worse (i.e., when y k = 1 {\\displaystyle y\_{k}=1} and
p k → 0 {\\displaystyle p\_{k}\\to 0} or y k = 0 {\\displaystyle
y\_{k}=0} and p k → 1 {\\displaystyle p\_{k}\\to 1} ), meaning the
actual outcome is \"more surprising\". Since the value of the logistic
function is always strictly between zero and one, the log loss is always
greater than zero and less than infinity. Note that unlike in a linear
regression, where the model can have zero loss at a point by passing
through a data point (and zero loss overall if all points are on a
line), in a logistic regression it is not possible to have zero loss at
any points, since y k {\\displaystyle y\_{k}} is either 0 or 1, but 0 \<
p k \< 1 {\\displaystyle 0 0 i.e. − ε i \< β ⋅ X i , 0 otherwise.
{\\displaystyle Y\_{i}={\\begin{cases}1&{\\text{if }}Y\_{i}\^{\\ast
}\>0\\ {\\text{ i.e. }}-\\varepsilon \_{i}\<{\\boldsymbol {\\beta
}}\\cdot \\mathbf {X} \_{i},\\\\0&{\\text{otherwise.}}\\end{cases}}} The
choice of modeling the error variable specifically with a standard
logistic distribution, rather than a general logistic distribution with
the location and scale set to arbitrary values, seems restrictive, but
in fact, it is not. It must be kept in mind that we can choose the
regression coefficients ourselves, and very often can use them to offset
changes in the parameters of the error variable\'s distribution. For
example, a logistic error-variable distribution with a non-zero location
parameter μ (which sets the mean) is equivalent to a distribution with a
zero location parameter, where μ has been added to the intercept
coefficient. Both situations produce the same value for Yi\* regardless
of settings of explanatory variables. Similarly, an arbitrary scale
parameter s is equivalent to setting the scale parameter to 1 and then
dividing all regression coefficients by s. In the latter case, the
resulting value of Yi\* will be smaller by a factor of s than in the
former case, for all sets of explanatory variables --- but critically,
it will always remain on the same side of 0, and hence lead to the same
Yi choice. (Note that this predicts that the irrelevancy of the scale
parameter may not carry over into more complex models where more than
two choices are available.) It turns out that this formulation is
exactly equivalent to the preceding one, phrased in terms of the
generalized linear model and without any latent variables. This can be
shown as follows, using the fact that the cumulative distribution
function (CDF) of the standard logistic distribution is the logistic
function, which is the inverse of the logit function, i.e. Pr ( ε i \< x
) = logit − 1 ⁡ ( x ) {\\displaystyle \\Pr(\\varepsilon \_{i} 0 ∣ X i ) =
Pr ( β ⋅ X i + ε i \> 0 ) = Pr ( ε i \> − β ⋅ X i ) = Pr ( ε i \< β ⋅ X
i ) (because the logistic distribution is symmetric) = logit − 1 ⁡ ( β ⋅
X i ) = p i (see above) {\\displaystyle
{\\begin{aligned}\\Pr(Y\_{i}=1\\mid \\mathbf {X}
\_{i})&=\\Pr(Y\_{i}\^{\\ast }\>0\\mid \\mathbf {X}
\_{i})\\\\\[5pt\]&=\\Pr({\\boldsymbol {\\beta }}\\cdot \\mathbf {X}
\_{i}+\\varepsilon \_{i}\>0)\\\\\[5pt\]&=\\Pr(\\varepsilon
\_{i}\>-{\\boldsymbol {\\beta }}\\cdot \\mathbf {X}
\_{i})\\\\\[5pt\]&=\\Pr(\\varepsilon \_{i}\<{\\boldsymbol {\\beta
}}\\cdot \\mathbf {X} \_{i})&&{\\text{(because the logistic distribution
is symmetric)}}\\\\\[5pt\]&=\\operatorname {logit} \^{-1}({\\boldsymbol
{\\beta }}\\cdot \\mathbf {X} \_{i})&\\\\\[5pt\]&=p\_{i}&&{\\text{(see
above)}}\\end{aligned}}} This formulation---which is standard in
discrete choice models---makes clear the relationship between logistic
regression (the \"logit model\") and the probit model, which uses an
error variable distributed according to a standard normal distribution
instead of a standard logistic distribution. Both the logistic and
normal distributions are symmetric with a basic unimodal, \"bell curve\"
shape. The only difference is that the logistic distribution has
somewhat heavier tails, which means that it is less sensitive to
outlying data (and hence somewhat more robust to model
mis-specifications or erroneous data). Two-way latent-variable model Yet
another formulation uses two separate latent variables: Y i 0 ∗ = β 0 ⋅
X i + ε 0 Y i 1 ∗ = β 1 ⋅ X i + ε 1 {\\displaystyle
{\\begin{aligned}Y\_{i}\^{0\\ast }&={\\boldsymbol {\\beta }}\_{0}\\cdot
\\mathbf {X} \_{i}+\\varepsilon \_{0}\\,\\\\Y\_{i}\^{1\\ast
}&={\\boldsymbol {\\beta }}\_{1}\\cdot \\mathbf {X} \_{i}+\\varepsilon
\_{1}\\,\\end{aligned}}} where ε 0 ∼ EV 1 ⁡ ( 0 , 1 ) ε 1 ∼ EV 1 ⁡ ( 0 , 1
) {\\displaystyle {\\begin{aligned}\\varepsilon \_{0}&\\sim
\\operatorname {EV} \_{1}(0,1)\\\\\\varepsilon \_{1}&\\sim
\\operatorname {EV} \_{1}(0,1)\\end{aligned}}} where EV1(0,1) is a
standard type-1 extreme value distribution: i.e. Pr ( ε 0 = x ) = Pr ( ε
1 = x ) = e − x e − e − x {\\displaystyle \\Pr(\\varepsilon
\_{0}=x)=\\Pr(\\varepsilon \_{1}=x)=e\^{-x}e\^{-e\^{-x}}} Then Y i = { 1
if Y i 1 ∗ \> Y i 0 ∗ , 0 otherwise. {\\displaystyle
Y\_{i}={\\begin{cases}1&{\\text{if }}Y\_{i}\^{1\\ast }\>Y\_{i}\^{0\\ast
},\\\\0&{\\text{otherwise.}}\\end{cases}}} This model has a separate
latent variable and a separate set of regression coefficients for each
possible outcome of the dependent variable. The reason for this
separation is that it makes it easy to extend logistic regression to
multi-outcome categorical variables, as in the multinomial logit model.
In such a model, it is natural to model each possible outcome using a
different set of regression coefficients. It is also possible to
motivate each of the separate latent variables as the theoretical
utility associated with making the associated choice, and thus motivate
logistic regression in terms of utility theory. (In terms of utility
theory, a rational actor always chooses the choice with the greatest
associated utility.) This is the approach taken by economists when
formulating discrete choice models, because it both provides a
theoretically strong foundation and facilitates intuitions about the
model, which in turn makes it easy to consider various sorts of
extensions. (See the example below.) The choice of the type-1 extreme
value distribution seems fairly arbitrary, but it makes the mathematics
work out, and it may be possible to justify its use through rational
choice theory. It turns out that this model is equivalent to the
previous model, although this seems non-obvious, since there are now two
sets of regression coefficients and error variables, and the error
variables have a different distribution. In fact, this model reduces
directly to the previous one with the following substitutions: β = β 1 −
β 0 {\\displaystyle {\\boldsymbol {\\beta }}={\\boldsymbol {\\beta
}}\_{1}-{\\boldsymbol {\\beta }}\_{0}} ε = ε 1 − ε 0 {\\displaystyle
\\varepsilon =\\varepsilon \_{1}-\\varepsilon \_{0}} An intuition for
this comes from the fact that, since we choose based on the maximum of
two values, only their difference matters, not the exact values --- and
this effectively removes one degree of freedom. Another critical fact is
that the difference of two type-1 extreme-value-distributed variables is
a logistic distribution, i.e. ε = ε 1 − ε 0 ∼ Logistic ⁡ ( 0 , 1 ) .
{\\displaystyle \\varepsilon =\\varepsilon \_{1}-\\varepsilon \_{0}\\sim
\\operatorname {Logistic} (0,1).} We can demonstrate the equivalent as
follows: Pr ( Y i = 1 ∣ X i ) = Pr ( Y i 1 ∗ \> Y i 0 ∗ ∣ X i ) = Pr ( Y
i 1 ∗ − Y i 0 ∗ \> 0 ∣ X i ) = Pr ( β 1 ⋅ X i + ε 1 − ( β 0 ⋅ X i + ε 0
) \> 0 ) = Pr ( ( β 1 ⋅ X i − β 0 ⋅ X i ) + ( ε 1 − ε 0 ) \> 0 ) = Pr (
( β 1 − β 0 ) ⋅ X i + ( ε 1 − ε 0 ) \> 0 ) = Pr ( ( β 1 − β 0 ) ⋅ X i +
ε \> 0 ) (substitute ε as above) = Pr ( β ⋅ X i + ε \> 0 ) (substitute β
as above) = Pr ( ε \> − β ⋅ X i ) (now, same as above model) = Pr ( ε \<
β ⋅ X i ) = logit − 1 ⁡ ( β ⋅ X i ) = p i {\\displaystyle
{\\begin{aligned}\\Pr(Y\_{i}=1\\mid \\mathbf {X} \_{i})={}&\\Pr
\\left(Y\_{i}\^{1\\ast }\>Y\_{i}\^{0\\ast }\\mid \\mathbf {X}
\_{i}\\right)&\\\\\[5pt\]={}&\\Pr \\left(Y\_{i}\^{1\\ast
}-Y\_{i}\^{0\\ast }\>0\\mid \\mathbf {X}
\_{i}\\right)&\\\\\[5pt\]={}&\\Pr \\left({\\boldsymbol {\\beta
}}\_{1}\\cdot \\mathbf {X} \_{i}+\\varepsilon \_{1}-\\left({\\boldsymbol
{\\beta }}\_{0}\\cdot \\mathbf {X} \_{i}+\\varepsilon
\_{0}\\right)\>0\\right)&\\\\\[5pt\]={}&\\Pr \\left(({\\boldsymbol
{\\beta }}\_{1}\\cdot \\mathbf {X} \_{i}-{\\boldsymbol {\\beta
}}\_{0}\\cdot \\mathbf {X} \_{i})+(\\varepsilon \_{1}-\\varepsilon
\_{0})\>0\\right)&\\\\\[5pt\]={}&\\Pr(({\\boldsymbol {\\beta
}}\_{1}-{\\boldsymbol {\\beta }}\_{0})\\cdot \\mathbf {X}
\_{i}+(\\varepsilon \_{1}-\\varepsilon
\_{0})\>0)&\\\\\[5pt\]={}&\\Pr(({\\boldsymbol {\\beta
}}\_{1}-{\\boldsymbol {\\beta }}\_{0})\\cdot \\mathbf {X}
\_{i}+\\varepsilon \>0)&&{\\text{(substitute }}\\varepsilon {\\text{ as
above)}}\\\\\[5pt\]={}&\\Pr({\\boldsymbol {\\beta }}\\cdot \\mathbf {X}
\_{i}+\\varepsilon \>0)&&{\\text{(substitute }}{\\boldsymbol {\\beta
}}{\\text{ as above)}}\\\\\[5pt\]={}&\\Pr(\\varepsilon \>-{\\boldsymbol
{\\beta }}\\cdot \\mathbf {X} \_{i})&&{\\text{(now, same as above
model)}}\\\\\[5pt\]={}&\\Pr(\\varepsilon \<{\\boldsymbol {\\beta
}}\\cdot \\mathbf {X} \_{i})&\\\\\[5pt\]={}&\\operatorname {logit}
\^{-1}({\\boldsymbol {\\beta }}\\cdot \\mathbf {X}
\_{i})\\\\\[5pt\]={}&p\_{i}\\end{aligned}}} Example As an example,
consider a province-level election where the choice is between a
right-of-center party, a left-of-center party, and a secessionist party
(e.g. the Parti Québécois, which wants Quebec to secede from Canada). We
would then use three latent variables, one for each choice. Then, in
accordance with utility theory, we can then interpret the latent
variables as expressing the utility that results from making each of the
choices. We can also interpret the regression coefficients as indicating
the strength that the associated factor (i.e. explanatory variable) has
in contributing to the utility --- or more correctly, the amount by
which a unit change in an explanatory variable changes the utility of a
given choice. A voter might expect that the right-of-center party would
lower taxes, especially on rich people. This would give low-income
people no benefit, i.e. no change in utility (since they usually don\'t
pay taxes); would cause moderate benefit (i.e. somewhat more money, or
moderate utility increase) for middle-incoming people; would cause
significant benefits for high-income people. On the other hand, the
left-of-center party might be expected to raise taxes and offset it with
increased welfare and other assistance for the lower and middle classes.
This would cause significant positive benefit to low-income people,
perhaps a weak benefit to middle-income people, and significant negative
benefit to high-income people. Finally, the secessionist party would
take no direct actions on the economy, but simply secede. A low-income
or middle-income voter might expect basically no clear utility gain or
loss from this, but a high-income voter might expect negative utility
since he/she is likely to own companies, which will have a harder time
doing business in such an environment and probably lose money. These
intuitions can be expressed as follows: This clearly shows that Separate
sets of regression coefficients need to exist for each choice. When
phrased in terms of utility, this can be seen very easily. Different
choices have different effects on net utility; furthermore, the effects
vary in complex ways that depend on the characteristics of each
individual, so there need to be separate sets of coefficients for each
characteristic, not simply a single extra per-choice characteristic.
Even though income is a continuous variable, its effect on utility is
too complex for it to be treated as a single variable. Either it needs
to be directly split up into ranges, or higher powers of income need to
be added so that polynomial regression on income is effectively done. As
a \"log-linear\" model Yet another formulation combines the two-way
latent variable formulation above with the original formulation higher
up without latent variables, and in the process provides a link to one
of the standard formulations of the multinomial logit. Here, instead of
writing the logit of the probabilities pi as a linear predictor, we
separate the linear predictor into two, one for each of the two
outcomes: ln ⁡ Pr ( Y i = 0 ) = β 0 ⋅ X i − ln ⁡ Z ln ⁡ Pr ( Y i = 1 ) = β
1 ⋅ X i − ln ⁡ Z {\\displaystyle {\\begin{aligned}\\ln
\\Pr(Y\_{i}=0)&={\\boldsymbol {\\beta }}\_{0}\\cdot \\mathbf {X}
\_{i}-\\ln Z\\\\\\ln \\Pr(Y\_{i}=1)&={\\boldsymbol {\\beta }}\_{1}\\cdot
\\mathbf {X} \_{i}-\\ln Z\\end{aligned}}} Two separate sets of
regression coefficients have been introduced, just as in the two-way
latent variable model, and the two equations appear a form that writes
the logarithm of the associated probability as a linear predictor, with
an extra term − ln ⁡ Z {\\displaystyle -\\ln Z} at the end. This term, as
it turns out, serves as the normalizing factor ensuring that the result
is a distribution. This can be seen by exponentiating both sides: Pr ( Y
i = 0 ) = 1 Z e β 0 ⋅ X i Pr ( Y i = 1 ) = 1 Z e β 1 ⋅ X i
{\\displaystyle {\\begin{aligned}\\Pr(Y\_{i}=0)&={\\frac
{1}{Z}}e\^{{\\boldsymbol {\\beta }}\_{0}\\cdot \\mathbf {X}
\_{i}}\\\\\[5pt\]\\Pr(Y\_{i}=1)&={\\frac {1}{Z}}e\^{{\\boldsymbol
{\\beta }}\_{1}\\cdot \\mathbf {X} \_{i}}\\end{aligned}}} In this form
it is clear that the purpose of Z is to ensure that the resulting
distribution over Yi is in fact a probability distribution, i.e. it sums
to 1. This means that Z is simply the sum of all un-normalized
probabilities, and by dividing each probability by Z, the probabilities
become \"normalized\". That is: Z = e β 0 ⋅ X i + e β 1 ⋅ X i
{\\displaystyle Z=e\^{{\\boldsymbol {\\beta }}\_{0}\\cdot \\mathbf {X}
\_{i}}+e\^{{\\boldsymbol {\\beta }}\_{1}\\cdot \\mathbf {X} \_{i}}} and
the resulting equations are Pr ( Y i = 0 ) = e β 0 ⋅ X i e β 0 ⋅ X i + e
β 1 ⋅ X i Pr ( Y i = 1 ) = e β 1 ⋅ X i e β 0 ⋅ X i + e β 1 ⋅ X i .
{\\displaystyle {\\begin{aligned}\\Pr(Y\_{i}=0)&={\\frac
{e\^{{\\boldsymbol {\\beta }}\_{0}\\cdot \\mathbf {X}
\_{i}}}{e\^{{\\boldsymbol {\\beta }}\_{0}\\cdot \\mathbf {X}
\_{i}}+e\^{{\\boldsymbol {\\beta }}\_{1}\\cdot \\mathbf {X}
\_{i}}}}\\\\\[5pt\]\\Pr(Y\_{i}=1)&={\\frac {e\^{{\\boldsymbol {\\beta
}}\_{1}\\cdot \\mathbf {X} \_{i}}}{e\^{{\\boldsymbol {\\beta
}}\_{0}\\cdot \\mathbf {X} \_{i}}+e\^{{\\boldsymbol {\\beta
}}\_{1}\\cdot \\mathbf {X} \_{i}}}}.\\end{aligned}}} Or generally: Pr (
Y i = c ) = e β c ⋅ X i ∑ h e β h ⋅ X i {\\displaystyle
\\Pr(Y\_{i}=c)={\\frac {e\^{{\\boldsymbol {\\beta }}\_{c}\\cdot \\mathbf
{X} \_{i}}}{\\sum \_{h}e\^{{\\boldsymbol {\\beta }}\_{h}\\cdot \\mathbf
{X} \_{i}}}}} This shows clearly how to generalize this formulation to
more than two outcomes, as in multinomial logit. Note that this general
formulation is exactly the softmax function as in Pr ( Y i = c ) =
softmax ⁡ ( c , β 0 ⋅ X i , β 1 ⋅ X i , ... ) . {\\displaystyle
\\Pr(Y\_{i}=c)=\\operatorname {softmax} (c,{\\boldsymbol {\\beta
}}\_{0}\\cdot \\mathbf {X} \_{i},{\\boldsymbol {\\beta }}\_{1}\\cdot
\\mathbf {X} \_{i},\\dots ).} In order to prove that this is equivalent
to the previous model, note that the above model is overspecified, in
that Pr ( Y i = 0 ) {\\displaystyle \\Pr(Y\_{i}=0)} and Pr ( Y i = 1 )
{\\displaystyle \\Pr(Y\_{i}=1)} cannot be independently specified:
rather Pr ( Y i = 0 ) + Pr ( Y i = 1 ) = 1 {\\displaystyle
\\Pr(Y\_{i}=0)+\\Pr(Y\_{i}=1)=1} so knowing one automatically determines
the other. As a result, the model is nonidentifiable, in that multiple
combinations of β0 and β1 will produce the same probabilities for all
possible explanatory variables. In fact, it can be seen that adding any
constant vector to both of them will produce the same probabilities: Pr
( Y i = 1 ) = e ( β 1 + C ) ⋅ X i e ( β 0 + C ) ⋅ X i + e ( β 1 + C ) ⋅
X i = e β 1 ⋅ X i e C ⋅ X i e β 0 ⋅ X i e C ⋅ X i + e β 1 ⋅ X i e C ⋅ X
i = e C ⋅ X i e β 1 ⋅ X i e C ⋅ X i ( e β 0 ⋅ X i + e β 1 ⋅ X i ) = e β
1 ⋅ X i e β 0 ⋅ X i + e β 1 ⋅ X i . {\\displaystyle
{\\begin{aligned}\\Pr(Y\_{i}=1)&={\\frac {e\^{({\\boldsymbol {\\beta
}}\_{1}+\\mathbf {C} )\\cdot \\mathbf {X} \_{i}}}{e\^{({\\boldsymbol
{\\beta }}\_{0}+\\mathbf {C} )\\cdot \\mathbf {X}
\_{i}}+e\^{({\\boldsymbol {\\beta }}\_{1}+\\mathbf {C} )\\cdot \\mathbf
{X} \_{i}}}}\\\\\[5pt\]&={\\frac {e\^{{\\boldsymbol {\\beta
}}\_{1}\\cdot \\mathbf {X} \_{i}}e\^{\\mathbf {C} \\cdot \\mathbf {X}
\_{i}}}{e\^{{\\boldsymbol {\\beta }}\_{0}\\cdot \\mathbf {X}
\_{i}}e\^{\\mathbf {C} \\cdot \\mathbf {X} \_{i}}+e\^{{\\boldsymbol
{\\beta }}\_{1}\\cdot \\mathbf {X} \_{i}}e\^{\\mathbf {C} \\cdot
\\mathbf {X} \_{i}}}}\\\\\[5pt\]&={\\frac {e\^{\\mathbf {C} \\cdot
\\mathbf {X} \_{i}}e\^{{\\boldsymbol {\\beta }}\_{1}\\cdot \\mathbf {X}
\_{i}}}{e\^{\\mathbf {C} \\cdot \\mathbf {X} \_{i}}(e\^{{\\boldsymbol
{\\beta }}\_{0}\\cdot \\mathbf {X} \_{i}}+e\^{{\\boldsymbol {\\beta
}}\_{1}\\cdot \\mathbf {X} \_{i}})}}\\\\\[5pt\]&={\\frac
{e\^{{\\boldsymbol {\\beta }}\_{1}\\cdot \\mathbf {X}
\_{i}}}{e\^{{\\boldsymbol {\\beta }}\_{0}\\cdot \\mathbf {X}
\_{i}}+e\^{{\\boldsymbol {\\beta }}\_{1}\\cdot \\mathbf {X}
\_{i}}}}.\\end{aligned}}} As a result, we can simplify matters, and
restore identifiability, by picking an arbitrary value for one of the
two vectors. We choose to set β 0 = 0 . {\\displaystyle {\\boldsymbol
{\\beta }}\_{0}=\\mathbf {0} .} Then, e β 0 ⋅ X i = e 0 ⋅ X i = 1
{\\displaystyle e\^{{\\boldsymbol {\\beta }}\_{0}\\cdot \\mathbf {X}
\_{i}}=e\^{\\mathbf {0} \\cdot \\mathbf {X} \_{i}}=1} and so Pr ( Y i =
1 ) = e β 1 ⋅ X i 1 + e β 1 ⋅ X i = 1 1 + e − β 1 ⋅ X i = p i
{\\displaystyle \\Pr(Y\_{i}=1)={\\frac {e\^{{\\boldsymbol {\\beta
}}\_{1}\\cdot \\mathbf {X} \_{i}}}{1+e\^{{\\boldsymbol {\\beta
}}\_{1}\\cdot \\mathbf {X} \_{i}}}}={\\frac {1}{1+e\^{-{\\boldsymbol
{\\beta }}\_{1}\\cdot \\mathbf {X} \_{i}}}}=p\_{i}} which shows that
this formulation is indeed equivalent to the previous formulation. (As
in the two-way latent variable formulation, any settings where β = β 1 −
β 0 {\\displaystyle {\\boldsymbol {\\beta }}={\\boldsymbol {\\beta
}}\_{1}-{\\boldsymbol {\\beta }}\_{0}} will produce equivalent results.)
Note that most treatments of the multinomial logit model start out
either by extending the \"log-linear\" formulation presented here or the
two-way latent variable formulation presented above, since both clearly
show the way that the model could be extended to multi-way outcomes. In
general, the presentation with latent variables is more common in
econometrics and political science, where discrete choice models and
utility theory reign, while the \"log-linear\" formulation here is more
common in computer science, e.g. machine learning and natural language
processing. As a single-layer perceptron The model has an equivalent
formulation p i = 1 1 + e − ( β 0 + β 1 x 1 , i + ⋯ + β k x k , i ) .
{\\displaystyle p\_{i}={\\frac {1}{1+e\^{-(\\beta \_{0}+\\beta
\_{1}x\_{1,i}+\\cdots +\\beta \_{k}x\_{k,i})}}}.\\,} This functional
form is commonly called a single-layer perceptron or single-layer
artificial neural network. A single-layer neural network computes a
continuous output instead of a step function. The derivative of pi with
respect to X = (x1, \..., xk) is computed from the general form: y = 1
1 + e − f ( X ) {\\displaystyle y={\\frac {1}{1+e\^{-f(X)}}}} where f(X)
is an analytic function in X. With this choice, the single-layer neural
network is identical to the logistic regression model. This function has
a continuous derivative, which allows it to be used in backpropagation.
This function is also preferred because its derivative is easily
calculated: d y d X = y ( 1 − y ) d f d X . {\\displaystyle {\\frac
{\\mathrm {d} y}{\\mathrm {d} X}}=y(1-y){\\frac {\\mathrm {d}
f}{\\mathrm {d} X}}.\\,} In terms of binomial data A closely related
model assumes that each i is associated not with a single Bernoulli
trial but with ni independent identically distributed trials, where the
observation Yi is the number of successes observed (the sum of the
individual Bernoulli-distributed random variables), and hence follows a
binomial distribution: Y i ∼ Bin ⁡ ( n i , p i ) , for i = 1 , ... , n
{\\displaystyle Y\_{i}\\,\\sim \\operatorname {Bin}
(n\_{i},p\_{i}),{\\text{ for }}i=1,\\dots ,n} An example of this
distribution is the fraction of seeds (pi) that germinate after ni are
planted. In terms of expected values, this model is expressed as
follows: p i = E ⁡ \[ Y i n i \| X i \] , {\\displaystyle
p\_{i}=\\operatorname {\\mathbb {E} } \\left\[\\left.{\\frac
{Y\_{i}}{n\_{i}}}\\,\\right\|\\,\\mathbf {X} \_{i}\\right\]\\,,} so that
logit ⁡ ( E ⁡ \[ Y i n i \| X i \] ) = logit ⁡ ( p i ) = ln ⁡ ( p i 1 − p i
) = β ⋅ X i , {\\displaystyle \\operatorname {logit}
\\left(\\operatorname {\\mathbb {E} } \\left\[\\left.{\\frac
{Y\_{i}}{n\_{i}}}\\,\\right\|\\,\\mathbf {X}
\_{i}\\right\]\\right)=\\operatorname {logit} (p\_{i})=\\ln
\\left({\\frac {p\_{i}}{1-p\_{i}}}\\right)={\\boldsymbol {\\beta
}}\\cdot \\mathbf {X} \_{i}\\,,} Or equivalently: Pr ( Y i = y ∣ X i ) =
( n i y ) p i y ( 1 − p i ) n i − y = ( n i y ) ( 1 1 + e − β ⋅ X i ) y
( 1 − 1 1 + e − β ⋅ X i ) n i − y . {\\displaystyle \\Pr(Y\_{i}=y\\mid
\\mathbf {X} \_{i})={n\_{i} \\choose
y}p\_{i}\^{y}(1-p\_{i})\^{n\_{i}-y}={n\_{i} \\choose y}\\left({\\frac
{1}{1+e\^{-{\\boldsymbol {\\beta }}\\cdot \\mathbf {X}
\_{i}}}}\\right)\^{y}\\left(1-{\\frac {1}{1+e\^{-{\\boldsymbol {\\beta
}}\\cdot \\mathbf {X} \_{i}}}}\\right)\^{n\_{i}-y}\\,.} This model can
be fit using the same sorts of methods as the above more basic model.
Model fitting Maximum likelihood estimation (MLE) The regression
coefficients are usually estimated using maximum likelihood estimation.
Unlike linear regression with normally distributed residuals, it is not
possible to find a closed-form expression for the coefficient values
that maximize the likelihood function, so that an iterative process must
be used instead; for example Newton\'s method. This process begins with
a tentative solution, revises it slightly to see if it can be improved,
and repeats this revision until no more improvement is made, at which
point the process is said to have converged.In some instances, the model
may not reach convergence. Non-convergence of a model indicates that the
coefficients are not meaningful because the iterative process was unable
to find appropriate solutions. A failure to converge may occur for a
number of reasons: having a large ratio of predictors to cases,
multicollinearity, sparseness, or complete separation. Having a large
ratio of variables to cases results in an overly conservative Wald
statistic (discussed below) and can lead to non-convergence. Regularized
logistic regression is specifically intended to be used in this
situation. Multicollinearity refers to unacceptably high correlations
between predictors. As multicollinearity increases, coefficients remain
unbiased but standard errors increase and the likelihood of model
convergence decreases. To detect multicollinearity amongst the
predictors, one can conduct a linear regression analysis with the
predictors of interest for the sole purpose of examining the tolerance
statistic used to assess whether multicollinearity is unacceptably high.
Sparseness in the data refers to having a large proportion of empty
cells (cells with zero counts). Zero cell counts are particularly
problematic with categorical predictors. With continuous predictors, the
model can infer values for the zero cell counts, but this is not the
case with categorical predictors. The model will not converge with zero
cell counts for categorical predictors because the natural logarithm of
zero is an undefined value so that the final solution to the model
cannot be reached. To remedy this problem, researchers may collapse
categories in a theoretically meaningful way or add a constant to all
cells. Another numerical problem that may lead to a lack of convergence
is complete separation, which refers to the instance in which the
predictors perfectly predict the criterion -- all cases are accurately
classified and the likelihood maximized with infinite coefficients. In
such instances, one should re-examine the data, as there may be some
kind of error. One can also take semi-parametric or non-parametric
approaches, e.g., via local-likelihood or nonparametric quasi-likelihood
methods, which avoid assumptions of a parametric form for the index
function and is robust to the choice of the link function (e.g., probit
or logit). Iteratively reweighted least squares (IRLS) Binary logistic
regression ( y = 0 {\\displaystyle y=0} or y = 1 {\\displaystyle y=1} )
can, for example, be calculated using iteratively reweighted least
squares (IRLS), which is equivalent to maximizing the log-likelihood of
a Bernoulli distributed process using Newton\'s method. If the problem
is written in vector matrix form, with parameters w T = \[ β 0 , β 1 , β
2 , ... \] {\\displaystyle \\mathbf {w} \^{T}=\[\\beta \_{0},\\beta
\_{1},\\beta \_{2},\\ldots \]} , explanatory variables x ( i ) = \[ 1 ,
x 1 ( i ) , x 2 ( i ) , ... \] T {\\displaystyle \\mathbf {x}
(i)=\[1,x\_{1}(i),x\_{2}(i),\\ldots \]\^{T}} and expected value of the
Bernoulli distribution μ ( i ) = 1 1 + e − w T x ( i ) {\\displaystyle
\\mu (i)={\\frac {1}{1+e\^{-\\mathbf {w} \^{T}\\mathbf {x} (i)}}}} , the
parameters w {\\displaystyle \\mathbf {w} } can be found using the
following iterative algorithm: w k + 1 = ( X T S k X ) − 1 X T ( S k X w
k + y − μ k ) {\\displaystyle \\mathbf {w} \_{k+1}=\\left(\\mathbf {X}
\^{T}\\mathbf {S} \_{k}\\mathbf {X} \\right)\^{-1}\\mathbf {X}
\^{T}\\left(\\mathbf {S} \_{k}\\mathbf {X} \\mathbf {w} \_{k}+\\mathbf
{y} -\\mathbf {\\boldsymbol {\\mu }} \_{k}\\right)} where S = diag ⁡ ( μ
( i ) ( 1 − μ ( i ) ) ) {\\displaystyle \\mathbf {S} =\\operatorname
{diag} (\\mu (i)(1-\\mu (i)))} is a diagonal weighting matrix, μ = \[ μ
( 1 ) , μ ( 2 ) , ... \] {\\displaystyle {\\boldsymbol {\\mu }}=\[\\mu
(1),\\mu (2),\\ldots \]} the vector of expected values, X = \[ 1 x 1 ( 1
) x 2 ( 1 ) ... 1 x 1 ( 2 ) x 2 ( 2 ) ... ⋮ ⋮ ⋮ \] {\\displaystyle
\\mathbf {X} ={\\begin{bmatrix}1&x\_{1}(1)&x\_{2}(1)&\\ldots
\\\\1&x\_{1}(2)&x\_{2}(2)&\\ldots \\\\\\vdots &\\vdots &\\vdots
\\end{bmatrix}}} The regressor matrix and y ( i ) = \[ y ( 1 ) , y ( 2 )
, ... \] T {\\displaystyle \\mathbf {y} (i)=\[y(1),y(2),\\ldots \]\^{T}}
the vector of response variables. More details can be found in the
literature. Bayesian In a Bayesian statistics context, prior
distributions are normally placed on the regression coefficients, for
example in the form of Gaussian distributions. There is no conjugate
prior of the likelihood function in logistic regression. When Bayesian
inference was performed analytically, this made the posterior
distribution difficult to calculate except in very low dimensions. Now,
though, automatic software such as OpenBUGS, JAGS, PyMC3, Stan or
Turing.jl allows these posteriors to be computed using simulation, so
lack of conjugacy is not a concern. However, when the sample size or the
number of parameters is large, full Bayesian simulation can be slow, and
people often use approximate methods such as variational Bayesian
methods and expectation propagation. \"Rule of ten\" A widely used rule
of thumb, the \"one in ten rule\", states that logistic regression
models give stable values for the explanatory variables if based on a
minimum of about 10 events per explanatory variable (EPV); where event
denotes the cases belonging to the less frequent category in the
dependent variable. Thus a study designed to use k {\\displaystyle k}
explanatory variables for an event (e.g. myocardial infarction) expected
to occur in a proportion p {\\displaystyle p} of participants in the
study will require a total of 10 k / p {\\displaystyle 10k/p}
participants. However, there is considerable debate about the
reliability of this rule, which is based on simulation studies and lacks
a secure theoretical underpinning. According to some authors the rule is
overly conservative in some circumstances, with the authors stating,
\"If we (somewhat subjectively) regard confidence interval coverage less
than 93 percent, type I error greater than 7 percent, or relative bias
greater than 15 percent as problematic, our results indicate that
problems are fairly frequent with 2--4 EPV, uncommon with 5--9 EPV, and
still observed with 10--16 EPV. The worst instances of each problem were
not severe with 5--9 EPV and usually comparable to those with 10--16
EPV\".Others have found results that are not consistent with the above,
using different criteria. A useful criterion is whether the fitted model
will be expected to achieve the same predictive discrimination in a new
sample as it appeared to achieve in the model development sample. For
that criterion, 20 events per candidate variable may be required. Also,
one can argue that 96 observations are needed only to estimate the
model\'s intercept precisely enough that the margin of error in
predicted probabilities is ±0.1 with a 0.95 confidence level. Error and
significance of fit Deviance and likelihood ratio test ─ a simple case
In any fitting procedure, the addition of another fitting parameter to a
model (e.g. the beta parameters in a logistic regression model) will
almost always improve the ability of the model to predict the measured
outcomes. This will be true even if the additional term has no
predictive value, since the model will simply be \"overfitting\" to the
noise in the data. The question arises as to whether the improvement
gained by the addition of another fitting parameter is significant
enough to recommend the inclusion of the additional term, or whether the
improvement is simply that which may be expected from overfitting. In
short, for logistic regression, a statistic known as the deviance is
defined which is a measure of the error between the logistic model fit
and the outcome data. In the limit of a large number of data points, the
deviance is chi-squared distributed, which allows a chi-squared test to
be implemented in order to determine the significance of the explanatory
variables. Linear regression and logistic regression have many
similarities. For example, in simple linear regression, a set of K data
points (xk, yk) are fitted to a proposed model function of the form y =
b 0 + b 1 x {\\displaystyle y=b\_{0}+b\_{1}x} . The fit is obtained by
choosing the b parameters which minimize the sum of the squares of the
residuals (the squared error term) for each data point: ϵ 2 = ∑ k = 1 K
( b 0 + b 1 x k − y k ) 2 . {\\displaystyle \\epsilon \^{2}=\\sum
\_{k=1}\^{K}(b\_{0}+b\_{1}x\_{k}-y\_{k})\^{2}.} The minimum value which
constitutes the fit will be denoted by ϵ \^ 2 {\\displaystyle {\\hat
{\\epsilon }}\^{2}} The idea of a null model may be introduced, in which
it is assumed that the x variable is of no use in predicting the yk
outcomes: The data points are fitted to a null model function of the
form y=b0 with a squared error term: ϵ 2 = ∑ k = 1 K ( b 0 − y k ) 2 .
{\\displaystyle \\epsilon \^{2}=\\sum \_{k=1}\^{K}(b\_{0}-y\_{k})\^{2}.}
The fitting process consists of choosing a value of b0 which minimizes ϵ
2 {\\displaystyle \\epsilon \^{2}} of the fit to the null model, denoted
by ϵ φ 2 {\\displaystyle \\epsilon \_{\\varphi }\^{2}} where the φ
{\\displaystyle \\varphi } subscript denotes the null model. It is seen
that the null model is optimized by b 0 = y ¯ {\\displaystyle
b\_{0}={\\overline {y}}} where y ¯ {\\displaystyle {\\overline {y}}} is
the mean of the yk values, and the optimized ϵ φ 2 {\\displaystyle
\\epsilon \_{\\varphi }\^{2}} is: ϵ \^ φ 2 = ∑ k = 1 K ( y ¯ − y k ) 2
{\\displaystyle {\\hat {\\epsilon }}\_{\\varphi }\^{2}=\\sum
\_{k=1}\^{K}({\\overline {y}}-y\_{k})\^{2}} which is proportional to the
square of the (uncorrected) sample standard deviation of the yk data
points. We can imagine a case where the yk data points are randomly
assigned to the various xk, and then fitted using the proposed model.
Specifically, we can consider the fits of the proposed model to every
permutation of the yk outcomes. It can be shown that the optimized error
of any of these fits will never be less than the optimum error of the
null model, and that the difference between these minimum error will
follow a chi-squared distribution, with degrees of freedom equal those
of the proposed model minus those of the null model which, in this case,
will be 2-1=1. Using the chi-squared test, we may then estimate how many
of these permuted sets of yk will yield an minimum error less than or
equal to the minimum error using the original yk, and so we can estimate
how significant an improvement is given by the inclusion of the x
variable in the proposed model. For logistic regression, the measure of
goodness-of-fit is the likelihood function L, or its logarithm, the
log-likelihood ℓ. The likelihood function L is analogous to the ϵ 2
{\\displaystyle \\epsilon \^{2}} in the linear regression case, except
that the likelihood is maximized rather than minimized. Denote the
maximized log-likelihood of the proposed model by ℓ \^ {\\displaystyle
{\\hat {\\ell }}} . In the case of simple binary logistic regression,
the set of K data points are fitted in a probabilistic sense to a
function of the form: p ( x ) = 1 1 + e − t {\\displaystyle p(x)={\\frac
{1}{1+e\^{-t}}}} where p ( x ) {\\displaystyle p(x)} is the probability
that y = 1 {\\displaystyle y=1} . The log-odds are given by: t = β 0 + β
1 x {\\displaystyle t=\\beta \_{0}+\\beta \_{1}x} and the log-likelihood
is: ℓ = ∑ k = 1 K ( y k ln ⁡ ( p ( x k ) ) + ( 1 − y k ) ln ⁡ ( 1 − p ( x
k ) ) ) {\\displaystyle \\ell =\\sum
\_{k=1}\^{K}\\left(y\_{k}\\ln(p(x\_{k}))+(1-y\_{k})\\ln(1-p(x\_{k}))\\right)}
For the null model, the probability that y = 1 {\\displaystyle y=1} is
given by: p φ ( x ) = 1 1 + e − t φ {\\displaystyle p\_{\\varphi
}(x)={\\frac {1}{1+e\^{-t\_{\\varphi }}}}} The log-odds for the null
model are given by: t φ = β 0 {\\displaystyle t\_{\\varphi }=\\beta
\_{0}} and the log-likelihood is: ℓ φ = ∑ k = 1 K ( y k ln ⁡ ( p φ ) + (
1 − y k ) ln ⁡ ( 1 − p φ ) ) {\\displaystyle \\ell \_{\\varphi }=\\sum
\_{k=1}\^{K}\\left(y\_{k}\\ln(p\_{\\varphi
})+(1-y\_{k})\\ln(1-p\_{\\varphi })\\right)} Since we have p φ = y ¯
{\\displaystyle p\_{\\varphi }={\\overline {y}}} at the maximum of L,
the maximum log-likelihood for the null model is ℓ \^ φ = K ( y ¯ ln ⁡ (
y ¯ ) + ( 1 − y ¯ ) ln ⁡ ( 1 − y ¯ ) ) {\\displaystyle {\\hat {\\ell
}}\_{\\varphi }=K(\\,{\\overline {y}}\\ln({\\overline
{y}})+(1-{\\overline {y}})\\ln(1-{\\overline {y}}))} The optimum β 0
{\\displaystyle \\beta \_{0}} is: β 0 = ln ⁡ ( y ¯ 1 − y ¯ )
{\\displaystyle \\beta \_{0}=\\ln \\left({\\frac {\\overline
{y}}{1-{\\overline {y}}}}\\right)} where y ¯ {\\displaystyle {\\overline
{y}}} is again the mean of the yk values. Again, we can conceptually
consider the fit of the proposed model to every permutation of the yk
and it can be shown that the maximum log-likelihood of these permutation
fits will never be smaller than that of the null model: ℓ \^ ≥ ℓ \^ φ
{\\displaystyle {\\hat {\\ell }}\\geq {\\hat {\\ell }}\_{\\varphi }}
Also, as an analog to the error of the linear regression case, we may
define the deviance of a logistic regression fit as: D = ln ⁡ ( L \^ 2 L
\^ φ 2 ) = 2 ( ℓ \^ − ℓ \^ φ ) {\\displaystyle D=\\ln \\left({\\frac
{{\\hat {L}}\^{2}}{{\\hat {L}}\_{\\varphi }\^{2}}}\\right)=2({\\hat
{\\ell }}-{\\hat {\\ell }}\_{\\varphi })} which will always be positive
or zero. The reason for this choice is that not only is the deviance a
good measure of the goodness of fit, it is also approximately
chi-squared distributed, with the approximation improving as the number
of data points (K) increases, becoming exactly chi-square distributed in
the limit of an infinite number of data points. As in the case of linear
regression, we may use this fact to estimate the probability that a
random set of data points will give a better fit than the fit obtained
by the proposed model, and so have an estimate how significantly the
model is improved by including the xk data points in the proposed model.
For the simple model of student test scores described above, the maximum
value of the log-likelihood of the null model is ℓ \^ φ = − 13.8629\...
{\\displaystyle {\\hat {\\ell }}\_{\\varphi }=-13.8629\...} The maximum
value of the log-likelihood for the simple model is ℓ \^ = − 8.02988\...
{\\displaystyle {\\hat {\\ell }}=-8.02988\...} so that the deviance is D
= 2 ( ℓ \^ − ℓ \^ φ ) = 11.6661\... {\\displaystyle D=2({\\hat {\\ell
}}-{\\hat {\\ell }}\_{\\varphi })=11.6661\...} Using the chi-squared
test of significance, the integral of the chi-squared distribution with
one degree of freedom from 11.6661\... to infinity is equal to
0.00063649\... This effectively means that about 6 out of a 10,000 fits
to random yk can be expected to have a better fit (smaller deviance)
than the given yk and so we can conclude that the inclusion of the x
variable and data in the proposed model is a very significant
improvement over the null model. In other words, we reject the null
hypothesis with 1 − D ≈ 99.94 % {\\displaystyle 1-D\\approx 99.94\\%}
confidence. Goodness of fit summary Goodness of fit in linear regression
models is generally measured using R2. Since this has no direct analog
in logistic regression, various methods: ch.21  including the following
can be used instead. Deviance and likelihood ratio tests In linear
regression analysis, one is concerned with partitioning variance via the
sum of squares calculations -- variance in the criterion is essentially
divided into variance accounted for by the predictors and residual
variance. In logistic regression analysis, deviance is used in lieu of a
sum of squares calculations. Deviance is analogous to the sum of squares
calculations in linear regression and is a measure of the lack of fit to
the data in a logistic regression model. When a \"saturated\" model is
available (a model with a theoretically perfect fit), deviance is
calculated by comparing a given model with the saturated model. This
computation gives the likelihood-ratio test: D = − 2 ln ⁡ likelihood of
the fitted model likelihood of the saturated model . {\\displaystyle
D=-2\\ln {\\frac {\\text{likelihood of the fitted
model}}{\\text{likelihood of the saturated model}}}.} In the above
equation, D represents the deviance and ln represents the natural
logarithm. The log of this likelihood ratio (the ratio of the fitted
model to the saturated model) will produce a negative value, hence the
need for a negative sign. D can be shown to follow an approximate
chi-squared distribution. Smaller values indicate better fit as the
fitted model deviates less from the saturated model. When assessed upon
a chi-square distribution, nonsignificant chi-square values indicate
very little unexplained variance and thus, good model fit. Conversely, a
significant chi-square value indicates that a significant amount of the
variance is unexplained. When the saturated model is not available (a
common case), deviance is calculated simply as −2·(log likelihood of the
fitted model), and the reference to the saturated model\'s log
likelihood can be removed from all that follows without harm. Two
measures of deviance are particularly important in logistic regression:
null deviance and model deviance. The null deviance represents the
difference between a model with only the intercept (which means \"no
predictors\") and the saturated model. The model deviance represents the
difference between a model with at least one predictor and the saturated
model. In this respect, the null model provides a baseline upon which to
compare predictor models. Given that deviance is a measure of the
difference between a given model and the saturated model, smaller values
indicate better fit. Thus, to assess the contribution of a predictor or
set of predictors, one can subtract the model deviance from the null
deviance and assess the difference on a χ s − p 2 , {\\displaystyle
\\chi \_{s-p}\^{2},} chi-square distribution with degrees of freedom
equal to the difference in the number of parameters estimated. Let D
null = − 2 ln ⁡ likelihood of null model likelihood of the saturated
model D fitted = − 2 ln ⁡ likelihood of fitted model likelihood of the
saturated model . {\\displaystyle
{\\begin{aligned}D\_{\\text{null}}&=-2\\ln {\\frac {\\text{likelihood of
null model}}{\\text{likelihood of the saturated
model}}}\\\\\[6pt\]D\_{\\text{fitted}}&=-2\\ln {\\frac
{\\text{likelihood of fitted model}}{\\text{likelihood of the saturated
model}}}.\\end{aligned}}} Then the difference of both is: D null − D
fitted = − 2 ( ln ⁡ likelihood of null model likelihood of the saturated
model − ln ⁡ likelihood of fitted model likelihood of the saturated model
) = − 2 ln ⁡ ( likelihood of null model likelihood of the saturated model
) ( likelihood of fitted model likelihood of the saturated model ) = − 2
ln ⁡ likelihood of the null model likelihood of fitted model .
{\\displaystyle
{\\begin{aligned}D\_{\\text{null}}-D\_{\\text{fitted}}&=-2\\left(\\ln
{\\frac {\\text{likelihood of null model}}{\\text{likelihood of the
saturated model}}}-\\ln {\\frac {\\text{likelihood of fitted
model}}{\\text{likelihood of the saturated
model}}}\\right)\\\\\[6pt\]&=-2\\ln {\\frac {\\left({\\dfrac
{\\text{likelihood of null model}}{\\text{likelihood of the saturated
model}}}\\right)}{\\left({\\dfrac {\\text{likelihood of fitted
model}}{\\text{likelihood of the saturated
model}}}\\right)}}\\\\\[6pt\]&=-2\\ln {\\frac {\\text{likelihood of the
null model}}{\\text{likelihood of fitted model}}}.\\end{aligned}}} If
the model deviance is significantly smaller than the null deviance then
one can conclude that the predictor or set of predictors significantly
improve the model\'s fit. This is analogous to the F-test used in linear
regression analysis to assess the significance of prediction.
Pseudo-R-squared In linear regression the squared multiple correlation,
R2 is used to assess goodness of fit as it represents the proportion of
variance in the criterion that is explained by the predictors. In
logistic regression analysis, there is no agreed upon analogous measure,
but there are several competing measures each with limitations.Four of
the most commonly used indices and one less commonly used one are
examined on this page: Likelihood ratio R2L Cox and Snell R2CS
Nagelkerke R2N McFadden R2McF Tjur R2T Hosmer--Lemeshow test The
Hosmer--Lemeshow test uses a test statistic that asymptotically follows
a χ 2 {\\displaystyle \\chi \^{2}} distribution to assess whether or not
the observed event rates match expected event rates in subgroups of the
model population. This test is considered to be obsolete by some
statisticians because of its dependence on arbitrary binning of
predicted probabilities and relative low power. Coefficient significance
After fitting the model, it is likely that researchers will want to
examine the contribution of individual predictors. To do so, they will
want to examine the regression coefficients. In linear regression, the
regression coefficients represent the change in the criterion for each
unit change in the predictor. In logistic regression, however, the
regression coefficients represent the change in the logit for each unit
change in the predictor. Given that the logit is not intuitive,
researchers are likely to focus on a predictor\'s effect on the
exponential function of the regression coefficient -- the odds ratio
(see definition). In linear regression, the significance of a regression
coefficient is assessed by computing a t test. In logistic regression,
there are several different tests designed to assess the significance of
an individual predictor, most notably the likelihood ratio test and the
Wald statistic. Likelihood ratio test The likelihood-ratio test
discussed above to assess model fit is also the recommended procedure to
assess the contribution of individual \"predictors\" to a given model.
In the case of a single predictor model, one simply compares the
deviance of the predictor model with that of the null model on a
chi-square distribution with a single degree of freedom. If the
predictor model has significantly smaller deviance (c.f. chi-square
using the difference in degrees of freedom of the two models), then one
can conclude that there is a significant association between the
\"predictor\" and the outcome. Although some common statistical packages
(e.g. SPSS) do provide likelihood ratio test statistics, without this
computationally intensive test it would be more difficult to assess the
contribution of individual predictors in the multiple logistic
regression case. To assess the contribution of individual predictors one
can enter the predictors hierarchically, comparing each new model with
the previous to determine the contribution of each predictor. There is
some debate among statisticians about the appropriateness of so-called
\"stepwise\" procedures. The fear is that they may not preserve nominal
statistical properties and may become misleading. Wald statistic
Alternatively, when assessing the contribution of individual predictors
in a given model, one may examine the significance of the Wald
statistic. The Wald statistic, analogous to the t-test in linear
regression, is used to assess the significance of coefficients. The Wald
statistic is the ratio of the square of the regression coefficient to
the square of the standard error of the coefficient and is
asymptotically distributed as a chi-square distribution. W j = β j 2 S E
β j 2 {\\displaystyle W\_{j}={\\frac {\\beta \_{j}\^{2}}{SE\_{\\beta
\_{j}}\^{2}}}} Although several statistical packages (e.g., SPSS, SAS)
report the Wald statistic to assess the contribution of individual
predictors, the Wald statistic has limitations. When the regression
coefficient is large, the standard error of the regression coefficient
also tends to be larger increasing the probability of Type-II error. The
Wald statistic also tends to be biased when data are sparse.
Case-control sampling Suppose cases are rare. Then we might wish to
sample them more frequently than their prevalence in the population. For
example, suppose there is a disease that affects 1 person in 10,000 and
to collect our data we need to do a complete physical. It may be too
expensive to do thousands of physicals of healthy people in order to
obtain data for only a few diseased individuals. Thus, we may evaluate
more diseased individuals, perhaps all of the rare outcomes. This is
also retrospective sampling, or equivalently it is called unbalanced
data. As a rule of thumb, sampling controls at a rate of five times the
number of cases will produce sufficient control data.Logistic regression
is unique in that it may be estimated on unbalanced data, rather than
randomly sampled data, and still yield correct coefficient estimates of
the effects of each independent variable on the outcome. That is to say,
if we form a logistic model from such data, if the model is correct in
the general population, the β j {\\displaystyle \\beta \_{j}} parameters
are all correct except for β 0 {\\displaystyle \\beta \_{0}} . We can
correct β 0 {\\displaystyle \\beta \_{0}} if we know the true prevalence
as follows: β \^ 0 ∗ = β \^ 0 + log ⁡ π 1 − π − log ⁡ π \~ 1 − π \~
{\\displaystyle {\\widehat {\\beta }}\_{0}\^{\*}={\\widehat {\\beta
}}\_{0}+\\log {\\frac {\\pi }{1-\\pi }}-\\log {{\\tilde {\\pi }} \\over
{1-{\\tilde {\\pi }}}}} where π {\\displaystyle \\pi } is the true
prevalence and π \~ {\\displaystyle {\\tilde {\\pi }}} is the prevalence
in the sample. Discussion Like other forms of regression analysis,
logistic regression makes use of one or more predictor variables that
may be either continuous or categorical. Unlike ordinary linear
regression, however, logistic regression is used for predicting
dependent variables that take membership in one of a limited number of
categories (treating the dependent variable in the binomial case as the
outcome of a Bernoulli trial) rather than a continuous outcome. Given
this difference, the assumptions of linear regression are violated. In
particular, the residuals cannot be normally distributed. In addition,
linear regression may make nonsensical predictions for a binary
dependent variable. What is needed is a way to convert a binary variable
into a continuous one that can take on any real value (negative or
positive). To do that, binomial logistic regression first calculates the
odds of the event happening for different levels of each independent
variable, and then takes its logarithm to create a continuous criterion
as a transformed version of the dependent variable. The logarithm of the
odds is the logit of the probability, the logit is defined as follows:
Although the dependent variable in logistic regression is Bernoulli, the
logit is on an unrestricted scale. The logit function is the link
function in this kind of generalized linear model, i.e. Y is the
Bernoulli-distributed response variable and x is the predictor variable;
the β values are the linear parameters. The logit of the probability of
success is then fitted to the predictors. The predicted value of the
logit is converted back into predicted odds, via the inverse of the
natural logarithm -- the exponential function. Thus, although the
observed dependent variable in binary logistic regression is a 0-or-1
variable, the logistic regression estimates the odds, as a continuous
variable, that the dependent variable is a \'success\'. In some
applications, the odds are all that is needed. In others, a specific
yes-or-no prediction is needed for whether the dependent variable is or
is not a \'success\'; this categorical prediction can be based on the
computed odds of success, with predicted odds above some chosen cutoff
value being translated into a prediction of success. Maximum entropy Of
all the functional forms used for estimating the probabilities of a
particular categorical outcome which optimize the fit by maximizing the
likelihood function (e.g. probit regression, Poisson regression, etc.),
the logistic regression solution is unique in that it is a maximum
entropy solution. This is a case of a general property: an exponential
family of distributions maximizes entropy, given an expected value. In
the case of the logistic model, the logistic function is the natural
parameter of the Bernoulli distribution (it is in \"canonical form\",
and the logistic function is the canonical link function), while other
sigmoid functions are non-canonical link functions; this underlies its
mathematical elegance and ease of optimization. See Exponential family §
Maximum entropy derivation for details. Proof In order to show this, we
use the method of Lagrange multipliers. The Lagrangian is equal to the
entropy plus the sum of the products of Lagrange multipliers times
various constraint expressions. The general multinomial case will be
considered, since the proof is not made that much simpler by considering
simpler cases. Equating the derivative of the Lagrangian with respect to
the various probabilities to zero yields a functional form for those
probabilities which corresponds to those used in logistic regression.As
in the above section on multinomial logistic regression, we will
consider M + 1 {\\displaystyle M+1} explanatory variables denoted x m
{\\displaystyle x\_{m}} and which include x 0 = 1 {\\displaystyle
x\_{0}=1} . There will be a total of K data points, indexed by k = { 1 ,
2 , ... , K } {\\displaystyle k=\\{1,2,\\dots ,K\\}} , and the data
points are given by x m k {\\displaystyle x\_{mk}} and y k
{\\displaystyle y\_{k}} . The xmk will also be represented as an ( M + 1
) {\\displaystyle (M+1)} -dimensional vector x k = { x 0 k , x 1 k , ...
, x M k } {\\displaystyle {\\boldsymbol
{x}}\_{k}=\\{x\_{0k},x\_{1k},\\dots ,x\_{Mk}\\}} . There will be N + 1
{\\displaystyle N+1} possible values of the categorical variable y
ranging from 0 to N. Let pn(x) be the probability, given explanatory
variable vector x, that the outcome will be y = n {\\displaystyle y=n} .
Define p n k = p n ( x k ) {\\displaystyle p\_{nk}=p\_{n}({\\boldsymbol
{x}}\_{k})} which is the probability that for the k-th measurement, the
categorical outcome is n. The Lagrangian will be expressed as a function
of the probabilities pnk and will minimized by equating the derivatives
of the Lagrangian with respect to these probabilities to zero. An
important point is that the probabilities are treated equally and the
fact that they sum to unity is part of the Lagrangian formulation,
rather than being assumed from the beginning. The first contribution to
the Lagrangian is the entropy: L e n t = − ∑ k = 1 K ∑ n = 0 N p n k ln ⁡
( p n k ) {\\displaystyle {\\mathcal {L}}\_{ent}=-\\sum
\_{k=1}\^{K}\\sum \_{n=0}\^{N}p\_{nk}\\ln(p\_{nk})} The log-likelihood
is: ℓ = ∑ k = 1 K ∑ n = 0 N Δ ( n , y k ) ln ⁡ ( p n k ) {\\displaystyle
\\ell =\\sum \_{k=1}\^{K}\\sum \_{n=0}\^{N}\\Delta
(n,y\_{k})\\ln(p\_{nk})} Assuming the multinomial logistic function, the
derivative of the log-likelihood with respect the beta coefficients was
found to be: ∂ ℓ ∂ β n m = ∑ k = 1 K ( p n k x m k − Δ ( n , y k ) x m k
) {\\displaystyle {\\frac {\\partial \\ell }{\\partial \\beta
\_{nm}}}=\\sum \_{k=1}\^{K}(p\_{nk}x\_{mk}-\\Delta (n,y\_{k})x\_{mk})} A
very important point here is that this expression is (remarkably) not an
explicit function of the beta coefficients. It is only a function of the
probabilities pnk and the data. Rather than being specific to the
assumed multinomial logistic case, it is taken to be a general statement
of the condition at which the log-likelihood is maximized and makes no
reference to the functional form of pnk. There are then (M+1)(N+1)
fitting constraints and the fitting constraint term in the Lagrangian is
then: L f i t = ∑ n = 0 N ∑ m = 0 M λ n m ∑ k = 1 K ( p n k x m k − Δ (
n , y k ) x m k ) {\\displaystyle {\\mathcal {L}}\_{fit}=\\sum
\_{n=0}\^{N}\\sum \_{m=0}\^{M}\\lambda \_{nm}\\sum
\_{k=1}\^{K}(p\_{nk}x\_{mk}-\\Delta (n,y\_{k})x\_{mk})} where the λnm
are the appropriate Lagrange multipliers. There are K normalization
constraints which may be written: ∑ n = 0 N p n k = 1 {\\displaystyle
\\sum \_{n=0}\^{N}p\_{nk}=1} so that the normalization term in the
Lagrangian is: L n o r m = ∑ k = 1 K α k ( 1 − ∑ n = 1 N p n k )
{\\displaystyle {\\mathcal {L}}\_{norm}=\\sum \_{k=1}\^{K}\\alpha
\_{k}\\left(1-\\sum \_{n=1}\^{N}p\_{nk}\\right)} where the αk are the
appropriate Lagrange multipliers. The Lagrangian is then the sum of the
above three terms: L = L e n t + L f i t + L n o r m {\\displaystyle
{\\mathcal {L}}={\\mathcal {L}}\_{ent}+{\\mathcal {L}}\_{fit}+{\\mathcal
{L}}\_{norm}} Setting the derivative of the Lagrangian with respect to
one of the probabilities to zero yields: ∂ L ∂ p n ′ k ′ = 0 = − ln ⁡ ( p
n ′ k ′ ) − 1 + ∑ m = 0 M ( λ n ′ m x m k ′ ) − α k ′ {\\displaystyle
{\\frac {\\partial {\\mathcal {L}}}{\\partial
p\_{n\'k\'}}}=0=-\\ln(p\_{n\'k\'})-1+\\sum \_{m=0}\^{M}(\\lambda
\_{n\'m}x\_{mk\'})-\\alpha \_{k\'}} Using the more condensed vector
notation: ∑ m = 0 M λ n m x m k = λ n ⋅ x k {\\displaystyle \\sum
\_{m=0}\^{M}\\lambda \_{nm}x\_{mk}={\\boldsymbol {\\lambda }}\_{n}\\cdot
{\\boldsymbol {x}}\_{k}} and dropping the primes on the n and k indices,
and then solving for p n k {\\displaystyle p\_{nk}} yields: p n k = e λ
n ⋅ x k / Z k {\\displaystyle p\_{nk}=e\^{{\\boldsymbol {\\lambda
}}\_{n}\\cdot {\\boldsymbol {x}}\_{k}}/Z\_{k}} where: Z k = e 1 + α k
{\\displaystyle Z\_{k}=e\^{1+\\alpha \_{k}}} Imposing the normalization
constraint, we can solve for the Zk and write the probabilities as: p n
k = e λ n ⋅ x k ∑ u = 0 N e λ u ⋅ x k {\\displaystyle p\_{nk}={\\frac
{e\^{{\\boldsymbol {\\lambda }}\_{n}\\cdot {\\boldsymbol
{x}}\_{k}}}{\\sum \_{u=0}\^{N}e\^{{\\boldsymbol {\\lambda }}\_{u}\\cdot
{\\boldsymbol {x}}\_{k}}}}} The λ n {\\displaystyle {\\boldsymbol
{\\lambda }}\_{n}} are not all independent. We can add any constant (
M + 1 ) {\\displaystyle (M+1)} -dimensional vector to each of the λ n
{\\displaystyle {\\boldsymbol {\\lambda }}\_{n}} without changing the
value of the p n k {\\displaystyle p\_{nk}} probabilities so that there
are only N rather than N + 1 {\\displaystyle N+1} independent λ n
{\\displaystyle {\\boldsymbol {\\lambda }}\_{n}} . In the multinomial
logistic regression section above, the λ 0 {\\displaystyle {\\boldsymbol
{\\lambda }}\_{0}} was subtracted from each λ n {\\displaystyle
{\\boldsymbol {\\lambda }}\_{n}} which set the exponential term
involving λ 0 {\\displaystyle {\\boldsymbol {\\lambda }}\_{0}} to unity,
and the beta coefficients were given by β n = λ n − λ 0 {\\displaystyle
{\\boldsymbol {\\beta }}\_{n}={\\boldsymbol {\\lambda
}}\_{n}-{\\boldsymbol {\\lambda }}\_{0}} . Other approaches In machine
learning applications where logistic regression is used for binary
classification, the MLE minimises the Cross entropy loss function.
Logistic regression is an important machine learning algorithm. The goal
is to model the probability of a random variable Y {\\displaystyle Y}
being 0 or 1 given experimental data.Consider a generalized linear model
function parameterized by θ {\\displaystyle \\theta } , h θ ( X ) = 1
1 + e − θ T X = Pr ( Y = 1 ∣ X ; θ ) {\\displaystyle h\_{\\theta
}(X)={\\frac {1}{1+e\^{-\\theta \^{T}X}}}=\\Pr(Y=1\\mid X;\\theta )}
Therefore, Pr ( Y = 0 ∣ X ; θ ) = 1 − h θ ( X ) {\\displaystyle
\\Pr(Y=0\\mid X;\\theta )=1-h\_{\\theta }(X)} and since Y ∈ { 0 , 1 }
{\\displaystyle Y\\in \\{0,1\\}} , we see that Pr ( y ∣ X ; θ )
{\\displaystyle \\Pr(y\\mid X;\\theta )} is given by Pr ( y ∣ X ; θ ) =
h θ ( X ) y ( 1 − h θ ( X ) ) ( 1 − y ) . {\\displaystyle \\Pr(y\\mid
X;\\theta )=h\_{\\theta }(X)\^{y}(1-h\_{\\theta }(X))\^{(1-y)}.} We now
calculate the likelihood function assuming that all the observations in
the sample are independently Bernoulli distributed, L ( θ ∣ y ; x ) = Pr
( Y ∣ X ; θ ) = ∏ i Pr ( y i ∣ x i ; θ ) = ∏ i h θ ( x i ) y i ( 1 − h θ
( x i ) ) ( 1 − y i ) {\\displaystyle {\\begin{aligned}L(\\theta \\mid
y;x)&=\\Pr(Y\\mid X;\\theta )\\\\&=\\prod \_{i}\\Pr(y\_{i}\\mid
x\_{i};\\theta )\\\\&=\\prod \_{i}h\_{\\theta
}(x\_{i})\^{y\_{i}}(1-h\_{\\theta
}(x\_{i}))\^{(1-y\_{i})}\\end{aligned}}} Typically, the log likelihood
is maximized, N − 1 log ⁡ L ( θ ∣ y ; x ) = N − 1 ∑ i = 1 N log ⁡ Pr ( y i
∣ x i ; θ ) {\\displaystyle N\^{-1}\\log L(\\theta \\mid
y;x)=N\^{-1}\\sum \_{i=1}\^{N}\\log \\Pr(y\_{i}\\mid x\_{i};\\theta )}
which is maximized using optimization techniques such as gradient
descent. Assuming the ( x , y ) {\\displaystyle (x,y)} pairs are drawn
uniformly from the underlying distribution, then in the limit of large
N, lim N → + ∞ N − 1 ∑ i = 1 N log ⁡ Pr ( y i ∣ x i ; θ ) = ∑ x ∈ X ∑ y ∈
Y Pr ( X = x , Y = y ) log ⁡ Pr ( Y = y ∣ X = x ; θ ) = ∑ x ∈ X ∑ y ∈ Y
Pr ( X = x , Y = y ) ( − log ⁡ Pr ( Y = y ∣ X = x ) Pr ( Y = y ∣ X = x ;
θ ) + log ⁡ Pr ( Y = y ∣ X = x ) ) = − D KL ( Y ∥ Y θ ) − H ( Y ∣ X )
{\\displaystyle {\\begin{aligned}&\\lim \\limits \_{N\\rightarrow
+\\infty }N\^{-1}\\sum \_{i=1}\^{N}\\log \\Pr(y\_{i}\\mid x\_{i};\\theta
)=\\sum \_{x\\in {\\mathcal {X}}}\\sum \_{y\\in {\\mathcal
{Y}}}\\Pr(X=x,Y=y)\\log \\Pr(Y=y\\mid X=x;\\theta )\\\\\[6pt\]={}&\\sum
\_{x\\in {\\mathcal {X}}}\\sum \_{y\\in {\\mathcal
{Y}}}\\Pr(X=x,Y=y)\\left(-\\log {\\frac {\\Pr(Y=y\\mid
X=x)}{\\Pr(Y=y\\mid X=x;\\theta )}}+\\log \\Pr(Y=y\\mid
X=x)\\right)\\\\\[6pt\]={}&-D\_{\\text{KL}}(Y\\parallel Y\_{\\theta
})-H(Y\\mid X)\\end{aligned}}} where H ( Y ∣ X ) {\\displaystyle
H(Y\\mid X)} is the conditional entropy and D KL {\\displaystyle
D\_{\\text{KL}}} is the Kullback--Leibler divergence. This leads to the
intuition that by maximizing the log-likelihood of a model, you are
minimizing the KL divergence of your model from the maximal entropy
distribution. Intuitively searching for the model that makes the fewest
assumptions in its parameters. Comparison with linear regression
Logistic regression can be seen as a special case of the generalized
linear model and thus analogous to linear regression. The model of
logistic regression, however, is based on quite different assumptions
(about the relationship between the dependent and independent variables)
from those of linear regression. In particular, the key differences
between these two models can be seen in the following two features of
logistic regression. First, the conditional distribution y ∣ x
{\\displaystyle y\\mid x} is a Bernoulli distribution rather than a
Gaussian distribution, because the dependent variable is binary. Second,
the predicted values are probabilities and are therefore restricted to
(0,1) through the logistic distribution function because logistic
regression predicts the probability of particular outcomes rather than
the outcomes themselves. Alternatives A common alternative to the
logistic model (logit model) is the probit model, as the related names
suggest. From the perspective of generalized linear models, these differ
in the choice of link function: the logistic model uses the logit
function (inverse logistic function), while the probit model uses the
probit function (inverse error function). Equivalently, in the latent
variable interpretations of these two methods, the first assumes a
standard logistic distribution of errors and the second a standard
normal distribution of errors. Other sigmoid functions or error
distributions can be used instead. Logistic regression is an alternative
to Fisher\'s 1936 method, linear discriminant analysis. If the
assumptions of linear discriminant analysis hold, the conditioning can
be reversed to produce logistic regression. The converse is not true,
however, because logistic regression does not require the multivariate
normal assumption of discriminant analysis.The assumption of linear
predictor effects can easily be relaxed using techniques such as spline
functions. History A detailed history of the logistic regression is
given in Cramer (2002). The logistic function was developed as a model
of population growth and named \"logistic\" by Pierre François Verhulst
in the 1830s and 1840s, under the guidance of Adolphe Quetelet; see
Logistic function § History for details. In his earliest paper (1838),
Verhulst did not specify how he fit the curves to the data. In his more
detailed paper (1845), Verhulst determined the three parameters of the
model by making the curve pass through three observed points, which
yielded poor predictions.The logistic function was independently
developed in chemistry as a model of autocatalysis (Wilhelm Ostwald,
1883). An autocatalytic reaction is one in which one of the products is
itself a catalyst for the same reaction, while the supply of one of the
reactants is fixed. This naturally gives rise to the logistic equation
for the same reason as population growth: the reaction is
self-reinforcing but constrained. The logistic function was
independently rediscovered as a model of population growth in 1920 by
Raymond Pearl and Lowell Reed, published as Pearl & Reed (1920), which
led to its use in modern statistics. They were initially unaware of
Verhulst\'s work and presumably learned about it from L. Gustave du
Pasquier, but they gave him little credit and did not adopt his
terminology. Verhulst\'s priority was acknowledged and the term
\"logistic\" revived by Udny Yule in 1925 and has been followed since.
Pearl and Reed first applied the model to the population of the United
States, and also initially fitted the curve by making it pass through
three points; as with Verhulst, this again yielded poor results.In the
1930s, the probit model was developed and systematized by Chester Ittner
Bliss, who coined the term \"probit\" in Bliss (1934), and by John
Gaddum in Gaddum (1933), and the model fit by maximum likelihood
estimation by Ronald A. Fisher in Fisher (1935), as an addendum to
Bliss\'s work. The probit model was principally used in bioassay, and
had been preceded by earlier work dating to 1860; see Probit model §
History. The probit model influenced the subsequent development of the
logit model and these models competed with each other.The logistic model
was likely first used as an alternative to the probit model in bioassay
by Edwin Bidwell Wilson and his student Jane Worcester in Wilson &
Worcester (1943). However, the development of the logistic model as a
general alternative to the probit model was principally due to the work
of Joseph Berkson over many decades, beginning in Berkson (1944), where
he coined \"logit\", by analogy with \"probit\", and continuing through
Berkson (1951) and following years. The logit model was initially
dismissed as inferior to the probit model, but \"gradually achieved an
equal footing with the logit\", particularly between 1960 and 1970. By
1970, the logit model achieved parity with the probit model in use in
statistics journals and thereafter surpassed it. This relative
popularity was due to the adoption of the logit outside of bioassay,
rather than displacing the probit within bioassay, and its informal use
in practice; the logit\'s popularity is credited to the logit model\'s
computational simplicity, mathematical properties, and generality,
allowing its use in varied fields.Various refinements occurred during
that time, notably by David Cox, as in Cox (1958).The multinomial logit
model was introduced independently in Cox (1966) and Theil (1969), which
greatly increased the scope of application and the popularity of the
logit model. In 1973 Daniel McFadden linked the multinomial logit to the
theory of discrete choice, specifically Luce\'s choice axiom, showing
that the multinomial logit followed from the assumption of independence
of irrelevant alternatives and interpreting odds of alternatives as
relative preferences; this gave a theoretical foundation for the
logistic regression. Extensions There are large numbers of extensions:
Multinomial logistic regression (or multinomial logit) handles the case
of a multi-way categorical dependent variable (with unordered values,
also called \"classification\"). Note that the general case of having
dependent variables with more than two values is termed polytomous
regression. Ordered logistic regression (or ordered logit) handles
ordinal dependent variables (ordered values). Mixed logit is an
extension of multinomial logit that allows for correlations among the
choices of the dependent variable. An extension of the logistic model to
sets of interdependent variables is the conditional random field.
Conditional logistic regression handles matched or stratified data when
the strata are small. It is mostly used in the analysis of observational
studies. Software Most statistical software can do binary logistic
regression. SPSS \[1\] for basic logistic regression. Stata SAS PROC
LOGISTIC for basic logistic regression. PROC CATMOD when all the
variables are categorical. PROC GLIMMIX for multilevel model logistic
regression. R glm in the stats package (using family = binomial) lrm in
the rms package GLMNET package for an efficient implementation
regularized logistic regression lmer for mixed effects logistic
regression Rfast package command gm_logistic for fast and heavy
calculations involving large scale data. arm package for bayesian
logistic regression Python Logit in the Statsmodels module.
LogisticRegression in the scikit-learn module. LogisticRegressor in the
TensorFlow module. Full example of logistic regression in the Theano
tutorial \[2\] Bayesian Logistic Regression with ARD prior code,
tutorial Variational Bayes Logistic Regression with ARD prior code ,
tutorial Bayesian Logistic Regression code, tutorial NCSS Logistic
Regression in NCSS Matlab mnrfit in the Statistics and Machine Learning
Toolbox (with \"incorrect\" coded as 2 instead of 0) fminunc/fmincon,
fitglm, mnrfit, fitclinear, mle can all do logistic regression. Java
(JVM) LibLinear Apache Flink Apache Spark SparkML supports Logistic
Regression FPGA Logistic Regresesion IP core in HLS for FPGA.Notably,
Microsoft Excel\'s statistics extension package does not include it. See
also Logistic function Discrete choice Jarrow--Turnbull model Limited
dependent variable Multinomial logit model Ordered logit
Hosmer--Lemeshow test Brier score mlpack - contains a C++ implementation
of logistic regression Local case-control sampling Logistic model tree
References Further reading External links Media related to Logistic
regression at Wikimedia Commons Econometrics Lecture (topic: Logit
model) on YouTube by Mark Thoma Logistic Regression tutorial mlelr:
software in C for teaching purposes
