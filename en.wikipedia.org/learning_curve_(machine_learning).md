In machine learning, a learning curve (or training curve) plots the
optimal value of a model\'s loss function for a training set against
this loss function evaluated on a validation data set with same
parameters as produced the optimal function. It is a tool to find out
how much a machine model benefits from adding more training data and
whether the estimator suffers more from a variance error or a bias
error. If both the validation score and the training score converge to a
value that is too low with increasing size of the training set, it will
not benefit much from more training data.The machine learning curve is
useful for many purposes including comparing different algorithms,
choosing model parameters during design, adjusting optimization to
improve convergence, and determining the amount of data used for
training.In the machine learning domain, there are two implications of
learning curves differing in the x-axis of the curves, with experience
of the model graphed either as the number of training examples used for
learning or the number of iterations used in training the model. Formal
definition One model of a machine learning is producing a function,
f(x), which given some information, x, predicts some variable, y, from
training data X train {\\displaystyle X\_{\\text{train}}} and Y train
{\\displaystyle Y\_{\\text{train}}} . It is distinct from mathematical
optimization because f {\\displaystyle f} should predict well for x
{\\displaystyle x} outside of X train {\\displaystyle
X\_{\\text{train}}} . We often constrain the possible functions to a
parameterized family of functions, { f θ ( x ) : θ ∈ Θ } {\\displaystyle
\\{f\_{\\theta }(x):\\theta \\in \\Theta \\}} , so that our function is
more generalizable or so that the function has certain properties such
as those that make finding a good f {\\displaystyle f} easier, or
because we have some a priori reason to think that these properties are
true.: 172 Given that it is not possible to produce a function that
perfectly fits out data, it is then necessary to produce a loss function
L ( f θ ( X ) , Y ′ ) {\\displaystyle L(f\_{\\theta }(X),Y\')} to
measure how good our prediction is. We then define an optimization
process which finds a θ {\\displaystyle \\theta } which minimizes L ( f
θ ( X , Y ) ) {\\displaystyle L(f\_{\\theta }(X\_{,}Y))} referred to as
θ ∗ ( X , Y ) {\\displaystyle \\theta \^{\*}(X,Y)} . Training curve for
amount of data Then if our training data is { x 1 , x 2 , ... , x n } ,
{ y 1 , y 2 , ... y n } {\\displaystyle \\{x\_{1},x\_{2},\\dots
,x\_{n}\\},\\{y\_{1},y\_{2},\\dots y\_{n}\\}} and our validation data is
{ x 1 ′ , x 2 ′ , ... x m ′ } , { y 1 ′ , y 2 ′ , ... y m ′ }
{\\displaystyle \\{x\_{1}\',x\_{2}\',\\dots
x\_{m}\'\\},\\{y\_{1}\',y\_{2}\',\\dots y\_{m}\'\\}} a learning curve is
the plot of the two curves i ↦ L ( f θ ∗ ( X i , Y i ) ( X i ) , Y i )
{\\displaystyle i\\mapsto L(f\_{\\theta
\^{\*}(X\_{i},Y\_{i})}(X\_{i}),Y\_{i})} i ↦ L ( f θ ∗ ( X i , Y i ) ( X
i ′ ) , Y i ′ ) {\\displaystyle i\\mapsto L(f\_{\\theta
\^{\*}(X\_{i},Y\_{i})}(X\_{i}\'),Y\_{i}\')} where X i = { x 1 , x 2 ,
... x i } {\\displaystyle X\_{i}=\\{x\_{1},x\_{2},\\dots x\_{i}\\}}
Training curve for number of iterations Many optimization processes are
iterative, repeating the same step until the process converges to an
optimal value. Gradient descent is one such algorithm. If you define θ i
∗ {\\displaystyle \\theta \_{i}\^{\*}} as the approximation of the
optimal θ {\\displaystyle \\theta } after i {\\displaystyle i} steps, a
learning curve is the plot of i ↦ L ( f θ i ∗ ( X , Y ) ( X ) , Y )
{\\displaystyle i\\mapsto L(f\_{\\theta \_{i}\^{\*}(X,Y)}(X),Y)} i ↦ L (
f θ i ∗ ( X , Y ) ( X ′ ) , Y ′ ) {\\displaystyle i\\mapsto
L(f\_{\\theta \_{i}\^{\*}(X,Y)}(X\'),Y\')} See also Overfitting
Bias--variance tradeoff Model selection Cross-validation (statistics)
Validity (statistics) Verification and validation == References ==
