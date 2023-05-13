Sparse coding is a representation learning method which aims at finding
a sparse representation of the input data (also known as sparse coding)
in the form of a linear combination of basic elements as well as those
basic elements themselves. These elements are called atoms and they
compose a dictionary. Atoms in the dictionary are not required to be
orthogonal, and they may be an over-complete spanning set. This problem
setup also allows the dimensionality of the signals being represented to
be higher than the one of the signals being observed. The above two
properties lead to having seemingly redundant atoms that allow multiple
representations of the same signal but also provide an improvement in
sparsity and flexibility of the representation. One of the most
important applications of sparse dictionary learning is in the field of
compressed sensing or signal recovery. In compressed sensing, a
high-dimensional signal can be recovered with only a few linear
measurements provided that the signal is sparse or nearly sparse. Since
not all signals satisfy this sparsity condition, it is of great
importance to find a sparse representation of that signal such as the
wavelet transform or the directional gradient of a rasterized matrix.
Once a matrix or a high dimensional vector is transferred to a sparse
space, different recovery algorithms like basis pursuit, CoSaMP or fast
non-iterative algorithms can be used to recover the signal. One of the
key principles of dictionary learning is that the dictionary has to be
inferred from the input data. The emergence of sparse dictionary
learning methods was stimulated by the fact that in signal processing
one typically wants to represent the input data using as few components
as possible. Before this approach the general practice was to use
predefined dictionaries (such as Fourier or wavelet transforms).
However, in certain cases a dictionary that is trained to fit the input
data can significantly improve the sparsity, which has applications in
data decomposition, compression and analysis and has been used in the
fields of image denoising and classification, video and audio
processing. Sparsity and overcomplete dictionaries have immense
applications in image compression, image fusion and inpainting. Problem
statement Given the input dataset X = \[ x 1 , . . . , x K \] , x i ∈ R
d {\\displaystyle X=\[x\_{1},\...,x\_{K}\],x\_{i}\\in \\mathbb {R}
\^{d}} we wish to find a dictionary D ∈ R d × n : D = \[ d 1 , . . . , d
n \] {\\displaystyle \\mathbf {D} \\in \\mathbb {R} \^{d\\times
n}:D=\[d\_{1},\...,d\_{n}\]} and a representation R = \[ r 1 , . . . , r
K \] , r i ∈ R n {\\displaystyle R=\[r\_{1},\...,r\_{K}\],r\_{i}\\in
\\mathbb {R} \^{n}} such that both ‖ X − D R ‖ F 2 {\\displaystyle
\\\|X-\\mathbf {D} R\\\|\_{F}\^{2}} is minimized and the representations
r i {\\displaystyle r\_{i}} are sparse enough. This can be formulated as
the following optimization problem: argmin D ∈ C , r i ∈ R n ∑ i = 1 K ‖
x i − D r i ‖ 2 2 + λ ‖ r i ‖ 0 {\\displaystyle {\\underset {\\mathbf
{D} \\in {\\mathcal {C}},r\_{i}\\in \\mathbb {R}
\^{n}}{\\text{argmin}}}\\sum \_{i=1}\^{K}\\\|x\_{i}-\\mathbf {D}
r\_{i}\\\|\_{2}\^{2}+\\lambda \\\|r\_{i}\\\|\_{0}} , where C ≡ { D ∈ R d
× n : ‖ d i ‖ 2 ≤ 1 ∀ i = 1 , . . . , n } {\\displaystyle {\\mathcal
{C}}\\equiv \\{\\mathbf {D} \\in \\mathbb {R} \^{d\\times
n}:\\\|d\_{i}\\\|\_{2}\\leq 1\\,\\,\\forall i=1,\...,n\\}} , λ \> 0
{\\displaystyle \\lambda \>0} C {\\displaystyle {\\mathcal {C}}} is
required to constrain D {\\displaystyle \\mathbf {D} } so that its atoms
would not reach arbitrarily high values allowing for arbitrarily low
(but non-zero) values of r i {\\displaystyle r\_{i}} . λ {\\displaystyle
\\lambda } controls the trade off between the sparsity and the
minimization error. The minimization problem above is not convex because
of the ℓ0-\"norm\" and solving this problem is NP-hard. In some cases
L1-norm is known to ensure sparsity and so the above becomes a convex
optimization problem with respect to each of the variables D
{\\displaystyle \\mathbf {D} } and R {\\displaystyle \\mathbf {R} } when
the other one is fixed, but it is not jointly convex in ( D , R )
{\\displaystyle (\\mathbf {D} ,\\mathbf {R} )} . Properties of the
dictionary The dictionary D {\\displaystyle \\mathbf {D} } defined above
can be \"undercomplete\" if n \< d {\\displaystyle n d {\\displaystyle
n\>d} with the latter being a typical assumption for a sparse dictionary
learning problem. The case of a complete dictionary does not provide any
improvement from a representational point of view and thus isn\'t
considered. Undercomplete dictionaries represent the setup in which the
actual input data lies in a lower-dimensional space. This case is
strongly related to dimensionality reduction and techniques like
principal component analysis which require atoms d 1 , . . . , d n
{\\displaystyle d\_{1},\...,d\_{n}} to be orthogonal. The choice of
these subspaces is crucial for efficient dimensionality reduction, but
it is not trivial. And dimensionality reduction based on dictionary
representation can be extended to address specific tasks such as data
analysis or classification. However, their main downside is limiting the
choice of atoms. Overcomplete dictionaries, however, do not require the
atoms to be orthogonal (they will never be a basis anyway) thus allowing
for more flexible dictionaries and richer data representations. An
overcomplete dictionary which allows for sparse representation of signal
can be a famous transform matrix (wavelets transform, fourier transform)
or it can be formulated so that its elements are changed in such a way
that it sparsely represents the given signal in a best way. Learned
dictionaries are capable of giving sparser solutions as compared to
predefined transform matrices. Algorithms As the optimization problem
described above can be solved as a convex problem with respect to either
dictionary or sparse coding while the other one of the two is fixed,
most of the algorithms are based on the idea of iteratively updating one
and then the other. The problem of finding an optimal sparse coding R
{\\displaystyle R} with a given dictionary D {\\displaystyle \\mathbf
{D} } is known as sparse approximation (or sometimes just sparse coding
problem). A number of algorithms have been developed to solve it (such
as matching pursuit and LASSO) and are incorporated in the algorithms
described below. Method of optimal directions (MOD) The method of
optimal directions (or MOD) was one of the first methods introduced to
tackle the sparse dictionary learning problem. The core idea of it is to
solve the minimization problem subject to the limited number of non-zero
components of the representation vector: min D , R { ‖ X − D R ‖ F 2 }
s.t. ∀ i ‖ r i ‖ 0 ≤ T {\\displaystyle \\min \_{\\mathbf {D}
,R}\\{\\\|X-\\mathbf {D}
R\\\|\_{F}\^{2}\\}\\,\\,{\\text{s.t.}}\\,\\,\\forall
i\\,\\,\\\|r\_{i}\\\|\_{0}\\leq T} Here, F {\\displaystyle F} denotes
the Frobenius norm. MOD alternates between getting the sparse coding
using a method such as matching pursuit and updating the dictionary by
computing the analytical solution of the problem given by D = X R +
{\\displaystyle \\mathbf {D} =XR\^{+}} where R + {\\displaystyle R\^{+}}
is a Moore-Penrose pseudoinverse. After this update D {\\displaystyle
\\mathbf {D} } is renormalized to fit the constraints and the new sparse
coding is obtained again. The process is repeated until convergence (or
until a sufficiently small residue). MOD has proved to be a very
efficient method for low-dimensional input data X {\\displaystyle X}
requiring just a few iterations to converge. However, due to the high
complexity of the matrix-inversion operation, computing the
pseudoinverse in high-dimensional cases is in many cases intractable.
This shortcoming has inspired the development of other dictionary
learning methods. K-SVD K-SVD is an algorithm that performs SVD at its
core to update the atoms of the dictionary one by one and basically is a
generalization of K-means. It enforces that each element of the input
data x i {\\displaystyle x\_{i}} is encoded by a linear combination of
not more than T 0 {\\displaystyle T\_{0}} elements in a way identical to
the MOD approach: min D , R { ‖ X − D R ‖ F 2 } s.t. ∀ i ‖ r i ‖ 0 ≤ T 0
{\\displaystyle \\min \_{\\mathbf {D} ,R}\\{\\\|X-\\mathbf {D}
R\\\|\_{F}\^{2}\\}\\,\\,{\\text{s.t.}}\\,\\,\\forall
i\\,\\,\\\|r\_{i}\\\|\_{0}\\leq T\_{0}} This algorithm\'s essence is to
first fix the dictionary, find the best possible R {\\displaystyle R}
under the above constraint (using Orthogonal Matching Pursuit) and then
iteratively update the atoms of dictionary D {\\displaystyle \\mathbf
{D} } in the following manner: ‖ X − D R ‖ F 2 = \| X − ∑ i = 1 K d i x
T i \| F 2 = ‖ E k − d k x T k ‖ F 2 {\\displaystyle \\\|X-\\mathbf {D}
R\\\|\_{F}\^{2}=\\left\|X-\\sum
\_{i=1}\^{K}d\_{i}x\_{T}\^{i}\\right\|\_{F}\^{2}=\\\|E\_{k}-d\_{k}x\_{T}\^{k}\\\|\_{F}\^{2}}
The next steps of the algorithm include rank-1 approximation of the
residual matrix E k {\\displaystyle E\_{k}} , updating d k
{\\displaystyle d\_{k}} and enforcing the sparsity of x k
{\\displaystyle x\_{k}} after the update. This algorithm is considered
to be standard for dictionary learning and is used in a variety of
applications. However, it shares weaknesses with MOD being efficient
only for signals with relatively low dimensionality and having the
possibility for being stuck at local minima. Stochastic gradient descent
One can also apply a widespread stochastic gradient descent method with
iterative projection to solve this problem. The idea of this method is
to update the dictionary using the first order stochastic gradient and
project it on the constraint set C {\\displaystyle {\\mathcal {C}}} .
The step that occurs at i-th iteration is described by this expression:
D i = proj C { D i − 1 − δ i ∇ D ∑ i ∈ S ‖ x i − D r i ‖ 2 2 + λ ‖ r i ‖
1 } {\\displaystyle \\mathbf {D} \_{i}={\\text{proj}}\_{\\mathcal
{C}}\\left\\{\\mathbf {D} \_{i-1}-\\delta \_{i}\\nabla \_{\\mathbf {D}
}\\sum \_{i\\in S}\\\|x\_{i}-\\mathbf {D} r\_{i}\\\|\_{2}\^{2}+\\lambda
\\\|r\_{i}\\\|\_{1}\\right\\}} , where S {\\displaystyle S} is a random
subset of { 1\... K } {\\displaystyle \\{1\...K\\}} and δ i
{\\displaystyle \\delta \_{i}} is a gradient step. Lagrange dual method
An algorithm based on solving a dual Lagrangian problem provides an
efficient way to solve for the dictionary having no complications
induced by the sparsity function. Consider the following Lagrangian: L (
D , Λ ) = tr ( ( X − D R ) T ( X − D R ) ) + ∑ j = 1 n λ j ( ∑ i = 1 d D
i j 2 − c ) {\\displaystyle {\\mathcal {L}}(\\mathbf {D} ,\\Lambda
)={\\text{tr}}\\left((X-\\mathbf {D} R)\^{T}(X-\\mathbf {D}
R)\\right)+\\sum \_{j=1}\^{n}\\lambda \_{j}\\left({\\sum
\_{i=1}\^{d}\\mathbf {D} \_{ij}\^{2}-c}\\right)} , where c
{\\displaystyle c} is a constraint on the norm of the atoms and λ i
{\\displaystyle \\lambda \_{i}} are the so-called dual variables forming
the diagonal matrix Λ {\\displaystyle \\Lambda } . We can then provide
an analytical expression for the Lagrange dual after minimization over D
{\\displaystyle \\mathbf {D} } : D ( Λ ) = min D L ( D , Λ ) = tr ( X T
X − X R T ( R R T + Λ ) − 1 ( X R T ) T − c Λ ) {\\displaystyle
{\\mathcal {D}}(\\Lambda )=\\min \_{\\mathbf {D} }{\\mathcal
{L}}(\\mathbf {D} ,\\Lambda
)={\\text{tr}}(X\^{T}X-XR\^{T}(RR\^{T}+\\Lambda
)\^{-1}(XR\^{T})\^{T}-c\\Lambda )} . After applying one of the
optimization methods to the value of the dual (such as Newton\'s method
or conjugate gradient) we get the value of D {\\displaystyle \\mathbf
{D} } : D T = ( R R T + Λ ) − 1 ( X R T ) T {\\displaystyle \\mathbf {D}
\^{T}=(RR\^{T}+\\Lambda )\^{-1}(XR\^{T})\^{T}} Solving this problem is
less computational hard because the amount of dual variables n
{\\displaystyle n} is a lot of times much less than the amount of
variables in the primal problem. LASSO In this approach, the
optimization problem is formulated as: min r ∈ R n { ‖ r ‖ 1 } subject
to ‖ X − D R ‖ F 2 \< ϵ {\\displaystyle \\min \_{r\\in \\mathbb {R}
\^{n}}\\{\\,\\,\\\|r\\\|\_{1}\\}\\,\\,{\\text{subject
to}}\\,\\,\\\|X-\\mathbf {D} R\\\|\_{F}\^{2}\<\\epsilon } , where ϵ
{\\displaystyle \\epsilon } is the permitted error in the reconstruction
LASSO. It finds an estimate of r i {\\displaystyle r\_{i}} by minimizing
the least square error subject to a L1-norm constraint in the solution
vector, formulated as: min r ∈ R n 1 2 ‖ X − D r ‖ F 2 + λ ‖ r ‖ 1
{\\displaystyle \\min \_{r\\in \\mathbb {R} \^{n}}\\,\\,{\\dfrac
{1}{2}}\\,\\,\\\|X-\\mathbf {D} r\\\|\_{F}\^{2}+\\lambda
\\,\\,\\\|r\\\|\_{1}} , where λ \> 0 {\\displaystyle \\lambda \>0}
controls the trade-off between sparsity and the reconstruction error.
This gives the global optimal solution. See also Online dictionary
learning for Sparse coding Parametric training methods Parametric
training methods are aimed to incorporate the best of both worlds ---
the realm of analytically constructed dictionaries and the learned ones.
This allows to construct more powerful generalized dictionaries that can
potentially be applied to the cases of arbitrary-sized signals. Notable
approaches include: Translation-invariant dictionaries. These
dictionaries are composed by the translations of the atoms originating
from the dictionary constructed for a finite-size signal patch. This
allows the resulting dictionary to provide a representation for the
arbitrary-sized signal. Multiscale dictionaries. This method focuses on
constructing a dictionary that is composed of differently scaled
dictionaries to improve sparsity. Sparse dictionaries. This method
focuses on not only providing a sparse representation but also
constructing a sparse dictionary which is enforced by the expression D =
B A {\\displaystyle \\mathbf {D} =\\mathbf {B} \\mathbf {A} } where B
{\\displaystyle \\mathbf {B} } is some pre-defined analytical dictionary
with desirable properties such as fast computation and A {\\displaystyle
\\mathbf {A} } is a sparse matrix. Such formulation allows to directly
combine the fast implementation of analytical dictionaries with the
flexibility of sparse approaches. Online dictionary learning (LASSO
approach) Many common approaches to sparse dictionary learning rely on
the fact that the whole input data X {\\displaystyle X} (or at least a
large enough training dataset) is available for the algorithm. However,
this might not be the case in the real-world scenario as the size of the
input data might be too big to fit it into memory. The other case where
this assumption can not be made is when the input data comes in a form
of a stream. Such cases lie in the field of study of online learning
which essentially suggests iteratively updating the model upon the new
data points x {\\displaystyle x} becoming available. A dictionary can be
learned in an online manner the following way: For t = 1\... T :
{\\displaystyle t=1\...T:} Draw a new sample x t {\\displaystyle x\_{t}}
Find a sparse coding using LARS: r t = argmin r ∈ R n ( 1 2 ‖ x t − D t
− 1 r ‖ + λ ‖ r ‖ 1 ) {\\displaystyle r\_{t}={\\underset {r\\in \\mathbb
{R} \^{n}}{\\text{argmin}}}\\left({\\frac {1}{2}}\\\|x\_{t}-\\mathbf {D}
\_{t-1}r\\\|+\\lambda \\\|r\\\|\_{1}\\right)} Update dictionary using
block-coordinate approach: D t = argmin D ∈ C 1 t ∑ i = 1 t ( 1 2 ‖ x i
− D r i ‖ 2 2 + λ ‖ r i ‖ 1 ) {\\displaystyle \\mathbf {D}
\_{t}={\\underset {\\mathbf {D} \\in {\\mathcal
{C}}}{\\text{argmin}}}{\\frac {1}{t}}\\sum \_{i=1}\^{t}\\left({\\frac
{1}{2}}\\\|x\_{i}-\\mathbf {D} r\_{i}\\\|\_{2}\^{2}+\\lambda
\\\|r\_{i}\\\|\_{1}\\right)} This method allows us to gradually update
the dictionary as new data becomes available for sparse representation
learning and helps drastically reduce the amount of memory needed to
store the dataset (which often has a huge size). Applications The
dictionary learning framework, namely the linear decomposition of an
input signal using a few basis elements learned from data itself, has
led to state-of-art results in various image and video processing tasks.
This technique can be applied to classification problems in a way that
if we have built specific dictionaries for each class, the input signal
can be classified by finding the dictionary corresponding to the
sparsest representation. It also has properties that are useful for
signal denoising since usually one can learn a dictionary to represent
the meaningful part of the input signal in a sparse way but the noise in
the input will have a much less sparse representation.Sparse dictionary
learning has been successfully applied to various image, video and audio
processing tasks as well as to texture synthesis and unsupervised
clustering. In evaluations with the Bag-of-Words model, sparse coding
was found empirically to outperform other coding approaches on the
object category recognition tasks. Dictionary learning is used to
analyse medical signals in detail. Such medical signals include those
from electroencephalography (EEG), electrocardiography (ECG), magnetic
resonance imaging (MRI), functional MRI (fMRI), continuous glucose
monitors and ultrasound computer tomography (USCT), where different
assumptions are used to analyze each signal. See also Sparse
approximation Sparse PCA K-SVD Matrix factorization Neural sparse coding
== References ==
