In machine learning, a probabilistic classifier is a classifier that is
able to predict, given an observation of an input, a probability
distribution over a set of classes, rather than only outputting the most
likely class that the observation should belong to. Probabilistic
classifiers provide classification that can be useful in its own right
or when combining classifiers into ensembles. Types of classification
Formally, an \"ordinary\" classifier is some rule, or function, that
assigns to a sample x a class label ŷ: y \^ = f ( x ) {\\displaystyle
{\\hat {y}}=f(x)} The samples come from some set X (e.g., the set of all
documents, or the set of all images), while the class labels form a
finite set Y defined prior to training. Probabilistic classifiers
generalize this notion of classifiers: instead of functions, they are
conditional distributions Pr ( Y \| X ) {\\displaystyle \\Pr(Y\\vert X)}
, meaning that for a given x ∈ X {\\displaystyle x\\in X} , they assign
probabilities to all y ∈ Y {\\displaystyle y\\in Y} (and these
probabilities sum to one). \"Hard\" classification can then be done
using the optimal decision rule: 39--40  y \^ = arg ⁡ max y ⁡ Pr ( Y = y
\| X ) {\\displaystyle {\\hat {y}}=\\operatorname {\\arg \\max }
\_{y}\\Pr(Y=y\\vert X)} or, in English, the predicted class is that
which has the highest probability. Binary probabilistic classifiers are
also called binary regression models in statistics. In econometrics,
probabilistic classification in general is called discrete choice. Some
classification models, such as naive Bayes, logistic regression and
multilayer perceptrons (when trained under an appropriate loss function)
are naturally probabilistic. Other models such as support vector
machines are not, but methods exist to turn them into probabilistic
classifiers. Generative and conditional training Some models, such as
logistic regression, are conditionally trained: they optimize the
conditional probability Pr ( Y \| X ) {\\displaystyle \\Pr(Y\\vert X)}
directly on a training set (see empirical risk minimization). Other
classifiers, such as naive Bayes, are trained generatively: at training
time, the class-conditional distribution Pr ( X \| Y ) {\\displaystyle
\\Pr(X\\vert Y)} and the class prior Pr ( Y ) {\\displaystyle \\Pr(Y)}
are found, and the conditional distribution Pr ( Y \| X )
{\\displaystyle \\Pr(Y\\vert X)} is derived using Bayes\' rule.: 43
Probability calibration Not all classification models are naturally
probabilistic, and some that are, notably naive Bayes classifiers,
decision trees and boosting methods, produce distorted class probability
distributions. In the case of decision trees, where Pr(y\|x) is the
proportion of training samples with label y in the leaf where x ends up,
these distortions come about because learning algorithms such as C4.5 or
CART explicitly aim to produce homogeneous leaves (giving probabilities
close to zero or one, and thus high bias) while using few samples to
estimate the relevant proportion (high variance). Calibration can be
assessed using a calibration plot (also called a reliability diagram). A
calibration plot shows the proportion of items in each class for bands
of predicted probability or score (such as a distorted probability
distribution or the \"signed distance to the hyperplane\" in a support
vector machine). Deviations from the identity function indicate a
poorly-calibrated classifier for which the predicted probabilities or
scores can not be used as probabilities. In this case one can use a
method to turn these scores into properly calibrated class membership
probabilities. For the binary case, a common approach is to apply Platt
scaling, which learns a logistic regression model on the scores. An
alternative method using isotonic regression is generally superior to
Platt\'s method when sufficient training data is available.In the
multiclass case, one can use a reduction to binary tasks, followed by
univariate calibration with an algorithm as described above and further
application of the pairwise coupling algorithm by Hastie and Tibshirani.
Evaluating probabilistic classification Commonly used loss functions for
probabilistic classification include log loss and the Brier score
between the predicted and the true probability distributions. The former
of these is commonly used to train logistic models. A method used to
assign scores to pairs of predicted probabilities and actual discrete
outcomes, so that different predictive methods can be compared, is
called a scoring rule. Software Implementations MoRPE is a trainable
probabilistic classifier that uses isotonic regression for probability
calibration. It solves the multiclass case by reduction to binary tasks.
It is a type of kernel machine that uses an inhomogeneous polynomial
kernel. == References ==
