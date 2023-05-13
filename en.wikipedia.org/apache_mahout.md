Apache Mahout is a project of the Apache Software Foundation to produce
free implementations of distributed or otherwise scalable machine
learning algorithms focused primarily on linear algebra. In the past,
many of the implementations use the Apache Hadoop platform, however
today it is primarily focused on Apache Spark. Mahout also provides
Java/Scala libraries for common math operations (focused on linear
algebra and statistics) and primitive Java collections. Mahout is a work
in progress; a number of algorithms have been implemented. Features
Samsara Apache Mahout-Samsara refers to a Scala domain specific language
(DSL) that allows users to use R-Like syntax as opposed to traditional
Scala-like syntax. This allows user to express algorithms concisely and
clearly. Backend Agnostic Apache Mahout\'s code abstracts the domain
specific language from the engine where the code is run. While active
development is done with the Apache Spark engine, users are free to
implement any engine they choose- H2O and Apache Flink have been
implemented in the past and examples exist in the code base. GPU/CPU
accelerators The JVM has notoriously slow computation. To improve speed,
"native solvers" were added which move in-core, and by extension,
distributed BLAS operations out of the JVM, offloading to off-heap or
GPU memory for processing via multiple CPUs and/or CPU cores, or GPUs
when built against the ViennaCL library. \"Extending Mahout Samsara to
GPU Clusters\".. ViennaCL is a highly optimized C++ library with BLAS
operations implemented in OpenMP, and OpenCL. As of release 14.1, the
OpenMP build considered to be stable, leaving the OpenCL build is still
in its experimental POC phase. Recommenders Apache Mahout features
implementations of Alternating Least Squares, Co-Occurrence, and
Correlated Co-Occurrence, a unique-to-Mahout recommender algorithm that
extends co-occurrence to be used on multiple dimensions of data. History
Transition from Map Reduce to Apache Spark While Mahout\'s core
algorithms for clustering, classification and batch based collaborative
filtering were implemented on top of Apache Hadoop using the map/reduce
paradigm, it did not restrict contributions to Hadoop-based
implementations. Contributions that run on a single node or on a
non-Hadoop cluster were also welcomed. For example, the \'Taste\'
collaborative-filtering recommender component of Mahout was originally a
separate project and can run stand-alone without Hadoop. Starting with
the release 0.10.0, the project shifted its focus to building a
backend-independent programming environment, code named \"Samsara\". The
environment consists of an algebraic backend-independent optimizer and
an algebraic Scala DSL unifying in-memory and distributed algebraic
operators. Supported algebraic platforms are Apache Spark, H2O, and
Apache Flink. Support for MapReduce algorithms started being gradually
phased out in 2014. Release History Developers Apache Mahout is
developed by a community. The project is managed by a group called the
\"Project Management Committee\" (PMC). The current PMC is Andrew
Musselman, Andrew Palumbo, Drew Farris, Isabel Drost-Fromm, Jake Mannix,
Pat Ferrel, Paritosh Ranjan, Trevor Grant, Robin Anil, Sebastian
Schelter, Stevo Slavić. References External links Official website
