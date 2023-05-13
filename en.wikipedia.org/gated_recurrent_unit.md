Gated recurrent units (GRUs) are a gating mechanism in recurrent neural
networks, introduced in 2014 by Kyunghyun Cho et al. The GRU is like a
long short-term memory (LSTM) with a forget gate, but has fewer
parameters than LSTM, as it lacks an output gate. GRU\'s performance on
certain tasks of polyphonic music modeling, speech signal modeling and
natural language processing was found to be similar to that of LSTM.
GRUs shown that gating is indeed helpful in general and Bengio\'s team
concluding that no concrete conclusion on which of the two gating units
was better. Architecture There are several variations on the full gated
unit, with gating done using the previous hidden state and the bias in
various combinations, and a simplified form called minimal gated
unit.The operator ⊙ {\\displaystyle \\odot } denotes the Hadamard
product in the following. Fully gated unit Initially, for t = 0
{\\displaystyle t=0} , the output vector is h 0 = 0 {\\displaystyle
h\_{0}=0} . z t = σ g ( W z x t + U z h t − 1 + b z ) r t = σ g ( W r x
t + U r h t − 1 + b r ) h \^ t = ϕ h ( W h x t + U h ( r t ⊙ h t − 1 ) +
b h ) h t = ( 1 − z t ) ⊙ h t − 1 + z t ⊙ h \^ t {\\displaystyle
{\\begin{aligned}z\_{t}&=\\sigma
\_{g}(W\_{z}x\_{t}+U\_{z}h\_{t-1}+b\_{z})\\\\r\_{t}&=\\sigma
\_{g}(W\_{r}x\_{t}+U\_{r}h\_{t-1}+b\_{r})\\\\{\\hat {h}}\_{t}&=\\phi
\_{h}(W\_{h}x\_{t}+U\_{h}(r\_{t}\\odot
h\_{t-1})+b\_{h})\\\\h\_{t}&=(1-z\_{t})\\odot h\_{t-1}+z\_{t}\\odot
{\\hat {h}}\_{t}\\end{aligned}}} Variables x t {\\displaystyle x\_{t}} :
input vector h t {\\displaystyle h\_{t}} : output vector h \^ t
{\\displaystyle {\\hat {h}}\_{t}} : candidate activation vector z t
{\\displaystyle z\_{t}} : update gate vector r t {\\displaystyle r\_{t}}
: reset gate vector W {\\displaystyle W} , U {\\displaystyle U} and b
{\\displaystyle b} : parameter matrices and vectorActivation functions σ
g {\\displaystyle \\sigma \_{g}} : The original is a sigmoid function. ϕ
h {\\displaystyle \\phi \_{h}} : The original is a hyperbolic
tangent.Alternative activation functions are possible, provided that σ g
( x ) ∈ \[ 0 , 1 \] {\\displaystyle \\sigma \_{g}(x)\\in \[0,1\]} .
Alternate forms can be created by changing z t {\\displaystyle z\_{t}}
and r t {\\displaystyle r\_{t}} Type 1, each gate depends only on the
previous hidden state and the bias. z t = σ g ( U z h t − 1 + b z ) r t
= σ g ( U r h t − 1 + b r ) {\\displaystyle
{\\begin{aligned}z\_{t}&=\\sigma
\_{g}(U\_{z}h\_{t-1}+b\_{z})\\\\r\_{t}&=\\sigma
\_{g}(U\_{r}h\_{t-1}+b\_{r})\\\\\\end{aligned}}} Type 2, each gate
depends only on the previous hidden state. z t = σ g ( U z h t − 1 ) r t
= σ g ( U r h t − 1 ) {\\displaystyle {\\begin{aligned}z\_{t}&=\\sigma
\_{g}(U\_{z}h\_{t-1})\\\\r\_{t}&=\\sigma
\_{g}(U\_{r}h\_{t-1})\\\\\\end{aligned}}} Type 3, each gate is computed
using only the bias. z t = σ g ( b z ) r t = σ g ( b r ) {\\displaystyle
{\\begin{aligned}z\_{t}&=\\sigma \_{g}(b\_{z})\\\\r\_{t}&=\\sigma
\_{g}(b\_{r})\\\\\\end{aligned}}} Minimal gated unit The minimal gated
unit is similar to the fully gated unit, except the update and reset
gate vector is merged into a forget gate. This also implies that the
equation for the output vector must be changed: f t = σ g ( W f x t + U
f h t − 1 + b f ) h \^ t = ϕ h ( W h x t + U h ( f t ⊙ h t − 1 ) + b h )
h t = ( 1 − f t ) ⊙ h t − 1 + f t ⊙ h \^ t {\\displaystyle
{\\begin{aligned}f\_{t}&=\\sigma
\_{g}(W\_{f}x\_{t}+U\_{f}h\_{t-1}+b\_{f})\\\\{\\hat {h}}\_{t}&=\\phi
\_{h}(W\_{h}x\_{t}+U\_{h}(f\_{t}\\odot
h\_{t-1})+b\_{h})\\\\h\_{t}&=(1-f\_{t})\\odot h\_{t-1}+f\_{t}\\odot
{\\hat {h}}\_{t}\\end{aligned}}} Variables x t {\\displaystyle x\_{t}} :
input vector h t {\\displaystyle h\_{t}} : output vector h \^ t
{\\displaystyle {\\hat {h}}\_{t}} : candidate activation vector f t
{\\displaystyle f\_{t}} : forget vector W {\\displaystyle W} , U
{\\displaystyle U} and b {\\displaystyle b} : parameter matrices and
vector Learning Algorithm Recommendation Framework A Learning Algorithm
Recommendation Framework may help guiding the selection of learning
algorithm and scientific discipline (e.g. RNN, GAN, RL, CNN,\...). The
framework has the advantage of having been generated from an extensive
analysis of the literature and dedicated to recurrent neural networks
and their variations. == References ==
