Seq2seq is a family of machine learning approaches used for natural
language processing. Applications include language translation, image
captioning, conversational models and text summarization. History The
algorithm was developed by Google for use in machine translation.Similar
earlier work includes Tomáš Mikolov\'s 2012 PhD thesis.In 2019, Facebook
announced its use in symbolic integration and resolution of differential
equations. The company claimed that it could solve complex equations
more rapidly and with greater accuracy than commercial solutions such as
Mathematica, MATLAB and Maple. First, the equation is parsed into a tree
structure to avoid notational idiosyncrasies. An LSTM neural network
then applies its standard pattern recognition facilities to process the
tree.In 2020, Google released Meena, a 2.6 billion parameter
seq2seq-based chatbot trained on a 341 GB data set. Google claimed that
the chatbot has 1.7 times greater model capacity than OpenAI\'s GPT-2,
whose May 2020 successor, the 175 billion parameter GPT-3, trained on a
\"45TB dataset of plaintext words (45,000 GB) that was \... filtered
down to 570 GB.\"In 2022, Amazon introduced AlexaTM 20B, a
moderate-sized (20 billion parameter) seq2seq language model. It uses an
encoder-decoder to accomplish few-shot learning. The encoder outputs a
representation of the input that the decoder uses as input to perform a
specific task, such as translating the input into another language. The
model outperforms the much larger GPT-3 in language translation and
summarization. Training mixes denoising (appropriately inserting missing
text in strings) and causal-language-modeling (meaningfully extending an
input text). It allows adding features across different languages
without massive training workflows. AlexaTM 20B achieved
state-of-the-art performance in few-shot-learning tasks across all
Flores-101 language pairs, outperforming GPT-3 on several tasks.
Technique Seq2seq turns one sequence into another sequence (sequence
transformation). It does so by use of a recurrent neural network (RNN)
or more often LSTM or GRU to avoid the problem of vanishing gradient.
The context for each item is the output from the previous step. The
primary components are one encoder and one decoder network. The encoder
turns each item into a corresponding hidden vector containing the item
and its context. The decoder reverses the process, turning the vector
into an output item, using the previous output as the input
context.Optimizations include: Attention: The input to the decoder is a
single vector which stores the entire context. Attention allows the
decoder to look at the input sequence selectively. Beam Search: Instead
of picking the single output (word) as the output, multiple highly
probable choices are retained, structured as a tree (using a Softmax on
the set of attention scores). Average the encoder states weighted by the
attention distribution. Bucketing: Variable-length sequences are
possible because of padding with 0s, which may be done to both input and
output. However, if the sequence length is 100 and the input is just 3
items long, expensive space is wasted. Buckets can be of varying sizes
and specify both input and output lengths.Training typically uses a
cross-entropy loss function, whereby one output is penalized to the
extent that the probability of the succeeding output is less than 1.
Related software Software adopting similar approaches includes OpenNMT
(Torch), Neural Monkey (TensorFlow) and NEMATUS (Theano). See also
Artificial neural network References External links \"A ten-minute
introduction to sequence-to-sequence learning in Keras\". blog.keras.io.
Retrieved 2019-12-19. Dugar, Pranay (2019-11-24). \"Attention ---
Seq2Seq Models\". Medium. Retrieved 2019-12-19. Nag, Dev (2019-04-24).
\"seq2seq: the clown car of deep learning\". Medium. Retrieved
2019-12-19. Adiwardana, Daniel; Luong, Minh-Thang; So, David R.; Hall,
Jamie; Fiedel, Noah; Thoppilan, Romal; Yang, Zi; Kulshreshtha, Apoorv;
Nemade, Gaurav; Lu, Yifeng; Le, Quoc V. (2020-01-31). \"Towards a
Human-like Open-Domain Chatbot\". arXiv:2001.09977 \[cs.CL\].
