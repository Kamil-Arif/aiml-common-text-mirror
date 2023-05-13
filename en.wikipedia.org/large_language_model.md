A large language model (LLM) is a language model consisting of a neural
network with many parameters (typically billions of weights or more),
trained on large quantities of unlabeled text using self-supervised
learning or semi-supervised learning. LLMs emerged around 2018 and
perform well at a wide variety of tasks. This has shifted the focus of
natural language processing research away from the previous paradigm of
training specialized supervised models for specific tasks.Though the
term large language model has no formal definition, it often refers to
deep learning models having a parameter count on the order of billions
or more. LLMs are general purpose models which excel at a wide range of
tasks, as opposed to being trained for one specific task (such as
sentiment analysis, named entity recognition, or mathematical
reasoning). The skill with which they accomplish tasks, and the range of
tasks at which they are capable, seems to be a function of the amount of
resources (data, parameter-size, computing power) devoted to them, in a
way that is not dependent on additional breakthroughs in design.Though
trained on simple tasks along the lines of predicting the next word in a
sentence, neural language models with sufficient training and parameter
counts are found to capture much of the syntax and semantics of human
language. In addition, large language models demonstrate considerable
general knowledge about the world, and are able to \"memorize\" a great
quantity of facts during training. Properties Pretraining datasets LLMs
are pre-trained on large textual datasets. Some commonly used textual
datasets are Common Crawl, The Pile, MassiveText, Wikipedia, and GitHub.
The datasets run up to 10 trillion words in size. The stock of
high-quality language data is within 4.6-17 trillion words, which is
within an order of magnitude for the largest textual datasets. Scaling
laws In general, a LLM can be characterized by 4 parameters: size of the
model, size of the training dataset, cost of training, performance after
training. Each of these four variables can be precisely defined into a
real number, and they are empirically found to be related by simple
statistical laws, called \"scaling laws\". One particular scaling law
(\"Chinchilla scaling\") for LLM autoregressively trained for one epoch,
with a log-log learning rate schedule, states that:where the variables
are C {\\displaystyle C} is the cost of training the model, in FLOPs. N
{\\displaystyle N} is the number of parameters in the model. D
{\\displaystyle D} is the number of tokens in the training set. L
{\\displaystyle L} is the average negative log-likelihood loss per token
(nats/token), achieved by the trained LLM on the test dataset.and the
statistical parameters are C 0 = 6 {\\displaystyle C\_{0}=6} , meaning
that it costs 6 FLOPs per parameter to train on one token. Note that
training cost is much higher than inference cost, where it costs 1 to 2
FLOPs per parameter to infer on one token. α = 0.34 , β = 0.28 , A =
406.4 , B = 410.7 , L 0 = 1.69 {\\displaystyle \\alpha =0.34,\\beta
=0.28,A=406.4,B=410.7,L\_{0}=1.69} . Emergent abilities While it is
generally the case that performance of large models on various tasks can
be extrapolated based on the performance of similar smaller models,
sometimes \"breaks\" in downstream scaling laws occur such that larger
models suddenly acquire substantial abilities at a different rate than
in smaller models. These are often referred to as \"emergent
abilities\", and have been the subject of substantial study. Researchers
note that such abilities often \"cannot be predicted simply by
extrapolating the performance of smaller models\". These abilities are
discovered rather than programmed-in or designed, in some cases only
after the LLM has been publicly deployed. Hundreds of emergent abilities
have been described. Examples include multi-step arithmetic, taking
college-level exams, identifying the intended meaning of a word,
chain-of-thought prompting, decoding the International Phonetic
Alphabet, unscrambling a word's letters, identifying offensive content
in paragraphs of Hinglish (a combination of Hindi and English), and
generating a similar English equivalent of Kiswahili proverbs.
Hallucination Generative LLMs have been observed to confidently assert
claims of fact which do not seem to be justified by their training data,
a phenomenon which has been termed \"hallucination\". Architecture Large
language models have most commonly used the transformer architecture,
which, since 2018, has become the standard deep learning technique for
sequential data (previously, recurrent architectures such as the LSTM
were most common). Tokenization LLMs are mathematical functions whose
input and output are lists of numbers. Consequently, words must be
converted to numbers. In general, a LLM uses a separate tokenizer. A
tokenizer maps between texts and lists of integers. The tokenizer is
generally adapted to the entire training dataset first, then frozen,
before the LLM is trained. A common choice is byte pair encoding.
Another function of tokenizers is text compression, which saves compute.
Common words or phrases like \"where is\" can be encoded into one token,
instead of 7 characters. The OpenAI GPT series uses a tokenizer where 1
token maps to around 4 characters, or around 0.75 words, in common
English text. Uncommon English text is less predictable, thus less
compressible, thus requiring more tokens to encode. A tokenizer cannot
output arbitrary integers. They generally outputs only integers in the
range { 0 , 1 , 2 , . . . , V − 1 } {\\displaystyle
\\{0,1,2,\...,V-1\\}} , where V {\\displaystyle V} is called its
vocabulary size. Some tokenizers are capable of handling arbitrary text
(generally by operating directly on Unicode), but some do not. When
encountering un-encodable text, a tokenizer would output a special token
(often 0) that represents \"unknown text\". This is often written as
\[UNK\], such as in the BERT paper. Another special token commonly used
is \[PAD\] (often 1), for \"padding\". This is used because LLMs are
generally used on batches of text at one time, and these texts do not
encode to the same length. Since LLMs generally require input to be an
array that is not jagged, the shorter encoded texts must be padded until
they match the length of the longest one. Output The output of a LLM is
a probability distribution over its vocabulary. This is usually
implemented as follows: Upon receiving a text, the bulk of the LLM
outputs a vector y ∈ R V {\\displaystyle y\\in \\mathbb {R} \^{V}} where
V {\\displaystyle V} is its vocabulary size (defined above). The vector
y {\\displaystyle y} is passed through a softmax function to obtain
softmax ( y ) {\\displaystyle {\\textit {softmax}}(y)} .In the process,
the vector y {\\displaystyle y} is usually called the unnormalized logit
vector, and the vector softmax ( y ) {\\displaystyle {\\textit
{softmax}}(y)} is called the probability vector. Since the vector
softmax ( y ) {\\displaystyle {\\textit {softmax}}(y)} has V
{\\displaystyle V} entries, all non-negative, and they sum to 1, we can
interpret it as a probability distribution over { 0 , 1 , 2 , . . . , V
− 1 } {\\displaystyle \\{0,1,2,\...,V-1\\}} ---that is, it is a
probability distribution over the LLM\'s vocabulary. Note that the
softmax function is defined mathematically with no parameters to vary.
Consequently it is not trained. Training Most LLM are trained by
generative pretraining, that is, given a training dataset of text
tokens, the model predicts the tokens in the dataset. There are two
general styles of generative pretraining: autoregressive (GPT-style,
\"predict the next word\"): Given a segment of text like \"I like to
eat\" the model predicts the next tokens, like \"ice cream\". masked
(\"BERT-style\", \"cloze test\"): Given a segment of text like \"I like
to \[MASK\] \[MASK\] cream\" the model predicts the masked tokens, like
\"eat ice\".LLMs may be trained on auxiliary tasks which test their
understanding of the data distribution, such as Next Sentence Prediction
(NSP), in which pairs of sentences are presented and the model must
predict whether they appear consecutively in the training
corpus.Usually, LLMs are trained to minimize a specific loss function:
the average negative log likelihood per token (also called cross-entropy
loss). For example, if an autoregressive model, given \"I like to eat\",
predicts a probability distribution P r ( ⋅ \| I like to eat )
{\\displaystyle Pr(\\cdot \|{\\text{I like to eat}})} then the negative
log likelihood loss on this token is − log ⁡ P r ( ice \| I like to eat )
{\\displaystyle -\\log Pr({\\text{ice}}\|{\\text{I like to eat}})} .
During training, regularization loss is also used to stabilize training.
However regularization loss is usually not used during testing and
evaluation. There are also many more evaluation criteria than just
negative log likelihood. See the section below for details. Training
dataset size The earliest LLMs were trained on corpora having on the
order of billions of words. GPT-1, the first model in OpenAI\'s numbered
series of generative pre-trained transformer models, was trained in 2018
on BookCorpus, consisting of 985 million words. In the same year, BERT
was trained on a combination of BookCorpus and English Wikipedia,
totalling 3.3 billion words. Since then, training corpora for LLMs have
increased by orders of magnitude, reaching up to trillions of tokens.
Training cost LLMs are computationally expensive to train. A 2020 study
estimated the cost of training a 1.5 billion parameter model (2 orders
of magnitude smaller than the state of the art at the time) at \$1.6
million. Advances in software and hardware have brought the cost
substantially down, with a 2023 paper reporting a cost of 72,300
A100-GPU-hours to train a 12 billion parameter model.For
Transformer-based LLM, it costs 6 FLOPs per parameter to train on one
token. Note that training cost is much higher than inference cost, where
it costs 1 to 2 FLOPs per parameter to infer on one token. Application
to downstream tasks Between 2018 and 2020, the standard method for
harnessing an LLM for a specific natural language processing (NLP) task
was to fine tune the model with additional task-specific training. It
has subsequently been found that more powerful LLMs such as GPT-3 can
solve tasks without additional training via \"prompting\" techniques, in
which the problem to be solved is presented to the model as a text
prompt, possibly with some textual examples of similar problems and
their solutions. Fine-tuning Fine-tuning is the practice of modifying an
existing pretrained language model by training it (in a supervised
fashion) on a specific task (e.g. sentiment analysis, named-entity
recognition, or part-of-speech tagging). It is a form of transfer
learning. It generally involves the introduction of a new set of weights
connecting the final layer of the language model to the output of the
downstream task. The original weights of the language model may be
\"frozen\", such that only the new layer of weights connecting them to
the output are learned during training. Alternatively, the original
weights may receive small updates (possibly with earlier layers frozen).
Prompting In the prompting paradigm, popularized by GPT-3, the problem
to be solved is formulated via a text prompt, which the model must solve
by providing a completion (via inference). In \"few-shot prompting\",
the prompt includes a small number of examples of similar (problem,
solution) pairs. For example, a sentiment analysis task of labelling the
sentiment of a movie review could be prompted as follows: Review: This
movie stinks. Sentiment: negative Review: This movie is fantastic!
Sentiment: If the model outputs \"positive\", then it has correctly
solved the task. In zero-shot prompting, no solved examples are
provided. An example of a zero-shot prompt for the same sentiment
analysis task would be \"The sentiment associated with the movie review
\'This movie is fantastic!\' is\".Few-shot performance of LLMs has been
shown to achieve competitive results on NLP tasks, sometimes surpassing
prior state-of-the-art fine-tuning approaches. Examples of such NLP
tasks are translation, question answering, cloze tasks, unscrambling
words, and using a novel word in a sentence. The creation and
optimisation of such prompts is called prompt engineering. Instruction
tuning Instruction tuning is a form of fine-tuning designed to
facilitate more natural and accurate zero-shot prompting interactions.
Given a text input, a pretrained language model will generate a
completion which matches the distribution of text on which it was
trained. A naive language model given the prompt \"Write an essay about
the main themes of Hamlet.\" might provide a completion such as \"A late
penalty of 10% per day will be applied to submissions received after
March 17.\" In instruction tuning, the language model is trained on many
examples of tasks formulated as natural language instructions, along
with appropriate responses. Various techniques for instruction tuning
have been applied in practice. One example, \"self-instruct\",
fine-tunes the language model on a training set of examples which are
themselves generated by an LLM (bootstrapped from a small initial set of
human-generated examples). Reinforcement learning OpenAI\'s InstructGPT
protocol involves supervised fine-tuning on a dataset of human-generated
(prompt, response) pairs, followed by reinforcement learning from human
feedback (RLHF), in which a reward model was supervised-learned on a
dataset of human preferences, then this reward model was used to train
the LLM itself by proximal policy optimization. Evaluation Perplexity
The most commonly used measure of a language model\'s performance is its
perplexity on a given text corpus. Perplexity is a measure of how well a
model is able to predict the contents of a dataset; the higher the
likelihood the model assigns to the dataset, the lower the perplexity.
Mathematically, perplexity is defined as the exponential of the average
negative log likelihood per token:here N {\\displaystyle N} is the
number of tokens in the text corpus, and \"context for token i\" depends
on the specific type of LLM used. If the LLM is autoregressive, then
\"context for token i\" is the segment of text appearing before token i.
If the LLM is masked, then \"context for token i\" is the segment of
text surrounding token i. Because language models may overfit to their
training data, models are usually evaluated by their perplexity on a
test set of unseen data. This presents particular challenges for the
evaluation of large language models. As they are trained on increasingly
large corpora of text largely scraped from the web, it becomes
increasingly likely that models\' training data inadvertently includes
portions of any given test set. Task-specific datasets and benchmarks A
large number of testing datasets and benchmarks have also been developed
to evaluate the capabilities of language models on more specific
downstream tasks. Tests may be designed to evaluate a variety of
capabilities, including general knowledge, commonsense reasoning, and
mathematical problem-solving. One broad category of evaluation dataset
is question answering datasets, consisting of pairs of questions and
correct answers, for example, (\"Have the San Jose Sharks won the
Stanley Cup?\", \"No\"). A question answering task is considered \"open
book\" if the model\'s prompt includes text from which the expected
answer can be derived (for example, the previous question could be
adjoined with some text which includes the sentence \"The Sharks have
advanced to the Stanley Cup finals once, losing to the Pittsburgh
Penguins in 2016.\"). Otherwise, the task is considered \"closed book\",
and the model must draw on knowledge retained during training. Some
examples of commonly used question answering datasets include
TruthfulQA, Web Questions, TriviaQA, and SQuAD.Evaluation datasets may
also take the form of text completion, having the model select the most
likely word or sentence to complete a prompt, for example: \"Alice was
friends with Bob. Alice went to visit her friend, \_\_\_\_\".Some
composite benchmarks have also been developed which combine a diversity
of different evaluation datasets and tasks. Examples include GLUE,
SuperGLUE, MMLU, BIG-bench, and HELM.It was previously standard to
report results on a heldout portion of an evaluation dataset after doing
supervised fine-tuning on the remainder. It is now more common to
evaluate a pre-trained model directly through prompting techniques,
though researchers vary in the details of how they formulate prompts for
particular tasks, particularly with respect to how many examples of
solved tasks are adjoined to the prompt (i.e. the value of n in n-shot
prompting). Adversarially constructed evaluations Because of the rapid
pace of improvement of large language models, evaluation benchmarks have
suffered from short lifespans, with state of the art models quickly
\"saturating\" existing benchmarks, exceeding the performance of human
annotators, leading to efforts to replace or augment the benchmark with
more challenging tasks.Some datasets have been constructed
adversarially, focusing on particular problems on which extant language
models seem to have unusually poor performance compared to humans. One
example is the TruthfulQA dataset, a question answering dataset
consisting of 817 questions which language models are susceptible to
answering incorrectly by mimicking falsehoods to which they were
repeatedly exposed during training. For example, an LLM may answer
\"No\" to the question \"Can you teach an old dog new tricks?\" because
of its exposure to the English idiom you can\'t teach an old dog new
tricks, even though this is not literally true.Another example of an
adversarial evaluation dataset is Swag and its successor, HellaSwag,
collections of problems in which one of multiple options must be
selected to complete a text passage. The incorrect completions were
generated by sampling from a language model and filtering with a set of
classifiers. The resulting problems are trivial for humans but at the
time the datasets were created state of the art language models had poor
accuracy on them. For example: We see a fitness center sign. We then see
a man talking to the camera and sitting and laying on a exercise ball.
The man\... a) demonstrates how to increase efficient exercise work by
running up and down balls. b) moves all his arms and legs and builds up
a lot of muscle. c) then plays the ball and we see a graphics and hedge
trimming demonstration. d) performs sits ups while on the ball and
talking. BERT selects b) as the most likely completion, though the
correct answer is d). List of large language models See also Foundation
models Notes == References ==
