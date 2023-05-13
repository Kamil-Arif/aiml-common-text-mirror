In applied mathematics, k-SVD is a dictionary learning algorithm for
creating a dictionary for sparse representations, via a singular value
decomposition approach. k-SVD is a generalization of the k-means
clustering method, and it works by iteratively alternating between
sparse coding the input data based on the current dictionary, and
updating the atoms in the dictionary to better fit the data. It is
structurally related to the expectation maximization (EM) algorithm.
k-SVD can be found widely in use in applications such as image
processing, audio processing, biology, and document analysis. k-SVD
algorithm k-SVD is a kind of generalization of k-means, as follows. The
k-means clustering can be also regarded as a method of sparse
representation. That is, finding the best possible codebook to represent
the data samples { y i } i = 1 M {\\displaystyle
\\{y\_{i}\\}\_{i=1}\^{M}} by nearest neighbor, by solving min D , X { ‖
Y − D X ‖ F 2 } subject to ∀ i , x i = e k for some k . {\\displaystyle
\\quad \\min \\limits \_{D,X}\\{\\\|Y-DX\\\|\_{F}\^{2}\\}\\qquad
{\\text{subject to }}\\forall i,x\_{i}=e\_{k}{\\text{ for some }}k.}
which is nearly equivalent to min D , X { ‖ Y − D X ‖ F 2 } subject to ∀
i , ‖ x i ‖ 0 = 1 {\\displaystyle \\quad \\min \\limits
\_{D,X}\\{\\\|Y-DX\\\|\_{F}\^{2}\\}\\qquad {\\text{subject to }}\\quad
\\forall i,\\\|x\_{i}\\\|\_{0}=1} which is k-means that allows
\"weights\". The letter F denotes the Frobenius norm. The sparse
representation term x i = e k {\\displaystyle x\_{i}=e\_{k}} enforces
k-means algorithm to use only one atom (column) in dictionary D
{\\displaystyle D} . To relax this constraint, the target of the k-SVD
algorithm is to represent signal as a linear combination of atoms in D
{\\displaystyle D} . The k-SVD algorithm follows the construction flow
of the k-means algorithm. However, in contrary to k-means, in order to
achieve a linear combination of atoms in D {\\displaystyle D} , the
sparsity term of the constraint is relaxed so that the number of nonzero
entries of each column x i {\\displaystyle x\_{i}} can be more than 1,
but less than a number T 0 {\\displaystyle T\_{0}} . So, the objective
function becomes min D , X { ‖ Y − D X ‖ F 2 } subject to ∀ i , ‖ x i ‖
0 ≤ T 0 . {\\displaystyle \\quad \\min \\limits
\_{D,X}\\{\\\|Y-DX\\\|\_{F}\^{2}\\}\\qquad {\\text{subject to }}\\quad
\\forall i\\;,\\\|x\_{i}\\\|\_{0}\\leq T\_{0}.} or in another objective
form min D , X ∑ i ‖ x i ‖ 0 subject to ∀ i , ‖ Y − D X ‖ F 2 ≤ ϵ .
{\\displaystyle \\quad \\min \\limits \_{D,X}\\sum
\_{i}\\\|x\_{i}\\\|\_{0}\\qquad {\\text{subject to }}\\quad \\forall
i\\;,\\\|Y-DX\\\|\_{F}\^{2}\\leq \\epsilon .} In the k-SVD algorithm,
the D {\\displaystyle D} is first fixed and the best coefficient matrix
X {\\displaystyle X} is found. As finding the truly optimal X
{\\displaystyle X} is hard, we use an approximation pursuit method. Any
algorithm such as OMP, the orthogonal matching pursuit can be used for
the calculation of the coefficients, as long as it can supply a solution
with a fixed and predetermined number of nonzero entries T 0
{\\displaystyle T\_{0}} . After the sparse coding task, the next is to
search for a better dictionary D {\\displaystyle D} . However, finding
the whole dictionary all at a time is impossible, so the process is to
update only one column of the dictionary D {\\displaystyle D} each time,
while fixing X {\\displaystyle X} . The update of the k {\\displaystyle
k} -th column is done by rewriting the penalty term as ‖ Y − D X ‖ F 2 =
‖ Y − ∑ j = 1 K d j x j T ‖ F 2 = ‖ ( Y − ∑ j ≠ k d j x j T ) − d k x k
T ‖ F 2 = ‖ E k − d k x k T ‖ F 2 {\\displaystyle
\\\|Y-DX\\\|\_{F}\^{2}=\\left\\\|Y-\\sum
\_{j=1}\^{K}d\_{j}x\_{j}\^{\\text{T}}\\right\\\|\_{F}\^{2}=\\left\\\|\\left(Y-\\sum
\_{j\\neq
k}d\_{j}x\_{j}\^{\\text{T}}\\right)-d\_{k}x\_{k}\^{\\text{T}}\\right\\\|\_{F}\^{2}=\\\|E\_{k}-d\_{k}x\_{k}\^{\\text{T}}\\\|\_{F}\^{2}}
where x k T {\\displaystyle x\_{k}\^{\\text{T}}} denotes the k-th row of
X. By decomposing the multiplication D X {\\displaystyle DX} into sum of
K {\\displaystyle K} rank 1 matrices, we can assume the other K − 1
{\\displaystyle K-1} terms are assumed fixed, and the k {\\displaystyle
k} -th remains unknown. After this step, we can solve the minimization
problem by approximate the E k {\\displaystyle E\_{k}} term with a r a n
k − 1 {\\displaystyle rank-1} matrix using singular value decomposition,
then update d k {\\displaystyle d\_{k}} with it. However, the new
solution of vector x k T {\\displaystyle x\_{k}\^{\\text{T}}} is very
likely to be filled, because the sparsity constraint is not enforced. To
cure this problem, define ω k {\\displaystyle \\omega \_{k}} as ω k = {
i ∣ 1 ≤ i ≤ N , x k T ( i ) ≠ 0 } , {\\displaystyle \\omega
\_{k}=\\{i\\mid 1\\leq i\\leq N,x\_{k}\^{\\text{T}}(i)\\neq 0\\},} which
points to examples { y i } i = 1 N {\\displaystyle
\\{y\_{i}\\}\_{i=1}\^{N}} that use atom d k {\\displaystyle d\_{k}}
(also the entries of x i {\\displaystyle x\_{i}} that is nonzero). Then,
define Ω k {\\displaystyle \\Omega \_{k}} as a matrix of size N × \| ω k
\| {\\displaystyle N\\times \|\\omega \_{k}\|} , with ones on the ( i ,
ω k ( i ) ) th {\\displaystyle (i,\\omega \_{k}(i)){\\text{th}}} entries
and zeros otherwise. When multiplying x \~ k T = x k T Ω k
{\\displaystyle {\\tilde
{x}}\_{k}\^{\\text{T}}=x\_{k}\^{\\text{T}}\\Omega \_{k}} , this shrinks
the row vector x k T {\\displaystyle x\_{k}\^{\\text{T}}} by discarding
the zero entries. Similarly, the multiplication Y \~ k = Y Ω k
{\\displaystyle {\\tilde {Y}}\_{k}=Y\\Omega \_{k}} is the subset of the
examples that are current using the d k {\\displaystyle d\_{k}} atom.
The same effect can be seen on E \~ k = E k Ω k {\\displaystyle {\\tilde
{E}}\_{k}=E\_{k}\\Omega \_{k}} . So the minimization problem as
mentioned before becomes ‖ E k Ω k − d k x k T Ω k ‖ F 2 = ‖ E \~ k − d
k x \~ k T ‖ F 2 {\\displaystyle \\\|E\_{k}\\Omega
\_{k}-d\_{k}x\_{k}\^{\\text{T}}\\Omega \_{k}\\\|\_{F}\^{2}=\\\|{\\tilde
{E}}\_{k}-d\_{k}{\\tilde {x}}\_{k}\^{\\text{T}}\\\|\_{F}\^{2}} and can
be done by directly using SVD. SVD decomposes E \~ k {\\displaystyle
{\\tilde {E}}\_{k}} into U Δ V T {\\displaystyle U\\Delta
V\^{\\text{T}}} . The solution for d k {\\displaystyle d\_{k}} is the
first column of U, the coefficient vector x \~ k T {\\displaystyle
{\\tilde {x}}\_{k}\^{\\text{T}}} as the first column of V × Δ ( 1 , 1 )
{\\displaystyle V\\times \\Delta (1,1)} . After updating the whole
dictionary, the process then turns to iteratively solve X, then
iteratively solve D. Limitations Choosing an appropriate \"dictionary\"
for a dataset is a non-convex problem, and k-SVD operates by an
iterative update which does not guarantee to find the global optimum.
However, this is common to other algorithms for this purpose, and k-SVD
works fairly well in practice. See also Sparse approximation Singular
value decomposition Matrix norm k-means clustering Low-rank
approximation == References ==
