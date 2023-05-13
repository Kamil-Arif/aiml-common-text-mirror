An artificial neuron is a mathematical function conceived as a model of
biological neurons, a neural network. Artificial neurons are elementary
units in an artificial neural network. The artificial neuron receives
one or more inputs (representing excitatory postsynaptic potentials and
inhibitory postsynaptic potentials at neural dendrites) and sums them to
produce an output (or activation, representing a neuron\'s action
potential which is transmitted along its axon). Usually each input is
separately weighted, and the sum is passed through a non-linear function
known as an activation function or transfer function. The transfer
functions usually have a sigmoid shape, but they may also take the form
of other non-linear functions, piecewise linear functions, or step
functions. They are also often monotonically increasing, continuous,
differentiable and bounded. Non-monotonic, unbounded and oscillating
activation functions with multiple zeros that outperform sigmoidal and
ReLU like activation functions on many tasks have also been recently
explored. The thresholding function has inspired building logic gates
referred to as threshold logic; applicable to building logic circuits
resembling brain processing. For example, new devices such as memristors
have been extensively used to develop such logic in recent times.The
artificial neuron transfer function should not be confused with a linear
system\'s transfer function. Artificial neurons can also refer to
artificial cells in neuromorphic engineering (see below) that are
similar to natural physical neurons. Basic structure For a given
artificial neuron k, let there be m + 1 inputs with signals x0 through
xm and weights wk0 through wkm. Usually, the x0 input is assigned the
value +1, which makes it a bias input with wk0 = bk. This leaves only m
actual inputs to the neuron: from x1 to xm. The output of the kth neuron
is: y k = φ ( ∑ j = 0 m w k j x j ) {\\displaystyle y\_{k}=\\varphi
\\left(\\sum \_{j=0}\^{m}w\_{kj}x\_{j}\\right)} Where φ {\\displaystyle
\\varphi } (phi) is the transfer function (commonly a threshold
function). The output is analogous to the axon of a biological neuron,
and its value propagates to the input of the next layer, through a
synapse. It may also exit the system, possibly as part of an output
vector. It has no learning process as such. Its transfer function
weights are calculated and threshold value are predetermined. Types
Depending on the specific model used they may be called a semi-linear
unit, Nv neuron, binary neuron, linear threshold function, or
McCulloch--Pitts (MCP) neuron. Simple artificial neurons, such as the
McCulloch--Pitts model, are sometimes described as \"caricature
models\", since they are intended to reflect one or more
neurophysiological observations, but without regard to realism.
Biological models Artificial neurons are designed to mimic aspects of
their biological counterparts. However a significant performance gap
exists between biological and artificial neural networks. In particular
single biological neurons in the human brain with oscillating activation
function capable of learning the XOR function have been discovered.
Dendrites -- In a biological neuron, the dendrites act as the input
vector. These dendrites allow the cell to receive signals from a large
(\>1000) number of neighboring neurons. As in the above mathematical
treatment, each dendrite is able to perform \"multiplication\" by that
dendrite\'s \"weight value.\" The multiplication is accomplished by
increasing or decreasing the ratio of synaptic neurotransmitters to
signal chemicals introduced into the dendrite in response to the
synaptic neurotransmitter. A negative multiplication effect can be
achieved by transmitting signal inhibitors (i.e. oppositely charged
ions) along the dendrite in response to the reception of synaptic
neurotransmitters. Soma -- In a biological neuron, the soma acts as the
summation function, seen in the above mathematical description. As
positive and negative signals (exciting and inhibiting, respectively)
arrive in the soma from the dendrites, the positive and negative ions
are effectively added in summation, by simple virtue of being mixed
together in the solution inside the cell\'s body. Axon -- The axon gets
its signal from the summation behavior which occurs inside the soma. The
opening to the axon essentially samples the electrical potential of the
solution inside the soma. Once the soma reaches a certain potential, the
axon will transmit an all-in signal pulse down its length. In this
regard, the axon behaves as the ability for us to connect our artificial
neuron to other artificial neurons.Unlike most artificial neurons,
however, biological neurons fire in discrete pulses. Each time the
electrical potential inside the soma reaches a certain threshold, a
pulse is transmitted down the axon. This pulsing can be translated into
continuous values. The rate (activations per second, etc.) at which an
axon fires converts directly into the rate at which neighboring cells
get signal ions introduced into them. The faster a biological neuron
fires, the faster nearby neurons accumulate electrical potential (or
lose electrical potential, depending on the \"weighting\" of the
dendrite that connects to the neuron that fired). It is this conversion
that allows computer scientists and mathematicians to simulate
biological neural networks using artificial neurons which can output
distinct values (often from −1 to 1). Encoding Research has shown that
unary coding is used in the neural circuits responsible for birdsong
production. The use of unary in biological networks is presumably due to
the inherent simplicity of the coding. Another contributing factor could
be that unary coding provides a certain degree of error correction.
Physical artificial cells There is research and development into
physical artificial neurons -- organic and inorganic. For example, some
artificial neurons can receive and release dopamine (chemical signals
rather than electrical signals) and communicate with natural rat muscle
and brain cells, with potential for use in BCIs/prosthetics.Low-power
biocompatible memristors may enable construction of artificial neurons
which function at voltages of biological action potentials and could be
used to directly process biosensing signals, for neuromorphic computing
and/or direct communication with biological neurons.Organic neuromorphic
circuits made out of polymers, coated with an ion-rich gel to enable a
material to carry an electric charge like real neurons, have been built
into a robot, enabling it to learn sensorimotorically within the real
world, rather than via simulations or virtually. Moreover, artificial
spiking neurons made of soft matter (polymers) can operate in
biologically relevant environments and enable the synergetic
communication between the artificial and biological domains. History The
first artificial neuron was the Threshold Logic Unit (TLU), or Linear
Threshold Unit, first proposed by Warren McCulloch and Walter Pitts in
1943. The model was specifically targeted as a computational model of
the \"nerve net\" in the brain. As a transfer function, it employed a
threshold, equivalent to using the Heaviside step function. Initially,
only a simple model was considered, with binary inputs and outputs, some
restrictions on the possible weights, and a more flexible threshold
value. Since the beginning it was already noticed that any boolean
function could be implemented by networks of such devices, what is
easily seen from the fact that one can implement the AND and OR
functions, and use them in the disjunctive or the conjunctive normal
form. Researchers also soon realized that cyclic networks, with
feedbacks through neurons, could define dynamical systems with memory,
but most of the research concentrated (and still does) on strictly
feed-forward networks because of the smaller difficulty they present.
One important and pioneering artificial neural network that used the
linear threshold function was the perceptron, developed by Frank
Rosenblatt. This model already considered more flexible weight values in
the neurons, and was used in machines with adaptive capabilities. The
representation of the threshold values as a bias term was introduced by
Bernard Widrow in 1960 -- see ADALINE. In the late 1980s, when research
on neural networks regained strength, neurons with more continuous
shapes started to be considered. The possibility of differentiating the
activation function allows the direct use of the gradient descent and
other optimization algorithms for the adjustment of the weights. Neural
networks also started to be used as a general function approximation
model. The best known training algorithm called backpropagation has been
rediscovered several times but its first development goes back to the
work of Paul Werbos. Types of transfer functions The transfer function
(activation function) of a neuron is chosen to have a number of
properties which either enhance or simplify the network containing the
neuron. Crucially, for instance, any multilayer perceptron using a
linear transfer function has an equivalent single-layer network; a
non-linear function is therefore necessary to gain the advantages of a
multi-layer network.Below, u refers in all cases to the weighted sum of
all the inputs to the neuron, i.e. for n inputs, u = ∑ i = 1 n w i x i
{\\displaystyle u=\\sum \_{i=1}\^{n}w\_{i}x\_{i}} where w is a vector of
synaptic weights and x is a vector of inputs. Step function The output y
of this transfer function is binary, depending on whether the input
meets a specified threshold, θ. The \"signal\" is sent, i.e. the output
is set to one, if the activation meets the threshold. y = { 1 if u ≥ θ 0
if u \< θ {\\displaystyle y={\\begin{cases}1&{\\text{if }}u\\geq \\theta
\\\\0&{\\text{if }}u\<\\theta \\end{cases}}} This function is used in
perceptrons and often shows up in many other models. It performs a
division of the space of inputs by a hyperplane. It is specially useful
in the last layer of a network intended to perform binary classification
of the inputs. It can be approximated from other sigmoidal functions by
assigning large values to the weights. Linear combination In this case,
the output unit is simply the weighted sum of its inputs plus a bias
term. A number of such linear neurons perform a linear transformation of
the input vector. This is usually more useful in the first layers of a
network. A number of analysis tools exist based on linear models, such
as harmonic analysis, and they can all be used in neural networks with
this linear neuron. The bias term allows us to make affine
transformations to the data. See: Linear transformation, Harmonic
analysis, Linear filter, Wavelet, Principal component analysis,
Independent component analysis, Deconvolution. Sigmoid A fairly simple
non-linear function, the sigmoid function such as the logistic function
also has an easily calculated derivative, which can be important when
calculating the weight updates in the network. It thus makes the network
more easily manipulable mathematically, and was attractive to early
computer scientists who needed to minimize the computational load of
their simulations. It was previously commonly seen in multilayer
perceptrons. However, recent work has shown sigmoid neurons to be less
effective than rectified linear neurons. The reason is that the
gradients computed by the backpropagation algorithm tend to diminish
towards zero as activations propagate through layers of sigmoidal
neurons, making it difficult to optimize neural networks using multiple
layers of sigmoidal neurons. Rectifier In the context of artificial
neural networks, the rectifier or ReLU (Rectified Linear Unit) is an
activation function defined as the positive part of its argument: f ( x
) = x + = max ( 0 , x ) , {\\displaystyle f(x)=x\^{+}=\\max(0,x),} where
x is the input to a neuron. This is also known as a ramp function and is
analogous to half-wave rectification in electrical engineering. This
activation function was first introduced to a dynamical network by
Hahnloser et al. in a 2000 paper in Nature with strong biological
motivations and mathematical justifications. It has been demonstrated
for the first time in 2011 to enable better training of deeper networks,
compared to the widely used activation functions prior to 2011, i.e.,
the logistic sigmoid (which is inspired by probability theory; see
logistic regression) and its more practical counterpart, the hyperbolic
tangent. A commonly used variant of the ReLU activation function is the
Leaky ReLU which allows a small, positive gradient when the unit is not
active: f ( x ) = { x if x \> 0 , a x otherwise . {\\displaystyle
f(x)={\\begin{cases}x&{\\text{if
}}x\>0,\\\\ax&{\\text{otherwise}}.\\end{cases}}} where x is the input to
the neuron and a is a small positive constant (in the original paper the
value 0.01 was used for a). Pseudocode algorithm The following is a
simple pseudocode implementation of a single TLU which takes boolean
inputs (true or false), and returns a single boolean output when
activated. An object-oriented model is used. No method of training is
defined, since several exist. If a purely functional model were used,
the class TLU below would be replaced with a function TLU with input
parameters threshold, weights, and inputs that returned a boolean value.
class TLU defined as: data member threshold : number data member weights
: list of numbers of size X function member fire(inputs : list of
booleans of size X) : boolean defined as: variable T : number T ← 0 for
each i in 1 to X do if inputs(i) is true then T ← T + weights(i) end if
end for each if T \> threshold then return true else: return false end
if end function end class See also Binding neuron Connectionism
References Further reading External links Artifical \[sic\] neuron
mimicks function of human cells McCulloch-Pitts Neurons (Overview)
