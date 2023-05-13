Linear discriminant analysis (LDA), normal discriminant analysis (NDA),
or discriminant function analysis is a generalization of Fisher\'s
linear discriminant, a method used in statistics and other fields, to
find a linear combination of features that characterizes or separates
two or more classes of objects or events. The resulting combination may
be used as a linear classifier, or, more commonly, for dimensionality
reduction before later classification. LDA is closely related to
analysis of variance (ANOVA) and regression analysis, which also attempt
to express one dependent variable as a linear combination of other
features or measurements. However, ANOVA uses categorical independent
variables and a continuous dependent variable, whereas discriminant
analysis has continuous independent variables and a categorical
dependent variable (i.e. the class label). Logistic regression and
probit regression are more similar to LDA than ANOVA is, as they also
explain a categorical variable by the values of continuous independent
variables. These other methods are preferable in applications where it
is not reasonable to assume that the independent variables are normally
distributed, which is a fundamental assumption of the LDA method. LDA is
also closely related to principal component analysis (PCA) and factor
analysis in that they both look for linear combinations of variables
which best explain the data. LDA explicitly attempts to model the
difference between the classes of data. PCA, in contrast, does not take
into account any difference in class, and factor analysis builds the
feature combinations based on differences rather than similarities.
Discriminant analysis is also different from factor analysis in that it
is not an interdependence technique: a distinction between independent
variables and dependent variables (also called criterion variables) must
be made. LDA works when the measurements made on independent variables
for each observation are continuous quantities. When dealing with
categorical independent variables, the equivalent technique is
discriminant correspondence analysis.Discriminant analysis is used when
groups are known a priori (unlike in cluster analysis). Each case must
have a score on one or more quantitative predictor measures, and a score
on a group measure. In simple terms, discriminant function analysis is
classification - the act of distributing things into groups, classes or
categories of the same type. History The original dichotomous
discriminant analysis was developed by Sir Ronald Fisher in 1936. It is
different from an ANOVA or MANOVA, which is used to predict one (ANOVA)
or multiple (MANOVA) continuous dependent variables by one or more
independent categorical variables. Discriminant function analysis is
useful in determining whether a set of variables is effective in
predicting category membership. LDA for two classes Consider a set of
observations x → {\\displaystyle {\\vec {x}}} (also called features,
attributes, variables or measurements) for each sample of an object or
event with known class y {\\displaystyle y} . This set of samples is
called the training set. The classification problem is then to find a
good predictor for the class y {\\displaystyle y} of any sample of the
same distribution (not necessarily from the training set) given only an
observation x → {\\displaystyle {\\vec {x}}} .: 338 LDA approaches the
problem by assuming that the conditional probability density functions p
( x → \| y = 0 ) {\\displaystyle p({\\vec {x}}\|y=0)} and p ( x → \| y =
1 ) {\\displaystyle p({\\vec {x}}\|y=1)} are both the normal
distribution with mean and covariance parameters ( μ → 0 , Σ 0 )
{\\displaystyle \\left({\\vec {\\mu }}\_{0},\\Sigma \_{0}\\right)} and (
μ → 1 , Σ 1 ) {\\displaystyle \\left({\\vec {\\mu }}\_{1},\\Sigma
\_{1}\\right)} , respectively. Under this assumption, the Bayes-optimal
solution is to predict points as being from the second class if the log
of the likelihood ratios is bigger than some threshold T, so that: ( x →
− μ → 0 ) T Σ 0 − 1 ( x → − μ → 0 ) + ln ⁡ \| Σ 0 \| − ( x → − μ → 1 ) T
Σ 1 − 1 ( x → − μ → 1 ) − ln ⁡ \| Σ 1 \| \> T {\\displaystyle ({\\vec
{x}}-{\\vec {\\mu }}\_{0})\^{\\mathrm {T} }\\Sigma \_{0}\^{-1}({\\vec
{x}}-{\\vec {\\mu }}\_{0})+\\ln \|\\Sigma \_{0}\|-({\\vec {x}}-{\\vec
{\\mu }}\_{1})\^{\\mathrm {T} }\\Sigma \_{1}\^{-1}({\\vec {x}}-{\\vec
{\\mu }}\_{1})-\\ln \|\\Sigma \_{1}\|\\ \>\\ T} Without any further
assumptions, the resulting classifier is referred to as quadratic
discriminant analysis (QDA). LDA instead makes the additional
simplifying homoscedasticity assumption (i.e. that the class covariances
are identical, so Σ 0 = Σ 1 = Σ {\\displaystyle \\Sigma \_{0}=\\Sigma
\_{1}=\\Sigma } ) and that the covariances have full rank. In this case,
several terms cancel: x → T Σ 0 − 1 x → = x → T Σ 1 − 1 x →
{\\displaystyle {\\vec {x}}\^{\\mathrm {T} }\\Sigma \_{0}\^{-1}{\\vec
{x}}={\\vec {x}}\^{\\mathrm {T} }\\Sigma \_{1}\^{-1}{\\vec {x}}} x → T Σ
i − 1 μ → i = μ → i T Σ i − 1 x → {\\displaystyle {\\vec {x}}\^{\\mathrm
{T} }{\\Sigma \_{i}}\^{-1}{\\vec {\\mu }}\_{i}={{\\vec {\\mu
}}\_{i}}\^{\\mathrm {T} }{\\Sigma \_{i}}\^{-1}{\\vec {x}}} because Σ i
{\\displaystyle \\Sigma \_{i}} is Hermitianand the above decision
criterion becomes a threshold on the dot product w → T x → \> c
{\\displaystyle {\\vec {w}}\^{\\mathrm {T} }{\\vec {x}}\>c} for some
threshold constant c, where w → = Σ − 1 ( μ → 1 − μ → 0 )
{\\displaystyle {\\vec {w}}=\\Sigma \^{-1}({\\vec {\\mu }}\_{1}-{\\vec
{\\mu }}\_{0})} c = 1 2 w → T ( μ → 1 + μ → 0 ) {\\displaystyle
c={\\frac {1}{2}}\\,{\\vec {w}}\^{\\mathrm {T} }({\\vec {\\mu
}}\_{1}+{\\vec {\\mu }}\_{0})} This means that the criterion of an input
x → {\\displaystyle {\\vec {x}}} being in a class y {\\displaystyle y}
is purely a function of this linear combination of the known
observations. It is often useful to see this conclusion in geometrical
terms: the criterion of an input x → {\\displaystyle {\\vec {x}}} being
in a class y {\\displaystyle y} is purely a function of projection of
multidimensional-space point x → {\\displaystyle {\\vec {x}}} onto
vector w → {\\displaystyle {\\vec {w}}} (thus, we only consider its
direction). In other words, the observation belongs to y {\\displaystyle
y} if corresponding x → {\\displaystyle {\\vec {x}}} is located on a
certain side of a hyperplane perpendicular to w → {\\displaystyle {\\vec
{w}}} . The location of the plane is defined by the threshold c
{\\displaystyle c} . Assumptions The assumptions of discriminant
analysis are the same as those for MANOVA. The analysis is quite
sensitive to outliers and the size of the smallest group must be larger
than the number of predictor variables. Multivariate normality:
Independent variables are normal for each level of the grouping
variable. Homogeneity of variance/covariance (homoscedasticity):
Variances among group variables are the same across levels of
predictors. Can be tested with Box\'s M statistic. It has been
suggested, however, that linear discriminant analysis be used when
covariances are equal, and that quadratic discriminant analysis may be
used when covariances are not equal. Multicollinearity: Predictive power
can decrease with an increased correlation between predictor variables.
Independence: Participants are assumed to be randomly sampled, and a
participant\'s score on one variable is assumed to be independent of
scores on that variable for all other participants.It has been suggested
that discriminant analysis is relatively robust to slight violations of
these assumptions, and it has also been shown that discriminant analysis
may still be reliable when using dichotomous variables (where
multivariate normality is often violated). Discriminant functions
Discriminant analysis works by creating one or more linear combinations
of predictors, creating a new latent variable for each function. These
functions are called discriminant functions. The number of functions
possible is either N g − 1 {\\displaystyle N\_{g}-1} where N g
{\\displaystyle N\_{g}} = number of groups, or p {\\displaystyle p} (the
number of predictors), whichever is smaller. The first function created
maximizes the differences between groups on that function. The second
function maximizes differences on that function, but also must not be
correlated with the previous function. This continues with subsequent
functions with the requirement that the new function not be correlated
with any of the previous functions. Given group j {\\displaystyle j} ,
with R j {\\displaystyle \\mathbb {R} \_{j}} sets of sample space, there
is a discriminant rule such that if x ∈ R j {\\displaystyle x\\in
\\mathbb {R} \_{j}} , then x ∈ j {\\displaystyle x\\in j} . Discriminant
analysis then, finds "good" regions of R j {\\displaystyle \\mathbb {R}
\_{j}} to minimize classification error, therefore leading to a high
percent correct classified in the classification table.Each function is
given a discriminant score to determine how well it predicts group
placement. Structure Correlation Coefficients: The correlation between
each predictor and the discriminant score of each function. This is a
zero-order correlation (i.e., not corrected for the other predictors).
Standardized Coefficients: Each predictor\'s weight in the linear
combination that is the discriminant function. Like in a regression
equation, these coefficients are partial (i.e., corrected for the other
predictors). Indicates the unique contribution of each predictor in
predicting group assignment. Functions at Group Centroids: Mean
discriminant scores for each grouping variable are given for each
function. The farther apart the means are, the less error there will be
in classification. Discrimination rules Maximum likelihood: Assigns x
{\\displaystyle x} to the group that maximizes population (group)
density. Bayes Discriminant Rule: Assigns x {\\displaystyle x} to the
group that maximizes π i f i ( x ) {\\displaystyle \\pi \_{i}f\_{i}(x)}
, where πi represents the prior probability of that classification, and
f i ( x ) {\\displaystyle f\_{i}(x)} represents the population density.
Fisher\'s linear discriminant rule: Maximizes the ratio between
SSbetween and SSwithin, and finds a linear combination of the predictors
to predict group. Eigenvalues An eigenvalue in discriminant analysis is
the characteristic root of each function. It is an indication of how
well that function differentiates the groups, where the larger the
eigenvalue, the better the function differentiates. This however, should
be interpreted with caution, as eigenvalues have no upper limit. The
eigenvalue can be viewed as a ratio of SSbetween and SSwithin as in
ANOVA when the dependent variable is the discriminant function, and the
groups are the levels of the IV. This means that the largest eigenvalue
is associated with the first function, the second largest with the
second, etc.. Effect size Some suggest the use of eigenvalues as effect
size measures, however, this is generally not supported. Instead, the
canonical correlation is the preferred measure of effect size. It is
similar to the eigenvalue, but is the square root of the ratio of
SSbetween and SStotal. It is the correlation between groups and the
function. Another popular measure of effect size is the percent of
variance for each function. This is calculated by: (λx/Σλi) X 100 where
λx is the eigenvalue for the function and Σλi is the sum of all
eigenvalues. This tells us how strong the prediction is for that
particular function compared to the others. Percent correctly classified
can also be analyzed as an effect size. The kappa value can describe
this while correcting for chance agreement.Kappa normalizes across all
categorizes rather than biased by a significantly good or poorly
performing classes. Canonical discriminant analysis for k classes
Canonical discriminant analysis (CDA) finds axes (k − 1 canonical
coordinates, k being the number of classes) that best separate the
categories. These linear functions are uncorrelated and define, in
effect, an optimal k − 1 space through the n-dimensional cloud of data
that best separates (the projections in that space of) the k groups. See
"Multiclass LDA" for details below. Fisher\'s linear discriminant The
terms Fisher\'s linear discriminant and LDA are often used
interchangeably, although Fisher\'s original article actually describes
a slightly different discriminant, which does not make some of the
assumptions of LDA such as normally distributed classes or equal class
covariances. Suppose two classes of observations have means μ → 0 , μ →
1 {\\displaystyle {\\vec {\\mu }}\_{0},{\\vec {\\mu }}\_{1}} and
covariances Σ 0 , Σ 1 {\\displaystyle \\Sigma \_{0},\\Sigma \_{1}} .
Then the linear combination of features w → T x → {\\displaystyle {\\vec
{w}}\^{\\mathrm {T} }{\\vec {x}}} will have means w → T μ → i
{\\displaystyle {\\vec {w}}\^{\\mathrm {T} }{\\vec {\\mu }}\_{i}} and
variances w → T Σ i w → {\\displaystyle {\\vec {w}}\^{\\mathrm {T}
}\\Sigma \_{i}{\\vec {w}}} for i = 0 , 1 {\\displaystyle i=0,1} . Fisher
defined the separation between these two distributions to be the ratio
of the variance between the classes to the variance within the classes:
S = σ between 2 σ within 2 = ( w → ⋅ μ → 1 − w → ⋅ μ → 0 ) 2 w → T Σ 1 w
→ + w → T Σ 0 w → = ( w → ⋅ ( μ → 1 − μ → 0 ) ) 2 w → T ( Σ 0 + Σ 1 ) w
→ {\\displaystyle S={\\frac {\\sigma \_{\\text{between}}\^{2}}{\\sigma
\_{\\text{within}}\^{2}}}={\\frac {({\\vec {w}}\\cdot {\\vec {\\mu
}}\_{1}-{\\vec {w}}\\cdot {\\vec {\\mu }}\_{0})\^{2}}{{\\vec
{w}}\^{\\mathrm {T} }\\Sigma \_{1}{\\vec {w}}+{\\vec {w}}\^{\\mathrm {T}
}\\Sigma \_{0}{\\vec {w}}}}={\\frac {({\\vec {w}}\\cdot ({\\vec {\\mu
}}\_{1}-{\\vec {\\mu }}\_{0}))\^{2}}{{\\vec {w}}\^{\\mathrm {T}
}(\\Sigma \_{0}+\\Sigma \_{1}){\\vec {w}}}}} This measure is, in some
sense, a measure of the signal-to-noise ratio for the class labelling.
It can be shown that the maximum separation occurs when w → ∝ ( Σ 0 + Σ
1 ) − 1 ( μ → 1 − μ → 0 ) {\\displaystyle {\\vec {w}}\\propto (\\Sigma
\_{0}+\\Sigma \_{1})\^{-1}({\\vec {\\mu }}\_{1}-{\\vec {\\mu }}\_{0})}
When the assumptions of LDA are satisfied, the above equation is
equivalent to LDA. Be sure to note that the vector w → {\\displaystyle
{\\vec {w}}} is the normal to the discriminant hyperplane. As an
example, in a two dimensional problem, the line that best divides the
two groups is perpendicular to w → {\\displaystyle {\\vec {w}}} .
Generally, the data points to be discriminated are projected onto w →
{\\displaystyle {\\vec {w}}} ; then the threshold that best separates
the data is chosen from analysis of the one-dimensional distribution.
There is no general rule for the threshold. However, if projections of
points from both classes exhibit approximately the same distributions, a
good choice would be the hyperplane between projections of the two
means, w → ⋅ μ → 0 {\\displaystyle {\\vec {w}}\\cdot {\\vec {\\mu
}}\_{0}} and w → ⋅ μ → 1 {\\displaystyle {\\vec {w}}\\cdot {\\vec {\\mu
}}\_{1}} . In this case the parameter c in threshold condition w → ⋅ x →
\> c {\\displaystyle {\\vec {w}}\\cdot {\\vec {x}}\>c} can be found
explicitly: c = w → ⋅ 1 2 ( μ → 0 + μ → 1 ) = 1 2 μ → 1 T Σ 1 − 1 μ → 1
− 1 2 μ → 0 T Σ 0 − 1 μ → 0 {\\displaystyle c={\\vec {w}}\\cdot {\\frac
{1}{2}}({\\vec {\\mu }}\_{0}+{\\vec {\\mu }}\_{1})={\\frac {1}{2}}{\\vec
{\\mu }}\_{1}\^{\\mathrm {T} }\\Sigma \_{1}\^{-1}{\\vec {\\mu
}}\_{1}-{\\frac {1}{2}}{\\vec {\\mu }}\_{0}\^{\\mathrm {T} }\\Sigma
\_{0}\^{-1}{\\vec {\\mu }}\_{0}} .Otsu\'s method is related to Fisher\'s
linear discriminant, and was created to binarize the histogram of pixels
in a grayscale image by optimally picking the black/white threshold that
minimizes intra-class variance and maximizes inter-class variance
within/between grayscales assigned to black and white pixel classes.
Multiclass LDA In the case where there are more than two classes, the
analysis used in the derivation of the Fisher discriminant can be
extended to find a subspace which appears to contain all of the class
variability. This generalization is due to C. R. Rao. Suppose that each
of C classes has a mean μ i {\\displaystyle \\mu \_{i}} and the same
covariance Σ {\\displaystyle \\Sigma } . Then the scatter between class
variability may be defined by the sample covariance of the class means Σ
b = 1 C ∑ i = 1 C ( μ i − μ ) ( μ i − μ ) T {\\displaystyle \\Sigma
\_{b}={\\frac {1}{C}}\\sum \_{i=1}\^{C}(\\mu \_{i}-\\mu )(\\mu
\_{i}-\\mu )\^{\\mathrm {T} }} where μ {\\displaystyle \\mu } is the
mean of the class means. The class separation in a direction w →
{\\displaystyle {\\vec {w}}} in this case will be given by S = w → T Σ b
w → w → T Σ w → {\\displaystyle S={\\frac {{\\vec {w}}\^{\\mathrm {T}
}\\Sigma \_{b}{\\vec {w}}}{{\\vec {w}}\^{\\mathrm {T} }\\Sigma {\\vec
{w}}}}} This means that when w → {\\displaystyle {\\vec {w}}} is an
eigenvector of Σ − 1 Σ b {\\displaystyle \\Sigma \^{-1}\\Sigma \_{b}}
the separation will be equal to the corresponding eigenvalue. If Σ − 1 Σ
b {\\displaystyle \\Sigma \^{-1}\\Sigma \_{b}} is diagonalizable, the
variability between features will be contained in the subspace spanned
by the eigenvectors corresponding to the C − 1 largest eigenvalues
(since Σ b {\\displaystyle \\Sigma \_{b}} is of rank C − 1 at most).
These eigenvectors are primarily used in feature reduction, as in PCA.
The eigenvectors corresponding to the smaller eigenvalues will tend to
be very sensitive to the exact choice of training data, and it is often
necessary to use regularisation as described in the next section. If
classification is required, instead of dimension reduction, there are a
number of alternative techniques available. For instance, the classes
may be partitioned, and a standard Fisher discriminant or LDA used to
classify each partition. A common example of this is \"one against the
rest\" where the points from one class are put in one group, and
everything else in the other, and then LDA applied. This will result in
C classifiers, whose results are combined. Another common method is
pairwise classification, where a new classifier is created for each pair
of classes (giving C(C − 1)/2 classifiers in total), with the individual
classifiers combined to produce a final classification. Incremental LDA
The typical implementation of the LDA technique requires that all the
samples are available in advance. However, there are situations where
the entire data set is not available and the input data are observed as
a stream. In this case, it is desirable for the LDA feature extraction
to have the ability to update the computed LDA features by observing the
new samples without running the algorithm on the whole data set. For
example, in many real-time applications such as mobile robotics or
on-line face recognition, it is important to update the extracted LDA
features as soon as new observations are available. An LDA feature
extraction technique that can update the LDA features by simply
observing new samples is an incremental LDA algorithm, and this idea has
been extensively studied over the last two decades. Chatterjee and
Roychowdhury proposed an incremental self-organized LDA algorithm for
updating the LDA features. In other work, Demir and Ozmehmet proposed
online local learning algorithms for updating LDA features incrementally
using error-correcting and the Hebbian learning rules. Later, Aliyari et
al. derived fast incremental algorithms to update the LDA features by
observing the new samples. Practical use In practice, the class means
and covariances are not known. They can, however, be estimated from the
training set. Either the maximum likelihood estimate or the maximum a
posteriori estimate may be used in place of the exact value in the above
equations. Although the estimates of the covariance may be considered
optimal in some sense, this does not mean that the resulting
discriminant obtained by substituting these values is optimal in any
sense, even if the assumption of normally distributed classes is
correct. Another complication in applying LDA and Fisher\'s discriminant
to real data occurs when the number of measurements of each sample
(i.e., the dimensionality of each data vector) exceeds the number of
samples in each class. In this case, the covariance estimates do not
have full rank, and so cannot be inverted. There are a number of ways to
deal with this. One is to use a pseudo inverse instead of the usual
matrix inverse in the above formulae. However, better numeric stability
may be achieved by first projecting the problem onto the subspace
spanned by Σ b {\\displaystyle \\Sigma \_{b}} . Another strategy to deal
with small sample size is to use a shrinkage estimator of the covariance
matrix, which can be expressed mathematically as Σ = ( 1 − λ ) Σ + λ I
{\\displaystyle \\Sigma =(1-\\lambda )\\Sigma +\\lambda I\\,} where I
{\\displaystyle I} is the identity matrix, and λ {\\displaystyle
\\lambda } is the shrinkage intensity or regularisation parameter. This
leads to the framework of regularized discriminant analysis or shrinkage
discriminant analysis.Also, in many practical cases linear discriminants
are not suitable. LDA and Fisher\'s discriminant can be extended for use
in non-linear classification via the kernel trick. Here, the original
observations are effectively mapped into a higher dimensional non-linear
space. Linear classification in this non-linear space is then equivalent
to non-linear classification in the original space. The most commonly
used example of this is the kernel Fisher discriminant. LDA can be
generalized to multiple discriminant analysis, where c becomes a
categorical variable with N possible states, instead of only two.
Analogously, if the class-conditional densities p ( x → ∣ c = i )
{\\displaystyle p({\\vec {x}}\\mid c=i)} are normal with shared
covariances, the sufficient statistic for P ( c ∣ x → ) {\\displaystyle
P(c\\mid {\\vec {x}})} are the values of N projections, which are the
subspace spanned by the N means, affine projected by the inverse
covariance matrix. These projections can be found by solving a
generalized eigenvalue problem, where the numerator is the covariance
matrix formed by treating the means as the samples, and the denominator
is the shared covariance matrix. See "Multiclass LDA" above for details.
Applications In addition to the examples given below, LDA is applied in
positioning and product management. Bankruptcy prediction In bankruptcy
prediction based on accounting ratios and other financial variables,
linear discriminant analysis was the first statistical method applied to
systematically explain which firms entered bankruptcy vs. survived.
Despite limitations including known nonconformance of accounting ratios
to the normal distribution assumptions of LDA, Edward Altman\'s 1968
model is still a leading model in practical applications. Face
recognition In computerised face recognition, each face is represented
by a large number of pixel values. Linear discriminant analysis is
primarily used here to reduce the number of features to a more
manageable number before classification. Each of the new dimensions is a
linear combination of pixel values, which form a template. The linear
combinations obtained using Fisher\'s linear discriminant are called
Fisher faces, while those obtained using the related principal component
analysis are called eigenfaces. Marketing In marketing, discriminant
analysis was once often used to determine the factors which distinguish
different types of customers and/or products on the basis of surveys or
other forms of collected data. Logistic regression or other methods are
now more commonly used. The use of discriminant analysis in marketing
can be described by the following steps: Formulate the problem and
gather data---Identify the salient attributes consumers use to evaluate
products in this category---Use quantitative marketing research
techniques (such as surveys) to collect data from a sample of potential
customers concerning their ratings of all the product attributes. The
data collection stage is usually done by marketing research
professionals. Survey questions ask the respondent to rate a product
from one to five (or 1 to 7, or 1 to 10) on a range of attributes chosen
by the researcher. Anywhere from five to twenty attributes are chosen.
They could include things like: ease of use, weight, accuracy,
durability, colourfulness, price, or size. The attributes chosen will
vary depending on the product being studied. The same question is asked
about all the products in the study. The data for multiple products is
codified and input into a statistical program such as R, SPSS or SAS.
(This step is the same as in Factor analysis). Estimate the Discriminant
Function Coefficients and determine the statistical significance and
validity---Choose the appropriate discriminant analysis method. The
direct method involves estimating the discriminant function so that all
the predictors are assessed simultaneously. The stepwise method enters
the predictors sequentially. The two-group method should be used when
the dependent variable has two categories or states. The multiple
discriminant method is used when the dependent variable has three or
more categorical states. Use Wilks\'s Lambda to test for significance in
SPSS or F stat in SAS. The most common method used to test validity is
to split the sample into an estimation or analysis sample, and a
validation or holdout sample. The estimation sample is used in
constructing the discriminant function. The validation sample is used to
construct a classification matrix which contains the number of correctly
classified and incorrectly classified cases. The percentage of correctly
classified cases is called the hit ratio. Plot the results on a two
dimensional map, define the dimensions, and interpret the results. The
statistical program (or a related module) will map the results. The map
will plot each product (usually in two-dimensional space). The distance
of products to each other indicate either how different they are. The
dimensions must be labelled by the researcher. This requires subjective
judgement and is often very challenging. See perceptual mapping.
Biomedical studies The main application of discriminant analysis in
medicine is the assessment of severity state of a patient and prognosis
of disease outcome. For example, during retrospective analysis, patients
are divided into groups according to severity of disease -- mild,
moderate and severe form. Then results of clinical and laboratory
analyses are studied in order to reveal variables which are
statistically different in studied groups. Using these variables,
discriminant functions are built which help to objectively classify
disease in a future patient into mild, moderate or severe form. In
biology, similar principles are used in order to classify and define
groups of different biological objects, for example, to define phage
types of Salmonella enteritidis based on Fourier transform infrared
spectra, to detect animal source of Escherichia coli studying its
virulence factors etc. Earth science This method can be used to separate
the alteration zones. For example, when different data from various
zones are available, discriminant analysis can find the pattern within
the data and classify it effectively. Comparison to logistic regression
Discriminant function analysis is very similar to logistic regression,
and both can be used to answer the same research questions. Logistic
regression does not have as many assumptions and restrictions as
discriminant analysis. However, when discriminant analysis' assumptions
are met, it is more powerful than logistic regression. Unlike logistic
regression, discriminant analysis can be used with small sample sizes.
It has been shown that when sample sizes are equal, and homogeneity of
variance/covariance holds, discriminant analysis is more accurate.
Despite all these advantages, logistic regression has none-the-less
become the common choice, since the assumptions of discriminant analysis
are rarely met. Linear discriminant in high dimension Geometric
anomalies in higher dimensions lead to the well-known curse of
dimensionality. Nevertheless, proper utilization of concentration of
measure phenomena can make computation easier. An important case of
these blessing of dimensionality phenomena was highlighted by Donoho and
Tanner: if a sample is essentially high-dimensional then each point can
be separated from the rest of the sample by linear inequality, with high
probability, even for exponentially large samples. These linear
inequalities can be selected in the standard (Fisher\'s) form of the
linear discriminant for a rich family of probability distribution. In
particular, such theorems are proven for log-concave distributions
including multidimensional normal distribution (the proof is based on
the concentration inequalities for log-concave measures) and for product
measures on a multidimensional cube (this is proven using Talagrand\'s
concentration inequality for product probability spaces). Data
separability by classical linear discriminants simplifies the problem of
error correction for artificial intelligence systems in high dimension.
See also Data mining Decision tree learning Factor analysis Kernel
Fisher discriminant analysis Logit (for logistic regression) Linear
regression Multiple discriminant analysis Multidimensional scaling
Pattern recognition Preference regression Quadratic classifier
Statistical classification References Further reading Duda, R. O.; Hart,
P. E.; Stork, D. H. (2000). Pattern Classification (2nd ed.). Wiley
Interscience. ISBN 978-0-471-05669-0. MR 1802993. Hilbe, J. M. (2009).
Logistic Regression Models. Chapman & Hall/CRC Press. ISBN
978-1-4200-7575-5. Mika, S.; et al. (1999). \"Fisher Discriminant
Analysis with Kernels\". Neural Networks for Signal Processing IX:
Proceedings of the 1999 IEEE Signal Processing Society Workshop (Cat.
No.98TH8468). IEEE Conference on Neural Networks for Signal Processing
IX. pp. 41--48. CiteSeerX 10.1.1.35.9904. doi:10.1109/NNSP.1999.788121.
ISBN 978-0-7803-5673-3. S2CID 8473401. McFarland, H. Richard; Donald,
St. P. Richards (2001). \"Exact Misclassification Probabilities for
Plug-In Normal Quadratic Discriminant Functions. I. The Equal-Means
Case\". Journal of Multivariate Analysis. 77 (1): 21--53.
doi:10.1006/jmva.2000.1924. McFarland, H. Richard; Donald, St. P.
Richards (2002). \"Exact Misclassification Probabilities for Plug-In
Normal Quadratic Discriminant Functions. II. The Heterogeneous Case\".
Journal of Multivariate Analysis. 82 (2): 299--330.
doi:10.1006/jmva.2001.2034. Haghighat, M.; Abdel-Mottaleb, M.; Alhalabi,
W. (2016). \"Discriminant Correlation Analysis: Real-Time Feature Level
Fusion for Multimodal Biometric Recognition\". IEEE Transactions on
Information Forensics and Security. 11 (9): 1984--1996.
doi:10.1109/TIFS.2016.2569061. S2CID 15624506. External links
Discriminant Correlation Analysis (DCA) of the Haghighat article (see
above) ALGLIB contains open-source LDA implementation in C# / C++ /
Pascal / VBA. LDA in Python- LDA implementation in Python LDA tutorial
using MS Excel Biomedical statistics. Discriminant analysis StatQuest:
Linear Discriminant Analysis (LDA) clearly explained on YouTube Course
notes, Discriminant function analysis by G. David Garson, NC State
University Discriminant analysis tutorial in Microsoft Excel by Kardi
Teknomo Course notes, Discriminant function analysis by David W.
Stockburger, Missouri State University Discriminant function analysis
(DA) by John Poulsen and Aaron French, San Francisco State University
