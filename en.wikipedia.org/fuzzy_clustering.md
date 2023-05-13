Fuzzy clustering (also referred to as soft clustering or soft k-means)
is a form of clustering in which each data point can belong to more than
one cluster. Clustering or cluster analysis involves assigning data
points to clusters such that items in the same cluster are as similar as
possible, while items belonging to different clusters are as dissimilar
as possible. Clusters are identified via similarity measures. These
similarity measures include distance, connectivity, and intensity.
Different similarity measures may be chosen based on the data or the
application. Comparison to hard clustering In non-fuzzy clustering (also
known as hard clustering), data are divided into distinct clusters,
where each data point can only belong to exactly one cluster. In fuzzy
clustering, data points can potentially belong to multiple clusters. For
example, an apple can be red or green (hard clustering), but an apple
can also be red AND green (fuzzy clustering). Here, the apple can be red
to a certain degree as well as green to a certain degree. Instead of the
apple belonging to green \[green = 1\] and not red \[red = 0\], the
apple can belong to green \[green = 0.5\] and red \[red = 0.5\]. These
value are normalized between 0 and 1; however, they do not represent
probabilities, so the two values do not need to add up to 1. Membership
Membership grades are assigned to each of the data points (tags). These
membership grades indicate the degree to which data points belong to
each cluster. Thus, points on the edge of a cluster, with lower
membership grades, may be in the cluster to a lesser degree than points
in the center of cluster. Fuzzy C-means clustering One of the most
widely used fuzzy clustering algorithms is the Fuzzy C-means clustering
(FCM) algorithm. History Fuzzy c-means (FCM) clustering was developed by
J.C. Dunn in 1973, and improved by J.C. Bezdek in 1981. General
description The fuzzy c-means algorithm is very similar to the k-means
algorithm: Choose a number of clusters. Assign coefficients randomly to
each data point for being in the clusters. Repeat until the algorithm
has converged (that is, the coefficients\' change between two iterations
is no more than ε {\\displaystyle \\varepsilon } , the given sensitivity
threshold) : Compute the centroid for each cluster (shown below). For
each data point, compute its coefficients of being in the clusters.
Centroid Any point x has a set of coefficients giving the degree of
being in the kth cluster wk(x). With fuzzy c-means, the centroid of a
cluster is the mean of all points, weighted by their degree of belonging
to the cluster, or, mathematically, c k = ∑ x w k ( x ) m x ∑ x w k ( x
) m , {\\displaystyle c\_{k}={{\\sum \_{x}{w\_{k}(x)}\^{m}x} \\over
{\\sum \_{x}{w\_{k}(x)}\^{m}}},} where m is the hyper- parameter that
controls how fuzzy the cluster will be. The higher it is, the fuzzier
the cluster will be in the end. Algorithm The FCM algorithm attempts to
partition a finite collection of n {\\displaystyle n} elements X = { x 1
, . . . , x n } {\\displaystyle X=\\{\\mathbf {x} \_{1},\...,\\mathbf
{x} \_{n}\\}} into a collection of c fuzzy clusters with respect to some
given criterion. Given a finite set of data, the algorithm returns a
list of c {\\displaystyle c} cluster centres C = { c 1 , . . . , c c }
{\\displaystyle C=\\{\\mathbf {c} \_{1},\...,\\mathbf {c} \_{c}\\}} and
a partition matrix W = w i , j ∈ \[ 0 , 1 \] , i = 1 , . . . , n , j = 1
, . . . , c {\\displaystyle W=w\_{i,j}\\in
\[0,1\],\\;i=1,\...,n,\\;j=1,\...,c} , where each element, w i j
{\\displaystyle w\_{ij}} , tells the degree to which element, x i
{\\displaystyle \\mathbf {x} \_{i}} , belongs to cluster c j
{\\displaystyle \\mathbf {c} \_{j}} . The FCM aims to minimize an
objective function: J ( W , C ) = ∑ i = 1 n ∑ j = 1 c w i j m ‖ x i − c
j ‖ 2 {\\displaystyle J(W,C)=\\sum \_{i=1}\^{n}\\sum
\_{j=1}\^{c}w\_{ij}\^{m}\\left\\\|\\mathbf {x} \_{i}-\\mathbf {c}
\_{j}\\right\\\|\^{2}} ,where: w i j = 1 ∑ k = 1 c ( ‖ x i − c j ‖ ‖ x i
− c k ‖ ) 2 m − 1 {\\displaystyle w\_{ij}={\\frac {1}{\\sum
\_{k=1}\^{c}\\left({\\frac {\\left\\\|\\mathbf {x} \_{i}-\\mathbf {c}
\_{j}\\right\\\|}{\\left\\\|\\mathbf {x} \_{i}-\\mathbf {c}
\_{k}\\right\\\|}}\\right)\^{\\frac {2}{m-1}}}}} . Comparison to K-means
clustering K-means clustering also attempts to minimize the objective
function shown above, except that in K-means, the membership values are
either zero or one, and cannot take values in between, i.e. w i j ∈ { 0
, 1 } {\\displaystyle w\_{ij}\\in \\{0,1\\}} . In Fuzzy C-means, the
degree of fuzziness is parametrized by m ∈ ( 1 , ∞ ) {\\displaystyle
m\\in (1,\\infty )} , where a larger m {\\displaystyle m} results in
fuzzier clusters. In the limit m → 1 {\\displaystyle m\\rightarrow 1} ,
the memberships, w i j {\\displaystyle w\_{ij}} , converge to 0 or 1,
and the Fuzzy C-means objective coincides with that of K-means. In the
absence of experimentation or domain knowledge, m {\\displaystyle m} is
commonly set to 2. The algorithm minimizes intra-cluster variance as
well, but has the same problems as \'k\'-means; the minimum is a local
minimum, and the results depend on the initial choice of weights.
Implementation There are several implementations of this algorithm that
are publicly available. Related algorithms Fuzzy C-means (FCM) with
automatically determined for the number of clusters could enhance the
detection accuracy. Using a mixture of Gaussians along with the
expectation-maximization algorithm is a more statistically formalized
method which includes some of these ideas: partial membership in
classes. Example To better understand this principle, a classic example
of mono-dimensional data is given below on an x axis. This data set can
be traditionally grouped into two clusters. By selecting a threshold on
the x-axis, the data is separated into two clusters. The resulting
clusters are labelled \'A\' and \'B\', as seen in the following image.
Each point belonging to the data set would therefore have a membership
coefficient of 1 or 0. This membership coefficient of each corresponding
data point is represented by the inclusion of the y-axis. In fuzzy
clustering, each data point can have membership to multiple clusters. By
relaxing the definition of membership coefficients from strictly 1 or 0,
these values can range from any value from 1 to 0. The following image
shows the data set from the previous clustering, but now fuzzy c-means
clustering is applied. First, a new threshold value defining two
clusters may be generated. Next, new membership coefficients for each
data point are generated based on clusters centroids, as well as
distance from each cluster centroid. As one can see, the middle data
point belongs to cluster A and cluster B. the value of 0.3 is this data
point\'s membership coefficient for cluster A . Applications Clustering
problems have applications in surface science, biology, medicine,
psychology, economics, and many other disciplines. Bioinformatics In the
field of bioinformatics, clustering is used for a number of
applications. One use is as a pattern recognition technique to analyze
gene expression data from RNA-sequencing data or other technologies. In
this case, genes with similar expression patterns are grouped into the
same cluster, and different clusters display distinct, well-separated
patterns of expression. Use of clustering can provide insight into gene
function and regulation. Because fuzzy clustering allows genes to belong
to more than one cluster, it allows for the identification of genes that
are conditionally co-regulated or co-expressed. For example, one gene
may be acted on by more than one transcription factor, and one gene may
encode a protein that has more than one function. Thus, fuzzy clustering
is more appropriate than hard clustering. Image analysis Fuzzy c-means
has been a very important tool for image processing in clustering
objects in an image. In the 1970s, mathematicians introduced the spatial
term into the FCM algorithm to improve the accuracy of clustering under
noise. Furthermore, FCM algorithms have been used to distinguish between
different activities using image-based features such as the Hu and the
Zernike Moments. Alternatively, A fuzzy logic model can be described on
fuzzy sets that are defined on three components of the HSL color space
HSL and HSV; The membership functions aim to describe colors follow the
human intuition of color identification. Marketing In marketing,
customers can be grouped into fuzzy clusters based on their needs, brand
choices, psycho-graphic profiles, or other marketing related partitions.
Image processing example Image segmentation using k-means clustering
algorithms has long been used for pattern recognition, object detection,
and medical imaging. However, due to real world limitations such as
noise, shadowing, and variations in cameras, traditional hard clustering
is often unable to reliably perform image processing tasks as stated
above. Fuzzy clustering has been proposed as a more applicable algorithm
in the performance to these tasks. Given is gray scale image that has
undergone fuzzy clustering in Matlab. The original image is seen next to
a clustered image. Colors are used to give a visual representation of
the three distinct clusters used to identify the membership of each
pixel. Below, a chart is given that defines the fuzzy membership
coefficients of their corresponding intensity values. Depending on the
application for which the fuzzy clustering coefficients are to be used,
different pre-processing techniques can be applied to RGB images. RGB to
HCL conversion is common practice. See also FLAME Clustering Cluster
Analysis Expectation-maximization algorithm (a similar, but more
statistically formalized method) == References ==
