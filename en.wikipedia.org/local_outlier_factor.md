In anomaly detection, the local outlier factor (LOF) is an algorithm
proposed by Markus M. Breunig, Hans-Peter Kriegel, Raymond T. Ng and
Jörg Sander in 2000 for finding anomalous data points by measuring the
local deviation of a given data point with respect to its neighbours.LOF
shares some concepts with DBSCAN and OPTICS such as the concepts of
\"core distance\" and \"reachability distance\", which are used for
local density estimation. Basic idea The local outlier factor is based
on a concept of a local density, where locality is given by k nearest
neighbors, whose distance is used to estimate the density. By comparing
the local density of an object to the local densities of its neighbors,
one can identify regions of similar density, and points that have a
substantially lower density than their neighbors. These are considered
to be outliers. The local density is estimated by the typical distance
at which a point can be \"reached\" from its neighbors. The definition
of \"reachability distance\" used in LOF is an additional measure to
produce more stable results within clusters. The \"reachability
distance\" used by LOF has some subtle details that are often found
incorrect in secondary sources, e.g., in the textbook of Ethem Alpaydin.
Formal Let k-distance(A) be the distance of the object A to the k-th
nearest neighbor. Note that the set of the k nearest neighbors includes
all objects at this distance, which can in the case of a \"tie\" be more
than k objects. We denote the set of k nearest neighbors as Nk(A). This
distance is used to define what is called reachability distance:
reachability-distancek(A,B)=max{k-distance(B), d(A,B)} In words, the
reachability distance of an object A from B is the true distance of the
two objects, but at least the k-distance of B. Objects that belong to
the k nearest neighbors of B (the \"core\" of B, see DBSCAN cluster
analysis) are considered to be equally distant. The reason for this is
to reduce the statistical fluctuations between all points A close to B,
where increasing the value for k increases the smoothing effect. Note
that this is not a distance in the mathematical definition, since it is
not symmetric. (While it is a common mistake to always use the
k-distance(A), this yields a slightly different method, referred to as
Simplified-LOF) The local reachability density of an object A is defined
by lrdk(A):=1/(ΣB ∈ Nk(A)reachability-distancek(A, B)/\|Nk(A)\|) which
is the inverse of the average reachability distance of the object A from
its neighbors. Note that it is not the average reachability of the
neighbors from A (which by definition would be the k-distance(A)), but
the distance at which A can be \"reached\" from its neighbors. With
duplicate points, this value can become infinite. The local reachability
densities are then compared with those of the neighbors using
LOFk(A):=ΣB ∈ Nk(A)lrdk(B)/lrdk(A)/\|Nk(A)\| = ΣB ∈
Nk(A)lrdk(B)/\|Nk(A)\| · lrdk(A) which is the average local reachability
density of the neighbors divided by the object\'s own local reachability
density. A value of approximately 1 indicates that the object is
comparable to its neighbors (and thus not an outlier). A value below 1
indicates a denser region (which would be an inlier), while values
significantly larger than 1 indicate outliers. LOF(k) \~ 1 means Similar
density as neighbors, LOF(k) \< 1 means Higher density than neighbors
(Inlier), LOF(k) \> 1 means Lower density than neighbors (Outlier)
Advantages Due to the local approach, LOF is able to identify outliers
in a data set that would not be outliers in another area of the data
set. For example, a point at a \"small\" distance to a very dense
cluster is an outlier, while a point within a sparse cluster might
exhibit similar distances to its neighbors. While the geometric
intuition of LOF is only applicable to low-dimensional vector spaces,
the algorithm can be applied in any context a dissimilarity function can
be defined. It has experimentally been shown to work very well in
numerous setups, often outperforming the competitors, for example in
network intrusion detection and on processed classification benchmark
data.The LOF family of methods can be easily generalized and then
applied to various other problems, such as detecting outliers in
geographic data, video streams or authorship networks. Disadvantages and
Extensions The resulting values are quotient-values and hard to
interpret. A value of 1 or even less indicates a clear inlier, but there
is no clear rule for when a point is an outlier. In one data set, a
value of 1.1 may already be an outlier, in another dataset and
parameterization (with strong local fluctuations) a value of 2 could
still be an inlier. These differences can also occur within a dataset
due to the locality of the method. There exist extensions of LOF that
try to improve over LOF in these aspects: Feature Bagging for Outlier
Detection runs LOF on multiple projections and combines the results for
improved detection qualities in high dimensions. This is the first
ensemble learning approach to outlier detection, for other variants see
ref. Local Outlier Probability (LoOP) is a method derived from LOF but
using inexpensive local statistics to become less sensitive to the
choice of the parameter k. In addition, the resulting values are scaled
to a value range of \[0:1\]. Interpreting and Unifying Outlier Scores
proposes a normalization of the LOF outlier scores to the interval
\[0:1\] using statistical scaling to increase usability and can be seen
an improved version of the LoOP ideas. On Evaluation of Outlier Rankings
and Outlier Scores proposes methods for measuring similarity and
diversity of methods for building advanced outlier detection ensembles
using LOF variants and other algorithms and improving on the Feature
Bagging approach discussed above. Local outlier detection reconsidered:
a generalized view on locality with applications to spatial, video, and
network outlier detection discusses the general pattern in various local
outlier detection methods (including, e.g., LOF, a simplified version of
LOF and LoOP) and abstracts from this into a general framework. This
framework is then applied, e.g., to detecting outliers in geographic
data, video streams and authorship networks. == References ==
