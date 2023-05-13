Ordering points to identify the clustering structure (OPTICS) is an
algorithm for finding density-based clusters in spatial data. It was
presented by Mihael Ankerst, Markus M. Breunig, Hans-Peter Kriegel and
Jörg Sander. Its basic idea is similar to DBSCAN, but it addresses one
of DBSCAN\'s major weaknesses: the problem of detecting meaningful
clusters in data of varying density. To do so, the points of the
database are (linearly) ordered such that spatially closest points
become neighbors in the ordering. Additionally, a special distance is
stored for each point that represents the density that must be accepted
for a cluster so that both points belong to the same cluster. This is
represented as a dendrogram. Basic idea Like DBSCAN, OPTICS requires two
parameters: ε, which describes the maximum distance (radius) to
consider, and MinPts, describing the number of points required to form a
cluster. A point p is a core point if at least MinPts points are found
within its ε-neighborhood N ε ( p ) {\\displaystyle N\_{\\varepsilon
}(p)} (including point p itself). In contrast to DBSCAN, OPTICS also
considers points that are part of a more densely packed cluster, so each
point is assigned a core distance that describes the distance to the
MinPtsth closest point: core-dist ε , M i n P t s ( p ) = { UNDEFINED if
\| N ε ( p ) \| \< M i n P t s M i n P t s -th smallest distance in N ε
( p ) otherwise {\\displaystyle {\\text{core-dist}}\_{\\mathit
{\\varepsilon ,MinPts}}(p)={\\begin{cases}{\\text{UNDEFINED}}&{\\text{if
}}\|N\_{\\varepsilon }(p)\|\<{\\mathit {MinPts}}\\\\{\\mathit
{MinPts}}{\\text{-th smallest distance in }}N\_{\\varepsilon
}(p)&{\\text{otherwise}}\\end{cases}}} The reachability-distance of
another point o from a point p is either the distance between o and p,
or the core distance of p, whichever is bigger: reachability-dist ε , M
i n P t s ( o , p ) = { UNDEFINED if \| N ε ( p ) \| \< M i n P t s max
( core-dist ε , M i n P t s ( p ) , dist ( p , o ) ) otherwise
{\\displaystyle {\\text{reachability-dist}}\_{\\mathit {\\varepsilon
,MinPts}}(o,p)={\\begin{cases}{\\text{UNDEFINED}}&{\\text{if
}}\|N\_{\\varepsilon }(p)\|\<{\\mathit
{MinPts}}\\\\\\max({\\text{core-dist}}\_{\\mathit {\\varepsilon
,MinPts}}(p),{\\text{dist}}(p,o))&{\\text{otherwise}}\\end{cases}}} If p
and o are nearest neighbors, this is the ε ′ \< ε {\\displaystyle
\\varepsilon \'\<\\varepsilon } we need to assume to have p and o belong
to the same cluster. Both core-distance and reachability-distance are
undefined if no sufficiently dense cluster (w.r.t. ε) is available.
Given a sufficiently large ε, this never happens, but then every
ε-neighborhood query returns the entire database, resulting in O ( n 2 )
{\\displaystyle O(n\^{2})} runtime. Hence, the ε parameter is required
to cut off the density of clusters that are no longer interesting, and
to speed up the algorithm. The parameter ε is, strictly speaking, not
necessary. It can simply be set to the maximum possible value. When a
spatial index is available, however, it does play a practical role with
regards to complexity. OPTICS abstracts from DBSCAN by removing this
parameter, at least to the extent of only having to give the maximum
value. Pseudocode The basic approach of OPTICS is similar to DBSCAN, but
instead of maintaining known, but so far unprocessed cluster members in
a set, they are maintained in a priority queue (e.g. using an indexed
heap). function OPTICS(DB, ε, MinPts) is for each point p of DB do
p.reachability-distance = UNDEFINED for each unprocessed point p of DB
do N = getNeighbors(p, ε) mark p as processed output p to the ordered
list if core-distance(p, ε, MinPts) != UNDEFINED then Seeds = empty
priority queue update(N, p, Seeds, ε, MinPts) for each next q in Seeds
do N\' = getNeighbors(q, ε) mark q as processed output q to the ordered
list if core-distance(q, ε, MinPts) != UNDEFINED do update(N\', q,
Seeds, ε, MinPts) In update(), the priority queue Seeds is updated with
the ε {\\displaystyle \\varepsilon } -neighborhood of p {\\displaystyle
p} and q {\\displaystyle q} , respectively: function update(N, p, Seeds,
ε, MinPts) is coredist = core-distance(p, ε, MinPts) for each o in N if
o is not processed then new-reach-dist = max(coredist, dist(p,o)) if
o.reachability-distance == UNDEFINED then // o is not in Seeds
o.reachability-distance = new-reach-dist Seeds.insert(o, new-reach-dist)
else // o in Seeds, check for improvement if new-reach-dist \<
o.reachability-distance then o.reachability-distance = new-reach-dist
Seeds.move-up(o, new-reach-dist) OPTICS hence outputs the points in a
particular ordering, annotated with their smallest reachability distance
(in the original algorithm, the core distance is also exported, but this
is not required for further processing). Extracting the clusters Using a
reachability-plot (a special kind of dendrogram), the hierarchical
structure of the clusters can be obtained easily. It is a 2D plot, with
the ordering of the points as processed by OPTICS on the x-axis and the
reachability distance on the y-axis. Since points belonging to a cluster
have a low reachability distance to their nearest neighbor, the clusters
show up as valleys in the reachability plot. The deeper the valley, the
denser the cluster. The image above illustrates this concept. In its
upper left area, a synthetic example data set is shown. The upper right
part visualizes the spanning tree produced by OPTICS, and the lower part
shows the reachability plot as computed by OPTICS. Colors in this plot
are labels, and not computed by the algorithm; but it is well visible
how the valleys in the plot correspond to the clusters in above data
set. The yellow points in this image are considered noise, and no valley
is found in their reachability plot. They are usually not assigned to
clusters, except the omnipresent \"all data\" cluster in a hierarchical
result. Extracting clusters from this plot can be done manually by
selecting a range on the x-axis after visual inspection, by selecting a
threshold on the y-axis (the result is then similar to a DBSCAN
clustering result with the same ε {\\displaystyle \\varepsilon } and
minPts parameters; here a value of 0.1 may yield good results), or by
different algorithms that try to detect the valleys by steepness, knee
detection, or local maxima. Clusterings obtained this way usually are
hierarchical, and cannot be achieved by a single DBSCAN run. Complexity
Like DBSCAN, OPTICS processes each point once, and performs one ε
{\\displaystyle \\varepsilon } -neighborhood query during this
processing. Given a spatial index that grants a neighborhood query in O
( log ⁡ n ) {\\displaystyle O(\\log n)} runtime, an overall runtime of O
( n ⋅ log ⁡ n ) {\\displaystyle O(n\\cdot \\log n)} is obtained. The
authors of the original OPTICS paper report an actual constant slowdown
factor of 1.6 compared to DBSCAN. Note that the value of ε
{\\displaystyle \\varepsilon } might heavily influence the cost of the
algorithm, since a value too large might raise the cost of a
neighborhood query to linear complexity. In particular, choosing ε \>
max x , y d ( x , y ) {\\displaystyle \\varepsilon \>\\max
\_{x,y}d(x,y)} (larger than the maximum distance in the data set) is
possible, but leads to quadratic complexity, since every neighborhood
query returns the full data set. Even when no spatial index is
available, this comes at additional cost in managing the heap.
Therefore, ε {\\displaystyle \\varepsilon } should be chosen
appropriately for the data set. Extensions OPTICS-OF is an outlier
detection algorithm based on OPTICS. The main use is the extraction of
outliers from an existing run of OPTICS at low cost compared to using a
different outlier detection method. The better known version LOF is
based on the same concepts. DeLi-Clu, Density-Link-Clustering combines
ideas from single-linkage clustering and OPTICS, eliminating the ε
{\\displaystyle \\varepsilon } parameter and offering performance
improvements over OPTICS. HiSC is a hierarchical subspace clustering
(axis-parallel) method based on OPTICS. HiCO is a hierarchical
correlation clustering algorithm based on OPTICS. DiSH is an improvement
over HiSC that can find more complex hierarchies. FOPTICS is a faster
implementation using random projections. HDBSCAN\* is based on a
refinement of DBSCAN, excluding border-points from the clusters and thus
following more strictly the basic definition of density-levels by
Hartigan. Availability Java implementations of OPTICS, OPTICS-OF,
DeLi-Clu, HiSC, HiCO and DiSH are available in the ELKI data mining
framework (with index acceleration for several distance functions, and
with automatic cluster extraction using the ξ extraction method). Other
Java implementations include the Weka extension (no support for ξ
cluster extraction). The R package \"dbscan\" includes a C++
implementation of OPTICS (with both traditional dbscan-like and ξ
cluster extraction) using a k-d tree for index acceleration for
Euclidean distance only. Python implementations of OPTICS are available
in the PyClustering library and in scikit-learn. HDBSCAN\* is available
in the hdbscan library. == References ==
