In machine learning and mathematical optimization, loss functions for
classification are computationally feasible loss functions representing
the price paid for inaccuracy of predictions in classification problems
(problems of identifying which category a particular observation belongs
to). Given X {\\displaystyle {\\mathcal {X}}} as the space of all
possible inputs (usually X ⊂ R d {\\displaystyle {\\mathcal {X}}\\subset
\\mathbb {R} \^{d}} ), and Y = { − 1 , 1 } {\\displaystyle {\\mathcal
{Y}}=\\{-1,1\\}} as the set of labels (possible outputs), a typical goal
of classification algorithms is to find a function f : X → Y
{\\displaystyle f:{\\mathcal {X}}\\to {\\mathcal {Y}}} which best
predicts a label y {\\displaystyle y} for a given input x →
{\\displaystyle {\\vec {x}}} . However, because of incomplete
information, noise in the measurement, or probabilistic components in
the underlying process, it is possible for the same x → {\\displaystyle
{\\vec {x}}} to generate different y {\\displaystyle y} . As a result,
the goal of the learning problem is to minimize expected loss (also
known as the risk), defined as I \[ f \] = ∫ X × Y V ( f ( x → ) , y ) p
( x → , y ) d x → d y {\\displaystyle I\[f\]=\\displaystyle \\int
\_{{\\mathcal {X}}\\times {\\mathcal {Y}}}V(f({\\vec {x}}),y)\\,p({\\vec
{x}},y)\\,d{\\vec {x}}\\,dy} where V ( f ( x → ) , y ) {\\displaystyle
V(f({\\vec {x}}),y)} is a given loss function, and p ( x → , y )
{\\displaystyle p({\\vec {x}},y)} is the probability density function of
the process that generated the data, which can equivalently be written
as p ( x → , y ) = p ( y ∣ x → ) p ( x → ) . {\\displaystyle p({\\vec
{x}},y)=p(y\\mid {\\vec {x}})p({\\vec {x}}).} Within classification,
several commonly used loss functions are written solely in terms of the
product of the true label y {\\displaystyle y} and the predicted label f
( x → ) {\\displaystyle f({\\vec {x}})} . Therefore, they can be defined
as functions of only one variable υ = y f ( x → ) {\\displaystyle
\\upsilon =yf({\\vec {x}})} , so that V ( f ( x → ) , y ) = ϕ ( y f ( x
→ ) ) = ϕ ( υ ) {\\displaystyle V(f({\\vec {x}}),y)=\\phi (yf({\\vec
{x}}))=\\phi (\\upsilon )} with a suitably chosen function ϕ : R → R
{\\displaystyle \\phi :\\mathbb {R} \\to \\mathbb {R} } . These are
called margin-based loss functions. Choosing a margin-based loss
function amounts to choosing ϕ {\\displaystyle \\phi } . Selection of a
loss function within this framework impacts the optimal f ϕ ∗
{\\displaystyle f\_{\\phi }\^{\*}} which minimizes the expected risk. In
the case of binary classification, it is possible to simplify the
calculation of expected risk from the integral specified above.
Specifically, I \[ f \] = ∫ X × Y V ( f ( x → ) , y ) p ( x → , y ) d x
→ d y = ∫ X ∫ Y ϕ ( y f ( x → ) ) p ( y ∣ x → ) p ( x → ) d y d x → = ∫
X \[ ϕ ( f ( x → ) ) p ( 1 ∣ x → ) + ϕ ( − f ( x → ) ) p ( − 1 ∣ x → )
\] p ( x → ) d x → = ∫ X \[ ϕ ( f ( x → ) ) p ( 1 ∣ x → ) + ϕ ( − f ( x
→ ) ) ( 1 − p ( 1 ∣ x → ) ) \] p ( x → ) d x → {\\displaystyle
{\\begin{aligned}I\[f\]&=\\int \_{{\\mathcal {X}}\\times {\\mathcal
{Y}}}V(f({\\vec {x}}),y)\\,p({\\vec {x}},y)\\,d{\\vec
{x}}\\,dy\\\\\[6pt\]&=\\int \_{\\mathcal {X}}\\int \_{\\mathcal
{Y}}\\phi (yf({\\vec {x}}))\\,p(y\\mid {\\vec {x}})\\,p({\\vec
{x}})\\,dy\\,d{\\vec {x}}\\\\\[6pt\]&=\\int \_{\\mathcal {X}}\[\\phi
(f({\\vec {x}}))\\,p(1\\mid {\\vec {x}})+\\phi (-f({\\vec
{x}}))\\,p(-1\\mid {\\vec {x}})\]\\,p({\\vec {x}})\\,d{\\vec
{x}}\\\\\[6pt\]&=\\int \_{\\mathcal {X}}\[\\phi (f({\\vec
{x}}))\\,p(1\\mid {\\vec {x}})+\\phi (-f({\\vec {x}}))\\,(1-p(1\\mid
{\\vec {x}}))\]\\,p({\\vec {x}})\\,d{\\vec {x}}\\end{aligned}}} The
second equality follows from the properties described above. The third
equality follows from the fact that 1 and −1 are the only possible
values for y {\\displaystyle y} , and the fourth because p ( − 1 ∣ x ) =
1 − p ( 1 ∣ x ) {\\displaystyle p(-1\\mid x)=1-p(1\\mid x)} . The term
within brackets \[ ϕ ( f ( x → ) ) p ( 1 ∣ x → ) + ϕ ( − f ( x → ) ) ( 1
− p ( 1 ∣ x → ) ) \] {\\displaystyle \[\\phi (f({\\vec {x}}))p(1\\mid
{\\vec {x}})+\\phi (-f({\\vec {x}}))(1-p(1\\mid {\\vec {x}}))\]} is
known as the conditional risk. One can solve for the minimizer of I \[ f
\] {\\displaystyle I\[f\]} by taking the functional derivative of the
last equality with respect to f {\\displaystyle f} and setting the
derivative equal to 0. This will result in the following equation ∂ ϕ (
f ) ∂ f η + ∂ ϕ ( − f ) ∂ f ( 1 − η ) = 0 ( 1 ) {\\displaystyle {\\frac
{\\partial \\phi (f)}{\\partial f}}\\eta +{\\frac {\\partial \\phi
(-f)}{\\partial f}}(1-\\eta )=0\\;\\;\\;\\;\\;(1)} which is also
equivalent to setting the derivative of the conditional risk equal to
zero. Given the binary nature of classification, a natural selection for
a loss function (assuming equal cost for false positives and false
negatives) would be the 0-1 loss function (0--1 indicator function),
which takes the value of 0 if the predicted classification equals that
of the true class or a 1 if the predicted classification does not match
the true class. This selection is modeled by V ( f ( x → ) , y ) = H ( −
y f ( x → ) ) {\\displaystyle V(f({\\vec {x}}),y)=H(-yf({\\vec {x}}))}
where H {\\displaystyle H} indicates the Heaviside step function.
However, this loss function is non-convex and non-smooth, and solving
for the optimal solution is an NP-hard combinatorial optimization
problem. As a result, it is better to substitute loss function
surrogates which are tractable for commonly used learning algorithms, as
they have convenient properties such as being convex and smooth. In
addition to their computational tractability, one can show that the
solutions to the learning problem using these loss surrogates allow for
the recovery of the actual solution to the original classification
problem. Some of these surrogates are described below. In practice, the
probability distribution p ( x → , y ) {\\displaystyle p({\\vec {x}},y)}
is unknown. Consequently, utilizing a training set of n {\\displaystyle
n} independently and identically distributed sample points S = { ( x → 1
, y 1 ) , ... , ( x → n , y n ) } {\\displaystyle S=\\{({\\vec
{x}}\_{1},y\_{1}),\\dots ,({\\vec {x}}\_{n},y\_{n})\\}} drawn from the
data sample space, one seeks to minimize empirical risk I S \[ f \] = 1
n ∑ i = 1 n V ( f ( x → i ) , y i ) {\\displaystyle I\_{S}\[f\]={\\frac
{1}{n}}\\sum \_{i=1}\^{n}V(f({\\vec {x}}\_{i}),y\_{i})} as a proxy for
expected risk. (See statistical learning theory for a more detailed
description.) Bayes consistency Utilizing Bayes\' theorem, it can be
shown that the optimal f 0 / 1 ∗ {\\displaystyle f\_{0/1}\^{\*}} , i.e.,
the one that minimizes the expected risk associated with the zero-one
loss, implements the Bayes optimal decision rule for a binary
classification problem and is in the form of f 0 / 1 ∗ ( x → ) = { 1 if
p ( 1 ∣ x → ) \> p ( − 1 ∣ x → ) 0 if p ( 1 ∣ x → ) = p ( − 1 ∣ x → ) −
1 if p ( 1 ∣ x → ) \< p ( − 1 ∣ x → ) {\\displaystyle
f\_{0/1}\^{\*}({\\vec {x}})\\;=\\;{\\begin{cases}\\;\\;\\;1&{\\text{if
}}p(1\\mid {\\vec {x}})\>p(-1\\mid {\\vec {x}})\\\\\\;\\;\\;0&{\\text{if
}}p(1\\mid {\\vec {x}})=p(-1\\mid {\\vec {x}})\\\\-1&{\\text{if
}}p(1\\mid {\\vec {x}}) p ( − 1 ∣ x → ) − 1 if p ( 1 ∣ x → ) \< p ( − 1
∣ x → ) {\\displaystyle f\_{\\text{Hinge}}\^{\*}({\\vec
{x}})\\;=\\;{\\begin{cases}1&{\\text{if }}p(1\\mid {\\vec
{x}})\>p(-1\\mid {\\vec {x}})\\\\-1&{\\text{if }}p(1\\mid {\\vec {x}})
