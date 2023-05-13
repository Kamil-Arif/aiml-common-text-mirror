In computational learning theory, probably approximately correct (PAC)
learning is a framework for mathematical analysis of machine learning.
It was proposed in 1984 by Leslie Valiant.In this framework, the learner
receives samples and must select a generalization function (called the
hypothesis) from a certain class of possible functions. The goal is
that, with high probability (the \"probably\" part), the selected
function will have low generalization error (the \"approximately
correct\" part). The learner must be able to learn the concept given any
arbitrary approximation ratio, probability of success, or distribution
of the samples. The model was later extended to treat noise
(misclassified samples). An important innovation of the PAC framework is
the introduction of computational complexity theory concepts to machine
learning. In particular, the learner is expected to find efficient
functions (time and space requirements bounded to a polynomial of the
example size), and the learner itself must implement an efficient
procedure (requiring an example count bounded to a polynomial of the
concept size, modified by the approximation and likelihood bounds).
Definitions and terminology In order to give the definition for
something that is PAC-learnable, we first have to introduce some
terminology.For the following definitions, two examples will be used.
The first is the problem of character recognition given an array of n
{\\displaystyle n} bits encoding a binary-valued image. The other
example is the problem of finding an interval that will correctly
classify points within the interval as positive and the points outside
of the range as negative. Let X {\\displaystyle X} be a set called the
instance space or the encoding of all the samples. In the character
recognition problem, the instance space is X = { 0 , 1 } n
{\\displaystyle X=\\{0,1\\}\^{n}} . In the interval problem the instance
space, X {\\displaystyle X} , is the set of all bounded intervals in R
{\\displaystyle \\mathbb {R} } , where R {\\displaystyle \\mathbb {R} }
denotes the set of all real numbers. A concept is a subset c ⊂ X
{\\displaystyle c\\subset X} . One concept is the set of all patterns of
bits in X = { 0 , 1 } n {\\displaystyle X=\\{0,1\\}\^{n}} that encode a
picture of the letter \"P\". An example concept from the second example
is the set of open intervals, { ( a , b ) ∣ 0 ≤ a ≤ π / 2 , π ≤ b ≤ 13 }
{\\displaystyle \\{(a,b)\\mid 0\\leq a\\leq \\pi /2,\\pi \\leq b\\leq
{\\sqrt {13}}\\}} , each of which contains only the positive points. A
concept class C {\\displaystyle C} is a collection of concepts over X
{\\displaystyle X} . This could be the set of all subsets of the array
of bits that are skeletonized 4-connected (width of the font is 1). Let
E X ( c , D ) {\\displaystyle EX(c,D)} be a procedure that draws an
example, x {\\displaystyle x} , using a probability distribution D
{\\displaystyle D} and gives the correct label c ( x ) {\\displaystyle
c(x)} , that is 1 if x ∈ c {\\displaystyle x\\in c} and 0 otherwise.
Now, given 0 \< ϵ , δ \< 1 {\\displaystyle 0\<\\epsilon ,\\delta \<1} ,
assume there is an algorithm A {\\displaystyle A} and a polynomial p
{\\displaystyle p} in 1 / ϵ , 1 / δ {\\displaystyle 1/\\epsilon
,1/\\delta } (and other relevant parameters of the class C
{\\displaystyle C} ) such that, given a sample of size p {\\displaystyle
p} drawn according to E X ( c , D ) {\\displaystyle EX(c,D)} , then,
with probability of at least 1 − δ {\\displaystyle 1-\\delta } , A
{\\displaystyle A} outputs a hypothesis h ∈ C {\\displaystyle h\\in C}
that has an average error less than or equal to ϵ {\\displaystyle
\\epsilon } on X {\\displaystyle X} with the same distribution D
{\\displaystyle D} . Further if the above statement for algorithm A
{\\displaystyle A} is true for every concept c ∈ C {\\displaystyle c\\in
C} and for every distribution D {\\displaystyle D} over X
{\\displaystyle X} , and for all 0 \< ϵ , δ \< 1 {\\displaystyle
0\<\\epsilon ,\\delta \<1} then C {\\displaystyle C} is (efficiently)
PAC learnable (or distribution-free PAC learnable). We can also say that
A {\\displaystyle A} is a PAC learning algorithm for C {\\displaystyle
C} . Equivalence Under some regularity conditions these conditions are
equivalent: The concept class C is PAC learnable. The VC dimension of C
is finite. C is a uniformly Glivenko-Cantelli class. C is compressible
in the sense of Littlestone and Warmuth See also Occam learning Data
mining Error tolerance (PAC learning) Sample complexity References
Further reading M. Kearns, U. Vazirani. An Introduction to Computational
Learning Theory. MIT Press, 1994. A textbook. M. Mohri, A. Rostamizadeh,
and A. Talwalkar. Foundations of Machine Learning. MIT Press, 2018.
Chapter 2 contains a detailed treatment of PAC-learnability. Readable
through open access from the publisher. D. Haussler. Overview of the
Probably Approximately Correct (PAC) Learning Framework. An introduction
to the topic. L. Valiant. Probably Approximately Correct. Basic Books,
2013. In which Valiant argues that PAC learning describes how organisms
evolve and learn. Littlestone, N.; Warmuth, M. K. (1986). \"Relating
Data Compression and Learnability\" (PDF). Archived from the original
(PDF) on 2017-09-08. {{cite journal}}: Cite journal requires \|journal=
(help) Moran, Shay; Yehudayoff, Amir (2015). \"Sample compression
schemes for VC classes\". arXiv:1503.06960 \[cs.LG\].
