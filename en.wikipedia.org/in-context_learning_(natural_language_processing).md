In natural language processing, in-context learning, few-shot learning
or few-shot prompting is a prompting technique that allows a model to
process examples before attempting a task. The method was popularized
after the advent of GPT-3 and is considered to be an emergent property
of large language models.A few-shot prompt normally includes n examples
of (problem, solution) pairs known as \"shots\", with the overall usage
of such a prompt being known as n-shot prompting. For instance, the
following is a one-shot prompt for review sentiment classification:
Review: This movie sucks. Sentiment: negative. Review: I love this
movie. Sentiment: If the model outputs \"positive\", then it has
correctly solved the task.The term zero-shot prompting is often used to
signify that no examples are provided. An example of a zero-shot prompt
for a question-answering task would be \"Who wrote the book On the
Origin of Species?\". In-context learning was initially proposed as an
alternative to fine-tuning a pre-trained language model on a
task-specific dataset. The main advantages of in-context learning over
fine-tuning are a reduction in the amount of task-specific data needed
and a reduced potential of overfitting by learning an overly narrow
distribution from a large but narrow fine-tuning dataset. Few-shot
performance of large language models has been shown to achieve
competitive results on NLP tasks, sometimes surpassing prior
state-of-the-art fine-tuning approaches. Examples of such NLP tasks are
translation, question answering, cloze tasks, unscrambling words, and
using a novel word in a sentence. The creation and optimization of such
few-shot prompts is part of the now active field of study of prompt
engineering.While few-shot prompting has performed competitively when
compared to fine-tuned models, it has its own drawbacks. For example, it
has been shown that the order in which the shots are listed can make the
difference between state-of-the-art and random guess performance. A set
of few-shot examples that works well in some specific order with one
model may not work at all when used with a different model.A common
example of in-context learning is chain-of-thought prompting, where
few-shot examples are given to teach the model to output a string of
reasoning before attempting to answer a question. This technique has
been shown to improve performance of models in tasks that require
logical thinking and reasoning. See also Prompt engineering Fine-tuning
(machine learning) Chain-of-thought prompting == References ==
