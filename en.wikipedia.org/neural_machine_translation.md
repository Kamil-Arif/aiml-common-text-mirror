Neural machine translation (NMT) is an approach to machine translation
that uses an artificial neural network to predict the likelihood of a
sequence of words, typically modeling entire sentences in a single
integrated model. Properties They require only a fraction of the memory
needed by traditional statistical machine translation (SMT) models.
Furthermore, unlike conventional translation systems, all parts of the
neural translation model are trained jointly (end-to-end) to maximize
the translation performance. History Deep learning applications appeared
first in speech recognition in the 1990s. The first scientific paper on
using neural networks in machine translation appeared in 2014. This year
Bahdanau et al. and Sutskever et al.proposed end-to-end neural network
translation models and formally used the term \"neural machine
translation\". First large-scale NMT system was launched by Baidu in
2015. Next year Google launched an NMT system too, followed by others.
It was followed by a lot of advances in the following few years.
(Large-vocabulary NMT, application to Image captioning, Subword-NMT,
Multilingual NMT, Multi-Source NMT, Character-dec NMT, Zero-Resource
NMT, Google, Fully Character-NMT, Zero-Shot NMT in 2017) In 2015 there
was the first appearance of a NMT system in a public machine translation
competition (OpenMT\'15). WMT\'15 also for the first time had a NMT
contender; the following year it already had 90% of NMT systems among
its winners.Since 2017, neural machine translation has been used by the
European Patent Office to make information from the global patent system
instantly accessible. The system, developed in collaboration with
Google, is paired with 31 languages, and as of 2018, the system has
translated over nine million documents. Workings NMT departs from
phrase-based statistical approaches that use separately engineered
subcomponents. Neural machine translation (NMT) is not a drastic step
beyond what has been traditionally done in statistical machine
translation (SMT). Its main departure is the use of vector
representations (\"embeddings\", \"continuous space representations\")
for words and internal states. The structure of the models is simpler
than phrase-based models. There is no separate language model,
translation model, and reordering model, but just a single sequence
model that predicts one word at a time. However, this sequence
prediction is conditioned on the entire source sentence and the entire
already produced target sequence. NMT models use deep learning and
representation learning. The word sequence modeling was at first
typically done using a recurrent neural network (RNN). A bidirectional
recurrent neural network, known as an encoder, is used by the neural
network to encode a source sentence for a second RNN, known as a
decoder, that is used to predict words in the target language. Recurrent
neural networks face difficulties in encoding long inputs into a single
vector. This can be compensated by an attention mechanism which allows
the decoder to focus on different parts of the input while generating
each word of the output. There are further Coverage Models addressing
the issues in such attention mechanisms, such as ignoring of past
alignment information leading to over-translation and
under-translation.Convolutional Neural Networks (Convnets) are in
principle somewhat better for long continuous sequences, but were
initially not used due to several weaknesses. These were successfully
compensated for in 2017 by using \"attention mechanisms\".The
Transformer an attention-based model, remains the dominant architecture
for several language pairs. The self-attention layers of the Transformer
model learn the dependencies between words in a sequence by examining
links between all the words in the paired sequences and by directly
modeling those relationships. It\'s a simpler approach than the gating
mechanism that RNNs employ. And its simplicity has enabled researchers
to develop high-quality translation models with the Transformer model,
even in low-resource settings. Remarks == References ==
