Temporal difference (TD) learning refers to a class of model-free
reinforcement learning methods which learn by bootstrapping from the
current estimate of the value function. These methods sample from the
environment, like Monte Carlo methods, and perform updates based on
current estimates, like dynamic programming methods.While Monte Carlo
methods only adjust their estimates once the final outcome is known, TD
methods adjust predictions to match later, more accurate, predictions
about the future before the final outcome is known. This is a form of
bootstrapping, as illustrated with the following example: Suppose you
wish to predict the weather for Saturday, and you have some model that
predicts Saturday\'s weather, given the weather of each day in the week.
In the standard case, you would wait until Saturday and then adjust all
your models. However, when it is, for example, Friday, you should have a
pretty good idea of what the weather would be on Saturday -- and thus be
able to change, say, Saturday\'s model before Saturday arrives. Temporal
difference methods are related to the temporal difference model of
animal learning. Mathematical formulation The tabular TD(0) method is
one of the simplest TD methods. It is a special case of more general
stochastic approximation methods. It estimates the state value function
of a finite-state Markov decision process (MDP) under a policy π
{\\displaystyle \\pi } . Let V π {\\displaystyle V\^{\\pi }} denote the
state value function of the MDP with states ( s t ) t ∈ N
{\\displaystyle (s\_{t})\_{t\\in \\mathbb {N} }} , rewards ( r t ) t ∈ N
{\\displaystyle (r\_{t})\_{t\\in \\mathbb {N} }} and discount rate γ
{\\displaystyle \\gamma } under the policy π {\\displaystyle \\pi } : V
π ( s ) = E a ∼ π { ∑ t = 0 ∞ γ t r t ( a t ) \| s 0 = s } .
{\\displaystyle V\^{\\pi }(s)=E\_{a\\sim \\pi }\\left\\{\\sum
\_{t=0}\^{\\infty }\\gamma \^{t}r\_{t}(a\_{t}){\\Bigg
\|}s\_{0}=s\\right\\}.} We drop the action from the notation for
convenience. V π {\\displaystyle V\^{\\pi }} satisfies the
Hamilton-Jacobi-Bellman Equation: V π ( s ) = E π { r 0 + γ V π ( s 1 )
\| s 0 = s } , {\\displaystyle V\^{\\pi }(s)=E\_{\\pi }\\{r\_{0}+\\gamma
V\^{\\pi }(s\_{1})\|s\_{0}=s\\},} so r 0 + γ V π ( s 1 ) {\\displaystyle
r\_{0}+\\gamma V\^{\\pi }(s\_{1})} is an unbiased estimate for V π ( s )
{\\displaystyle V\^{\\pi }(s)} . This observation motivates the
following algorithm for estimating V π {\\displaystyle V\^{\\pi }} . The
algorithm starts by initializing a table V ( s ) {\\displaystyle V(s)}
arbitrarily, with one value for each state of the MDP. A positive
learning rate α {\\displaystyle \\alpha } is chosen. We then repeatedly
evaluate the policy π {\\displaystyle \\pi } , obtain a reward r
{\\displaystyle r} and update the value function for the old state using
the rule: V ( s ) ← V ( s ) + α ( r + γ V ( s ′ ) ⏞ The TD target − V (
s ) ) {\\displaystyle V(s)\\leftarrow V(s)+\\alpha (\\overbrace
{r+\\gamma V(s\')} \^{\\text{The TD target}}-V(s))} where s
{\\displaystyle s} and s ′ {\\displaystyle s\'} are the old and new
states, respectively. The value r + γ V ( s ′ ) {\\displaystyle
r+\\gamma V(s\')} is known as the TD target. TD-Lambda TD-Lambda is a
learning algorithm invented by Richard S. Sutton based on earlier work
on temporal difference learning by Arthur Samuel. This algorithm was
famously applied by Gerald Tesauro to create TD-Gammon, a program that
learned to play the game of backgammon at the level of expert human
players.The lambda ( λ {\\displaystyle \\lambda } ) parameter refers to
the trace decay parameter, with 0 ⩽ λ ⩽ 1 {\\displaystyle 0\\leqslant
\\lambda \\leqslant 1} . Higher settings lead to longer lasting traces;
that is, a larger proportion of credit from a reward can be given to
more distant states and actions when λ {\\displaystyle \\lambda } is
higher, with λ = 1 {\\displaystyle \\lambda =1} producing parallel
learning to Monte Carlo RL algorithms. In neuroscience The TD algorithm
has also received attention in the field of neuroscience. Researchers
discovered that the firing rate of dopamine neurons in the ventral
tegmental area (VTA) and substantia nigra (SNc) appear to mimic the
error function in the algorithm. The error function reports back the
difference between the estimated reward at any given state or time step
and the actual reward received. The larger the error function, the
larger the difference between the expected and actual reward. When this
is paired with a stimulus that accurately reflects a future reward, the
error can be used to associate the stimulus with the future reward.
Dopamine cells appear to behave in a similar manner. In one experiment
measurements of dopamine cells were made while training a monkey to
associate a stimulus with the reward of juice. Initially the dopamine
cells increased firing rates when the monkey received juice, indicating
a difference in expected and actual rewards. Over time this increase in
firing back propagated to the earliest reliable stimulus for the reward.
Once the monkey was fully trained, there was no increase in firing rate
upon presentation of the predicted reward. Subsequently, the firing rate
for the dopamine cells decreased below normal activation when the
expected reward was not produced. This mimics closely how the error
function in TD is used for reinforcement learning. The relationship
between the model and potential neurological function has produced
research attempting to use TD to explain many aspects of behavioral
research. It has also been used to study conditions such as
schizophrenia or the consequences of pharmacological manipulations of
dopamine on learning. See also PVLV Q-learning Rescorla--Wagner model
State--action--reward--state--action (SARSA) Notes Works cited Sutton,
Richard S.; Barto, Andrew G. (2018). Reinforcement Learning: An
Introduction (2nd ed.). Cambridge, MA: MIT Press. Tesauro, Gerald (March
1995). \"Temporal Difference Learning and TD-Gammon\". Communications of
the ACM. 38 (3): 58--68. doi:10.1145/203330.203343. S2CID 6023746.
Further reading Meyn, S. P. (2007). Control Techniques for Complex
Networks. Cambridge University Press. ISBN 978-0521884419. See final
chapter and appendix. Sutton, R. S.; Barto, A. G. (1990). \"Time
Derivative Models of Pavlovian Reinforcement\" (PDF). Learning and
Computational Neuroscience: Foundations of Adaptive Networks: 497--537.
External links Connect Four TDGravity Applet (+ mobile phone version) --
self-learned using TD-Leaf method (combination of TD-Lambda with shallow
tree search) Self Learning Meta-Tic-Tac-Toe Example web app showing how
temporal difference learning can be used to learn state evaluation
constants for a minimax AI playing a simple board game. Reinforcement
Learning Problem, document explaining how temporal difference learning
can be used to speed up Q-learning TD-Simulator Temporal difference
simulator for classical conditioning
