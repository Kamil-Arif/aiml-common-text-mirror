In machine learning, hyperparameter optimization or tuning is the
problem of choosing a set of optimal hyperparameters for a learning
algorithm. A hyperparameter is a parameter whose value is used to
control the learning process. By contrast, the values of other
parameters (typically node weights) are learned. The same kind of
machine learning model can require different constraints, weights or
learning rates to generalize different data patterns. These measures are
called hyperparameters, and have to be tuned so that the model can
optimally solve the machine learning problem. Hyperparameter
optimization finds a tuple of hyperparameters that yields an optimal
model which minimizes a predefined loss function on given independent
data. The objective function takes a tuple of hyperparameters and
returns the associated loss. Cross-validation is often used to estimate
this generalization performance. Approaches Grid search The traditional
way of performing hyperparameter optimization has been grid search, or a
parameter sweep, which is simply an exhaustive searching through a
manually specified subset of the hyperparameter space of a learning
algorithm. A grid search algorithm must be guided by some performance
metric, typically measured by cross-validation on the training set or
evaluation on a hold-out validation set.Since the parameter space of a
machine learner may include real-valued or unbounded value spaces for
certain parameters, manually set bounds and discretization may be
necessary before applying grid search. For example, a typical
soft-margin SVM classifier equipped with an RBF kernel has at least two
hyperparameters that need to be tuned for good performance on unseen
data: a regularization constant C and a kernel hyperparameter γ. Both
parameters are continuous, so to perform grid search, one selects a
finite set of \"reasonable\" values for each, say C ∈ { 10 , 100 , 1000
} {\\displaystyle C\\in \\{10,100,1000\\}} γ ∈ { 0.1 , 0.2 , 0.5 , 1.0 }
{\\displaystyle \\gamma \\in \\{0.1,0.2,0.5,1.0\\}} Grid search then
trains an SVM with each pair (C, γ) in the Cartesian product of these
two sets and evaluates their performance on a held-out validation set
(or by internal cross-validation on the training set, in which case
multiple SVMs are trained per pair). Finally, the grid search algorithm
outputs the settings that achieved the highest score in the validation
procedure. Grid search suffers from the curse of dimensionality, but is
often embarrassingly parallel because the hyperparameter settings it
evaluates are typically independent of each other. Random search Random
Search replaces the exhaustive enumeration of all combinations by
selecting them randomly. This can be simply applied to the discrete
setting described above, but also generalizes to continuous and mixed
spaces. It can outperform Grid search, especially when only a small
number of hyperparameters affects the final performance of the machine
learning algorithm. In this case, the optimization problem is said to
have a low intrinsic dimensionality. Random Search is also
embarrassingly parallel, and additionally allows the inclusion of prior
knowledge by specifying the distribution from which to sample. Despite
its simplicity, random search remains one of the important base-lines
against which to compare the performance of new hyperparameter
optimization methods. Bayesian optimization Bayesian optimization is a
global optimization method for noisy black-box functions. Applied to
hyperparameter optimization, Bayesian optimization builds a
probabilistic model of the function mapping from hyperparameter values
to the objective evaluated on a validation set. By iteratively
evaluating a promising hyperparameter configuration based on the current
model, and then updating it, Bayesian optimization aims to gather
observations revealing as much information as possible about this
function and, in particular, the location of the optimum. It tries to
balance exploration (hyperparameters for which the outcome is most
uncertain) and exploitation (hyperparameters expected close to the
optimum). In practice, Bayesian optimization has been shown to obtain
better results in fewer evaluations compared to grid search and random
search, due to the ability to reason about the quality of experiments
before they are run. Gradient-based optimization For specific learning
algorithms, it is possible to compute the gradient with respect to
hyperparameters and then optimize the hyperparameters using gradient
descent. The first usage of these techniques was focused on neural
networks. Since then, these methods have been extended to other models
such as support vector machines or logistic regression.A different
approach in order to obtain a gradient with respect to hyperparameters
consists in differentiating the steps of an iterative optimization
algorithm using automatic differentiation. A more recent work along this
direction uses the implicit function theorem to calculate hypergradients
and proposes a stable approximation of the inverse Hessian. The method
scales to millions of hyperparameters and requires constant memory. In a
different approach, a hypernetwork is trained to approximate the best
response function. One of the advantages of this method is that it can
handle discrete hyperparameters as well. Self-tuning networks offer a
memory efficient version of this approach by choosing a compact
representation for the hypernetwork. More recently, Δ-STN has improved
this method further by a slight reparameterization of the hypernetwork
which speeds up training. Δ-STN also yields a better approximation of
the best-response Jacobian by linearizing the network in the weights,
hence removing unnecessary nonlinear effects of large changes in the
weights. Apart from hypernetwork approaches, gradient-based methods can
be used to optimize discrete hyperparameters also by adopting a
continuous relaxation of the parameters. Such methods have been
extensively used for the optimization of architecture hyperparameters in
neural architecture search. Evolutionary optimization Evolutionary
optimization is a methodology for the global optimization of noisy
black-box functions. In hyperparameter optimization, evolutionary
optimization uses evolutionary algorithms to search the space of
hyperparameters for a given algorithm. Evolutionary hyperparameter
optimization follows a process inspired by the biological concept of
evolution: Create an initial population of random solutions (i.e.,
randomly generate tuples of hyperparameters, typically 100+) Evaluate
the hyperparameters tuples and acquire their fitness function (e.g.,
10-fold cross-validation accuracy of the machine learning algorithm with
those hyperparameters) Rank the hyperparameter tuples by their relative
fitness Replace the worst-performing hyperparameter tuples with new
hyperparameter tuples generated through crossover and mutation Repeat
steps 2-4 until satisfactory algorithm performance is reached or
algorithm performance is no longer improvingEvolutionary optimization
has been used in hyperparameter optimization for statistical machine
learning algorithms, automated machine learning, typical neural network
and deep neural network architecture search, as well as training of the
weights in deep neural networks. Population-based Population Based
Training (PBT) learns both hyperparameter values and network weights.
Multiple learning processes operate independently, using different
hyperparameters. As with evolutionary methods, poorly performing models
are iteratively replaced with models that adopt modified hyperparameter
values and weights based on the better performers. This replacement
model warm starting is the primary differentiator between PBT and other
evolutionary methods. PBT thus allows the hyperparameters to evolve and
eliminates the need for manual hypertuning. The process makes no
assumptions regarding model architecture, loss functions or training
procedures. PBT and its variants are adaptive methods: they update
hyperparameters during the training of the models. On the contrary,
non-adaptive methods have the sub-optimal strategy to assign a constant
set of hyperparameters for the whole training. Early stopping-based A
class of early stopping-based hyperparameter optimization algorithms is
purpose built for large search spaces of continuous and discrete
hyperparameters, particularly when the computational cost to evaluate
the performance of a set of hyperparameters is high. Irace implements
the iterated racing algorithm, that focuses the search around the most
promising configurations, using statistical tests to discard the ones
that perform poorly. Another early stopping hyperparameter optimization
algorithm is successive halving (SHA), which begins as a random search
but periodically prunes low-performing models, thereby focusing
computational resources on more promising models. Asynchronous
successive halving (ASHA) further improves upon SHA\'s resource
utilization profile by removing the need to synchronously evaluate and
prune low-performing models. Hyperband is a higher level early
stopping-based algorithm that invokes SHA or ASHA multiple times with
varying levels of pruning aggressiveness, in order to be more widely
applicable and with fewer required inputs. Others RBF and spectral
approaches have also been developed. See also Automated machine learning
Neural architecture search Meta-optimization Model selection Self-tuning
XGBoost == References ==
