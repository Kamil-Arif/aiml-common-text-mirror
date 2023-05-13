Self-play is a technique for improving the performance of reinforcement
learning agents. Intuitively, agents learn to improve their performance
by playing \"against themselves\". Definition and motivation In
multi-agent reinforcement learning experiments, researchers try to
optimize the performance of a learning agent on a given task, in
cooperation or competition with one or more agents. These agents learn
by trial-and-error, and researchers may choose to have the learning
algorithm play the role of two or more of the different agents. When
successfully executed, this technique has a double advantage: It
provides a straightforward way to determine the actions of the other
agents, resulting in a meaningful challenge. It increases the amount of
experience that can be used to improve the policy, by a factor of two or
more, since the viewpoints of each of the different agents can be used
for learning. Usage Self-play is used by the AlphaZero program to
improve its performance in the games of chess, shogi and go.Self-play is
also used to train the Cicero AI system to outperform humans at the game
of Diplomacy. The technique is also used in training the DeepNash system
to play the game Stratego. Comparison of different self-play techniques
Self-Play (SP): Train agents against itself. Yields an open-ended
curriculum whereby opponent\'s and agent\'s strengths match. Susceptible
to cycles in strategy space: Agent forgets how to play against its prior
versions. Fictitious Self-Play (FSP): Training an agent against a
uniform distribution of all previous policies. Wasting a large number of
interactions against weaker opponents. Prioritized Fictitious Self-Play
(PFSP): Yields a curriculum over opponents that provide a good learning
signal Matches agent A with a frozen opponent B from the set of
candidates C with a specific probability. Connections to other
disciplines Self-play has been compared to the epistemological concept
of tabula rasa that describes the way that humans acquire knowledge from
a \"blank slate\". Further reading DiGiovanni, Anthony; Zell, Ethan; et
al. (2021). \"Survey of Self-Play in Reinforcement Learning\".
arXiv:2107.02850 \[cs.GT\]. == References ==
