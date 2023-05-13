Vapnik--Chervonenkis theory (also known as VC theory) was developed
during 1960--1990 by Vladimir Vapnik and Alexey Chervonenkis. The theory
is a form of computational learning theory, which attempts to explain
the learning process from a statistical point of view. Introduction VC
theory covers at least four parts (as explained in The Nature of
Statistical Learning Theory): Theory of consistency of learning
processes What are (necessary and sufficient) conditions for consistency
of a learning process based on the empirical risk minimization
principle? Nonasymptotic theory of the rate of convergence of learning
processes How fast is the rate of convergence of the learning process?
Theory of controlling the generalization ability of learning processes
How can one control the rate of convergence (the generalization ability)
of the learning process? Theory of constructing learning machines How
can one construct algorithms that can control the generalization
ability?VC Theory is a major subbranch of statistical learning theory.
One of its main applications in statistical learning theory is to
provide generalization conditions for learning algorithms. From this
point of view, VC theory is related to stability, which is an
alternative approach for characterizing generalization. In addition, VC
theory and VC dimension are instrumental in the theory of empirical
processes, in the case of processes indexed by VC classes. Arguably
these are the most important applications of the VC theory, and are
employed in proving generalization. Several techniques will be
introduced that are widely used in the empirical process and VC theory.
The discussion is mainly based on the book Weak Convergence and
Empirical Processes: With Applications to Statistics. Overview of VC
theory in empirical processes Background on empirical processes Let ( X
, A ) {\\displaystyle ({\\mathcal {X}},{\\mathcal {A}})} be a measurable
space. For any measure Q {\\displaystyle Q} on ( X , A ) {\\displaystyle
({\\mathcal {X}},{\\mathcal {A}})} , and any measurable functions f : X
→ R {\\displaystyle f:{\\mathcal {X}}\\to \\mathbf {R} } , define Q f =
∫ f d Q {\\displaystyle Qf=\\int fdQ} Measurability issues will be
ignored here, for more technical detail see. Let F {\\displaystyle
{\\mathcal {F}}} be a class of measurable functions f : X → R
{\\displaystyle f:{\\mathcal {X}}\\to \\mathbf {R} } and define: ‖ Q ‖ F
= sup { \| Q f \| : f ∈ F } . {\\displaystyle \\\|Q\\\|\_{\\mathcal
{F}}=\\sup\\{\\vert Qf\\vert \\ :\\ f\\in {\\mathcal {F}}\\}.} Let X 1 ,
... , X n {\\displaystyle X\_{1},\\ldots ,X\_{n}} be independent,
identically distributed random elements of ( X , A ) {\\displaystyle
({\\mathcal {X}},{\\mathcal {A}})} . Then define the empirical measure P
n = n − 1 ∑ i = 1 n δ X i , {\\displaystyle \\mathbb {P}
\_{n}=n\^{-1}\\sum \_{i=1}\^{n}\\delta \_{X\_{i}},} where δ here stands
for the Dirac measure. The empirical measure induces a map F → R
{\\displaystyle {\\mathcal {F}}\\to \\mathbf {R} } given by: f ↦ P n f =
1 n ( f ( X 1 ) + . . . + f ( X n ) ) {\\displaystyle f\\mapsto \\mathbb
{P} \_{n}f={\\frac {1}{n}}(f(X\_{1})+\...+f(X\_{n}))} Now suppose P is
the underlying true distribution of the data, which is unknown.
Empirical Processes theory aims at identifying classes F {\\displaystyle
{\\mathcal {F}}} for which statements such as the following hold:
uniform law of large numbers: ‖ P n − P ‖ F → n 0 , {\\displaystyle
\\\|\\mathbb {P} \_{n}-P\\\|\_{\\mathcal {F}}{\\underset {n}{\\to }}0,}
That is, as n → ∞ {\\displaystyle n\\to \\infty } , \| 1 n ( f ( X 1 ) +
. . . + f ( X n ) ) − ∫ f d P \| → 0 {\\displaystyle \\left\|{\\frac
{1}{n}}(f(X\_{1})+\...+f(X\_{n}))-\\int fdP\\right\|\\to 0} uniformly
for all f ∈ F {\\displaystyle f\\in {\\mathcal {F}}} .uniform central
limit theorem: G n = n ( P n − P ) ⇝ G , in ℓ ∞ ( F ) {\\displaystyle
\\mathbb {G} \_{n}={\\sqrt {n}}(\\mathbb {P} \_{n}-P)\\rightsquigarrow
\\mathbb {G} ,\\quad {\\text{in }}\\ell \^{\\infty }({\\mathcal {F}})}
In the former case F {\\displaystyle {\\mathcal {F}}} is called
Glivenko--Cantelli class, and in the latter case (under the assumption ∀
x , sup f ∈ F \| f ( x ) − P f \| \< ∞ {\\displaystyle \\forall x,\\sup
\\nolimits \_{f\\in {\\mathcal {F}}}\\vert f(x)-Pf\\vert \<\\infty } )
the class F {\\displaystyle {\\mathcal {F}}} is called Donsker or
P-Donsker. A Donsker class is Glivenko--Cantelli in probability by an
application of Slutsky\'s theorem . These statements are true for a
single f {\\displaystyle f} , by standard LLN, CLT arguments under
regularity conditions, and the difficulty in the Empirical Processes
comes in because joint statements are being made for all f ∈ F
{\\displaystyle f\\in {\\mathcal {F}}} . Intuitively then, the set F
{\\displaystyle {\\mathcal {F}}} cannot be too large, and as it turns
out that the geometry of F {\\displaystyle {\\mathcal {F}}} plays a very
important role. One way of measuring how big the function set F
{\\displaystyle {\\mathcal {F}}} is to use the so-called covering
numbers. The covering number N ( ε , F , ‖ ⋅ ‖ ) {\\displaystyle
N(\\varepsilon ,{\\mathcal {F}},\\\|\\cdot \\\|)} is the minimal number
of balls { g : ‖ g − f ‖ \< ε } {\\displaystyle
\\{g:\\\|g-f\\\|\<\\varepsilon \\}} needed to cover the set F
{\\displaystyle {\\mathcal {F}}} (here it is obviously assumed that
there is an underlying norm on F {\\displaystyle {\\mathcal {F}}} ). The
entropy is the logarithm of the covering number. Two sufficient
conditions are provided below, under which it can be proved that the set
F {\\displaystyle {\\mathcal {F}}} is Glivenko--Cantelli or Donsker. A
class F {\\displaystyle {\\mathcal {F}}} is P-Glivenko--Cantelli if it
is P-measurable with envelope F such that P ∗ F \< ∞ {\\displaystyle
P\^{\\ast }F\<\\infty } and satisfies: ∀ ε \> 0 sup Q N ( ε ‖ F ‖ Q , F
, L 1 ( Q ) ) \< ∞ . {\\displaystyle \\forall \\varepsilon \>0\\quad
\\sup \\nolimits \_{Q}N(\\varepsilon \\\|F\\\|\_{Q},{\\mathcal
{F}},L\_{1}(Q))\<\\infty .} The next condition is a version of the
celebrated Dudley\'s theorem. If F {\\displaystyle {\\mathcal {F}}} is a
class of functions such that ∫ 0 ∞ sup Q log ⁡ N ( ε ‖ F ‖ Q , 2 , F , L
2 ( Q ) ) d ε \< ∞ {\\displaystyle \\int \_{0}\^{\\infty }\\sup
\\nolimits \_{Q}{\\sqrt {\\log N\\left(\\varepsilon
\\\|F\\\|\_{Q,2},{\\mathcal {F}},L\_{2}(Q)\\right)}}d\\varepsilon
\<\\infty } then F {\\displaystyle {\\mathcal {F}}} is P-Donsker for
every probability measure P such that P ∗ F 2 \< ∞ {\\displaystyle
P\^{\\ast }F\^{2}\<\\infty } . In the last integral, the notation means
‖ f ‖ Q , 2 = ( ∫ \| f \| 2 d Q ) 1 2 {\\displaystyle
\\\|f\\\|\_{Q,2}=\\left(\\int \|f\|\^{2}dQ\\right)\^{\\frac {1}{2}}} .
Symmetrization The majority of the arguments of how to bound the
empirical process, rely on symmetrization, maximal and concentration
inequalities and chaining. Symmetrization is usually the first step of
the proofs, and since it is used in many machine learning proofs on
bounding empirical loss functions (including the proof of the VC
inequality which is discussed in the next section) it is presented here.
Consider the empirical process: f ↦ ( P n − P ) f = 1 n ∑ i = 1 n ( f (
X i ) − P f ) {\\displaystyle f\\mapsto (\\mathbb {P} \_{n}-P)f={\\dfrac
{1}{n}}\\sum \_{i=1}\^{n}(f(X\_{i})-Pf)} Turns out that there is a
connection between the empirical and the following symmetrized process:
f ↦ P n 0 f = 1 n ∑ i = 1 n ε i f ( X i ) {\\displaystyle f\\mapsto
\\mathbb {P} \_{n}\^{0}f={\\dfrac {1}{n}}\\sum \_{i=1}\^{n}\\varepsilon
\_{i}f(X\_{i})} The symmetrized process is a Rademacher process,
conditionally on the data X i {\\displaystyle X\_{i}} . Therefore, it is
a sub-Gaussian process by Hoeffding\'s inequality. Lemma
(Symmetrization). For every nondecreasing, convex Φ: R → R and class of
measurable functions F {\\displaystyle {\\mathcal {F}}} , E Φ ( ‖ P n −
P ‖ F ) ≤ E Φ ( 2 ‖ P n 0 ‖ F ) {\\displaystyle \\mathbb {E} \\Phi
(\\\|\\mathbb {P} \_{n}-P\\\|\_{\\mathcal {F}})\\leq \\mathbb {E} \\Phi
\\left(2\\left\\\|\\mathbb {P} \_{n}\^{0}\\right\\\|\_{\\mathcal
{F}}\\right)} The proof of the Symmetrization lemma relies on
introducing independent copies of the original variables X i
{\\displaystyle X\_{i}} (sometimes referred to as a ghost sample) and
replacing the inner expectation of the LHS by these copies. After an
application of Jensen\'s inequality different signs could be introduced
(hence the name symmetrization) without changing the expectation. The
proof can be found below because of its instructive nature. A typical
way of proving empirical CLTs, first uses symmetrization to pass the
empirical process to P n 0 {\\displaystyle \\mathbb {P} \_{n}\^{0}} and
then argue conditionally on the data, using the fact that Rademacher
processes are simple processes with nice properties. VC Connection It
turns out that there is a fascinating connection between certain
combinatorial properties of the set F {\\displaystyle {\\mathcal {F}}}
and the entropy numbers. Uniform covering numbers can be controlled by
the notion of Vapnik--Chervonenkis classes of sets -- or shortly VC
sets. Consider a collection C {\\displaystyle {\\mathcal {C}}} of
subsets of the sample space X {\\displaystyle {\\mathcal {X}}} . C
{\\displaystyle {\\mathcal {C}}} is said to pick out a certain subset W
{\\displaystyle W} of the finite set S = { x 1 , ... , x n } ⊂ X
{\\displaystyle S=\\{x\_{1},\\ldots ,x\_{n}\\}\\subset {\\mathcal {X}}}
if W = S ∩ C {\\displaystyle W=S\\cap C} for some C ∈ C {\\displaystyle
C\\in {\\mathcal {C}}} . C {\\displaystyle {\\mathcal {C}}} is said to
shatter S if it picks out each of its 2n subsets. The VC-index (similar
to VC dimension + 1 for an appropriately chosen classifier set) V ( C )
{\\displaystyle V({\\mathcal {C}})} of C {\\displaystyle {\\mathcal
{C}}} is the smallest n for which no set of size n is shattered by C
{\\displaystyle {\\mathcal {C}}} . Sauer\'s lemma then states that the
number Δ n ( C , x 1 , ... , x n ) {\\displaystyle \\Delta
\_{n}({\\mathcal {C}},x\_{1},\\ldots ,x\_{n})} of subsets picked out by
a VC-class C {\\displaystyle {\\mathcal {C}}} satisfies: max x 1 , ... ,
x n Δ n ( C , x 1 , ... , x n ) ≤ ∑ j = 0 V ( C ) − 1 ( n j ) ≤ ( n e V
( C ) − 1 ) V ( C ) − 1 {\\displaystyle \\max \_{x\_{1},\\ldots
,x\_{n}}\\Delta \_{n}({\\mathcal {C}},x\_{1},\\ldots ,x\_{n})\\leq \\sum
\_{j=0}\^{V({\\mathcal {C}})-1}{n \\choose j}\\leq \\left({\\frac
{ne}{V({\\mathcal {C}})-1}}\\right)\^{V({\\mathcal {C}})-1}} Which is a
polynomial number O ( n V ( C ) − 1 ) {\\displaystyle O(n\^{V({\\mathcal
{C}})-1})} of subsets rather than an exponential number. Intuitively
this means that a finite VC-index implies that C {\\displaystyle
{\\mathcal {C}}} has an apparent simplistic structure. A similar bound
can be shown (with a different constant, same rate) for the so-called VC
subgraph classes. For a function f : X → R {\\displaystyle f:{\\mathcal
{X}}\\to \\mathbf {R} } the subgraph is a subset of X × R
{\\displaystyle {\\mathcal {X}}\\times \\mathbf {R} } such that: { ( x ,
t ) : t \< f ( x ) } {\\displaystyle \\{(x,t):t 0 a i ( f ( x i ) − t i
) = ∑ a i \< 0 ( − a i ) ( f ( x i ) − t i ) , ∀ f ∈ F {\\displaystyle
\\sum \_{a\_{i}\>0}a\_{i}(f(x\_{i})-t\_{i})=\\sum
\_{a\_{i}\<0}(-a\_{i})(f(x\_{i})-t\_{i}),\\quad \\forall f\\in
{\\mathcal {F}}} Consider the set S = { ( x i , t i ) : a i \> 0 }
{\\displaystyle S=\\{(x\_{i},t\_{i}):a\_{i}\>0\\}} . This set cannot be
picked out since if there is some f {\\displaystyle f} such that S = { (
x i , t i ) : f ( x i ) \> t i } {\\displaystyle
S=\\{(x\_{i},t\_{i}):f(x\_{i})\>t\_{i}\\}} that would imply that the LHS
is strictly positive but the RHS is non-positive. There are
generalizations of the notion VC subgraph class, e.g. there is the
notion of pseudo-dimension. The interested reader can look into. VC
inequality A similar setting is considered, which is more common to
machine learning. Let X {\\displaystyle {\\mathcal {X}}} is a feature
space and Y = { 0 , 1 } {\\displaystyle {\\mathcal {Y}}=\\{0,1\\}} . A
function f : X → Y {\\displaystyle f:{\\mathcal {X}}\\to {\\mathcal
{Y}}} is called a classifier. Let F {\\displaystyle {\\mathcal {F}}} be
a set of classifiers. Similarly to the previous section, define the
shattering coefficient (also known as growth function): S ( F , n ) =
max x 1 , ... , x n \| { ( f ( x 1 ) , ... , f ( x n ) ) , f ∈ F } \|
{\\displaystyle S({\\mathcal {F}},n)=\\max \_{x\_{1},\\ldots
,x\_{n}}\|\\{(f(x\_{1}),\\ldots ,f(x\_{n})),f\\in {\\mathcal {F}}\\}\|}
Note here that there is a 1:1 go between each of the functions in F
{\\displaystyle {\\mathcal {F}}} and the set on which the function is 1.
We can thus define C {\\displaystyle {\\mathcal {C}}} to be the
collection of subsets obtained from the above mapping for every f ∈ F
{\\displaystyle f\\in {\\mathcal {F}}} . Therefore, in terms of the
previous section the shattering coefficient is precisely max x 1 , ... ,
x n Δ n ( C , x 1 , ... , x n ) {\\displaystyle \\max \_{x\_{1},\\ldots
,x\_{n}}\\Delta \_{n}({\\mathcal {C}},x\_{1},\\ldots ,x\_{n})} .This
equivalence together with Sauer\'s Lemma implies that S ( F , n )
{\\displaystyle S({\\mathcal {F}},n)} is going to be polynomial in n,
for sufficiently large n provided that the collection C {\\displaystyle
{\\mathcal {C}}} has a finite VC-index. Let D n = { ( X 1 , Y 1 ) , ...
, ( X n , Y m ) } {\\displaystyle D\_{n}=\\{(X\_{1},Y\_{1}),\\ldots
,(X\_{n},Y\_{m})\\}} is an observed dataset. Assume that the data is
generated by an unknown probability distribution P X Y {\\displaystyle
P\_{XY}} . Define R ( f ) = P ( f ( X ) ≠ Y ) {\\displaystyle
R(f)=P(f(X)\\neq Y)} to be the expected 0/1 loss. Of course since P X Y
{\\displaystyle P\_{XY}} is unknown in general, one has no access to R (
f ) {\\displaystyle R(f)} . However the empirical risk, given by: R \^ n
( f ) = 1 n ∑ i = 1 n I ( f ( X i ) ≠ Y i ) {\\displaystyle {\\hat
{R}}\_{n}(f)={\\dfrac {1}{n}}\\sum \_{i=1}\^{n}\\mathbb {I}
(f(X\_{i})\\neq Y\_{i})} can certainly be evaluated. Then one has the
following Theorem: Theorem (VC Inequality) For binary classification and
the 0/1 loss function we have the following generalization bounds: P (
sup f ∈ F \| R \^ n ( f ) − R ( f ) \| \> ε ) ≤ 8 S ( F , n ) e − n ε 2
/ 32 E \[ sup f ∈ F \| R \^ n ( f ) − R ( f ) \| \] ≤ 2 log ⁡ S ( F , n
) + log ⁡ 2 n {\\displaystyle {\\begin{aligned}P\\left(\\sup \_{f\\in
{\\mathcal {F}}}\\left\|{\\hat {R}}\_{n}(f)-R(f)\\right\|\>\\varepsilon
\\right)&\\leq 8S({\\mathcal {F}},n)e\^{-n\\varepsilon
\^{2}/32}\\\\\\mathbb {E} \\left\[\\sup \_{f\\in {\\mathcal
{F}}}\\left\|{\\hat {R}}\_{n}(f)-R(f)\\right\|\\right\]&\\leq 2{\\sqrt
{\\dfrac {\\log S({\\mathcal {F}},n)+\\log 2}{n}}}\\end{aligned}}} In
words the VC inequality is saying that as the sample increases, provided
that F {\\displaystyle {\\mathcal {F}}} has a finite VC dimension, the
empirical 0/1 risk becomes a good proxy for the expected 0/1 risk. Note
that both RHS of the two inequalities will converge to 0, provided that
S ( F , n ) {\\displaystyle S({\\mathcal {F}},n)} grows polynomially in
n. The connection between this framework and the Empirical Process
framework is evident. Here one is dealing with a modified empirical
process \| R \^ n − R \| F {\\displaystyle \\left\|{\\hat
{R}}\_{n}-R\\right\|\_{\\mathcal {F}}} but not surprisingly the ideas
are the same. The proof of the (first part of) VC inequality, relies on
symmetrization, and then argue conditionally on the data using
concentration inequalities (in particular Hoeffding\'s inequality). The
interested reader can check the book Theorems 12.4 and 12.5. References
See references in articles: Richard M. Dudley, empirical processes,
Shattered set. Bousquet, Olivier; Elisseeff, Andr´e (1 March 2002).
\"Stability and Generalization\". The Journal of Machine Learning
Research. 2: 499--526. doi:10.1162/153244302760200704. Retrieved 10
December 2022. Vapnik, V.; Chervonenkis, A. (2004). \"On the Uniform
Convergence of Relative Frequencies of Events to Their Probabilities\".
Theory Probab. Appl. 16 (2): 264--280. doi:10.1137/1116025.
