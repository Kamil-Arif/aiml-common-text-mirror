A language model is a probability distribution over sequences of words.
Given any sequence of words of length m, a language model assigns a
probability P ( w 1 , ... , w m ) {\\displaystyle P(w\_{1},\\ldots
,w\_{m})} to the whole sequence. Language models generate probabilities
by training on text corpora in one or many languages. Given that
languages can be used to express an infinite variety of valid sentences
(the property of digital infinity), language modeling faces the problem
of assigning non-zero probabilities to linguistically valid sequences
that may never be encountered in the training data. Several modelling
approaches have been designed to surmount this problem, such as applying
the Markov assumption or using neural architectures such as recurrent
neural networks or transformers. Language models are useful for a
variety of problems in computational linguistics; from initial
applications in speech recognition to ensure nonsensical (i.e.
low-probability) word sequences are not predicted, to wider use in
machine translation (e.g. scoring candidate translations), natural
language generation (generating more human-like text), part-of-speech
tagging, parsing, optical character recognition, handwriting
recognition, grammar induction, information retrieval, and other
applications. Language models are used in information retrieval in the
query likelihood model. There, a separate language model is associated
with each document in a collection. Documents are ranked based on the
probability of the query Q {\\displaystyle Q} in the document\'s
language model M d {\\displaystyle M\_{d}} : P ( Q ∣ M d )
{\\displaystyle P(Q\\mid M\_{d})} . Commonly, the unigram language model
is used for this purpose. Since 2018, large language models (LLMs)
consisting of deep neural networks with billions of trainable
parameters, trained on massive datasets of unlabelled text, have
demonstrated impressive results on a wide variety of natural language
processing tasks. This development has led to a shift in research focus
toward the use of general-purpose LLMs. Model types n-gram Exponential
Maximum entropy language models encode the relationship between a word
and the n-gram history using feature functions. The equation is where Z
( w 1 , ... , w m − 1 ) {\\displaystyle Z(w\_{1},\\ldots ,w\_{m-1})} is
the partition function, a {\\displaystyle a} is the parameter vector,
and f ( w 1 , ... , w m ) {\\displaystyle f(w\_{1},\\ldots ,w\_{m})} is
the feature function. In the simplest case, the feature function is just
an indicator of the presence of a certain n-gram. It is helpful to use a
prior on a {\\displaystyle a} or some form of regularization. The
log-bilinear model is another example of an exponential language model.
Neural network Neural language models (or continuous space language
models) use continuous representations or embeddings of words to make
their predictions. These models make use of neural networks. Continuous
space embeddings help to alleviate the curse of dimensionality in
language modeling: as language models are trained on larger and larger
texts, the number of unique words (the vocabulary) increases. The number
of possible sequences of words increases exponentially with the size of
the vocabulary, causing a data sparsity problem because of the
exponentially many sequences. Thus, statistics are needed to properly
estimate probabilities. Neural networks avoid this problem by
representing words in a distributed way, as non-linear combinations of
weights in a neural net. An alternate description is that a neural net
approximates the language function. The neural net architecture might be
feed-forward or recurrent, and while the former is simpler the latter is
more common.Typically, neural net language models are constructed and
trained as probabilistic classifiers that learn to predict a probability
distribution That is, the network is trained to predict a probability
distribution over the vocabulary, given some linguistic context. This is
done using standard neural net training algorithms such as stochastic
gradient descent with backpropagation. The context might be a fixed-size
window of previous words, so that the network predicts from a feature
vector representing the previous k words. Another option is to use
\"future\" words as well as \"past\" words as features, so that the
estimated probability is This is called a bag-of-words model. When the
feature vectors for the words in the context are combined by a
continuous operation, this model is referred to as the continuous
bag-of-words architecture (CBOW).A third option that trains slower than
the CBOW but performs slightly better is to invert the previous problem
and make a neural network learn the context, given a word. More
formally, given a sequence of training words w 1 , w 2 , w 3 , ... , w T
{\\displaystyle w\_{1},w\_{2},w\_{3},\\dots ,w\_{T}} , one maximizes the
average log-probability where k, the size of the training context, can
be a function of the center word w t {\\displaystyle w\_{t}} . This is
called a skip-gram language model. Bag-of-words and skip-gram models are
the basis of the word2vec program.Instead of using neural net language
models to produce actual probabilities, it is common to instead use the
distributed representation encoded in the networks\' \"hidden\" layers
as representations of words; each word is then mapped onto an
n-dimensional real vector called the word embedding, where n is the size
of the layer just before the output layer. The representations in
skip-gram models have the distinct characteristic that they model
semantic relations between words as linear combinations, capturing a
form of compositionality. For example, in some such models, if v is the
function that maps a word w to its n-d vector representation, then where
≈ is made precise by stipulating that its right-hand side must be the
nearest neighbor of the value of the left-hand side. Other A positional
language model assesses the probability of given words occurring close
to one another in a text, not necessarily immediately adjacent.
Similarly, bag-of-concepts models leverage the semantics associated with
multi-word expressions such as buy_christmas_present, even when they are
used in information-rich sentences like \"today I bought a lot of very
nice Christmas presents\". Despite the limited successes in using neural
networks, authors acknowledge the need for other techniques when
modelling sign languages. Evaluation and benchmarks Evaluation of the
quality of language models is mostly done by comparison to human created
sample benchmarks created from typical language-oriented tasks. Other,
less established, quality tests examine the intrinsic character of a
language model or compare two such models. Since language models are
typically intended to be dynamic and to learn from data it sees, some
proposed models investigate the rate of learning, e.g. through
inspection of learning curves. Various data sets have been developed to
use to evaluate language processing systems. These include: Corpus of
Linguistic Acceptability GLUE benchmark Microsoft Research Paraphrase
Corpus Multi-Genre Natural Language Inference Question Natural Language
Inference Quora Question Pairs Recognizing Textual Entailment Semantic
Textual Similarity Benchmark SQuAD question answering Test Stanford
Sentiment Treebank Winograd NLI BoolQ, PIQA, SIQA, HellaSwag,
WinoGrande, ARC, OpenBookQA, NaturalQuestions, TriviaQA, RACE, MMLU
(Measuring Massive Multitask Language Understanding), BIG-bench hard,
GSM8k, RealToxicityPrompts, WinoGender, CrowS-Pairs. (LLaMa Benchmark)
Criticism Although contemporary language models, such as GPTs, can be
shown to match human performance on some tasks, it is not clear they are
plausible cognitive models. For instance, recurrent neural networks have
been shown to learn patterns humans do not learn and fail to learn
patterns that humans do learn. See also Notes References == Further
reading ==
