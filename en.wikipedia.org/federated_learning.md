Federated learning (also known as collaborative learning) is a machine
learning technique that trains an algorithm via multiple independent
sessions, each using its own dataset. This approach stands in contrast
to traditional centralized machine learning techniques where local
datasets are merged into one training session, as well as to approaches
that assume that local data samples are identically distributed.
Federated learning enables multiple actors to build a common, robust
machine learning model without sharing data, thus addressing critical
issues such as data privacy, data security, data access rights and
access to heterogeneous data. Its applications engage industries
including defense, telecommunications, Internet of Things, and
pharmaceuticals. A major open question at is when/whether federated
learning is preferable to pooled data learning. Another open question
concerns the trustworthiness of the devices and the impact of malicious
actors on the learned model. Definition Federated learning aims at
training a machine learning algorithm, for instance deep neural
networks, on multiple local datasets contained in local nodes without
explicitly exchanging data samples. The general principle consists in
training local models on local data samples and exchanging parameters
(e.g. the weights and biases of a deep neural network) between these
local nodes at some frequency to generate a global model shared by all
nodes. The main difference between federated learning and distributed
learning lies in the assumptions made on the properties of the local
datasets, as distributed learning originally aims at parallelizing
computing power where federated learning originally aims at training on
heterogeneous datasets. While distributed learning also aims at training
a single model on multiple servers, a common underlying assumption is
that the local datasets are independent and identically distributed
(i.i.d.) and roughly have the same size. None of these hypotheses are
made for federated learning; instead, the datasets are typically
heterogeneous and their sizes may span several orders of magnitude.
Moreover, the clients involved in federated learning may be unreliable
as they are subject to more failures or drop out since they commonly
rely on less powerful communication media (i.e. Wi-Fi) and
battery-powered systems (i.e. smartphones and IoT devices) compared to
distributed learning where nodes are typically datacenters that have
powerful computational capabilities and are connected to one another
with fast networks. Mathematical formulation The objective function for
federated learning is as follows: f ( x 1 , ... , x K ) = 1 K ∑ i = 1 K
f i ( x i ) {\\displaystyle f(\\mathbf {x} \_{1},\\dots ,\\mathbf {x}
\_{K})={\\dfrac {1}{K}}\\sum \_{i=1}\^{K}f\_{i}(\\mathbf {x} \_{i})}
where K {\\displaystyle K} is the number of nodes, x i {\\displaystyle
\\mathbf {x} \_{i}} are the weights of model as viewed by node i
{\\displaystyle i} , and f i {\\displaystyle f\_{i}} is node i
{\\displaystyle i} \'s local objective function, which describes how
model weights x i {\\displaystyle \\mathbf {x} \_{i}} conforms to node i
{\\displaystyle i} \'s local dataset. The goal of federated learning is
to train a common model on all of the nodes\' local datasets, in other
words: Optimizing the objective function f ( x 1 , ... , x K )
{\\displaystyle f(\\mathbf {x} \_{1},\\dots ,\\mathbf {x} \_{K})}
.Achieving consensus on x i {\\displaystyle \\mathbf {x} \_{i}} . In
other words, x 1 , ... , x K {\\displaystyle \\mathbf {x} \_{1},\\dots
,\\mathbf {x} \_{K}} converge to some common x {\\displaystyle \\mathbf
{x} } at the end of the training process. Centralized federated learning
In the centralized federated learning setting, a central server is used
to orchestrate the different steps of the algorithms and coordinate all
the participating nodes during the learning process. The server is
responsible for the nodes selection at the beginning of the training
process and for the aggregation of the received model updates. Since all
the selected nodes have to send updates to a single entity, the server
may become a bottleneck of the system. Decentralized federated learning
In the decentralized federated learning setting, the nodes are able to
coordinate themselves to obtain the global model. This setup prevents
single point failures as the model updates are exchanged only between
interconnected nodes without the orchestration of the central server.
Nevertheless, the specific network topology may affect the performances
of the learning process. See blockchain-based federated learning and the
references therein. Heterogeneous federated learning An increasing
number of application domains involve a large set of heterogeneous
clients, e.g., mobile phones and IoT devices. Most of the existing
Federated learning strategies assume that local models share the same
global model architecture. Recently, a new federated learning framework
named HeteroFL was developed to address heterogeneous clients equipped
with very different computation and communication capabilities. The
HeteroFL technique can enable the training of heterogeneous local models
with dynamically varying computation and non-iid data complexities while
still producing a single accurate global inference model. Main features
Iterative learning To ensure good task performance of a final, central
machine learning model, federated learning relies on an iterative
process broken up into an atomic set of client-server interactions known
as a federated learning round. Each round of this process consists in
transmitting the current global model state to participating nodes,
training local models on these local nodes to produce a set of potential
model updates at each node, and then aggregating and processing these
local updates into a single global update and applying it to the global
model.In the methodology below, a central server is used for
aggregation, while local nodes perform local training depending on the
central server\'s orders. However, other strategies lead to the same
results without central servers, in a peer-to-peer approach, using
gossip or consensus methodologies.Assuming a federated round composed by
one iteration of the learning process, the learning procedure can be
summarized as follows: Initialization: according to the server inputs, a
machine learning model (e.g., linear regression, neural network,
boosting) is chosen to be trained on local nodes and initialized. Then,
nodes are activated and wait for the central server to give the
calculation tasks. Client selection: a fraction of local nodes are
selected to start training on local data. The selected nodes acquire the
current statistical model while the others wait for the next federated
round. Configuration: the central server orders selected nodes to
undergo training of the model on their local data in a pre-specified
fashion (e.g., for some mini-batch updates of gradient descent).
Reporting: each selected node sends its local model to the server for
aggregation. The central server aggregates the received models and sends
back the model updates to the nodes. It also handles failures for
disconnected nodes or lost model updates. The next federated round is
started returning to the client selection phase. Termination: once a
pre-defined termination criterion is met (e.g., a maximum number of
iterations is reached or the model accuracy is greater than a threshold)
the central server aggregates the updates and finalizes the global
model.The procedure considered before assumes synchronized model
updates. Recent federated learning developments introduced novel
techniques to tackle asynchronicity during the training process, or
training with dynamically varying models. Compared to synchronous
approaches where local models are exchanged once the computations have
been performed for all layers of the neural network, asynchronous ones
leverage the properties of neural networks to exchange model updates as
soon as the computations of a certain layer are available. These
techniques are also commonly referred to as split learning and they can
be applied both at training and inference time regardless of centralized
or decentralized federated learning settings. Non-IID data In most
cases, the assumption of independent and identically distributed samples
across local nodes does not hold for federated learning setups. Under
this setting, the performances of the training process may vary
significantly according to the unbalanced local data samples as well as
the particular probability distribution of the training examples (i.e.,
features and labels) stored at the local nodes. To further investigate
the effects of non-IID data, the following description considers the
main categories presented in the preprint by Peter Kairouz et al. from
2019.The description of non-IID data relies on the analysis of the joint
probability between features and labels for each node. This allows to
decouple each contribution according to the specific distribution
available at the local nodes. The main categories for non-iid data can
be summarized as follows: Covariate shift: local nodes may store
examples that have different statistical distributions compared to other
nodes. An example occurs in natural language processing datasets where
people typically write the same digits/letters with different stroke
widths or slants. Prior probability shift: local nodes may store labels
that have different statistical distributions compared to other nodes.
This can happen if datasets are regional and/or demographically
partitioned. For example, datasets containing images of animals vary
significantly from country to country. Concept drift (same label,
different features): local nodes may share the same labels but some of
them correspond to different features at different local nodes. For
example, images that depict a particular object can vary according to
the weather condition in which they were captured. Concept shift (same
features, different labels): local nodes may share the same features but
some of them correspond to different labels at different local nodes.
For example, in natural language processing, the sentiment analysis may
yield different sentiments even if the same text is observed.
Unbalanced: the amount of data available at the local nodes may vary
significantly in size.The loss in accuracy due to non-iid data can be
bounded through using more sophisticated means of doing data
normalization, rather than batch normalization. Algorithmic
hyper-parameters Network topology The way the statistical local outputs
are pooled and the way the nodes communicate with each other can change
from the centralized model explained in the previous section. This leads
to a variety of federated learning approaches: for instance no central
orchestrating server, or stochastic communication.In particular,
orchestrator-less distributed networks are one important variation. In
this case, there is no central server dispatching queries to local nodes
and aggregating local models. Each local node sends its outputs to
several randomly-selected others, which aggregate their results locally.
This restrains the number of transactions, thereby sometimes reducing
training time and computing cost. Federated learning parameters Once the
topology of the node network is chosen, one can control different
parameters of the federated learning process (in opposition to the
machine learning model\'s own hyperparameters) to optimize learning:
Number of federated learning rounds: T {\\displaystyle T} Total number
of nodes used in the process: K {\\displaystyle K} Fraction of nodes
used at each iteration for each node: C {\\displaystyle C} Local batch
size used at each learning iteration: B {\\displaystyle B} Other
model-dependent parameters can also be tinkered with, such as: Number of
iterations for local training before pooling: N {\\displaystyle N} Local
learning rate: η {\\displaystyle \\eta } Those parameters have to be
optimized depending on the constraints of the machine learning
application (e.g., available computing power, available memory,
bandwidth). For instance, stochastically choosing a limited fraction C
{\\displaystyle C} of nodes for each iteration diminishes computing cost
and may prevent overfitting, in the same way that stochastic gradient
descent can reduce overfitting. Technical limitations Federated learning
requires frequent communication between nodes during the learning
process. Thus, it requires not only enough local computing power and
memory, but also high bandwidth connections to be able to exchange
parameters of the machine learning model. However, the technology also
avoids data communication, which can require significant resources
before starting centralized machine learning. Nevertheless, the devices
typically employed in federated learning are communication-constrained,
for example IoT devices or smartphones are generally connected to Wi-Fi
networks, thus, even if the models are commonly less expensive to be
transmitted compared to raw data, federated learning mechanisms may not
be suitable in their general form.Federated learning raises several
statistical challenges: Heterogeneity between the different local
datasets: each node may have some bias with respect to the general
population, and the size of the datasets may vary significantly;
Temporal heterogeneity: each local dataset\'s distribution may vary with
time; Interoperability of each node\'s dataset is a prerequisite; Each
node\'s dataset may require regular curations; Hiding training data
might allow attackers to inject backdoors into the global model; Lack of
access to global training data makes it harder to identify unwanted
biases entering the training e.g. age, gender, sexual orientation;
Partial or total loss of model updates due to node failures affecting
the global model; Lack of annotations or labels on the client side.
Heterogeneity between the processing platform Federated learning
variations In this section, the notation of the paper published by H.
Brendan McMahan and al. in 2017 is followed.To describe the federated
strategies, let us introduce some notations: K {\\displaystyle K} :
total number of clients; k {\\displaystyle k} : index of clients; n k
{\\displaystyle n\_{k}} : number of data samples available during
training for client k {\\displaystyle k} ; k t {\\displaystyle k\_{t}} :
model\'s weight vector on client k {\\displaystyle k} , at the federated
round t {\\displaystyle t} ; ℓ ( w , b ) {\\displaystyle \\ell (w,b)} :
loss function for weights w {\\displaystyle w} and batch b
{\\displaystyle b} ; E {\\displaystyle E} : number of local updates;
Federated stochastic gradient descent (FedSGD) Deep learning training
mainly relies on variants of stochastic gradient descent, where
gradients are computed on a random subset of the total dataset and then
used to make one step of the gradient descent. Federated stochastic
gradient descent is the direct transposition of this algorithm to the
federated setting, but by using a random fraction C {\\displaystyle C}
of the nodes and using all the data on this node. The gradients are
averaged by the server proportionally to the number of training samples
on each node, and used to make a gradient descent step. Federated
averaging Federated averaging (FedAvg) is a generalization of FedSGD,
which allows local nodes to perform more than one batch update on local
data and exchanges the updated weights rather than the gradients. The
rationale behind this generalization is that in FedSGD, if all local
nodes start from the same initialization, averaging the gradients is
strictly equivalent to averaging the weights themselves. Further,
averaging tuned weights coming from the same initialization does not
necessarily hurt the resulting averaged model\'s performance. Federated
Learning with Dynamic Regularization (FedDyn) Federated learning methods
suffer when the device datasets are heterogeneously distributed.
Fundamental dilemma in heterogeneously distributed device setting is
that minimizing the device loss functions is not the same as minimizing
the global loss objective. In 2021, Acar et al. introduced FedDyn method
as a solution to heterogenous dataset setting. FedDyn dynamically
regularizes each devices loss function so that the modified device
losses converges to the actual global loss. Since the local losses are
aligned, FedDyn is robust to the different heterogeneity levels and it
can safely perform full minimization in each device. Theoretically,
FedDyn converges to the optimal (a stationary point for nonconvex
losses) by being agnostic to the heterogeneity levels. These claims are
verified with extensive experimentations on various datasets.Minimizing
the number of communications is the gold-standard for comparison in
federated learning. We may also want to decrease the local computation
levels per device in each round. FedDynOneGD is an extension of FedDyn
with less local compute requirements. FedDynOneGD calculates only one
gradients per device in each round and update the model with a
regularized version of the gradient. Hence, the computation complexity
is linear in local dataset size. Moreover, gradient computation can be
parallelizable within each device which is different from successive SGD
steps. Theoretically, FedDynOneGD achieves the same convergence
guarantees as in FedDyn with less local computation. Personalized
Federated Learning by Pruning (Sub-FedAvg) Federated Learning methods
cannot achieve good global performance under Non-IID settings which
motivates the participating clients to yield personalized models in
federation. Recently, Vahidian et al. introduced Sub-FedAvg opening a
new personalized FL algorithm paradigm by proposing Hybrid Pruning
(structured + unstructured pruning) with averaging on the intersection
of clients' drawn subnetworks which simultaneously handles communication
efficiency, resource constraints and personalized models
accuracies.Sub-FedAvg is the first work which shows existence of
personalized winning tickets for clients in federated learning through
experiments. Moreover, it also proposes two algorithms on how to
effectively draw the personalized subnetworks. Sub-FedAvg tries to
extend \"Lottery Ticket Hypothesis\" which is for centrally trained
neural networks to federated learning trained neural networks leading to
this open research problem: "Do winning tickets exist for clients'
neural networks being trained in federated learning? If yes, how to
effectively draw the personalized subnetworks for each client?" Dynamic
Aggregation - Inverse Distance Aggregation IDA (Inverse Distance
Aggregation) is a novel adaptive weighting approach for clients based on
meta-information which handles unbalanced and non-iid data. It uses the
distance of the model parameters as a strategy to minimize the effect of
outliers and improve the model\'s convergence rate. Hybrid Federated
Dual Coordinate Ascent (HyFDCA) Very few methods for hybrid federated
learning, where clients only hold subsets of both features and samples,
exist. Yet, this scenario is very important in practical settings.
Hybrid Federated Dual Coordinate Ascent (HyFDCA) is a novel algorithm
proposed in 2022 that solves convex problems in the hybrid FL setting.
This algorithm extends CoCoA, a primal-dual distributed optimization
algorithm introduced by Jaggi et al. (2014) and Smith et al. (2017), to
the case where both samples and features are partitioned across clients.
HyFDCA claims several improvement over existing algorithms: HyFDCA is a
provably convergent primal-dual algorithm for hybrid FL in at least the
following settings. Hybrid Federated Setting with Complete Client
Participation Horizontal Federated Setting with Random Subsets of
Available Clients The authors show HyFDCA enjoys a convergence rate of
O(1⁄t) which matches the convergence rate of FedAvg (see below).
Vertical Federated Setting with Incomplete Client Participation The
authors show HyFDCA enjoys a convergence rate of O(log(t)⁄t) whereas
FedBCD exhibits a slower O(1⁄sqrt(t)) convergence rate and requires full
client participation. HyFDCA provides the privacy steps that ensure
privacy of client data in the primal-dual setting. These principles
apply to future efforts in developing primal-dual algorithms for FL.
HyFDCA empirically outperforms FedAvg in loss function value and
validation accuracy across a multitude of problem settings and datasets.
The authors also introduce a hyperparameter selection framework for FL
with competing metrics using ideas from multiobjective
optimization.There is only one other algorithm that focuses on hybrid
FL, HyFEM proposed by Zhang et al. (2020). This algorithm uses a feature
matching formulation that balances clients building accurate local
models and the server learning an accurate global model. This requires a
matching regularizer constant that must be tuned based on user goals and
results in disparate local and global models. Furthermore, the
convergence results provided for HyFEM only prove convergence of the
matching formulation not of the original global problem. This work is
substantially different than HyFDCA\'s approach which uses data on local
clients to build a global model that converges to the same solution as
if the model was trained centrally. Furthermore, the local and global
models are synchronized and do not require the adjustment of a matching
parameter between local and global models. However, HyFEM is suitable
for a vast array of architectures including deep learning architectures,
whereas HyFDCA is designed for convex problems like logistic regression
and support vector machines. Federated ViT using Dynamic Aggregation
(FED-REV) Federated Learning (FL) provides training of global shared
model using decentralized data sources on edge nodes while preserving
data privacy. However, its performance in the computer vision
applications using Convolution neural network (CNN) considerably behind
that of centralized training due to limited communication resources and
low processing capability at edge nodes. Alternatively, Pure Vision
transformer models (VIT) outperform CNNs by almost four times when it
comes to computational efficiency and accuracy. Hence, we propose a new
FL model with reconstructive strategy called FED-REV, Illustrates how
attention-based structures (pure Vision Transformers) enhance FL
accuracy over large and diverse data distributed over edge nodes, in
addition to the proposed reconstruction strategy that determines the
dimensions influence of each stage of the vision transformer and then
reduce its dimension complexity which reduce computation cost of edge
devices in addition to preserving accuracy achieved due to using the
pure Vision transformer. Current research topics Federated learning has
started to emerge as an important research topic in 2015 and 2016, with
the first publications on federated averaging in telecommunication
settings. Another important aspect of active research is the reduction
of the communication burden during the federated learning process. In
2017 and 2018, publications have emphasized the development of resource
allocation strategies, especially to reduce communication requirements
between nodes with gossip algorithms as well as on the characterization
of the robustness to differential privacy attacks. Other research
activities focus on the reduction of the bandwidth during training
through sparsification and quantization methods, where the machine
learning models are sparsified and/or compressed before they are shared
with other nodes. Developing ultra-light DNN architectures is essential
for device-/edge- learning and recent work recognises both the energy
efficiency requirements for future federated learning and the need to
compress deep learning, especially during learning.Recent research
advancements are starting to consider real-world propagating channels as
in previous implementations ideal channels were assumed. Another active
direction of research is to develop Federated learning for training
heterogeneous local models with varying computation complexities and
producing a single powerful global inference model.A learning framework
named Assisted learning was recently developed to improve each agent\'s
learning capabilities without transmitting private data, models, and
even learning objectives. Compared with Federated learning that often
requires a central controller to orchestrate the learning and
optimization, Assisted learning aims to provide protocols for the agents
to optimize and learn among themselves without a global model. Use cases
Federated learning typically applies when individual actors need to
train models on larger datasets than their own, but cannot afford to
share the data in itself with others (e.g., for legal, strategic or
economic reasons). The technology yet requires good connections between
local servers and minimum computational power for each node.
Transportation: self-driving cars Self-driving cars encapsulate many
machine learning technologies to function: computer vision for analyzing
obstacles, machine learning for adapting their pace to the environment
(e.g., bumpiness of the road). Due to the potential high number of
self-driving cars and the need for them to quickly respond to real world
situations, traditional cloud approach may generate safety risks.
Federated learning can represent a solution for limiting volume of data
transfer and accelerating learning processes. Industry 4.0: smart
manufacturing In Industry 4.0, there is a widespread adoption of machine
learning techniques to improve the efficiency and effectiveness of
industrial process while guaranteeing a high level of safety.
Nevertheless, privacy of sensitive data for industries and manufacturing
companies is of paramount importance. Federated learning algorithms can
be applied to these problems as they do not disclose any sensitive data.
In addition, FL also implemented for PM2.5 prediction to support Smart
city sensing applications. Medicine: digital health Federated learning
seeks to address the problem of data governance and privacy by training
algorithms collaboratively without exchanging the data itself. Today\'s
standard approach of centralizing data from multiple centers comes at
the cost of critical concerns regarding patient privacy and data
protection. To solve this problem, the ability to train machine learning
models at scale across multiple medical institutions without moving the
data is a critical technology. Nature Digital Medicine published the
paper \"The Future of Digital Health with Federated Learning\" in
September 2020, in which the authors explore how federated learning may
provide a solution for the future of digital health, and highlight the
challenges and considerations that need to be addressed. Recently, a
collaboration of 20 different institutions around the world validated
the utility of training AI models using federated learning. In a paper
published in Nature Medicine \"Federated learning for predicting
clinical outcomes in patients with COVID-19\", they showcased the
accuracy and generalizability of a federated AI model for the prediction
of oxygen needs in patients with COVID-19 infections. Furthermore, in a
published paper \"A Systematic Review of Federated Learning in the
Healthcare Area: From the Perspective of Data Properties and
Applications\", the authors trying to provide a set of challenges on FL
challenges on medical data-centric perspective. Robotics Robotics
includes a wide range of applications of machine learning methods: from
perception and decision-making to control. As robotic technologies have
been increasingly deployed from simple and repetitive tasks (e.g.
repetitive manipulation) to complex and unpredictable tasks (e.g.
autonomous navigation), the need for machine learning grows. Federated
Learning provides a solution to improve over conventional machine
learning training methods. In the paper, mobile robots learned
navigation over diverse environments using the FL-based method, helping
generalization. In the paper, Federated Learning is applied to improve
multi-robot navigation under limited communication bandwidth scenarios,
which is a current challenge in real-world learning-based robotic tasks.
In the paper, Federated Learning is used to learn Vision-based
navigation, helping better sim-to-real transfer. References External
links \"Regulation (EU) 2016/679 of the European Parliament and of the
Council of 27 April 2016\" at eur-lex.europa.eu. Retrieved October 18,
2019. \"Data minimisation and privacy-preserving techniques in AI
systems\" Archived 2020-07-23 at the Wayback Machine at UK Information
Commissioners Office. Retrieved July 22, 2020 \"Realising the Potential
of Data Whilst Preserving Privacy with EyA and Conclave from R3\" at
eya.global. Retrieved March 31, 2022.
