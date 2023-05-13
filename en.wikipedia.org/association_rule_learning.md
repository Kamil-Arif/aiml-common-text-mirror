Association rule learning is a rule-based machine learning method for
discovering interesting relations between variables in large databases.
It is intended to identify strong rules discovered in databases using
some measures of interestingness. In any given transaction with a
variety of items, association rules are meant to discover the rules that
determine how or why certain items are connected. Based on the concept
of strong rules, Rakesh Agrawal, Tomasz Imieliński and Arun Swami
introduced association rules for discovering regularities between
products in large-scale transaction data recorded by point-of-sale (POS)
systems in supermarkets. For example, the rule { o n i o n s , p o t a t
o e s } ⇒ { b u r g e r } {\\displaystyle \\{\\mathrm {onions,potatoes}
\\}\\Rightarrow \\{\\mathrm {burger} \\}} found in the sales data of a
supermarket would indicate that if a customer buys onions and potatoes
together, they are likely to also buy hamburger meat. Such information
can be used as the basis for decisions about marketing activities such
as, e.g., promotional pricing or product placements. In addition to the
above example from market basket analysis, association rules are
employed today in many application areas including Web usage mining,
intrusion detection, continuous production, and bioinformatics. In
contrast with sequence mining, association rule learning typically does
not consider the order of items either within a transaction or across
transactions. The association rule algorithm itself consists of various
parameters that can make it difficult for those without some expertise
in data mining to execute, with many rules that are arduous to
understand. Definition Following the original definition by Agrawal,
Imieliński, Swami the problem of association rule mining is defined as:
Let I = { i 1 , i 2 , ... , i n } {\\displaystyle
I=\\{i\_{1},i\_{2},\\ldots ,i\_{n}\\}} be a set of n {\\displaystyle n}
binary attributes called items. Let D = { t 1 , t 2 , ... , t m }
{\\displaystyle D=\\{t\_{1},t\_{2},\\ldots ,t\_{m}\\}} be a set of
transactions called the database. Each transaction in D {\\displaystyle
D} has a unique transaction ID and contains a subset of the items in I
{\\displaystyle I} . A rule is defined as an implication of the form: X
⇒ Y {\\displaystyle X\\Rightarrow Y} , where X , Y ⊆ I {\\displaystyle
X,Y\\subseteq I} . In Agrawal, Imieliński, Swami a rule is defined only
between a set and a single item, X ⇒ i j {\\displaystyle X\\Rightarrow
i\_{j}} for i j ∈ I {\\displaystyle i\_{j}\\in I} . Every rule is
composed by two different sets of items, also known as itemsets, X
{\\displaystyle X} and Y {\\displaystyle Y} , where X {\\displaystyle X}
is called antecedent or left-hand-side (LHS) and Y {\\displaystyle Y}
consequent or right-hand-side (RHS). The antecedent is that item that
can be found in the data while the consequent is the item found when
combined with the antecedent. The statement X ⇒ Y {\\displaystyle
X\\Rightarrow Y} is often read as if X {\\displaystyle X} then Y
{\\displaystyle Y} , where the antecedent ( X {\\displaystyle X} ) is
the if and the consequent ( Y {\\displaystyle Y} ) is the then. This
simply implies that, in theory, whenever X {\\displaystyle X} occurs in
a dataset, then Y {\\displaystyle Y} will as well. Process Association
rules are made by searching data for frequent if-then patterns and by
using a certain criterion under Support and Confidence to define what
the most important relationships are. Support is the evidence of how
frequent an item appears in the data given, as Confidence is defined by
how many times the if-then statements are found true. However, there is
a third criteria that can be used, it is called Lift and it can be used
to compare the expected Confidence and the actual Confidence. Lift will
show how many times the if-then statement is expected to be found to be
true. Association rules are made to calculate from itemsets, which are
created by two or more items. If the rules were built from the analyzing
from all the possible itemsets from the data then there would be so many
rules that they wouldn't have any meaning. That is why Association rules
are typically made from rules that are well represented by the data.
There are many different data mining techniques you could use to find
certain analytics and results, for example, there is Classification
analysis, Clustering analysis, and Regression analysis. What technique
you should use depends on what you are looking for with your data.
Association rules are primarily used to find analytics and a prediction
of customer behavior. For Classification analysis, it would most likely
be used to question, make decisions, and predict behavior. Clustering
analysis is primarily used when there are no assumptions made about the
likely relationships within the data. Regression analysis Is used when
you want to predict the value of a continuous dependent from a number of
independent variables.Benefits There are many benefits of using
Association rules like finding the pattern that helps understand the
correlations and co-occurrences between data sets. A very good
real-world example that uses Association rules would be medicine.
Medicine uses Association rules to help diagnose patients. When
diagnosing patients there are many variables to consider as many
diseases will share similar symptoms. With the use of the Association
rules, doctors can determine the conditional probability of an illness
by comparing symptom relationships from past cases.Downsides However,
Association rules also lead to many different downsides such as finding
the appropriate parameter and threshold settings for the mining
algorithm. But there is also the downside of having a large number of
discovered rules. The reason is that this does not guarantee that the
rules will be found relevant, but it could also cause the algorithm to
have low performance. Sometimes the implemented algorithms will contain
too many variables and parameters. For someone that doesn't have a good
concept of data mining, this might cause them to have trouble
understanding it. ThresholdsWhen using Association rules, you are most
likely to only use Support and Confidence. However, this means you have
to satisfy a user-specified minimum support and a user-specified minimum
confidence at the same time. Usually, the Association rule generation is
split into two different steps that needs to be applied: A minimum
Support threshold to find all the frequent itemsets that are in the
database. A minimum Confidence threshold to the frequent itemsets found
to create rules.The Support Threshold is 30%, Confidence Threshold is
50% The Table on the left is the original unorganized data and the table
on the right is organized by the thresholds. In this case Item C is
better than the thresholds for both Support and Confidence which is why
it is first. Item A is second because its threshold values are spot on.
Item D has met the threshold for Support but not Confidence. Item B has
not met the threshold for either Support or Confidence and that is why
it is last. To find all the frequent itemsets in a database is not an
easy task since it involves going through all the data to find all
possible item combinations from all possible itemsets. The set of
possible itemsets is the power set over I and has size 2 n − 1
{\\displaystyle 2\^{n}-1} , of course this means to exclude the empty
set which is not considered to be a valid itemset. However, the size of
the power set will grow exponentially in the number of item n that is
within the power set I. An efficient search is possible by using the
downward-closure property of support (also called anti-monotonicity).
This would guarantee that a frequent itemset and all its subsets are
also frequent and thus will have no infrequent itemsets as a subset of a
frequent itemset. Exploiting this property, efficient algorithms (e.g.,
Apriori and Eclat) can find all frequent itemsets. Useful Concepts To
illustrate the concepts, we use a small example from the supermarket
domain. Table 2 shows a small database containing the items where, in
each entry, the value 1 means the presence of the item in the
corresponding transaction, and the value 0 represents the absence of an
item in that transaction. The set of items is I = { m i l k , b r e a d
, b u t t e r , b e e r , d i a p e r s , e g g s , f r u i t }
{\\displaystyle I=\\{\\mathrm
{milk,bread,butter,beer,diapers,eggs,fruit} \\}} . An example rule for
the supermarket could be { b u t t e r , b r e a d } ⇒ { m i l k }
{\\displaystyle \\{\\mathrm {butter,bread} \\}\\Rightarrow \\{\\mathrm
{milk} \\}} meaning that if butter and bread are bought, customers also
buy milk. In order to select interesting rules from the set of all
possible rules, constraints on various measures of significance and
interest are used. The best-known constraints are minimum thresholds on
support and confidence. Let X , Y {\\displaystyle X,Y} be itemsets, X ⇒
Y {\\displaystyle X\\Rightarrow Y} an association rule and T a set of
transactions of a given database. Note: this example is extremely small.
In practical applications, a rule needs a support of several hundred
transactions before it can be considered statistically significant, and
datasets often contain thousands or millions of transactions. Support
Support is an indication of how frequently the itemset appears in the
dataset. In our example, it can be easier to explain support by writing
s u p p o r t = P ( A ∩ B ) = ( number of transactions containing A and
B ) (total number of transactions) {\\displaystyle support=P(A\\cap
B)={\\frac {({\\text{number of transactions containing }}A{\\text{ and
}}B)}{\\text{ (total number of transactions)}}}} where A and B are
separate item sets that occur in at the same time in a transaction.
Using Table 2 as an example, the itemset X = { b e e r , d i a p e r s }
{\\displaystyle X=\\{\\mathrm {beer,diapers} \\}} has a support of 1 / 5
= 0.2 {\\displaystyle 1/5=0.2} since it occurs in 20% of all
transactions (1 out of 5 transactions). The argument of support of X is
a set of preconditions, and thus becomes more restrictive as it grows
(instead of more inclusive).Furthermore, the itemset Y = { m i l k , b r
e a d , b u t t e r } {\\displaystyle Y=\\{\\mathrm {milk,bread,butter}
\\}} has a support of 1 / 5 = 0.2 {\\displaystyle 1/5=0.2} as it appears
in 20% of all transactions as well. When using antecedents and
consequents, it allows a data miner to determine the support of multiple
items being bought together in comparison to the whole data set. For
example, Table 2 shows that if milk is bought, then bread is bought has
a support of 0.4 or 40%. This because in 2 out 5 of the transactions,
milk as well as bread are bought. In smaller data sets like this
example, it is harder to see a strong correlation when there are few
samples, but when the data set grows larger, support can be used to find
correlation between two or more products in the supermarket example.
Minimum support thresholds are useful for determining which itemsets are
preferred or interesting. If we set the support threshold to ≥0.4 in
Table 3, then the { m i l k } ⇒ { e g g s } {\\displaystyle \\{\\mathrm
{milk} \\}\\Rightarrow \\{\\mathrm {eggs} \\}} would be removed since it
did not meet the minimum threshold of 0.4. Minimum threshold is used to
remove samples where there is not a strong enough support or confidence
to deem the sample as important or interesting in the dataset. Another
way of finding interesting samples is to find the value of
(support)X(confidence); this allows a data miner to see the samples
where support and confidence are high enough to be highlighted in the
dataset and prompt a closer look at the sample to find more information
on the connection between the items. Support can be beneficial for
finding the connection between products in comparison to the whole
dataset, whereas confidence looks at the connection between one or more
items and another item. Below is a table that shows the comparison and
contrast between support and support x confidence, using the information
from Table 4 to derive the confidence values. The support of X with
respect to T is defined as the proportion of transactions in the dataset
which contains the itemset X. Denoting a transaction by ( i , t )
{\\displaystyle (i,t)} where i is the unique identifier of the
transaction and t is its itemset, the support may be written as: s u p p
o r t o f X = \| { ( i , t ) ∈ T : X ⊆ t } \| \| T \| {\\displaystyle
\\mathrm {support\\,of\\,X} ={\\frac {\|\\{(i,t)\\in T:X\\subseteq
t\\}\|}{\|T\|}}} This notation can be used when defining more
complicated datasets where the items and itemsets may not be as easy as
our supermarket example above. Other examples of where support can be
used is in finding groups of genetic mutations that work collectively to
cause a disease, investigating the number of subscribers that respond to
upgrade offers, and discovering which products in a drug store are never
bought together. Confidence Confidence is the percentage of all
transactions satisfying X that also satisfy Y.With respect to T, the
confidence value of an association rule, often denoted as X ⇒ Y
{\\displaystyle X\\Rightarrow Y} , is the ratio of transactions
containing both X and Y to the total amount of X values present, where X
is the antecedent and Y is the consequent. Confidence can also be
interpreted as an estimate of the conditional probability P ( E Y \| E X
) {\\displaystyle P(E\_{Y}\|E\_{X})} , the probability of finding the
RHS of the rule in transactions under the condition that these
transactions also contain the LHS.It is commonly depicted as: c o n f (
X ⇒ Y ) = P ( Y \| X ) = s u p p ( X ∩ Y ) s u p p ( X ) = number of
transactions containing X and Y number of transactions containing X
{\\displaystyle \\mathrm {conf} (X\\Rightarrow Y)=P(Y\|X)={\\frac
{\\mathrm {supp} (X\\cap Y)}{\\mathrm {supp} (X)}}={\\frac
{{\\text{number of transactions containing }}X{\\text{ and
}}Y}{{\\text{number of transactions containing }}X}}} The equation
illustrates that confidence can be computed by calculating the
co-occurrence of transactions X and Y within the dataset in ratio to
transactions containing only X. This means that the number of
transactions in both X and Y is divided by those just in X . For
example, Table 2 shows the rule { b u t t e r , b r e a d } ⇒ { m i l k
} {\\displaystyle \\{\\mathrm {butter,bread} \\}\\Rightarrow \\{\\mathrm
{milk} \\}} which has a confidence of 1 / 5 1 / 5 = 0.2 0.2 = 1.0
{\\displaystyle {\\frac {1/5}{1/5}}={\\frac {0.2}{0.2}}=1.0} in the
dataset, which denotes that every time a customer buys butter and bread,
they also buy milk. This particular example demonstrates the rule being
correct 100% of the time for transactions containing both butter and
bread. The rule { f r u i t } ⇒ { e g g s } {\\displaystyle \\{\\mathrm
{fruit} \\}\\Rightarrow \\{\\mathrm {eggs} \\}} , however, has a
confidence of 2 / 5 3 / 5 = 0.4 0.6 = 0.67 {\\displaystyle {\\frac
{2/5}{3/5}}={\\frac {0.4}{0.6}}=0.67} . This suggests that eggs are
bought 67% of the times that fruit is brought. Within this particular
dataset, fruit is purchased a total of 3 times, with two of those times
consisting of egg purchases. For larger datasets, a minimum threshold,
or a percentage cutoff, for the confidence can be useful for determining
item relationships. When applying this method to some of the data in
Table 2, information that does not meet the requirements are removed.
Table 4 shows association rule examples where the minimum threshold for
confidence is 0.5 (50%). Any data that does not have a confidence of at
least 0.5 is omitted. Generating thresholds allow for the association
between items to become stronger as the data is further researched by
emphasizing those that co-occur the most. The table uses the confidence
information from Table 3 to implement the Support x Confidence column,
where the relationship between items via their both confidence and
support, instead of just one concept, is highlighted. Ranking the rules
by Support x Confidence multiples the confidence of a particular rule to
its support and is often implemented for a more in-depth understanding
of the relationship between the items. Overall, using confidence in
association rule mining is great way to bring awareness to data
relations. Its greatest benefit is highlighting the relationship between
particular items to one another within the set, as it compares
co-occurrences of items to the total occurrence of the antecedent in the
specific rule. However, confidence is not the optimal method for every
concept in association rule mining. The disadvantage of using it is that
it does not offer multiple difference outlooks on the associations.
Unlike support, for instance, confidence does not provide the
perspective of relationships between certain items in comparison to the
entire dataset, so while milk and bread, for example, may occur 100% of
the time for confidence, it only has a support of 0.4 (40%). This is why
it is important to look at other viewpoints, such as Support x
Confidence, instead of solely relying on one concept incessantly to
define the relationships. Lift The lift of a rule is defined as: l i f t
( X ⇒ Y ) = s u p p ( X ∩ Y ) s u p p ( X ) × s u p p ( Y )
{\\displaystyle \\mathrm {lift} (X\\Rightarrow Y)={\\frac {\\mathrm
{supp} (X\\cap Y)}{\\mathrm {supp} (X)\\times \\mathrm {supp} (Y)}}} or
the ratio of the observed support to that expected if X and Y were
independent. For example, the rule { m i l k , b r e a d } ⇒ { b u t t e
r } {\\displaystyle \\{\\mathrm {milk,bread} \\}\\Rightarrow \\{\\mathrm
{butter} \\}} has a lift of 0.2 0.4 × 0.4 = 1.25 {\\displaystyle {\\frac
{0.2}{0.4\\times 0.4}}=1.25} . If the rule had a lift of 1, it would
imply that the probability of occurrence of the antecedent and that of
the consequent are independent of each other. When two events are
independent of each other, no rule can be drawn involving those two
events. If the lift is \> 1, that lets us know the degree to which those
two occurrences are dependent on one another, and makes those rules
potentially useful for predicting the consequent in future data sets. If
the lift is \< 1, that lets us know the items are substitute to each
other. This means that presence of one item has negative effect on
presence of other item and vice versa. The value of lift is that it
considers both the support of the rule and the overall data set.
Conviction The conviction of a rule is defined as c o n v ( X ⇒ Y ) = 1
− s u p p ( Y ) 1 − c o n f ( X ⇒ Y ) {\\displaystyle \\mathrm {conv}
(X\\Rightarrow Y)={\\frac {1-\\mathrm {supp} (Y)}{1-\\mathrm {conf}
(X\\Rightarrow Y)}}} .For example, the rule { m i l k , b r e a d } ⇒ {
b u t t e r } {\\displaystyle \\{\\mathrm {milk,bread} \\}\\Rightarrow
\\{\\mathrm {butter} \\}} has a conviction of 1 − 0.4 1 − 0.5 = 1.2
{\\displaystyle {\\frac {1-0.4}{1-0.5}}=1.2} , and can be interpreted as
the ratio of the expected frequency that X occurs without Y (that is to
say, the frequency that the rule makes an incorrect prediction) if X and
Y were independent divided by the observed frequency of incorrect
predictions. In this example, the conviction value of 1.2 shows that the
rule { m i l k , b r e a d } ⇒ { b u t t e r } {\\displaystyle
\\{\\mathrm {milk,bread} \\}\\Rightarrow \\{\\mathrm {butter} \\}} would
be incorrect 20% more often (1.2 times as often) if the association
between X and Y was purely random chance. Alternative measures of
interestingness In addition to confidence, other measures of
interestingness for rules have been proposed. Some popular measures are:
All-confidence Collective strength LeverageSeveral more measures are
presented and compared by Tan et al. and by Hahsler. Looking for
techniques that can model what the user has known (and using these
models as interestingness measures) is currently an active research
trend under the name of \"Subjective Interestingness.\" History The
concept of association rules was popularized particularly due to the
1993 article of Agrawal et al., which has acquired more than 23,790
citations according to Google Scholar, as of April 2021, and is thus one
of the most cited papers in the Data Mining field. However, what is now
called \"association rules\" is introduced already in the 1966 paper on
GUHA, a general data mining method developed by Petr Hájek et al.An
early (circa 1989) use of minimum support and confidence to find all
association rules is the Feature Based Modeling framework, which found
all rules with s u p p ( X ) {\\displaystyle \\mathrm {supp} (X)} and c
o n f ( X ⇒ Y ) {\\displaystyle \\mathrm {conf} (X\\Rightarrow Y)}
greater than user defined constraints. Statistically sound associations
One limitation of the standard approach to discovering associations is
that by searching massive numbers of possible associations to look for
collections of items that appear to be associated, there is a large risk
of finding many spurious associations. These are collections of items
that co-occur with unexpected frequency in the data, but only do so by
chance. For example, suppose we are considering a collection of 10,000
items and looking for rules containing two items in the left-hand-side
and 1 item in the right-hand-side. There are approximately
1,000,000,000,000 such rules. If we apply a statistical test for
independence with a significance level of 0.05 it means there is only a
5% chance of accepting a rule if there is no association. If we assume
there are no associations, we should nonetheless expect to find
50,000,000,000 rules. Statistically sound association discovery controls
this risk, in most cases reducing the risk of finding any spurious
associations to a user-specified significance level. Algorithms Many
algorithms for generating association rules have been proposed. Some
well-known algorithms are Apriori, Eclat and FP-Growth, but they only do
half the job, since they are algorithms for mining frequent itemsets.
Another step needs to be done after to generate rules from frequent
itemsets found in a database. Apriori algorithm Apriori is given by R.
Agrawal and R. Srikant in 1994 for frequent item set mining and
association rule learning. It proceeds by identifying the frequent
individual items in the database and extending them to larger and larger
item sets as long as those item sets appear sufficiently often. The name
of the algorithm is Apriori because it uses prior knowledge of frequent
itemset properties. Overview: Apriori uses a \"bottom up\" approach,
where frequent subsets are extended one item at a time (a step known as
candidate generation), and groups of candidates are tested against the
data. The algorithm terminates when no further successful extensions are
found. Apriori uses breadth-first search and a Hash tree structure to
count candidate item sets efficiently. It generates candidate item sets
of length from item sets of length . Then it prunes the candidates which
have an infrequent sub pattern. According to the downward closure lemma,
the candidate set contains all frequent -length item sets. After that,
it scans the transaction database to determine frequent item sets among
the candidates. Example: Assume that each row is a cancer sample with a
certain combination of mutations labeled by a character in the alphabet.
For example a row could have {a, c} which means it is affected by
mutation \'a\' and mutation \'c\'. Now we will generate the frequent
item set by counting the number of occurrences of each character. This
is also known as finding the support values. Then we will prune the item
set by picking a minimum support threshold. For this pass of the
algorithm we will pick 3. Since all support values are three or above
there is no pruning. The frequent item set is {a}, {b}, {c}, and {d}.
After this we will repeat the process by counting pairs of mutations in
the input set. Now we will make our minimum support value 4 so only {a,
d} and {c, d} will remain after pruning. Now we will use the frequent
item set to make combinations of triplets. We will then repeat the
process by counting occurrences of triplets of mutations in the input
set. Since we only have one item the next set of combinations of
quadruplets is empty so the algorithm will stop. Advantages and
Limitations: Apriori has some limitations. Candidate generation can
result in large candidate sets. For example a 10\^4 frequent 1-itemset
will generate a 10\^7 candidate 2-itemset. The algorithm also needs to
frequently scan the database, to be specific n+1 scans where n is the
length of the longest pattern. Apriori is slower than the Eclat
algorithm. However, Apriori performs well compared to Eclat when the
dataset is large. This is because in the Eclat algorithm if the dataset
is too large the tid-lists become too large for memory. FP-growth
outperforms the Apriori and Eclat. This is due to the FP-growth
algorithm not having candidate generation or test, using a compact data
structure, and only having one database scan. Eclat algorithm Eclat
(alt. ECLAT, stands for Equivalence Class Transformation) is a
backtracking algorithm, which traverses the frequent itemset lattice
graph in a depth-first search (DFS) fashion. Whereas the breadth-first
search (BFS) traversal used in the Apriori algorithm will end up
checking every subset of an itemset before checking it, DFS traversal
checks larger itemsets and can save on checking the support of some of
its subsets by virtue of the downward-closer property. Furthermore it
will almost certainly use less memory as DFS has a lower space
complexity than BFS. To illustrate this, let there be a frequent itemset
{a, b, c}. a DFS may check the nodes in the frequent itemset lattice in
the following order: {a} → {a, b} → {a, b, c}, at which point it is
known that {b}, {c}, {a, c}, {b, c} all satisfy the support constraint
by the downward-closure property. BFS would explore each subset of {a,
b, c} before finally checking it. As the size of an itemset increases,
the number of its subsets undergoes combinatorial explosion. It is
suitable for both sequential as well as parallel execution with
locality-enhancing properties. FP-growth algorithm FP stands for
frequent pattern.In the first pass, the algorithm counts the occurrences
of items (attribute-value pairs) in the dataset of transactions, and
stores these counts in a \'header table\'. In the second pass, it builds
the FP-tree structure by inserting transactions into a trie. Items in
each transaction have to be sorted by descending order of their
frequency in the dataset before being inserted so that the tree can be
processed quickly. Items in each transaction that do not meet the
minimum support requirement are discarded. If many transactions share
most frequent items, the FP-tree provides high compression close to tree
root. Recursive processing of this compressed version of the main
dataset grows frequent item sets directly, instead of generating
candidate items and testing them against the entire database (as in the
apriori algorithm). Growth begins from the bottom of the header table
i.e. the item with the smallest support by finding all sorted
transactions that end in that item. Call this item I {\\displaystyle I}
. A new conditional tree is created which is the original FP-tree
projected onto I {\\displaystyle I} . The supports of all nodes in the
projected tree are re-counted with each node getting the sum of its
children counts. Nodes (and hence subtrees) that do not meet the minimum
support are pruned. Recursive growth ends when no individual items
conditional on I {\\displaystyle I} meet the minimum support threshold.
The resulting paths from root to I {\\displaystyle I} will be frequent
itemsets. After this step, processing continues with the next
least-supported header item of the original FP-tree. Once the recursive
process has completed, all frequent item sets will have been found, and
association rule creation begins. Others ASSOC The ASSOC procedure is a
GUHA method which mines for generalized association rules using fast
bitstrings operations. The association rules mined by this method are
more general than those output by apriori, for example \"items\" can be
connected both with conjunction and disjunctions and the relation
between antecedent and consequent of the rule is not restricted to
setting minimum support and confidence as in apriori: an arbitrary
combination of supported interest measures can be used. OPUS search OPUS
is an efficient algorithm for rule discovery that, in contrast to most
alternatives, does not require either monotone or anti-monotone
constraints such as minimum support. Initially used to find rules for a
fixed consequent it has subsequently been extended to find rules with
any item as a consequent. OPUS search is the core technology in the
popular Magnum Opus association discovery system. Lore A famous story
about association rule mining is the \"beer and diaper\" story. A
purported survey of behavior of supermarket shoppers discovered that
customers (presumably young men) who buy diapers tend also to buy beer.
This anecdote became popular as an example of how unexpected association
rules might be found from everyday data. There are varying opinions as
to how much of the story is true. Daniel Powers says: In 1992, Thomas
Blischok, manager of a retail consulting group at Teradata, and his
staff prepared an analysis of 1.2 million market baskets from about 25
Osco Drug stores. Database queries were developed to identify
affinities. The analysis \"did discover that between 5:00 and 7:00 p.m.
that consumers bought beer and diapers\". Osco managers did NOT exploit
the beer and diapers relationship by moving the products closer together
on the shelves. Other types of association rule mining Multi-Relation
Association Rules (MRAR): These are association rules where each item
may have several relations. These relations indicate indirect
relationships between the entities. Consider the following MRAR where
the first item consists of three relations live in, nearby and humid:
"Those who live in a place which is nearby a city with humid climate
type and also are younger than 20 ⟹ {\\displaystyle \\implies } their
health condition is good". Such association rules can be extracted from
RDBMS data or semantic web data.Contrast set learning is a form of
associative learning. Contrast set learners use rules that differ
meaningfully in their distribution across subsets.Weighted class
learning is another form of associative learning where weights may be
assigned to classes to give focus to a particular issue of concern for
the consumer of the data mining results. High-order pattern discovery
facilitates the capture of high-order (polythetic) patterns or event
associations that are intrinsic to complex real-world data. K-optimal
pattern discovery provides an alternative to the standard approach to
association rule learning which requires that each pattern appear
frequently in the data. Approximate Frequent Itemset mining is a relaxed
version of Frequent Itemset mining that allows some of the items in some
of the rows to be 0.Generalized Association Rules hierarchical taxonomy
(concept hierarchy) Quantitative Association Rules categorical and
quantitative data Interval Data Association Rules e.g. partition the age
into 5-year-increment ranged Sequential pattern mining discovers
subsequences that are common to more than minsup (minimum support
threshold) sequences in a sequence database, where minsup is set by the
user. A sequence is an ordered list of transactions.Subspace Clustering,
a specific type of clustering high-dimensional data, is in many variants
also based on the downward-closure property for specific clustering
models.Warmr, shipped as part of the ACE data mining suite, allows
association rule learning for first order relational rules. See also
Sequence mining Production system (computer science) Learning classifier
system Rule-based machine learning References Bibliographies Annotated
Bibliography on Association Rules by M. Hahsler
