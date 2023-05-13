Generative Pre-trained Transformer 2 (GPT-2) is an open-source
artificial intelligence large language model created by OpenAI in
February 2019. GPT-2 translates text, answers questions, summarizes
passages, and generates text output on a level that, while sometimes
indistinguishable from that of humans, can become repetitive or
nonsensical when generating long passages. It is a general-purpose
learner; it was not specifically trained to do any of these tasks, and
its ability to perform them is an extension of its general ability to
accurately synthesize the next item in an arbitrary sequence. GPT-2 was
created as a \"direct scale-up\" of OpenAI\'s 2018 GPT model
(\"GPT-1\"), with a ten-fold increase in both its parameter count and
the size of its training dataset.GPT-2 has a generative pre-trained
transformer architecture which implements a deep neural network,
specifically a transformer model, which uses attention in place of
previous recurrence- and convolution-based architectures. Attention
mechanisms allow the model to selectively focus on segments of input
text it predicts to be the most relevant. This model allows for greatly
increased parallelization, and outperforms previous benchmarks for
RNN/CNN/LSTM-based models.OpenAI released the complete version of the
GPT-2 language model (with 1.5 billion parameters) in November 2019.
Background: GPT-1 (Predecessor model) Google invented the transformer
architecture in 2017. Building upon that development, in 2018 OpenAI
released a paper entitled \"Improving Language Understanding by
Generative Pre-Training\", in which they introduced the concept of a
generative pre-trained transformer and the first example which became
known as GPT-1.Up to that point, the best-performing neural NLP models
primarily employed supervised learning from large amounts of manually
labeled data. This reliance on supervised learning limited their use on
datasets that were not well-annotated, in addition to making it
prohibitively expensive and time-consuming to train extremely large
models; many languages (such as Swahili or Haitian Creole) are difficult
to translate and interpret using such models due to a lack of available
text for corpus-building. In contrast, a GPT\'s \"semi-supervised\"
approach involved two stages: an unsupervised generative
\"pre-training\" stage in which a language modeling objective was used
to set initial parameters, and a supervised discriminative
\"fine-tuning\" stage in which these parameters were adapted to a target
task.The use of a transformer architecture, as opposed to previous
techniques involving attention-augmented RNNs, provided GPT models with
a more structured memory than could be achieved through recurrent
mechanisms; this resulted in \"robust transfer performance across
diverse tasks\". Corpus The unsupervised pre-training was performed
using \"Common Crawl\" (a massive dataset of web pages) and BookCorpus,
a dataset of over 7,000 unpublished fiction books from various genres;
this dataset was chosen in part because its long passages of continuous
text conditioned the model to handle long-range information. Other
available datasets, while larger, were rejected on the basis that they
lacked this long-range structure (being \"shuffled\" at a sentence
level). The ftfy library was used to clean the BookCorpus text
(standardize punctuation and whitespace); it was tokenized using spaCy.
Architecture The GPT-1 architecture itself was a twelve-layer
decoder-only transformer, using twelve masked self-attention heads, with
64 dimensional states each (for a total of 768). Rather than simple
stochastic gradient descent, the Adam optimization algorithm was used;
the learning rate was increased linearly from zero over the first 2,000
updates, to a maximum of 2.5×10−4, and annealed to 0 using a cosine
schedule.While the fine-tuning was adapted to specific tasks, its
pre-training was not; to perform the various tasks, minimal changes were
performed to its underlying task-agnostic model architecture. Despite
this, GPT-1 still improved on previous benchmarks in several language
processing tasks, outperforming discriminatively-trained models with
task-oriented architectures on a number of diverse tasks. Performance On
natural language inference (also known as textual entailment) tasks,
models are evaluated on their ability to interpret pairs of sentences
from various datasets and classify the relationship between them as
\"entailment\", \"contradiction\" or \"neutral\". Examples of such
datasets include QNLI (Wikipedia articles) and MultiNLI (transcribed
speech, popular fiction and government reports, among other sources); on
these GPT-1 achieved, respectively, a 5.8% and 1.5% improvement over
previous best results. It similarly outperformed previous models on two
tasks related to question answering and commonsense reasoning---by 5.7%
on RACE, a dataset of written question--answer pairs from middle and
high school exams, and by 8.9% on the Story Cloze Test.Another task,
semantic similarity (or paraphrase detection), assesses whether a model
can predict whether two sentences are paraphrases of one another; on the
Quora Question Pairs (QQP) dataset, GPT-1 improved on previous
best-performing models by 4.2%. In a text classification task using the
Corpus of Linguistic Acceptability (CoLA), GPT-1 achieved a score of
45.4, versus a previous best of 35.0. Finally, on GLUE, a multi-task
test, GPT-1 achieved an overall score of 72.8 (compared to a previous
record of 68.9). Scale-up from GPT-1 to GPT-2 GPT-2 was created as a
direct scale-up of GPT-1, with both its parameter count and dataset size
increased by a factor of 10. Both are unsupervised transformer models
trained to generate text by predicting the next word in a sequence of
tokens. The GPT-2 model has 1.5 billion parameters, and was trained on a
dataset of 8 million web pages. While GPT-2 was reinforced on very
simple criteria (interpreting a sequence of words in a text sample and
predicting the most likely next word), it produces full sentences and
paragraphs by continuing to predict additional words, generating fully
comprehensible (and semantically meaningful) statements in natural
language. Notably, GPT-2 was evaluated on its performance on tasks in a
zero-shot setting. Training Since the transformer architecture enabled
massive parallelization, GPT models could be trained on larger corpora
than previous NLP models. While the GPT-1 model demonstrated that the
approach was viable, GPT-2 would further explore the emergent properties
of networks trained on extremely large corpora. CommonCrawl, a large
corpus produced by web crawling and previously used in training NLP
systems, was considered due to its large size, but was rejected after
further review revealed large amounts of unintelligible content.
Instead, OpenAI developed a new corpus, known as WebText; rather than
scraping content indiscriminately from the World Wide Web, WebText was
generated by scraping only pages linked to by Reddit posts that had
received at least three upvotes prior to December 2017. The corpus was
subsequently cleaned; HTML documents were parsed into plain text,
duplicate pages were eliminated, and Wikipedia pages were removed (since
their presence in many other datasets could have induced
overfitting).While the cost of training GPT-2 is known to have been
\$256 per hour, the amount of hours it took to complete training is
unknown; therefore, the overall training cost cannot be estimated
accurately. However, comparable large language models using transformer
architectures have had their costs documented in more detail; the
training processes for BERT and XLNet consumed, respectively, \$6,912
and \$245,000 of resources. Performance GPT-2 became capable of
performing a variety of tasks beyond simple text production due to the
breadth of its dataset and technique: answering questions, summarizing,
and even translating between languages in a variety of specific domains,
without being instructed in anything beyond how to predict the next word
in a sequence.One example of generalized learning is GPT-2\'s ability to
perform machine translation between French and English, for which task
GPT-2\'s performance was assessed using WMT-14 translation tasks.
GPT-2\'s training corpus included virtually no French text; non-English
text was deliberately removed while cleaning the dataset prior to
training, and as a consequence, only 10MB of French of the remaining
40,000MB was available for the model to learn from (mostly from
foreign-language quotations in English posts and articles).Despite this,
GPT-2 achieved 5 BLEU on the WMT-14 English-to-French test set (slightly
below the score of a translation via word-for-word substitution). It was
also able to outperform several contemporary (2017) unsupervised machine
translation baselines on the French-to-English test set, where GPT-2
achieved 11.5 BLEU. This remained below the highest-performing
contemporary unsupervised approach (2019), which had achieved 33.5 BLEU.
However, other models used large amounts of French text to achieve these
results; GPT-2 was estimated to have used a monolingual French corpus
approximately 1/500 the size of comparable approaches. GPT-2 was to be
followed by the 175-billion-parameter GPT-3, revealed to the public in
2020 (whose source code has never been made available). Access to GPT-3
is provided exclusively through APIs offered by OpenAI and Microsoft.
That was then later followed by GPT-4. Release GPT-2 was first announced
on 14 February 2019. A February 2019 article in The Verge by James
Vincent said that, while \"\[the\] writing it produces is usually easily
identifiable as non-human\", it remained \"one of the most exciting
examples yet\" of language generation programs: Give it a fake headline,
and it'll write the rest of the article, complete with fake quotations
and statistics. Feed it the first line of a short story, and it'll tell
you what happens to your character next. It can even write fan fiction,
given the right prompt. The Guardian described this output as
\"plausible newspaper prose\"; Kelsey Piper of Vox said \"one of the
coolest AI systems I've ever seen may also be the one that will kick me
out of my job\". GPT-2\'s flexibility was described as \"impressive\" by
The Verge; specifically, its ability to translate text between
languages, summarize long articles, and answer trivia questions were
noted.A study by the University of Amsterdam employing a modified Turing
test found that at least in some scenarios, participants were unable to
distinguish poems generated by GPT-2 from those written by humans.
Restrictions and partial release While previous OpenAI models had been
made immediately available to the public, OpenAI initially refused to
make a public release of GPT-2\'s source code when announcing it in
February, citing the risk of malicious use; limited access to the model
(i.e. an interface that allowed input and provided output, not the
source code itself) was allowed for selected press outlets on
announcement. One commonly-cited justification was that, since generated
text was usually completely novel, it could be used by spammers to evade
automated filters; OpenAI demonstrated a version of GPT-2 fine-tuned to
\"generate infinite positive -- or negative -- reviews of
products\".Another justification was that GPT-2 could be used to
generate text that was obscene or racist. Researchers such as Jeremy
Howard warned of \"the technology to totally fill Twitter, email, and
the web up with reasonable-sounding, context-appropriate prose, which
would drown out all other speech and be impossible to filter\". The
Allen Institute for Artificial Intelligence, in response to GPT-2,
announced a tool to detect \"neural fake news\".However, opinion was
divided. A February 2019 article in The Verge argued that the threat
posed by GPT-2 had been exaggerated; Anima Anandkumar, a professor at
Caltech and director of machine learning research at Nvidia, said that
there was no evidence that GPT-2 had the capabilities to pose the
threats described by OpenAI, and that what they did was the \"opposite
of open\", characterizing their refusal to release the full model as
\"malicious BS\". The Gradient published an open letter to OpenAI
requesting that they release the model publicly, comparing the threat
posed by text-generation AI to the threat posed by the printing press,
and giving Photoshop as an example of \"a technology that has
(thankfully) not destroyed modern society despite its potential for
chaos\": Thirty years later, society has emerged relatively unscathed
despite Photoshop being simple enough for high school students to use
and ubiquitous enough to commandeer its own verb. Why? Precisely because
everyone knows about Photoshop. 774M release While OpenAI did not
release the fully-trained model or the corpora it was trained on,
description of their methods in prior publications (and the free
availability of underlying technology) made it possible for GPT-2 to be
replicated by others as free software; one such replication, OpenGPT-2,
was released in August 2019, in conjunction with a freely licensed
version of WebText called OpenWebText. The cloud compute costs for
OpenGPT-2 were given as approximately \$50,000.On August 20, 2019,
OpenAI released a partial version of GPT-2, with 774 million parameters
(roughly half the size of the full 1.5 billion parameter model). Full
1.5B release Initial concerns that GPT-2 would lend itself to widespread
misuse did not come to pass; The Verge said that \"there are reasons to
be skeptical about claims that AI technology will usher in some sort of
'infopocalypse.' For a start, we already have programs that can generate
plausible text at high volume for little cost: humans.\" By November
2019, OpenAI said that they had \"seen no strong evidence of misuse so
far\", and the full version, with 1.5 billion parameters, was released
on November 5, 2019. Limitations While GPT-2\'s ability to generate
plausible passages of natural language text were generally remarked on
positively, its shortcomings were noted as well, especially when
generating texts longer than a couple paragraphs; Vox said \"the prose
is pretty rough, there's the occasional non-sequitur, and the articles
get less coherent the longer they get\". The Verge similarly noted that
longer samples of GPT-2 writing tended to \"stray off topic\" and lack
overall coherence; The Register opined that \"a human reading it should,
after a short while, realize something\'s up\", and noted that \"GPT-2
doesn\'t answer questions as well as other systems that rely on
algorithms to extract and retrieve information.\"GPT-2 deployment is
resource-intensive; the full version of the model is larger than five
gigabytes, making it difficult to embed locally into applications, and
consumes large amounts of RAM. In addition, performing a single
prediction \"can occupy a CPU at 100% utilization for several minutes\",
and even with GPU processing, \"a single prediction can take seconds\".
To alleviate these issues, the company Hugging Face created DistilGPT2,
using knowledge distillation to produce a smaller model that \"scores a
few points lower on some quality benchmarks\", but is \"33% smaller and
twice as fast\". Implementations and subsequent research Possible
applications of GPT-2 described by journalists included aiding humans in
writing text like news articles. Even before the release of the full
version, GPT-2 was used for a variety of applications and services, as
well as for entertainment. In June 2019, a subreddit named
r/SubSimulatorGPT2 was created in which a variety of GPT-2 instances
trained on different subreddits made posts and replied to each other\'s
comments, creating a situation where one could observe \"an AI
personification of r/Bitcoin argue with the machine learning-derived
spirit of r/ShittyFoodPorn\"; by July of that year, a GPT-2-based
software program released to autocomplete lines of code in a variety of
programming languages was described by users as a \"game-changer\".In
2019, AI Dungeon was launched, which used GPT-2 to generate dynamic text
adventures based on user input. AI Dungeon now offers access to the
largest release of GPT-3 API as an optional paid upgrade, the free
version of the site uses the 2nd largest release of GPT-3. Latitude, the
company formed around AI Dungeon, raised \$3.3 million in seed funding
in 2021. Several websites host interactive demonstrations of different
instances of GPT-2 and other transformer models.In February 2021, a
crisis center for troubled teens announced that they would begin using a
GPT-2-derived chatbot to help train counselors by allowing them to have
conversations with simulated teens (this use was purely for internal
purposes, and did not involve having GPT-2 communicate with the teens
themselves).On May 9, 2023, OpenAI released a mapped version of GPT-2.
OpenAI used successor model, GPT-4, to map each neuron of GPT-2 to
determine their functions. == References ==
