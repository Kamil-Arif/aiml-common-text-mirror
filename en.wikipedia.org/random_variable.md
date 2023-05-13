A random variable (also called random quantity, aleatory variable, or
stochastic variable) is a mathematical formalization of a quantity or
object which depends on random events. The term \'random variable\' can
be misleading as it is not actually random or a variable, but rather it
is a mapping or a function from possible outcomes (e.g., the possible
upper sides of a flipped coin such as heads H {\\displaystyle H} and
tails T {\\displaystyle T} ) in a sample space (e.g., the set { H , T }
{\\displaystyle \\{H,T\\}} ) to a measurable space (e.g., { − 1 , 1 }
{\\displaystyle \\{-1,1\\}} in which 1 corresponding to H
{\\displaystyle H} and −1 corresponding to T {\\displaystyle T} ), often
to the real numbers. Informally, randomness typically represents some
fundamental element of chance, such as in the roll of a dice; it may
also represent uncertainty, such as measurement error. However, the
interpretation of probability is philosophically complicated, and even
in specific cases is not always straightforward. The purely mathematical
analysis of random variables is independent of such interpretational
difficulties, and can be based upon a rigorous axiomatic setup. In the
formal mathematical language of measure theory, a random variable is
defined as a measurable function from a probability measure space
(called the sample space) to a measurable space. This allows
consideration of the pushforward measure, which is called the
distribution of the random variable; the distribution is thus a
probability measure on the set of all possible values of the random
variable. It is possible for two random variables to have identical
distributions but to differ in significant ways; for instance, they may
be independent. It is common to consider the special cases of discrete
random variables and absolutely continuous random variables,
corresponding to whether a random variable is valued in a discrete set
(such as a finite set) or in an interval of real numbers. There are
other important possibilities, especially in the theory of stochastic
processes, wherein it is natural to consider random sequences or random
functions. Sometimes a random variable is taken to be automatically
valued in the real numbers, with more general random quantities instead
being called random elements. According to George Mackey, Pafnuty
Chebyshev was the first person \"to think systematically in terms of
random variables\". Definition A random variable X {\\displaystyle X} is
a measurable function X : Ω → E {\\displaystyle X\\colon \\Omega \\to E}
from a sample space Ω {\\displaystyle \\Omega } as a set of possible
outcomes to a measurable space E {\\displaystyle E} . The technical
axiomatic definition requires the sample space Ω {\\displaystyle \\Omega
} to be a sample space of a probability triple ( Ω , F , P )
{\\displaystyle (\\Omega ,{\\mathcal {F}},\\operatorname {P} )} (see the
measure-theoretic definition). A random variable is often denoted by
capital Roman letters such as X , Y , Z , T {\\displaystyle X,Y,Z,T}
.The probability that X {\\displaystyle X} takes on a value in a
measurable set S ⊆ E {\\displaystyle S\\subseteq E} is written as P ⁡ ( X
∈ S ) = P ⁡ ( { ω ∈ Ω ∣ X ( ω ) ∈ S } ) {\\displaystyle \\operatorname
{P} (X\\in S)=\\operatorname {P} (\\{\\omega \\in \\Omega \\mid
X(\\omega )\\in S\\})} Standard case In many cases, X {\\displaystyle X}
is real-valued, i.e. E = R {\\displaystyle E=\\mathbb {R} } . In some
contexts, the term random element (see extensions) is used to denote a
random variable not of this form. When the image (or range) of X
{\\displaystyle X} is countable, the random variable is called a
discrete random variable: 399  and its distribution is a discrete
probability distribution, i.e. can be described by a probability mass
function that assigns a probability to each value in the image of X
{\\displaystyle X} . If the image is uncountably infinite (usually an
interval) then X {\\displaystyle X} is called a continuous random
variable. In the special case that it is absolutely continuous, its
distribution can be described by a probability density function, which
assigns probabilities to intervals; in particular, each individual point
must necessarily have probability zero for an absolutely continuous
random variable. Not all continuous random variables are absolutely
continuous, a mixture distribution is one such counterexample; such
random variables cannot be described by a probability density or a
probability mass function. Any random variable can be described by its
cumulative distribution function, which describes the probability that
the random variable will be less than or equal to a certain value.
Extensions The term \"random variable\" in statistics is traditionally
limited to the real-valued case ( E = R {\\displaystyle E=\\mathbb {R} }
). In this case, the structure of the real numbers makes it possible to
define quantities such as the expected value and variance of a random
variable, its cumulative distribution function, and the moments of its
distribution. However, the definition above is valid for any measurable
space E {\\displaystyle E} of values. Thus one can consider random
elements of other sets E {\\displaystyle E} , such as random boolean
values, categorical values, complex numbers, vectors, matrices,
sequences, trees, sets, shapes, manifolds, and functions. One may then
specifically refer to a random variable of type E {\\displaystyle E} ,
or an E {\\displaystyle E} -valued random variable. This more general
concept of a random element is particularly useful in disciplines such
as graph theory, machine learning, natural language processing, and
other fields in discrete mathematics and computer science, where one is
often interested in modeling the random variation of non-numerical data
structures. In some cases, it is nonetheless convenient to represent
each element of E {\\displaystyle E} , using one or more real numbers.
In this case, a random element may optionally be represented as a vector
of real-valued random variables (all defined on the same underlying
probability space Ω {\\displaystyle \\Omega } , which allows the
different random variables to covary). For example: A random word may be
represented as a random integer that serves as an index into the
vocabulary of possible words. Alternatively, it can be represented as a
random indicator vector, whose length equals the size of the vocabulary,
where the only values of positive probability are ( 1 0 0 0 ⋯ )
{\\displaystyle (1\\ 0\\ 0\\ 0\\ \\cdots )} , ( 0 1 0 0 ⋯ )
{\\displaystyle (0\\ 1\\ 0\\ 0\\ \\cdots )} , ( 0 0 1 0 ⋯ )
{\\displaystyle (0\\ 0\\ 1\\ 0\\ \\cdots )} and the position of the 1
indicates the word. A random sentence of given length N {\\displaystyle
N} may be represented as a vector of N {\\displaystyle N} random words.
A random graph on N {\\displaystyle N} given vertices may be represented
as a N × N {\\displaystyle N\\times N} matrix of random variables, whose
values specify the adjacency matrix of the random graph. A random
function F {\\displaystyle F} may be represented as a collection of
random variables F ( x ) {\\displaystyle F(x)} , giving the function\'s
values at the various points x {\\displaystyle x} in the function\'s
domain. The F ( x ) {\\displaystyle F(x)} are ordinary real-valued
random variables provided that the function is real-valued. For example,
a stochastic process is a random function of time, a random vector is a
random function of some index set such as 1 , 2 , ... , n
{\\displaystyle 1,2,\\ldots ,n} , and random field is a random function
on any set (typically time, space, or a discrete set). Distribution
functions If a random variable X : Ω → R {\\displaystyle X\\colon
\\Omega \\to \\mathbb {R} } defined on the probability space ( Ω , F , P
) {\\displaystyle (\\Omega ,{\\mathcal {F}},\\operatorname {P} )} is
given, we can ask questions like \"How likely is it that the value of X
{\\displaystyle X} is equal to 2?\". This is the same as the probability
of the event { ω : X ( ω ) = 2 } {\\displaystyle \\{\\omega :X(\\omega
)=2\\}\\,\\!} which is often written as P ( X = 2 ) {\\displaystyle
P(X=2)\\,\\!} or p X ( 2 ) {\\displaystyle p\_{X}(2)} for short.
Recording all these probabilities of outputs of a random variable X
{\\displaystyle X} yields the probability distribution of X
{\\displaystyle X} . The probability distribution \"forgets\" about the
particular probability space used to define X {\\displaystyle X} and
only records the probabilities of various output values of X
{\\displaystyle X} . Such a probability distribution, if X
{\\displaystyle X} is real-valued, can always be captured by its
cumulative distribution function F X ( x ) = P ⁡ ( X ≤ x )
{\\displaystyle F\_{X}(x)=\\operatorname {P} (X\\leq x)} and sometimes
also using a probability density function, f X {\\displaystyle f\_{X}} .
In measure-theoretic terms, we use the random variable X {\\displaystyle
X} to \"push-forward\" the measure P {\\displaystyle P} on Ω
{\\displaystyle \\Omega } to a measure p X {\\displaystyle p\_{X}} on R
{\\displaystyle \\mathbb {R} } . The measure p X {\\displaystyle p\_{X}}
is called the \"(probability) distribution of X {\\displaystyle X} \" or
the \"law of X {\\displaystyle X} \". The density f X = d p X / d μ
{\\displaystyle f\_{X}=dp\_{X}/d\\mu } , the Radon--Nikodym derivative
of p X {\\displaystyle p\_{X}} with respect to some reference measure μ
{\\displaystyle \\mu } on R {\\displaystyle \\mathbb {R} } (often, this
reference measure is the Lebesgue measure in the case of continuous
random variables, or the counting measure in the case of discrete random
variables). The underlying probability space Ω {\\displaystyle \\Omega }
is a technical device used to guarantee the existence of random
variables, sometimes to construct them, and to define notions such as
correlation and dependence or independence based on a joint distribution
of two or more random variables on the same probability space. In
practice, one often disposes of the space Ω {\\displaystyle \\Omega }
altogether and just puts a measure on R {\\displaystyle \\mathbb {R} }
that assigns measure 1 to the whole real line, i.e., one works with
probability distributions instead of random variables. See the article
on quantile functions for fuller development. Examples Discrete random
variable In an experiment a person may be chosen at random, and one
random variable may be the person\'s height. Mathematically, the random
variable is interpreted as a function which maps the person to the
person\'s height. Associated with the random variable is a probability
distribution that allows the computation of the probability that the
height is in any subset of possible values, such as the probability that
the height is between 180 and 190 cm, or the probability that the height
is either less than 150 or more than 200 cm. Another random variable may
be the person\'s number of children; this is a discrete random variable
with non-negative integer values. It allows the computation of
probabilities for individual integer values -- the probability mass
function (PMF) -- or for sets of values, including infinite sets. For
example, the event of interest may be \"an even number of children\".
For both finite and infinite event sets, their probabilities can be
found by adding up the PMFs of the elements; that is, the probability of
an even number of children is the infinite sum PMF ⁡ ( 0 ) + PMF ⁡ ( 2 ) +
PMF ⁡ ( 4 ) + ⋯ {\\displaystyle \\operatorname {PMF} (0)+\\operatorname
{PMF} (2)+\\operatorname {PMF} (4)+\\cdots } . In examples such as
these, the sample space is often suppressed, since it is mathematically
hard to describe, and the possible values of the random variables are
then treated as a sample space. But when two random variables are
measured on the same sample space of outcomes, such as the height and
number of children being computed on the same random persons, it is
easier to track their relationship if it is acknowledged that both
height and number of children come from the same random person, for
example so that questions of whether such random variables are
correlated or not can be posed. If { a n } , { b n } {\\textstyle
\\{a\_{n}\\},\\{b\_{n}\\}} are countable sets of real numbers, b n \> 0
{\\textstyle b\_{n}\>0} and ∑ n b n = 1 {\\textstyle \\sum
\_{n}b\_{n}=1} , then F = ∑ n b n δ a n ( x ) {\\textstyle F=\\sum
\_{n}b\_{n}\\delta \_{a\_{n}}(x)} is a discrete distribution function.
Here δ t ( x ) = 0 {\\displaystyle \\delta \_{t}(x)=0} for x \< t
{\\displaystyle x 0 {\\displaystyle \\theta \>0} is a fixed parameter.
Consider the random variable Y = l o g ( 1 + e − X ) . {\\displaystyle
Y=\\mathrm {log} (1+e\^{-X}).} Then, F Y ( y ) = P ( Y ≤ y ) = P ( l o g
( 1 + e − X ) ≤ y ) = P ( X ≥ − l o g ( e y − 1 ) ) . {\\displaystyle
F\_{Y}(y)=P(Y\\leq y)=P(\\mathrm {log} (1+e\^{-X})\\leq y)=P(X\\geq
-\\mathrm {log} (e\^{y}-1)).\\,} The last expression can be calculated
in terms of the cumulative distribution of X , {\\displaystyle X,} so F
Y ( y ) = 1 − F X ( − log ⁡ ( e y − 1 ) ) = 1 − 1 ( 1 + e log ⁡ ( e y − 1
) ) θ = 1 − 1 ( 1 + e y − 1 ) θ = 1 − e − y θ . {\\displaystyle
{\\begin{aligned}F\_{Y}(y)&=1-F\_{X}(-\\log(e\^{y}-1))\\\\\[5pt\]&=1-{\\frac
{1}{(1+e\^{\\log(e\^{y}-1)})\^{\\theta }}}\\\\\[5pt\]&=1-{\\frac
{1}{(1+e\^{y}-1)\^{\\theta }}}\\\\\[5pt\]&=1-e\^{-y\\theta
}.\\end{aligned}}} which is the cumulative distribution function (CDF)
of an exponential distribution. Example 3 Suppose X {\\displaystyle X}
is a random variable with a standard normal distribution, whose density
is f X ( x ) = 1 2 π e − x 2 / 2 . {\\displaystyle f\_{X}(x)={\\frac
{1}{\\sqrt {2\\pi }}}e\^{-x\^{2}/2}.} Consider the random variable Y = X
2 . {\\displaystyle Y=X\^{2}.} We can find the density using the above
formula for a change of variables: f Y ( y ) = ∑ i f X ( g i − 1 ( y ) )
\| d g i − 1 ( y ) d y \| . {\\displaystyle f\_{Y}(y)=\\sum
\_{i}f\_{X}(g\_{i}\^{-1}(y))\\left\|{\\frac
{dg\_{i}\^{-1}(y)}{dy}}\\right\|.} In this case the change is not
monotonic, because every value of Y {\\displaystyle Y} has two
corresponding values of X {\\displaystyle X} (one positive and
negative). However, because of symmetry, both halves will transform
identically, i.e., f Y ( y ) = 2 f X ( g − 1 ( y ) ) \| d g − 1 ( y ) d
y \| . {\\displaystyle f\_{Y}(y)=2f\_{X}(g\^{-1}(y))\\left\|{\\frac
{dg\^{-1}(y)}{dy}}\\right\|.} The inverse transformation is x = g − 1 (
y ) = y {\\displaystyle x=g\^{-1}(y)={\\sqrt {y}}} and its derivative is
d g − 1 ( y ) d y = 1 2 y . {\\displaystyle {\\frac
{dg\^{-1}(y)}{dy}}={\\frac {1}{2{\\sqrt {y}}}}.} Then, f Y ( y ) = 2 1 2
π e − y / 2 1 2 y = 1 2 π y e − y / 2 . {\\displaystyle
f\_{Y}(y)=2{\\frac {1}{\\sqrt {2\\pi }}}e\^{-y/2}{\\frac {1}{2{\\sqrt
{y}}}}={\\frac {1}{\\sqrt {2\\pi y}}}e\^{-y/2}.} This is a chi-squared
distribution with one degree of freedom. Example 4 Suppose X
{\\displaystyle X} is a random variable with a normal distribution,
whose density is f X ( x ) = 1 2 π σ 2 e − ( x − μ ) 2 / ( 2 σ 2 ) .
{\\displaystyle f\_{X}(x)={\\frac {1}{\\sqrt {2\\pi \\sigma
\^{2}}}}e\^{-(x-\\mu )\^{2}/(2\\sigma \^{2})}.} Consider the random
variable Y = X 2 . {\\displaystyle Y=X\^{2}.} We can find the density
using the above formula for a change of variables: f Y ( y ) = ∑ i f X (
g i − 1 ( y ) ) \| d g i − 1 ( y ) d y \| . {\\displaystyle
f\_{Y}(y)=\\sum \_{i}f\_{X}(g\_{i}\^{-1}(y))\\left\|{\\frac
{dg\_{i}\^{-1}(y)}{dy}}\\right\|.} In this case the change is not
monotonic, because every value of Y {\\displaystyle Y} has two
corresponding values of X {\\displaystyle X} (one positive and
negative). Differently from the previous example, in this case however,
there is no symmetry and we have to compute the two distinct terms: f Y
( y ) = f X ( g 1 − 1 ( y ) ) \| d g 1 − 1 ( y ) d y \| + f X ( g 2 − 1
( y ) ) \| d g 2 − 1 ( y ) d y \| . {\\displaystyle
f\_{Y}(y)=f\_{X}(g\_{1}\^{-1}(y))\\left\|{\\frac
{dg\_{1}\^{-1}(y)}{dy}}\\right\|+f\_{X}(g\_{2}\^{-1}(y))\\left\|{\\frac
{dg\_{2}\^{-1}(y)}{dy}}\\right\|.} The inverse transformation is x = g 1
, 2 − 1 ( y ) = ± y {\\displaystyle x=g\_{1,2}\^{-1}(y)=\\pm {\\sqrt
{y}}} and its derivative is d g 1 , 2 − 1 ( y ) d y = ± 1 2 y .
{\\displaystyle {\\frac {dg\_{1,2}\^{-1}(y)}{dy}}=\\pm {\\frac
{1}{2{\\sqrt {y}}}}.} Then, f Y ( y ) = 1 2 π σ 2 1 2 y ( e − ( y − μ )
2 / ( 2 σ 2 ) + e − ( − y − μ ) 2 / ( 2 σ 2 ) ) . {\\displaystyle
f\_{Y}(y)={\\frac {1}{\\sqrt {2\\pi \\sigma \^{2}}}}{\\frac {1}{2{\\sqrt
{y}}}}(e\^{-({\\sqrt {y}}-\\mu )\^{2}/(2\\sigma \^{2})}+e\^{-(-{\\sqrt
{y}}-\\mu )\^{2}/(2\\sigma \^{2})}).} This is a noncentral chi-squared
distribution with one degree of freedom. Some properties The probability
distribution of the sum of two independent random variables is the
convolution of each of their distributions. Probability distributions
are not a vector space---they are not closed under linear combinations,
as these do not preserve non-negativity or total integral 1---but they
are closed under convex combination, thus forming a convex subset of the
space of functions (or measures). Equivalence of random variables There
are several different senses in which random variables can be considered
to be equivalent. Two random variables can be equal, equal almost
surely, or equal in distribution. In increasing order of strength, the
precise definition of these notions of equivalence is given below.
Equality in distribution If the sample space is a subset of the real
line, random variables X and Y are equal in distribution (denoted X = d
Y {\\displaystyle X{\\stackrel {d}{=}}Y} ) if they have the same
distribution functions: P ⁡ ( X ≤ x ) = P ⁡ ( Y ≤ x ) for all x .
{\\displaystyle \\operatorname {P} (X\\leq x)=\\operatorname {P} (Y\\leq
x)\\quad {\\text{for all }}x.} To be equal in distribution, random
variables need not be defined on the same probability space. Two random
variables having equal moment generating functions have the same
distribution. This provides, for example, a useful method of checking
equality of certain functions of independent, identically distributed
(IID) random variables. However, the moment generating function exists
only for distributions that have a defined Laplace transform. Almost
sure equality Two random variables X and Y are equal almost surely
(denoted X = a.s. Y {\\displaystyle X\\;{\\stackrel
{\\text{a.s.}}{=}}\\;Y} ) if, and only if, the probability that they are
different is zero: P ⁡ ( X ≠ Y ) = 0. {\\displaystyle \\operatorname {P}
(X\\neq Y)=0.} For all practical purposes in probability theory, this
notion of equivalence is as strong as actual equality. It is associated
to the following distance: d ∞ ( X , Y ) = ess ⁡ sup ω \| X ( ω ) − Y ( ω
) \| , {\\displaystyle d\_{\\infty }(X,Y)=\\operatorname {ess} \\sup
\_{\\omega }\|X(\\omega )-Y(\\omega )\|,} where \"ess sup\" represents
the essential supremum in the sense of measure theory. Equality Finally,
the two random variables X and Y are equal if they are equal as
functions on their measurable space: X ( ω ) = Y ( ω ) for all ω .
{\\displaystyle X(\\omega )=Y(\\omega )\\qquad {\\hbox{for all }}\\omega
.} This notion is typically the least useful in probability theory
because in practice and in theory, the underlying measure space of the
experiment is rarely explicitly characterized or even characterizable.
Convergence A significant theme in mathematical statistics consists of
obtaining convergence results for certain sequences of random variables;
for instance the law of large numbers and the central limit theorem.
There are various senses in which a sequence X n {\\displaystyle X\_{n}}
of random variables can converge to a random variable X {\\displaystyle
X} . These are explained in the article on convergence of random
variables. See also References Inline citations Literature External
links \"Random variable\", Encyclopedia of Mathematics, EMS Press, 2001
\[1994\] Zukerman, Moshe (2014), Introduction to Queueing Theory and
Stochastic Teletraffic Models (PDF), arXiv:1307.2968 Zukerman, Moshe
(2014), Basic Probability Topics (PDF)
