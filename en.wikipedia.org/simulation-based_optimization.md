Simulation-based optimization (also known as simply simulation
optimization) integrates optimization techniques into simulation
modeling and analysis. Because of the complexity of the simulation, the
objective function may become difficult and expensive to evaluate.
Usually, the underlying simulation model is stochastic, so that the
objective function must be estimated using statistical estimation
techniques (called output analysis in simulation methodology). Once a
system is mathematically modeled, computer-based simulations provide
information about its behavior. Parametric simulation methods can be
used to improve the performance of a system. In this method, the input
of each variable is varied with other parameters remaining constant and
the effect on the design objective is observed. This is a time-consuming
method and improves the performance partially. To obtain the optimal
solution with minimum computation and time, the problem is solved
iteratively where in each iteration the solution moves closer to the
optimum solution. Such methods are known as 'numerical optimization' or
'simulation-based optimization'.In simulation experiment, the goal is to
evaluate the effect of different values of input variables on a system.
However, the interest is sometimes in finding the optimal value for
input variables in terms of the system outcomes. One way could be
running simulation experiments for all possible input variables.
However, this approach is not always practical due to several possible
situations and it just makes it intractable to run experiments for each
scenario. For example, there might be too many possible values for input
variables, or the simulation model might be too complicated and
expensive to run for suboptimal input variable values. In these cases,
the goal is to find optimal values for the input variables rather than
trying all possible values. This process is called simulation
optimization.Specific simulation--based optimization methods can be
chosen according to Figure 1 based on the decision variable types.
Optimization exists in two main branches of operations research:
Optimization parametric (static) -- The objective is to find the values
of the parameters, which are "static" for all states, with the goal of
maximizing or minimizing a function. In this case, one can use
mathematical programming, such as linear programming. In this scenario,
simulation helps when the parameters contain noise or the evaluation of
the problem would demand excessive computer time, due to its
complexity.Optimization control (dynamic) -- This is used largely in
computer science and electrical engineering. The optimal control is per
state and the results change in each of them. One can use mathematical
programming, as well as dynamic programming. In this scenario,
simulation can generate random samples and solve complex and large-scale
problems. Simulation-based optimization methods Some important
approaches in simulation optimization are discussed below. Statistical
ranking and selection methods (R/S) Ranking and selection methods are
designed for problems where the alternatives are fixed and known, and
simulation is used to estimate the system performance. In the simulation
optimization setting, applicable methods include indifference zone
approaches, optimal computing budget allocation, and knowledge gradient
algorithms. Response surface methodology (RSM) In response surface
methodology, the objective is to find the relationship between the input
variables and the response variables. The process starts from trying to
fit a linear regression model. If the P-value turns out to be low, then
a higher degree polynomial regression, which is usually quadratic, will
be implemented. The process of finding a good relationship between input
and response variables will be done for each simulation test. In
simulation optimization, response surface method can be used to find the
best input variables that produce desired outcomes in terms of response
variables. Heuristic methods Heuristic methods change accuracy by speed.
Their goal is to find a good solution faster than the traditional
methods, when they are too slow or fail in solving the problem. Usually
they find local optimal instead of the optimal value; however, the
values are considered close enough of the final solution. Examples of
these kinds of methods include tabu search and genetic
algorithms.Metamodels enable researchers to obtain reliable approximate
model outputs without running expensive and time-consuming computer
simulations. Therefore, the process of model optimization can take less
computation time and cost. Stochastic approximation Stochastic
approximation is used when the function cannot be computed directly,
only estimated via noisy observations. In these scenarios, this method
(or family of methods) looks for the extrema of these function. The
objective function would be: min x ∈ θ f ( x ) = min x ∈ θ E \[ F ( x,y
) \] {\\displaystyle {\\underset {{\\text{x}}\\in \\theta }{\\min
}}f{\\bigl (}{\\text{x}}{\\bigr )}={\\underset {{\\text{x}}\\in \\theta
}{\\min }}\\mathrm {E} \[F{\\bigl (}{\\text{x,y}})\]} y {\\displaystyle
y} is a random variable that represents the noise. x {\\displaystyle x}
is the parameter that minimizes f ( x ) {\\displaystyle f{\\bigl
(}{\\text{x}}{\\bigr )}} . θ {\\displaystyle \\theta } is the domain of
the parameter x {\\displaystyle x} . Derivative-free optimization
methods Derivative-free optimization is a subject of mathematical
optimization. This method is applied to a certain optimization problem
when its derivatives are unavailable or unreliable. Derivative-free
methods establish a model based on sample function values or directly
draw a sample set of function values without exploiting a detailed
model. Since it needs no derivatives, it cannot be compared to
derivative-based methods.For unconstrained optimization problems, it has
the form: min x ∈ R n f ( x ) {\\displaystyle {\\underset
{{\\text{x}}\\in \\mathbb {R} \^{n}}{\\min }}f{\\bigl
(}{\\text{x}}{\\bigr )}} The limitations of derivative-free
optimization: 1. Some methods cannot handle optimization problems with
more than a few variables; the results are usually not so accurate.
However, there are numerous practical cases where derivative-free
methods have been successful in non-trivial simulation optimization
problems that include randomness manifesting as \"noise\" in the
objective function. See, for example, the following .2. When confronted
with minimizing non-convex functions, it will show its limitation. 3.
Derivative-free optimization methods are relatively simple and easy,
but, like most optimization methods, some care is required in practical
implementation (e.g., in choosing the algorithm parameters). Dynamic
programming and neuro-dynamic programming Dynamic programming Dynamic
programming deals with situations where decisions are made in stages.
The key to this kind of problem is to trade off the present and future
costs.One dynamic basic model has two features: 1) It has a discrete
time dynamic system. 2) The cost function is additive over time. For
discrete features, dynamic programming has the form: x k + 1 = f k ( x k
, u k , w k ) , k = 0 , 1 , . . . , N − 1 {\\displaystyle
x\_{k+1}=f\_{k}(x\_{k},u\_{k},w\_{k}),k=0,1,\...,N-1} k {\\displaystyle
k} represents the index of discrete time. x k {\\displaystyle x\_{k}} is
the state of the time k, it contains the past information and prepares
it for future optimization. u k {\\displaystyle u\_{k}} is the control
variable. w k {\\displaystyle w\_{k}} is the random parameter.For the
cost function, it has the form: g N ( X N ) + ∑ k = 0 N − 1 g k ( x k ,
u k , W k ) {\\displaystyle g\_{N}(X\_{N})+\\sum
\_{k=0}\^{N-1}g\_{k}(x\_{k},u\_{k},W\_{k})} g N ( X N ) {\\displaystyle
g\_{N}(X\_{N})} is the cost at the end of the process. As the cost
cannot be optimized meaningfully, it can be used the expect value: E { g
N ( X N ) + ∑ k = 0 N − 1 g k ( x k , u k , W k ) } {\\displaystyle
E\\{g\_{N}(X\_{N})+\\sum \_{k=0}\^{N-1}g\_{k}(x\_{k},u\_{k},W\_{k})\\}}
Neuro-dynamic programming Neuro-dynamic programming is the same as
dynamic programming except that the former has the concept of
approximation architectures. It combines artificial intelligence,
simulation-base algorithms, and functional approach techniques. "Neuro"
in this term origins from artificial intelligence community. It means
learning how to make improved decisions for the future via built-in
mechanism based on the current behavior. The most important part of
neuro-dynamic programming is to build a trained neuro network for the
optimal problem. Limitations Simulation-based optimization has some
limitations, such as the difficulty of creating a model that imitates
the dynamic behavior of a system in a way that is considered good enough
for its representation. Another problem is complexity in the determining
uncontrollable parameters of both real-world system and simulation.
Moreover, only a statistical estimation of real values can be obtained.
It is not easy to determine the objective function, since it is a result
of measurements, which can be harmful to the solutions. == References ==
