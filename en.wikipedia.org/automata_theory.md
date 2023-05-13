Automata theory is the study of abstract machines and automata, as well
as the computational problems that can be solved using them. It is a
theory in theoretical computer science. The word automata comes from the
Greek word αὐτόματος, which means \"self-acting, self-willed,
self-moving\". An automaton (automata in plural) is an abstract
self-propelled computing device which follows a predetermined sequence
of operations automatically. An automaton with a finite number of states
is called a Finite Automaton (FA) or Finite-State Machine (FSM). The
figure on the right illustrates a finite-state machine, which is a
well-known type of automaton. This automaton consists of states
(represented in the figure by circles) and transitions (represented by
arrows). As the automaton sees a symbol of input, it makes a transition
(or jump) to another state, according to its transition function, which
takes the previous state and current input symbol as its arguments.
Automata theory is closely related to formal language theory. In this
context, automata are used as finite representations of formal languages
that may be infinite. Automata are often classified by the class of
formal languages they can recognize, as in the Chomsky hierarchy, which
describes a nesting relationship between major classes of automata.
Automata play a major role in the theory of computation, compiler
construction, artificial intelligence, parsing and formal verification.
History The theory of abstract automata was developed in the mid-20th
century in connection with finite automata. Automata theory was
initially considered a branch of mathematical systems theory, studying
the behavior of discrete-parameter systems. Early work in automata
theory differed from previous work on systems by using abstract algebra
to describe information systems rather than differential calculus to
describe material systems. The theory of the finite-state transducer was
developed under different names by different research communities. The
earlier concept of Turing machine was also included in the discipline
along with new forms of infinite-state automata, such as pushdown
automata. 1956 saw the publication of Automata Studies, which collected
work by scientists including Claude Shannon, W. Ross Ashby, John von
Neumann, Marvin Minsky, Edward F. Moore, and Stephen Cole Kleene. With
the publication of this volume, \"automata theory emerged as a
relatively autonomous discipline\". The book included Kleene\'s
description of the set of regular events, or regular languages, and a
relatively stable measure of complexity in Turing machine programs by
Shannon. In the same year, Noam Chomsky described the Chomsky hierarchy,
a correspondence between automata and formal grammars, and Ross Ashby
published An Introduction to Cybernetics, an accessible textbook
explaining automata and information using basic set theory. The study of
linear bounded automata led to the Myhill--Nerode theorem, which gives a
necessary and sufficient condition for a formal language to be regular,
and an exact count of the number of states in a minimal machine for the
language. The pumping lemma for regular languages, also useful in
regularity proofs, was proven in this period by Michael O. Rabin and
Dana Scott, along with the computational equivalence of deterministic
and nondeterministic finite automata.In the 1960s, a body of algebraic
results known as \"structure theory\" or \"algebraic decomposition
theory\" emerged, which dealt with the realization of sequential
machines from smaller machines by interconnection. While any finite
automaton can be simulated using a universal gate set, this requires
that the simulating circuit contain loops of arbitrary complexity.
Structure theory deals with the \"loop-free\" realizability of machines.
The theory of computational complexity also took shape in the 1960s. By
the end of the decade, automata theory came to be seen as \"the pure
mathematics of computer science\". Automata What follows is a general
definition of an automaton, which restricts a broader definition of a
system to one viewed as acting in discrete time-steps, with its state
behavior and outputs defined at each step by unchanging functions of
only its state and input.0\'.\'\|01,\"\|\",1\| Informal description An
automaton runs when it is given some sequence of inputs in discrete
(individual) time steps (or just steps). An automaton processes one
input picked from a set of symbols or letters, which is called an input
alphabet. The symbols received by the automaton as input at any step are
a sequence of symbols called words. An automaton has a set of states. At
each moment during a run of the automaton, the automaton is in one of
its states. When the automaton receives new input it moves to another
state (or transitions) based on a transition function that takes the
previous state and current input symbol as parameters. At the same time,
another function called the output function produces symbols from the
output alphabet, also according to the previous state and current input
symbol. The automaton reads the symbols of the input word and
transitions between states until the word is read completely, if it is
finite in length, at which point the automaton halts. A state at which
the automaton halts is called the final state. To investigate the
possible state/input/output sequences in an automaton using formal
language theory, a machine can be assigned a starting state and a set of
accepting states. Then, depending on whether a run starting from the
starting state ends in an accepting state, the automaton can be said to
accept or reject an input sequence. The set of all the words accepted by
an automaton is called the language recognized by the automaton. A
familiar example of a machine recognizing a language is an electronic
lock, which accepts or rejects attempts to enter the correct code.
Formal definition AutomatonAn automaton can be represented formally by a
5-tuple M = ⟨ Σ , Γ , Q , δ , λ ⟩ {\\displaystyle M=\\langle \\Sigma
,\\Gamma ,Q,\\delta ,\\lambda \\rangle } , where: Σ {\\displaystyle
\\Sigma } is a finite set of symbols, called the input alphabet of the
automaton, Γ {\\displaystyle \\Gamma } is another finite set of symbols,
called the output alphabet of the automaton, Q {\\displaystyle Q} is a
set of states, δ {\\displaystyle \\delta } is the next-state function or
transition function δ : Q × Σ → Q {\\displaystyle \\delta :Q\\times
\\Sigma \\to Q} mapping state-input pairs to successor states, λ
{\\displaystyle \\lambda } is the next-output function λ : Q × Σ → Γ
{\\displaystyle \\lambda :Q\\times \\Sigma \\to \\Gamma } mapping
state-input pairs to outputs. If Q {\\displaystyle Q} is finite, then M
{\\displaystyle M} is a finite automaton.Input word An automaton reads a
finite string of symbols a 1 a 2 . . . a n {\\displaystyle
a\_{1}a\_{2}\...a\_{n}} , where a i ∈ Σ {\\displaystyle a\_{i}\\in
\\Sigma } , which is called an input word. The set of all words is
denoted by Σ ∗ {\\displaystyle \\Sigma \^{\*}} .Run A sequence of states
q 0 , q 1 , . . . , q n {\\displaystyle q\_{0},q\_{1},\...,q\_{n}} ,
where q i ∈ Q {\\displaystyle q\_{i}\\in Q} such that q i = δ ( q i − 1
, a i ) {\\displaystyle q\_{i}=\\delta (q\_{i-1},a\_{i})} for 0 \< i ≤ n
{\\displaystyle 0
