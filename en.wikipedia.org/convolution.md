In mathematics (in particular, functional analysis), convolution is a
mathematical operation on two functions (f and g) that produces a third
function ( f ∗ g {\\displaystyle f\*g} ) that expresses how the shape of
one is modified by the other. The term convolution refers to both the
result function and to the process of computing it. It is defined as the
integral of the product of the two functions after one is reflected
about the y-axis and shifted. The choice of which function is reflected
and shifted before the integral does not change the integral result (see
commutativity). The integral is evaluated for all values of shift,
producing the convolution function. Some features of convolution are
similar to cross-correlation: for real-valued functions, of a continuous
or discrete variable, convolution ( f ∗ g {\\displaystyle f\*g} )
differs from cross-correlation ( f ⋆ g {\\displaystyle f\\star g} ) only
in that either f(x) or g(x) is reflected about the y-axis in
convolution; thus it is a cross-correlation of g(−x) and f(x), or f(−x)
and g(x). For complex-valued functions, the cross-correlation operator
is the adjoint of the convolution operator. Convolution has applications
that include probability, statistics, acoustics, spectroscopy, signal
processing and image processing, geophysics, engineering, physics,
computer vision and differential equations.The convolution can be
defined for functions on Euclidean space and other groups (as algebraic
structures). For example, periodic functions, such as the discrete-time
Fourier transform, can be defined on a circle and convolved by periodic
convolution. (See row 18 at DTFT § Properties.) A discrete convolution
can be defined for functions on the set of integers. Generalizations of
convolution have applications in the field of numerical analysis and
numerical linear algebra, and in the design and implementation of finite
impulse response filters in signal processing.Computing the inverse of
the convolution operation is known as deconvolution. Definition The
convolution of f and g is written f∗g, denoting the operator with the
symbol ∗. It is defined as the integral of the product of the two
functions after one is reflected about the y-axis and shifted. As such,
it is a particular kind of integral transform: ( f ∗ g ) ( t ) := ∫ − ∞
∞ f ( τ ) g ( t − τ ) d τ . {\\displaystyle (f\*g)(t):=\\int \_{-\\infty
}\^{\\infty }f(\\tau )g(t-\\tau )\\,d\\tau .} An equivalent definition
is (see commutativity): ( f ∗ g ) ( t ) := ∫ − ∞ ∞ f ( t − τ ) g ( τ ) d
τ . {\\displaystyle (f\*g)(t):=\\int \_{-\\infty }\^{\\infty }f(t-\\tau
)g(\\tau )\\,d\\tau .} While the symbol t is used above, it need not
represent the time domain. At each t, the convolution formula can be
described as the area under the function f(τ) weighted by the function
g(−τ) shifted by the amount t. As t changes, the weighting function g(t
− τ) emphasizes different parts of the input function f(τ); If t is a
positive value, then g(t − τ) is equal to g(−τ) that slides or is
shifted along the τ {\\displaystyle \\tau } -axis toward the right
(toward +∞) by the amount of t, while if t is a negative value, then g(t
− τ) is equal to g(−τ) that slides or is shifted toward the left (toward
-∞) by the amount of \|t\|. For functions f, g supported on only \[0,
∞\] (i.e., zero for negative arguments), the integration limits can be
truncated, resulting in: ( f ∗ g ) ( t ) = ∫ 0 t f ( τ ) g ( t − τ ) d τ
for f , g : \[ 0 , ∞ ) → R . {\\displaystyle (f\*g)(t)=\\int
\_{0}\^{t}f(\\tau )g(t-\\tau )\\,d\\tau \\quad \\ {\\text{for
}}f,g:\[0,\\infty )\\to \\mathbb {R} .} For the multi-dimensional
formulation of convolution, see domain of definition (below). Notation A
common engineering notational convention is: f ( t ) ∗ g ( t ) := ∫ − ∞
∞ f ( τ ) g ( t − τ ) d τ ⏟ ( f ∗ g ) ( t ) , {\\displaystyle
f(t)\*g(t)\\mathrel {:=} \\underbrace {\\int \_{-\\infty }\^{\\infty
}f(\\tau )g(t-\\tau )\\,d\\tau } \_{(f\*g)(t)},} which has to be
interpreted carefully to avoid confusion. For instance, f(t)∗g(t − t0)
is equivalent to (f∗g)(t − t0), but f(t − t0)∗g(t − t0) is in fact
equivalent to (f∗g)(t − 2t0). Relations with other transforms Given two
functions f ( t ) {\\displaystyle f(t)} and g ( t ) {\\displaystyle
g(t)} with bilateral Laplace transforms (two-sided Laplace transform) F
( s ) = ∫ − ∞ ∞ e − s u f ( u ) d u {\\displaystyle F(s)=\\int
\_{-\\infty }\^{\\infty }e\^{-su}\\ f(u)\\ {\\text{d}}u} and G ( s ) = ∫
− ∞ ∞ e − s v g ( v ) d v {\\displaystyle G(s)=\\int \_{-\\infty
}\^{\\infty }e\^{-sv}\\ g(v)\\ {\\text{d}}v} respectively, the
convolution operation ( f ∗ g ) ( t ) {\\displaystyle (f\*g)(t)} can be
defined as the inverse Laplace transform of the product of F ( s )
{\\displaystyle F(s)} and G ( s ) {\\displaystyle G(s)} . More
precisely, F ( s ) ⋅ G ( s ) = ∫ − ∞ ∞ e − s u f ( u ) d u ⋅ ∫ − ∞ ∞ e −
s v g ( v ) d v = ∫ − ∞ ∞ ∫ − ∞ ∞ e − s ( u + v ) f ( u ) g ( v ) d u d
v {\\displaystyle {\\begin{aligned}F(s)\\cdot G(s)&=\\int \_{-\\infty
}\^{\\infty }e\^{-su}\\ f(u)\\ {\\text{d}}u\\cdot \\int \_{-\\infty
}\^{\\infty }e\^{-sv}\\ g(v)\\ {\\text{d}}v\\\\&=\\int \_{-\\infty
}\^{\\infty }\\int \_{-\\infty }\^{\\infty }e\^{-s(u+v)}\\ f(u)\\ g(v)\\
{\\text{d}}u\\ {\\text{d}}v\\end{aligned}}} Let t = u + v
{\\displaystyle t=u+v} such that F ( s ) ⋅ G ( s ) = ∫ − ∞ ∞ ∫ − ∞ ∞ e −
s t f ( u ) g ( t − u ) d u d t = ∫ − ∞ ∞ e − s t ∫ − ∞ ∞ f ( u ) g ( t
− u ) d u ⏟ ( f ∗ g ) ( t ) d t = ∫ − ∞ ∞ e − s t ( f ∗ g ) ( t ) d t
{\\displaystyle {\\begin{aligned}F(s)\\cdot G(s)&=\\int \_{-\\infty
}\^{\\infty }\\int \_{-\\infty }\^{\\infty }e\^{-st}\\ f(u)\\ g(t-u)\\
{\\text{d}}u\\ {\\text{d}}t\\\\&=\\int \_{-\\infty }\^{\\infty
}e\^{-st}\\underbrace {\\int \_{-\\infty }\^{\\infty }f(u)\\ g(t-u)\\
{\\text{d}}u} \_{(f\*g)(t)}\\ {\\text{d}}t\\\\&=\\int \_{-\\infty
}\^{\\infty }e\^{-st}(f\*g)(t)\\ {\\text{d}}t\\end{aligned}}} Note that
F ( s ) ⋅ G ( s ) {\\displaystyle F(s)\\cdot G(s)} is the bilateral
Laplace transform of ( f ∗ g ) ( t ) {\\displaystyle (f\*g)(t)} . A
similar derivation can be done using the unilateral Laplace transform
(one-sided Laplace transform). The convolution operation also describes
the output (in terms of the input) of an important class of operations
known as linear time-invariant (LTI). See LTI system theory for a
derivation of convolution as the result of LTI constraints. In terms of
the Fourier transforms of the input and output of an LTI operation, no
new frequency components are created. The existing ones are only
modified (amplitude and/or phase). In other words, the output transform
is the pointwise product of the input transform with a third transform
(known as a transfer function). See Convolution theorem for a derivation
of that property of convolution. Conversely, convolution can be derived
as the inverse Fourier transform of the pointwise product of two Fourier
transforms. Visual explanation Historical developments One of the
earliest uses of the convolution integral appeared in D\'Alembert\'s
derivation of Taylor\'s theorem in Recherches sur différents points
importants du système du monde, published in 1754.Also, an expression of
the type: ∫ f ( u ) ⋅ g ( x − u ) d u {\\displaystyle \\int f(u)\\cdot
g(x-u)\\,du} is used by Sylvestre François Lacroix on page 505 of his
book entitled Treatise on differences and series, which is the last of 3
volumes of the encyclopedic series: Traité du calcul différentiel et du
calcul intégral, Chez Courcier, Paris, 1797--1800. Soon thereafter,
convolution operations appear in the works of Pierre Simon Laplace,
Jean-Baptiste Joseph Fourier, Siméon Denis Poisson, and others. The term
itself did not come into wide use until the 1950s or 60s. Prior to that
it was sometimes known as Faltung (which means folding in German),
composition product, superposition integral, and Carson\'s integral. Yet
it appears as early as 1903, though the definition is rather unfamiliar
in older uses.The operation: ∫ 0 t φ ( s ) ψ ( t − s ) d s , 0 ≤ t \< ∞
, {\\displaystyle \\int \_{0}\^{t}\\varphi (s)\\psi (t-s)\\,ds,\\quad
0\\leq t\<\\infty ,} is a particular case of composition products
considered by the Italian mathematician Vito Volterra in 1913. Circular
convolution When a function gT is periodic, with period T, then for
functions, f, such that f ∗ gT exists, the convolution is also periodic
and identical to: ( f ∗ g T ) ( t ) ≡ ∫ t 0 t 0 + T \[ ∑ k = − ∞ ∞ f (
τ + k T ) \] g T ( t − τ ) d τ , {\\displaystyle (f\*g\_{T})(t)\\equiv
\\int \_{t\_{0}}\^{t\_{0}+T}\\left\[\\sum \_{k=-\\infty }\^{\\infty
}f(\\tau +kT)\\right\]g\_{T}(t-\\tau )\\,d\\tau ,} where t0 is an
arbitrary choice. The summation is called a periodic summation of the
function f. When gT is a periodic summation of another function, g, then
f ∗ gT is known as a circular or cyclic convolution of f and g. And if
the periodic summation above is replaced by fT, the operation is called
a periodic convolution of fT and gT. Discrete convolution For
complex-valued functions f, g defined on the set Z of integers, the
discrete convolution of f and g is given by: ( f ∗ g ) \[ n \] = ∑ m = −
∞ ∞ f \[ m \] g \[ n − m \] , {\\displaystyle (f\*g)\[n\]=\\sum
\_{m=-\\infty }\^{\\infty }f\[m\]g\[n-m\],} or equivalently (see
commutativity) by: ( f ∗ g ) \[ n \] = ∑ m = − ∞ ∞ f \[ n − m \] g \[ m
\] . {\\displaystyle (f\*g)\[n\]=\\sum \_{m=-\\infty }\^{\\infty
}f\[n-m\]g\[m\].} The convolution of two finite sequences is defined by
extending the sequences to finitely supported functions on the set of
integers. When the sequences are the coefficients of two polynomials,
then the coefficients of the ordinary product of the two polynomials are
the convolution of the original two sequences. This is known as the
Cauchy product of the coefficients of the sequences. Thus when g has
finite support in the set { − M , − M + 1 , ... , M − 1 , M }
{\\displaystyle \\{-M,-M+1,\\dots ,M-1,M\\}} (representing, for
instance, a finite impulse response), a finite summation may be used: (
f ∗ g ) \[ n \] = ∑ m = − M M f \[ n − m \] g \[ m \] . {\\displaystyle
(f\*g)\[n\]=\\sum \_{m=-M}\^{M}f\[n-m\]g\[m\].} Circular discrete
convolution When a function gN is periodic, with period N, then for
functions, f, such that f∗gN exists, the convolution is also periodic
and identical to: ( f ∗ g N ) \[ n \] ≡ ∑ m = 0 N − 1 ( ∑ k = − ∞ ∞ f \[
m + k N \] ) g N \[ n − m \] . {\\displaystyle (f\*g\_{N})\[n\]\\equiv
\\sum \_{m=0}\^{N-1}\\left(\\sum \_{k=-\\infty }\^{\\infty
}{f}\[m+kN\]\\right)g\_{N}\[n-m\].} The summation on k is called a
periodic summation of the function f. If gN is a periodic summation of
another function, g, then f∗gN is known as a circular convolution of f
and g. When the non-zero durations of both f and g are limited to the
interval \[0, N − 1\], f∗gN reduces to these common forms: The notation
(f ∗N g) for cyclic convolution denotes convolution over the cyclic
group of integers modulo N. Circular convolution arises most often in
the context of fast convolution with a fast Fourier transform (FFT)
algorithm. Fast convolution algorithms In many situations, discrete
convolutions can be converted to circular convolutions so that fast
transforms with a convolution property can be used to implement the
computation. For example, convolution of digit sequences is the kernel
operation in multiplication of multi-digit numbers, which can therefore
be efficiently implemented with transform techniques (Knuth 1997,
§4.3.3.C; von zur Gathen & Gerhard 2003, §8.2). Eq.1 requires N
arithmetic operations per output value and N2 operations for N outputs.
That can be significantly reduced with any of several fast algorithms.
Digital signal processing and other applications typically use fast
convolution algorithms to reduce the cost of the convolution to O(N log
N) complexity. The most common fast convolution algorithms use fast
Fourier transform (FFT) algorithms via the circular convolution theorem.
Specifically, the circular convolution of two finite-length sequences is
found by taking an FFT of each sequence, multiplying pointwise, and then
performing an inverse FFT. Convolutions of the type defined above are
then efficiently implemented using that technique in conjunction with
zero-extension and/or discarding portions of the output. Other fast
convolution algorithms, such as the Schönhage--Strassen algorithm or the
Mersenne transform, use fast Fourier transforms in other rings. If one
sequence is much longer than the other, zero-extension of the shorter
sequence and fast circular convolution is not the most computationally
efficient method available. Instead, decomposing the longer sequence
into blocks and convolving each block allows for faster algorithms such
as the overlap--save method and overlap--add method. A hybrid
convolution method that combines block and FIR algorithms allows for a
zero input-output latency that is useful for real-time convolution
computations. Domain of definition The convolution of two complex-valued
functions on Rd is itself a complex-valued function on Rd, defined by: (
f ∗ g ) ( x ) = ∫ R d f ( y ) g ( x − y ) d y = ∫ R d f ( x − y ) g ( y
) d y , {\\displaystyle (f\*g)(x)=\\int \_{\\mathbf {R}
\^{d}}f(y)g(x-y)\\,dy=\\int \_{\\mathbf {R} \^{d}}f(x-y)g(y)\\,dy,} and
is well-defined only if f and g decay sufficiently rapidly at infinity
in order for the integral to exist. Conditions for the existence of the
convolution may be tricky, since a blow-up in g at infinity can be
easily offset by sufficiently rapid decay in f. The question of
existence thus may involve different conditions on f and g: Compactly
supported functions If f and g are compactly supported continuous
functions, then their convolution exists, and is also compactly
supported and continuous (Hörmander 1983, Chapter 1). More generally, if
either function (say f) is compactly supported and the other is locally
integrable, then the convolution f∗g is well-defined and continuous.
Convolution of f and g is also well defined when both functions are
locally square integrable on R and supported on an interval of the form
\[a, +∞) (or both supported on \[−∞, a\]). Integrable functions The
convolution of f and g exists if f and g are both Lebesgue integrable
functions in L1(Rd), and in this case f∗g is also integrable (Stein &
Weiss 1971, Theorem 1.3). This is a consequence of Tonelli\'s theorem.
This is also true for functions in L1, under the discrete convolution,
or more generally for the convolution on any group. Likewise, if f ∈
L1(Rd) and g ∈ Lp(Rd) where 1 ≤ p ≤ ∞, then f∗g ∈ Lp(Rd), and ‖ f ∗ g ‖
p ≤ ‖ f ‖ 1 ‖ g ‖ p . {\\displaystyle \\\|{f}\*g\\\|\_{p}\\leq
\\\|f\\\|\_{1}\\\|g\\\|\_{p}.} In the particular case p = 1, this shows
that L1 is a Banach algebra under the convolution (and equality of the
two sides holds if f and g are non-negative almost everywhere). More
generally, Young\'s inequality implies that the convolution is a
continuous bilinear map between suitable Lp spaces. Specifically, if 1 ≤
p, q, r ≤ ∞ satisfy: 1 p + 1 q = 1 r + 1 , {\\displaystyle {\\frac
{1}{p}}+{\\frac {1}{q}}={\\frac {1}{r}}+1,} then ‖ f ∗ g ‖ r ≤ ‖ f ‖ p ‖
g ‖ q , f ∈ L p , g ∈ L q , {\\displaystyle \\left\\Vert
f\*g\\right\\Vert \_{r}\\leq \\left\\Vert f\\right\\Vert
\_{p}\\left\\Vert g\\right\\Vert \_{q},\\quad f\\in {\\mathcal
{L}}\^{p},\\ g\\in {\\mathcal {L}}\^{q},} so that the convolution is a
continuous bilinear mapping from Lp×Lq to Lr. The Young inequality for
convolution is also true in other contexts (circle group, convolution on
Z). The preceding inequality is not sharp on the real line: when 1 \< p,
q, r \< ∞, there exists a constant Bp,q \< 1 such that: ‖ f ∗ g ‖ r ≤ B
p , q ‖ f ‖ p ‖ g ‖ q , f ∈ L p , g ∈ L q . {\\displaystyle \\left\\Vert
f\*g\\right\\Vert \_{r}\\leq B\_{p,q}\\left\\Vert f\\right\\Vert
\_{p}\\left\\Vert g\\right\\Vert \_{q},\\quad f\\in {\\mathcal
{L}}\^{p},\\ g\\in {\\mathcal {L}}\^{q}.} The optimal value of Bp,q was
discovered in 1975 and independently in 1976, see Brascamp--Lieb
inequality. A stronger estimate is true provided 1 \< p, q, r \< ∞ : ‖ f
∗ g ‖ r ≤ C p , q ‖ f ‖ p ‖ g ‖ q , w {\\displaystyle
\\\|f\*g\\\|\_{r}\\leq C\_{p,q}\\\|f\\\|\_{p}\\\|g\\\|\_{q,w}} where ‖ g
‖ q , w {\\displaystyle \\\|g\\\|\_{q,w}} is the weak Lq norm.
Convolution also defines a bilinear continuous map L p , w × L q , w → L
r , w {\\displaystyle L\^{p,w}\\times L\^{q,w}\\to L\^{r,w}} for 1 \< p
, q , r \< ∞ {\\displaystyle 1
