In machine learning, support vector machines (SVMs, also support vector
networks) are supervised learning models with associated learning
algorithms that analyze data for classification and regression analysis.
Developed at AT&T Bell Laboratories by Vladimir Vapnik with colleagues
(Boser et al., 1992, Guyon et al., 1993, Cortes and Vapnik, 1995, Vapnik
et al., 1997) SVMs are one of the most robust prediction methods, being
based on statistical learning frameworks or VC theory proposed by Vapnik
(1982, 1995) and Chervonenkis (1974). Given a set of training examples,
each marked as belonging to one of two categories, an SVM training
algorithm builds a model that assigns new examples to one category or
the other, making it a non-probabilistic binary linear classifier
(although methods such as Platt scaling exist to use SVM in a
probabilistic classification setting). SVM maps training examples to
points in space so as to maximise the width of the gap between the two
categories. New examples are then mapped into that same space and
predicted to belong to a category based on which side of the gap they
fall. In addition to performing linear classification, SVMs can
efficiently perform a non-linear classification using what is called the
kernel trick, implicitly mapping their inputs into high-dimensional
feature spaces. The support vector clustering algorithm, created by Hava
Siegelmann and Vladimir Vapnik, applies the statistics of support
vectors, developed in the support vector machines algorithm, to
categorize unlabeled data. These data sets require unsupervised learning
approaches, which attempt to find natural clustering of the data to
groups and, then, to map new data according to these clusters.
Motivation Classifying data is a common task in machine learning.
Suppose some given data points each belong to one of two classes, and
the goal is to decide which class a new data point will be in. In the
case of support vector machines, a data point is viewed as a p
{\\displaystyle p} -dimensional vector (a list of p {\\displaystyle p}
numbers), and we want to know whether we can separate such points with a
( p − 1 ) {\\displaystyle (p-1)} -dimensional hyperplane. This is called
a linear classifier. There are many hyperplanes that might classify the
data. One reasonable choice as the best hyperplane is the one that
represents the largest separation, or margin, between the two classes.
So we choose the hyperplane so that the distance from it to the nearest
data point on each side is maximized. If such a hyperplane exists, it is
known as the maximum-margin hyperplane and the linear classifier it
defines is known as a maximum-margin classifier; or equivalently, the
perceptron of optimal stability.More formally, a support vector machine
constructs a hyperplane or set of hyperplanes in a high or
infinite-dimensional space, which can be used for classification,
regression, or other tasks like outliers detection. Intuitively, a good
separation is achieved by the hyperplane that has the largest distance
to the nearest training-data point of any class (so-called functional
margin), since in general the larger the margin, the lower the
generalization error of the classifier. Whereas the original problem may
be stated in a finite-dimensional space, it often happens that the sets
to discriminate are not linearly separable in that space. For this
reason, it was proposed that the original finite-dimensional space be
mapped into a much higher-dimensional space, presumably making the
separation easier in that space. To keep the computational load
reasonable, the mappings used by SVM schemes are designed to ensure that
dot products of pairs of input data vectors may be computed easily in
terms of the variables in the original space, by defining them in terms
of a kernel function k ( x , y ) {\\displaystyle k(x,y)} selected to
suit the problem. The hyperplanes in the higher-dimensional space are
defined as the set of points whose dot product with a vector in that
space is constant, where such a set of vectors is an orthogonal (and
thus minimal) set of vectors that defines a hyperplane. The vectors
defining the hyperplanes can be chosen to be linear combinations with
parameters α i {\\displaystyle \\alpha \_{i}} of images of feature
vectors x i {\\displaystyle x\_{i}} that occur in the data base. With
this choice of a hyperplane, the points x {\\displaystyle x} in the
feature space that are mapped into the hyperplane are defined by the
relation ∑ i α i k ( x i , x ) = constant . {\\displaystyle \\textstyle
\\sum \_{i}\\alpha \_{i}k(x\_{i},x)={\\text{constant}}.} Note that if k
( x , y ) {\\displaystyle k(x,y)} becomes small as y {\\displaystyle y}
grows further away from x {\\displaystyle x} , each term in the sum
measures the degree of closeness of the test point x {\\displaystyle x}
to the corresponding data base point x i {\\displaystyle x\_{i}} . In
this way, the sum of kernels above can be used to measure the relative
nearness of each test point to the data points originating in one or the
other of the sets to be discriminated. Note the fact that the set of
points x {\\displaystyle x} mapped into any hyperplane can be quite
convoluted as a result, allowing much more complex discrimination
between sets that are not convex at all in the original space.
Applications SVMs can be used to solve various real-world problems: SVMs
are helpful in text and hypertext categorization, as their application
can significantly reduce the need for labeled training instances in both
the standard inductive and transductive settings. Some methods for
shallow semantic parsing are based on support vector machines.
Classification of images can also be performed using SVMs. Experimental
results show that SVMs achieve significantly higher search accuracy than
traditional query refinement schemes after just three to four rounds of
relevance feedback. This is also true for image segmentation systems,
including those using a modified version SVM that uses the privileged
approach as suggested by Vapnik. Classification of satellite data like
SAR data using supervised SVM. Hand-written characters can be recognized
using SVM. The SVM algorithm has been widely applied in the biological
and other sciences. They have been used to classify proteins with up to
90% of the compounds classified correctly. Permutation tests based on
SVM weights have been suggested as a mechanism for interpretation of SVM
models. Support vector machine weights have also been used to interpret
SVM models in the past. Posthoc interpretation of support vector machine
models in order to identify features used by the model to make
predictions is a relatively new area of research with special
significance in the biological sciences. History The original SVM
algorithm was invented by Vladimir N. Vapnik and Alexey Ya. Chervonenkis
in 1964. In 1992, Bernhard Boser, Isabelle Guyon and Vladimir Vapnik
suggested a way to create nonlinear classifiers by applying the kernel
trick to maximum-margin hyperplanes. The \"soft margin\" incarnation, as
is commonly used in software packages, was proposed by Corinna Cortes
and Vapnik in 1993 and published in 1995. Linear SVM We are given a
training dataset of n {\\displaystyle n} points of the form where the y
i {\\displaystyle y\_{i}} are either 1 or −1, each indicating the class
to which the point x i {\\displaystyle \\mathbf {x} \_{i}} belongs. Each
x i {\\displaystyle \\mathbf {x} \_{i}} is a p {\\displaystyle p}
-dimensional real vector. We want to find the \"maximum-margin
hyperplane\" that divides the group of points x i {\\displaystyle
\\mathbf {x} \_{i}} for which y i = 1 {\\displaystyle y\_{i}=1} from the
group of points for which y i = − 1 {\\displaystyle y\_{i}=-1} , which
is defined so that the distance between the hyperplane and the nearest
point x i {\\displaystyle \\mathbf {x} \_{i}} from either group is
maximized. Any hyperplane can be written as the set of points x
{\\displaystyle \\mathbf {x} } satisfying where w {\\displaystyle
\\mathbf {w} } is the (not necessarily normalized) normal vector to the
hyperplane. This is much like Hesse normal form, except that w
{\\displaystyle \\mathbf {w} } is not necessarily a unit vector. The
parameter b ‖ w ‖ {\\displaystyle {\\tfrac {b}{\\\|\\mathbf {w} \\\|}}}
determines the offset of the hyperplane from the origin along the normal
vector w {\\displaystyle \\mathbf {w} } . Hard-margin If the training
data is linearly separable, we can select two parallel hyperplanes that
separate the two classes of data, so that the distance between them is
as large as possible. The region bounded by these two hyperplanes is
called the \"margin\", and the maximum-margin hyperplane is the
hyperplane that lies halfway between them. With a normalized or
standardized dataset, these hyperplanes can be described by the
equations w T x − b = 1 {\\displaystyle \\mathbf {w} \^{\\mathsf
{T}}\\mathbf {x} -b=1} (anything on or above this boundary is of one
class, with label 1)and w T x − b = − 1 {\\displaystyle \\mathbf {w}
\^{\\mathsf {T}}\\mathbf {x} -b=-1} (anything on or below this boundary
is of the other class, with label −1).Geometrically, the distance
between these two hyperplanes is 2 ‖ w ‖ {\\displaystyle {\\tfrac
{2}{\\\|\\mathbf {w} \\\|}}} , so to maximize the distance between the
planes we want to minimize ‖ w ‖ {\\displaystyle \\\|\\mathbf {w} \\\|}
. The distance is computed using the distance from a point to a plane
equation. We also have to prevent data points from falling into the
margin, we add the following constraint: for each i {\\displaystyle i}
either or These constraints state that each data point must lie on the
correct side of the margin. This can be rewritten as We can put this
together to get the optimization problem: minimize w , b ‖ w ‖ 2 2
subject to y i ( w ⊤ x i − b ) ≥ 1 ∀ i ∈ { 1 , ... , n } {\\displaystyle
{\\begin{aligned}&{\\underset {\\mathbf {w} ,\\;b}{\\operatorname
{minimize} }}&&\\\|\\mathbf {w} \\\|\_{2}\^{2}\\\\&{\\text{subject
to}}&&y\_{i}(\\mathbf {w} \^{\\top }\\mathbf {x} \_{i}-b)\\geq 1\\quad
\\forall i\\in \\{1,\\dots ,n\\}\\end{aligned}}} The w {\\displaystyle
\\mathbf {w} } and b {\\displaystyle b} that solve this problem
determine our classifier, x ↦ sgn ⁡ ( w T x − b ) {\\displaystyle
\\mathbf {x} \\mapsto \\operatorname {sgn}(\\mathbf {w} \^{\\mathsf
{T}}\\mathbf {x} -b)} where sgn ⁡ ( ⋅ ) {\\displaystyle \\operatorname
{sgn}(\\cdot )} is the sign function. An important consequence of this
geometric description is that the max-margin hyperplane is completely
determined by those x i {\\displaystyle \\mathbf {x} \_{i}} that lie
nearest to it. These x i {\\displaystyle \\mathbf {x} \_{i}} are called
support vectors. Soft-margin To extend SVM to cases in which the data
are not linearly separable, the hinge loss function is helpful Note that
y i {\\displaystyle y\_{i}} is the i-th target (i.e., in this case, 1 or
−1), and w T x i − b {\\displaystyle \\mathbf {w} \^{\\mathsf
{T}}\\mathbf {x} \_{i}-b} is the i-th output. This function is zero if
the constraint in (1) is satisfied, in other words, if x i
{\\displaystyle \\mathbf {x} \_{i}} lies on the correct side of the
margin. For data on the wrong side of the margin, the function\'s value
is proportional to the distance from the margin. The goal of the
optimization then is to minimize where the parameter λ \> 0
{\\displaystyle \\lambda \>0} determines the trade-off between
increasing the margin size and ensuring that the x i {\\displaystyle
\\mathbf {x} \_{i}} lie on the correct side of the margin. By
deconstructing the hinge loss, this optimization problem can be massaged
into the following: minimize w , b , ζ ‖ w ‖ 2 2 + C ∑ i = 1 n ζ i
subject to y i ( w ⊤ x i − b ) ≥ 1 − ζ i , ζ i ≥ 0 ∀ i ∈ { 1 , ... , n }
{\\displaystyle {\\begin{aligned}&{\\underset {\\mathbf {w}
,\\;b,\\;\\mathbf {\\zeta } }{\\operatorname {minimize} }}&&\\\|\\mathbf
{w} \\\|\_{2}\^{2}+C\\sum \_{i=1}\^{n}\\zeta \_{i}\\\\&{\\text{subject
to}}&&y\_{i}(\\mathbf {w} \^{\\top }\\mathbf {x} \_{i}-b)\\geq 1-\\zeta
\_{i},\\quad \\zeta \_{i}\\geq 0\\quad \\forall i\\in \\{1,\\dots
,n\\}\\end{aligned}}} Thus, for large values of C {\\displaystyle C} ,
it will behave similar to the hard-margin SVM, if the input data are
linearly classifiable, but will still learn if a classification rule is
viable or not. ( λ {\\displaystyle \\lambda } is inversely related to C
{\\displaystyle C} , e.g. in LIBSVM.) Nonlinear Kernels The original
maximum-margin hyperplane algorithm proposed by Vapnik in 1963
constructed a linear classifier. However, in 1992, Bernhard Boser,
Isabelle Guyon and Vladimir Vapnik suggested a way to create nonlinear
classifiers by applying the kernel trick (originally proposed by
Aizerman et al.) to maximum-margin hyperplanes. The resulting algorithm
is formally similar, except that every dot product is replaced by a
nonlinear kernel function. This allows the algorithm to fit the
maximum-margin hyperplane in a transformed feature space. The
transformation may be nonlinear and the transformed space
high-dimensional; although the classifier is a hyperplane in the
transformed feature space, it may be nonlinear in the original input
space. It is noteworthy that working in a higher-dimensional feature
space increases the generalization error of support vector machines,
although given enough samples the algorithm still performs well.Some
common kernels include: Polynomial (homogeneous): k ( x i , x j ) = ( x
i ⋅ x j ) d {\\displaystyle k(\\mathbf {x} \_{i},\\mathbf {x}
\_{j})=(\\mathbf {x} \_{i}\\cdot \\mathbf {x} \_{j})\^{d}} .
Particularly, when d = 1 {\\displaystyle d=1} , this becomes the linear
kernel. Polynomial (inhomogeneous): k ( x i , x j ) = ( x i ⋅ x j + r )
d {\\displaystyle k(\\mathbf {x} \_{i},\\mathbf {x} \_{j})=(\\mathbf {x}
\_{i}\\cdot \\mathbf {x} \_{j}+r)\^{d}} . Gaussian radial basis
function: k ( x i , x j ) = exp ⁡ ( − γ ‖ x i − x j ‖ 2 ) {\\displaystyle
k(\\mathbf {x} \_{i},\\mathbf {x} \_{j})=\\exp \\left(-\\gamma
\\left\\\|\\mathbf {x} \_{i}-\\mathbf {x} \_{j}\\right\\\|\^{2}\\right)}
for γ \> 0 {\\displaystyle \\gamma \>0} . Sometimes parametrized using γ
= 1 / ( 2 σ 2 ) {\\displaystyle \\gamma =1/(2\\sigma \^{2})} . Sigmoid
function (Hyperbolic tangent): k ( x i , x j ) = tanh ⁡ ( κ x i ⋅ x j + c
) {\\displaystyle k(\\mathbf {x\_{i}} ,\\mathbf {x\_{j}}
)=\\tanh(\\kappa \\mathbf {x} \_{i}\\cdot \\mathbf {x} \_{j}+c)} for
some (not every) κ \> 0 {\\displaystyle \\kappa \>0} and c \< 0
{\\displaystyle c\<0} .The kernel is related to the transform φ ( x i )
{\\displaystyle \\varphi (\\mathbf {x} \_{i})} by the equation k ( x i ,
x j ) = φ ( x i ) ⋅ φ ( x j ) {\\displaystyle k(\\mathbf {x}
\_{i},\\mathbf {x} \_{j})=\\varphi (\\mathbf {x} \_{i})\\cdot \\varphi
(\\mathbf {x\_{j}} )} . The value w is also in the transformed space,
with w = ∑ i α i y i φ ( x i ) {\\textstyle \\mathbf {w} =\\sum
\_{i}\\alpha \_{i}y\_{i}\\varphi (\\mathbf {x} \_{i})} . Dot products
with w for classification can again be computed by the kernel trick,
i.e. w ⋅ φ ( x ) = ∑ i α i y i k ( x i , x ) {\\textstyle \\mathbf {w}
\\cdot \\varphi (\\mathbf {x} )=\\sum \_{i}\\alpha \_{i}y\_{i}k(\\mathbf
{x} \_{i},\\mathbf {x} )} . Computing the SVM classifier Computing the
(soft-margin) SVM classifier amounts to minimizing an expression of the
form We focus on the soft-margin classifier since, as noted above,
choosing a sufficiently small value for λ {\\displaystyle \\lambda }
yields the hard-margin classifier for linearly classifiable input data.
The classical approach, which involves reducing (2) to a quadratic
programming problem, is detailed below. Then, more recent approaches
such as sub-gradient descent and coordinate descent will be discussed.
Primal Minimizing (2) can be rewritten as a constrained optimization
problem with a differentiable objective function in the following way.
For each i ∈ { 1 , ... , n } {\\displaystyle i\\in \\{1,\\,\\ldots
,\\,n\\}} we introduce a variable ζ i = max ( 0 , 1 − y i ( w T x i − b
) ) {\\displaystyle \\zeta \_{i}=\\max \\left(0,1-y\_{i}(\\mathbf {w}
\^{\\mathsf {T}}\\mathbf {x} \_{i}-b)\\right)} . Note that ζ i
{\\displaystyle \\zeta \_{i}} is the smallest nonnegative number
satisfying y i ( w T x i − b ) ≥ 1 − ζ i . {\\displaystyle
y\_{i}(\\mathbf {w} \^{\\mathsf {T}}\\mathbf {x} \_{i}-b)\\geq 1-\\zeta
\_{i}.} Thus we can rewrite the optimization problem as follows This is
called the primal problem. Dual By solving for the Lagrangian dual of
the above problem, one obtains the simplified problem This is called the
dual problem. Since the dual maximization problem is a quadratic
function of the c i {\\displaystyle c\_{i}} subject to linear
constraints, it is efficiently solvable by quadratic programming
algorithms. Here, the variables c i {\\displaystyle c\_{i}} are defined
such that Moreover, c i = 0 {\\displaystyle c\_{i}=0} exactly when x i
{\\displaystyle \\mathbf {x} \_{i}} lies on the correct side of the
margin, and 0 \< c i \< ( 2 n λ ) − 1 {\\displaystyle 0
