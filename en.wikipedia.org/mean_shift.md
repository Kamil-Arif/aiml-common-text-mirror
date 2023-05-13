Mean shift is a non-parametric feature-space mathematical analysis
technique for locating the maxima of a density function, a so-called
mode-seeking algorithm. Application domains include cluster analysis in
computer vision and image processing. History The mean shift procedure
is usually credited to work by Fukunaga and Hostetler in 1975. It is,
however, reminiscent of earlier work by Schnell in 1964. Overview Mean
shift is a procedure for locating the maxima---the modes---of a density
function given discrete data sampled from that function. This is an
iterative method, and we start with an initial estimate x
{\\displaystyle x} . Let a kernel function K ( x i − x ) {\\displaystyle
K(x\_{i}-x)} be given. This function determines the weight of nearby
points for re-estimation of the mean. Typically a Gaussian kernel on the
distance to the current estimate is used, K ( x i − x ) = e − c \| \| x
i − x \| \| 2 {\\displaystyle K(x\_{i}-x)=e\^{-c\|\|x\_{i}-x\|\|\^{2}}}
. The weighted mean of the density in the window determined by K
{\\displaystyle K} is m ( x ) = ∑ x i ∈ N ( x ) K ( x i − x ) x i ∑ x i
∈ N ( x ) K ( x i − x ) {\\displaystyle m(x)={\\frac {\\sum
\_{x\_{i}\\in N(x)}K(x\_{i}-x)x\_{i}}{\\sum \_{x\_{i}\\in
N(x)}K(x\_{i}-x)}}} where N ( x ) {\\displaystyle N(x)} is the
neighborhood of x {\\displaystyle x} , a set of points for which K ( x i
− x ) ≠ 0 {\\displaystyle K(x\_{i}-x)\\neq 0} . The difference m ( x ) −
x {\\displaystyle m(x)-x} is called mean shift in Fukunaga and
Hostetler. The mean-shift algorithm now sets x ← m ( x ) {\\displaystyle
x\\leftarrow m(x)} , and repeats the estimation until m ( x )
{\\displaystyle m(x)} converges. Although the mean shift algorithm has
been widely used in many applications, a rigid proof for the convergence
of the algorithm using a general kernel in a high dimensional space is
still not known. Aliyari Ghassabeh showed the convergence of the mean
shift algorithm in one dimension with a differentiable, convex, and
strictly decreasing profile function. However, the one-dimensional case
has limited real world applications. Also, the convergence of the
algorithm in higher dimensions with a finite number of the stationary
(or isolated) points has been proved. However, sufficient conditions for
a general kernel function to have finite stationary (or isolated) points
have not been provided. Gaussian Mean-Shift is an
Expectation--maximization algorithm. Details Let data be a finite set S
{\\displaystyle S} embedded in the n {\\displaystyle n} -dimensional
Euclidean space, X {\\displaystyle X} . Let K {\\displaystyle K} be a
flat kernel that is the characteristic function of the λ {\\displaystyle
\\lambda } -ball in X {\\displaystyle X} , In each iteration of the
algorithm, s ← m ( s ) {\\displaystyle s\\leftarrow m(s)} is performed
for all s ∈ S {\\displaystyle s\\in S} simultaneously. The first
question, then, is how to estimate the density function given a sparse
set of samples. One of the simplest approaches is to just smooth the
data, e.g., by convolving it with a fixed kernel of width h
{\\displaystyle h} , where x i {\\displaystyle x\_{i}} are the input
samples and k ( r ) {\\displaystyle k(r)} is the kernel function (or
Parzen window). h {\\displaystyle h} is the only parameter in the
algorithm and is called the bandwidth. This approach is known as kernel
density estimation or the Parzen window technique. Once we have computed
f ( x ) {\\displaystyle f(x)} from the equation above, we can find its
local maxima using gradient ascent or some other optimization technique.
The problem with this \"brute force\" approach is that, for higher
dimensions, it becomes computationally prohibitive to evaluate f ( x )
{\\displaystyle f(x)} over the complete search space. Instead, mean
shift uses a variant of what is known in the optimization literature as
multiple restart gradient descent. Starting at some guess for a local
maximum, y k {\\displaystyle y\_{k}} , which can be a random input data
point x 1 {\\displaystyle x\_{1}} , mean shift computes the gradient of
the density estimate f ( x ) {\\displaystyle f(x)} at y k
{\\displaystyle y\_{k}} and takes an uphill step in that direction.
Types of kernels Kernel definition: Let X {\\displaystyle X} be the n
{\\displaystyle n} -dimensional Euclidean space, R n {\\displaystyle
\\mathbb {R} \^{n}} . The norm of x {\\displaystyle x} is a non-negative
number, ‖ x ‖ 2 = x ⊤ x ≥ 0 {\\displaystyle \\\|x\\\|\^{2}=x\^{\\top
}x\\geq 0} . A function K : X → R {\\displaystyle K:X\\rightarrow
\\mathbb {R} } is said to be a kernel if there exists a profile, k : \[
0 , ∞ \] → R {\\displaystyle k:\[0,\\infty \]\\rightarrow \\mathbb {R} }
, such that K ( x ) = k ( ‖ x ‖ 2 ) {\\displaystyle
K(x)=k(\\\|x\\\|\^{2})} and k is non-negative. k is non-increasing: k (
a ) ≥ k ( b ) {\\displaystyle k(a)\\geq k(b)} if a \< b {\\displaystyle
a
