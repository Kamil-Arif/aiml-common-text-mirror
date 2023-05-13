Isolation Forest is an algorithm for data anomaly detection initially
developed by Fei Tony Liu and Zhi-Hua Zhou in 2008. Isolation Forest
detects anomalies using binary trees. The algorithm has a linear time
complexity and a low memory requirement, which works well with
high-volume data. Isolation Forest splits the data space using lines
that are orthogonal to the origin and assigns higher anomaly scores to
data points that need fewer splits to be isolated. The figure on the
right shows an application of the Isolation Forest algorithm to the
waiting time between eruptions and the duration of the eruption of the
Old Faithful geyser in Yellowstone National Park. Darker shades of red
indicate higher estimated anomaly scores. History The Isolation Forest
(iForest) algorithm was initially proposed by Fei Tony Liu, Kai Ming
Ting and Zhi-Hua Zhou in 2008. In 2010, an extension of the algorithm -
SCiforest was developed to address clustered and axis-paralleled
anomalies. In 2012 the same authors demonstrated that iForest has linear
time complexity, a small memory requirement, and is applicable to high
dimensional data. In 2013 Zhiguo Ding and Minrui Fei proposed a
framework based on iForest to resolve the problem of detecting anomalies
in streaming data. More applications of iForest to streaming data are
described in papers by Tan et al., Susto et al. and Weng et al.In 2018,
an extension of iForest, aimed at improving the reliability of the
anomaly score produced for a given data point was proposed. Algorithm
The premise of the Isolation Forest algorithm is that anomalous data
points are easier to separate from the rest of the sample. In order to
isolate a data point, the algorithm recursively generates partitions on
the sample by randomly selecting an attribute and then randomly
selecting a split value between the minimum and maximum values allowed
for that attribute. An example of random partitioning in a 2D dataset of
normally distributed points is given in Fig. 2 for a non-anomalous point
and Fig. 3 for a point that\'s more likely to be an anomaly. It is
apparent from the pictures how anomalies require fewer random partitions
to be isolated, compared to normal points. Recursive partitioning can be
represented by a tree structure named Isolation Tree, while the number
of partitions required to isolate a point can be interpreted as the
length of the path, within the tree, to reach a terminating node
starting from the root. For example, the path length of point x i
{\\displaystyle x\_{i}} in Fig. 2 is greater than the path length of x j
{\\displaystyle x\_{j}} in Fig. 3. Let X = { x 1 , ... , x n }
{\\displaystyle X=\\{x\_{1},\\dots ,x\_{n}\\}} be a set of d-dimensional
points and X ′ ⊂ X {\\displaystyle X\'\\subset X} . An Isolation Tree
(iTree) is defined as a data structure with the following properties:
for each node T {\\displaystyle T} in the Tree, T {\\displaystyle T} is
either an external-node with no child, or an internal-node with one
"test" and exactly two child nodes ( T l {\\displaystyle T\_{l}} and T r
{\\displaystyle T\_{r}} ) a test at node T {\\displaystyle T} consists
of an attribute q {\\displaystyle q} and a split value p {\\displaystyle
p} such that the test q \< p {\\displaystyle q 2 1 for m = 2 0 otherwise
{\\displaystyle c(m)={\\begin{cases}2H(m-1)-{\\frac
{2(m-1)}{n}}&{\\text{for }}m\>2\\\\1&{\\text{for
}}m=2\\\\0&{\\text{otherwise}}\\end{cases}}} where n {\\displaystyle n}
is the testing data size, m {\\displaystyle m} is the size of the sample
set and H {\\displaystyle H} is the harmonic number, which can be
estimated by H ( i ) = l n ( i ) + γ {\\displaystyle H(i)=ln(i)+\\gamma
} , where γ = 0.5772156649 {\\displaystyle \\gamma =0.5772156649} is the
Euler-Mascheroni constant. The value of c(m) above represents the
average of h ( x ) {\\displaystyle h(x)} given m {\\displaystyle m} , so
we can use it to normalize h ( x ) {\\displaystyle h(x)} and get an
estimation of the anomaly score for a given instance x: s ( x , m ) = 2
− E ( h ( x ) ) c ( m ) {\\displaystyle s(x,m)=2\^{\\frac
{-E(h(x))}{c(m)}}} where E ( h ( x ) ) {\\displaystyle E(h(x))} is the
average value of h ( x ) {\\displaystyle h(x)} from a collection of
iTrees. It is interesting to note that for any given instance x
{\\displaystyle x} : if s {\\displaystyle s} is close to 1
{\\displaystyle 1} then x {\\displaystyle x} is very likely to be an
anomaly if s {\\displaystyle s} is smaller than 0.5 {\\displaystyle 0.5}
then x {\\displaystyle x} is likely to be a normal value if for a given
sample all instances are assigned an anomaly score of around 0.5
{\\displaystyle 0.5} , then it is safe to assume that the sample
doesn\'t have any anomaly Open source implementations Original
implementation: Isolation Forest, an algorithm that detects
data-anomalies using binary trees written in R. Released by the paper\'s
first author Liu, Fei Tony in 2009.Other implementations (in
alphabetical order): Isolation Forest - A Spark/Scala implementation,
created by James Verbus from the LinkedIn Anti-Abuse AI team. Isolation
Forest by H2O-3 - An implementation of Isolation Forest for Anomaly
Detection by H2O-3. Package solitude implementation in R by Srikanth
Komala Sheshachala. Python implementation with examples in scikit-learn.
Spark iForest - A distributed implementation in Scala and Python, which
runs on Apache Spark. Written by Yang, Fangzhou. PyOD IForest - Another
Python implementation in the popular Python Outlier Detection (PyOD)
library.Other variations of Isolation Forest algorithm implementations:
Extended Isolation Forest -- An implementation of Extended Isolation
Forest for Anomaly Detection by Sahand Hariri.Extended Isolation Forest
by H2O-3 - An implementation of Extended Isolation Forest for Anomaly
Detection by H2O-3.(Python, R, C/C++) Isolation Forest and variations by
David Cortes - An implementation of Isolation Forest and its variations
by David Cortes. See also Anomaly detection Random forest == References
==
