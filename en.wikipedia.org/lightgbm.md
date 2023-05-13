LightGBM, short for light gradient-boosting machine, is a free and
open-source distributed gradient-boosting framework for machine
learning, originally developed by Microsoft. It is based on decision
tree algorithms and used for ranking, classification and other machine
learning tasks. The development focus is on performance and scalability.
Overview The LightGBM framework supports different algorithms including
GBT, GBDT, GBRT, GBM, MART and RF. LightGBM has many of XGBoost\'s
advantages, including sparse optimization, parallel training, multiple
loss functions, regularization, bagging, and early stopping. A major
difference between the two lies in the construction of trees. LightGBM
does not grow a tree level-wise --- row by row --- as most other
implementations do. Instead it grows trees leaf-wise. It chooses the
leaf it believes will yield the largest decrease in loss. Besides,
LightGBM does not use the widely used sorted-based decision tree
learning algorithm, which searches the best split point on sorted
feature values, as XGBoost or other implementations do. Instead,
LightGBM implements a highly optimized histogram-based decision tree
learning algorithm, which yields great advantages on both efficiency and
memory consumption. The LightGBM algorithm utilizes two novel techniques
called Gradient-Based One-Side Sampling (GOSS) and Exclusive Feature
Bundling (EFB) which allow the algorithm to run faster while maintaining
a high level of accuracy.LightGBM works on Linux, Windows, and macOS and
supports C++, Python, R, and C#. The source code is licensed under MIT
License and available on GitHub. Gradient-based one-side sampling
Gradient-based one-side sampling (GOSS) is a method that leverages the
fact that there is no native weight for data instance in GBDT. Since
data instances with different gradients play different roles in the
computation of information gain, the instances with larger gradients
will contribute more to the information gain. So to retain the accuracy
of the information, GOSS keeps the instances with large gradients and
randomly drops the instances with small gradients. Exclusive feature
bundling Exclusive feature bundling (EFB) is a near-lossless method to
reduce the number of effective features. In a sparse feature space many
features are nearly exclusive, implying they rarely take nonzero values
simultaneously. One-hot encoded features are a perfect example of
exclusive features. EFB bundles these features, reducing dimensionality
to improve efficiency while maintaining a high level of accuracy. The
bundle of exclusive features into a single feature is called an
exclusive feature bundle. See also Machine learning ML.NET Data binning
Gradient boosting XGBoost CatBoost scikit-learn References Further
reading Guolin Ke; Qi Meng; Thomas Finely; Taifeng Wang; Wei Chen;
Weidong Ma; Qiwei Ye; Tie-Yan Liu (2017). \"LightGBM: A Highly Efficient
Gradient Boosting Decision Tree\" (PDF). {{cite journal}}: Cite journal
requires \|journal= (help) Quinto, Butch (2020). Next-Generation Machine
Learning with Spark -- Covers XGBoost, LightGBM, Spark NLP, Distributed
Deep Learning with Keras, and More. Apress. ISBN 978-1-4842-5668-8.
Bhave, Roshan (2021). Practical Machine Learning with LightGBM and
Python: Explore Microsoft\'s gradient boosting framework to optimize
machine learning. Packt Publishing. ISBN 978-1800564749. External links
GitHub - microsoft/LightGBM LightGBM - Microsoft Research
