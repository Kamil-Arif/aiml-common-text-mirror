A transformer is a deep learning model. It is distinguished by its
adoption of self-attention, differentially weighting the significance of
each part of the input (which includes the recursive output) data. It is
used primarily in the fields of natural language processing (NLP) and
computer vision (CV).Like recurrent neural networks (RNNs), transformers
are designed to process sequential input data, such as natural language,
with applications towards tasks such as translation and text
summarization. However, unlike RNNs, transformers process the entire
input all at once. The attention mechanism provides context for any
position in the input sequence. For example, if the input data is a
natural language sentence, the transformer does not have to process one
word at a time. This allows for more parallelization than RNNs and
therefore reduces training times. Transformers were introduced in 2017
by a team at Google Brain and are increasingly becoming the model of
choice for NLP problems, replacing RNN models such as long short-term
memory (LSTM). Compared to RNN models, transformers are more amenable to
parallelization, allowing training on larger datasets. This led to the
development of pretrained systems such as BERT (Bidirectional Encoder
Representations from Transformers) and GPT (Generative Pre-trained
Transformer), which were trained with large language datasets, such as
the Wikipedia Corpus and Common Crawl, and can be fine-tuned for
specific tasks. Background Before transformers, most state-of-the-art
NLP systems relied on gated RNNs, such as LSTMs and gated recurrent
units (GRUs), with added attention mechanisms. Transformers also make
use of attention mechanisms but, unlike RNNs, do not have a recurrent
structure. This means that provided with enough training data, attention
mechanisms alone can match the performance of RNNs with attention.The
terms \"query\", \"key\", \"value\" are borrowed from key--value
databases. Previous work In 1992, Jürgen Schmidhuber published the fast
weight controller as an alternative to RNNs that can learn \"internal
spotlights of attention,\" and experimented with using it to learn
variable binding.In a fast weight controller, a feedforward neural
network (\"slow\") learns by gradient descent to control the weights of
another neural network (\"fast\") through outer products of
self-generated activation patterns called \"FROM\" and \"TO\" which
corresponds to \"key\" and \"value\" in the attention mechanism. This
fast weight is applied to queries. The attention mechanism may be
obtained by interposing a softmax operator and three linear operators
(one for each of query, key, and value). Sequential processing Gated
RNNs process tokens sequentially, maintaining a state vector that
contains a representation of the data seen prior to the current token.
To process the n {\\textstyle n} th token, the model combines the state
representing the sentence up to token n − 1 {\\textstyle n-1} with the
information of the new token to create a new state, representing the
sentence up to token n {\\textstyle n} . Theoretically, the information
from one token can propagate arbitrarily far down the sequence, if at
every point the state continues to encode contextual information about
the token. In practice this mechanism is flawed: the vanishing gradient
problem leaves the model\'s state at the end of a long sentence without
precise, extractable information about preceding tokens. The dependency
of token computations on the results of previous token computations also
makes it hard to parallelize computation on modern deep-learning
hardware. This can make the training of RNNs inefficient. Self-attention
These problems were addressed by attention mechanisms. Attention
mechanisms let a model draw from the state at any preceding point along
the sequence. The attention layer can access all previous states and
weigh them according to a learned measure of relevance, providing
relevant information about far-away tokens. A clear example of the value
of attention is in language translation, where context is essential to
assign the meaning of a word in a sentence. In an English-to-French
translation system, the first word of the French output most probably
depends heavily on the first few words of the English input. However, in
a classic LSTM model, in order to produce the first word of the French
output, the model is given only the state vector after processing the
last English word. Theoretically, this vector can encode information
about the whole English sentence, giving the model all the necessary
knowledge. In practice, this information is often poorly preserved by
the LSTM. An attention mechanism can be added to address this problem:
the decoder is given access to the state vectors of every English input
word, not just the last, and can learn attention weights that dictate
how much to attend to each English input state vector. When added to
RNNs, attention mechanisms increase performance. In 2016, a new type of
highly parallelizable decomposable attention was successfully combined
with a feedforward network. This indicated that attention mechanisms
were powerful in themselves and that sequential recurrent processing of
data was not necessary to achieve the quality gains of RNNs with
attention. Soon Jakob Uszkoreit from Google Research also proposed
replacing RNNs with self-attention and started the effort to evaluate
that idea. Transformers use an attention mechanism without an RNN,
processing all tokens simultaneously and calculating attention weights
between them in successive layers. Since the attention mechanism only
uses information about other tokens from lower layers, it can be
computed for all tokens in parallel, which leads to improved training
speed. Architecture Input The input text is parsed into tokens by a byte
pair encoding tokenizer, and each token is converted via a word
embedding into a vector. Then, positional information of the token is
added to the word embedding. Encoder/decoder architecture Like earlier
seq2seq models, the original Transformer model used an encoder/decoder
architecture. The encoder consists of encoding layers that process the
input iteratively one layer after another, while the decoder consists of
decoding layers that do the same thing to the encoder\'s output. The
function of each encoder layer is to generate encodings that contain
information about which parts of the inputs are relevant to each other.
It passes its encodings to the next encoder layer as inputs. Each
decoder layer does the opposite, taking all the encodings and using
their incorporated contextual information to generate an output
sequence. To achieve this, each encoder and decoder layer makes use of
an attention mechanism. For each part of the input, attention weighs the
relevance of every other part and draws from them to produce the output.
Each decoder layer has an additional attention mechanism that draws
information from the outputs of previous decoders, before the decoder
layer draws information from the encodings. Both the encoder and decoder
layers have a feed-forward neural network for additional processing of
the outputs and contain residual connections and layer normalization
steps. Scaled dot-product attention The transformer building blocks are
scaled dot-product attention units. When a sentence is passed into a
transformer model, attention weights are calculated between every token
simultaneously. The attention unit produces embeddings for every token
in context that contain information about the token itself along with a
weighted combination of other relevant tokens each weighted by its
attention weight. For each attention unit, the transformer model learns
three weight matrices; the query weights W Q {\\displaystyle W\_{Q}} ,
the key weights W K {\\displaystyle W\_{K}} , and the value weights W V
{\\displaystyle W\_{V}} . For each token i {\\displaystyle i} , the
input word embedding x i {\\displaystyle x\_{i}} is multiplied with each
of the three weight matrices to produce a query vector q i = x i W Q
{\\displaystyle q\_{i}=x\_{i}W\_{Q}} , a key vector k i = x i W K
{\\displaystyle k\_{i}=x\_{i}W\_{K}} , and a value vector v i = x i W V
{\\displaystyle v\_{i}=x\_{i}W\_{V}} . Attention weights are calculated
using the query and key vectors: the attention weight a i j
{\\displaystyle a\_{ij}} from token i {\\displaystyle i} to token j
{\\displaystyle j} is the dot product between q i {\\displaystyle
q\_{i}} and k j {\\displaystyle k\_{j}} . The attention weights are
divided by the square root of the dimension of the key vectors, d k
{\\displaystyle {\\sqrt {d\_{k}}}} , which stabilizes gradients during
training, and passed through a softmax which normalizes the weights. The
fact that W Q {\\displaystyle W\_{Q}} and W K {\\displaystyle W\_{K}}
are different matrices allows attention to be non-symmetric: if token i
{\\displaystyle i} attends to token j {\\displaystyle j} (i.e. q i ⋅ k j
{\\displaystyle q\_{i}\\cdot k\_{j}} is large), this does not
necessarily mean that token j {\\displaystyle j} will attend to token i
{\\displaystyle i} (i.e. q j ⋅ k i {\\displaystyle q\_{j}\\cdot k\_{i}}
could be small). The output of the attention unit for token i
{\\displaystyle i} is the weighted sum of the value vectors of all
tokens, weighted by a i j {\\displaystyle a\_{ij}} , the attention from
token i {\\displaystyle i} to each token. The attention calculation for
all tokens can be expressed as one large matrix calculation using the
softmax function, which is useful for training due to computational
matrix operation optimizations that quickly compute matrix operations.
The matrices Q {\\displaystyle Q} , K {\\displaystyle K} and V
{\\displaystyle V} are defined as the matrices where the i
{\\displaystyle i} th rows are vectors q i {\\displaystyle q\_{i}} , k i
{\\displaystyle k\_{i}} , and v i {\\displaystyle v\_{i}} respectively.
Then we can represent the attention as Attention ( Q , K , V ) = softmax
( Q K T d k ) V {\\displaystyle
{\\begin{aligned}{\\text{Attention}}(Q,K,V)={\\text{softmax}}\\left({\\frac
{QK\^{\\mathrm {T} }}{\\sqrt {d\_{k}}}}\\right)V\\end{aligned}}} where
softmax is taken over the horizontal axis. Multi-head attention One set
of ( W Q , W K , W V ) {\\displaystyle
\\left(W\_{Q},W\_{K},W\_{V}\\right)} matrices is called an attention
head, and each layer in a transformer model has multiple attention
heads. While each attention head attends to the tokens that are relevant
to each token, with multiple attention heads the model can do this for
different definitions of \"relevance\". In addition, the influence field
representing relevance can become progressively dilated in successive
layers. Many transformer attention heads encode relevance relations that
are meaningful to humans. For example, some attention heads can attend
mostly to the next word, while others mainly attend from verbs to their
direct objects. The computations for each attention head can be
performed in parallel, which allows for fast processing. The outputs for
the attention layer are concatenated to pass into the feed-forward
neural network layers. Concretely, let the multiple attention heads be
indexed by i {\\displaystyle i} , then we have where the matrices W i Q
, W i K , W i V {\\displaystyle W\_{i}\^{Q},W\_{i}\^{K},W\_{i}\^{V}} are
\"projection matrices\" owned by individual attention head i
{\\displaystyle i} , and W O {\\displaystyle W\^{O}} is a final
projection matrix owned by the whole multi-headed attention head. Masked
attention It may be necessary to cut out attention links between some
word-pairs. For example, the decoder for token position t
{\\displaystyle t} should not have access to token position t + 1
{\\displaystyle t+1} . This may be accomplished before the softmax stage
by adding a mask matrix M {\\displaystyle M} that is negative infinity
at entries where the attention link must be cut, and zero at other
places. Encoder Each encoder consists of two major components: a
self-attention mechanism and a feed-forward neural network. The
self-attention mechanism accepts input encodings from the previous
encoder and weights their relevance to each other to generate output
encodings. The feed-forward neural network further processes each output
encoding individually. These output encodings are then passed to the
next encoder as its input, as well as to the decoders. The first encoder
takes positional information and embeddings of the input sequence as its
input, rather than encodings. The positional information is necessary
for the transformer to make use of the order of the sequence, because no
other part of the transformer makes use of this.The encoder is
bidirectional. Attention can be placed on tokens before and after the
current token. Tokens are used instead of words to account for polysemy.
Positional encoding A positional encoding is a fixed-size vector
representation that encapsulates the relative positions of tokens within
a target sequence: it provides the transformer model with information
about where the words are in the input sequence. The positional encoding
is defined as a function of type f : R → R d ; d ∈ Z , d \> 0
{\\displaystyle f:\\mathbb {R} \\to \\mathbb {R} \^{d};d\\in \\mathbb
{Z} ,d\>0} , where d {\\displaystyle d} is a positive even integer. The
full positional encoding - as defined in the original paper - is given
by the equation:where θ = t r k , r = N 2 / d {\\displaystyle \\theta
={\\frac {t}{r\^{k}}},r=N\^{2/d}} . Here, N {\\displaystyle N} is a free
parameter that should be significantly larger than the biggest k
{\\displaystyle k} that would be input into the positional encoding
function. In the original paper, the authors chose N = 10000
{\\displaystyle N=10000} . The function is in a simpler form when
written as a complex function of type f : R → C d / 2 {\\displaystyle
f:\\mathbb {R} \\to \\mathbb {C} \^{d/2}} where r = N 2 / d
{\\displaystyle r=N\^{2/d}} . The main reason the authors chose this as
the positional encoding function is that it allows one to perform shifts
as linear transformations:where Δ t ∈ R {\\displaystyle \\Delta t\\in
\\mathbb {R} } is the distance one wishes to shift. This allows the
transformer to take any encoded position, and find the encoding of the
position n-steps-ahead or n-steps-behind, by a matrix multiplication. By
taking a linear sum, any convolution can also be implemented as linear
transformations:for any constants c j {\\displaystyle c\_{j}} . This
allows the transformer to take any encoded position and find a linear
sum of the encoded locations of its neighbors. This sum of encoded
positions, when fed into the attention mechanism, would create attention
weights on its neighbors, much like what happens in a convolutional
neural network language model. In the author\'s words, \"we hypothesized
it would allow the model to easily learn to attend by relative
position\". In typical implementations, all operations are done over the
real numbers, not the complex numbers, but since complex multiplication
can be implemented as real 2-by-2 matrix multiplication, this is a mere
notational difference. Other positional encoding schemes exist. Decoder
Each decoder consists of three major components: a self-attention
mechanism, an attention mechanism over the encodings, and a feed-forward
neural network. The decoder functions in a similar fashion to the
encoder, but an additional attention mechanism is inserted which instead
draws relevant information from the encodings generated by the encoders.
This mechanism can also be called the encoder-decoder attention.Like the
first encoder, the first decoder takes positional information and
embeddings of the output sequence as its input, rather than encodings.
The transformer must not use the current or future output to predict an
output, so the output sequence must be partially masked to prevent this
reverse information flow. This allows for autoregressive text
generation. For all attention heads, attention can\'t be placed on
following tokens. The last decoder is followed by a final linear
transformation and softmax layer, to produce the output probabilities
over the vocabulary. All members of the GPT series have a decoder-only
architecture. Subsequent work Sub-quadratic transformers Training
transformer-based architectures can be expensive, especially for long
inputs. Alternative architectures include the Reformer (which reduces
the computational load from O ( N 2 ) {\\displaystyle O(N\^{2})} to O (
N ln ⁡ N ) {\\displaystyle O(N\\ln N)} ), or models like ETC/BigBird
(which can reduce it to O ( N ) {\\displaystyle O(N)} ) where N
{\\displaystyle N} is the length of the sequence. This is done using
locality-sensitive hashing and reversible layers.Ordinary transformers
require a memory size that is quadratic in the size of the context
window. Attention Free Transformers reduce this to a linear dependence
while still retaining the advantages of a transformer by linking the key
to the value. Long Range Arena (2020) is a standard benchmark for
comparing the behavior of transformer architectures over long inputs.
Random Feature Attention (2021) uses Fourier random features:where w 1 ,
. . . , w D {\\displaystyle w\_{1},\...,w\_{D}} are independent samples
from the normal distribution N ( 0 , σ 2 I ) {\\displaystyle N(0,\\sigma
\^{2}I)} . This choice of parameters satisfy E \[ ⟨ φ ( x ) , φ ( y ) ⟩
\] = e ‖ x − y ‖ 2 2 σ 2 {\\displaystyle \\mathbb {E} \[\\langle
\\varphi (x),\\varphi (y)\\rangle \]=e\^{\\frac
{\\\|x-y\\\|\^{2}}{2\\sigma \^{2}}}} , or Consequently, the one-headed
attention, with one query, can be written as where σ = d K 1 / 4
{\\displaystyle \\sigma =d\_{K}\^{1/4}} . Similarly for multiple
queries, and for multiheaded attention. This approximation can be
computed in linear time, as we can compute the matrix φ ( k i ) v i T
{\\displaystyle \\varphi (k\_{i})v\_{i}\^{T}} first, then multiply it
with the query. In essence, we have managed to obtain a more precise
version of Performer (2022) uses the same Random Feature Attention, but
w 1 , . . . , w D {\\displaystyle w\_{1},\...,w\_{D}} are first
independently sampled from the normal distribution N ( 0 , σ 2 I )
{\\displaystyle N(0,\\sigma \^{2}I)} , then they are Gram-Schmidt
processed. Other modalities Perceivers by Andrew Jaegle et al. (2021)
can learn from large amounts of heterogeneous data. Vision transformers
by Jean-Baptiste Cordonnier et al. breaks down input images as a series
of patches which, once transformed into vectors, are treated like words
in a standard transformer. Training Methods for stabilizing training The
plain Transformer architecture has difficulty converging. In the
original paper the authors recommended using learning rate warmup. That
is, the learning rate should linearly scale up from 0 to maximal value
for the first part of the training (usually recommended to be 2% of the
total number of training steps), before decaying again. A 2020 paper
found that using layer normalization before (instead of after)
multiheaded attention and feedforward layers stabilizes training, not
requiring learning rate warmup. Pretrain-finetune Transformers typically
undergo self-supervised learning involving unsupervised pretraining
followed by supervised fine-tuning. Pretraining is typically done on a
larger dataset than fine-tuning, due to the limited availability of
labeled training data. Tasks for pretraining and fine-tuning commonly
include: language modeling next-sentence prediction question answering
reading comprehension sentiment analysis paraphrasing Applications The
transformer has had great success in natural language processing (NLP),
for example the tasks of machine translation and time series prediction.
Many pretrained models such as GPT-2, GPT-3, GPT-4, BERT, XLNet, RoBERTa
and ChatGPT demonstrate the ability of transformers to perform a wide
variety of such NLP-related tasks, and have the potential to find
real-world applications. These may include: machine translation document
summarization document generation named entity recognition (NER)
biological sequence analysis video understanding.In addition to the NLP
applications, it has also been successful in other fields, such as
Computer vision, or the protein folding applications (such as
AlphaFold). Implementations The transformer model has been implemented
in standard deep learning frameworks such as TensorFlow and PyTorch.
Transformers is a library produced by Hugging Face that supplies
transformer-based architectures and pretrained models. See also
Perceiver -- Machine learning algorithm for non-textual data BERT
(language model) -- Masked neural language model developed by Google
GPT-3 -- 2020 text-generating language model GPT-4 -- 2023
text-generating language model ChatGPT -- AI chatbot developed by OpenAI
Wu Dao -- Chinese multimodal artificial intelligence program Vision
transformer -- Machine learning algorithm for vision processing BLOOM
(language model) -- Open-access multilingual language model References
== Further reading ==
