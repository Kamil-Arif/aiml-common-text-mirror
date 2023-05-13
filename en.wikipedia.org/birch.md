BIRCH (balanced iterative reducing and clustering using hierarchies) is
an unsupervised data mining algorithm used to perform hierarchical
clustering over particularly large data-sets. With modifications it can
also be used to accelerate k-means clustering and Gaussian mixture
modeling with the expectation--maximization algorithm. An advantage of
BIRCH is its ability to incrementally and dynamically cluster incoming,
multi-dimensional metric data points in an attempt to produce the best
quality clustering for a given set of resources (memory and time
constraints). In most cases, BIRCH only requires a single scan of the
database. Its inventors claim BIRCH to be the \"first clustering
algorithm proposed in the database area to handle \'noise\' (data points
that are not part of the underlying pattern) effectively\", beating
DBSCAN by two months. The BIRCH algorithm received the SIGMOD 10 year
test of time award in 2006. Problem with previous methods Previous
clustering algorithms performed less effectively over very large
databases and did not adequately consider the case wherein a data-set
was too large to fit in main memory. As a result, there was a lot of
overhead maintaining high clustering quality while minimizing the cost
of additional IO (input/output) operations. Furthermore, most of
BIRCH\'s predecessors inspect all data points (or all currently existing
clusters) equally for each \'clustering decision\' and do not perform
heuristic weighting based on the distance between these data points.
Advantages with BIRCH It is local in that each clustering decision is
made without scanning all data points and currently existing clusters.
It exploits the observation that the data space is not usually uniformly
occupied and not every data point is equally important. It makes full
use of available memory to derive the finest possible sub-clusters while
minimizing I/O costs. It is also an incremental method that does not
require the whole data set in advance. Algorithm The BIRCH algorithm
takes as input a set of N data points, represented as real-valued
vectors, and a desired number of clusters K. It operates in four phases,
the second of which is optional. The first phase builds a clustering
feature ( C F {\\displaystyle CF} ) tree out of the data points, a
height-balanced tree data structure, defined as follows: Given a set of
N d-dimensional data points, the clustering feature C F {\\displaystyle
CF} of the set is defined as the triple C F = ( N , L S → , S S )
{\\displaystyle CF=(N,{\\overrightarrow {LS}},SS)} , where L S → = ∑ i =
1 N X i → {\\displaystyle {\\overrightarrow {LS}}=\\sum
\_{i=1}\^{N}{\\overrightarrow {X\_{i}}}} is the linear sum. S S = ∑ i =
1 N ( X i → ) 2 {\\displaystyle SS=\\sum \_{i=1}\^{N}({\\overrightarrow
{X\_{i}}})\^{2}} is the square sum of data points. Clustering features
are organized in a CF tree, a height-balanced tree with two parameters:
branching factor B {\\displaystyle B} and threshold T {\\displaystyle T}
. Each non-leaf node contains at most B {\\displaystyle B} entries of
the form \[ C F i , c h i l d i \] {\\displaystyle
\[CF\_{i},child\_{i}\]} , where c h i l d i {\\displaystyle child\_{i}}
is a pointer to its i {\\displaystyle i} th child node and C F i
{\\displaystyle CF\_{i}} the clustering feature representing the
associated subcluster. A leaf node contains at most L {\\displaystyle L}
entries each of the form \[ C F i \] {\\displaystyle \[CF\_{i}\]} . It
also has two pointers prev and next which are used to chain all leaf
nodes together. The tree size depends on the parameter T {\\displaystyle
T} . A node is required to fit in a page of size P {\\displaystyle P} .
B {\\displaystyle B} and L {\\displaystyle L} are determined by P
{\\displaystyle P} . So P {\\displaystyle P} can be varied for
performance tuning. It is a very compact representation of the dataset
because each entry in a leaf node is not a single data point but a
subcluster.In the second step, the algorithm scans all the leaf entries
in the initial C F {\\displaystyle CF} tree to rebuild a smaller C F
{\\displaystyle CF} tree, while removing outliers and grouping crowded
subclusters into larger ones. This step is marked optional in the
original presentation of BIRCH. In step three an existing clustering
algorithm is used to cluster all leaf entries. Here an agglomerative
hierarchical clustering algorithm is applied directly to the subclusters
represented by their C F {\\displaystyle CF} vectors. It also provides
the flexibility of allowing the user to specify either the desired
number of clusters or the desired diameter threshold for clusters. After
this step a set of clusters is obtained that captures major distribution
pattern in the data. However, there might exist minor and localized
inaccuracies which can be handled by an optional step 4. In step 4 the
centroids of the clusters produced in step 3 are used as seeds and
redistribute the data points to its closest seeds to obtain a new set of
clusters. Step 4 also provides us with an option of discarding outliers.
That is a point which is too far from its closest seed can be treated as
an outlier. Calculations with the clustering features Given only the
clustering feature C F = \[ N , L S → , S S \] {\\displaystyle
CF=\[N,{\\overrightarrow {LS}},SS\]} , the same measures can be
calculated without the knowledge of the underlying actual values.
Centroid: C → = ∑ i = 1 N X i → N = L S → N {\\displaystyle
{\\overrightarrow {C}}={\\frac {\\sum \_{i=1}\^{N}{\\overrightarrow
{X\_{i}}}}{N}}={\\frac {\\overrightarrow {LS}}{N}}} Radius: R = ∑ i = 1
N ( X i → − C → ) 2 N = N ⋅ C → 2 + S S − 2 ⋅ C → ⋅ L S → N = S S N − (
L S → N ) 2 {\\displaystyle R={\\sqrt {\\frac {\\sum
\_{i=1}\^{N}({\\overrightarrow {X\_{i}}}-{\\overrightarrow
{C}})\^{2}}{N}}}={\\sqrt {\\frac {N\\cdot {\\overrightarrow
{C}}\^{2}+SS-2\\cdot {\\overrightarrow {C}}\\cdot {\\overrightarrow
{LS}}}{N}}}={\\sqrt {{\\frac {SS}{N}}-({\\frac {\\overrightarrow
{LS}}{N}})\^{2}}}} Average Linkage Distance between clusters C F 1 = \[
N 1 , L S 1 → , S S 1 \] {\\displaystyle
CF\_{1}=\[N\_{1},{\\overrightarrow {LS\_{1}}},SS\_{1}\]} and C F 2 = \[
N 2 , L S 2 → , S S 2 \] {\\displaystyle
CF\_{2}=\[N\_{2},{\\overrightarrow {LS\_{2}}},SS\_{2}\]} : D 2 = ∑ i = 1
N 1 ∑ j = 1 N 2 ( X i → − Y j → ) 2 N 1 ⋅ N 2 = N 1 ⋅ S S 2 + N 2 ⋅ S S
1 − 2 ⋅ L S 1 → ⋅ L S 2 → N 1 ⋅ N 2 {\\displaystyle D\_{2}={\\sqrt
{\\frac {\\sum \_{i=1}\^{N\_{1}}\\sum
\_{j=1}\^{N\_{2}}({\\overrightarrow {X\_{i}}}-{\\overrightarrow
{Y\_{j}}})\^{2}}{N\_{1}\\cdot N\_{2}}}}={\\sqrt {\\frac {N\_{1}\\cdot
SS\_{2}+N\_{2}\\cdot SS\_{1}-2\\cdot {\\overrightarrow {LS\_{1}}}\\cdot
{\\overrightarrow {LS\_{2}}}}{N\_{1}\\cdot N\_{2}}}}} In
multidimensional cases the square root should be replaced with a
suitable norm. Numerical issues in BIRCH clustering features
Unfortunately, there are numerical issues associated with the use of the
term S S {\\displaystyle SS} in BIRCH. When subtracting S S N − ( L S →
N ) 2 {\\displaystyle {\\frac {SS}{N}}-{\\big (}{\\frac {\\vec
{LS}}{N}}{\\big )}\^{2}} or similar in the other distances such as D 2
{\\displaystyle D\_{2}} , catastrophic cancellation can occur and yield
a poor precision, and which can in some cases even cause the result to
be negative (and the square root then become undefined). This can be
resolved by using BETULA cluster features C F = ( N , μ , S )
{\\displaystyle CF=(N,\\mu ,S)} instead, which store the count N
{\\displaystyle N} , mean μ {\\displaystyle \\mu } , and sum of squared
deviations instead based on numerically more reliable online algorithms
to calculate variance. For these features, a similar additivity theorem
holds. When storing a vector respectively a matrix for the squared
deviations, the resulting BIRCH CF-tree can also be used to accelerate
Gaussian Mixture Modeling with the expectation--maximization algorithm,
besides k-means clustering and hierarchical agglomerative clustering. ==
Notes ==
