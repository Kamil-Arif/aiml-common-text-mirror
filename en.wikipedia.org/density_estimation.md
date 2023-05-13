In statistics, probability density estimation or simply density
estimation is the construction of an estimate, based on observed data,
of an unobservable underlying probability density function. The
unobservable density function is thought of as the density according to
which a large population is distributed; the data are usually thought of
as a random sample from that population. A variety of approaches to
density estimation are used, including Parzen windows and a range of
data clustering techniques, including vector quantization. The most
basic form of density estimation is a rescaled histogram. Example We
will consider records of the incidence of diabetes. The following is
quoted verbatim from the data set description: A population of women who
were at least 21 years old, of Pima Indian heritage and living near
Phoenix, Arizona, was tested for diabetes mellitus according to World
Health Organization criteria. The data were collected by the US National
Institute of Diabetes and Digestive and Kidney Diseases. We used the 532
complete records.In this example, we construct three density estimates
for \"glu\" (plasma glucose concentration), one conditional on the
presence of diabetes, the second conditional on the absence of diabetes,
and the third not conditional on diabetes. The conditional density
estimates are then used to construct the probability of diabetes
conditional on \"glu\". The \"glu\" data were obtained from the MASS
package of the R programming language. Within R, ?Pima.tr and ?Pima.te
give a fuller account of the data. The mean of \"glu\" in the diabetes
cases is 143.1 and the standard deviation is 31.26. The mean of \"glu\"
in the non-diabetes cases is 110.0 and the standard deviation is 24.29.
From this we see that, in this data set, diabetes cases are associated
with greater levels of \"glu\". This will be made clearer by plots of
the estimated density functions. The first figure shows density
estimates of p(glu \| diabetes=1), p(glu \| diabetes=0), and p(glu). The
density estimates are kernel density estimates using a Gaussian kernel.
That is, a Gaussian density function is placed at each data point, and
the sum of the density functions is computed over the range of the data.
From the density of \"glu\" conditional on diabetes, we can obtain the
probability of diabetes conditional on \"glu\" via Bayes\' rule. For
brevity, \"diabetes\" is abbreviated \"db.\" in this formula. p (
diabetes = 1 \| glu ) = p ( glu \| db. = 1 ) p ( db. = 1 ) p ( glu \|
db. = 1 ) p ( db. = 1 ) + p ( glu \| db. = 0 ) p ( db. = 0 )
{\\displaystyle p({\\mbox{diabetes}}=1\|{\\mbox{glu}})={\\frac
{p({\\mbox{glu}}\|{\\mbox{db.}}=1)\\,p({\\mbox{db.}}=1)}{p({\\mbox{glu}}\|{\\mbox{db.}}=1)\\,p({\\mbox{db.}}=1)+p({\\mbox{glu}}\|{\\mbox{db.}}=0)\\,p({\\mbox{db.}}=0)}}}
The second figure shows the estimated posterior probability p(diabetes=1
\| glu). From these data, it appears that an increased level of \"glu\"
is associated with diabetes. Application and Purpose A very natural use
of density estimates is in the informal investigation of the properties
of a given set of data. Density estimates can give valuable indication
of such features as skewness and multimodality in the data. In some
cases they will yield conclusions that may then be regarded as
self-evidently true, while in others all they will do is to point the
way to further analysis and/or data collection. An important aspect of
statistics is often the presentation of data back to the client in order
to provide explanation and illustration of conclusions that may possibly
have been obtained by other means. Density estimates are ideal for this
purpose, for the simple reason that they are fairly easily
comprehensible to non-mathematicians. More examples illustrating the use
of density estimates for exploratory and presentational purposes,
including the important case of bivariate data.Density estimation is
also frequently used in anomaly detection or novelty detection: if an
observation lies in a very low-density region, it is likely to be an
anomaly or a novelty. In hydrology the histogram and estimated density
function of rainfall and river discharge data, analysed with a
probability distribution, are used to gain insight in their behaviour
and frequency of occurrence. An example is shown in the blue figure.
Kernel density estimation See also Kernel density estimation Mean
integrated squared error Histogram Multivariate kernel density
estimation Spectral density estimation Kernel embedding of distributions
Generative model Application of Order Statistics: Non-parametric Density
Estimation Probability distribution fitting References Sources Brian D.
Ripley (1996). Pattern Recognition and Neural Networks. Cambridge:
Cambridge University Press. ISBN 978-0521460866. Trevor Hastie, Robert
Tibshirani, and Jerome Friedman. The Elements of Statistical Learning.
New York: Springer, 2001. ISBN 0-387-95284-5. (See Chapter 6.) Qi Li and
Jeffrey S. Racine. Nonparametric Econometrics: Theory and Practice.
Princeton University Press, 2007, ISBN 0-691-12161-3. (See Chapter 1.)
D.W. Scott. Multivariate Density Estimation. Theory, Practice and
Visualization. New York: Wiley, 1992. B.W. Silverman. Density
Estimation. London: Chapman and Hall, 1986. ISBN 978-0-412-24620-3
External links CREEM: Centre for Research Into Ecological and
Environmental Modelling Downloads for free density estimation software
packages Distance 4 (from Research Unit for Wildlife Population
Assessment \"RUWPA\") and WiSP. UCI Machine Learning Repository Content
Summary (See \"Pima Indians Diabetes Database\" for the original data
set of 732 records, and additional notes.) MATLAB code for one
dimensional and two dimensional density estimation libAGF C++ software
for variable kernel density estimation.
