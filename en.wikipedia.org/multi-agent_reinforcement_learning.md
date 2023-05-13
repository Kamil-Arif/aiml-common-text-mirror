Multi-agent reinforcement learning (MARL) is a sub-field of
reinforcement learning. It focuses on studying the behavior of multiple
learning agents that coexist in a shared environment. Each agent is
motivated by its own rewards, and does actions to advance its own
interests; in some environments these interests are opposed to the
interests of other agents, resulting in complex group dynamics.
Multi-agent reinforcement learning is closely related to game theory and
especially repeated games, as well as multi-agent systems. Its study
combines the pursuit of finding ideal algorithms that maximize rewards
with a more sociological set of concepts. While research in single-agent
reinforcement learning is concerned with finding the algorithm that gets
the biggest number of points for one agent, research in multi-agent
reinforcement learning evaluates and quantifies social metrics, such as
cooperation, reciprocity, equity, social influence, language and
discrimination. Definition Similarly to single-agent reinforcement
learning, multi-agent reinforcement learning is modeled as some form of
a Markov decision process (MDP). For example, A set S {\\displaystyle S}
of environment states. One set A i {\\displaystyle {\\mathcal {A}}\_{i}}
of actions for each of the agents i ∈ I = { 1 , . . . , N }
{\\displaystyle i\\in I=\\{1,\...,N\\}} . P a → ( s , s ′ ) = Pr ( s t +
1 = s ′ ∣ s t = s , a → t = a → ) {\\displaystyle P\_{\\overrightarrow
{a}}(s,s\')=\\Pr(s\_{t+1}=s\'\\mid s\_{t}=s,{\\overrightarrow
{a}}\_{t}={\\overrightarrow {a}})} is the probability of transition (at
time t {\\displaystyle t} ) from state s {\\displaystyle s} to state s ′
{\\displaystyle s\'} under joint action a → {\\displaystyle
{\\overrightarrow {a}}} . R → a → ( s , s ′ ) {\\displaystyle
{\\overrightarrow {R}}\_{\\overrightarrow {a}}(s,s\')} is the immediate
joint reward after transition from s {\\displaystyle s} to s ′
{\\displaystyle s\'} with joint action a → {\\displaystyle
{\\overrightarrow {a}}} .In settings with perfect information, such as
the games of chess and Go, the MDP would be fully observable. In
settings with imperfect information, especially in real-world
applications like self-driving cars, each agent would access an
observation that only has part of the information about the current
state. In the partially observable setting, the core model is the
partially observable stochastic game in the general case, and the
Decentralized POMDP in the cooperative case. Cooperation vs. competition
When multiple agents are acting in a shared environment their interests
might be aligned or misaligned. MARL allows exploring all the different
alignments and how they affect the agents\' behavior: In pure
competition settings the agents\' rewards are exactly opposite to each
other, and therefore they are playing against each other. Pure
cooperation settings are the other extreme, in which agents get the
exact same rewards, and therefore they are playing with each other.
Mixed-sum settings cover all the games that combine elements of both
cooperation and competition. Pure competition settings When two agents
are playing a zero-sum game, they are in pure competition with each
other. Many traditional games such as chess and Go fall under this
category, as do two-player variants of modern games like StarCraft.
Because each agent can only win at the expense of the other agent, many
complexities are stripped away. There\'s no prospect of communication or
social dilemmas, as neither agent is incentivized to take actions that
benefit its opponent. The Deep Blue and AlphaGo projects demonstrate how
to optimize the performance of agents in pure competition settings. One
complexity that isn\'t stripped away in pure competition settings is
autocurricula. As the agents\' policy is improved using self-play,
multiple layers of learning may occur. Pure cooperation settings MARL is
used to explore how separate agents with identical interests can
communicate and work together. Pure cooperation settings are explored in
recreational cooperative games such as Overcooked, as well as real-world
scenarios in robotics.In pure cooperation settings all the agents get
identical rewards, which means that social dilemmas do not occur. In
pure cooperation settings, oftentimes there are an arbitrary number of
coordination strategies, and agents converge to specific \"conventions\"
when coordinating with each other. The notion of conventions has been
studied in language and also alluded to in more general multi-agent
collaborative tasks. Mixed-sum settings Most real-world scenarios
involving multiple agents have elements of both cooperation and
competition. For example, when multiple self-driving cars are planning
their respective paths, each of them has interests that are diverging
but not exclusive: Each car is minimizing the amount of time it\'s
taking to reach its destination, but all cars have the shared interest
of avoiding a traffic collision.Mixed-sum settings can be explored using
classic matrix games such as prisoner\'s dilemma, more complex
sequential social dilemmas, and recreational mixed-sum games such as
Among Us, Diplomacy and StarCraft II.Mixed-sum settings can give rise to
communication and social dilemmas. Social dilemmas As in game theory,
much of the research in MARL revolves around social dilemmas, such as
prisoner\'s dilemma, chicken and stag hunt.While game theory research
might focus on Nash equilibria and what an ideal policy for an agent
would be, MARL research focuses on how the agents would learn these
ideal policies using a trial-and-error process. The reinforcement
learning algorithms that are used to train the agents are maximizing the
agent\'s own reward; the conflict between the needs of the agents and
the needs of the group is a subject of active research.Various
techniques have been explored in order to induce cooperation in agents:
Modifying the environment rules, adding intrinsic rewards, and more.
Sequential social dilemmas Social dilemmas like prisoner\'s dilemma,
chicken and stag hunt are \"matrix games\". Each agent takes only one
action from a choice of two possible actions, and a simple 2x2 matrix is
used to describe the reward that each agent will get, given the actions
that each agent took. In humans and other living creatures, social
dilemmas tend to be more complex. Agents take multiple actions over
time, and the distinction between cooperating and defecting isn\'t as
clear cut as in matrix games. The concept of a sequential social dilemma
(SSD) was introduced in 2017 as an attempt to model that complexity.
There is ongoing research into defining different kinds of SSDs and
showing cooperative behavior in the agents that act in them.
Autocurricula An autocurriculum (plural: autocurricula) is a
reinforcement learning concept that\'s salient in multi-agent
experiments. As agents improve their performance, they change their
environment; this change in the environment affects themselves and the
other agents. The feedback loop results in several distinct phases of
learning, each depending on the previous one. The stacked layers of
learning are called an autocurriculum. Autocurricula are especially
apparent in adversarial settings, where each group of agents is racing
to counter the current strategy of the opposing group. The Hide and Seek
game is an accessible example of an autocurriculum occurring in an
adversarial setting. In this experiment, a team of seekers is competing
against a team of hiders. Whenever one of the teams learns a new
strategy, the opposing team adapts its strategy to give the best
possible counter. When the hiders learn to use boxes to build a shelter,
the seekers respond by learning to use a ramp to break into that
shelter. The hiders respond by locking the ramps, making them
unavailable for the seekers to use. The seekers then respond by \"box
surfing\", exploiting a glitch in the game to penetrate the shelter.
Each \"level\" of learning is an emergent phenomenon, with the previous
level as its premise. This results in a stack of behaviors, each
dependent on its predecessor. Autocurricula in reinforcement learning
experiments are compared to the stages of the evolution of life on earth
and the development of human culture. A major stage in evolution
happened 2-3 billion years ago, when photosynthesizing life forms
started to produce massive amounts of oxygen, changing the balance of
gases in the atmosphere. In the next stages of evolution,
oxygen-breathing life forms evolved, eventually leading up to land
mammals and human beings. These later stages could only happen after the
photosynthesis stage made oxygen widely available. Similarly, human
culture couldn\'t have gone through the industrial revolution in the
18th century without the resources and insights gained by the
agricultural revolution at around 10,000 BC. Applications Multi-agent
reinforcement learning has been applied to a variety of use cases in
science and industry: AI alignment Multi-agent reinforcement learning
has been used in research into AI alignment. The relationship between
the different agents in a MARL setting can be compared to the
relationship between a human and an AI agent. Research efforts in the
intersection of these two fields attempt to simulate possible conflicts
between a human\'s intentions and an AI agent\'s actions, and then
explore which variables could be changed to prevent these conflicts.
Limitations There are some inherent difficulties about multi-agent deep
reinforcement learning. The environment is not stationary anymore, thus
the Markov property is violated: transitions and rewards do not only
depend on the current state of an agent. Software There are various
tools and frameworks for working with multi-agent reinforcement learning
environments: Further reading Yang, Yaodong; Wang, Jun (2020). \"An
Overview of Multi-Agent Reinforcement Learning from Game Theoretical
Perspective\". arXiv:2011.00583 \[cs.MA\]. == References ==
