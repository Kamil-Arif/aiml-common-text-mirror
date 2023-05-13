Apache SystemDS (Previously, Apache SystemML) is an open source ML
system for the end-to-end data science lifecycle. SystemDS\'s
distinguishing characteristics are: Algorithm customizability via R-like
and Python-like languages. Multiple execution modes, including
Standalone, Spark Batch, Spark MLContext, Hadoop Batch, and JMLC.
Automatic optimization based on data and cluster characteristics to
ensure both efficiency and scalability. History SystemML was created in
2010 by researchers at the IBM Almaden Research Center led by IBM Fellow
Shivakumar Vaithyanathan. It was observed that data scientists would
write machine learning algorithms in languages such as R and Python for
small data. When it came time to scale to big data, a systems programmer
would be needed to scale the algorithm in a language such as Scala. This
process typically involved days or weeks per iteration, and errors would
occur translating the algorithms to operate on big data. SystemML seeks
to simplify this process. A primary goal of SystemML is to automatically
scale an algorithm written in an R-like or Python-like language to
operate on big data, generating the same answer without the error-prone,
multi-iterative translation approach. On June 15, 2015, at the Spark
Summit in San Francisco, Beth Smith, General Manager of IBM Analytics,
announced that IBM was open-sourcing SystemML as part of IBM\'s major
commitment to Apache Spark and Spark-related projects. SystemML became
publicly available on GitHub on August 27, 2015 and became an Apache
Incubator project on November 2, 2015. On May 17, 2017, the Apache
Software Foundation Board approved the graduation of Apache SystemML as
an Apache Top Level Project. Key technologies The following are some of
the technologies built into the SystemDS engine. Compressed Linear
Algebra for Large Scale Machine Learning Declarative Machine Learning
Language Examples Principal Component Analysis The following code
snippet does the Principal component analysis of input matrix A
{\\displaystyle A} , which returns the e i g e n v e c t o r s
{\\displaystyle eigenvectors} and the e i g e n v a l u e s {\\textstyle
eigenvalues} . Invocation script Database functions DBSCAN clustering
algorithm with Euclidean distance. Improvements SystemDS 2.0.0 is the
first major release under the new name. This release contains a major
refactoring, a few major features, a large number of improvements and
fixes, and some experimental features to better support the end-to-end
data science lifecycle. In addition to that, this release also removes
several features that are not up date and outdated. New mechanism for
DML-bodied (script-level) builtin functions, and a wealth of new
built-in functions for data preprocessing including data cleaning,
augmentation and feature engineering techniques, new ML algorithms, and
model debugging. Several methods for data cleaning have been implemented
including multiple imputations with multivariate imputation by chained
equations (MICE) and other techniques, SMOTE, an oversampling technique
for class imbalance, forward and backward NA filling, cleaning using
schema and length information, support for outlier detection using
standard deviation and inter-quartile range, and functional dependency
discovery. A complete framework for lineage tracing and reuse including
support for loop deduplication, full and partial reuse, compiler
assisted reuse, several new rewrites to facilitate reuse. New federated
runtime backend including support for federated matrices and frames,
federated builtins (transform-encode, decode etc.). Refactor compression
package and add functionalities including quantization for lossy
compression, binary cell operations, left matrix multiplication.
\[experimental\] New python bindings with supports for several builtins,
matrix operations, federated tensors and lineage traces. Cuda
implementation of cumulative aggregate operators (cumsum, cumprod etc.)
New model debugging technique with slice finder. New tensor data model
(basic tensors of different value types, data tensors with schema)
\[experimental\] Cloud deployment scripts for AWS and scripts to set up
and start federated operations. Performance improvements with parallel
sort, gpu cum agg, append cbind etc. Various compiler and runtime
improvements including new and improved rewrites, reduced Spark context
creation, new eval framework, list operations, updated native kernel
libraries to name a few. New data reader/writer for json frames and
support for sql as a data source. Miscellaneous improvements: improved
documentation, better testing, run/release scripts, improved packaging,
Docker container for systemds, support for lambda expressions, bug
fixes. Removed MapReduce compiler and runtime backend, pydml parser,
Java-UDF framework, script-level debugger. Deprecated
./scripts/algorithms, as those algorithms gradually will be part of
SystemDS builtins. Contributions Apache SystemDS welcomes contributions
in code, question and answer, community building, or spreading the word.
The contributor guide is available at
https://github.com/apache/systemds/blob/main/CONTRIBUTING.md See also
Comparison of deep learning software References External links Apache
SystemML website IBM Research - SystemML Q & A with Shiv Vaithyanathan,
Creator of SystemML and IBM Fellow A Universal Translator for Big Data
and Machine Learning SystemML: Declarative Machine Learning at Scale
presentation by Fred Reiss SystemML: Declarative Machine Learning on
MapReduce Hybrid Parallelization Strategies for Large-Scale Machine
Learning in SystemML SystemML\'s Optimizer: Plan Generation for
Large-Scale Machine Learning Programs IBM\'s SystemML machine learning
system becomes Apache Incubator project IBM donates machine learning
tech to Apache Spark open source community IBM\'s SystemML Moves Forward
as Apache Incubator Project
