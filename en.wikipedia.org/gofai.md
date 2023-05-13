GOFAI is an acronym for \"Good Old-Fashioned Artificial Intelligence\"
invented by the philosopher John Haugeland in his 1985 book, Artificial
Intelligence: The Very Idea. Technically, GOFAI refers only to a
restricted kind of symbolic AI, namely rule-based or logical agents.
This approach was popular in the 1980s, especially as an approach to
implementing expert systems, but symbolic AI has since been extended in
many ways to better handle uncertain reasoning and more open-ended
systems. Some of these extensions include probabilistic reasoning,
non-monotonic reasoning, multi-agent systems, and neuro-symbolic
systems. Significant contributions of symbolic AI, not encompassed by
the GOFAI view, include search algorithms; automated planning and
scheduling; constraint-based reasoning; the semantic web; ontologies;
knowledge graphs; non-monotonic logic; circumscription; automated
theorem proving; and symbolic mathematics. For a more complete list, see
the main article on symbolic AI. Symbolic AI after GOFAI and confusions
caused by viewing symbolic AI as only GOFAI Although the term GOFAI
encompasses only a small part of symbolic AI, prominent in the 1980s,
contemporary critics of symbolic AI sometimes use GOFAI as a synonym for
it. This conflation of terms can lead to conclusions that symbolic AI
research ended in the 1980s and avoided machine learning. Since both
conclusions are false and important to correct, we address them below.
The 1980s GOFAI version of symbolic AI characterized by production rules
and expert systems During the Second AI Summer, i.e., the expert systems
boom of the 1980s, production-rule systems requiring knowledge
engineering were used to implement expert systems. Knowledge engineering
required working with subject matter experts to model task knowledge as
rules. At the time, rules were hand-authored by knowledge engineers or
the subject matter experts. GOFAI correctly describes this approach.
Haugeland and Dreyfus also correctly pointed out various limitations,
discussed in later sections. The Second AI Winter occurred after the
expert systems and Lisp Machines markets collapsed. Expert systems did
not handle uncertainty well, required more resources to build and
maintain than expected, and proved brittle outside their intended
domains due to a lack of common-sense reasoning capabilities.
Language-specific Lisp machines could become easily replaced by newer
workstations with similar performance, obviating their need. Symbolic AI
after GOFAI Symbolic AI continued, albeit with reduced funding. It
redirected focus to address limitations in handling uncertainty, using
statistical AI; and to speed knowledge acquisition, with symbolic
approaches to machine learning. Work in semantic networks and knowledge
representations led to formalizing ontologies with languages such as RDF
and OWL, leading to large ontologies such as YAGO. However, the research
and applications of symbolic AI since the Second AI Winter and outside
of the production-rule approach to expert systems are less well known
and now eclipsed by the media focus on deep learning since 2012. For
example, research in symbolic AI machine learning includes decision tree
learning, Mitchell\'s version space learning, Valiant\'s contributions
to PAC learning, statistical relational learning, inductive logic
programming, and various interactive learning approaches to incorporate
user advice, examples, and explanations as an integral part of the
learning process. Problems when current symbolic AI is viewed as GOFAI
Using GOFAI as a synonym for current symbolic AI leads to erroneous
conclusions and confusion. Garcez and Lamb provide an example:Turing
award winner Judea Pearl offers a critique of machine learning which,
unfortunately, conflates the terms machine learning and deep learning.
Similarly, when Geoffrey Hinton refers to symbolic AI, the connotation
of the term tends to be that of expert systems dispossessed of any
ability to learn. The use of the terminology is in need of
clarification. Machine learning is not confined to association rule
mining, c.f. the body of work on symbolic ML \[machine learning\] and
relational learning (the differences to deep learning being the choice
of representation, localist logical rather than distributed, and the
non-use of gradient-based learning algorithms). Equally, symbolic AI is
not just about production rules written by hand. A proper definition of
AI concerns knowledge representation and reasoning, autonomous
multi-agent systems, planning and argumentation, as well as learning.
The key points above are that symbolic AI research has long since moved
beyond GOFAI, research continues, and GOFAI no longer describes it.
Further, there are symbolic learning approaches to machine learning,
such as inductive logic programming and statistical relational learning,
i.e., it is not just the domain of deep learning. Below, we return to
the philosophical critiques leveled against GOFAI, the symbolic AI
approach of the 1980s. The GOFAI critique of rule-based agents GOFAI,
the rule-based approach of 1980s symbolic AI, was attacked by
philosophers such as Hubert Dreyfus, his brother Stuart Dreyfus, and
philosopher Kenneth Sayre. The essence of what they criticized was
described earlier by computer scientist Alan Turing, in his 1950 paper
Computing Machinery and Intelligence, when he said that \"human behavior
is far too complex to be captured by any formal set of rules---humans
must be using some informal guidelines that ... could never be captured
in a formal set of rules and thus could never be codified in a computer
program.\" Turing called this \"The Argument from Informality of
Behaviour.\" Russell and Norvig, describe the GOFAI critique in
Artificial Intelligence: A Modern Approach: The position they criticize
came to be called \"Good Old-Fashioned Al,\" or GOFAI, a term coined by
Haugeland (1985). GOFAI is supposed to claim that all intelligent
behavior can be captured by a system that reasons logically from a set
of facts and rules describing the domain. It therefore corresponds to
the simplest logical agent described in Chapter 7. Dreyfus is correct in
saying that logical agents are vulnerable to the qualification problem.
As we saw in Chapter 13, probabilistic reasoning systems are more
appropriate for open-ended domains. The Dreyfus critique therefore is
not addressed against computers per se, but rather against one
particular way of programming them. It is reasonable to suppose,
however, that a book called What First-Order Logical Rule-Based Systems
Without Learning Can\'t Do might have had less impact.In other words,
GOFAI restricts its view of agents to those controlled by logical rules.
In contrast to this view, symbolic AI also includes non-monotonic logic,
modal logic, probabilistic logics, multi-agent systems, symbolic machine
learning, and hybrid neuro-symbolic architectures. Symbolic machine
learning, i.e., non-connectionist machine learning specific to symbolic
AI, includes inductive logic programming, statistical relational
learning, case-based learning, knowledge compilation (chunking),
macro-operator learning, learning from analogy, and interactive learning
from human advice, explanations, and exemplars. The GOFAI critique of
disembodied agents Russell and Norvig do not reject all of Dreyfus's
arguments, they accept his strongest argument, one that applies to all
disembodied AIs, whatever their approach: One of Dreyfus\'s strongest
arguments is for situated agents rather than disembodied logical
inference engines. An agent whose understanding of \"dog\" comes only
from a limited set of logical sentences such as \"Dog(x) ⇒ Mammal(x)\"
is at a disadvantage compared to an agent that has watched dogs run, has
played fetch with them, and has been licked by one. As philosopher Andy
Clark (1998) says, \"Biological brains are first and foremost the
control systems for biological bodies. Biological bodies move and act in
rich real-world surroundings: According to Clark, we are \"good at
frisbee, bad at logic.\" The embodied cognition approach claims that it
makes no sense to consider the brain separately: cognition takes place
within a body, which is embedded in an environment. We need to study the
system as a whole; the brain\'s functioning exploits regularities in its
environment, including the rest of its body. Under the embodied
cognition approach, robotics, vision, and other sensors become central,
not peripheral. Citations References Garcez, Artur; Besold, Tarek; De
Raedt, Luc; Földiák, Peter; Hitzler, Pascal; Icard, Thomas; Kühnberger,
Kai-Uwe; Lamb, Luís; Miikkulainen, Risto; Silver, Daniel (2015).
Neural-Symbolic Learning and Reasoning: Contributions and Challenges.
AAI Spring Symposium - Knowledge Representation and Reasoning:
Integrating Symbolic and Neural Approaches. Stanford, CA: AAAI Press.
doi:10.13140/2.1.1779.4243. Garcez, Artur d\'Avila; Lamb, Luis C.
(2020), Neurosymbolic AI: The 3rd Wave, arXiv:2012.05876 Haugeland, John
(1985), Artificial Intelligence: The Very Idea, Cambridge, Mass: MIT
Press, ISBN 0-262-08153-9 Kautz, Henry (2020). The Third AI Summer,
Henry Kautz, AAAI 2020 Robert S. Engelmore Memorial Award Lecture.
Retrieved 2022-07-06. Kautz, Henry (2022). \"The Third AI Summer: AAAI
Robert S. Engelmore Memorial Lecture\". AI Magazine. 43 (1): 93--104.
doi:10.1609/aimag.v43i1.19122. ISSN 2371-9621. S2CID 248213051.
Retrieved 2022-07-12. Kodratoff, Yves; Michalski, Ryszard, eds. (1990).
Machine Learning : an Artificial Intelligence Approach. Vol. III. San
Mateo, Calif.: Morgan Kaufman. ISBN 0-934613-09-5. OCLC 893488404.
Marcus, Gary (2020), The Next Decade in AI: Four Steps Towards Robust
Artificial Intelligence, arXiv:2002.06177 Michalski, R. S.; Carbonell,
J. G.; Mitchell, T. M., eds. (1983). Machine Learning: An Artificial
Intelligence Approach. Vol. I. Palo Alto, CA: Tioga. Michalski, R. S.;
Carbonell, J. G.; Mitchell, T. M., eds. (1986). Machine Learning: An
Artificial Intelligence Approach. Vol. II. Morgan Kaufmann. Rossi,
Francesca (2022-07-06). \"AAAI2022: Thinking Fast and Slow in AI (AAAI
2022 Invited Talk)\". Retrieved 2022-07-06. Russell, Stuart J.; Norvig,
Peter (2003). Artificial Intelligence: A Modern Approach (2nd ed.).
Upper Saddle River, N.J: Prentice Hall. ISBN 978-0-13-790395-5. Russell,
Stuart J.; Norvig, Peter (2021). Artificial Intelligence: A Modern
Approach (4th ed.). Hoboken: Pearson. ISBN 9780134610993. LCCN 20190474.
Selman, Bart (2022-07-06). \"AAAI2022: Presidential Address: The State
of AI\". Retrieved 2022-07-06. Turing, A. M. (1950). \"I.---Computing
Machinery and Intelligence\". Mind. LIX (236): 433--460.
doi:10.1093/mind/LIX.236.433. ISSN 0026-4423. Retrieved 2022-09-14.
