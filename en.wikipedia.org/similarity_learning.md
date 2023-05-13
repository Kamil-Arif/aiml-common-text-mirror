Similarity learning is an area of supervised machine learning in
artificial intelligence. It is closely related to regression and
classification, but the goal is to learn a similarity function that
measures how similar or related two objects are. It has applications in
ranking, in recommendation systems, visual identity tracking, face
verification, and speaker verification. Learning setup There are four
common setups for similarity and metric distance learning. Regression
similarity learning In this setup, pairs of objects are given ( x i 1 ,
x i 2 ) {\\displaystyle (x\_{i}\^{1},x\_{i}\^{2})} together with a
measure of their similarity y i ∈ R {\\displaystyle y\_{i}\\in R} . The
goal is to learn a function that approximates f ( x i 1 , x i 2 ) ∼ y i
{\\displaystyle f(x\_{i}\^{1},x\_{i}\^{2})\\sim y\_{i}} for every new
labeled triplet example ( x i 1 , x i 2 , y i ) {\\displaystyle
(x\_{i}\^{1},x\_{i}\^{2},y\_{i})} . This is typically achieved by
minimizing a regularized loss min W ∑ i l o s s ( w ; x i 1 , x i 2 , y
i ) + r e g ( w ) {\\displaystyle \\min \_{W}\\sum
\_{i}loss(w;x\_{i}\^{1},x\_{i}\^{2},y\_{i})+reg(w)} . Classification
similarity learning Given are pairs of similar objects ( x i , x i + )
{\\displaystyle (x\_{i},x\_{i}\^{+})} and non similar objects ( x i , x
i − ) {\\displaystyle (x\_{i},x\_{i}\^{-})} . An equivalent formulation
is that every pair ( x i 1 , x i 2 ) {\\displaystyle
(x\_{i}\^{1},x\_{i}\^{2})} is given together with a binary label y i ∈ {
0 , 1 } {\\displaystyle y\_{i}\\in \\{0,1\\}} that determines if the two
objects are similar or not. The goal is again to learn a classifier that
can decide if a new pair of objects is similar or not. Ranking
similarity learning Given are triplets of objects ( x i , x i + , x i −
) {\\displaystyle (x\_{i},x\_{i}\^{+},x\_{i}\^{-})} whose relative
similarity obey a predefined order: x i {\\displaystyle x\_{i}} is known
to be more similar to x i + {\\displaystyle x\_{i}\^{+}} than to x i −
{\\displaystyle x\_{i}\^{-}} . The goal is to learn a function f
{\\displaystyle f} such that for any new triplet of objects ( x , x + ,
x − ) {\\displaystyle (x,x\^{+},x\^{-})} , it obeys f ( x , x + ) \> f (
x , x − ) {\\displaystyle f(x,x\^{+})\>f(x,x\^{-})} (contrastive
learning). This setup assumes a weaker form of supervision than in
regression, because instead of providing an exact measure of similarity,
one only has to provide the relative order of similarity. For this
reason, ranking-based similarity learning is easier to apply in real
large-scale applications. Locality sensitive hashing (LSH) Hashes input
items so that similar items map to the same \"buckets\" in memory with
high probability (the number of buckets being much smaller than the
universe of possible input items). It is often applied in nearest
neighbor search on large-scale high-dimensional data, e.g., image
databases, document collections, time-series databases, and genome
databases.A common approach for learning similarity is to model the
similarity function as a bilinear form. For example, in the case of
ranking similarity learning, one aims to learn a matrix W that
parametrizes the similarity function f W ( x , z ) = x T W z
{\\displaystyle f\_{W}(x,z)=x\^{T}Wz} . When data is abundant, a common
approach is to learn a siamese network - A deep network model with
parameter sharing. Metric learning Similarity learning is closely
related to distance metric learning. Metric learning is the task of
learning a distance function over objects. A metric or distance function
has to obey four axioms: non-negativity, identity of indiscernibles,
symmetry and subadditivity (or the triangle inequality). In practice,
metric learning algorithms ignore the condition of identity of
indiscernibles and learn a pseudo-metric. When the objects x i
{\\displaystyle x\_{i}} are vectors in R d {\\displaystyle R\^{d}} ,
then any matrix W {\\displaystyle W} in the symmetric positive
semi-definite cone S + d {\\displaystyle S\_{+}\^{d}} defines a distance
pseudo-metric of the space of x through the form D W ( x 1 , x 2 ) 2 = (
x 1 − x 2 ) ⊤ W ( x 1 − x 2 ) {\\displaystyle
D\_{W}(x\_{1},x\_{2})\^{2}=(x\_{1}-x\_{2})\^{\\top }W(x\_{1}-x\_{2})} .
When W {\\displaystyle W} is a symmetric positive definite matrix, D W
{\\displaystyle D\_{W}} is a metric. Moreover, as any symmetric positive
semi-definite matrix W ∈ S + d {\\displaystyle W\\in S\_{+}\^{d}} can be
decomposed as W = L ⊤ L {\\displaystyle W=L\^{\\top }L} where L ∈ R e ×
d {\\displaystyle L\\in R\^{e\\times d}} and e ≥ r a n k ( W )
{\\displaystyle e\\geq rank(W)} , the distance function D W
{\\displaystyle D\_{W}} can be rewritten equivalently D W ( x 1 , x 2 )
2 = ( x 1 − x 2 ) ⊤ L ⊤ L ( x 1 − x 2 ) = ‖ L ( x 1 − x 2 ) ‖ 2 2
{\\displaystyle D\_{W}(x\_{1},x\_{2})\^{2}=(x\_{1}-x\_{2})\^{\\top
}L\^{\\top }L(x\_{1}-x\_{2})=\\\|L(x\_{1}-x\_{2})\\\|\_{2}\^{2}} . The
distance D W ( x 1 , x 2 ) 2 = ‖ x 1 ′ − x 2 ′ ‖ 2 2 {\\displaystyle
D\_{W}(x\_{1},x\_{2})\^{2}=\\\|x\_{1}\'-x\_{2}\'\\\|\_{2}\^{2}}
corresponds to the Euclidean distance between the transformed feature
vectors x 1 ′ = L x 1 {\\displaystyle x\_{1}\'=Lx\_{1}} and x 2 ′ = L x
2 {\\displaystyle x\_{2}\'=Lx\_{2}} . Many formulations for metric
learning have been proposed. Some well-known approaches for metric
learning include Learning from relative comparisons which is based on
the Triplet loss, Large margin nearest neighbor, Information theoretic
metric learning (ITML).In statistics, the covariance matrix of the data
is sometimes used to define a distance metric called Mahalanobis
distance. Applications Similarity learning is used in information
retrieval for learning to rank, in face verification or face
identification, and in recommendation systems. Also, many machine
learning approaches rely on some metric. This includes unsupervised
learning such as clustering, which groups together close or similar
objects. It also includes supervised approaches like K-nearest neighbor
algorithm which rely on labels of nearby objects to decide on the label
of a new object. Metric learning has been proposed as a preprocessing
step for many of these approaches. Scalability Metric and similarity
learning naively scale quadratically with the dimension of the input
space, as can easily see when the learned metric has a bilinear form f W
( x , z ) = x T W z {\\displaystyle f\_{W}(x,z)=x\^{T}Wz} . Scaling to
higher dimensions can be achieved by enforcing a sparseness structure
over the matrix model, as done with HDSL, and with COMET. Software
metric-learn is a free software Python library which offers efficient
implementations of several supervised and weakly-supervised similarity
and metric learning algorithms. The API of metric-learn is compatible
with scikit-learn.OpenMetricLearning is a Python framework to train and
validate the models producing high-quality embeddings. See also Kernel
method Learning to rank Latent semantic analysis Further reading For
further information on this topic, see the surveys on metric and
similarity learning by Bellet et al. and Kulis. == References ==
