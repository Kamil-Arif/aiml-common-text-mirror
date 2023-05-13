In representation learning, knowledge graph embedding (KGE), also
referred to as knowledge representation learning (KRL), or
multi-relation learning, is a machine learning task of learning a
low-dimensional representation of a knowledge graph\'s entities and
relations while preserving their semantic meaning. Leveraging their
embedded representation, knowledge graphs (KGs) can be used for various
applications such as link prediction, triple classification, entity
recognition, clustering, and relation extraction. Definition A knowledge
graph G = { E , R , F } {\\displaystyle {\\mathcal {G}}=\\{E,R,F\\}} is
a collection of entities E {\\displaystyle E} , relations R
{\\displaystyle R} , and facts F {\\displaystyle F} . A fact is a triple
( h , r , t ) ∈ F {\\displaystyle (h,r,t)\\in F} that denotes a link r ∈
R {\\displaystyle r\\in R} between the head h ∈ E {\\displaystyle h\\in
E} and the tail t ∈ E {\\displaystyle t\\in E} of the triple. Another
notation that is often used in the literature to represent a triple (or
fact) is \< h e a d , r e l a t i o n , t a i l \> {\\displaystyle } .
This notation is called resource description framework (RDF). A
knowledge graph represents the knowledge related to a specific domain;
leveraging this structured representation, it is possible to infer a
piece of new knowledge from it after some refinement steps. However,
nowadays, people have to deal with the sparsity of data and the
computational inefficiency to use them in a real-world application.The
embedding of a knowledge graph translates each entity and relation of a
knowledge graph, G {\\displaystyle {\\mathcal {G}}} into a vector of a
given dimension d {\\displaystyle d} , called embedding dimension. In
the general case, we can have different embedding dimensions for the
entities d {\\displaystyle d} and the relations k {\\displaystyle k} .
The collection of embedding vectors for all the entities and relations
in the knowledge graph are a more dense and efficient representation of
the domain that can more easily be used for many different tasks.A
knowledge graph embedding is characterized by four different aspects:
Representation space: The low-dimensional space in which the entities
and relations are represented. Scoring function: A measure of the
goodness of a triple embedded representation. Encoding models: The
modality in which the embedded representation of the entities and
relations interact with each other. Additional information: Any
additional information coming from the knowledge graph that can enrich
the embedded representation. Usually, an ad hoc scoring function is
integrated into the general scoring function for each additional
information. Embedding procedure All the different knowledge graph
embedding models follow roughly the same procedure to learn the semantic
meaning of the facts. First of all, to learn an embedded representation
of a knowledge graph, the embedding vectors of the entities and
relations are initialized to random values. Then, starting from a
training set until a stop condition is reached, the algorithm
continuously optimizes the embeddings. Usually, the stop condition is
given by the overfitting over the training set. For each iteration, is
sampled a batch of size b {\\displaystyle b} from the training set, and
for each triple of the batch is sampled a random corrupted fact---i.e.,
a triple that does not represent a true fact in the knowledge graph. The
corruption of a triple involves substituting the head or the tail (or
both) of the triple with another entity that makes the fact false. The
original triple and the corrupted triple are added in the training
batch, and then the embeddings are updated, optimizing a scoring
function. At the end of the algorithm, the learned embeddings should
have extracted the semantic meaning from the triples and should
correctly unseen true facts in the knowledge graph. Pseudocode The
following is the pseudocode for the general embedding procedure.
algorithm Compute entity and relation embeddings is input: The training
set S = { ( h , r , t ) } {\\displaystyle S=\\{(h,r,t)\\}} , entity set
E {\\displaystyle E} , relation set R {\\displaystyle R} , embedding
dimension k {\\displaystyle k} output: Entity and relation embeddings
initialization: the entities e {\\displaystyle e} and relations r
{\\displaystyle r} embeddings (vectors) are randomly initialized while
stop condition do S b a t c h ← s a m p l e ( S , b ) {\\displaystyle
S\_{batch}\\leftarrow sample(S,b)} // From the training set randomly
sample a batch of size b for each ( h , r , t ) {\\displaystyle (h,r,t)}
in S b a t c h {\\displaystyle S\_{batch}} do ( h ′ , r , t ′ ) ← s a m
p l e ( S ′ ) {\\displaystyle (h\',r,t\')\\leftarrow sample(S\')} //
sample a corrupted fact of triple T b a t c h ← T b a t c h ∪ { ( ( h ,
r , t ) , ( h ′ , r , t ′ ) ) } {\\displaystyle T\_{batch}\\leftarrow
T\_{batch}\\cup \\{((h,r,t),(h\',r,t\'))\\}} end for Update embeddings
by minimizing the loss function end while Performance indicators These
indexes are often used to measure the embedding quality of a model. The
simplicity of the indexes makes them very suitable for evaluating the
performance of an embedding algorithm even on a large scale. Given Q
{\\displaystyle {\\ce {Q}}} as the set of all ranked predictions of a
model, it is possible to define three different performance indexes:
Hits@K, MR, and MRR. Hits@K Hits@K or in short, H@K, is a performance
index that measures the probability to find the correct prediction in
the first top K model predictions. Usually, it is used k = 10
{\\displaystyle k=10} . Hits@K reflects the accuracy of an embedding
model to predict the relation between two given triples correctly.Hits@K
= \| { q ∈ Q : q \< k } \| \| Q \| ∈ \[ 0 , 1 \] {\\displaystyle
={\\frac {\|\\{q\\in Q:q } {\\displaystyle {\\mathcal {F}}=\\{\\}} , the
knowledge graph embedding model produces, for each entity and relation
present in the knowledge graph a continuous vector representation. ( h ,
r , t ) {\\displaystyle (h,r,t)} is the corresponding embedding of a
triple with h , t ∈ I R d {\\displaystyle h,t\\in {\\rm {I\\!R}}\^{d}}
and r ∈ I R k {\\displaystyle r\\in {\\rm {I\\!R}}\^{k}} , where d
{\\displaystyle d} is the embedding dimension for the entities, and k
{\\displaystyle k} for the relations. The score function of a given
model is denoted by f r ( h , t ) {\\displaystyle {\\mathcal
{f}}\_{r}(h,t)} and measures the distance of the embedding of the head
from the embedding of tail given the embedding of the relation, or in
other words, it quantifies the plausibility of the embedded
representation of a given fact.Rossi et al. propose a taxonomy of the
embedding models and identifies three main families of models: tensor
decomposition models, geometric models, and deep learning models. Tensor
decomposition model The tensor decomposition is a family of knowledge
graph embedding models that use a multi-dimensional matrix to represent
a knowledge graph, that is partially knowable due to the gaps of the
knowledge graph describing a particular domain thoroughly. In
particular, these models use a three-way (3D) tensor, which is then
factorized into low-dimensional vectors that are the entities and
relations embeddings. The third-order tensor is a suitable methodology
to represent a knowledge graph because it records only the existence or
the absence of a relation between entities, and for this reason is
simple, and there is no need to know a priori the network structure,
making this class of embedding models light, and easy to train even if
they suffer from high-dimensional and sparsity of data. Bilinear models
This family of models uses a linear equation to embed the connection
between the entities through a relation. In particular, the embedded
representation of the relations is a bidimensional matrix. These models,
during the embedding procedure, only use the single facts to compute the
embedded representation and ignore the other associations to the same
entity or relation. DistMult: Since the embedding matrix of the relation
is a diagonal matrix, the scoring function can not distinguish
asymmetric facts. ComplEx: As DistMult uses a diagonal matrix to
represent the relations embedding but adds a representation in the
complex vector space and the hermitian product, it can distinguish
symmetric and asymmetric facts. This approach is scalable to a large
knowledge graph in terms of time and space cost. ANALOGY: This model
encodes in the embedding the analogical structure of the knowledge graph
to simulate inductive reasoning. Using a differentiable objective
function, ANALOGY has good theoretical generality and computational
scalability. It is proven that the embedding produced by ANALOGY fully
recovers the embedding of DistMult, ComplEx, and HolE. SimplE: This
model is the improvement of canonical polyadic decomposition (CP), in
which an embedding vector for the relation and two independent embedding
vectors for each entity are learned, depending on whether it is a head
or a tail in the knowledge graph fact. SimplE resolves the problem of
independent learning of the two entity embeddings using an inverse
relation and average the CP score of ( h , r , t ) {\\displaystyle
(h,r,t)} and ( t , r − 1 , h ) {\\displaystyle (t,r\^{-1},h)} . In this
way, SimplE collects the relation between entities while they appear in
the role of subject or object inside a fact, and it is able to embed
asymmetric relations. Non-bilinear models HolE: HolE uses circular
correlation to create an embedded representation of the knowledge graph,
which can be seen as a compression of the matrix product, but is more
computationally efficient and scalable while keeping the capabilities to
express asymmetric relation since the circular correlation is not
commutative. HolE links holographic and complex embeddings since, if
used together with Fourier, can be seen as a special case of ComplEx.
TuckER: TuckER sees the knowledge graph as a tensor that could be
decomposed using the Tucker decomposition in a collection of
vectors---i.e., the embeddings of entities and relations---with a shared
core. The weights of the core tensor are learned together with the
embeddings and represent the level of interaction of the entries. Each
entity and relation has its own embedding dimension, and the size of the
core tensor is determined by the shape of the entities and relations
that interact. The embedding of the subject and object of a fact are
summed in the same way, making TuckER fully expressive, and other
embedding models such as RESCAL, DistMult, ComplEx, and SimplE can be
expressed as a special formulation of TuckER. MEI: MEI introduces the
multi-partition embedding interaction technique with the block term
tensor format, which is a generalization of CP decomposition and Tucker
decomposition. It divides the embedding vector into multiple partitions
and learns the local interaction patterns from data instead of using
fixed special patterns as in ComplEx or SimplE models. This enables MEI
to achieve optimal efficiency\--expressiveness trade-off, not just being
fully expressive. Previous models such as TuckER, RESCAL, DistMult,
ComplEx, and SimplE are suboptimal restricted special cases of MEI.
MEIM: MEIM goes beyond the block term tensor format to introduce the
independent core tensor for ensemble boosting effects and the soft
orthogonality for max-rank relational mapping, in addition to
multi-partition embedding interaction. MEIM generalizes several previous
models such as MEI and its subsumed models, RotaE, and QuatE. MEIM
improves expressiveness while still being highly efficient in practice,
helping it achieve good results using fairly small model sizes.
Geometric models The geometric space defined by this family of models
encodes the relation as a geometric transformation between the head and
tail of a fact. For this reason, to compute the embedding of the tail,
it is necessary to apply a transformation τ {\\displaystyle \\tau } to
the head embedding, and a distance function δ {\\displaystyle \\delta }
is used to measure the goodness of the embedding or to score the
reliability of a fact. f r ( h , t ) = δ ( τ ( h , r ) , t )
{\\displaystyle {\\mathcal {f}}\_{r}(h,t)=\\delta (\\tau (h,r),t)}
Geometric models are similar to the tensor decomposition model, but the
main difference between the two is that they have to preserve the
applicability of the transformation τ {\\displaystyle \\tau } in the
geometric space in which it is defined. Pure translational models This
class of models is inspired by the idea of translation invariance
introduced in word2vec. A pure translational model relies on the fact
that the embedding vector of the entities are close to each other after
applying a proper relational translation in the geometric space in which
they are defined. In other words, given a fact, when the embedding of
head is added to the embedding of relation, the expected result should
be the embedding of the tail. The closeness of the entities embedding is
given by some distance measure and quantifies the reliability of a fact.
TransE: This model uses a scoring function that forces the embeddings to
satisfy a simple vector sum equation in each fact in which they appear:
h + r = t {\\displaystyle h+r=t} . The embedding will be exact if each
entity and relation appears in only one fact, and, for this reason, in
practice does not well represent one-to-many, many-to-one, and
asymmetric relations. TransH: It is an evolution of TransE introducing a
hyperplane as geometric space to solve the problem of representing
correctly the types of relations. In TransH, each relation has a
different embedded representation, on a different hyperplane, based on
which entities it interacts with. Therefore, to compute, for example,
the score function of a fact, the embedded representation of the head
and tail need to be projected using a relational projection matrix on
the correct hyperplane of the relation. TransR: TransR is an evolution
of TransH because it uses two different spaces to represent the embedded
representation of the entities and the relations, and separate
completely the semantic space of entities and relations. Also TransR
uses a relational projection matrix to translate the embedding of the
entities to the relation space. TransD: Given a fact, in TransR, the
head and the tail of a fact could belongs to two different types of
entities, for example, in the fact ( O b a m a , p r e s i d e n t \_ o
f , U S A ) {\\displaystyle (Obama,president\\\_of,USA)} , Obama and USA
are two entities but one is a person and the other is a country. The
matrix multiplication also is an expensive procedure in TransR to
compute the projection. In this context, TransD employs two vector for
each entity-relation pair to compute a dynamic mapping that substitutes
the projection matrix while reducing the dimensional complexity. The
first vector is used to represent the semantic meaning of the entities
and relations, the second one to compute the mapping matrix. TransA: All
the translational models define a score function in their representation
space, but they oversimplify this metric loss. Since the vector
representation of the entities and relations is not perfect, a pure
translation of h + r {\\displaystyle h+r} could be distant from t
{\\displaystyle t} , and a spherical equipotential Euclidean distance
makes it hard to distinguish which is the closest entity. TransA,
instead, introduces an adaptive Mahalanobis distance to weights the
embedding dimensions, together with elliptical surfaces to remove the
ambiguity. Translational models with additional embeddings It is
possible to associate additional information to each element in the
knowledge graph and their common representation facts. Each entity and
relation can be enriched with text descriptions, weights, constraints,
and others in order to improve the overall description of the domain
with a knowledge graph. During the embedding of the knowledge graph,
this information can be used to learn specialized embeddings for these
characteristics together with the usual embedded representation of
entities and relations, with the cost of learning a more significant
number of vectors. STransE: This model is the result of the combination
of TransE and of the structure embedding in such a way it is able to
better represent the one-to-many, many-to-one, and many-to-many
relations. To do so, the model involves two additional independent
matrix W r h {\\displaystyle W\_{r}\^{h}} and W r t {\\displaystyle
W\_{r}\^{t}} for each embedded relation r {\\displaystyle r} in the KG.
Each additional matrix is used based on the fact the specific relation
interact with the head or the tail of the fact. In other words, given a
fact ( h , r , t ) {\\displaystyle (h,r,t)} , before applying the vector
translation, the head h {\\displaystyle h} is multiplied by W r h
{\\displaystyle W\_{r}\^{h}} and the tail is multiplied by W r t
{\\displaystyle W\_{r}\^{t}} . CrossE: Crossover interactions can be
used for related information selection, and could be very useful for the
embedding procedure. Crossover interactions provide two distinct
contributions in the information selection: interactions from relations
to entities and interactions from entities to relations. This means that
a relation, e.g.\'president_of\' automatically selects the types of
entities that are connecting the subject to the object of a fact. In a
similar way, the entity of a fact inderectly determine which is
inference path that has to be choose to predict the object of a related
triple. CrossE, to do so, learns an additional interaction matrix C
{\\displaystyle C} , uses the element-wise product to compute the
interaction between h {\\displaystyle h} and r {\\displaystyle r} . Even
if, CrossE, does not rely on a neural network architecture, it is shown
that this methodology can be encoded in such architecture.
Roto-translational models This family of models, in addition or in
substitution of a translation they employ a rotation-like
transformation. TorusE: The regularization term of TransE makes the
entity embedding to built a spheric space, and consequently loses the
translation properties of the geometric space. To address this problem,
TorusE leverages the use of a compact Lie group that in this specific
case is n-dimensional torus space, and avoid the use of regularization.
TorusE defines the distance functions to substitute the L1 and L2 norm
of TransE. RotatE: RotatE is inspired by the Euler\'s identity and
involves the use of Hadmard product to represent a relation r
{\\displaystyle r} as a rotation from the head h {\\displaystyle h} to
the tail t {\\displaystyle t} in the complex space. For each element of
the triple, the complex part of the embedding describes a
counterclockwise rotation respect to an axis, that can be describe with
the Euler\'s identity, whereas the modulus of the relation vector is 1.
It is shown that the model is capable of embedding symmetric,
asymmetric, inversion, and composition relations from the knowledge
graph. Deep learning models This group of embedding models uses deep
neural network to learn patterns from the knowledge graph that are the
input data. These models have the generality to distinguish the type of
entity and relation, temporal information, path information, underlay
structured information, and resolve the limitations of distance-based
and semantic-matching-based models in representing all the features of a
knowledge graph. The use of deep learning for knowledge graph embedding
has shown good predictive performance even if they are more expensive in
the training phase, angry of data, and often required a pre-trained
embedding representation of knowledge graph coming from a different
embedding model. Convolutional neural networks This family of models,
instead of using fully connected layers, employs one or more
convolutional layers that convolve the input data applying a
low-dimensional filter capable of embedding complex structures with few
parameters by learning nonlinear features. ConvE: ConvE is an embedding
model that represents a good tradeoff expressiveness of deep learning
models and computational expensiveness, in fact it is shown that it used
8x less parameters, when compared to DistMult. ConvE uses a
one-dimensional d {\\displaystyle d} -sized embedding to represent the
entities and relations of a knowledge graph. To compute the score
function of a triple, ConvE apply a simple procedure: first concatenes
and merge the embeddings of the head of the triple and the relation in a
single data \[ h ; r \] {\\displaystyle {\\ce {\[h;{\\mathcal {r}}\]}}}
, then this matrix is used as input for the 2D convolutional layer. The
result is then passed through a dense layer that apply a linear
transformation parameterized by the matrix W {\\displaystyle {\\mathcal
{W}}} and at the end, with the inner product is linked to the tail
triple. ConvE is also particularly efficient in the evaluation
procedure: using a 1-N scoring, the model matches, given a head and a
relation, all the tails at the same time, saving a lot of evaluation
time when compared to the 1-1 evaluation program of the other models.
ConvR: ConvR is an adaptive convolutional network aimed to deeply
represent all the possible interactions between the entities and the
relations. For this task, ConvR, computes convolutional filter for each
relation, and , when required, applies these filters to the entity of
interest to extract convoluted features. The procedure to compute the
score of triple is the same as ConvE. ConvKB: ConvKB, to compute score
function of a given triple ( h , r , t ) {\\displaystyle (h,r,t)} , it
produces an input \[ h ; r ; t \] {\\displaystyle {\\ce {\[h;{\\mathcal
{r}};t\]}}} of dimension d × 3 {\\displaystyle d\\times 3} without
reshaping and passes it to series of convolutional filter of size 1 × 3
{\\displaystyle 1\\times 3} . This result feeds a dense layer with only
one neuron that produces the final score. The single final neuron makes
this architecture as a binary classifier in which the fact could be true
or false. A difference with ConvE is that the dimensionality of the
entities is not changed. Capsule neural networks This family of models
uses capsule neural networks to create a more stable representation that
is able to recognize a feature in the input without losing spatial
information. The network is composed of convolutional layers, but they
are organized in capsules, and the overall result of a capsule is sent
to a higher-capsule decided by a dynamic process routine. CapsE: CapsE
implements a capsule network to model a fact ( h , r , t )
{\\displaystyle (h,r,t)} . Like in ConvKB, each triple element is
concatenated to built a matrix \[ h ; r ; t \] {\\displaystyle {\\ce
{\[h;{\\mathcal {r}};t\]}}} and is used to feed to a convolutional layer
to extract the convolutional features. These features are then
redirected to a capsule to produce a continuous vector, more the vector
is long, more the fact is true. Recurrent neural networks This class of
models leverages the use of recurrent neural network. The advantage of
this architecture is to memorize a sequence of fact, rather than just
elaborate single events. RSN: During the embedding procedure is commonly
assumed that, similar entities has similar relations. In practice, this
type of information is not leveraged, because the embedding is computed
just on the undergoing fact rather than a history of facts. Recurrent
skipping networks (RSN) uses a recurrent neural network to learn
relational path using a random walk sampling. Model performance The
machine learning task for knowledge graph embedding that is more often
used to evaluate the embedding accuracy of the models is the link
prediction. Rossi et al. produced an extensive benchmark of the models,
but also other surveys produces similar results. The benchmark involves
five datasets FB15k, WN18, FB15k-237, WN18RR, and YAGO3-10. More
recently, it has been discussed that these datasets are far away from
real-world applications, and other datasets should be integrated as a
standard benchmark. Libraries KGE on GitHub MEI-KGE on GitHub Pykg2vec
on GitHub DGL-KE on GitHub PyKEEN on GitHub TorchKGE on GitHub
AmpliGraph on GitHub OpenKE on GitHub scikit-kge on GitHub Fast-TransX
on GitHub MEIM-KGE on GitHub DICEE on GitHub See also Knowledge graph
Embedding Machine learning Knowledge base Knowledge extraction
Statistical relational learning Representation learning Graph embedding
References External links Open Graph Benchmark - Stanford WordNet -
Princeton
