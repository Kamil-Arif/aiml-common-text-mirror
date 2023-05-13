Reservoir computing is a framework for computation derived from
recurrent neural network theory that maps input signals into higher
dimensional computational spaces through the dynamics of a fixed,
non-linear system called a reservoir. After the input signal is fed into
the reservoir, which is treated as a \"black box,\" a simple readout
mechanism is trained to read the state of the reservoir and map it to
the desired output. The first key benefit of this framework is that
training is performed only at the readout stage, as the reservoir
dynamics are fixed. The second is that the computational power of
naturally available systems, both classical and quantum mechanical, can
be used to reduce the effective computational cost. History The concept
of reservoir computing stems from the use of recursive connections
within neural networks to create a complex dynamical system. It is a
generalisation of earlier neural network architectures such as recurrent
neural networks, liquid-state machines and echo-state networks.
Reservoir computing also extends to physical systems that are not
networks in the classical sense, but rather continuous systems in space
and/or time: e.g. a literal \"bucket of water\" can serve as a reservoir
that performs computations on inputs given as perturbations of the
surface. The resultant complexity of such recurrent neural networks was
found to be useful in solving a variety of problems including language
processing and dynamic system modeling. However, training of recurrent
neural networks is challenging and computationally expensive. Reservoir
computing reduces those training-related challenges by fixing the
dynamics of the reservoir and only training the linear output layer.A
large variety of nonlinear dynamical systems can serve as a reservoir
that performs computations. In recent years semiconductor lasers have
attracted considerable interest as computation can be fast and energy
efficient compared to electrical components. Recent advances in both AI
and quantum information theory have given rise to the concept of quantum
neural networks. These hold promise in quantum information processing,
which is challenging to classical networks, but can also find
application in solving classical problems. In 2018, a physical
realization of a quantum reservoir computing architecture was
demonstrated in the form of nuclear spins within a molecular solid.
However, the nuclear spin experiments in did not demonstrate quantum
reservoir computing per se as they did not involve processing of
sequential data. Rather the data were vector inputs, which makes this
more accurately a demonstration of quantum implementation of a random
kitchen sink algorithm (also going by the name of extreme learning
machines in some communities). In 2019, another possible implementation
of quantum reservoir processors was proposed in the form of
two-dimensional fermionic lattices. In 2020, realization of reservoir
computing on gate-based quantum computers was proposed and demonstrated
on cloud-based IBM superconducting near-term quantum computers.Reservoir
computers have been used for time-series analysis purposes. In
particular, some of their usages involve chaotic time-series prediction,
separation of chaotic signals, and link inference of networks from their
dynamics. Classical reservoir computing Reservoir The \'reservoir\' in
reservoir computing is the internal structure of the computer, and must
have two properties: it must be made up of individual, non-linear units,
and it must be capable of storing information. The non-linearity
describes the response of each unit to input, which is what allows
reservoir computers to solve complex problems. Reservoirs are able to
store information by connecting the units in recurrent loops, where the
previous input affects the next response. The change in reaction due to
the past allows the computers to be trained to complete specific
tasks.Reservoirs can be virtual or physical. Virtual reservoirs are
typically randomly generated and are designed like neural networks.
Virtual reservoirs can be designed to have non-linearity and recurrent
loops, but, unlike neural networks, the connections between units are
randomized and remain unchanged throughout computation. Physical
reservoirs are possible because of the inherent non-linearity of certain
natural systems. The interaction between ripples on the surface of water
contains the nonlinear dynamics required in reservoir creation, and a
pattern recognition RC was developed by first inputting ripples with
electric motors then recording and analyzing the ripples in the readout.
Readout The readout is a neural network layer that performs a linear
transformation on the output of the reservoir. The weights of the
readout layer are trained by analyzing the spatiotemporal patterns of
the reservoir after excitation by known inputs, and by utilizing a
training method such as a linear regression or a Ridge regression. As
its implementation depends on spatiotemporal reservoir patterns, the
details of readout methods are tailored to each type of reservoir. For
example, the readout for a reservoir computer using a container of
liquid as its reservoir might entail observing spatiotemporal patterns
on the surface of the liquid. Types Context reverberation network An
early example of reservoir computing was the context reverberation
network. In this architecture, an input layer feeds into a high
dimensional dynamical system which is read out by a trainable
single-layer perceptron. Two kinds of dynamical system were described: a
recurrent neural network with fixed random weights, and a continuous
reaction--diffusion system inspired by Alan Turing's model of
morphogenesis. At the trainable layer, the perceptron associates current
inputs with the signals that reverberate in the dynamical system; the
latter were said to provide a dynamic \"context\" for the inputs. In the
language of later work, the reaction--diffusion system served as the
reservoir. Echo state network The Tree Echo State Network (TreeESN)
model represents a generalization of the reservoir computing framework
to tree structured data. Liquid-state machine Chaotic Liquid State
Machine The liquid (i.e. reservoir) of a Chaotic Liquid State Machine
(CLSM), or chaotic reservoir, is made from chaotic spiking neurons but
which stabilize their activity by settling to a single hypothesis that
describes the trained inputs of the machine. This is in contrast to
general types of reservoirs that don't stabilize. The liquid
stabilization occurs via synaptic plasticity and chaos control that
govern neural connections inside the liquid. CLSM showed promising
results in learning sensitive time series data. Nonlinear transient
computation This type of information processing is most relevant when
time-dependent input signals depart from the mechanism's internal
dynamics. These departures cause transients or temporary altercations
which are represented in the device's output. Deep reservoir computing
The extension of the reservoir computing framework towards Deep
Learning, with the introduction of Deep Reservoir Computing and of the
Deep Echo State Network (DeepESN) model allows to develop efficiently
trained models for hierarchical processing of temporal data, at the same
time enabling the investigation on the inherent role of layered
composition in recurrent neural networks. Quantum reservoir computing
Quantum reservoir computing may use the nonlinear nature of quantum
mechanical interactions or processes to form the characteristic
nonlinear reservoirs but may also be done with linear reservoirs when
the injection of the input to the reservoir creates the nonlinearity.
The marriage of machine learning and quantum devices is leading to the
emergence of quantum neuromorphic computing as a new research area.
Types Gaussian states of interacting quantum harmonic oscillators
Gaussian states are a paradigmatic class of states of continuous
variable quantum systems. Although they can nowadays be created and
manipulated in, e.g, state-of-the-art optical platforms, naturally
robust to decoherence, it is well-known that they are not sufficient
for, e.g., universal quantum computing because transformations that
preserve the Gaussian nature of a state are linear. Normally, linear
dynamics would not be sufficient for nontrivial reservoir computing
either. It is nevertheless possible to harness such dynamics for
reservoir computing purposes by considering a network of interacting
quantum harmonic oscillators and injecting the input by periodical state
resets of a subset of the oscillators. With a suitable choice of how the
states of this subset of oscillators depends on the input, the
observables of the rest of the oscillators can become nonlinear
functions of the input suitable for reservoir computing; indeed, thanks
to the properties of these functions, even universal reservoir computing
becomes possible by combining the observables with a polynomial readout
function. In principle, such reservoir computers could be implemented
with controlled multimode optical parametric processes, however
efficient extraction of the output from the system is challenging
especially in the quantum regime where measurement back-action must be
taken into account. 2-D quantum dot lattices In this architecture,
randomized coupling between lattice sites grants the reservoir the
"black box" property inherent to reservoir processors. The reservoir is
then excited, which acts as the input, by an incident optical field.
Readout occurs in the form of occupational numbers of lattice sites,
which are naturally nonlinear functions of the input. Nuclear spins in a
molecular solid In this architecture, quantum mechanical coupling
between spins of neighboring atoms within the molecular solid provides
the non-linearity required to create the higher-dimensional
computational space. The reservoir is then excited by radiofrequency
electromagnetic radiation tuned to the resonance frequencies of relevant
nuclear spins. Readout occurs by measuring the nuclear spin states.
Reservoir computing on gate-based near-term superconducting quantum
computers The most prevalent model of quantum computing is the
gate-based model where quantum computation is performed by sequential
applications of unitary quantum gates on qubits of a quantum computer. A
theory for the implementation of reservoir computing on a gate-based
quantum computer with proof-of-principle demonstrations on a number of
IBM superconducting noisy intermediate-scale quantum (NISQ) computers
has been reported in. See also Deep learning Extreme learning machines
Unconventional computing References Further reading Reservoir Computing
using delay systems, Nature Communications 2011 Optoelectronic Reservoir
Computing, Scientific Reports February 2012 Optoelectronic Reservoir
Computing, Optics Express 2012 All-optical Reservoir Computing, Nature
Communications 2013 Memristor Models for Machine learning, Neural
Computation 2014 arxiv
