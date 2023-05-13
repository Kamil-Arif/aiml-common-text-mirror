Mutation is a genetic operator used to maintain genetic diversity of the
chromosomes of a population of a genetic or, more generally, an
evolutionary algorithm (EA). It is analogous to biological mutation. The
classic example of a mutation operator of a binary coded genetic
algorithm (GA) involves a probability that an arbitrary bit in a genetic
sequence will be flipped from its original state. A common method of
implementing the mutation operator involves generating a random variable
for each bit in a sequence. This random variable tells whether or not a
particular bit will be flipped. This mutation procedure, based on the
biological point mutation, is called single point mutation. Other types
of mutation operators are commonly used for representations other than
binary, such as floating-point encodings or representations for
combinatorial problems. The purpose of mutation in EAs is to introduce
diversity into the sampled population. Mutation operators are used in an
attempt to avoid local minima by preventing the population of
chromosomes from becoming too similar to each other, thus slowing or
even stopping convergence to the global optimum. This reasoning also
leads most EAs to avoid only taking the fittest of the population in
generating the next generation, but rather selecting a random (or
semi-random) set with a weighting toward those that are fitter.The
following requirements apply to all mutation operators used in an EA:
every point in the search space must be reachable by one or more
mutations. there must be no preference for parts or directions in the
search space (no drift). small mutations should be more probable than
large ones.For different genome types, different mutation types are
suitable. An overview and more operators than those presented below can
be found in the introductory book by Eiben and Smith or in. Bit string
mutation The mutation of bit strings ensue through bit flips at random
positions. Example: The probability of a mutation of a bit is 1 l
{\\displaystyle {\\frac {1}{l}}} , where l {\\displaystyle l} is the
length of the binary vector. Thus, a mutation rate of 1 {\\displaystyle
1} per mutation and individual selected for mutation is reached.
Mutation of real numbers Many EAs, such as the evolution strategy or the
real-coded genetic algorithms, work with real numbers instead of bit
strings. This is due to the good experiences that have been made with
this type of coding.The value of a real-valued gene can either be
changed or redetermined. A mutation that implements the latter should
only ever be used in conjunction with the value-changing mutations and
then only with comparatively low probability, as it can lead to large
changes. In practical applications, the decision variables to be changed
of the optimisation problem to be solved are usually limited.
Accordingly, the values of the associated genes are each restricted to
an interval \[ x min , x max \] {\\displaystyle \[x\_{\\min },x\_{\\max
}\]} . Mutations may or may not take these restrictions into account. In
the latter case, suitable post-treatment is then required as described
below. Mutation without consideration of restrictions A real number x
{\\displaystyle x} can be mutated using normal distribution N ( 0 , σ )
{\\displaystyle {\\mathcal {N}}(0,\\sigma )} by adding the generated
random value to the old value of the gene, resulting in the mutated
value x ′ {\\displaystyle x\'} : x ′ = x + N ( 0 , σ ) {\\displaystyle
x\'=x+{\\mathcal {N}}(0,\\sigma )} In the case of genes with a
restricted range of values, it is a good idea to choose the step size of
the mutation σ {\\displaystyle \\sigma } so that it reasonably fits the
range \[ x min , x max \] {\\displaystyle \[x\_{\\min },x\_{\\max }\]}
of the gene to be changed, e.g.: σ = x max − x min 6 {\\displaystyle
\\sigma ={\\frac {x\_{\\text{max}}-x\_{\\text{min}}}{6}}} The step size
can also be adjusted to the smaller permissible change range depending
on the current value. In any case, however, it is likely that the new
value x ′ {\\displaystyle x\'} of the gene will be outside the
permissible range of values. Such a case must be considered a lethal
mutation, since the obvious repair by using the respective violated
limit as the new value of the gene would lead to a drift. This is
because the limit value would then be selected with the entire
probability of the values beyond the limit of the value range. The
evolution strategy works with real numbers and mutation based on normal
distribution. The step sizes are part of the chromosome and are subject
to evolution together with the actual decision variables. Mutation with
consideration of restrictions One possible form of changing the value of
a gene while taking its value range \[ x min , x max \] {\\displaystyle
\[x\_{\\min },x\_{\\max }\]} into account is the mutation relative
parameter change of the evolutionary algorithm GLEAM (General Learning
Evolutionary Algorithm and Method), in which, as with the mutation
presented earlier, small changes are more likely than large ones. First,
an equally distributed decision is made as to whether the current value
x {\\displaystyle x} should be increased or decreased and then the
corresponding total change interval is determined. Without loss of
generality, an increase is assumed for the explanation and the total
change interval is then \[ x , x max \] {\\displaystyle \[x,x\_{\\max
}\]} . It is divided into k {\\displaystyle k} sub-areas of equal size
with the width δ {\\displaystyle \\delta } , from which k
{\\displaystyle k} sub-change intervals of different size are formed: i
{\\displaystyle i} -th sub-change interval: \[ x , x + δ ⋅ i \]
{\\displaystyle \[x,x+\\delta \\cdot i\]} with δ = ( x max − x ) k
{\\displaystyle \\delta ={\\frac {(x\_{\\text{max}}-x)}{k}}} and i = 1 ,
... , k {\\displaystyle i=1,\\dots ,k} Subsequently, one of the k
{\\displaystyle k} sub-change intervals is selected in equal
distribution and a random number, also equally distributed, is drawn
from it as the new value x ′ {\\displaystyle x\'} of the gene. The
resulting summed probabilities of the sub-change intervals result in the
probability distribution of the k {\\displaystyle k} sub-areas for the
exemplary case of k = 10 {\\displaystyle k=10} shown in the adjacent
figure. This is not a normal distribution as before, but this
distribution also clearly favours small changes over larger ones. This
mutation for larger values of k {\\displaystyle k} , such as 10, is less
well suited for tasks where the optimum lies on one of the value range
boundaries. This can be remedied by significantly reducing k
{\\displaystyle k} when a gene value approaches its limits very closely.
Mutation of permutations Mutations of permutations are specially
designed for genomes that are themselves permutations of a set. These
are often used to solve combinatorial tasks. In the two mutations
presented, parts of the genome are rotated or inverted. Rotation to the
right The presentation of the procedure is illustrated by an example on
the right: Inversion The presentation of the procedure is illustrated by
an example on the right: Variants with preference for smaller changes
The requirement raised at the beginning for mutations, according to
which small changes should be more probable than large ones, is only
inadequately fulfilled by the two permutation mutations presented, since
the lengths of the partial lists and the number of shift positions are
determined in an equally distributed manner. However, the longer the
partial list and the shift, the greater the change in gene order. This
can be remedied by the following modifications. The end index j
{\\displaystyle j} of the partial lists is determined as the distance d
{\\displaystyle d} to the start index i {\\displaystyle i} : j = ( i + d
) mod \| P 0 \| {\\displaystyle j=(i+d){\\bmod
{\\left\|P\_{0}\\right\|}}} where d {\\displaystyle d} is determined
randomly according to one of the two procedures for the mutation of real
numbers from the interval \[ 0 , \| P 0 \| − 1 \] {\\displaystyle
\\left\[0,\\left\|P\_{0}\\right\|-1\\right\]} and rounded. For the
rotation, k {\\displaystyle k} is determined similarly to the distance d
{\\displaystyle d} , but the value 0 {\\displaystyle 0} is forbidden.
For the inversion, note that i ≠ j {\\displaystyle i\\neq j} must hold,
so for d {\\displaystyle d} the value 0 {\\displaystyle 0} must be
excluded. See also Evolutionary algorithms Genetic algorithms References
Bibliography John Holland (1975). Adaptation in Natural and Artificial
Systems, PhD thesis, University of Michigan Press, Ann Arbor, Michigan.
ISBN 0-262-58111-6. Schwefel, Hans-Paul (1995). Evolution and Optimum
Seeking. New York: John Wiley & Sons. ISBN 0-471-57148-2. Davis,
Lawrence (1991). Handbook of genetic algorithms. New York: Van Nostrand
Reinhold. ISBN 0-442-00173-8. OCLC 23081440. Eiben, A.E.; Smith, J.E.
(2015). Introduction to Evolutionary Computing. Natural Computing
Series. Berlin, Heidelberg: Springer. doi:10.1007/978-3-662-44874-8.
ISBN 978-3-662-44873-1. Yu, Xinjie; Gen, Mitsuo (2010). Introduction to
Evolutionary Algorithms. Decision Engineering. London: Springer.
doi:10.1007/978-1-84996-129-5. ISBN 978-1-84996-128-8. De Jong, Kenneth
A. (2006). Evolutionary computation : a unified approach. Cambridge,
Mass.: MIT Press. ISBN 978-0-262-25598-1. OCLC 69652176. Fogel, David
B.; Bäck, Thomas; Michalewicz, Zbigniew, eds. (1999). Evolutionary
computation. Vol. 1, Basic algorithms and operators. Bristol: Institute
of Physics Pub. ISBN 0-585-30560-9. OCLC 45730387.
