A Vision Transformer (ViT) is a transformer that is targeted at vision
processing tasks such as image recognition. Vision Transformers
Transformers found their initial applications in natural language
processing (NLP) tasks, as demonstrated by language models such as BERT
and GPT-3. By contrast the typical image processing system uses a
convolutional neural network (CNN). Well-known projects include
Xception, ResNet, EfficientNet, DenseNet, and Inception.Transformers
measure the relationships between pairs of input tokens (words in the
case of text strings), termed attention. The cost is quadratic in the
number of tokens. For images, the basic unit of analysis is the pixel.
However, computing relationships for every pixel pair in a typical image
is prohibitive in terms of memory and computation. Instead, ViT computes
relationships among pixels in various small sections of the image (e.g.,
16x16 pixels), at a drastically reduced cost. The sections (with
positional embeddings) are placed in a sequence. The embeddings are
learnable vectors. Each section is arranged into a linear sequence and
multiplied by the embedding matrix. The result, with the position
embedding is fed to the transformer.As in the case of BERT, a
fundamental role in classification tasks is played by the class token. A
special token that is used as the only input of the final MLP Head as it
has been influenced by all the others. The architecture for image
classification is the most common and uses only the Transformer Encoder
in order to transform the various input tokens. However, there are also
other applications in which the decoder part of the traditional
Transformer Architecture is also used. History The general transformer
architecture was initially introduced in 2017 in the well-known paper
\"Attention is All You Need\". They have spread widely in the field of
Natural Language Processing and have become one of the most widely used
and promising neural network architectures in the field. In 2019 the
Vision Transformer architecture for processing images without the need
of any convolutions was proposed by Cordonnier et al., and later
empirically evaluated more extensively in the well-known paper \"An
image is worth 16x16 words\". The idea is basically to break down input
images as a series of patches which, once transformed into vectors, are
seen as words in a normal transformer. If in the field of Natural
Language Processing the mechanism of attention of the Transformers tried
to capture the relationships between different words of the text to be
analysed, in Computer Vision the Vision Transformers try instead to
capture the relationships between different portions of an image. In
2021 a pure transformer model demonstrated better performance and
greater efficiency than CNNs on image classification.A study in June
2021 added a transformer backend to Resnet, which dramatically reduced
costs and increased accuracy.In the same year, some important variants
of the Vision Transformers were proposed. These variants are mainly
intended to be more efficient, more accurate or better suited to a
specific domain. Among the most relevant is the Swin Transformer, which
through some modifications to the attention mechanism and a multi-stage
approach achieved state-of-the-art results on some object detection
datasets such as COCO. Another interesting variant is the TimeSformer,
designed for video understanding tasks and able to capture spatial and
temporal information through the use of divided space-time
attention.Vision Transformers were also able to get out of the lab and
into one of the most important fields of Computer Vision, autonomous
driving. Comparison with Convolutional Neural Networks ViT performance
depends on decisions including that of the optimizer, dataset-specific
hyperparameters, and network depth. CNN are much easier to optimize. A
variation on a pure transformer is to marry a transformer to a CNN
stem/front end. A typical ViT stem uses a 16x16 convolution with a 16
stride. By contrast a 3x3 convolution with stride 2, increases stability
and also improves accuracy.The CNN translates from the basic pixel level
to a feature map. A tokenizer translates the feature map into a series
of tokens that are then fed into the transformer, which applies the
attention mechanism to produce a series of output tokens. Finally, a
projector reconnects the output tokens to the feature map. The latter
allows the analysis to exploit potentially significant pixel-level
details. This drastically reduces the number of tokens that need to be
analyzed, reducing costs accordingly.The differences between CNNs and
Vision Transformers are many and lie mainly in their architectural
differences. In fact, CNNs achieve excellent results even with training
based on data volumes that are not as large as those required by Vision
Transformers. This different behaviour seems to derive from the presence
in the CNNs of some inductive biases that can be somehow exploited by
these networks to grasp more quickly the particularities of the analysed
images even if, on the other hand, they end up limiting them making it
more complex to grasp global relations.On the other hand, the Vision
Transformers are free from these biases which leads them to be able to
capture also global and wider range relations but at the cost of a more
onerous training in terms of data. Vision Transformers also proved to be
much more robust to input image distortions such as adversarial patches
or permutations.However, choosing one architecture over another is not
always the wisest choice, and excellent results have been obtained in
several Computer Vision tasks through hybrid architectures combining
convolutional layers with Vision Transformers. The Role of
Self-Supervised Learning The considerable need for data during the
training phase has made it essential to find alternative methods to
train these models, and a central role is now played by self-supervised
methods. Using these approaches, it is possible to train a neural
network in an almost autonomous way, allowing it to deduce the
peculiarities of a specific problem without having to build a large
dataset or provide it with accurately assigned labels. Being able to
train a Vision Transformer without having to have a huge vision dataset
at its disposal could be the key to the widespread dissemination of this
promising new architecture. Applications Vision Transformers have been
used in many Computer Vision tasks with excellent results and in some
cases even state-of-the-art. Among the most relevant areas of
application are: Image Classification Object Detection Video Deepfake
Detection Image segmentation Anomaly detection Image Synthesis Cluster
analysis Autonomous Driving Implementations There are many
implementations of Vision Transformers and its variants available in
open source online. The main versions of this architecture have been
implemented in PyTorch but implementations have also been made available
for TensorFlow. See also Transformer (machine learning model) Attention
(machine learning) Perceiver Deep learning PyTorch TensorFlow References
External links Igarashi, Yoshiyuki (2021-02-04). \"Are You Ready for
Vision Transformer (ViT)?\". Medium. Retrieved 2021-07-11. Coccomini,
Davide (2021-05-03). \"On DINO, Self-Distillation with no labels\".
Towards Data Science. Retrieved 2021-10-03.
