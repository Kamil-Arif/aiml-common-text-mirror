The MNIST database (Modified National Institute of Standards and
Technology database) is a large database of handwritten digits that is
commonly used for training various image processing systems. The
database is also widely used for training and testing in the field of
machine learning. It was created by \"re-mixing\" the samples from
NIST\'s original datasets. The creators felt that since NIST\'s training
dataset was taken from American Census Bureau employees, while the
testing dataset was taken from American high school students, it was not
well-suited for machine learning experiments. Furthermore, the black and
white images from NIST were normalized to fit into a 28x28 pixel
bounding box and anti-aliased, which introduced grayscale levels.The
MNIST database contains 60,000 training images and 10,000 testing
images. Half of the training set and half of the test set were taken
from NIST\'s training dataset, while the other half of the training set
and the other half of the test set were taken from NIST\'s testing
dataset. The original creators of the database keep a list of some of
the methods tested on it. In their original paper, they use a
support-vector machine to get an error rate of 0.8%.Extended MNIST
(EMNIST) is a newer dataset developed and released by NIST to be the
(final) successor to MNIST. MNIST included images only of handwritten
digits. EMNIST includes all the images from NIST Special Database 19,
which is a large database of handwritten uppercase and lower case
letters as well as digits. The images in EMNIST were converted into the
same 28x28 pixel format, by the same process, as were the MNIST images.
Accordingly, tools which work with the older, smaller, MNIST dataset
will likely work unmodified with EMNIST. History The set of images in
the MNIST database was created in 1994 as a combination of two of
NIST\'s databases: Special Database 1 and Special Database 3. Special
Database 1 and Special Database 3 consist of digits written by high
school students and employees of the United States Census Bureau,
respectively. Performance Some researchers have achieved \"near-human
performance\" on the MNIST database, using a committee of neural
networks; in the same paper, the authors achieve performance double that
of humans on other recognition tasks. The highest error rate listed on
the original website of the database is 12 percent, which is achieved
using a simple linear classifier with no preprocessing.In 2004, a
best-case error rate of 0.42 percent was achieved on the database by
researchers using a new classifier called the LIRA, which is a neural
classifier with three neuron layers based on Rosenblatt\'s perceptron
principles.Some researchers have tested artificial intelligence systems
using the database put under random distortions. The systems in these
cases are usually neural networks and the distortions used tend to be
either affine distortions or elastic distortions. Sometimes, these
systems can be very successful; one such system achieved an error rate
on the database of 0.39 percent.In 2011, an error rate of 0.27 percent,
improving on the previous best result, was reported by researchers using
a similar system of neural networks. In 2013, an approach based on
regularization of neural networks using DropConnect has been claimed to
achieve a 0.21 percent error rate. In 2016, the single convolutional
neural network best performance was 0.25 percent error rate. As of
August 2018, the best performance of a single convolutional neural
network trained on MNIST training data using no data augmentation is
0.25 percent error rate. Also, the Parallel Computing Center
(Khmelnytskyi, Ukraine) obtained an ensemble of only 5 convolutional
neural networks which performs on MNIST at 0.21 percent error rate. Some
images in the testing dataset are barely readable and may prevent
reaching test error rates of 0%. In 2018, researchers from Department of
System and Information Engineering, University of Virginia announced
0.18% error with simultaneous stacked three kind of neural networks
(fully connected, recurrent and convolution neural networks).
Classifiers This is a table of some of the machine learning methods used
on the dataset and their error rates, by type of classifier: See also
List of datasets for machine learning research Caltech 101 LabelMe OCR
References Further reading Ciresan, Dan; Meier, Ueli; Schmidhuber,
Jürgen (June 2012). \"Multi-column deep neural networks for image
classification\" (PDF). 2012 IEEE Conference on Computer Vision and
Pattern Recognition. New York, NY: Institute of Electrical and
Electronics Engineers. pp. 3642--3649. arXiv:1202.2745. CiteSeerX
10.1.1.300.3283. doi:10.1109/CVPR.2012.6248110. ISBN 9781467312264. OCLC
812295155. S2CID 2161592. Retrieved 2013-12-09. External links Official
website Visualization of the MNIST database -- groups of images of MNIST
handwritten digits on GitHub
