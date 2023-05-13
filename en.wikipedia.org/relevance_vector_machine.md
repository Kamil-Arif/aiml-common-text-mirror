In mathematics, a Relevance Vector Machine (RVM) is a machine learning
technique that uses Bayesian inference to obtain parsimonious solutions
for regression and probabilistic classification. The RVM has an
identical functional form to the support vector machine, but provides
probabilistic classification. It is actually equivalent to a Gaussian
process model with covariance function: k ( x , x ′ ) = ∑ j = 1 N 1 α j
φ ( x , x j ) φ ( x ′ , x j ) {\\displaystyle k(\\mathbf {x} ,\\mathbf
{x\'} )=\\sum \_{j=1}\^{N}{\\frac {1}{\\alpha \_{j}}}\\varphi (\\mathbf
{x} ,\\mathbf {x} \_{j})\\varphi (\\mathbf {x} \',\\mathbf {x} \_{j})}
where φ {\\displaystyle \\varphi } is the kernel function (usually
Gaussian), α j {\\displaystyle \\alpha \_{j}} are the variances of the
prior on the weight vector w ∼ N ( 0 , α − 1 I ) {\\displaystyle w\\sim
N(0,\\alpha \^{-1}I)} , and x 1 , ... , x N {\\displaystyle \\mathbf {x}
\_{1},\\ldots ,\\mathbf {x} \_{N}} are the input vectors of the training
set.Compared to that of support vector machines (SVM), the Bayesian
formulation of the RVM avoids the set of free parameters of the SVM
(that usually require cross-validation-based post-optimizations).
However RVMs use an expectation maximization (EM)-like learning method
and are therefore at risk of local minima. This is unlike the standard
sequential minimal optimization (SMO)-based algorithms employed by SVMs,
which are guaranteed to find a global optimum (of the convex problem).
The relevance vector machine was patented in the United States by
Microsoft (patent expired September 4, 2019). See also Kernel trick
Platt scaling: turns an SVM into a probability model References Software
dlib C++ Library The Kernel-Machine Library rvmbinary: R package for
binary classification scikit-rvm fast-scikit-rvm, rvm tutorial External
links Tipping\'s webpage on Sparse Bayesian Models and the RVM A
Tutorial on RVM by Tristan Fletcher Applied tutorial on RVM Comparison
of RVM and SVM
