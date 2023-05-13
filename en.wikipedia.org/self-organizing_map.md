A self-organizing map (SOM) or self-organizing feature map (SOFM) is an
unsupervised machine learning technique used to produce a
low-dimensional (typically two-dimensional) representation of a higher
dimensional data set while preserving the topological structure of the
data. For example, a data set with p {\\displaystyle p} variables
measured in n {\\displaystyle n} observations could be represented as
clusters of observations with similar values for the variables. These
clusters then could be visualized as a two-dimensional \"map\" such that
observations in proximal clusters have more similar values than
observations in distal clusters. This can make high-dimensional data
easier to visualize and analyze. An SOM is a type of artificial neural
network but is trained using competitive learning rather than the
error-correction learning (e.g., backpropagation with gradient descent)
used by other artificial neural networks. The SOM was introduced by the
Finnish professor Teuvo Kohonen in the 1980s and therefore is sometimes
called a Kohonen map or Kohonen network. The Kohonen map or network is a
computationally convenient abstraction building on biological models of
neural systems from the 1970s and morphogenesis models dating back to
Alan Turing in the 1950s. SOMs create internal representations
reminiscent of the cortical homunculus, a distorted representation of
the human body, based on a neurological \"map\" of the areas and
proportions of the human brain dedicated to processing sensory
functions, for different parts of the body. Overview Self-organizing
maps, like most artificial neural networks, operate in two modes:
training and mapping. First, training uses an input data set (the
\"input space\") to generate a lower-dimensional representation of the
input data (the \"map space\"). Second, mapping classifies additional
input data using the generated map. In most cases, the goal of training
is to represent an input space with p dimensions as a map space with two
dimensions. Specifically, an input space with p variables is said to
have p dimensions. A map space consists of components called \"nodes\"
or \"neurons,\" which are arranged as a hexagonal or rectangular grid
with two dimensions. The number of nodes and their arrangement are
specified beforehand based on the larger goals of the analysis and
exploration of the data. Each node in the map space is associated with a
\"weight\" vector, which is the position of the node in the input space.
While nodes in the map space stay fixed, training consists in moving
weight vectors toward the input data (reducing a distance metric such as
Euclidean distance) without spoiling the topology induced from the map
space. After training, the map can be used to classify additional
observations for the input space by finding the node with the closest
weight vector (smallest distance metric) to the input space vector.
Learning algorithm The goal of learning in the self-organizing map is to
cause different parts of the network to respond similarly to certain
input patterns. This is partly motivated by how visual, auditory or
other sensory information is handled in separate parts of the cerebral
cortex in the human brain. The weights of the neurons are initialized
either to small random values or sampled evenly from the subspace
spanned by the two largest principal component eigenvectors. With the
latter alternative, learning is much faster because the initial weights
already give a good approximation of SOM weights.The network must be fed
a large number of example vectors that represent, as close as possible,
the kinds of vectors expected during mapping. The examples are usually
administered several times as iterations. The training utilizes
competitive learning. When a training example is fed to the network, its
Euclidean distance to all weight vectors is computed. The neuron whose
weight vector is most similar to the input is called the best matching
unit (BMU). The weights of the BMU and neurons close to it in the SOM
grid are adjusted towards the input vector. The magnitude of the change
decreases with time and with the grid-distance from the BMU. The update
formula for a neuron v with weight vector Wv(s) is W v ( s + 1 ) = W v (
s ) + θ ( u , v , s ) ⋅ α ( s ) ⋅ ( D ( t ) − W v ( s ) )
{\\displaystyle W\_{v}(s+1)=W\_{v}(s)+\\theta (u,v,s)\\cdot \\alpha
(s)\\cdot (D(t)-W\_{v}(s))} ,where s is the step index, t is an index
into the training sample, u is the index of the BMU for the input vector
D(t), α(s) is a monotonically decreasing learning coefficient; θ(u, v,
s) is the neighborhood function which gives the distance between the
neuron u and the neuron v in step s. Depending on the implementations, t
can scan the training data set systematically (t is 0, 1, 2\...T-1, then
repeat, T being the training sample\'s size), be randomly drawn from the
data set (bootstrap sampling), or implement some other sampling method
(such as jackknifing). The neighborhood function θ(u, v, s) (also called
function of lateral interaction) depends on the grid-distance between
the BMU (neuron u) and neuron v. In the simplest form, it is 1 for all
neurons close enough to BMU and 0 for others, but the Gaussian and
mexican-hat functions are common choices, too. Regardless of the
functional form, the neighborhood function shrinks with time. At the
beginning when the neighborhood is broad, the self-organizing takes
place on the global scale. When the neighborhood has shrunk to just a
couple of neurons, the weights are converging to local estimates. In
some implementations, the learning coefficient α and the neighborhood
function θ decrease steadily with increasing s, in others (in particular
those where t scans the training data set) they decrease in step-wise
fashion, once every T steps. This process is repeated for each input
vector for a (usually large) number of cycles λ. The network winds up
associating output nodes with groups or patterns in the input data set.
If these patterns can be named, the names can be attached to the
associated nodes in the trained net. During mapping, there will be one
single winning neuron: the neuron whose weight vector lies closest to
the input vector. This can be simply determined by calculating the
Euclidean distance between input vector and weight vector. While
representing input data as vectors has been emphasized in this article,
any kind of object which can be represented digitally, which has an
appropriate distance measure associated with it, and in which the
necessary operations for training are possible can be used to construct
a self-organizing map. This includes matrices, continuous functions or
even other self-organizing maps. Variables These are the variables
needed, with vectors in bold, s {\\displaystyle s} is the current
iteration λ {\\displaystyle \\lambda } is the iteration limit t
{\\displaystyle t} is the index of the target input data vector in the
input data set D {\\displaystyle \\mathbf {D} } D ( t ) {\\displaystyle
{D}(t)} is a target input data vector v {\\displaystyle v} is the index
of the node in the map W v {\\displaystyle \\mathbf {W} \_{v}} is the
current weight vector of node v {\\displaystyle v} u {\\displaystyle u}
is the index of the best matching unit (BMU) in the map θ ( u , v , s )
{\\displaystyle \\theta (u,v,s)} is a restraint due to distance from
BMU, usually called the neighbourhood function, and α ( s )
{\\displaystyle \\alpha (s)} is a learning restraint due to iteration
progress. Algorithm Randomize the node weight vectors in a map Randomly
pick an input vector D ( t ) {\\displaystyle {D}(t)} Traverse each node
in the map Use the Euclidean distance formula to find the similarity
between the input vector and the map\'s node\'s weight vector Track the
node that produces the smallest distance (this node is the best matching
unit, BMU) Update the weight vectors of the nodes in the neighborhood of
the BMU (including the BMU itself) by pulling them closer to the input
vector W v ( s + 1 ) = W v ( s ) + θ ( u , v , s ) ⋅ α ( s ) ⋅ ( D ( t )
− W v ( s ) ) {\\displaystyle W\_{v}(s+1)=W\_{v}(s)+\\theta
(u,v,s)\\cdot \\alpha (s)\\cdot (D(t)-W\_{v}(s))} Increase s
{\\displaystyle s} and repeat from step 2 while s \< λ {\\displaystyle
s\<\\lambda } Alternative algorithm Randomize the map\'s nodes\' weight
vectors Traverse each input vector in the input data set Traverse each
node in the map Use the Euclidean distance formula to find the
similarity between the input vector and the map\'s node\'s weight vector
Track the node that produces the smallest distance (this node is the
best matching unit, BMU) Update the nodes in the neighborhood of the BMU
(including the BMU itself) by pulling them closer to the input vector W
v ( s + 1 ) = W v ( s ) + θ ( u , v , s ) ⋅ α ( s ) ⋅ ( D ( t ) − W v (
s ) ) {\\displaystyle W\_{v}(s+1)=W\_{v}(s)+\\theta (u,v,s)\\cdot
\\alpha (s)\\cdot (D(t)-W\_{v}(s))} Increase s {\\displaystyle s} and
repeat from step 2 while s \< λ {\\displaystyle s\<\\lambda }
Initialization options Selection of initial weights as good
approximations of the final weights is a well-known problem for all
iterative methods of artificial neural networks, including
self-organizing maps. Kohonen originally proposed random initiation of
weights. (This approach is reflected by the algorithms described above.)
More recently, principal component initialization, in which initial map
weights are chosen from the space of the first principal components, has
become popular due to the exact reproducibility of the results.A careful
comparison of random initialization to principal component
initialization for a one-dimensional map, however, found that the
advantages of principal component initialization are not universal. The
best initialization method depends on the geometry of the specific
dataset. Principal component initialization was preferable (for a
one-dimensional map) when the principal curve approximating the dataset
could be univalently and linearly projected on the first principal
component (quasilinear sets). For nonlinear datasets, however, random
initiation performed better. Interpretation There are two ways to
interpret a SOM. Because in the training phase weights of the whole
neighborhood are moved in the same direction, similar items tend to
excite adjacent neurons. Therefore, SOM forms a semantic map where
similar samples are mapped close together and dissimilar ones apart.
This may be visualized by a U-Matrix (Euclidean distance between weight
vectors of neighboring cells) of the SOM.The other way is to think of
neuronal weights as pointers to the input space. They form a discrete
approximation of the distribution of training samples. More neurons
point to regions with high training sample concentration and fewer where
the samples are scarce. SOM may be considered a nonlinear generalization
of Principal components analysis (PCA). It has been shown, using both
artificial and real geophysical data, that SOM has many advantages over
the conventional feature extraction methods such as Empirical Orthogonal
Functions (EOF) or PCA. Originally, SOM was not formulated as a solution
to an optimisation problem. Nevertheless, there have been several
attempts to modify the definition of SOM and to formulate an
optimisation problem which gives similar results. For example, Elastic
maps use the mechanical metaphor of elasticity to approximate principal
manifolds: the analogy is an elastic membrane and plate. Examples
Fisher\'s iris flower data Consider an n×m array of nodes, each of which
contains a weight vector and is aware of its location in the array. Each
weight vector is of the same dimension as the node\'s input vector. The
weights may initially be set to random values. Now we need input to feed
the map. Colors can be represented by their red, green, and blue
components. Consequently, we will represent colors as vectors in the
unit cube of the free vector space over ℝ generated by the basis: R =
\<255, 0, 0\> G = \<0, 255, 0\> B = \<0, 0, 255\> The diagram shown
compares the results of training on the data setsthreeColors = \[255, 0,
0\], \[0, 255, 0\], \[0, 0, 255\] eightColors = \[0, 0, 0\], \[255, 0,
0\], \[0, 255, 0\], \[0, 0, 255\], \[255, 255, 0\], \[0, 255, 255\],
\[255, 0, 255\], \[255, 255, 255\]and the original images. Note the
striking resemblance between the two. Similarly, after training a 40×40
grid of neurons for 250 iterations with a learning rate of 0.1 on
Fisher\'s Iris, the map can already detect the main differences between
species. Other Project prioritization and selection Investigating the
banking as well as the interbank payment business Seismic facies
analysis for oil and gas exploration Failure mode and effects analysis
Finding representative data in large datasets representative species for
ecological communities representative days for energy system models
Alternatives The generative topographic map (GTM) is a potential
alternative to SOMs. In the sense that a GTM explicitly requires a
smooth and continuous mapping from the input space to the map space, it
is topology preserving. However, in a practical sense, this measure of
topological preservation is lacking. The time adaptive self-organizing
map (TASOM) network is an extension of the basic SOM. The TASOM employs
adaptive learning rates and neighborhood functions. It also includes a
scaling parameter to make the network invariant to scaling, translation
and rotation of the input space. The TASOM and its variants have been
used in several applications including adaptive clustering, multilevel
thresholding, input space approximation, and active contour modeling.
Moreover, a Binary Tree TASOM or BTASOM, resembling a binary natural
tree having nodes composed of TASOM networks has been proposed where the
number of its levels and the number of its nodes are adaptive with its
environment. The growing self-organizing map (GSOM) is a growing variant
of the self-organizing map. The GSOM was developed to address the issue
of identifying a suitable map size in the SOM. It starts with a minimal
number of nodes (usually four) and grows new nodes on the boundary based
on a heuristic. By using a value called the spread factor, the data
analyst has the ability to control the growth of the GSOM. The elastic
maps approach borrows from the spline interpolation the idea of
minimization of the elastic energy. In learning, it minimizes the sum of
quadratic bending and stretching energy with the least squares
approximation error. The conformal approach that uses conformal mapping
to interpolate each training sample between grid nodes in a continuous
surface. A one-to-one smooth mapping is possible in this approach. The
oriented and scalable map (OS-Map) generalises the neighborhood function
and the winner selection. The homogeneous Gaussian neighborhood function
is replaced with the matrix exponential. Thus one can specify the
orientation either in the map space or in the data space. SOM has a
fixed scale (=1), so that the maps \"optimally describe the domain of
observation\". But what about a map covering the domain twice or in
n-folds? This entails the conception of scaling. The OS-Map regards the
scale as a statistical description of how many best-matching nodes an
input has in the map. See also Deep learning Hybrid Kohonen
self-organizing map Learning vector quantization Liquid state machine
Neocognitron Neural gas Sparse coding Sparse distributed memory
Topological data analysis Notes References Further reading Rustum,
Rabee, Adebayo Adeloye, and Aurore Simala (2007). \"Kohonen
self-organising map (KSOM) extracted features for enhancing MLP-ANN
prediction models of BOD5\" (PDF). International Symposium:
Quantification and Reduction of Predictive Uncertainty for Sustainable
Water Resources Management-24th General Assembly of the International
Union of Geodesy and Geophysics (IUGG). pp. 181--7. ISBN
978-1-901502-14-5. External links Media related to Self-organizing maps
at Wikimedia Commons
