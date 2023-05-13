A multilayer perceptron (MLP) is a fully connected class of feedforward
artificial neural network (ANN). The term MLP is used ambiguously,
sometimes loosely to mean any feedforward ANN, sometimes strictly to
refer to networks composed of multiple layers of perceptrons (with
threshold activation); see § Terminology. Multilayer perceptrons are
sometimes colloquially referred to as \"vanilla\" neural networks,
especially when they have a single hidden layer.An MLP consists of at
least three layers of nodes: an input layer, a hidden layer and an
output layer. Except for the input nodes, each node is a neuron that
uses a nonlinear activation function. MLP utilizes a chain rule based
supervised learning technique called backpropagation or reverse mode of
automatic differentiation for training. Its multiple layers and
non-linear activation distinguish MLP from a linear perceptron. It can
distinguish data that is not linearly separable. Theory Activation
function If a multilayer perceptron has a linear activation function in
all neurons, that is, a linear function that maps the weighted inputs to
the output of each neuron, then linear algebra shows that any number of
layers can be reduced to a two-layer input-output model. In MLPs some
neurons use a nonlinear activation function that was developed to model
the frequency of action potentials, or firing, of biological neurons.
The two historically common activation functions are both sigmoids, and
are described by y ( v i ) = tanh ⁡ ( v i ) and y ( v i ) = ( 1 + e − v i
) − 1 {\\displaystyle y(v\_{i})=\\tanh(v\_{i})\~\~{\\textrm
{and}}\~\~y(v\_{i})=(1+e\^{-v\_{i}})\^{-1}} .The first is a hyperbolic
tangent that ranges from -1 to 1, while the other is the logistic
function, which is similar in shape but ranges from 0 to 1. Here y i
{\\displaystyle y\_{i}} is the output of the i {\\displaystyle i} th
node (neuron) and v i {\\displaystyle v\_{i}} is the weighted sum of the
input connections. Alternative activation functions have been proposed,
including the rectifier and softplus functions. More specialized
activation functions include radial basis functions (used in radial
basis networks, another class of supervised neural network models). In
recent developments of deep learning the rectified linear unit (ReLU) is
more frequently used as one of the possible ways to overcome the
numerical problems related to the sigmoids. Layers The MLP consists of
three or more layers (an input and an output layer with one or more
hidden layers) of nonlinearly-activating nodes. Since MLPs are fully
connected, each node in one layer connects with a certain weight w i j
{\\displaystyle w\_{ij}} to every node in the following layer. Learning
Learning occurs in the perceptron by changing connection weights after
each piece of data is processed, based on the amount of error in the
output compared to the expected result. This is an example of supervised
learning, and is carried out through backpropagation, a generalization
of the least mean squares algorithm in the linear perceptron. We can
represent the degree of error in an output node j {\\displaystyle j} in
the n {\\displaystyle n} th data point (training example) by e j ( n ) =
d j ( n ) − y j ( n ) {\\displaystyle e\_{j}(n)=d\_{j}(n)-y\_{j}(n)} ,
where d j ( n ) {\\displaystyle d\_{j}(n)} is the desired target value
for n {\\displaystyle n} th data point at node j {\\displaystyle j} ,
and y j ( n ) {\\displaystyle y\_{j}(n)} is the value produced by the
perceptron at node j {\\displaystyle j} when the n {\\displaystyle n} th
data point is given as an input. The node weights can then be adjusted
based on corrections that minimize the error in the entire output for
the n {\\displaystyle n} th data point, given by E ( n ) = 1 2 ∑ output
node j e j 2 ( n ) {\\displaystyle {\\mathcal {E}}(n)={\\frac
{1}{2}}\\sum \_{{\\text{output node }}j}e\_{j}\^{2}(n)} .Using gradient
descent, the change in each weight w i j {\\displaystyle w\_{ij}} is Δ w
j i ( n ) = − η ∂ E ( n ) ∂ v j ( n ) y i ( n ) {\\displaystyle \\Delta
w\_{ji}(n)=-\\eta {\\frac {\\partial {\\mathcal {E}}(n)}{\\partial
v\_{j}(n)}}y\_{i}(n)} where y i ( n ) {\\displaystyle y\_{i}(n)} is the
output of the previous neuron i {\\displaystyle i} , and η
{\\displaystyle \\eta } is the learning rate, which is selected to
ensure that the weights quickly converge to a response, without
oscillations. In the previous expression, ∂ E ( n ) ∂ v j ( n )
{\\displaystyle {\\frac {\\partial {\\mathcal {E}}(n)}{\\partial
v\_{j}(n)}}} denotes the partial derivate of the error E ( n )
{\\displaystyle {\\mathcal {E}}(n)} according to the weighted sum v j (
n ) {\\displaystyle v\_{j}(n)} of the input connections of neuron i
{\\displaystyle i} . The derivative to be calculated depends on the
induced local field v j {\\displaystyle v\_{j}} , which itself varies.
It is easy to prove that for an output node this derivative can be
simplified to − ∂ E ( n ) ∂ v j ( n ) = e j ( n ) ϕ ′ ( v j ( n ) )
{\\displaystyle -{\\frac {\\partial {\\mathcal {E}}(n)}{\\partial
v\_{j}(n)}}=e\_{j}(n)\\phi \^{\\prime }(v\_{j}(n))} where ϕ ′
{\\displaystyle \\phi \^{\\prime }} is the derivative of the activation
function described above, which itself does not vary. The analysis is
more difficult for the change in weights to a hidden node, but it can be
shown that the relevant derivative is − ∂ E ( n ) ∂ v j ( n ) = ϕ ′ ( v
j ( n ) ) ∑ k − ∂ E ( n ) ∂ v k ( n ) w k j ( n ) {\\displaystyle
-{\\frac {\\partial {\\mathcal {E}}(n)}{\\partial v\_{j}(n)}}=\\phi
\^{\\prime }(v\_{j}(n))\\sum \_{k}-{\\frac {\\partial {\\mathcal
{E}}(n)}{\\partial v\_{k}(n)}}w\_{kj}(n)} .This depends on the change in
weights of the k {\\displaystyle k} th nodes, which represent the output
layer. So to change the hidden layer weights, the output layer weights
change according to the derivative of the activation function, and so
this algorithm represents a backpropagation of the activation function.
Terminology The term \"multilayer perceptron\" does not refer to a
single perceptron that has multiple layers. Rather, it contains many
perceptrons that are organized into layers. An alternative is
\"multilayer perceptron network\". Moreover, MLP \"perceptrons\" are not
perceptrons in the strictest possible sense. True perceptrons are
formally a special case of artificial neurons that use a threshold
activation function such as the Heaviside step function. MLP perceptrons
can employ arbitrary activation functions. A true perceptron performs
binary classification, an MLP neuron is free to either perform
classification or regression, depending upon its activation function.
The term \"multilayer perceptron\" later was applied without respect to
nature of the nodes/layers, which can be composed of arbitrarily defined
artificial neurons, and not perceptrons specifically. This
interpretation avoids the loosening of the definition of \"perceptron\"
to mean an artificial neuron in general. History Frank Rosenblatt, who
published the Perceptron in 1958, also introduced an MLP with 3 layers:
an input layer, a hidden layer with randomized weights that did not
learn, and an output layer. Since only the output layer had learning
connections, this was not yet deep learning. It was what later was
called an extreme learning machine.The first deep learning MLP was
published by Alexey Grigorevich Ivakhnenko and Valentin Lapa in 1965, as
the Group Method of Data Handling.The first deep learning MLP trained by
stochastic gradient descent was published in 1967 by Shun\'ichi Amari.
In computer experiments conducted by Amari\'s student Saito, a five
layer MLP with two modifiable layers learned internal representations
required to classify non-linearily separable pattern classes.In 1970,
Seppo Linnainmaa published the general method for automatic
differentiation of discrete connected networks of nested differentiable
functions. This became known as backpropagation or reverse mode of
automatic differentiation. It is an efficient application of the chain
rule derived by Gottfried Wilhelm Leibniz in 1673 to networks of
differentiable nodes. The terminology \"back-propagating errors\" was
actually introduced in 1962 by Rosenblatt himself, but he did not know
how to implement this, although Henry J. Kelley had a continuous
precursor of backpropagation already in 1960 in the context of control
theory. In 1982, Paul Werbos applied backpropagation to MLPs in the way
that has become standard. In 1985, David E. Rumelhart et al. published
an experimental analysis of the technique. Many improvements have been
implemented in subsequent decades.As late as 2021, a very simple NN
architecture combining two MLPs with skip connections and layer
normalizations was designed and called MLP-Mixer; its realizations
featuring 19 to 431 millions of parameters were shown to be comparable
to visual transformers of similar size om ImageNet and similar image
classification tasks. Applications MLPs are useful in research for their
ability to solve problems stochastically, which often allows approximate
solutions for extremely complex problems like fitness approximation.
MLPs are universal function approximators as shown by Cybenko\'s
theorem, so they can be used to create mathematical models by regression
analysis. As classification is a particular case of regression when the
response variable is categorical, MLPs make good classifier algorithms.
MLPs were a popular machine learning solution in the 1980s, finding
applications in diverse fields such as speech recognition, image
recognition, and machine translation software, but thereafter faced
strong competition from much simpler (and related) support vector
machines. Interest in backpropagation networks returned due to the
successes of deep learning. References External links Weka: Open source
data mining software with multilayer perceptron implementation. Neuroph
Studio documentation, implements this algorithm and a few others.
