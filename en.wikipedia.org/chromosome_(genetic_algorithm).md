In genetic algorithms (GA), or more general, evolutionary algorithms
(EA), a chromosome (also sometimes called a genotype) is a set of
parameters which define a proposed solution of the problem that the
evolutionary algorithm is trying to solve. The set of all solutions,
also called individuals according to the biological model, is known as
the population. The genome of an individual consists of one, more rarely
of several, chromosomes and corresponds to the genetic representation of
the task to be solved. A chromosome is composed of a set of genes, where
a gene consists of one or more semantically connected parameters, which
are often also called decision variables. They determine one or more
phenotypic characteristics of the individual or at least have an
influence on them. In the basic form of genetic algorithms, the
chromosome is represented as a binary string, while in later variants
and in EAs in general, a wide variety of other data structures are used.
Chromosome design When creating the genetic representation of a task, it
is determined which decision variables and other degrees of freedom of
the task should be improved by the EA and possible additional heuristics
and how the genotype-phenotype mapping should look like. The design of a
chromosome translates these considerations into concrete data structures
for which an EA then has to be selected, configured, extended, or, in
the worst case, created. Finding a suitable representation of the
problem domain for a chromosome is an important consideration, as a good
representation will make the search easier by limiting the search space;
similarly, a poorer representation will allow a larger search space. In
this context, suitable mutation and crossover operators must also be
found or newly defined to fit the chosen chromosome design. An important
requirement for these operators is that they not only allow all points
in the search space to be reached in principle, but also make this as
easy as possible.The following requirements must be met by a well-suited
chromosome: It must allow the accessibility of all admissible points in
the search space. Design of the chromosome in such a way that it covers
only the search space and no additional areas. so that there is no
redundancy or only as little redundancy as possible.Observance of strong
causality: small changes in the chromosome should only lead to small
changes in the phenotype. This is also called locality of the
relationship between search and problem space. Designing the chromosome
in such a way that it excludes prohibited regions in the search space
completely or as much as possible.While the first requirement is
indispensable, depending on the application and the EA used, one usually
only has to be satisfied with fulfilling the remaining requirements as
far as possible. It should be noted, however, that the evolutionary
search is supported and possibly considerably accelerated by a
fulfillment as complete as possible. Examples of chromosomes Chromosomes
for binary codings In their classical form, GAs use bit strings and map
the decision variables to be optimized onto them. An example for one
boolean and three integer decision variables with the value ranges 0 ≤ D
1 ≤ 60 {\\displaystyle 0\\leq D\_{1}\\leq 60} , 28 ≤ D 2 ≤ 30
{\\displaystyle 28\\leq D\_{2}\\leq 30} and − 12 ≤ D 3 ≤ 14
{\\displaystyle -12\\leq D\_{3}\\leq 14} may illustrate this: Note that
the negative number here is given in two\'s complement. This straight
forward representation uses five bits to represent the three values of D
2 {\\displaystyle D\_{2}} , although two bits would suffice. This is a
significant redundancy. An improved alternative, where 28 is to be added
for the genotype-phenotype mapping, could look like this: with D 2 =
28 + D 2 ′ = 29 {\\displaystyle D\_{2}=28+D\'\_{2}=29} . Chromosomes
with real-valued or integer genes For the processing of tasks with
real-valued or mixed-integer decision variables, EAs such as the
evolution strategy or the real-coded GAs are suited. In the case of
mixed-integer values, rounding is often used, but this represents some
violation of the redundancy requirement. If the necessary precisions of
the real values can be reasonably narrowed down, this violation can be
remedied by using integer-coded GAs. For this purpose, the valid digits
of real values are mapped to integers by multiplication with a suitable
factor. For example, 12.380 becomes the integer 12380 by multiplying by
1000. This must of course be taken into account in genotype-phenotype
mapping for evaluation and result presentation. A common form is a
chromosome consisting of a list or an array of integer or real values.
Chromosomes for permutations Combinatorial problems are mainly concerned
with finding an optimal sequence of a set of elementary items. As an
example, consider the problem of the traveling salesman who wants to
visit a given number of cities exactly once on the shortest possible
tour. The simplest and most obvious mapping onto a chromosome is to
number the cities consecutively, to interpret a resulting sequence as
permutation and to store it directly in a chromosome, where one gene
corresponds to the ordinal number of a city. Then, however, the
variation operators may only change the gene order and not remove or
duplicate any genes. The chromosm thus contains the path of a possible
tour to the cities. As an example the sequence 3 , 5 , 7 , 1 , 4 , 2 , 9
, 6 , 8 {\\displaystyle 3,5,7,1,4,2,9,6,8} of nine cities may serve, to
which the following chromosome corresponds: In addition to this encoding
frequently called path representation, there are several other ways of
representing a permutation, for example the ordinal representation or
the matrix representation. Chromosomes for co-evolution When a genetic
representation contains, in addition to the decision variables,
additional information that influences evolution and/or the mapping of
the genotype to the phenotype and is itself subject to evolution, this
is referred to as co-evolution. A typical example is the evolution
strategy (ES), which includes one or more mutation step sizes as
strategy parameters in each chromosome. Another example is an additional
gene to control a selection heuristic for resource allocation in a
scheduling tasks.This approach is based on the assumption that good
solutions are based on an appropriate selection of strategy parameters
or on control gene(s) that influences genotype-phenotype mapping. The
success of the ES gives evidence to this assumption. Chromosomes for
complex representations The chromosomes presented above are well suited
for processing tasks of continuous, mixed-integer, pure-integer or
combinatorial optimization. For a combination of these optimization
areas, on the other hand, it becomes increasingly difficult to map them
to simple strings of values, depending on the task. The following
extension of the gene concept is proposed by the EA GLEAM (General
Learning Evolutionary Algorithm and Method) for this purpose: A gene is
considered to be the description of an element or elementary trait of
the phenotype, which may have multiple parameters. For this purpose,
gene types are defined that contain as many parameters of the
appropriate data type as are required to describe the particular element
of the phenotype. A chromosome now consists of genes as data objects of
the gene types, whereby, depending on the application, each gene type
occurs exactly once as a gene or can be contained in the chromosome any
number of times. The latter leads to chromosomes of dynamic length, as
they are required for some problems. The gene type definitions also
contain information on the permissible value ranges of the gene
parameters, which are observed during chromosome generation and by
corresponding mutations, so they cannot lead to lethal mutations. For
tasks with a combinatorial part, there are suitable genetic operators
that can move or reposition genes as a whole, i.e. with their
parameters. A scheduling task is used as an illustration, in which
workflows are to be scheduled that require different numbers of
heterogeneous resources. A workflow specifies which work steps can be
processed in parallel and which have to be executed one after the other.
In this context, heterogeneous resources mean different processing times
at different costs in addition to different processing capabilities.
Each scheduling operation therefore requires one or more parameters that
determine the resource selection, where the value ranges of the
parameters depend on the number of alternative resources available for
each work step. A suitable chromosome provides one gene type per work
step and in this case one corresponding gene, which has one parameter
for each required resource. The order of genes determines the order of
scheduling operations and, therefore, the precedence in case of
allocation conflicts. The exemplary gene type definition of work step 15
with two resources, for which there are four and seven alternatives
respectively, would then look as shown in the left image. Since the
parameters represent indices in lists of available resources for the
respective work step, their value range starts at 0. The right image
shows an example of three genes of a chromosome belonging to the gene
types in list representation. Chromosomes for tree representations Tree
representations in a chromosome are used by genetic programming, an EA
type for generating computer programs or circuits. The trees correspond
to the syntax trees generated by a compiler as internal representation
when translating a computer program. The adjacent figure shows the
syntax tree of a mathematical expression as an example. Mutation
operators can rearrange, change or delete subtrees depending on the
represented syntax structure. Recombination is performed by exchanging
suitable subtrees. Bibliography Thomas Bäck (1996): Evolutionary
Algorithms in Theory and Practice: Evolution Strategies, Evolutionary
Programming, Genetic Algorithms, Oxford Univ. Press. ISBN
978-0-19-509971-3 Wolfgang Banzhaf, P. Nordin, R. Keller, F. Francone
(1998): Genetic Programming - An Introduction, Morgan Kaufmann, San
Francisco. ISBN 1-55860-510-X Kenneth A. de Jong (2006): Evolutionary
Computation: A Unified Approach. MIT Press, Cambridge, MA. ISBN
0-262-04194-4 Melanie Mitchell (1996): An Introduction to Genetic
Algorithms. MIT Press, Cambridge MA. ISBN 978-0-262-63185-3 Hans-Paul
Schwefel (1995): Evolution and Optimum Seeking. Wiley & Sons, New York.
ISBN 0-471-57148-2 == References ==
