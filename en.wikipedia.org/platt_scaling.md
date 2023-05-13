In machine learning, Platt scaling or Platt calibration is a way of
transforming the outputs of a classification model into a probability
distribution over classes. The method was invented by John Platt in the
context of support vector machines, replacing an earlier method by
Vapnik, but can be applied to other classification models. Platt scaling
works by fitting a logistic regression model to a classifier\'s scores.
Description Consider the problem of binary classification: for inputs x,
we want to determine whether they belong to one of two classes,
arbitrarily labeled +1 and −1. We assume that the classification problem
will be solved by a real-valued function f, by predicting a class label
y = sign(f(x)). For many problems, it is convenient to get a probability
P ( y = 1 \| x ) {\\displaystyle P(y=1\|x)} , i.e. a classification that
not only gives an answer, but also a degree of certainty about the
answer. Some classification models do not provide such a probability, or
give poor probability estimates. Platt scaling is an algorithm to solve
the aforementioned problem. It produces probability estimates P ( y = 1
\| x ) = 1 1 + exp ⁡ ( A f ( x ) + B ) {\\displaystyle \\mathrm {P}
(y=1\|x)={\\frac {1}{1+\\exp(Af(x)+B)}}} ,i.e., a logistic
transformation of the classifier scores f(x), where A and B are two
scalar parameters that are learned by the algorithm. Note that
predictions can now be made according to y = 1 iff P ( y = 1 \| x ) \> 1
2 ; {\\displaystyle y=1{\\text{ iff }}P(y=1\|x)\>{\\frac {1}{2}};} if B
≠ 0 , {\\displaystyle B\\neq 0,} the probability estimates contain a
correction compared to the old decision function y = sign(f(x)).The
parameters A and B are estimated using a maximum likelihood method that
optimizes on the same training set as that for the original classifier
f. To avoid overfitting to this set, a held-out calibration set or
cross-validation can be used, but Platt additionally suggests
transforming the labels y to target probabilities t + = N + + 1 N + + 2
{\\displaystyle t\_{+}={\\frac {N\_{+}+1}{N\_{+}+2}}} for positive
samples (y = 1), and t − = 1 N − + 2 {\\displaystyle t\_{-}={\\frac
{1}{N\_{-}+2}}} for negative samples, y = -1.Here, N+ and N− are the
number of positive and negative samples, respectively. This
transformation follows by applying Bayes\' rule to a model of
out-of-sample data that has a uniform prior over the labels. The
constants 1 and 2, on the numerator and denominator respectively, are
derived from the application of Laplace smoothing. Platt himself
suggested using the Levenberg--Marquardt algorithm to optimize the
parameters, but a Newton algorithm was later proposed that should be
more numerically stable. Analysis Platt scaling has been shown to be
effective for SVMs as well as other types of classification models,
including boosted models and even naive Bayes classifiers, which produce
distorted probability distributions. It is particularly effective for
max-margin methods such as SVMs and boosted trees, which show sigmoidal
distortions in their predicted probabilities, but has less of an effect
with well-calibrated models such as logistic regression, multilayer
perceptrons, and random forests.An alternative approach to probability
calibration is to fit an isotonic regression model to an ill-calibrated
probability model. This has been shown to work better than Platt
scaling, in particular when enough training data is available. See also
Relevance vector machine: probabilistic alternative to the support
vector machine Notes == References ==
