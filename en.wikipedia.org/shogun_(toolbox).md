Shogun is a free, open-source machine learning software library written
in C++. It offers numerous algorithms and data structures for machine
learning problems. It offers interfaces for Octave, Python, R, Java,
Lua, Ruby and C# using SWIG. It is licensed under the terms of the GNU
General Public License version 3 or later. Description The focus of
Shogun is on kernel machines such as support vector machines for
regression and classification problems. Shogun also offers a full
implementation of Hidden Markov models. The core of Shogun is written in
C++ and offers interfaces for MATLAB, Octave, Python, R, Java, Lua, Ruby
and C#. Shogun has been under active development since 1999. Today there
is a vibrant user community all over the world using Shogun as a base
for research and education, and contributing to the core package.
Supported algorithms Currently Shogun supports the following algorithms:
Support vector machines Dimensionality reduction algorithms, such as
PCA, Kernel PCA, Locally Linear Embedding, Hessian Locally Linear
Embedding, Local Tangent Space Alignment, Linear Local Tangent Space
Alignment, Kernel Locally Linear Embedding, Kernel Local Tangent Space
Alignment, Multidimensional Scaling, Isomap, Diffusion Maps, Laplacian
Eigenmaps Online learning algorithms such as SGD-QN, Vowpal Wabbit
Clustering algorithms: k-means and GMM Kernel Ridge Regression, Support
Vector Regression Hidden Markov Models K-Nearest Neighbors Linear
discriminant analysis Kernel Perceptrons.Many different kernels are
implemented, ranging from kernels for numerical data (such as gaussian
or linear kernels) to kernels on special data (such as strings over
certain alphabets). The currently implemented kernels for numeric data
include: linear gaussian polynomial sigmoid kernelsThe supported kernels
for special data include: Spectrum Weighted Degree Weighted Degree with
ShiftsThe latter group of kernels allows processing of arbitrary
sequences over fixed alphabets such as DNA sequences as well as whole
e-mail texts. Special features As Shogun was developed with
bioinformatics applications in mind it is capable of processing huge
datasets consisting of up to 10 million samples. Shogun supports the use
of pre-calculated kernels. It is also possible to use a combined kernel
i.e. a kernel consisting of a linear combination of arbitrary kernels
over different domains. The coefficients or weights of the linear
combination can be learned as well. For this purpose Shogun offers a
multiple kernel learning functionality. References S. Sonnenburg, G.
Rätsch, S. Henschel, C. Widmer, J. Behr, A. Zien, F. De Bona, A. Binder,
C. Gehl and V. Franc: The SHOGUN Machine Learning Toolbox, Journal of
Machine Learning Research, 11:1799−1802, June 11, 2010. M. Gashler.
Waffles: A Machine Learning Toolkit. Journal of Machine Learning
Research, 12 (July):2383--2387, 2011. P. Vincent, Y. Bengio, N.
Chapados, and O. Delalleau. Plearn high-performance machine learning
library. URL http://plearn.berlios.de/. External links Shogun toolbox
homepage shogun on GitHub \"SHOGUN\". Freecode.
