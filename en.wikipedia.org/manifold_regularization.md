In machine learning, Manifold regularization is a technique for using
the shape of a dataset to constrain the functions that should be learned
on that dataset. In many machine learning problems, the data to be
learned do not cover the entire input space. For example, a facial
recognition system may not need to classify any possible image, but only
the subset of images that contain faces. The technique of manifold
learning assumes that the relevant subset of data comes from a manifold,
a mathematical structure with useful properties. The technique also
assumes that the function to be learned is smooth: data with different
labels are not likely to be close together, and so the labeling function
should not change quickly in areas where there are likely to be many
data points. Because of this assumption, a manifold regularization
algorithm can use unlabeled data to inform where the learned function is
allowed to change quickly and where it is not, using an extension of the
technique of Tikhonov regularization. Manifold regularization algorithms
can extend supervised learning algorithms in semi-supervised learning
and transductive learning settings, where unlabeled data are available.
The technique has been used for applications including medical imaging,
geographical imaging, and object recognition. Manifold regularizer
Motivation Manifold regularization is a type of regularization, a family
of techniques that reduces overfitting and ensures that a problem is
well-posed by penalizing complex solutions. In particular, manifold
regularization extends the technique of Tikhonov regularization as
applied to Reproducing kernel Hilbert spaces (RKHSs). Under standard
Tikhonov regularization on RKHSs, a learning algorithm attempts to learn
a function f {\\displaystyle f} from among a hypothesis space of
functions H {\\displaystyle {\\mathcal {H}}} . The hypothesis space is
an RKHS, meaning that it is associated with a kernel K {\\displaystyle
K} , and so every candidate function f {\\displaystyle f} has a norm ‖ f
‖ K {\\displaystyle \\left\\\|f\\right\\\|\_{K}} , which represents the
complexity of the candidate function in the hypothesis space. When the
algorithm considers a candidate function, it takes its norm into account
in order to penalize complex functions. Formally, given a set of labeled
training data ( x 1 , y 1 ) , ... , ( x ℓ , y ℓ ) {\\displaystyle
(x\_{1},y\_{1}),\\ldots ,(x\_{\\ell },y\_{\\ell })} with x i ∈ X , y i ∈
Y {\\displaystyle x\_{i}\\in X,y\_{i}\\in Y} and a loss function V
{\\displaystyle V} , a learning algorithm using Tikhonov regularization
will attempt to solve the expression arg min f ∈ H 1 ℓ ∑ i = 1 ℓ V ( f (
x i ) , y i ) + γ ‖ f ‖ K 2 {\\displaystyle {\\underset {f\\in
{\\mathcal {H}}}{\\arg \\!\\min }}{\\frac {1}{\\ell }}\\sum
\_{i=1}\^{\\ell }V(f(x\_{i}),y\_{i})+\\gamma
\\left\\\|f\\right\\\|\_{K}\^{2}} where γ {\\displaystyle \\gamma } is a
hyperparameter that controls how much the algorithm will prefer simpler
functions over functions that fit the data better. Manifold
regularization adds a second regularization term, the intrinsic
regularizer, to the ambient regularizer used in standard Tikhonov
regularization. Under the manifold assumption in machine learning, the
data in question do not come from the entire input space X
{\\displaystyle X} , but instead from a nonlinear manifold M ⊂ X
{\\displaystyle M\\subset X} . The geometry of this manifold, the
intrinsic space, is used to determine the regularization norm. Laplacian
norm There are many possible choices for the intrinsic regularizer ‖ f ‖
I {\\displaystyle \\left\\\|f\\right\\\|\_{I}} . Many natural choices
involve the gradient on the manifold ∇ M {\\displaystyle \\nabla \_{M}}
, which can provide a measure of how smooth a target function is. A
smooth function should change slowly where the input data are dense;
that is, the gradient ∇ M f ( x ) {\\displaystyle \\nabla \_{M}f(x)}
should be small where the marginal probability density P X ( x )
{\\displaystyle {\\mathcal {P}}\_{X}(x)} , the probability density of a
randomly drawn data point appearing at x {\\displaystyle x} , is large.
This gives one appropriate choice for the intrinsic regularizer: ‖ f ‖ I
2 = ∫ x ∈ M ‖ ∇ M f ( x ) ‖ 2 d P X ( x ) {\\displaystyle
\\left\\\|f\\right\\\|\_{I}\^{2}=\\int \_{x\\in M}\\left\\\|\\nabla
\_{M}f(x)\\right\\\|\^{2}\\,d{\\mathcal {P}}\_{X}(x)} In practice, this
norm cannot be computed directly because the marginal distribution P X
{\\displaystyle {\\mathcal {P}}\_{X}} is unknown, but it can be
estimated from the provided data. Graph-based approach of the Laplacian
norm When the distances between input points are interpreted as a graph,
then the Laplacian matrix of the graph can help to estimate the marginal
distribution. Suppose that the input data include ℓ {\\displaystyle
\\ell } labeled examples (pairs of an input x {\\displaystyle x} and a
label y {\\displaystyle y} ) and u {\\displaystyle u} unlabeled examples
(inputs without associated labels). Define W {\\displaystyle W} to be a
matrix of edge weights for a graph, where W i j {\\displaystyle W\_{ij}}
is a distance measure between the data points x i {\\displaystyle
x\_{i}} and x j {\\displaystyle x\_{j}} . Define D {\\displaystyle D} to
be a diagonal matrix with D i i = ∑ j = 1 ℓ + u W i j {\\displaystyle
D\_{ii}=\\sum \_{j=1}\^{\\ell +u}W\_{ij}} and L {\\displaystyle L} to be
the Laplacian matrix D − W {\\displaystyle D-W} . Then, as the number of
data points ℓ + u {\\displaystyle \\ell +u} increases, L {\\displaystyle
L} converges to the Laplace--Beltrami operator Δ M {\\displaystyle
\\Delta \_{M}} , which is the divergence of the gradient ∇ M
{\\displaystyle \\nabla \_{M}} . Then, if f {\\displaystyle \\mathbf {f}
} is a vector of the values of f {\\displaystyle f} at the data, f = \[
f ( x 1 ) , ... , f ( x l + u ) \] T {\\displaystyle \\mathbf {f}
=\[f(x\_{1}),\\ldots ,f(x\_{l+u})\]\^{\\mathrm {T} }} , the intrinsic
norm can be estimated: ‖ f ‖ I 2 = 1 ( ℓ + u ) 2 f T L f {\\displaystyle
\\left\\\|f\\right\\\|\_{I}\^{2}={\\frac {1}{(\\ell +u)\^{2}}}\\mathbf
{f} \^{\\mathrm {T} }L\\mathbf {f} } As the number of data points ℓ + u
{\\displaystyle \\ell +u} increases, this empirical definition of ‖ f ‖
I 2 {\\displaystyle \\left\\\|f\\right\\\|\_{I}\^{2}} converges to the
definition when P X {\\displaystyle {\\mathcal {P}}\_{X}} is known.
Solving the regularization problem with graph-based approach Using the
weights γ A {\\displaystyle \\gamma \_{A}} and γ I {\\displaystyle
\\gamma \_{I}} for the ambient and intrinsic regularizers, the final
expression to be solved becomes: arg min f ∈ H 1 ℓ ∑ i = 1 ℓ V ( f ( x i
) , y i ) + γ A ‖ f ‖ K 2 + γ I ( ℓ + u ) 2 f T L f {\\displaystyle
{\\underset {f\\in {\\mathcal {H}}}{\\arg \\!\\min }}{\\frac {1}{\\ell
}}\\sum \_{i=1}\^{\\ell }V(f(x\_{i}),y\_{i})+\\gamma
\_{A}\\left\\\|f\\right\\\|\_{K}\^{2}+{\\frac {\\gamma \_{I}}{(\\ell
+u)\^{2}}}\\mathbf {f} \^{\\mathrm {T} }L\\mathbf {f} } As with other
kernel methods, H {\\displaystyle {\\mathcal {H}}} may be an
infinite-dimensional space, so if the regularization expression cannot
be solved explicitly, it is impossible to search the entire space for a
solution. Instead, a representer theorem shows that under certain
conditions on the choice of the norm ‖ f ‖ I {\\displaystyle
\\left\\\|f\\right\\\|\_{I}} , the optimal solution f ∗ {\\displaystyle
f\^{\*}} must be a linear combination of the kernel centered at each of
the input points: for some weights α i {\\displaystyle \\alpha \_{i}} ,
f ∗ ( x ) = ∑ i = 1 ℓ + u α i K ( x i , x ) {\\displaystyle
f\^{\*}(x)=\\sum \_{i=1}\^{\\ell +u}\\alpha \_{i}K(x\_{i},x)} Using this
result, it is possible to search for the optimal solution f ∗
{\\displaystyle f\^{\*}} by searching the finite-dimensional space
defined by the possible choices of α i {\\displaystyle \\alpha \_{i}} .
Functional approach of the Laplacian norm The idea beyond
graph-Laplacian is to use neighbors to estimate Laplacian. This method
is akin local averaging methods, that are known to scale poorly in
high-dimensional problem. Indeed, graph Laplacian is known to suffer
from the curse of dimensionality. Luckily, it is possible to leverage
expected smoothness of the function to estimate thanks to more advanced
functional analysis. This method consists in estimating the Laplacian
operator thanks to derivatives of the kernel reading ∂ 1 , j K ( x i , x
) {\\displaystyle \\partial \_{1,j}K(x\_{i},x)} where ∂ 1 , j
{\\displaystyle \\partial \_{1,j}} denotes the partial derivatives
according to the j-th coordinate of the first variable. This second
approach of the Laplacian norm is to put in relation with meshfree
methods, that contrast with the finite difference method in PDE.
Applications Manifold regularization can extend a variety of algorithms
that can be expressed using Tikhonov regularization, by choosing an
appropriate loss function V {\\displaystyle V} and hypothesis space H
{\\displaystyle {\\mathcal {H}}} . Two commonly used examples are the
families of support vector machines and regularized least squares
algorithms. (Regularized least squares includes the ridge regression
algorithm; the related algorithms of LASSO and elastic net
regularization can be expressed as support vector machines.) The
extended versions of these algorithms are called Laplacian Regularized
Least Squares (abbreviated LapRLS) and Laplacian Support Vector Machines
(LapSVM), respectively. Laplacian Regularized Least Squares (LapRLS)
Regularized least squares (RLS) is a family of regression algorithms:
algorithms that predict a value y = f ( x ) {\\displaystyle y=f(x)} for
its inputs x {\\displaystyle x} , with the goal that the predicted
values should be close to the true labels for the data. In particular,
RLS is designed to minimize the mean squared error between the predicted
values and the true labels, subject to regularization. Ridge regression
is one form of RLS; in general, RLS is the same as ridge regression
combined with the kernel method. The problem statement for RLS results
from choosing the loss function V {\\displaystyle V} in Tikhonov
regularization to be the mean squared error: f ∗ = arg min f ∈ H 1 ℓ ∑ i
= 1 ℓ ( f ( x i ) − y i ) 2 + γ ‖ f ‖ K 2 {\\displaystyle
f\^{\*}={\\underset {f\\in {\\mathcal {H}}}{\\arg \\!\\min }}{\\frac
{1}{\\ell }}\\sum \_{i=1}\^{\\ell }(f(x\_{i})-y\_{i})\^{2}+\\gamma
\\left\\\|f\\right\\\|\_{K}\^{2}} Thanks to the representer theorem, the
solution can be written as a weighted sum of the kernel evaluated at the
data points: f ∗ ( x ) = ∑ i = 1 ℓ α i ∗ K ( x i , x ) {\\displaystyle
f\^{\*}(x)=\\sum \_{i=1}\^{\\ell }\\alpha \_{i}\^{\*}K(x\_{i},x)} and
solving for α ∗ {\\displaystyle \\alpha \^{\*}} gives: α ∗ = ( K + γ ℓ I
) − 1 Y {\\displaystyle \\alpha \^{\*}=(K+\\gamma \\ell I)\^{-1}Y} where
K {\\displaystyle K} is defined to be the kernel matrix, with K i j = K
( x i , x j ) {\\displaystyle K\_{ij}=K(x\_{i},x\_{j})} , and Y
{\\displaystyle Y} is the vector of data labels. Adding a Laplacian term
for manifold regularization gives the Laplacian RLS statement: f ∗ = arg
min f ∈ H 1 ℓ ∑ i = 1 ℓ ( f ( x i ) − y i ) 2 + γ A ‖ f ‖ K 2 + γ I (
ℓ + u ) 2 f T L f {\\displaystyle f\^{\*}={\\underset {f\\in {\\mathcal
{H}}}{\\arg \\!\\min }}{\\frac {1}{\\ell }}\\sum \_{i=1}\^{\\ell
}(f(x\_{i})-y\_{i})\^{2}+\\gamma
\_{A}\\left\\\|f\\right\\\|\_{K}\^{2}+{\\frac {\\gamma \_{I}}{(\\ell
+u)\^{2}}}\\mathbf {f} \^{\\mathrm {T} }L\\mathbf {f} } The representer
theorem for manifold regularization again gives f ∗ ( x ) = ∑ i = 1 ℓ +
u α i ∗ K ( x i , x ) {\\displaystyle f\^{\*}(x)=\\sum \_{i=1}\^{\\ell
+u}\\alpha \_{i}\^{\*}K(x\_{i},x)} and this yields an expression for the
vector α ∗ {\\displaystyle \\alpha \^{\*}} . Letting K {\\displaystyle
K} be the kernel matrix as above, Y {\\displaystyle Y} be the vector of
data labels, and J {\\displaystyle J} be the ( ℓ + u ) × ( ℓ + u )
{\\displaystyle (\\ell +u)\\times (\\ell +u)} block matrix \[ I ℓ 0 0 0
u \] {\\displaystyle {\\begin{bmatrix}I\_{\\ell
}&0\\\\0&0\_{u}\\end{bmatrix}}} : α ∗ = arg min α ∈ R ℓ + u 1 ℓ ( Y − J
K α ) T ( Y − J K α ) + γ A α T K α + γ I ( ℓ + u ) 2 α T K L K α
{\\displaystyle \\alpha \^{\*}={\\underset {\\alpha \\in \\mathbf {R}
\^{\\ell +u}}{\\arg \\!\\min }}{\\frac {1}{\\ell }}(Y-JK\\alpha
)\^{\\mathrm {T} }(Y-JK\\alpha )+\\gamma \_{A}\\alpha \^{\\mathrm {T}
}K\\alpha +{\\frac {\\gamma \_{I}}{(\\ell +u)\^{2}}}\\alpha \^{\\mathrm
{T} }KLK\\alpha } with a solution of α ∗ = ( J K + γ A ℓ I + γ I ℓ ( ℓ +
u ) 2 L K ) − 1 Y {\\displaystyle \\alpha \^{\*}=\\left(JK+\\gamma
\_{A}\\ell I+{\\frac {\\gamma \_{I}\\ell }{(\\ell
+u)\^{2}}}LK\\right)\^{-1}Y} LapRLS has been applied to problems
including sensor networks,medical imaging, object
detection,spectroscopy,document classification, drug-protein
interactions, and compressing images and videos. Laplacian Support
Vector Machines (LapSVM) Support vector machines (SVMs) are a family of
algorithms often used for classifying data into two or more groups, or
classes. Intuitively, an SVM draws a boundary between classes so that
the closest labeled examples to the boundary are as far away as
possible. This can be directly expressed as a linear program, but it is
also equivalent to Tikhonov regularization with the hinge loss function,
V ( f ( x ) , y ) = max ( 0 , 1 − y f ( x ) ) {\\displaystyle
V(f(x),y)=\\max(0,1-yf(x))} : f ∗ = arg min f ∈ H 1 ℓ ∑ i = 1 ℓ max ( 0
, 1 − y i f ( x i ) ) + γ ‖ f ‖ K 2 {\\displaystyle f\^{\*}={\\underset
{f\\in {\\mathcal {H}}}{\\arg \\!\\min }}{\\frac {1}{\\ell }}\\sum
\_{i=1}\^{\\ell }\\max(0,1-y\_{i}f(x\_{i}))+\\gamma
\\left\\\|f\\right\\\|\_{K}\^{2}} Adding the intrinsic regularization
term to this expression gives the LapSVM problem statement: f ∗ = arg
min f ∈ H 1 ℓ ∑ i = 1 ℓ max ( 0 , 1 − y i f ( x i ) ) + γ A ‖ f ‖ K 2 +
γ I ( ℓ + u ) 2 f T L f {\\displaystyle f\^{\*}={\\underset {f\\in
{\\mathcal {H}}}{\\arg \\!\\min }}{\\frac {1}{\\ell }}\\sum
\_{i=1}\^{\\ell }\\max(0,1-y\_{i}f(x\_{i}))+\\gamma
\_{A}\\left\\\|f\\right\\\|\_{K}\^{2}+{\\frac {\\gamma \_{I}}{(\\ell
+u)\^{2}}}\\mathbf {f} \^{\\mathrm {T} }L\\mathbf {f} } Again, the
representer theorem allows the solution to be expressed in terms of the
kernel evaluated at the data points: f ∗ ( x ) = ∑ i = 1 ℓ + u α i ∗ K (
x i , x ) {\\displaystyle f\^{\*}(x)=\\sum \_{i=1}\^{\\ell +u}\\alpha
\_{i}\^{\*}K(x\_{i},x)} α {\\displaystyle \\alpha } can be found by
writing the problem as a linear program and solving the dual problem.
Again letting K {\\displaystyle K} be the kernel matrix and J
{\\displaystyle J} be the block matrix \[ I ℓ 0 0 0 u \] {\\displaystyle
{\\begin{bmatrix}I\_{\\ell }&0\\\\0&0\_{u}\\end{bmatrix}}} , the
solution can be shown to be α = ( 2 γ A I + 2 γ I ( ℓ + u ) 2 L K ) − 1
J T Y β ∗ {\\displaystyle \\alpha =\\left(2\\gamma \_{A}I+2{\\frac
{\\gamma \_{I}}{(\\ell +u)\^{2}}}LK\\right)\^{-1}J\^{\\mathrm {T}
}Y\\beta \^{\*}} where β ∗ {\\displaystyle \\beta \^{\*}} is the
solution to the dual problem β ∗ = max β ∈ R ℓ ∑ i = 1 ℓ β i − 1 2 β T Q
β subject to ∑ i = 1 ℓ β i y i = 0 0 ≤ β i ≤ 1 ℓ i = 1 , ... , ℓ
{\\displaystyle {\\begin{aligned}&&\\beta \^{\*}=\\max \_{\\beta \\in
\\mathbf {R} \^{\\ell }}&\\sum \_{i=1}\^{\\ell }\\beta \_{i}-{\\frac
{1}{2}}\\beta \^{\\mathrm {T} }Q\\beta \\\\&{\\text{subject to}}&&\\sum
\_{i=1}\^{\\ell }\\beta \_{i}y\_{i}=0\\\\&&&0\\leq \\beta \_{i}\\leq
{\\frac {1}{\\ell }}\\;i=1,\\ldots ,\\ell \\end{aligned}}} and Q
{\\displaystyle Q} is defined by Q = Y J K ( 2 γ A I + 2 γ I ( ℓ + u ) 2
L K ) − 1 J T Y {\\displaystyle Q=YJK\\left(2\\gamma \_{A}I+2{\\frac
{\\gamma \_{I}}{(\\ell +u)\^{2}}}LK\\right)\^{-1}J\^{\\mathrm {T} }Y}
LapSVM has been applied to problems including geographical imaging,
medical imaging, face recognition, machine maintenance, and
brain--computer interfaces. Limitations Manifold regularization assumes
that data with different labels are not likely to be close together.
This assumption is what allows the technique to draw information from
unlabeled data, but it only applies to some problem domains. Depending
on the structure of the data, it may be necessary to use a different
semi-supervised or transductive learning algorithm. In some datasets,
the intrinsic norm of a function ‖ f ‖ I {\\displaystyle
\\left\\\|f\\right\\\|\_{I}} can be very close to the ambient norm ‖ f ‖
K {\\displaystyle \\left\\\|f\\right\\\|\_{K}} : for example, if the
data consist of two classes that lie on perpendicular lines, the
intrinsic norm will be equal to the ambient norm. In this case,
unlabeled data have no effect on the solution learned by manifold
regularization, even if the data fit the algorithm\'s assumption that
the separator should be smooth. Approaches related to co-training have
been proposed to address this limitation. If there are a very large
number of unlabeled examples, the kernel matrix K {\\displaystyle K}
becomes very large, and a manifold regularization algorithm may become
prohibitively slow to compute. Online algorithms and sparse
approximations of the manifold may help in this case. See also Manifold
learning Manifold hypothesis Semi-supervised learning Transduction
(machine learning) Spectral graph theory Reproducing kernel Hilbert
space Tikhonov regularization Differential geometry References External
links Software The ManifoldLearn library and the Primal LapSVM library
implement LapRLS and LapSVM in MATLAB. The Dlib library for C++ includes
a linear manifold regularization function.
