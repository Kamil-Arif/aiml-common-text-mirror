In data mining and statistics, hierarchical clustering (also called
hierarchical cluster analysis or HCA) is a method of cluster analysis
that seeks to build a hierarchy of clusters. Strategies for hierarchical
clustering generally fall into two categories: Agglomerative: This is a
\"bottom-up\" approach: Each observation starts in its own cluster, and
pairs of clusters are merged as one moves up the hierarchy. Divisive:
This is a \"top-down\" approach: All observations start in one cluster,
and splits are performed recursively as one moves down the hierarchy.In
general, the merges and splits are determined in a greedy manner. The
results of hierarchical clustering are usually presented in a
dendrogram. The standard algorithm for hierarchical agglomerative
clustering (HAC) has a time complexity of O ( n 3 ) {\\displaystyle
{\\mathcal {O}}(n\^{3})} and requires Ω ( n 2 ) {\\displaystyle \\Omega
(n\^{2})} memory, which makes it too slow for even medium data sets.
However, for some special cases, optimal efficient agglomerative methods
(of complexity O ( n 2 ) {\\displaystyle {\\mathcal {O}}(n\^{2})} ) are
known: SLINK for single-linkage and CLINK for complete-linkage
clustering. With a heap, the runtime of the general case can be reduced
to O ( n 2 log ⁡ n ) {\\displaystyle {\\mathcal {O}}(n\^{2}\\log n)} , an
improvement on the aforementioned bound of O ( n 3 ) {\\displaystyle
{\\mathcal {O}}(n\^{3})} , at the cost of further increasing the memory
requirements. In many cases, the memory overheads of this approach are
too large to make it practically usable. Except for the special case of
single-linkage, none of the algorithms (except exhaustive search in O (
2 n ) {\\displaystyle {\\mathcal {O}}(2\^{n})} ) can be guaranteed to
find the optimum solution. Divisive clustering with an exhaustive search
is O ( 2 n ) {\\displaystyle {\\mathcal {O}}(2\^{n})} , but it is common
to use faster heuristics to choose splits, such as k-means. Hierarchical
clustering has the distinct advantage that any valid measure of distance
can be used. In fact, the observations themselves are not required: all
that is used is a matrix of distances. Cluster Linkage In order to
decide which clusters should be combined (for agglomerative), or where a
cluster should be split (for divisive), a measure of dissimilarity
between sets of observations is required. In most methods of
hierarchical clustering, this is achieved by use of an appropriate
distance d, such as the Euclidean distance, between single observations
of the data set, and a linkage criterion, which specifies the
dissimilarity of sets as a function of the pairwise distances of
observations in the sets. The choice of metric as well as linkage can
have a major impact on the result of the clustering, where the lower
level metric determines which objects are most similar, whereas the
linkage criterion influences the shape of the clusters. For example,
complete-linkage tends to produce more spherical clusters than
single-linkage. The linkage criterion determines the distance between
sets of observations as a function of the pairwise distances between
observations. Some commonly used linkage criteria between two sets of
observations A and B and a distance d are: Some of these can only be
recomputed recursively (WPGMA, WPGMC), for many a recursive computation
with Lance-Williams-equations is more efficient, while for other
(Mini-Max, Hausdorff, Medoid) the distances have to be computed with the
slower full formula. Other linkage criteria include: The probability
that candidate clusters spawn from the same distribution function
(V-linkage). The product of in-degree and out-degree on a
k-nearest-neighbour graph (graph degree linkage). The increment of some
cluster descriptor (i.e., a quantity defined for measuring the quality
of a cluster) after merging two clusters. Agglomerative clustering
example For example, suppose this data is to be clustered, and the
Euclidean distance is the distance metric. The hierarchical clustering
dendrogram would be: Cutting the tree at a given height will give a
partitioning clustering at a selected precision. In this example,
cutting after the second row (from the top) of the dendrogram will yield
clusters {a} {b c} {d e} {f}. Cutting after the third row will yield
clusters {a} {b c} {d e f}, which is a coarser clustering, with a
smaller number but larger clusters. This method builds the hierarchy
from the individual elements by progressively merging clusters. In our
example, we have six elements {a} {b} {c} {d} {e} and {f}. The first
step is to determine which elements to merge in a cluster. Usually, we
want to take the two closest elements, according to the chosen distance.
Optionally, one can also construct a distance matrix at this stage,
where the number in the i-th row j-th column is the distance between the
i-th and j-th elements. Then, as clustering progresses, rows and columns
are merged as the clusters are merged and the distances updated. This is
a common way to implement this type of clustering, and has the benefit
of caching distances between clusters. A simple agglomerative clustering
algorithm is described in the single-linkage clustering page; it can
easily be adapted to different types of linkage (see below). Suppose we
have merged the two closest elements b and c, we now have the following
clusters {a}, {b, c}, {d}, {e} and {f}, and want to merge them further.
To do that, we need to take the distance between {a} and {b c}, and
therefore define the distance between two clusters. Usually the distance
between two clusters A {\\displaystyle {\\mathcal {A}}} and B
{\\displaystyle {\\mathcal {B}}} is one of the following: The maximum
distance between elements of each cluster (also called complete-linkage
clustering): max { d ( x , y ) : x ∈ A , y ∈ B } . {\\displaystyle
\\max\\{\\,d(x,y):x\\in {\\mathcal {A}},\\,y\\in {\\mathcal {B}}\\,\\}.}
The minimum distance between elements of each cluster (also called
single-linkage clustering): min { d ( x , y ) : x ∈ A , y ∈ B } .
{\\displaystyle \\min\\{\\,d(x,y):x\\in {\\mathcal {A}},\\,y\\in
{\\mathcal {B}}\\,\\}.} The mean distance between elements of each
cluster (also called average linkage clustering, used e.g. in UPGMA): 1
\| A \| ⋅ \| B \| ∑ x ∈ A ∑ y ∈ B d ( x , y ) . {\\displaystyle {1
\\over {\|{\\mathcal {A}}\|\\cdot \|{\\mathcal {B}}\|}}\\sum \_{x\\in
{\\mathcal {A}}}\\sum \_{y\\in {\\mathcal {B}}}d(x,y).} The sum of all
intra-cluster variance. The increase in variance for the cluster being
merged (Ward\'s method) The probability that candidate clusters spawn
from the same distribution function (V-linkage).In case of tied minimum
distances, a pair is randomly chosen, thus being able to generate
several structurally different dendrograms. Alternatively, all tied
pairs may be joined at the same time, generating a unique dendrogram.One
can always decide to stop clustering when there is a sufficiently small
number of clusters (number criterion). Some linkages may also guarantee
that agglomeration occurs at a greater distance between clusters than
the previous agglomeration, and then one can stop clustering when the
clusters are too far apart to be merged (distance criterion). However,
this is not the case of, e.g., the centroid linkage where the so-called
reversals (inversions, departures from ultrametricity) may occur.
Divisive clustering The basic principle of divisive clustering was
published as the DIANA (DIvisive ANAlysis Clustering) algorithm.
Initially, all data is in the same cluster, and the largest cluster is
split until every object is separate. Because there exist O ( 2 n )
{\\displaystyle O(2\^{n})} ways of splitting each cluster, heuristics
are needed. DIANA chooses the object with the maximum average
dissimilarity and then moves all objects to this cluster that are more
similar to the new cluster than to the remainder. Software Open source
implementations ALGLIB implements several hierarchical clustering
algorithms (single-link, complete-link, Ward) in C++ and C# with O(n²)
memory and O(n³) run time. ELKI includes multiple hierarchical
clustering algorithms, various linkage strategies and also includes the
efficient SLINK, CLINK and Anderberg algorithms, flexible cluster
extraction from dendrograms and various other cluster analysis
algorithms. Julia has an implementation inside the Clustering.jl
package. Octave, the GNU analog to MATLAB implements hierarchical
clustering in function \"linkage\". Orange, a data mining software
suite, includes hierarchical clustering with interactive dendrogram
visualisation. R has built-in functions and packages that provide
functions for hierarchical clustering. SciPy implements hierarchical
clustering in Python, including the efficient SLINK algorithm.
scikit-learn also implements hierarchical clustering in Python. Weka
includes hierarchical cluster analysis. Commercial implementations
MATLAB includes hierarchical cluster analysis. SAS includes hierarchical
cluster analysis in PROC CLUSTER. Mathematica includes a Hierarchical
Clustering Package. NCSS includes hierarchical cluster analysis. SPSS
includes hierarchical cluster analysis. Qlucore Omics Explorer includes
hierarchical cluster analysis. Stata includes hierarchical cluster
analysis. CrimeStat includes a nearest neighbor hierarchical cluster
algorithm with a graphical output for a Geographic Information System.
See also References Further reading Kaufman, L.; Rousseeuw, P.J. (1990).
Finding Groups in Data: An Introduction to Cluster Analysis (1 ed.). New
York: John Wiley. ISBN 0-471-87876-6. Hastie, Trevor; Tibshirani,
Robert; Friedman, Jerome (2009). \"14.3.12 Hierarchical clustering\".
The Elements of Statistical Learning (2nd ed.). New York: Springer. pp.
520--8. ISBN 978-0-387-84857-0. Archived from the original (PDF) on
2009-11-10. Retrieved 2009-10-20.
