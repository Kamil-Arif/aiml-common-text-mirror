A multi-agent system (MAS or \"self-organized system\") is a
computerized system composed of multiple interacting intelligent agents.
Multi-agent systems can solve problems that are difficult or impossible
for an individual agent or a monolithic system to solve. Intelligence
may include methodic, functional, procedural approaches, algorithmic
search or reinforcement learning.Despite considerable overlap, a
multi-agent system is not always the same as an agent-based model (ABM).
The goal of an ABM is to search for explanatory insight into the
collective behavior of agents (which don\'t necessarily need to be
\"intelligent\") obeying simple rules, typically in natural systems,
rather than in solving specific practical or engineering problems. The
terminology of ABM tends to be used more often in the science, and MAS
in engineering and technology. Applications where multi-agent systems
research may deliver an appropriate approach include online trading,
disaster response, target surveillance and social structure modelling.
Concept Multi-agent systems consist of agents and their environment.
Typically multi-agent systems research refers to software agents.
However, the agents in a multi-agent system could equally well be
robots, humans or human teams. A multi-agent system may contain combined
human-agent teams. Agents can be divided into types spanning simple to
complex. Categories include: Passive agents or \"agent without goals\"
(such as obstacle, apple or key in any simple simulation) Active agents
with simple goals (like birds in flocking, or wolf--sheep in
prey-predator model) Cognitive agents (complex calculations)Agent
environments can be divided into: Virtual Discrete ContinuousAgent
environments can also be organized according to properties such as
accessibility (whether it is possible to gather complete information
about the environment), determinism (whether an action causes a definite
effect), dynamics (how many entities influence the environment in the
moment), discreteness (whether the number of possible actions in the
environment is finite), episodicity (whether agent actions in certain
time periods influence other periods), and dimensionality (whether
spatial characteristics are important factors of the environment and the
agent considers space in its decision making). Agent actions are
typically mediated via an appropriate middleware. This middleware offers
a first-class design abstraction for multi-agent systems, providing
means to govern resource access and agent coordination. Characteristics
The agents in a multi-agent system have several important
characteristics: Autonomy: agents at least partially independent,
self-aware, autonomous Local views: no agent has a full global view, or
the system is too complex for an agent to exploit such knowledge
Decentralization: no agent is designated as controlling (or the system
is effectively reduced to a monolithic system) Self-organisation and
self-direction Multi-agent systems can manifest self-organisation as
well as self-direction and other control paradigms and related complex
behaviors even when the individual strategies of all their agents are
simple. When agents can share knowledge using any agreed language,
within the constraints of the system\'s communication protocol, the
approach may lead to a common improvement. Example languages are
Knowledge Query Manipulation Language (KQML) or Agent Communication
Language (ACL). System paradigms Many MAS are implemented in computer
simulations, stepping the system through discrete \"time steps\". The
MAS components communicate typically using a weighted request matrix,
e.g. Speed-VERY_IMPORTANT: min=45 mph, Path length-MEDIUM_IMPORTANCE:
max=60 expectedMax=40, Max-Weight-UNIMPORTANT Contract Priority-REGULAR
and a weighted response matrix, e.g. Speed-min:50 but only if weather
sunny, Path length:25 for sunny / 46 for rainy Contract Priority-REGULAR
note -- ambulance will override this priority and you\'ll have to wait A
challenge-response-contract scheme is common in MAS systems, where First
a \"Who can?\" question is distributed. Only the relevant components
respond: \"I can, at this price\". Finally, a contract is set up,
usually in several short communication steps between sides,also
considering other components, evolving \"contracts\" and the restriction
sets of the component algorithms. Another paradigm commonly used with
MAS is the \"pheromone\", where components leave information for other
nearby components. These pheromones may evaporate/concentrate with time,
that is their values may decrease (or increase). Properties MAS tend to
find the best solution for their problems without intervention. There is
high similarity here to physical phenomena, such as energy minimizing,
where physical objects tend to reach the lowest energy possible within
the physically constrained world. For example: many of the cars entering
a metropolis in the morning will be available for leaving that same
metropolis in the evening. The systems also tend to prevent propagation
of faults, self-recover and be fault tolerant, mainly due to the
redundancy of components. Research The study of multi-agent systems is
\"concerned with the development and analysis of sophisticated AI
problem-solving and control architectures for both single-agent and
multiple-agent systems.\" Research topics include: agent-oriented
software engineering beliefs, desires, and intentions (BDI) cooperation
and coordination distributed constraint optimization (DCOPs)
organization communication negotiation distributed problem solving
multi-agent learning agent mining scientific communities (e.g., on
biological flocking, language evolution, and economics) dependability
and fault-tolerance robotics, multi-robot systems (MRS), robotic
clusters Frameworks Frameworks have emerged that implement common
standards (such as the FIPA and OMG MASIF standards). These frameworks
e.g. JADE, save time and aid in the standardization of MAS
development.Currently though, no standard is actively maintained from
FIPA or OMG. Efforts for further development of software agents in
industrial context are carried out in IEEE IES technical committee on
Industrial Agents. Applications MAS have not only been applied in
academic research, but also in industry. MAS are applied in the real
world to graphical applications such as computer games. Agent systems
have been used in films. It is widely advocated for use in networking
and mobile technologies, to achieve automatic and dynamic load
balancing, high scalability and self-healing networks. They are being
used for coordinated defence systems. Other applications include
transportation, logistics, graphics, manufacturing, power system,
smartgrids and GIS. Also, Multi-agent Systems Artificial Intelligence
(MAAI) are used for simulating societies, the purpose thereof being
helpful in the fields of climate, energy, epidemiology, conflict
management, child abuse, \.... Some organisations working on using
multi-agent system models include Center for Modelling Social Systems,
Centre for Research in Social Simulation, Centre for Policy Modelling,
Society for Modelling and Simulation International.Vehicular traffic
with controlled autonomous vehicles can be modelling as a multi-agent
system involving crowd dynamics. Hallerbach et al. discussed the
application of agent-based approaches for the development and validation
of automated driving systems via a digital twin of the
vehicle-under-test and microscopic traffic simulation based on
independent agents. Waymo has created a multi-agent simulation
environment Carcraft to test algorithms for self-driving cars. It
simulates traffic interactions between human drivers, pedestrians and
automated vehicles. People\'s behavior is imitated by artificial agents
based on data of real human behavior. See also References Further
reading Wooldridge, Michael (2002). An Introduction to MultiAgent
Systems. John Wiley & Sons. p. 366. ISBN 978-0-471-49691-5. Shoham,
Yoav; Leyton-Brown, Kevin (2008). Multiagent Systems: Algorithmic,
Game-Theoretic, and Logical Foundations. Cambridge University Press. p.
496. ISBN 978-0-521-89943-7. Mamadou, Tadiou Koné; Shimazu, A.;
Nakajima, T. (August 2000). \"The State of the Art in Agent
Communication Languages (ACL)\". Knowledge and Information Systems. 2
(2): 1--26. Hewitt, Carl; Inman, Jeff (Nov--Dec 1991). \"DAI Betwixt and
Between: From \"Intelligent Agents\" to Open Systems Science\" (PDF).
IEEE Transactions on Systems, Man, and Cybernetics. 21 (6): 1409--1419.
doi:10.1109/21.135685. S2CID 39080989. Archived from the original (PDF)
on 2017-08-31. The Journal of Autonomous Agents and Multi-Agent Systems
(JAAMAS) Weiss, Gerhard, ed. (1999). Multiagent Systems, A Modern
Approach to Distributed Artificial Intelligence. MIT Press. ISBN
978-0-262-23203-6. Ferber, Jacques (1999). Multi-Agent Systems: An
Introduction to Artificial Intelligence. Addison-Wesley. ISBN
978-0-201-36048-6. Weyns, Danny (2010). Architecture-Based Design of
Multi-Agent Systems. Springer. ISBN 978-3-642-01063-7. Sun, Ron (2006).
Cognition and Multi-Agent Interaction. Cambridge University Press. ISBN
978-0-521-83964-8. Keil, David; Goldin, Dina (2006). Weyns, Danny;
Parunak, Van; Michel, Fabien (eds.). Indirect Interaction in
Environments for Multiagent Systems. Environments for Multiagent Systems
II. LNCS 3830. Vol. 3830. Springer. pp. 68--87. doi:10.1007/11678809_5.
ISBN 978-3-540-32614-4. Whitestein Series in Software Agent Technologies
and Autonomic Computing, published by Springer Science+Business Media
Group Salamon, Tomas (2011). Design of Agent-Based Models : Developing
Computer Simulations for a Better Understanding of Social Processes.
Bruckner Publishing. ISBN 978-80-904661-1-1. Russell, Stuart J.; Norvig,
Peter (2003), Artificial Intelligence: A Modern Approach (2nd ed.),
Upper Saddle River, New Jersey: Prentice Hall, ISBN 0-13-790395-2 Fasli,
Maria (2007). Agent-technology for E-commerce. John Wiley & Sons. p.
480. ISBN 978-0-470-03030-1. Cao, Longbing, Gorodetsky, Vladimir,
Mitkas, Pericles A. (2009). Agent Mining: The Synergy of Agents and Data
Mining, IEEE Intelligent Systems, vol. 24, no. 3, 64-72.
