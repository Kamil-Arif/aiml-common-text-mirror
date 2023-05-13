In computational learning theory, Occam learning is a model of
algorithmic learning where the objective of the learner is to output a
succinct representation of received training data. This is closely
related to probably approximately correct (PAC) learning, where the
learner is evaluated on its predictive power of a test set. Occam
learnability implies PAC learning, and for a wide variety of concept
classes, the converse is also true: PAC learnability implies Occam
learnability. Introduction Occam Learning is named after Occam\'s razor,
which is a principle stating that, given all other things being equal, a
shorter explanation for observed data should be favored over a lengthier
explanation. The theory of Occam learning is a formal and mathematical
justification for this principle. It was first shown by Blumer, et al.
that Occam learning implies PAC learning, which is the standard model of
learning in computational learning theory. In other words, parsimony (of
the output hypothesis) implies predictive power. Definition of Occam
learning The succinctness of a concept c {\\displaystyle c} in concept
class C {\\displaystyle {\\mathcal {C}}} can be expressed by the length
s i z e ( c ) {\\displaystyle size(c)} of the shortest bit string that
can represent c {\\displaystyle c} in C {\\displaystyle {\\mathcal {C}}}
. Occam learning connects the succinctness of a learning algorithm\'s
output to its predictive power on unseen data. Let C {\\displaystyle
{\\mathcal {C}}} and H {\\displaystyle {\\mathcal {H}}} be concept
classes containing target concepts and hypotheses respectively. Then,
for constants α ≥ 0 {\\displaystyle \\alpha \\geq 0} and 0 ≤ β \< 1
{\\displaystyle 0\\leq \\beta \<1} , a learning algorithm L
{\\displaystyle L} is an ( α , β ) {\\displaystyle (\\alpha ,\\beta )}
-Occam algorithm for C {\\displaystyle {\\mathcal {C}}} using H
{\\displaystyle {\\mathcal {H}}} iff, given a set S = { x 1 , ... , x m
} {\\displaystyle S=\\{x\_{1},\\dots ,x\_{m}\\}} of m {\\displaystyle m}
samples labeled according to a concept c ∈ C {\\displaystyle c\\in
{\\mathcal {C}}} , L {\\displaystyle L} outputs a hypothesis h ∈ H
{\\displaystyle h\\in {\\mathcal {H}}} such that h {\\displaystyle h} is
consistent with c {\\displaystyle c} on S {\\displaystyle S} (that is, h
( x ) = c ( x ) , ∀ x ∈ S {\\displaystyle h(x)=c(x),\\forall x\\in S} ),
and s i z e ( h ) ≤ ( n ⋅ s i z e ( c ) ) α m β {\\displaystyle
size(h)\\leq (n\\cdot size(c))\^{\\alpha }m\^{\\beta }} where n
{\\displaystyle n} is the maximum length of any sample x ∈ S
{\\displaystyle x\\in S} . An Occam algorithm is called efficient if it
runs in time polynomial in n {\\displaystyle n} , m {\\displaystyle m} ,
and s i z e ( c ) . {\\displaystyle size(c).} We say a concept class C
{\\displaystyle {\\mathcal {C}}} is Occam learnable with respect to a
hypothesis class H {\\displaystyle {\\mathcal {H}}} if there exists an
efficient Occam algorithm for C {\\displaystyle {\\mathcal {C}}} using H
. {\\displaystyle {\\mathcal {H}}.} The relation between Occam and PAC
learning Occam learnability implies PAC learnability, as the following
theorem of Blumer, et al. shows: Theorem (Occam learning implies PAC
learning) Let L {\\displaystyle L} be an efficient ( α , β )
{\\displaystyle (\\alpha ,\\beta )} -Occam algorithm for C
{\\displaystyle {\\mathcal {C}}} using H {\\displaystyle {\\mathcal
{H}}} . Then there exists a constant a \> 0 {\\displaystyle a\>0} such
that for any 0 \< ϵ , δ \< 1 {\\displaystyle 0\<\\epsilon ,\\delta \<1}
, for any distribution D {\\displaystyle {\\mathcal {D}}} , given m ≥ a
( 1 ϵ log ⁡ 1 δ + ( ( n ⋅ s i z e ( c ) ) α ) ϵ ) 1 1 − β )
{\\displaystyle m\\geq a\\left({\\frac {1}{\\epsilon }}\\log {\\frac
{1}{\\delta }}+\\left({\\frac {(n\\cdot size(c))\^{\\alpha })}{\\epsilon
}}\\right)\^{\\frac {1}{1-\\beta }}\\right)} samples drawn from D
{\\displaystyle {\\mathcal {D}}} and labelled according to a concept c ∈
C {\\displaystyle c\\in {\\mathcal {C}}} of length n {\\displaystyle n}
bits each, the algorithm L {\\displaystyle L} will output a hypothesis h
∈ H {\\displaystyle h\\in {\\mathcal {H}}} such that e r r o r ( h ) ≤ ϵ
{\\displaystyle error(h)\\leq \\epsilon } with probability at least 1 −
δ {\\displaystyle 1-\\delta } .Here, e r r o r ( h ) {\\displaystyle
error(h)} is with respect to the concept c {\\displaystyle c} and
distribution D {\\displaystyle {\\mathcal {D}}} . This implies that the
algorithm L {\\displaystyle L} is also a PAC learner for the concept
class C {\\displaystyle {\\mathcal {C}}} using hypothesis class H
{\\displaystyle {\\mathcal {H}}} . A slightly more general formulation
is as follows: Theorem (Occam learning implies PAC learning, cardinality
version) Let 0 \< ϵ , δ \< 1 {\\displaystyle 0\<\\epsilon ,\\delta \<1}
. Let L {\\displaystyle L} be an algorithm such that, given m
{\\displaystyle m} samples drawn from a fixed but unknown distribution D
{\\displaystyle {\\mathcal {D}}} and labeled according to a concept c ∈
C {\\displaystyle c\\in {\\mathcal {C}}} of length n {\\displaystyle n}
bits each, outputs a hypothesis h ∈ H n , m {\\displaystyle h\\in
{\\mathcal {H}}\_{n,m}} that is consistent with the labeled samples.
Then, there exists a constant b {\\displaystyle b} such that if log ⁡ \|
H n , m \| ≤ b ϵ m − log ⁡ 1 δ {\\displaystyle \\log \|{\\mathcal
{H}}\_{n,m}\|\\leq b\\epsilon m-\\log {\\frac {1}{\\delta }}} , then L
{\\displaystyle L} is guaranteed to output a hypothesis h ∈ H n , m
{\\displaystyle h\\in {\\mathcal {H}}\_{n,m}} such that e r r o r ( h )
≤ ϵ {\\displaystyle error(h)\\leq \\epsilon } with probability at least
1 − δ {\\displaystyle 1-\\delta } . While the above theorems show that
Occam learning is sufficient for PAC learning, it doesn\'t say anything
about necessity. Board and Pitt show that, for a wide variety of concept
classes, Occam learning is in fact necessary for PAC learning. They
proved that for any concept class that is polynomially closed under
exception lists, PAC learnability implies the existence of an Occam
algorithm for that concept class. Concept classes that are polynomially
closed under exception lists include Boolean formulas, circuits,
deterministic finite automata, decision-lists, decision-trees, and other
geometrically-defined concept classes. A concept class C {\\displaystyle
{\\mathcal {C}}} is polynomially closed under exception lists if there
exists a polynomial-time algorithm A {\\displaystyle A} such that, when
given the representation of a concept c ∈ C {\\displaystyle c\\in
{\\mathcal {C}}} and a finite list E {\\displaystyle E} of exceptions,
outputs a representation of a concept c ′ ∈ C {\\displaystyle c\'\\in
{\\mathcal {C}}} such that the concepts c {\\displaystyle c} and c ′
{\\displaystyle c\'} agree except on the set E {\\displaystyle E} .
Proof that Occam learning implies PAC learning We first prove the
Cardinality version. Call a hypothesis h ∈ H {\\displaystyle h\\in
{\\mathcal {H}}} bad if e r r o r ( h ) ≥ ϵ {\\displaystyle
error(h)\\geq \\epsilon } , where again e r r o r ( h ) {\\displaystyle
error(h)} is with respect to the true concept c {\\displaystyle c} and
the underlying distribution D {\\displaystyle {\\mathcal {D}}} . The
probability that a set of samples S {\\displaystyle S} is consistent
with h {\\displaystyle h} is at most ( 1 − ϵ ) m {\\displaystyle
(1-\\epsilon )\^{m}} , by the independence of the samples. By the union
bound, the probability that there exists a bad hypothesis in H n , m
{\\displaystyle {\\mathcal {H}}\_{n,m}} is at most \| H n , m \| ( 1 − ϵ
) m {\\displaystyle \|{\\mathcal {H}}\_{n,m}\|(1-\\epsilon )\^{m}} ,
which is less than δ {\\displaystyle \\delta } if log ⁡ \| H n , m \| ≤ O
( ϵ m ) − log ⁡ 1 δ {\\displaystyle \\log \|{\\mathcal {H}}\_{n,m}\|\\leq
O(\\epsilon m)-\\log {\\frac {1}{\\delta }}} . This concludes the proof
of the second theorem above. Using the second theorem, we can prove the
first theorem. Since we have a ( α , β ) {\\displaystyle (\\alpha
,\\beta )} -Occam algorithm, this means that any hypothesis output by L
{\\displaystyle L} can be represented by at most ( n ⋅ s i z e ( c ) ) α
m β {\\displaystyle (n\\cdot size(c))\^{\\alpha }m\^{\\beta }} bits, and
thus log ⁡ \| H n , m \| ≤ ( n ⋅ s i z e ( c ) ) α m β {\\displaystyle
\\log \|{\\mathcal {H}}\_{n,m}\|\\leq (n\\cdot size(c))\^{\\alpha
}m\^{\\beta }} . This is less than O ( ϵ m ) − log ⁡ 1 δ {\\displaystyle
O(\\epsilon m)-\\log {\\frac {1}{\\delta }}} if we set m ≥ a ( 1 ϵ log ⁡
1 δ + ( ( n ⋅ s i z e ( c ) ) α ) ϵ ) 1 1 − β ) {\\displaystyle m\\geq
a\\left({\\frac {1}{\\epsilon }}\\log {\\frac {1}{\\delta
}}+\\left({\\frac {(n\\cdot size(c))\^{\\alpha })}{\\epsilon
}}\\right)\^{\\frac {1}{1-\\beta }}\\right)} for some constant a \> 0
{\\displaystyle a\>0} . Thus, by the Cardinality version Theorem, L
{\\displaystyle L} will output a consistent hypothesis h {\\displaystyle
h} with probability at least 1 − δ {\\displaystyle 1-\\delta } . This
concludes the proof of the first theorem above. Improving sample
complexity for common problems Though Occam and PAC learnability are
equivalent, the Occam framework can be used to produce tighter bounds on
the sample complexity of classical problems including conjunctions,
conjunctions with few relevant variables, and decision lists. Extensions
Occam algorithms have also been shown to be successful for PAC learning
in the presence of errors, probabilistic concepts, function learning and
Markovian non-independent examples. See also Structural Risk
Minimization Computational learning theory == References ==
