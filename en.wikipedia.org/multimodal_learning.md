Multimodal learning attempts to model the combination of different
modalities of data, often arising in real-world applications. An example
of multi-modal data is data that combines text (typically represented as
discrete word count vectors) with imaging data consisting of pixel
intensities and annotation tags. As these modalities have fundamentally
different statistical properties, combining them is non-trivial, which
is why specialized modelling strategies and algorithms are required.
Motivation Many models and algorithms have been implemented to retrieve
and classify a certain type of data, e.g. image or text (where humans
who interact with machines can extract images in a form of pictures and
text that could be any message etc.). However, data usually comes with
different modalities (it is the degree to which a system\'s components
may be separated or combined) which carry different information. For
example, it is very common to caption an image to convey the information
not presented in the image itself. Similarly, sometimes it is more
straightforward to use an image to describe the information which may
not be obvious from texts. As a result, if different words appear in
similar images, then these words likely describe the same thing.
Conversely, if a word is used to describe seemingly dissimilar images,
then these images may represent the same object. Thus, in cases dealing
with multi-modal data, it is important to use a model which is able to
jointly represent the information such that the model can capture the
correlation structure between different modalities. Moreover, it should
also be able to recover missing modalities given observed ones (e.g.
predicting possible image object according to text description). The
Multimodal Deep Boltzmann Machine model satisfies the above purposes.
Background: Boltzmann machine A Boltzmann machine is a type of
stochastic neural network invented by Geoffrey Hinton and Terry
Sejnowski in 1985. Boltzmann machines can be seen as the stochastic,
generative counterpart of Hopfield nets. They are named after the
Boltzmann distribution in statistical mechanics. The units in Boltzmann
machines are divided into two groups: visible units and hidden units.
General Boltzmann machines allow connection between any units. However,
learning is impractical using general Boltzmann Machines because the
computational time is exponential to the size of the machine. A more
efficient architecture is called restricted Boltzmann machine where
connection is only allowed between hidden unit and visible unit, which
is described in the next section. Restricted Boltzmann machine A
restricted Boltzmann machine is an undirected graphical model with
stochastic visible variable and stochastic hidden variables. Each
visible variable is connected to each hidden variable. The energy
function of the model is defined as E ( v , h ; θ ) = − ∑ i = 1 D ∑ j =
1 F W i j v i h j − ∑ i = 1 D b i v i − ∑ j = 1 F a j h j
{\\displaystyle E(\\mathbf {v} ,\\mathbf {h} ;\\theta )=-\\sum
\_{i=1}\^{D}\\sum \_{j=1}\^{F}W\_{ij}v\_{i}h\_{j}-\\sum
\_{i=1}\^{D}b\_{i}v\_{i}-\\sum \_{j=1}\^{F}a\_{j}h\_{j}} where θ = { v ,
h ; θ } {\\displaystyle \\theta =\\{\\mathbf {v} ,\\mathbf {h} ;\\theta
\\}} are model parameters: W i j {\\displaystyle W\_{ij}} represents the
symmetric interaction term between visible unit i {\\displaystyle i} and
hidden unit j {\\displaystyle j} ; b i {\\displaystyle b\_{i}} and a j
{\\displaystyle a\_{j}} are bias terms. The joint distribution of the
system is defined as P ( v ; θ ) = 1 Z ( θ ) ∑ h e x p ( − E ( v , h ; θ
) ) {\\displaystyle P(\\mathbf {v} ;\\theta )={\\frac {1}{{\\mathcal
{Z}}(\\theta )}}\\sum \_{\\mathbf {h} }\\mathrm {exp} (-E(\\mathbf {v}
,\\mathbf {h} ;\\theta ))} where Z ( θ ) {\\displaystyle {\\mathcal
{Z}}(\\theta )} is a normalizing constant. The conditional distribution
over hidden h {\\displaystyle \\mathbf {h} } and v {\\displaystyle
\\mathbf {v} } can be derived as logistic function in terms of model
parameters. P ( h \| v ; θ ) = ∏ j = 1 F p ( h j \| v ) {\\displaystyle
P(\\mathbf {h} \|\\mathbf {v} ;\\theta )=\\prod
\_{j=1}\^{F}p(h\_{j}\|\\mathbf {v} )} , with p ( h j = 1 \| v ) = g ( ∑
i = 1 D W i j v i + a j ) {\\displaystyle p(h\_{j}=1\|\\mathbf {v}
)=g(\\sum \_{i=1}\^{D}W\_{ij}v\_{i}+a\_{j})} P ( v \| h ; θ ) = ∏ i = 1
D p ( v i \| h ) {\\displaystyle P(\\mathbf {v} \|\\mathbf {h} ;\\theta
)=\\prod \_{i=1}\^{D}p(v\_{i}\|\\mathbf {h} )} , with p ( v i = 1 \| h )
= g ( ∑ j = 1 F W i j h j + b i ) {\\displaystyle p(v\_{i}=1\|\\mathbf
{h} )=g(\\sum \_{j=1}\^{F}W\_{ij}h\_{j}+b\_{i})} where g ( x ) = 1 ( 1 +
e x p ( − x ) ) {\\displaystyle g(x)={\\frac {1}{(1+\\mathrm {exp}
(-x))}}} is the logistic function. The derivative of the log-likelihood
with respect to the model parameters can be decomposed as the difference
between the model\'s expectation and data-dependent expectation.
Gaussian-Bernoulli RBM Gaussian-Bernoulli RBMs are a variant of
restricted Boltzmann machine used for modeling real-valued vectors such
as pixel intensities. It is usually used to model the image data. The
energy of the system of the Gaussian-Bernoulli RBM is defined as E ( v ,
h ; θ ) = ∑ i = 1 D ( v i − b i ) 2 2 σ i 2 − ∑ i = 1 D ∑ j = 1 F v i σ
i W i j v i h j − ∑ i = 1 D b i v i − ∑ j = 1 F a j h j {\\displaystyle
E(\\mathbf {v} ,\\mathbf {h} ;\\theta )=\\sum \_{i=1}\^{D}{\\frac
{(v\_{i}-b\_{i})\^{2}}{2\\sigma \_{i}\^{2}}}-\\sum \_{i=1}\^{D}\\sum
\_{j=1}\^{F}{\\frac {v\_{i}}{\\sigma \_{i}}}W\_{ij}v\_{i}h\_{j}-\\sum
\_{i=1}\^{D}b\_{i}v\_{i}-\\sum \_{j=1}\^{F}a\_{j}h\_{j}} where θ = { a ,
b , w , σ } {\\displaystyle \\theta =\\{\\mathbf {a} ,\\mathbf {b}
,\\mathbf {w} ,\\mathbf {\\sigma } \\}} are the model parameters. The
joint distribution is defined the same as the one in restricted
Boltzmann machine. The conditional distributions now become P ( h \| v ;
θ ) = ∏ j = 1 F p ( h j \| v ) {\\displaystyle P(\\mathbf {h} \|\\mathbf
{v} ;\\theta )=\\prod \_{j=1}\^{F}p(h\_{j}\|\\mathbf {v} )} , with p ( h
j = 1 \| v ) = g ( ∑ i = 1 D W i j v i σ i + a j ) {\\displaystyle
p(h\_{j}=1\|\\mathbf {v} )=g(\\sum \_{i=1}\^{D}W\_{ij}{\\frac
{v\_{i}}{\\sigma \_{i}}}+a\_{j})} P ( v \| h ; θ ) = ∏ i = 1 D p ( v i
\| h ) {\\displaystyle P(\\mathbf {v} \|\\mathbf {h} ;\\theta )=\\prod
\_{i=1}\^{D}p(v\_{i}\|\\mathbf {h} )} , with p ( v i \| h ) ∼ N ( σ i ∑
j = 1 F W i j h j + b i , σ i 2 ) {\\displaystyle p(v\_{i}\|\\mathbf {h}
)\\sim {\\mathcal {N}}(\\sigma \_{i}\\sum
\_{j=1}\^{F}W\_{ij}h\_{j}+b\_{i},\\sigma \_{i}\^{2})} In
Gaussian-Bernoulli RBM, the visible unit conditioned on hidden units is
modeled as a Gaussian distribution. Replicated Softmax Model The
Replicated Softmax Model is also an variant of restricted Boltzmann
machine and commonly used to model word count vectors in a document. In
a typical text mining problem, let K {\\displaystyle K} be the
dictionary size, and M {\\displaystyle M} be the number of words in the
document. Let V {\\displaystyle \\mathbf {V} } be a M × K
{\\displaystyle M\\times K} binary matrix with v i k = 1 {\\displaystyle
v\_{ik}=1} only when the i t h {\\displaystyle i\^{th}} word in the
document is the k t h {\\displaystyle k\^{th}} word in the dictionary. v
\^ k {\\displaystyle {\\hat {v}}\_{k}} denotes the count for the k t h
{\\displaystyle k\^{th}} word in the dictionary. The energy of the state
{ V , h } {\\displaystyle \\{\\mathbf {V} ,\\mathbf {h} \\}} for a
document contains M {\\displaystyle M} words is defined as E ( V , h ) =
− ∑ j = 1 F ∑ k = 1 K W j k v \^ k h j − ∑ k = 1 K b k v \^ k − M ∑ j =
1 F a j h j {\\displaystyle E(\\mathbf {V} ,\\mathbf {h} )=-\\sum
\_{j=1}\^{F}\\sum \_{k=1}\^{K}W\_{jk}{\\hat {v}}\_{k}h\_{j}-\\sum
\_{k=1}\^{K}b\_{k}{\\hat {v}}\_{k}-M\\sum \_{j=1}\^{F}a\_{j}h\_{j}} The
conditional distributions are given by p ( h j = 1 \| V ) = g ( M a j +
∑ k = 1 K v \^ k W j k ) {\\displaystyle p(h\_{j}=1\|\\mathbf {V}
)=g(Ma\_{j}+\\sum \_{k=1}\^{K}{\\hat {v}}\_{k}W\_{jk})} p ( v i k = 1 \|
h ) = e x p ( b k + ∑ j = 1 F h j W j k ∑ q = 1 K e x p ( b q + ∑ j = 1
F h j W j q ) {\\displaystyle p(v\_{ik}=1\|\\mathbf {h} )={\\frac
{\\mathrm {exp} (b\_{k}+\\sum \_{j=1}\^{F}h\_{j}W\_{jk}}{\\sum
\_{q=1}\^{K}\\mathrm {exp} (b\_{q}+\\sum \_{j=1}\^{F}h\_{j}W\_{jq}}})}
Deep Boltzmann machines A deep Boltzmann machine has a sequence of
layers of hidden units.There are only connections between adjacent
hidden layers, as well as between visible units and hidden units in the
first hidden layer. The energy function of the system adds layer
interaction terms to the energy function of general restricted Boltzmann
machine and is defined by E ( v , h ; θ ) = − ∑ i = 1 D ∑ j = 1 F 1 W i
j ( 1 ) v i h j ( 1 ) − ∑ j = 1 F 1 ∑ l = 1 F 2 W j l ( 2 ) h j ( 1 ) h
l ( 2 ) − ∑ l = 1 F 2 ∑ p = 1 F 3 W l p ( 3 ) h l ( 2 ) h p ( 3 ) − ∑ i
= 1 D b i v i − ∑ j = 1 F 1 b j ( 1 ) h j ( 1 ) − ∑ l = 1 F 2 b l ( 2 )
h l ( 2 ) − ∑ p = 1 F 3 b p ( 3 ) h p ( 3 ) {\\displaystyle
{\\begin{aligned}E({\\mathbf {v} ,\\mathbf {h} ;\\theta })=&-\\sum
\_{i=1}\^{D}\\sum
\_{j=1}\^{F\_{1}}W\_{ij}\^{(1)}v\_{i}h\_{j}\^{(1)}-\\sum
\_{j=1}\^{F\_{1}}\\sum
\_{l=1}\^{F\_{2}}W\_{jl}\^{(2)}h\_{j}\^{(1)}h\_{l}\^{(2)}\\\\&-\\sum
\_{l=1}\^{F\_{2}}\\sum
\_{p=1}\^{F\_{3}}W\_{lp}\^{(3)}h\_{l}\^{(2)}h\_{p}\^{(3)}-\\sum
\_{i=1}\^{D}b\_{i}v\_{i}-\\sum
\_{j=1}\^{F\_{1}}b\_{j}\^{(1)}h\_{j}\^{(1)}-\\sum
\_{l=1}\^{F\_{2}}b\_{l}\^{(2)}h\_{l}\^{(2)}-\\sum
\_{p=1}\^{F\_{3}}b\_{p}\^{(3)}h\_{p}\^{(3)}\\end{aligned}}} The joint
distribution is P ( v ; θ ) = 1 Z ( θ ) ∑ h e x p ( − E ( v , h ( 1 ) ,
h ( 2 ) , h ( 3 ) ; θ ) ) {\\displaystyle P(\\mathbf {v} ;\\theta
)={\\frac {1}{{\\mathcal {Z}}(\\theta )}}\\sum \_{\\mathbf {h} }\\mathrm
{exp} (-E(\\mathbf {v} ,\\mathbf {h} \^{(1)},\\mathbf {h}
\^{(2)},\\mathbf {h} \^{(3)};\\theta ))} Multimodal deep Boltzmann
machines Multimodal deep Boltzmann machine uses an image-text bi-modal
DBM where the image pathway is modeled as Gaussian-Bernoulli DBM and
text pathway as Replicated Softmax DBM, and each DBM has two hidden
layers and one visible layer. The two DBMs join together at an
additional top hidden layer. The joint distribution over the multi-modal
inputs defined as P ( v m , v t ; θ ) = ∑ h ( 2 m ) , h ( 2 t ) , h ( 3
) P ( h ( 2 m ) , h ( 2 t ) , h ( 3 ) ) ( ∑ h ( 1 m ) P ( v m , h ( 1 m
) \| h ( 2 m ) ) ) ( ∑ h ( 1 t ) P ( v t , h ( 1 t ) \| h ( 2 t ) ) ) =
1 Z M ( θ ) ∑ h e x p ( ∑ k j W k j ( 1 t ) v k t h j ( 1 t ) + ∑ j l W
j l ( 2 t ) h j ( 1 t ) h l ( 2 t ) + ∑ k b k t v k t + M ∑ j b j ( 1 t
) h j ( 1 t ) + ∑ l b l ( 2 t ) h l ( 2 t ) − ∑ i ( v i m − b i m ) 2 2
σ 2 + ∑ i j v i m σ i W i j ( 1 m ) h j ( 1 m ) + ∑ j l W j l ( 2 m ) h
j ( 1 m ) h l ( 2 m ) + ∑ j b j ( 1 m ) h j ( 1 m ) + ∑ l b l ( 2 m ) h
l ( 2 m ) + ∑ l p W ( 3 t ) h l ( 2 t ) h p ( 3 ) + ∑ l p W ( 3 m ) h l
( 2 m ) h p ( 3 ) + ∑ p b p ( 3 ) h p ( 3 ) {\\displaystyle
{\\begin{aligned}P(\\mathbf {v} \^{m},\\mathbf {v} \^{t};\\theta
)&=\\sum \_{\\mathbf {h} \^{(2m)},\\mathbf {h} \^{(2t)},\\mathbf {h}
\^{(3)}}P(\\mathbf {h} \^{(2m)},\\mathbf {h} \^{(2t)},\\mathbf {h}
\^{(3)})(\\sum \_{\\mathbf {h} \^{(1m)}}P(\\mathbf {v} \_{m},\\mathbf
{h} \^{(1m)}\|\\mathbf {h} \^{(2m)}))(\\sum \_{\\mathbf {h}
\^{(1t)}}P(\\mathbf {v} \^{t},\\mathbf {h} \^{(1t)}\|\\mathbf {h}
\^{(2t)}))\\\\&={\\frac {1}{{\\mathcal {Z}}\_{M}(\\theta )}}\\sum
\_{\\mathbf {h} }\\mathrm {exp} (\\sum
\_{kj}W\_{kj}\^{(1t)}v\_{k}\^{t}h\_{j}\^{(1t)}\\\\&+\\sum
\_{jl}W\_{jl}\^{(2t)}h\_{j}\^{(1t)}h\_{l}\^{(2t)}+\\sum
\_{k}b\_{k}\^{t}v\_{k}\^{t}+M\\sum
\_{j}b\_{j}\^{(1t)}h\_{j}\^{(1t)}+\\sum
\_{l}b\_{l}\^{(2t)}h\_{l}\^{(2t)}\\\\&-\\sum \_{i}{\\frac
{(v\_{i}\^{m}-b\_{i}\^{m})\^{2}}{2\\sigma \^{2}}}+\\sum \_{ij}{\\frac
{v\_{i}\^{m}}{\\sigma \_{i}}}W\_{ij}\^{(1m)}h\_{j}\^{(1m)}\\\\&+\\sum
\_{jl}W\_{jl}\^{(2m)}h\_{j}\^{(1m)}h\_{l}\^{(2m)}+\\sum
\_{j}b\_{j}\^{(1m)}h\_{j}\^{(1m)}+\\sum
\_{l}b\_{l}\^{(2m)}h\_{l}{(2m)}\\\\&+\\sum
\_{lp}W\^{(3t)}h\_{l}\^{(2t)}h\_{p}\^{(3)}+\\sum
\_{lp}W\^{(3m)}h\_{l}\^{(2m)}h\_{p}\^{(3)}+\\sum
\_{p}b\_{p}\^{(3)}h\_{p}\^{(3)}\\end{aligned}}} The conditional
distributions over the visible and hidden units are p ( h j ( 1 m ) = 1
\| v m , h ( 2 m ) ) = g ( ∑ i = 1 D W i j ( 1 m ) v i m σ i + ∑ l = 1 F
2 m W j l ( 2 m ) h l ( 2 m ) + b j ( 1 m ) ) {\\displaystyle
p(h\_{j}\^{(1m)}=1\|\\mathbf {v} \^{m},\\mathbf {h} \^{(2m)})=g(\\sum
\_{i=1}\^{D}W\_{ij}\^{(1m)}{\\frac {v\_{i}\^{m}}{\\sigma \_{i}}}+\\sum
\_{l=1}\^{F\_{2}\^{m}}W\_{jl}\^{(2m)}h\_{l}\^{(2m)}+b\_{j}\^{(1m)})} p (
h l ( 2 m ) = 1 \| h ( 1 m ) , h ( 3 ) ) = g ( ∑ j = 1 F 1 m W j l ( 2 m
) h j ( 1 m ) + ∑ p = 1 F 3 W l p ( 3 m ) h p ( 3 ) + b l ( 2 m ) )
{\\displaystyle p(h\_{l}\^{(2m)}=1\|\\mathbf {h} \^{(1m)},\\mathbf {h}
\^{(3)})=g(\\sum
\_{j=1}\^{F\_{1}\^{m}}W\_{jl}\^{(2m)}h\_{j}\^{(1m)}+\\sum
\_{p=1}\^{F\_{3}}W\_{lp}\^{(3m)}h\_{p}\^{(3)}+b\_{l}\^{(2m)})} p ( h j (
1 t ) = 1 \| v t , h ( 2 t ) ) = g ( ∑ k = 1 K W k l ( 1 t ) v k ( t ) +
∑ l = 1 F 2 t W j l ( 2 t ) h l ( 2 t ) + M b j ( 1 t ) )
{\\displaystyle p(h\_{j}\^{(1t)}=1\|\\mathbf {v} \^{t},\\mathbf {h}
\^{(2t)})=g(\\sum \_{k=1}\^{K}W\_{kl}\^{(1t)}v\_{k}\^{(t)}+\\sum
\_{l=1}\^{F\_{2}\^{t}}W\_{jl}\^{(2t)}h\_{l}\^{(2t)}+Mb\_{j}\^{(1t)})} p
( h l ( 2 t ) = 1 \| h ( 1 t ) , h ( 3 ) ) = g ( ∑ j = 1 F 1 t W j l ( 2
t ) h j ( 1 t ) + ∑ p = 1 F 3 W l p ( 3 t ) h p ( 3 ) + b l ( 2 t ) )
{\\displaystyle p(h\_{l}\^{(2t)}=1\|\\mathbf {h} \^{(1t)},\\mathbf {h}
\^{(3)})=g(\\sum
\_{j=1}\^{F\_{1}\^{t}}W\_{jl}\^{(2t)}h\_{j}\^{(1t)}+\\sum
\_{p=1}\^{F\_{3}}W\_{lp}\^{(3t)}h\_{p}\^{(3)}+b\_{l}\^{(2t)})} p ( h p 3
) = 1 \| h ( 2 ) ) = g ( ∑ l = 1 F 2 m W l p ( 3 m ) h l ( 2 m ) + ∑ l =
1 F 2 t W l p ( 3 t ) h l ( 2 t ) + b p ( 3 ) ) {\\displaystyle
p(h\_{p}\^{3)}=1\|\\mathbf {h} \^{(2)})=g(\\sum
\_{l=1}\^{F\_{2}\^{m}}W\_{lp}\^{(3m)}h\_{l}\^{(2m)}+\\sum
\_{l=1}\^{F\_{2}\^{t}}W\_{lp}\^{(3t)}h\_{l}\^{(2t)}+b\_{p}\^{(3)})} p (
v i k t = 1 \| h ( 1 t ) ) = e x p ( ∑ j = 1 F 1 t h j ( 1 t ) W j k ( 1
t ) + b k t ) ∑ q = 1 K e x p ( ∑ j = 1 F 1 t h j ( 1 t ) W j q ( 1 t
) + b k t ) {\\displaystyle p(v\_{ik}\^{t}=1\|\\mathbf {h}
\^{(1t)})={\\frac {\\mathrm {exp} (\\sum
\_{j=1}\^{F\_{1}\^{t}}h\_{j}\^{(1t)}W\_{jk}\^{(1t)}+b\_{k}\^{t})}{\\sum
\_{q=1}\^{K}\\mathrm {exp} (\\sum
\_{j=1}\^{F\_{1}\^{t}}h\_{j}\^{(1t)}W\_{jq}\^{(1t)}+b\_{k}\^{t})}}} p (
v i m \| h ( 1 m ) ) ∼ N ( σ i ∑ j = 1 F 1 m W i j ( 1 m ) h j ( 1 m ) +
b i m , σ i 2 ) {\\displaystyle p(v\_{i}\^{m}\|\\mathbf {h}
\^{(1m)})\\sim {\\mathcal {N}}(\\sigma \_{i}\\sum
\_{j=1}\^{F\_{1}\^{m}}W\_{ij}\^{(1m)}h\_{j}\^{(1m)}+b\_{i}\^{m},\\sigma
\_{i}\^{2})} Inference and learning Exact maximum likelihood learning in
this model is intractable, but approximate learning of DBMs can be
carried out by using a variational approach, where mean-field inference
is used to estimate data-dependent expectations and an MCMC based
stochastic approximation procedure is used to approximate the model's
expected sufficient statistics. Application Multimodal deep Boltzmann
machines are successfully used in classification and missing data
retrieval. The classification accuracy of multimodal deep Boltzmann
machine outperforms support vector machines, latent Dirichlet allocation
and deep belief network, when models are tested on data with both
image-text modalities or with single modality. Multimodal deep Boltzmann
machine is also able to predict missing modalities given the observed
ones with reasonably good precision. Self Supervised Learning brings a
more interesting and powerful model for multimodality. OpenAI developed
CLIP and DALL-E models that revolutionized multimodality. Multimodal
deep learning is used for cancer screening -- at least one system under
development integrates such different types of data. See also Hopfield
network Markov random field Markov chain Monte Carlo == References ==
