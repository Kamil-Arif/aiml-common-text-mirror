ELKI (for Environment for DeveLoping KDD-Applications Supported by
Index-Structures) is a data mining (KDD, knowledge discovery in
databases) software framework developed for use in research and
teaching. It was originally at the database systems research unit of
Professor Hans-Peter Kriegel at the Ludwig Maximilian University of
Munich, Germany, and now continued at the Technical University of
Dortmund, Germany. It aims at allowing the development and evaluation of
advanced data mining algorithms and their interaction with database
index structures. Description The ELKI framework is written in Java and
built around a modular architecture. Most currently included algorithms
belong to clustering, outlier detection and database indexes. The
object-oriented architecture allows the combination of arbitrary
algorithms, data types, distance functions, indexes, and evaluation
measures. The Java just-in-time compiler optimizes all combinations to a
similar extent, making benchmarking results more comparable if they
share large parts of the code. When developing new algorithms or index
structures, the existing components can be easily reused, and the type
safety of Java detects many programming errors at compile time. ELKI has
been used in data science for example to cluster sperm whale codas,
phoneme clustering, for anomaly detection in spaceflight operations, for
bike sharing redistribution, and traffic prediction. Objectives The
university project is developed for use in teaching and research. The
source code is written with extensibility and reusability in mind, but
is also optimized for performance. The experimental evaluation of
algorithms depends on many environmental factors and implementation
details can have a large impact on the runtime. ELKI aims at providing a
shared codebase with comparable implementations of many algorithms. As
research project, it currently does not offer integration with business
intelligence applications or an interface to common database management
systems via SQL. The copyleft (AGPL) license may also be a hindrance to
an integration in commercial products; nevertheless it can be used to
evaluate algorithms prior to developing an own implementation for a
commercial product. Furthermore, the application of the algorithms
requires knowledge about their usage, parameters, and study of original
literature. The audience are students, researchers, data scientists, and
software engineers. Architecture ELKI is modeled around a
database-inspired core, which uses a vertical data layout that stores
data in column groups (similar to column families in NoSQL databases).
This database core provides nearest neighbor search, range/radius
search, and distance query functionality with index acceleration for a
wide range of dissimilarity measures. Algorithms based on such queries
(e.g. k-nearest-neighbor algorithm, local outlier factor and DBSCAN) can
be implemented easily and benefit from the index acceleration. The
database core also provides fast and memory efficient collections for
object collections and associative structures such as nearest neighbor
lists. ELKI makes extensive use of Java interfaces, so that it can be
extended easily in many places. For example, custom data types, distance
functions, index structures, algorithms, input parsers, and output
modules can be added and combined without modifying the existing code.
This includes the possibility of defining a custom distance function and
using existing indexes for acceleration. ELKI uses a service loader
architecture to allow publishing extensions as separate jar files. ELKI
uses optimized collections for performance rather than the standard Java
API. For loops for example are written similar to C++ iterators: In
contrast to typical Java iterators (which can only iterate over
objects), this conserves memory, because the iterator can internally use
primitive values for data storage. The reduced garbage collection
improves the runtime. Optimized collections libraries such as GNU
Trove3, Koloboke, and fastutil employ similar optimizations. ELKI
includes data structures such as object collections and heaps (for,
e.g., nearest neighbor search) using such optimizations. Visualization
The visualization module uses SVG for scalable graphics output, and
Apache Batik for rendering of the user interface as well as lossless
export into PostScript and PDF for easy inclusion in scientific
publications in LaTeX. Exported files can be edited with SVG editors
such as Inkscape. Since cascading style sheets are used, the graphics
design can be restyled easily. Unfortunately, Batik is rather slow and
memory intensive, so the visualizations are not very scalable to large
data sets (for larger data sets, only a subsample of the data is
visualized by default). Awards Version 0.4, presented at the \"Symposium
on Spatial and Temporal Databases\" 2011, which included various methods
for spatial outlier detection, won the conference\'s \"best
demonstration paper award\". Included algorithms Select included
algorithms: Cluster analysis: K-means clustering (including fast
algorithms such as Elkan, Hamerly, Annulus, and Exponion k-Means, and
robust variants such as k-means\--) K-medians clustering K-medoids
clustering (PAM) (including FastPAM and approximations such as CLARA,
CLARANS) Expectation-maximization algorithm for Gaussian mixture
modeling Hierarchical clustering (including the fast SLINK, CLINK,
NNChain and Anderberg algorithms) Single-linkage clustering Leader
clustering DBSCAN (Density-Based Spatial Clustering of Applications with
Noise, with full index acceleration for arbitrary distance functions)
OPTICS (Ordering Points To Identify the Clustering Structure), including
the extensions OPTICS-OF, DeLi-Clu, HiSC, HiCO and DiSH HDBSCAN
Mean-shift clustering BIRCH clustering SUBCLU (Density-Connected
Subspace Clustering for High-Dimensional Data) CLIQUE clustering ORCLUS
and PROCLUS clustering COPAC, ERiC and 4C clustering CASH clustering DOC
and FastDOC subspace clustering P3C clustering Canopy clustering
algorithm Anomaly detection: k-Nearest-Neighbor outlier detection LOF
(Local outlier factor) LoOP (Local Outlier Probabilities) OPTICS-OF
DB-Outlier (Distance-Based Outliers) LOCI (Local Correlation Integral)
LDOF (Local Distance-Based Outlier Factor) EM-Outlier SOD (Subspace
Outlier Degree) COP (Correlation Outlier Probabilities) Frequent Itemset
Mining and association rule learning Apriori algorithm Eclat FP-growth
Dimensionality reduction Principal component analysis Multidimensional
scaling T-distributed stochastic neighbor embedding (t-SNE) Spatial
index structures and other search indexes: R-tree R\*-tree M-tree k-d
tree X-tree Cover tree iDistance NN descent Locality sensitive hashing
(LSH) Evaluation: Precision and recall, F1 score, Average Precision
Receiver operating characteristic (ROC curve) Discounted cumulative gain
(including NDCG) Silhouette index Davies--Bouldin index Dunn index
Density-based cluster validation (DBCV) Visualization Scatter plots
Histograms Parallel coordinates (also in 3D, using OpenGL) Other:
Statistical distributions and many parameter estimators, including
robust MAD based and L-moment based estimators Dynamic time warping
Change point detection in time series Intrinsic dimensionality
estimators Version history Version 0.1 (July 2008) contained several
Algorithms from cluster analysis and anomaly detection, as well as some
index structures such as the R\*-tree. The focus of the first release
was on subspace clustering and correlation clustering algorithms.Version
0.2 (July 2009) added functionality for time series analysis, in
particular distance functions for time series.Version 0.3 (March 2010)
extended the choice of anomaly detection algorithms and visualization
modules.Version 0.4 (September 2011) added algorithms for geo data
mining and support for multi-relational database and index
structures.Version 0.5 (April 2012) focuses on the evaluation of cluster
analysis results, adding new visualizations and some new
algorithms.Version 0.6 (June 2013) introduces a new 3D adaption of
parallel coordinates for data visualization, apart from the usual
additions of algorithms and index structures.Version 0.7 (August 2015)
adds support for uncertain data types, and algorithms for the analysis
of uncertain data.Version 0.7.5 (February 2019) adds additional
clustering algorithms, anomaly detection algorithms, evaluation
measures, and indexing structures.Version 0.8 (October 2020) adds
automatic index creation, garbage collection, and incremental priority
search, as well as many more algorithms such as BIRCH. Similar
applications scikit-learn: machine learning library in python Weka: A
similar project by the University of Waikato, with a focus on
classification algorithms RapidMiner: An application available
commercially (a restricted version is available as open source) KNIME:
An open source platform which integrates various components for machine
learning and data mining See also Comparison of statistical packages
References External links Official website of ELKI with download and
documentation.
