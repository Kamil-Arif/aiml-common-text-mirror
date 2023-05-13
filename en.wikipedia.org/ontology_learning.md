Ontology learning (ontology extraction, ontology generation, or ontology
acquisition) is the automatic or semi-automatic creation of ontologies,
including extracting the corresponding domain\'s terms and the
relationships between the concepts that these terms represent from a
corpus of natural language text, and encoding them with an ontology
language for easy retrieval. As building ontologies manually is
extremely labor-intensive and time-consuming, there is great motivation
to automate the process. Typically, the process starts by extracting
terms and concepts or noun phrases from plain text using linguistic
processors such as part-of-speech tagging and phrase chunking. Then
statistical or symbolic techniques are used to extract relation
signatures, often based on pattern-based or definition-based hypernym
extraction techniques. Procedure Ontology learning (OL) is used to
(semi-)automatically extract whole ontologies from natural language
text. The process is usually split into the following eight tasks, which
are not all necessarily applied in every ontology learning system.
Domain terminology extraction During the domain terminology extraction
step, domain-specific terms are extracted, which are used in the
following step (concept discovery) to derive concepts. Relevant terms
can be determined, e.g., by calculation of the TF/IDF values or by
application of the C-value / NC-value method. The resulting list of
terms has to be filtered by a domain expert. In the subsequent step,
similarly to coreference resolution in information extraction, the OL
system determines synonyms, because they share the same meaning and
therefore correspond to the same concept. The most common methods
therefore are clustering and the application of statistical similarity
measures. Concept discovery In the concept discovery step, terms are
grouped to meaning bearing units, which correspond to an abstraction of
the world and therefore to concepts. The grouped terms are these
domain-specific terms and their synonyms, which were identified in the
domain terminology extraction step. Concept hierarchy derivation In the
concept hierarchy derivation step, the OL system tries to arrange the
extracted concepts in a taxonomic structure. This is mostly achieved
with unsupervised hierarchical clustering methods. Because the result of
such methods is often noisy, a supervision step, e.g., user evaluation,
is added. A further method for the derivation of a concept hierarchy
exists in the usage of several patterns that should indicate a sub- or
supersumption relationship. Patterns like "X, that is a Y" or "X is a Y"
indicate that X is a subclass of Y. Such pattern can be analyzed
efficiently, but they often occur too infrequently to extract enough
sub- or supersumption relationships. Instead, bootstrapping methods are
developed, which learn these patterns automatically and therefore ensure
broader coverage. Learning of non-taxonomic relations In the learning of
non-taxonomic relations step, relationships are extracted that do not
express any sub- or supersumption. Such relationships are, e.g.,
works-for or located-in. There are two common approaches to solve this
subtask. The first is based upon the extraction of anonymous
associations, which are named appropriately in a second step. The second
approach extracts verbs, which indicate a relationship between entities,
represented by the surrounding words. The result of both approaches need
to be evaluated by an ontologist to ensure accuracy. Rule discovery
During rule discovery, axioms (formal description of concepts) are
generated for the extracted concepts. This can be achieved, e.g., by
analyzing the syntactic structure of a natural language definition and
the application of transformation rules on the resulting dependency
tree. The result of this process is a list of axioms, which, afterwards,
is comprehended to a concept description. This output is then evaluated
by an ontologist. Ontology population At this step, the ontology is
augmented with instances of concepts and properties. For the
augmentation with instances of concepts, methods based on the matching
of lexico-syntactic patterns are used. Instances of properties are added
through the application of bootstrapping methods, which collect relation
tuples. Concept hierarchy extension In this step, the OL system tries to
extend the taxonomic structure of an existing ontology with further
concepts. This can be performed in a supervised manner with a trained
classifier or in an unsupervised manner via the application of
similarity measures. Frame and Event detection During frame/event
detection, the OL system tries to extract complex relationships from
text, e.g., who departed from where to what place and when. Approaches
range from applying SVM with kernel methods to semantic role labeling
(SRL) to deep semantic parsing techniques. Tools Dog4Dag (Dresden
Ontology Generator for Directed Acyclic Graphs) is an ontology
generation plugin for Protégé 4.1 and OBOEdit 2.1. It allows for term
generation, sibling generation, definition generation, and relationship
induction. Integrated into Protégé 4.1 and OBO-Edit 2.1, DOG4DAG allows
ontology extension for all common ontology formats (e.g., OWL and OBO).
Limited largely to EBI and Bio Portal lookup service extensions. See
also Automatic taxonomy construction Computational linguistics Domain
ontology Information extraction Natural language understanding Semantic
Web Text mining Bibliography P. Buitelaar, P. Cimiano (Eds.). Ontology
Learning and Population: Bridging the Gap between Text and Knowledge,
Series information for Frontiers in Artificial Intelligence and
Applications, IOS Press, 2008. P. Buitelaar, P. Cimiano, and B. Magnini
(Eds.). Ontology Learning from Text: Methods, Evaluation and
Applications, Series information for Frontiers in Artificial
Intelligence and Applications, IOS Press, 2005. Wong, W. (2009),
\"Learning Lightweight Ontologies from Text across Different Domains
using the Web as Background Knowledge\". Doctor of Philosophy thesis,
University of Western Australia. Wong, W., Liu, W. & Bennamoun, M.
(2012), \"Ontology Learning from Text: A Look back and into the
Future\". ACM Computing Surveys, Volume 44, Issue 4, Pages 20:1-20:36.
Thomas Wächter, Götz Fabian, Michael Schroeder: DOG4DAG: semi-automated
ontology generation in OBO-Edit and Protégé. SWAT4LS London, 2011.
doi:10.1145/2166896.2166926 == References ==
