In artificial neural networks, the activation function of a node defines
the output of that node given an input or set of inputs. A standard
integrated circuit can be seen as a digital network of activation
functions that can be \"ON\" (1) or \"OFF\" (0), depending on input.
This is similar to the linear perceptron in neural networks. However,
only nonlinear activation functions allow such networks to compute
nontrivial problems using only a small number of nodes, and such
activation functions are called nonlinearities. Classification of
activation functions The most common activation functions can be divided
in three categories: ridge functions, radial functions and fold
functions. An activation function f {\\displaystyle f} is saturating if
lim \| v \| → ∞ \| ∇ f ( v ) \| = 0 {\\displaystyle \\lim \_{\|v\|\\to
\\infty }\|\\nabla f(v)\|=0} . It is nonsaturating if it is not
saturating. Non-saturating activation functions, such as ReLU, may be
better than saturating activation functions, as they don\'t suffer from
vanishing gradient. Ridge activation functions Ridge functions are
multivariate functions acting on a linear combination of the input
variables. Often used examples include: Linear activation: ϕ ( v ) = a +
v ′ b {\\displaystyle \\phi (\\mathbf {v} )=a+\\mathbf {v} \'\\mathbf
{b} } , ReLU activation: ϕ ( v ) = max ( 0 , a + v ′ b ) {\\displaystyle
\\phi (\\mathbf {v} )=\\max(0,a+\\mathbf {v} \'\\mathbf {b} )} ,
Heaviside activation: ϕ ( v ) = 1 a + v ′ b \> 0 {\\displaystyle \\phi
(\\mathbf {v} )=1\_{a+\\mathbf {v} \'\\mathbf {b} \>0}} , Logistic
activation: ϕ ( v ) = ( 1 + exp ⁡ ( − a − v ′ b ) ) − 1 {\\displaystyle
\\phi (\\mathbf {v} )=(1+\\exp(-a-\\mathbf {v} \'\\mathbf {b} ))\^{-1}}
.In biologically inspired neural networks, the activation function is
usually an abstraction representing the rate of action potential firing
in the cell. In its simplest form, this function is binary---that is,
either the neuron is firing or not. The function looks like ϕ ( v ) = U
( a + v ′ b ) {\\displaystyle \\phi (\\mathbf {v} )=U(a+\\mathbf {v}
\'\\mathbf {b} )} , where U {\\displaystyle U} is the Heaviside step
function. A line of positive slope may be used to reflect the increase
in firing rate that occurs as input current increases. Such a function
would be of the form ϕ ( v ) = a + v ′ b {\\displaystyle \\phi (\\mathbf
{v} )=a+\\mathbf {v} \'\\mathbf {b} } . Neurons also cannot fire faster
than a certain rate, motivating sigmoid activation functions whose range
is a finite interval. Radial activation functions A special class of
activation functions known as radial basis functions (RBFs) are used in
RBF networks, which are extremely efficient as universal function
approximators. These activation functions can take many forms, but they
are usually found as one of the following functions: Gaussian: ϕ ( v ) =
exp ⁡ ( − ‖ v − c ‖ 2 2 σ 2 ) {\\displaystyle \\,\\phi (\\mathbf {v}
)=\\exp \\left(-{\\frac {\\\|\\mathbf {v} -\\mathbf {c}
\\\|\^{2}}{2\\sigma \^{2}}}\\right)} Multiquadratics: ϕ ( v ) = ‖ v − c
‖ 2 + a 2 {\\displaystyle \\,\\phi (\\mathbf {v} )={\\sqrt {\\\|\\mathbf
{v} -\\mathbf {c} \\\|\^{2}+a\^{2}}}} Inverse multiquadratics: ϕ ( v ) =
( ‖ v − c ‖ 2 + a 2 ) − 1 2 {\\displaystyle \\,\\phi (\\mathbf {v}
)=\\left(\\\|\\mathbf {v} -\\mathbf {c}
\\\|\^{2}+a\^{2}\\right)\^{-{\\frac {1}{2}}}} Polyharmonic splineswhere
c {\\displaystyle \\mathbf {c} } is the vector representing the function
center and a {\\displaystyle a} and σ {\\displaystyle \\sigma } are
parameters affecting the spread of the radius. Folding activation
functions Folding activation functions are extensively used in the
pooling layers in convolutional neural networks, and in output layers of
multiclass classification networks. These activations perform
aggregation over the inputs, such as taking the mean, minimum or
maximum. In multiclass classification the softmax activation is often
used. Comparison of activation functions There are numerous activation
functions. Hinton et al.\'s seminal 2012 paper on automatic speech
recognition uses a logistic sigmoid activation function. The seminal
2012 AlexNet computer vision architecture uses the ReLU activation
function, as did the seminal 2015 computer vision architecture ResNet.
The seminal 2018 language processing model BERT uses a smooth version of
the ReLU, the GELU.Aside from their empirical performance, activation
functions also have different mathematical properties: Nonlinear When
the activation function is non-linear, then a two-layer neural network
can be proven to be a universal function approximator. This is known as
the Universal Approximation Theorem. The identity activation function
does not satisfy this property. When multiple layers use the identity
activation function, the entire network is equivalent to a single-layer
model. Range When the range of the activation function is finite,
gradient-based training methods tend to be more stable, because pattern
presentations significantly affect only limited weights. When the range
is infinite, training is generally more efficient because pattern
presentations significantly affect most of the weights. In the latter
case, smaller learning rates are typically necessary. Continuously
differentiable This property is desirable (ReLU is not continuously
differentiable and has some issues with gradient-based optimization, but
it is still possible) for enabling gradient-based optimization methods.
The binary step activation function is not differentiable at 0, and it
differentiates to 0 for all other values, so gradient-based methods can
make no progress with it.These properties do not decisively influence
performance, nor are they the only mathematical properties that may be
useful. For instance, the strictly positive range of the softplus makes
it suitable for predicting variances in variational autoencoders. Table
of activation functions The following table compares the properties of
several activation functions that are functions of one fold x from the
previous layer or layers: The following table lists activation functions
that are not functions of a single fold x from the previous layer or
layers: \^ Here, δ i j {\\displaystyle \\delta \_{ij}} is the Kronecker
delta. \^ For instance, j {\\displaystyle j} could be iterating through
the number of kernels of the previous neural network layer while i
{\\displaystyle i} iterates through the number of kernels of the current
layer. See also Logistic function Rectifier (neural networks) Stability
(learning theory) Softmax function == References ==
