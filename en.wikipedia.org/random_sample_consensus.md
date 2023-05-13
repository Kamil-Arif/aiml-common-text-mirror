Random sample consensus (RANSAC) is an iterative method to estimate
parameters of a mathematical model from a set of observed data that
contains outliers, when outliers are to be accorded no influence on the
values of the estimates. Therefore, it also can be interpreted as an
outlier detection method. It is a non-deterministic algorithm in the
sense that it produces a reasonable result only with a certain
probability, with this probability increasing as more iterations are
allowed. The algorithm was first published by Fischler and Bolles at SRI
International in 1981. They used RANSAC to solve the Location
Determination Problem (LDP), where the goal is to determine the points
in the space that project onto an image into a set of landmarks with
known locations. RANSAC uses repeated random sub-sampling. A basic
assumption is that the data consists of \"inliers\", i.e., data whose
distribution can be explained by some set of model parameters, though
may be subject to noise, and \"outliers\" which are data that do not fit
the model. The outliers can come, for example, from extreme values of
the noise or from erroneous measurements or incorrect hypotheses about
the interpretation of data. RANSAC also assumes that, given a (usually
small) set of inliers, there exists a procedure which can estimate the
parameters of a model that optimally explains or fits this data. Example
A simple example is fitting a line in two dimensions to a set of
observations. Assuming that this set contains both inliers, i.e., points
which approximately can be fitted to a line, and outliers, points which
cannot be fitted to this line, a simple least squares method for line
fitting will generally produce a line with a bad fit to the data
including inliers and outliers. The reason is that it is optimally
fitted to all points, including the outliers. RANSAC, on the other hand,
attempts to exclude the outliers and find a linear model that only uses
the inliers in its calculation. This is done by fitting linear models to
several random samplings of the data and returning the model that has
the best fit to a subset of the data. Since the inliers tend to be more
linearly related than a random mixture of inliers and outliers, a random
subset that consists entirely of inliers will have the best model fit.
In practice, there is no guarantee that a subset of inliers will be
randomly sampled, and the probability of the algorithm succeeding
depends on the proportion of inliers in the data as well as the choice
of several algorithm parameters. Overview The RANSAC algorithm is a
learning technique to estimate parameters of a model by random sampling
of observed data. Given a dataset whose data elements contain both
inliers and outliers, RANSAC uses the voting scheme to find the optimal
fitting result. Data elements in the dataset are used to vote for one or
multiple models. The implementation of this voting scheme is based on
two assumptions: that the noisy features will not vote consistently for
any single model (few outliers) and there are enough features to agree
on a good model (few missing data). The RANSAC algorithm is essentially
composed of two steps that are iteratively repeated: In the first step,
a sample subset containing minimal data items is randomly selected from
the input dataset. A fitting model with model parameters is computed
using only the elements of this sample subset. The cardinality of the
sample subset (e.g., the amount of data in this subset) is sufficient to
determine the model parameters. In the second step, the algorithm checks
which elements of the entire dataset are consistent with the model
instantiated by the estimated model parameters obtained from the first
step. A data element will be considered as an outlier if it does not fit
the model within some error threshold defining the maximum data
deviation of inliers. (Data elements beyond this deviation are
outliers.)The set of inliers obtained for the fitting model is called
the consensus set. The RANSAC algorithm will iteratively repeat the
above two steps until the obtained consensus set in certain iteration
has enough inliers. The input to the RANSAC algorithm is a set of
observed data values, a model to fit to the observations, and some
confidence parameters defining outliers. In more details than the
aforementioned RANSAC algorithm overview, RANSAC achieves its goal by
repeating the following steps: Select a random subset of the original
data. Call this subset the hypothetical inliers. A model is fitted to
the set of hypothetical inliers. All data are then tested against the
fitted model. All the data points (of the original data) that fit the
estimated model well, according to some model-specific loss function,
are called the consensus set (i.e., the set of inliers for the model).
The estimated model is reasonably good if sufficiently many data points
have been classified as a part of the consensus set. The model may be
improved by re-estimating it by using all the members of the consensus
set. The fitting quality as a measure of how well the model fits to the
consensus set will be used to sharpen the model fitting as iterations
goes on (e.g., by setting this measure as the fitting quality criteria
at the next iteration).To converge to a sufficiently good model
parameter set, this procedure is repeated a fixed number of times, each
time producing either the rejection of a model because too few points
are a part of the consensus set, or a refined model with a consensus set
size larger than the previous consensus set. Pseudocode The generic
RANSAC algorithm works as the following pseudocode: Given: data -- A set
of observations. model -- A model to explain the observed data points. n
-- The minimum number of data points required to estimate the model
parameters. k -- The maximum number of iterations allowed in the
algorithm. t -- A threshold value to determine data points that are fit
well by the model (inlier). d -- The number of close data points
(inliers) required to assert that the model fits well to the data.
Return: bestFit -- The model parameters which may best fit the data (or
null if no good model is found). iterations = 0 bestFit = null bestErr =
something really large // This parameter is used to sharpen the model
parameters to the best data fitting as iterations goes on. while
iterations \< k do maybeInliers := n randomly selected values from data
maybeModel := model parameters fitted to maybeInliers confirmedInliers
:= empty set for every point in data do if point fits maybeModel with an
error smaller than t then add point to confirmedInliers end if end for
if the number of elements in confirmedInliers is \> d then // This
implies that we may have found a good model. // Now test how good it is.
betterModel := model parameters fitted to all the points in
confirmedInliers thisErr := a measure of how well betterModel fits these
points if thisErr \< bestErr then bestFit := betterModel bestErr :=
thisErr end if end if increment iterations end while return bestFit
Example code A Python implementation mirroring the pseudocode. This also
defines a LinearRegressor based on least squares, applies RANSAC to a 2D
regression problem, and visualizes the outcome: Parameters The threshold
value to determine when a data point fits a model (t), and the number of
inliers (data points fitted to the model within t) required to assert
that the model fits well to data (d) are determined based on specific
requirements of the application and the dataset, and possibly based on
experimental evaluation. The number of iterations (k), however, can be
roughly determined as a function of the desired probability of success
(p) as shown below. Let p be the desired probability that the RANSAC
algorithm provides at least one useful result after running. In extreme
(for simplifying the derivation), RANSAC returns a successful result if
in some iteration it selects only inliers from the input data set when
it chooses n points from the data set from which the model parameters
are estimated. (In other words, all the selected n data points are
inliers of the model estimated by these points). Let w {\\displaystyle
w} be the probability of choosing an inlier each time a single data
point is selected, that is roughly, w {\\displaystyle w} = number of
inliers in data / number of points in dataA common case is that w
{\\displaystyle w} is not well known beforehand because of an unknown
number of inliers in data before running the RANSAC algorithm, but some
rough value can be given. With a given rough value of w {\\displaystyle
w} and roughly assuming that the n points needed for estimating a model
are selected independently (It is a rough assumption because each data
point selection reduces the number of data point candidates to choose in
the next selection in reality), w n {\\displaystyle w\^{n}} is the
probability that all n points are inliers and 1 − w n {\\displaystyle
1-w\^{n}} is the probability that at least one of the n points is an
outlier, a case which implies that a bad model will be estimated from
this point set. That probability to the power of k (the number of
iterations in running the algorithm) is the probability that the
algorithm never selects a set of n points which all are inliers, and
this is the same as 1 − p {\\displaystyle 1-p} (the probability that the
algorithm does not result in a successful model estimation) in extreme.
Consequently, 1 − p = ( 1 − w n ) k {\\displaystyle
1-p=(1-w\^{n})\^{k}\\,} which, after taking the logarithm of both sides,
leads to k = log ⁡ ( 1 − p ) log ⁡ ( 1 − w n ) {\\displaystyle k={\\frac
{\\log(1-p)}{\\log(1-w\^{n})}}} This result assumes that the n data
points are selected independently, that is, a point which has been
selected once is replaced and can be selected again in the same
iteration. This is often not a reasonable approach and the derived value
for k should be taken as an upper limit in the case that the points are
selected without replacement. For example, in the case of finding a line
which fits the data set illustrated in the above figure, the RANSAC
algorithm typically chooses two points in each iteration and computes
maybe_model as the line between the points and it is then critical that
the two points are distinct. To gain additional confidence, the standard
deviation or multiples thereof can be added to k. The standard deviation
of k is defined as SD ⁡ ( k ) = 1 − w n w n {\\displaystyle
\\operatorname {SD} (k)={\\frac {\\sqrt {1-w\^{n}}}{w\^{n}}}} Advantages
and disadvantages An advantage of RANSAC is its ability to do robust
estimation of the model parameters, i.e., it can estimate the parameters
with a high degree of accuracy even when a significant number of
outliers are present in the data set. A disadvantage of RANSAC is that
there is no upper bound on the time it takes to compute these parameters
(except exhaustion). When the number of iterations computed is limited
the solution obtained may not be optimal, and it may not even be one
that fits the data in a good way. In this way RANSAC offers a trade-off;
by computing a greater number of iterations the probability of a
reasonable model being produced is increased. Moreover, RANSAC is not
always able to find the optimal set even for moderately contaminated
sets and it usually performs badly when the number of inliers is less
than 50%. Optimal RANSAC was proposed to handle both these problems and
is capable of finding the optimal set for heavily contaminated sets,
even for an inlier ratio under 5%. Another disadvantage of RANSAC is
that it requires the setting of problem-specific thresholds. RANSAC can
only estimate one model for a particular data set. As for any one-model
approach when two (or more) model instances exist, RANSAC may fail to
find either one. The Hough transform is one alternative robust
estimation technique that may be useful when more than one model
instance is present. Another approach for multi model fitting is known
as PEARL, which combines model sampling from data points as in RANSAC
with iterative re-estimation of inliers and the multi-model fitting
being formulated as an optimization problem with a global energy
function describing the quality of the overall solution. Applications
The RANSAC algorithm is often used in computer vision, e.g., to
simultaneously solve the correspondence problem and estimate the
fundamental matrix related to a pair of stereo cameras; see also:
Structure from motion, scale-invariant feature transform, image
stitching, rigid motion segmentation. Development and improvements Since
1981 RANSAC has become a fundamental tool in the computer vision and
image processing community. In 2006, for the 25th anniversary of the
algorithm, a workshop was organized at the International Conference on
Computer Vision and Pattern Recognition (CVPR) to summarize the most
recent contributions and variations to the original algorithm, mostly
meant to improve the speed of the algorithm, the robustness and accuracy
of the estimated solution and to decrease the dependency from user
defined constants. RANSAC can be sensitive to the choice of the correct
noise threshold that defines which data points fit a model instantiated
with a certain set of parameters. If such threshold is too large, then
all the hypotheses tend to be ranked equally (good). On the other hand,
when the noise threshold is too small, the estimated parameters tend to
be unstable ( i.e. by simply adding or removing a datum to the set of
inliers, the estimate of the parameters may fluctuate). To partially
compensate for this undesirable effect, Torr et al. proposed two
modification of RANSAC called MSAC (M-estimator SAmple and Consensus)
and MLESAC (Maximum Likelihood Estimation SAmple and Consensus). The
main idea is to evaluate the quality of the consensus set ( i.e. the
data that fit a model and a certain set of parameters) calculating its
likelihood (whereas in the original formulation by Fischler and Bolles
the rank was the cardinality of such set). An extension to MLESAC which
takes into account the prior probabilities associated to the input
dataset is proposed by Tordoff. The resulting algorithm is dubbed
Guided-MLESAC. Along similar lines, Chum proposed to guide the sampling
procedure if some a priori information regarding the input data is
known, i.e. whether a datum is likely to be an inlier or an outlier. The
proposed approach is called PROSAC, PROgressive SAmple Consensus.Chum et
al. also proposed a randomized version of RANSAC called R-RANSAC to
reduce the computational burden to identify a good consensus set. The
basic idea is to initially evaluate the goodness of the currently
instantiated model using only a reduced set of points instead of the
entire dataset. A sound strategy will tell with high confidence when it
is the case to evaluate the fitting of the entire dataset or when the
model can be readily discarded. It is reasonable to think that the
impact of this approach is more relevant in cases where the percentage
of inliers is large. The type of strategy proposed by Chum et al. is
called preemption scheme. Nistér proposed a paradigm called Preemptive
RANSAC that allows real time robust estimation of the structure of a
scene and of the motion of the camera. The core idea of the approach
consists in generating a fixed number of hypothesis so that the
comparison happens with respect to the quality of the generated
hypothesis rather than against some absolute quality metric. Other
researchers tried to cope with difficult situations where the noise
scale is not known and/or multiple model instances are present. The
first problem has been tackled in the work by Wang and Suter. Toldo et
al. represent each datum with the characteristic function of the set of
random models that fit the point. Then multiple models are revealed as
clusters which group the points supporting the same model. The
clustering algorithm, called J-linkage, does not require prior
specification of the number of models, nor does it necessitate manual
parameters tuning.RANSAC has also been tailored for recursive state
estimation applications, where the input measurements are corrupted by
outliers and Kalman filter approaches, which rely on a Gaussian
distribution of the measurement error, are doomed to fail. Such an
approach is dubbed KALMANSAC. Related methods MLESAC (Maximum Likelihood
Estimate Sample Consensus) -- maximizes the likelihood that the data was
generated from the sample-fitted model, e.g. a mixture model of inliers
and outliers MAPSAC (Maximum A Posterior Sample Consensus) -- extends
MLESAC to incorporate a prior probability of the parameters to be fitted
and maximizes the posterior probability KALMANSAC -- causal inference of
the state of a dynamical system Resampling (statistics) Hop-Diffusion
Monte Carlo uses randomized sampling involve global jumps and local
diffusion to choose the sample at each step of RANSAC for epipolar
geometry estimation between very wide-baseline images. See also Hough
transform Notes References Martin A. Fischler & Robert C. Bolles (June
1981). \"Random Sample Consensus: A Paradigm for Model Fitting with
Applications to Image Analysis and Automated Cartography\" (PDF). Comm.
ACM. 24 (6): 381--395. doi:10.1145/358669.358692. S2CID 972888. Archived
(PDF) from the original on December 10, 2014. David A. Forsyth & Jean
Ponce (2003). Computer Vision, a modern approach. Prentice Hall. ISBN
978-0-13-085198-7. Richard Hartley and Andrew Zisserman (2003). Multiple
View Geometry in Computer Vision (2nd ed.). Cambridge University Press.
Strutz, T. (2016). Data Fitting and Uncertainty (A practical
introduction to weighted least squares and beyond). 2nd edition,
Springer Vieweg. ISBN 978-3-658-11455-8. P.H.S. Torr & D.W. Murray
(1997). \"The Development and Comparison of Robust Methods for
Estimating the Fundamental Matrix\". International Journal of Computer
Vision. 24 (3): 271--300. doi:10.1023/A:1007927408552. S2CID 12031059.
Ondrej Chum (2005). \"Two-View Geometry Estimation by Random Sample and
Consensus\" (PDF). PhD Thesis. Sunglok Choi; Taemin Kim & Wonpil Yu
(2009). \"Performance Evaluation of RANSAC Family\" (PDF). In
Proceedings of the British Machine Vision Conference (BMVC).Anders Hast;
Johan Nysjö; Andrea Marchetti (2013). \"Optimal RANSAC -- Towards a
Repeatable Algorithm for Finding the Optimal Set\" (PDF). Journal of
WSCG. 21 (1): 21--30. Hossam Isack; Yuri Boykov (2012). \"Energy-based
Geometric Multi-Model Fitting\" (PDF). International Journal of Computer
Vision. 97 (2: 1): 23--147. CiteSeerX 10.1.1.381.2434.
doi:10.1007/s11263-011-0474-7. S2CID 5461268.
