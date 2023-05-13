SequenceL is a general purpose functional programming language and
auto-parallelizing (Parallel computing) compiler and tool set, whose
primary design objectives are performance on multi-core processor
hardware, ease of programming, platform portability/optimization, and
code clarity and readability. Its main advantage is that it can be used
to write straightforward code that automatically takes full advantage of
all the processing power available, without programmers needing to be
concerned with identifying parallelisms, specifying vectorization,
avoiding race conditions, and other challenges of manual directive-based
programming approaches such as OpenMP. Programs written in SequenceL can
be compiled to multithreaded code that runs in parallel, with no
explicit indications from a programmer of how or what to parallelize. As
of 2015, versions of the SequenceL compiler generate parallel code in
C++ and OpenCL, which allows it to work with most popular programming
languages, including C, C++, C#, Fortran, Java, and Python. A
platform-specific runtime manages the threads safely, automatically
providing parallel performance according to the number of cores
available, currently supporting x86, POWER8, and ARM platforms. History
SequenceL was initially developed over a 20-year period starting in
1989, mostly at Texas Tech University. Primary funding was from NASA,
which originally wanted to develop a specification language which was
\"self-verifying\"; that is, once written, the requirements could be
executed, and the results verified against the desired outcome. The
principal researcher on the project was initially Dr. Daniel Cooke, who
was soon joined by Dr. Nelson Rushton (another Texas Tech professor) and
later Dr. Brad Nemanich (then a PhD student under Cooke). The goal of
creating a language that was simple enough to be readable, but
unambiguous enough to be executable, drove the inventors to settle on a
functional, declarative language approach, where a programmer describes
desired results, rather than the means to achieve them. The language is
then free to solve the problem in the most efficient manner that it can
find. As the language evolved, the researchers developed new
computational approaches, including consume-simplify-produce (CSP). In
1998, research began to apply SequenceL to parallel computing. This
culminated in 2004 when it took its more complete form with the addition
of the normalize-transpose (NT) semantic, which coincided with the major
vendors of central processing units (CPUs) making a major shift to
multi-core processors rather than continuing to increase clock speeds.
NT is the semantic work-horse, being used to simplify and decompose
structures, based on a dataflow-like execution strategy similar to GAMMA
and NESL. The NT semantic achieves a goal similar to that of the Lämmel
and Peyton-Jones' boilerplate elimination. All other features of the
language are definable from these two laws - including recursion,
subscripting structures, function references, and evaluation of function
bodies.Though it was not the original intent, these new approaches
allowed the language to parallelize a large fraction of the operations
it performed, transparently to the programmer. In 2006, a prototype
auto-parallelizing compiler was developed at Texas Tech University. In
2009, Texas Tech licensed the intellectual property to Texas Multicore
Technologies (TMT), for follow-on commercial development. In January
2017 TMT released v3, which includes a free Community Edition for
download in addition to the commercial Professional Edition. Design
SequenceL is designed to be as simple as possible to learn and use,
focusing on algorithmic code where it adds value, e.g., the inventors
chose not to reinvent I/O since C handled that well. As a result, the
full language reference for SequenceL is only 40 pages, with copious
examples, and its formal grammar has around 15 production
rules.SequenceL is strictly evaluated (like Lisp), statically typed with
type inference (like Haskell), and uses a combination of infix and
prefix operators that resemble standard, informal mathematical notation
(like C, Pascal, Python, etc.). It is a purely declarative language,
meaning that a programmer defines functions, in the mathematical sense,
without giving instructions for their implementation. For example, the
mathematical definition of matrix multiplication is as follows: The
product of the m×p matrix A with the p×n matrix B is the m×n matrix
whose (i,j)\'th entry is ∑ k = 1 p A ( i , k ) B ( k , j )
{\\displaystyle \\sum \_{k=1}\^{p}A(i,k)B(k,j)} The SequenceL definition
mirrors that definition more or less exactly: matmul(A(2), B(2)) \[i,j\]
:= let k := 1\...size(B); in sum( A\[i,k\] \* B\[k,j\] ); The subscripts
following each parameter A and B on the left hand side of the definition
indicate that A and B are depth-2 structures (i.e., lists of lists of
scalars), which are here thought of as matrices. From this formal
definition, SequenceL infers the dimensions of the defined product from
the formula for its (i, j)\'th entry (as the set of pairs (i, j) for
which the right hand side is defined) and computes each entry by the
same formula as in the informal definition above. Notice there are no
explicit instructions for iteration in this definition, or for the order
in which operations are to be carried out. Because of this, the
SequenceL compiler can perform operations in any order (including
parallel order) which satisfies the defining equation. In this example,
computation of coordinates in the product will be parallelized in a way
that, for large matrices, scales linearly with the number of processors.
As noted above, SequenceL has no built-in constructs for input/output
(I/O) since it was designed to work in an additive manner with other
programming languages. The decision to compile to multithreaded C++ and
support the 20+ Simplified Wrapper and Interface Generator (SWIG)
languages (C, C++, C#, Java, Python, etc.) means it easily fits into
extant design flows, training, and tools. It can be used to enhance
extant applications, create multicore libraries, and even create
standalone applications by linking the resulting code with other code
which performs I/O tasks. SequenceL functions can also be queried from
an interpreter with given inputs, like Python and other interpreted
languages. Normalize--transpose The main non-scalar construct of
SequenceL is the sequence, which is essentially a list. Sequences may be
nested to any level. To avoid the routine use of recursion common in
many purely functional languages, SequenceL uses a technique termed
normalize--transpose (NT), in which scalar operations are automatically
distributed over elements of a sequence. For example, in SequenceL we
have \[ 1 , 2 , 3 \] + 10 == \[ 11 , 12 , 13 \] {\\displaystyle
\[1,2,3\]+10==\[11,12,13\]} This results not from overloading the \'+\'
operator, but from the effect of NT that extends to all operations, both
built-in and user-defined. As another example, if f() is a 3-argument
function whose arguments are scalars, then for any appropriate x and z
we will have f ( x , \[ 1 , 2 , 3 \] , z ) == \[ f ( x , 1 , z ) , f ( x
, 2 , z ) , f ( x , 3 , z ) \] {\\displaystyle
f(x,\[1,2,3\],z)==\[f(x,1,z),f(x,2,z),f(x,3,z)\]} The NT construct can
be used for multiple arguments at once, as in, for example \[ 1 , 2 , 3
\] + \[ 10 , 20 , 30 \] == \[ 11 , 22 , 33 \] {\\displaystyle
\[1,2,3\]+\[10,20,30\]==\[11,22,33\]} It also works when the expected
argument is a non-scalar of any type T, and the actual argument is a
list of objects of type T (or, in greater generality, any data structure
whose coordinates are of type T). For example, if A is a matrix and Xs
is a list of matrices \[X1, \..., Xn\], and given the above definition
of matrix multiply, in SequenceL we would have matmul(A,Xs) =
\[matmul(A,X1),\...,matmul(A,Xn)\] As a rule, NTs eliminate the need for
iteration, recursion, or high level functional operators to do the same
things to every member of a data structure, or to process corresponding
parts of similarly shaped structures together.This tends to account for
most uses of iteration and recursion. Example: prime numbers A good
example that demonstrates the above concepts would be in finding prime
numbers. A prime number is defined as An integer greater than 1, with no
positive divisors other than itself and 1.So a positive integer z is
prime if no numbers from 2 through z-1, inclusive, divide evenly.
SequenceL allows this problem to be programmed by literally transcribing
the above definition into the language. In SequenceL, a sequence of the
numbers from 2 through z-1, inclusive, is just (2\...(z-1)), so a
program to find all of the primes between 100 and 200 can be written:
prime(z) := z when none(z mod (2\...(z-1)) = 0); Which, in English just
says, \...return the argument if none of the numbers between 2, and 1
less than the argument itself, divide evenly into it.If that condition
isn't met, the function returns nothing. As a result, running this
program yields cmd:\>prime(17) 17 cmd:\>prime(18) empty The string
\"between 100 and 200\" doesn't appear in the program. Rather, a
programmer will typically pass that part in as the argument. Since the
program expects a scalar as an argument, passing it a sequence of
numbers instead will cause SequenceL to perform the operation on each
member of the sequence automatically. Since the function returns empty
for failing values, the result will be the input sequence, but filtered
to return only those numbers that satisfy the criteria for primes:
cmd:\>prime(100\...200)
\[101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199\]
In addition to solving this problem with a very short and readable
program, SequenceL's evaluation of the nested sequences would all be
performed in parallel. Components The following software components are
available and supported by TMT for use in writing SequenceL code. All
components are available on x86 platforms running Windows, macOS, and
most varieties of Linux (including CentOS, RedHat, OpenSUSE, and
Ubuntu), and on ARM and IBM Power platforms running most varieties of
Linux. Interpreter A command-line interpreter allows writing code
directly into a command shell, or loading code from prewritten text
files. This code can be executed, and the results evaluated, to assist
in checking code correctness, or finding a quick answer. It is also
available via the popular Eclipse integrated development environment
(IDE). Code executed in the interpreter does not run in parallel; it
executes in one thread. Compiler A command-line compiler reads SequenceL
code and generates highly parallelized, vectorized, C++, and optionally
OpenCL, which must be linked with the SequenceL runtime library to
execute. Runtime The runtime environment is a pre-compiled set of
libraries which works with the compiled parallelized C++ code to execute
optimally on the target platform. It builds on Intel Threaded Building
Blocks (TBB) and handles things such as cache optimization, memory
management, work queues-stealing, and performance monitoring. Eclipse
IDE plug-in with debugger An Eclipse integrated development environment
plug-in provides standard editing abilities (function rollup,
chromacoding, etc.), and a SequenceL debugging environment. This plug-in
runs against the SequenceL Interpreter, so cannot be used to debug the
multithreaded code; however, by providing automatic parallelization,
debugging of parallel SequenceL code is really verifying correctness of
sequential SequenceL code. That is, if it runs correctly sequentially,
it should run correctly in parallel -- so debugging in the interpreter
is sufficient. Libraries Various math and other standard function
libraries are included as SequenceL source code to streamline the
programming process and serve as best practice examples. These may be
imported, in much the same way that C or C++ libraries are #included.
See also Parallel computing Automatic parallelization tool Multi-core
processor Multiprocessing Functional programming Purely functional
programming Declarative programming Comparison of programming paradigms
Automatic vectorization Simon Peyton Jones Rosetta Code References
External links Official website Texas Multicore Technologies Why
SequenceL Works OpenMP compared to SequenceL SequenceL Features
Overview: Patented Automatic Parallelization in SequenceL YouTube: Texas
Multicore Technologies Free Downloads Programmer Resources and Education
Normalize, Transpose and Distribute: An Automatic Approach for Handling
Nonscalars US Patent 8,839,212, Method, apparatus and computer program
product for automatically generating a computer program using consume,
simplify and produce semantics with normalize, transpose and distribute
operations SequenceL examples on Rosetta Code wiki
