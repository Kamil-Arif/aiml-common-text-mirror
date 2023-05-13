Dynamic programming is both a mathematical optimization method and a
computer programming method. The method was developed by Richard Bellman
in the 1950s and has found applications in numerous fields, from
aerospace engineering to economics. In both contexts it refers to
simplifying a complicated problem by breaking it down into simpler
sub-problems in a recursive manner. While some decision problems cannot
be taken apart this way, decisions that span several points in time do
often break apart recursively. Likewise, in computer science, if a
problem can be solved optimally by breaking it into sub-problems and
then recursively finding the optimal solutions to the sub-problems, then
it is said to have optimal substructure. If sub-problems can be nested
recursively inside larger problems, so that dynamic programming methods
are applicable, then there is a relation between the value of the larger
problem and the values of the sub-problems. In the optimization
literature this relationship is called the Bellman equation. Overview
Mathematical optimization In terms of mathematical optimization, dynamic
programming usually refers to simplifying a decision by breaking it down
into a sequence of decision steps over time. This is done by defining a
sequence of value functions V1, V2, \..., Vn taking y as an argument
representing the state of the system at times i from 1 to n. The
definition of Vn(y) is the value obtained in state y at the last time n.
The values Vi at earlier times i = n −1, n − 2, \..., 2, 1 can be found
by working backwards, using a recursive relationship called the Bellman
equation. For i = 2, \..., n, Vi−1 at any state y is calculated from Vi
by maximizing a simple function (usually the sum) of the gain from a
decision at time i − 1 and the function Vi at the new state of the
system if this decision is made. Since Vi has already been calculated
for the needed states, the above operation yields Vi−1 for those states.
Finally, V1 at the initial state of the system is the value of the
optimal solution. The optimal values of the decision variables can be
recovered, one by one, by tracking back the calculations already
performed. Control theory In control theory, a typical problem is to
find an admissible control u ∗ {\\displaystyle \\mathbf {u} \^{\\ast }}
which causes the system x ˙ ( t ) = g ( x ( t ) , u ( t ) , t )
{\\displaystyle {\\dot {\\mathbf {x} }}(t)=\\mathbf {g} \\left(\\mathbf
{x} (t),\\mathbf {u} (t),t\\right)} to follow an admissible trajectory x
∗ {\\displaystyle \\mathbf {x} \^{\\ast }} on a continuous time interval
t 0 ≤ t ≤ t 1 {\\displaystyle t\_{0}\\leq t\\leq t\_{1}} that minimizes
a cost function J = b ( x ( t 1 ) , t 1 ) + ∫ t 0 t 1 f ( x ( t ) , u (
t ) , t ) d t {\\displaystyle J=b\\left(\\mathbf {x}
(t\_{1}),t\_{1}\\right)+\\int \_{t\_{0}}\^{t\_{1}}f\\left(\\mathbf {x}
(t),\\mathbf {u} (t),t\\right)\\mathrm {d} t} The solution to this
problem is an optimal control law or policy u ∗ = h ( x ( t ) , t )
{\\displaystyle \\mathbf {u} \^{\\ast }=h(\\mathbf {x} (t),t)} , which
produces an optimal trajectory x ∗ {\\displaystyle \\mathbf {x} \^{\\ast
}} and a cost-to-go function J ∗ {\\displaystyle J\^{\\ast }} . The
latter obeys the fundamental equation of dynamic programming: − J t ∗ =
min u { f ( x ( t ) , u ( t ) , t ) + J x ∗ T g ( x ( t ) , u ( t ) , t
) } {\\displaystyle -J\_{t}\^{\\ast }=\\min \_{\\mathbf {u}
}\\left\\{f\\left(\\mathbf {x} (t),\\mathbf {u}
(t),t\\right)+J\_{x}\^{\\ast {\\mathsf {T}}}\\mathbf {g} \\left(\\mathbf
{x} (t),\\mathbf {u} (t),t\\right)\\right\\}} a partial differential
equation known as the Hamilton--Jacobi--Bellman equation, in which J x ∗
= ∂ J ∗ ∂ x = \[ ∂ J ∗ ∂ x 1 ∂ J ∗ ∂ x 2 ... ∂ J ∗ ∂ x n \] T
{\\displaystyle J\_{x}\^{\\ast }={\\frac {\\partial J\^{\\ast
}}{\\partial \\mathbf {x} }}=\\left\[{\\frac {\\partial J\^{\\ast
}}{\\partial x\_{1}}}\~\~\~\~{\\frac {\\partial J\^{\\ast }}{\\partial
x\_{2}}}\~\~\~\~\\dots \~\~\~\~{\\frac {\\partial J\^{\\ast }}{\\partial
x\_{n}}}\\right\]\^{\\mathsf {T}}} and J t ∗ = ∂ J ∗ ∂ t {\\displaystyle
J\_{t}\^{\\ast }={\\frac {\\partial J\^{\\ast }}{\\partial t}}} . One
finds that minimizing u {\\displaystyle \\mathbf {u} } in terms of t
{\\displaystyle t} , x {\\displaystyle \\mathbf {x} } , and the unknown
function J x ∗ {\\displaystyle J\_{x}\^{\\ast }} and then substitutes
the result into the Hamilton--Jacobi--Bellman equation to get the
partial differential equation to be solved with boundary condition J ( t
1 ) = b ( x ( t 1 ) , t 1 ) {\\displaystyle
J\\left(t\_{1}\\right)=b\\left(\\mathbf {x} (t\_{1}),t\_{1}\\right)} .
In practice, this generally requires numerical techniques for some
discrete approximation to the exact optimization relationship.
Alternatively, the continuous process can be approximated by a discrete
system, which leads to a following recurrence relation analog to the
Hamilton--Jacobi--Bellman equation: J k ∗ ( x n − k ) = min u n − k { f
\^ ( x n − k , u n − k ) + J k − 1 ∗ ( g \^ ( x n − k , u n − k ) ) }
{\\displaystyle J\_{k}\^{\\ast }\\left(\\mathbf {x}
\_{n-k}\\right)=\\min \_{\\mathbf {u} \_{n-k}}\\left\\{{\\hat
{f}}\\left(\\mathbf {x} \_{n-k},\\mathbf {u}
\_{n-k}\\right)+J\_{k-1}\^{\\ast }\\left({\\hat {\\mathbf {g}
}}\\left(\\mathbf {x} \_{n-k},\\mathbf {u}
\_{n-k}\\right)\\right)\\right\\}} at the k {\\displaystyle k} -th stage
of n {\\displaystyle n} equally spaced discrete time intervals, and
where f \^ {\\displaystyle {\\hat {f}}} and g \^ {\\displaystyle {\\hat
{\\mathbf {g} }}} denote discrete approximations to f {\\displaystyle f}
and g {\\displaystyle \\mathbf {g} } . This functional equation is known
as the Bellman equation, which can be solved for an exact solution of
the discrete approximation of the optimization equation. Example from
economics: Ramsey\'s problem of optimal saving In economics, the
objective is generally to maximize (rather than minimize) some dynamic
social welfare function. In Ramsey\'s problem, this function relates
amounts of consumption to levels of utility. Loosely speaking, the
planner faces the trade-off between contemporaneous consumption and
future consumption (via investment in capital stock that is used in
production), known as intertemporal choice. Future consumption is
discounted at a constant rate β ∈ ( 0 , 1 ) {\\displaystyle \\beta \\in
(0,1)} . A discrete approximation to the transition equation of capital
is given by k t + 1 = g \^ ( k t , c t ) = f ( k t ) − c t
{\\displaystyle k\_{t+1}={\\hat
{g}}\\left(k\_{t},c\_{t}\\right)=f(k\_{t})-c\_{t}} where c
{\\displaystyle c} is consumption, k {\\displaystyle k} is capital, and
f {\\displaystyle f} is a production function satisfying the Inada
conditions. An initial capital stock k 0 \> 0 {\\displaystyle k\_{0}\>0}
is assumed. Let c t {\\displaystyle c\_{t}} be consumption in period t,
and assume consumption yields utility u ( c t ) = ln ⁡ ( c t )
{\\displaystyle u(c\_{t})=\\ln(c\_{t})} as long as the consumer lives.
Assume the consumer is impatient, so that he discounts future utility by
a factor b each period, where 0 \< b \< 1 {\\displaystyle 0 0
{\\displaystyle k\_{0}\>0} , and suppose that this period\'s capital and
consumption determine next period\'s capital as k t + 1 = A k t a − c t
{\\displaystyle k\_{t+1}=Ak\_{t}\^{a}-c\_{t}} , where A is a positive
constant and 0 \< a \< 1 {\\displaystyle 0 n c ( i , j ) i = 1 min ( q (
i − 1 , j − 1 ) , q ( i − 1 , j ) , q ( i − 1 , j + 1 ) ) + c ( i , j )
otherwise. {\\displaystyle q(i,j)={\\begin{cases}\\infty &j\<1{\\text{
or
}}j\>n\\\\c(i,j)&i=1\\\\\\min(q(i-1,j-1),q(i-1,j),q(i-1,j+1))+c(i,j)&{\\text{otherwise.}}\\end{cases}}}
The first line of this equation deals with a board modeled as squares
indexed on 1 at the lowest bound and n at the highest bound. The second
line specifies what happens at the first rank; providing a base case.
The third line, the recursion, is the important part. It represents the
A,B,C,D terms in the example. From this definition we can derive
straightforward recursive code for q(i, j). In the following pseudocode,
n is the size of the board, c(i, j) is the cost function, and min()
returns the minimum of a number of values: function minCost(i, j) if j
\< 1 or j \> n return infinity else if i = 1 return c(i, j) else return
min( minCost(i-1, j-1), minCost(i-1, j), minCost(i-1, j+1) ) + c(i, j)
This function only computes the path cost, not the actual path. We
discuss the actual path below. This, like the Fibonacci-numbers example,
is horribly slow because it too exhibits the overlapping sub-problems
attribute. That is, it recomputes the same path costs over and over.
However, we can compute it much faster in a bottom-up fashion if we
store path costs in a two-dimensional array q\[i, j\] rather than using
a function. This avoids recomputation; all the values needed for array
q\[i, j\] are computed ahead of time only once. Precomputed values for
(i,j) are simply looked up whenever needed. We also need to know what
the actual shortest path is. To do this, we use another array p\[i, j\];
a predecessor array. This array records the path to any square s. The
predecessor of s is modeled as an offset relative to the index (in q\[i,
j\]) of the precomputed path cost of s. To reconstruct the complete
path, we lookup the predecessor of s, then the predecessor of that
square, then the predecessor of that square, and so on recursively,
until we reach the starting square. Consider the following pseudocode:
function computeShortestPathArrays() for x from 1 to n q\[1, x\] := c(1,
x) for y from 1 to n q\[y, 0\] := infinity q\[y, n + 1\] := infinity for
y from 2 to n for x from 1 to n m := min(q\[y-1, x-1\], q\[y-1, x\],
q\[y-1, x+1\]) q\[y, x\] := m + c(y, x) if m = q\[y-1, x-1\] p\[y, x\]
:= -1 else if m = q\[y-1, x\] p\[y, x\] := 0 else p\[y, x\] := 1 Now the
rest is a simple matter of finding the minimum and printing it. function
computeShortestPath() computeShortestPathArrays() minIndex := 1 min :=
q\[n, 1\] for i from 2 to n if q\[n, i\] \< min minIndex := i min :=
q\[n, i\] printPath(n, minIndex) function printPath(y, x) print(x)
print(\"\<-\") if y = 2 print(x + p\[y, x\]) else printPath(y-1, x +
p\[y, x\]) Sequence alignment In genetics, sequence alignment is an
important application where dynamic programming is essential. Typically,
the problem consists of transforming one sequence into another using
edit operations that replace, insert, or remove an element. Each
operation has an associated cost, and the goal is to find the sequence
of edits with the lowest total cost. The problem can be stated naturally
as a recursion, a sequence A is optimally edited into a sequence B by
either: inserting the first character of B, and performing an optimal
alignment of A and the tail of B deleting the first character of A, and
performing the optimal alignment of the tail of A and B replacing the
first character of A with the first character of B, and performing
optimal alignments of the tails of A and B.The partial alignments can be
tabulated in a matrix, where cell (i,j) contains the cost of the optimal
alignment of A\[1..i\] to B\[1..j\]. The cost in cell (i,j) can be
calculated by adding the cost of the relevant operations to the cost of
its neighboring cells, and selecting the optimum. Different variants
exist, see Smith--Waterman algorithm and Needleman--Wunsch algorithm.
Tower of Hanoi puzzle The Tower of Hanoi or Towers of Hanoi is a
mathematical game or puzzle. It consists of three rods, and a number of
disks of different sizes which can slide onto any rod. The puzzle starts
with the disks in a neat stack in ascending order of size on one rod,
the smallest at the top, thus making a conical shape. The objective of
the puzzle is to move the entire stack to another rod, obeying the
following rules: Only one disk may be moved at a time. Each move
consists of taking the upper disk from one of the rods and sliding it
onto another rod, on top of the other disks that may already be present
on that rod. No disk may be placed on top of a smaller disk.The dynamic
programming solution consists of solving the functional equation
S(n,h,t) = S(n-1,h, not(h,t)) ; S(1,h,t) ; S(n-1,not(h,t),t)where n
denotes the number of disks to be moved, h denotes the home rod, t
denotes the target rod, not(h,t) denotes the third rod (neither h nor
t), \";\" denotes concatenation, and S(n, h, t) := solution to a problem
consisting of n disks that are to be moved from rod h to rod t.For n=1
the problem is trivial, namely S(1,h,t) = \"move a disk from rod h to
rod t\" (there is only one disk left). The number of moves required by
this solution is 2n − 1. If the objective is to maximize the number of
moves (without cycling) then the dynamic programming functional equation
is slightly more complicated and 3n − 1 moves are required. Egg dropping
puzzle The following is a description of the instance of this famous
puzzle involving N=2 eggs and a building with H=36 floors: Suppose that
we wish to know which stories in a 36-story building are safe to drop
eggs from, and which will cause the eggs to break on landing (using U.S.
English terminology, in which the first floor is at ground level). We
make a few assumptions:An egg that survives a fall can be used again. A
broken egg must be discarded. The effect of a fall is the same for all
eggs. If an egg breaks when dropped, then it would break if dropped from
a higher window. If an egg survives a fall, then it would survive a
shorter fall. It is not ruled out that the first-floor windows break
eggs, nor is it ruled out that eggs can survive the 36th-floor
windows.If only one egg is available and we wish to be sure of obtaining
the right result, the experiment can be carried out in only one way.
Drop the egg from the first-floor window; if it survives, drop it from
the second-floor window. Continue upward until it breaks. In the worst
case, this method may require 36 droppings. Suppose 2 eggs are
available. What is the lowest number of egg-droppings that is guaranteed
to work in all cases?To derive a dynamic programming functional equation
for this puzzle, let the state of the dynamic programming model be a
pair s = (n,k), where n = number of test eggs available, n = 0, 1, 2, 3,
\..., N − 1. k = number of (consecutive) floors yet to be tested, k = 0,
1, 2, \..., H − 1.For instance, s = (2,6) indicates that two test eggs
are available and 6 (consecutive) floors are yet to be tested. The
initial state of the process is s = (N,H) where N denotes the number of
test eggs available at the commencement of the experiment. The process
terminates either when there are no more test eggs (n = 0) or when k =
0, whichever occurs first. If termination occurs at state s = (0,k) and
k \> 0, then the test failed. Now, let W(n,k) = minimum number of trials
required to identify the value of the critical floor under the
worst-case scenario given that the process is in state s = (n,k).Then it
can be shown that W(n,k) = 1 + min{max(W(n − 1, x − 1), W(n,k − x)): x =
1, 2, \..., k }with W(n,0) = 0 for all n \> 0 and W(1,k) = k for all k.
It is easy to solve this equation iteratively by systematically
increasing the values of n and k. Faster DP solution using a different
parametrization Notice that the above solution takes O ( n k 2 )
{\\displaystyle O(nk\^{2})} time with a DP solution. This can be
improved to O ( n k log ⁡ k ) {\\displaystyle O(nk\\log k)} time by
binary searching on the optimal x {\\displaystyle x} in the above
recurrence, since W ( n − 1 , x − 1 ) {\\displaystyle W(n-1,x-1)} is
increasing in x {\\displaystyle x} while W ( n , k − x ) {\\displaystyle
W(n,k-x)} is decreasing in x {\\displaystyle x} , thus a local minimum
of max ( W ( n − 1 , x − 1 ) , W ( n , k − x ) ) {\\displaystyle
\\max(W(n-1,x-1),W(n,k-x))} is a global minimum. Also, by storing the
optimal x {\\displaystyle x} for each cell in the DP table and referring
to its value for the previous cell, the optimal x {\\displaystyle x} for
each cell can be found in constant time, improving it to O ( n k )
{\\displaystyle O(nk)} time. However, there is an even faster solution
that involves a different parametrization of the problem: Let k
{\\displaystyle k} be the total number of floors such that the eggs
break when dropped from the k {\\displaystyle k} th floor (The example
above is equivalent to taking k = 37 {\\displaystyle k=37} ). Let m
{\\displaystyle m} be the minimum floor from which the egg must be
dropped to be broken. Let f ( t , n ) {\\displaystyle f(t,n)} be the
maximum number of values of m {\\displaystyle m} that are
distinguishable using t {\\displaystyle t} tries and n {\\displaystyle
n} eggs. Then f ( t , 0 ) = f ( 0 , n ) = 1 {\\displaystyle
f(t,0)=f(0,n)=1} for all t , n ≥ 0 {\\displaystyle t,n\\geq 0} . Let a
{\\displaystyle a} be the floor from which the first egg is dropped in
the optimal strategy. If the first egg broke, m {\\displaystyle m} is
from 1 {\\displaystyle 1} to a {\\displaystyle a} and distinguishable
using at most t − 1 {\\displaystyle t-1} tries and n − 1 {\\displaystyle
n-1} eggs. If the first egg did not break, m {\\displaystyle m} is from
a + 1 {\\displaystyle a+1} to k {\\displaystyle k} and distinguishable
using t − 1 {\\displaystyle t-1} tries and n {\\displaystyle n} eggs.
Therefore, f ( t , n ) = f ( t − 1 , n − 1 ) + f ( t − 1 , n )
{\\displaystyle f(t,n)=f(t-1,n-1)+f(t-1,n)} . Then the problem is
equivalent to finding the minimum x {\\displaystyle x} such that f ( x ,
n ) ≥ k {\\displaystyle f(x,n)\\geq k} . To do so, we could compute { f
( t , i ) : 0 ≤ i ≤ n } {\\displaystyle \\{f(t,i):0\\leq i\\leq n\\}} in
order of increasing t {\\displaystyle t} , which would take O ( n x )
{\\displaystyle O(nx)} time. Thus, if we separately handle the case of n
= 1 {\\displaystyle n=1} , the algorithm would take O ( n k )
{\\displaystyle O(n{\\sqrt {k}})} time. But the recurrence relation can
in fact be solved, giving f ( t , n ) = ∑ i = 0 n ( t i )
{\\displaystyle f(t,n)=\\sum \_{i=0}\^{n}{\\binom {t}{i}}} , which can
be computed in O ( n ) {\\displaystyle O(n)} time using the identity ( t
i + 1 ) = ( t i ) t − i i + 1 {\\displaystyle {\\binom
{t}{i+1}}={\\binom {t}{i}}{\\frac {t-i}{i+1}}} for all i ≥ 0
{\\displaystyle i\\geq 0} . Since f ( t , n ) ≤ f ( t + 1 , n )
{\\displaystyle f(t,n)\\leq f(t+1,n)} for all t ≥ 0 {\\displaystyle
t\\geq 0} , we can binary search on t {\\displaystyle t} to find x
{\\displaystyle x} , giving an O ( n log ⁡ k ) {\\displaystyle O(n\\log
k)} algorithm. Matrix chain multiplication Matrix chain multiplication
is a well-known example that demonstrates utility of dynamic
programming. For example, engineering applications often have to
multiply a chain of matrices. It is not surprising to find matrices of
large dimensions, for example 100×100. Therefore, our task is to
multiply matrices A 1 , A 2 , . . . . A n {\\displaystyle
A\_{1},A\_{2},\....A\_{n}} . Matrix multiplication is not commutative,
but is associative; and we can multiply only two matrices at a time. So,
we can multiply this chain of matrices in many different ways, for
example: ((A1 × A2) × A3) × \... AnA1×(((A2×A3)× \... ) × An)(A1 × A2) ×
(A3 × \... An)and so on. There are numerous ways to multiply this chain
of matrices. They will all produce the same final result, however they
will take more or less time to compute, based on which particular
matrices are multiplied. If matrix A has dimensions m×n and matrix B has
dimensions n×q, then matrix C=A×B will have dimensions m×q, and will
require m\*n\*q scalar multiplications (using a simplistic matrix
multiplication algorithm for purposes of illustration). For example, let
us multiply matrices A, B and C. Let us assume that their dimensions are
m×n, n×p, and p×s, respectively. Matrix A×B×C will be of size m×s and
can be calculated in two ways shown below: Ax(B×C) This order of matrix
multiplication will require nps + mns scalar multiplications. (A×B)×C
This order of matrix multiplication will require mnp + mps scalar
calculations.Let us assume that m = 10, n = 100, p = 10 and s = 1000.
So, the first way to multiply the chain will require 1,000,000 +
1,000,000 calculations. The second way will require only 10,000+100,000
calculations. Obviously, the second way is faster, and we should
multiply the matrices using that arrangement of parenthesis. Therefore,
our conclusion is that the order of parenthesis matters, and that our
task is to find the optimal order of parenthesis. At this point, we have
several choices, one of which is to design a dynamic programming
algorithm that will split the problem into overlapping problems and
calculate the optimal arrangement of parenthesis. The dynamic
programming solution is presented below. Let\'s call m\[i,j\] the
minimum number of scalar multiplications needed to multiply a chain of
matrices from matrix i to matrix j (i.e. Ai × \.... × Aj, i.e. i\<=j).
We split the chain at some matrix k, such that i \<= k \< j, and try to
find out which combination produces minimum m\[i,j\]. The formula is: if
i = j, m\[i,j\]= 0 if i \< j, m\[i,j\]= min over all possible values of
k (m\[i,k\]+m\[k+1,j\] + p i − 1 ∗ p k ∗ p j {\\displaystyle
p\_{i-1}\*p\_{k}\*p\_{j}} ) where k ranges from i to j − 1. p i − 1
{\\displaystyle p\_{i-1}} is the row dimension of matrix i, p k
{\\displaystyle p\_{k}} is the column dimension of matrix k, p j
{\\displaystyle p\_{j}} is the column dimension of matrix j.This formula
can be coded as shown below, where input parameter \"chain\" is the
chain of matrices, i.e. A 1 , A 2 , . . . A n {\\displaystyle
A\_{1},A\_{2},\...A\_{n}} : function
OptimalMatrixChainParenthesis(chain) n = length(chain) for i = 1, n
m\[i,i\] = 0 // Since it takes no calculations to multiply one matrix
for len = 2, n for i = 1, n - len + 1 j = i + len -1 m\[i,j\] = infinity
// So that the first calculation updates for k = i, j-1 q = m\[i, k\] +
m\[k+1, j\] + p i − 1 ∗ p k ∗ p j {\\displaystyle
p\_{i-1}\*p\_{k}\*p\_{j}} if q \< m\[i, j\] // The new order of
parentheses is better than what we had m\[i, j\] = q // Update s\[i, j\]
= k // Record which k to split on, i.e. where to place the parenthesis
So far, we have calculated values for all possible m\[i, j\], the
minimum number of calculations to multiply a chain from matrix i to
matrix j, and we have recorded the corresponding \"split point\"s\[i,
j\]. For example, if we are multiplying chain A1×A2×A3×A4, and it turns
out that m\[1, 3\] = 100 and s\[1, 3\] = 2, that means that the optimal
placement of parenthesis for matrices 1 to 3 is ( A 1 × A 2 ) × A 3
{\\displaystyle (A\_{1}\\times A\_{2})\\times A\_{3}} and to multiply
those matrices will require 100 scalar calculations. This algorithm will
produce \"tables\" m\[, \] and s\[, \] that will have entries for all
possible values of i and j. The final solution for the entire chain is
m\[1, n\], with corresponding split at s\[1, n\]. Unraveling the
solution will be recursive, starting from the top and continuing until
we reach the base case, i.e. multiplication of single matrices.
Therefore, the next step is to actually split the chain, i.e. to place
the parenthesis where they (optimally) belong. For this purpose we could
use the following algorithm: function PrintOptimalParenthesis(s, i, j)
if i = j print \"A\"i else print \"(\" PrintOptimalParenthesis(s, i,
s\[i, j\]) PrintOptimalParenthesis(s, s\[i, j\] + 1, j) print \")\" Of
course, this algorithm is not useful for actual multiplication. This
algorithm is just a user-friendly way to see what the result looks like.
To actually multiply the matrices using the proper splits, we need the
following algorithm: History The term dynamic programming was originally
used in the 1940s by Richard Bellman to describe the process of solving
problems where one needs to find the best decisions one after another.
By 1953, he refined this to the modern meaning, referring specifically
to nesting smaller decision problems inside larger decisions, and the
field was thereafter recognized by the IEEE as a systems analysis and
engineering topic. Bellman\'s contribution is remembered in the name of
the Bellman equation, a central result of dynamic programming which
restates an optimization problem in recursive form. Bellman explains the
reasoning behind the term dynamic programming in his autobiography, Eye
of the Hurricane: An Autobiography: I spent the Fall quarter (of 1950)
at RAND. My first task was to find a name for multistage decision
processes. An interesting question is, \"Where did the name, dynamic
programming, come from?\" The 1950s were not good years for mathematical
research. We had a very interesting gentleman in Washington named
Wilson. He was Secretary of Defense, and he actually had a pathological
fear and hatred of the word \"research\". I'm not using the term
lightly; I'm using it precisely. His face would suffuse, he would turn
red, and he would get violent if people used the term research in his
presence. You can imagine how he felt, then, about the term
mathematical. The RAND Corporation was employed by the Air Force, and
the Air Force had Wilson as its boss, essentially. Hence, I felt I had
to do something to shield Wilson and the Air Force from the fact that I
was really doing mathematics inside the RAND Corporation. What title,
what name, could I choose? In the first place I was interested in
planning, in decision making, in thinking. But planning, is not a good
word for various reasons. I decided therefore to use the word
\"programming\". I wanted to get across the idea that this was dynamic,
this was multistage, this was time-varying. I thought, let\'s kill two
birds with one stone. Let\'s take a word that has an absolutely precise
meaning, namely dynamic, in the classical physical sense. It also has a
very interesting property as an adjective, and that is it\'s impossible
to use the word dynamic in a pejorative sense. Try thinking of some
combination that will possibly give it a pejorative meaning. It\'s
impossible. Thus, I thought dynamic programming was a good name. It was
something not even a Congressman could object to. So I used it as an
umbrella for my activities. The word dynamic was chosen by Bellman to
capture the time-varying aspect of the problems, and because it sounded
impressive. The word programming referred to the use of the method to
find an optimal program, in the sense of a military schedule for
training or logistics. This usage is the same as that in the phrases
linear programming and mathematical programming, a synonym for
mathematical optimization.The above explanation of the origin of the
term is lacking. As Russell and Norvig in their book have written,
referring to the above story: \"This cannot be strictly true, because
his first paper using the term (Bellman, 1952) appeared before Wilson
became Secretary of Defense in 1953.\" Also, there is a comment in a
speech by Harold J. Kushner, where he remembers Bellman. Quoting Kushner
as he speaks of Bellman: \"On the other hand, when I asked him the same
question, he replied that he was trying to upstage Dantzig\'s linear
programming by adding dynamic. Perhaps both motivations were true.\"
Algorithms that use dynamic programming Recurrent solutions to lattice
models for protein-DNA binding Backward induction as a solution method
for finite-horizon discrete-time dynamic optimization problems Method of
undetermined coefficients can be used to solve the Bellman equation in
infinite-horizon, discrete-time, discounted, time-invariant dynamic
optimization problems Many string algorithms including longest common
subsequence, longest increasing subsequence, longest common substring,
Levenshtein distance (edit distance) Many algorithmic problems on graphs
can be solved efficiently for graphs of bounded treewidth or bounded
clique-width by using dynamic programming on a tree decomposition of the
graph. The Cocke--Younger--Kasami (CYK) algorithm which determines
whether and how a given string can be generated by a given context-free
grammar Knuth\'s word wrapping algorithm that minimizes raggedness when
word wrapping text The use of transposition tables and refutation tables
in computer chess The Viterbi algorithm (used for hidden Markov models,
and particularly in part of speech tagging) The Earley algorithm (a type
of chart parser) The Needleman--Wunsch algorithm and other algorithms
used in bioinformatics, including sequence alignment, structural
alignment, RNA structure prediction Floyd\'s all-pairs shortest path
algorithm Optimizing the order for chain matrix multiplication
Pseudo-polynomial time algorithms for the subset sum, knapsack and
partition problems The dynamic time warping algorithm for computing the
global distance between two time series The Selinger (a.k.a. System R)
algorithm for relational database query optimization De Boor algorithm
for evaluating B-spline curves Duckworth--Lewis method for resolving the
problem when games of cricket are interrupted The value iteration method
for solving Markov decision processes Some graphic image edge following
selection methods such as the \"magnet\" selection tool in Photoshop
Some methods for solving interval scheduling problems Some methods for
solving the travelling salesman problem, either exactly (in exponential
time) or approximately (e.g. via the bitonic tour) Recursive least
squares method Beat tracking in music information retrieval
Adaptive-critic training strategy for artificial neural networks Stereo
algorithms for solving the correspondence problem used in stereo vision
Seam carving (content-aware image resizing) The Bellman--Ford algorithm
for finding the shortest distance in a graph Some approximate solution
methods for the linear search problem Kadane\'s algorithm for the
maximum subarray problem Optimization of electric generation expansion
plans in the Wein Automatic System Planning (WASP) package See also
References Further reading Adda, Jerome; Cooper, Russell (2003), Dynamic
Economics, MIT Press, ISBN 9780262012010. An accessible introduction to
dynamic programming in economics. MATLAB code for the book Archived
2020-10-09 at the Wayback Machine. Bellman, Richard (1954), \"The theory
of dynamic programming\", Bulletin of the American Mathematical Society,
60 (6): 503--516, doi:10.1090/S0002-9904-1954-09848-8, MR 0067459.
Includes an extensive bibliography of the literature in the area, up to
the year 1954. Bellman, Richard (1957), Dynamic Programming, Princeton
University Press. Dover paperback edition (2003), ISBN 0-486-42809-5.
Cormen, Thomas H.; Leiserson, Charles E.; Rivest, Ronald L.; Stein,
Clifford (2001), Introduction to Algorithms (2nd ed.), MIT Press &
McGraw--Hill, ISBN 978-0-262-03293-3. Especially pp. 323--69. Dreyfus,
Stuart E.; Law, Averill M. (1977), The Art and Theory of Dynamic
Programming, Academic Press, ISBN 978-0-12-221860-6. Giegerich, R.;
Meyer, C.; Steffen, P. (2004), \"A Discipline of Dynamic Programming
over Sequence Data\" (PDF), Science of Computer Programming, 51 (3):
215--263, doi:10.1016/j.scico.2003.12.005. Meyn, Sean (2007), Control
Techniques for Complex Networks, Cambridge University Press, ISBN
978-0-521-88441-9, archived from the original on 2010-06-19. Sritharan,
S. S. (1991). \"Dynamic Programming of the Navier-Stokes Equations\".
Systems and Control Letters. 16 (4): 299--307.
doi:10.1016/0167-6911(91)90020-f. Stokey, Nancy; Lucas, Robert E.;
Prescott, Edward (1989), Recursive Methods in Economic Dynamics, Harvard
Univ. Press, ISBN 978-0-674-75096-8. External links A Tutorial on
Dynamic programming MIT course on algorithms - Includes 4 video lectures
on DP, lectures 15-18 Applied Mathematical Programming by Bradley, Hax,
and Magnanti, Chapter 11 More DP Notes King, Ian, 2002 (1987), \"A
Simple Introduction to Dynamic Programming in Macroeconomic Models.\" An
introduction to dynamic programming as an important tool in economic
theory. Dynamic Programming: from novice to advanced A TopCoder.com
article by Dumitru on Dynamic Programming Algebraic Dynamic Programming
-- a formalized framework for dynamic programming, including an
entry-level course to DP, University of Bielefeld Dreyfus, Stuart,
\"Richard Bellman on the birth of Dynamic Programming.\" Dynamic
programming tutorial A Gentle Introduction to Dynamic Programming and
the Viterbi Algorithm Tabled Prolog BProlog, XSB, SWI-Prolog IFORS
online interactive dynamic programming modules including, shortest path,
traveling salesman, knapsack, false coin, egg dropping, bridge and
torch, replacement, chained matrix products, and critical path problem.
