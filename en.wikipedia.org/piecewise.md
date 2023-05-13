In mathematics, a piecewise-defined function (also called a piecewise
function, a hybrid function, or definition by cases) is a function
defined by multiple sub-functions, where each sub-function applies to a
different interval in the domain. Piecewise definition is actually a way
of expressing the function, rather than a characteristic of the function
itself. A distinct, but related notion is that of a property holding
piecewise for a function, used when the domain can be divided into
intervals on which the property holds. Unlike for the notion above, this
is actually a property of the function itself. A piecewise linear
function (which happens to be also continuous) is depicted as an
example. Notation and interpretation Piecewise functions can be defined
using the common functional notation, where the body of the function is
an array of functions and associated subdomains. These subdomains
together must cover the whole domain; often it is also required that
they are pairwise disjoint, i.e. form a partition of the domain. In
order for the overall function to be called \"piecewise\", the
subdomains are usually required to be intervals (some may be degenerated
intervals, i.e. single points or unbounded intervals). For bounded
intervals, the number of subdomains is required to be finite, for
unbounded intervals it is often only required to be locally finite. For
example, consider the piecewise definition of the absolute value
function: For all values of x {\\displaystyle x} less than zero, the
first function ( − x {\\displaystyle -x} ) is used, which negates the
sign of the input value, making negative numbers positive. For all
values of x {\\displaystyle x} greater than or equal to zero, the second
function ( x {\\displaystyle x} ) is used, which evaluates trivially to
the input value itself. The following table documents the absolute value
function at certain values of x {\\displaystyle x} : Here, notice that
in order to evaluate a piecewise function at a given input value, the
appropriate subdomain needs to be chosen in order to select the correct
function---and produce the correct output value. Continuity and
differentiability of piecewise functions A piecewise function is
continuous on a given interval in its domain if the following conditions
are met: its constituent functions are continuous on the corresponding
intervals (subdomains), there is no discontinuity at each endpoint of
the subdomains within that interval.The pictured function, for example,
is piecewise-continuous throughout its subdomains, but is not continuous
on the entire domain, as it contains a jump discontinuity at x 0
{\\displaystyle x\_{0}} . The filled circle indicates that the value of
the right function piece is used in this position. For a piecewise
function to be differentiable on a given interval in its domain, the
following conditions have to fulfilled in addition to those for
continuity above: its constituent functions are differentiable on the
corresponding open intervals, the one-sided derivatives exist at all
intervals endpoints, at the points where two subintervals touch, the
corresponding one-sided derivatives of the two neighboring subintervals
coincide. Applications In applied mathematical analysis, piecewise
functions have been found to be consistent with many models of the human
visual system, where images are perceived at a first stage as consisting
of smooth regions separated by edges. In particular, shearlets have been
used as a representation system to provide sparse approximations of this
model class in 2D and 3D. Common examples Piecewise linear function, a
piecewise function composed of line segments Step function, a piecewise
function composed of constant functions Boxcar function, Heaviside step
function Sign function Absolute value Triangular function Broken power
law, a piecewise function composed of power laws Spline, a piecewise
function composed of polynomial functions, possessing a high degree of
smoothness at the places where the polynomial pieces connect B-spline
PDIFF f ( x ) = { exp ⁡ ( − 1 1 − x 2 ) , x ∈ ( − 1 , 1 ) 0 , otherwise
{\\displaystyle f(x)={\\begin{cases}\\exp \\left(-{\\frac
{1}{1-x\^{2}}}\\right),&x\\in
(-1,1)\\\\0,&{\\text{otherwise}}\\end{cases}}} and some other common
Bump functions. These are infinitely differentiable, but analyticity
holds only piecewise. Continuous functions in the reals need not be
bounded or uniformly continuous, but are always piecewise bounded and
piecewise uniformly continuous. See also Piecewise linear continuation
== References ==
