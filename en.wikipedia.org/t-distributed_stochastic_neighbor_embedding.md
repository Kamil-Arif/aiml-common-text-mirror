t-distributed stochastic neighbor embedding (t-SNE) is a statistical
method for visualizing high-dimensional data by giving each datapoint a
location in a two or three-dimensional map. It is based on Stochastic
Neighbor Embedding originally developed by Sam Roweis and Geoffrey
Hinton, where Laurens van der Maaten proposed the t-distributed variant.
It is a nonlinear dimensionality reduction technique for embedding
high-dimensional data for visualization in a low-dimensional space of
two or three dimensions. Specifically, it models each high-dimensional
object by a two- or three-dimensional point in such a way that similar
objects are modeled by nearby points and dissimilar objects are modeled
by distant points with high probability. The t-SNE algorithm comprises
two main stages. First, t-SNE constructs a probability distribution over
pairs of high-dimensional objects in such a way that similar objects are
assigned a higher probability while dissimilar points are assigned a
lower probability. Second, t-SNE defines a similar probability
distribution over the points in the low-dimensional map, and it
minimizes the Kullback--Leibler divergence (KL divergence) between the
two distributions with respect to the locations of the points in the
map. While the original algorithm uses the Euclidean distance between
objects as the base of its similarity metric, this can be changed as
appropriate. A Riemannian variant is UMAP. t-SNE has been used for
visualization in a wide range of applications, including genomics,
computer security research, natural language processing, music analysis,
cancer research, bioinformatics, geological domain interpretation, and
biomedical signal processing.While t-SNE plots often seem to display
clusters, the visual clusters can be influenced strongly by the chosen
parameterization and therefore a good understanding of the parameters
for t-SNE is necessary. Such \"clusters\" can be shown to even appear in
non-clustered data, and thus may be false findings. Interactive
exploration may thus be necessary to choose parameters and validate
results. It has been demonstrated that t-SNE is often able to recover
well-separated clusters, and with special parameter choices,
approximates a simple form of spectral clustering. Details Given a set
of N {\\displaystyle N} high-dimensional objects x 1 , ... , x N
{\\displaystyle \\mathbf {x} \_{1},\\dots ,\\mathbf {x} \_{N}} , t-SNE
first computes probabilities p i j {\\displaystyle p\_{ij}} that are
proportional to the similarity of objects x i {\\displaystyle \\mathbf
{x} \_{i}} and x j {\\displaystyle \\mathbf {x} \_{j}} , as follows. For
i ≠ j {\\displaystyle i\\neq j} , define p j ∣ i = exp ⁡ ( − ‖ x i − x j
‖ 2 / 2 σ i 2 ) ∑ k ≠ i exp ⁡ ( − ‖ x i − x k ‖ 2 / 2 σ i 2 )
{\\displaystyle p\_{j\\mid i}={\\frac {\\exp(-\\lVert \\mathbf {x}
\_{i}-\\mathbf {x} \_{j}\\rVert \^{2}/2\\sigma \_{i}\^{2})}{\\sum
\_{k\\neq i}\\exp(-\\lVert \\mathbf {x} \_{i}-\\mathbf {x} \_{k}\\rVert
\^{2}/2\\sigma \_{i}\^{2})}}} and set p i ∣ i = 0 {\\displaystyle
p\_{i\\mid i}=0} . Note that ∑ j p j ∣ i = 1 {\\displaystyle \\sum
\_{j}p\_{j\\mid i}=1} for all i {\\displaystyle i} . As Van der Maaten
and Hinton explained: \"The similarity of datapoint x j {\\displaystyle
x\_{j}} to datapoint x i {\\displaystyle x\_{i}} is the conditional
probability, p j \| i {\\displaystyle p\_{j\|i}} , that x i
{\\displaystyle x\_{i}} would pick x j {\\displaystyle x\_{j}} as its
neighbor if neighbors were picked in proportion to their probability
density under a Gaussian centered at x i {\\displaystyle x\_{i}} .\"Now
define p i j = p j ∣ i + p i ∣ j 2 N {\\displaystyle p\_{ij}={\\frac
{p\_{j\\mid i}+p\_{i\\mid j}}{2N}}} This is motivated because p i
{\\displaystyle p\_{i}} and p j {\\displaystyle p\_{j}} from the N
samples are estimated as 1/N, so the conditional probability can be
written as p i ∣ j = N p i j {\\displaystyle p\_{i\\mid j}=Np\_{ij}} and
p j ∣ i = N p j i {\\displaystyle p\_{j\\mid i}=Np\_{ji}} . Since p i j
= p j i {\\displaystyle p\_{ij}=p\_{ji}} , you can obtain previous
formula. Also note that p i i = 0 {\\displaystyle p\_{ii}=0} and ∑ i , j
p i j = 1 {\\displaystyle \\sum \_{i,j}p\_{ij}=1} . The bandwidth of the
Gaussian kernels σ i {\\displaystyle \\sigma \_{i}} is set in such a way
that the entropy of the conditional distribution equals a predefined
entropy using the bisection method. As a result, the bandwidth is
adapted to the density of the data: smaller values of σ i
{\\displaystyle \\sigma \_{i}} are used in denser parts of the data
space. Since the Gaussian kernel uses the Euclidean distance ‖ x i − x j
‖ {\\displaystyle \\lVert x\_{i}-x\_{j}\\rVert } , it is affected by the
curse of dimensionality, and in high dimensional data when distances
lose the ability to discriminate, the p i j {\\displaystyle p\_{ij}}
become too similar (asymptotically, they would converge to a constant).
It has been proposed to adjust the distances with a power transform,
based on the intrinsic dimension of each point, to alleviate this.t-SNE
aims to learn a d {\\displaystyle d} -dimensional map y 1 , ... , y N
{\\displaystyle \\mathbf {y} \_{1},\\dots ,\\mathbf {y} \_{N}} (with y i
∈ R d {\\displaystyle \\mathbf {y} \_{i}\\in \\mathbb {R} \^{d}} and d
{\\displaystyle d} typically chosen as 2 or 3) that reflects the
similarities p i j {\\displaystyle p\_{ij}} as well as possible. To this
end, it measures similarities q i j {\\displaystyle q\_{ij}} between two
points in the map y i {\\displaystyle \\mathbf {y} \_{i}} and y j
{\\displaystyle \\mathbf {y} \_{j}} , using a very similar approach.
Specifically, for i ≠ j {\\displaystyle i\\neq j} , define q i j
{\\displaystyle q\_{ij}} as q i j = ( 1 + ‖ y i − y j ‖ 2 ) − 1 ∑ k ∑ l
≠ k ( 1 + ‖ y k − y l ‖ 2 ) − 1 {\\displaystyle q\_{ij}={\\frac
{(1+\\lVert \\mathbf {y} \_{i}-\\mathbf {y} \_{j}\\rVert
\^{2})\^{-1}}{\\sum \_{k}\\sum \_{l\\neq k}(1+\\lVert \\mathbf {y}
\_{k}-\\mathbf {y} \_{l}\\rVert \^{2})\^{-1}}}} and set q i i = 0
{\\displaystyle q\_{ii}=0} . Herein a heavy-tailed Student
t-distribution (with one-degree of freedom, which is the same as a
Cauchy distribution) is used to measure similarities between
low-dimensional points in order to allow dissimilar objects to be
modeled far apart in the map. The locations of the points y i
{\\displaystyle \\mathbf {y} \_{i}} in the map are determined by
minimizing the (non-symmetric) Kullback--Leibler divergence of the
distribution P {\\displaystyle P} from the distribution Q
{\\displaystyle Q} , that is: K L ( P ∥ Q ) = ∑ i ≠ j p i j log ⁡ p i j q
i j {\\displaystyle \\mathrm {KL} \\left(P\\parallel Q\\right)=\\sum
\_{i\\neq j}p\_{ij}\\log {\\frac {p\_{ij}}{q\_{ij}}}} The minimization
of the Kullback--Leibler divergence with respect to the points y i
{\\displaystyle \\mathbf {y} \_{i}} is performed using gradient descent.
The result of this optimization is a map that reflects the similarities
between the high-dimensional inputs. Software The R package Rtsne
implements t-SNE in R. ELKI contains tSNE, also with Barnes-Hut
approximation scikit-learn, a popular machine learning library in Python
implements t-SNE with both exact solutions and the Barnes-Hut
approximation. Tensorboard, the visualization kit associated with
TensorFlow, also implements t-SNE (online version) References External
links Visualizing Data Using t-SNE, Google Tech Talk about t-SNE
Implementations of t-SNE in various languages, A link collection
maintained by Laurens van der Maaten
