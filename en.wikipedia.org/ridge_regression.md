Ridge regression is a method of estimating the coefficients of
multiple-regression models in scenarios where the independent variables
are highly correlated. It has been used in many fields including
econometrics, chemistry, and engineering. Also known as Tikhonov
regularization, named for Andrey Tikhonov, it is a method of
regularization of ill-posed problems. It is particularly useful to
mitigate the problem of multicollinearity in linear regression, which
commonly occurs in models with large numbers of parameters. In general,
the method provides improved efficiency in parameter estimation problems
in exchange for a tolerable amount of bias (see bias--variance
tradeoff).The theory was first introduced by Hoerl and Kennard in 1970
in their Technometrics papers "RIDGE regressions: biased estimation of
nonorthogonal problems" and "RIDGE regressions: applications in
nonorthogonal problems". This was the result of ten years of research
into the field of ridge analysis.Ridge regression was developed as a
possible solution to the imprecision of least square estimators when
linear regression models have some multicollinear (highly correlated)
independent variables---by creating a ridge regression estimator (RR).
This provides a more precise ridge parameters estimate, as its variance
and mean square estimator are often smaller than the least square
estimators previously derived. Overview In the simplest case, the
problem of a near-singular moment matrix ( X T X ) {\\displaystyle
(\\mathbf {X} \^{\\mathsf {T}}\\mathbf {X} )} is alleviated by adding
positive elements to the diagonals, thereby decreasing its condition
number. Analogous to the ordinary least squares estimator, the simple
ridge estimator is then given by β \^ R = ( X T X + λ I ) − 1 X T y
{\\displaystyle {\\hat {\\beta }}\_{R}=(\\mathbf {X} \^{\\mathsf
{T}}\\mathbf {X} +\\lambda \\mathbf {I} )\^{-1}\\mathbf {X} \^{\\mathsf
{T}}\\mathbf {y} } where y {\\displaystyle \\mathbf {y} } is the
regressand, X {\\displaystyle \\mathbf {X} } is the design matrix, I
{\\displaystyle \\mathbf {I} } is the identity matrix, and the ridge
parameter λ ≥ 0 {\\displaystyle \\lambda \\geq 0} serves as the constant
shifting the diagonals of the moment matrix. It can be shown that this
estimator is the solution to the least squares problem subject to the
constraint β T β = c {\\displaystyle \\beta \^{\\mathsf {T}}\\beta =c} ,
which can be expressed as a Lagrangian: min β ( y − X β ) T ( y − X β
) + λ ( β T β − c ) {\\displaystyle \\min \_{\\beta }\\,(\\mathbf {y}
-\\mathbf {X} \\beta )\^{\\mathsf {T}}(\\mathbf {y} -\\mathbf {X} \\beta
)+\\lambda (\\beta \^{\\mathsf {T}}\\beta -c)} which shows that λ
{\\displaystyle \\lambda } is nothing but the Lagrange multiplier of the
constraint. Typically, λ {\\displaystyle \\lambda } is chosen according
to a heuristic criterion, so that the constraint will not be satisfied
exactly. Specifically in the case of λ = 0 {\\displaystyle \\lambda =0}
, in which the constraint is non-binding, the ridge estimator reduces to
ordinary least squares. A more general approach to Tikhonov
regularization is discussed below. History Tikhonov regularization has
been invented independently in many different contexts. It became widely
known from its application to integral equations from the work of Andrey
Tikhonov and David L. Phillips. Some authors use the term
Tikhonov--Phillips regularization. The finite-dimensional case was
expounded by Arthur E. Hoerl, who took a statistical approach, and by
Manus Foster, who interpreted this method as a Wiener--Kolmogorov
(Kriging) filter. Following Hoerl, it is known in the statistical
literature as ridge regression, named after the shape along the diagonal
of the identity matrix. Tikhonov regularization Suppose that for a known
matrix A {\\displaystyle A} and vector b {\\displaystyle \\mathbf {b} }
, we wish to find a vector x {\\displaystyle \\mathbf {x} } such that A
x = b . {\\displaystyle A\\mathbf {x} =\\mathbf {b} .} The standard
approach is ordinary least squares linear regression. However, if no x
{\\displaystyle \\mathbf {x} } satisfies the equation or more than one x
{\\displaystyle \\mathbf {x} } does---that is, the solution is not
unique---the problem is said to be ill posed. In such cases, ordinary
least squares estimation leads to an overdetermined, or more often an
underdetermined system of equations. Most real-world phenomena have the
effect of low-pass filters in the forward direction where A
{\\displaystyle A} maps x {\\displaystyle \\mathbf {x} } to b
{\\displaystyle \\mathbf {b} } . Therefore, in solving the
inverse-problem, the inverse mapping operates as a high-pass filter that
has the undesirable tendency of amplifying noise (eigenvalues / singular
values are largest in the reverse mapping where they were smallest in
the forward mapping). In addition, ordinary least squares implicitly
nullifies every element of the reconstructed version of x
{\\displaystyle \\mathbf {x} } that is in the null-space of A
{\\displaystyle A} , rather than allowing for a model to be used as a
prior for x {\\displaystyle \\mathbf {x} } . Ordinary least squares
seeks to minimize the sum of squared residuals, which can be compactly
written as ‖ A x − b ‖ 2 2 , {\\displaystyle \\\|A\\mathbf {x} -\\mathbf
{b} \\\|\_{2}\^{2},} where ‖ ⋅ ‖ 2 {\\displaystyle \\\|\\cdot \\\|\_{2}}
is the Euclidean norm. In order to give preference to a particular
solution with desirable properties, a regularization term can be
included in this minimization: ‖ A x − b ‖ 2 2 + ‖ Γ x ‖ 2 2
{\\displaystyle \\\|A\\mathbf {x} -\\mathbf {b}
\\\|\_{2}\^{2}+\\\|\\Gamma \\mathbf {x} \\\|\_{2}\^{2}} for some
suitably chosen Tikhonov matrix Γ {\\displaystyle \\Gamma } . In many
cases, this matrix is chosen as a scalar multiple of the identity matrix
( Γ = α I {\\displaystyle \\Gamma =\\alpha I} ), giving preference to
solutions with smaller norms; this is known as L2 regularization. In
other cases, high-pass operators (e.g., a difference operator or a
weighted Fourier operator) may be used to enforce smoothness if the
underlying vector is believed to be mostly continuous. This
regularization improves the conditioning of the problem, thus enabling a
direct numerical solution. An explicit solution, denoted by x \^
{\\displaystyle {\\hat {x}}} , is given by x \^ = ( A ⊤ A + Γ ⊤ Γ ) − 1
A ⊤ b . {\\displaystyle {\\hat {x}}=(A\^{\\top }A+\\Gamma \^{\\top
}\\Gamma )\^{-1}A\^{\\top }\\mathbf {b} .} The effect of regularization
may be varied by the scale of matrix Γ {\\displaystyle \\Gamma } . For Γ
= 0 {\\displaystyle \\Gamma =0} this reduces to the unregularized
least-squares solution, provided that (ATA)−1 exists. L2 regularization
is used in many contexts aside from linear regression, such as
classification with logistic regression or support vector machines, and
matrix factorization. Generalized Tikhonov regularization For general
multivariate normal distributions for x {\\displaystyle x} and the data
error, one can apply a transformation of the variables to reduce to the
case above. Equivalently, one can seek an x {\\displaystyle x} to
minimize ‖ A x − b ‖ P 2 + ‖ x − x 0 ‖ Q 2 , {\\displaystyle
\\\|Ax-b\\\|\_{P}\^{2}+\\\|x-x\_{0}\\\|\_{Q}\^{2},} where we have used ‖
x ‖ Q 2 {\\displaystyle \\\|x\\\|\_{Q}\^{2}} to stand for the weighted
norm squared x ⊤ Q x {\\displaystyle x\^{\\top }Qx} (compare with the
Mahalanobis distance). In the Bayesian interpretation P {\\displaystyle
P} is the inverse covariance matrix of b {\\displaystyle b} , x 0
{\\displaystyle x\_{0}} is the expected value of x {\\displaystyle x} ,
and Q {\\displaystyle Q} is the inverse covariance matrix of x
{\\displaystyle x} . The Tikhonov matrix is then given as a
factorization of the matrix Q = Γ ⊤ Γ {\\displaystyle Q=\\Gamma \^{\\top
}\\Gamma } (e.g. the Cholesky factorization) and is considered a
whitening filter. This generalized problem has an optimal solution x ∗
{\\displaystyle x\^{\*}} which can be written explicitly using the
formula x ∗ = ( A ⊤ P A + Q ) − 1 ( A ⊤ P b + Q x 0 ) , {\\displaystyle
x\^{\*}=(A\^{\\top }PA+Q)\^{-1}(A\^{\\top }Pb+Qx\_{0}),} or equivalently
x ∗ = x 0 + ( A ⊤ P A + Q ) − 1 ( A ⊤ P ( b − A x 0 ) ) .
{\\displaystyle x\^{\*}=x\_{0}+(A\^{\\top }PA+Q)\^{-1}(A\^{\\top
}P(b-Ax\_{0})).} Lavrentyev regularization In some situations, one can
avoid using the transpose A ⊤ {\\displaystyle A\^{\\top }} , as proposed
by Mikhail Lavrentyev. For example, if A {\\displaystyle A} is symmetric
positive definite, i.e. A = A ⊤ \> 0 {\\displaystyle A=A\^{\\top }\>0} ,
so is its inverse A − 1 {\\displaystyle A\^{-1}} , which can thus be
used to set up the weighted norm squared ‖ x ‖ P 2 = x ⊤ A − 1 x
{\\displaystyle \\\|x\\\|\_{P}\^{2}=x\^{\\top }A\^{-1}x} in the
generalized Tikhonov regularization, leading to minimizing ‖ A x − b ‖ A
− 1 2 + ‖ x − x 0 ‖ Q 2 {\\displaystyle
\\\|Ax-b\\\|\_{A\^{-1}}\^{2}+\\\|x-x\_{0}\\\|\_{Q}\^{2}} or,
equivalently up to a constant term, x ⊤ ( A + Q ) x − 2 x ⊤ ( b + Q x 0
) {\\displaystyle x\^{\\top }(A+Q)x-2x\^{\\top }(b+Qx\_{0})} .This
minimization problem has an optimal solution x ∗ {\\displaystyle
x\^{\*}} which can be written explicitly using the formula x ∗ = ( A + Q
) − 1 ( b + Q x 0 ) {\\displaystyle x\^{\*}=(A+Q)\^{-1}(b+Qx\_{0})}
,which is nothing but the solution of the generalized Tikhonov problem
where A = A ⊤ = P − 1 . {\\displaystyle A=A\^{\\top }=P\^{-1}.} The
Lavrentyev regularization, if applicable, is advantageous to the
original Tikhonov regularization, since the Lavrentyev matrix A + Q
{\\displaystyle A+Q} can be better conditioned, i.e., have a smaller
condition number, compared to the Tikhonov matrix A ⊤ A + Γ ⊤ Γ .
{\\displaystyle A\^{\\top }A+\\Gamma \^{\\top }\\Gamma .} Regularization
in Hilbert space Typically discrete linear ill-conditioned problems
result from discretization of integral equations, and one can formulate
a Tikhonov regularization in the original infinite-dimensional context.
In the above we can interpret A {\\displaystyle A} as a compact operator
on Hilbert spaces, and x {\\displaystyle x} and b {\\displaystyle b} as
elements in the domain and range of A {\\displaystyle A} . The operator
A ∗ A + Γ ⊤ Γ {\\displaystyle A\^{\*}A+\\Gamma \^{\\top }\\Gamma } is
then a self-adjoint bounded invertible operator. Relation to
singular-value decomposition and Wiener filter With Γ = α I
{\\displaystyle \\Gamma =\\alpha I} , this least-squares solution can be
analyzed in a special way using the singular-value decomposition. Given
the singular value decomposition A = U Σ V ⊤ {\\displaystyle A=U\\Sigma
V\^{\\top }} with singular values σ i {\\displaystyle \\sigma \_{i}} ,
the Tikhonov regularized solution can be expressed as x \^ = V D U ⊤ b ,
{\\displaystyle {\\hat {x}}=VDU\^{\\top }b,} where D {\\displaystyle D}
has diagonal values D i i = σ i σ i 2 + α 2 {\\displaystyle
D\_{ii}={\\frac {\\sigma \_{i}}{\\sigma \_{i}\^{2}+\\alpha \^{2}}}} and
is zero elsewhere. This demonstrates the effect of the Tikhonov
parameter on the condition number of the regularized problem. For the
generalized case, a similar representation can be derived using a
generalized singular-value decomposition.Finally, it is related to the
Wiener filter: x \^ = ∑ i = 1 q f i u i ⊤ b σ i v i , {\\displaystyle
{\\hat {x}}=\\sum \_{i=1}\^{q}f\_{i}{\\frac {u\_{i}\^{\\top }b}{\\sigma
\_{i}}}v\_{i},} where the Wiener weights are f i = σ i 2 σ i 2 + α 2
{\\displaystyle f\_{i}={\\frac {\\sigma \_{i}\^{2}}{\\sigma
\_{i}\^{2}+\\alpha \^{2}}}} and q {\\displaystyle q} is the rank of A
{\\displaystyle A} . Determination of the Tikhonov factor The optimal
regularization parameter α {\\displaystyle \\alpha } is usually unknown
and often in practical problems is determined by an ad hoc method. A
possible approach relies on the Bayesian interpretation described below.
Other approaches include the discrepancy principle, cross-validation,
L-curve method, restricted maximum likelihood and unbiased predictive
risk estimator. Grace Wahba proved that the optimal parameter, in the
sense of leave-one-out cross-validation minimizes G = RSS τ 2 = ‖ X β \^
− y ‖ 2 \[ Tr ⁡ ( I − X ( X T X + α 2 I ) − 1 X T ) \] 2 ,
{\\displaystyle G={\\frac {\\operatorname {RSS} }{\\tau \^{2}}}={\\frac
{\\\|X{\\hat {\\beta }}-y\\\|\^{2}}{\[\\operatorname {Tr}
(I-X(X\^{T}X+\\alpha \^{2}I)\^{-1}X\^{T})\]\^{2}}},} where RSS
{\\displaystyle \\operatorname {RSS} } is the residual sum of squares,
and τ {\\displaystyle \\tau } is the effective number of degrees of
freedom. Using the previous SVD decomposition, we can simplify the above
expression: RSS = ‖ y − ∑ i = 1 q ( u i ′ b ) u i ‖ 2 + ‖ ∑ i = 1 q α 2
σ i 2 + α 2 ( u i ′ b ) u i ‖ 2 , {\\displaystyle \\operatorname {RSS}
=\\left\\\|y-\\sum
\_{i=1}\^{q}(u\_{i}\'b)u\_{i}\\right\\\|\^{2}+\\left\\\|\\sum
\_{i=1}\^{q}{\\frac {\\alpha \^{2}}{\\sigma \_{i}\^{2}+\\alpha
\^{2}}}(u\_{i}\'b)u\_{i}\\right\\\|\^{2},} RSS = RSS 0 + ‖ ∑ i = 1 q α 2
σ i 2 + α 2 ( u i ′ b ) u i ‖ 2 , {\\displaystyle \\operatorname {RSS}
=\\operatorname {RSS} \_{0}+\\left\\\|\\sum \_{i=1}\^{q}{\\frac {\\alpha
\^{2}}{\\sigma \_{i}\^{2}+\\alpha
\^{2}}}(u\_{i}\'b)u\_{i}\\right\\\|\^{2},} and τ = m − ∑ i = 1 q σ i 2 σ
i 2 + α 2 = m − q + ∑ i = 1 q α 2 σ i 2 + α 2 . {\\displaystyle \\tau
=m-\\sum \_{i=1}\^{q}{\\frac {\\sigma \_{i}\^{2}}{\\sigma
\_{i}\^{2}+\\alpha \^{2}}}=m-q+\\sum \_{i=1}\^{q}{\\frac {\\alpha
\^{2}}{\\sigma \_{i}\^{2}+\\alpha \^{2}}}.} Relation to probabilistic
formulation The probabilistic formulation of an inverse problem
introduces (when all uncertainties are Gaussian) a covariance matrix C M
{\\displaystyle C\_{M}} representing the a priori uncertainties on the
model parameters, and a covariance matrix C D {\\displaystyle C\_{D}}
representing the uncertainties on the observed parameters. In the
special case when these two matrices are diagonal and isotropic, C M = σ
M 2 I {\\displaystyle C\_{M}=\\sigma \_{M}\^{2}I} and C D = σ D 2 I
{\\displaystyle C\_{D}=\\sigma \_{D}\^{2}I} , and, in this case, the
equations of inverse theory reduce to the equations above, with α = σ D
/ σ M {\\displaystyle \\alpha ={\\sigma \_{D}}/{\\sigma \_{M}}} .
Bayesian interpretation Although at first the choice of the solution to
this regularized problem may look artificial, and indeed the matrix Γ
{\\displaystyle \\Gamma } seems rather arbitrary, the process can be
justified from a Bayesian point of view. Note that for an ill-posed
problem one must necessarily introduce some additional assumptions in
order to get a unique solution. Statistically, the prior probability
distribution of x {\\displaystyle x} is sometimes taken to be a
multivariate normal distribution. For simplicity here, the following
assumptions are made: the means are zero; their components are
independent; the components have the same standard deviation σ x
{\\displaystyle \\sigma \_{x}} . The data are also subject to errors,
and the errors in b {\\displaystyle b} are also assumed to be
independent with zero mean and standard deviation σ b {\\displaystyle
\\sigma \_{b}} . Under these assumptions the Tikhonov-regularized
solution is the most probable solution given the data and the a priori
distribution of x {\\displaystyle x} , according to Bayes\' theorem.If
the assumption of normality is replaced by assumptions of
homoscedasticity and uncorrelatedness of errors, and if one still
assumes zero mean, then the Gauss--Markov theorem entails that the
solution is the minimal unbiased linear estimator. See also LASSO
estimator is another regularization method in statistics. Elastic net
regularization Matrix regularization Notes References Further reading
Gruber, Marvin (1998). Improving Efficiency by Shrinkage: The
James--Stein and Ridge Regression Estimators. Boca Raton: CRC Press.
ISBN 0-8247-0156-9. Kress, Rainer (1998). \"Tikhonov Regularization\".
Numerical Analysis. New York: Springer. pp. 86--90. ISBN 0-387-98408-9.
Press, W. H.; Teukolsky, S. A.; Vetterling, W. T.; Flannery, B. P.
(2007). \"Section 19.5. Linear Regularization Methods\". Numerical
Recipes: The Art of Scientific Computing (3rd ed.). New York: Cambridge
University Press. ISBN 978-0-521-88068-8. Saleh, A. K. Md. Ehsanes;
Arashi, Mohammad; Kibria, B. M. Golam (2019). Theory of Ridge Regression
Estimation with Applications. New York: John Wiley & Sons. ISBN
978-1-118-64461-4. Taddy, Matt (2019). \"Regularization\". Business Data
Science: Combining Machine Learning and Economics to Optimize, Automate,
and Accelerate Business Decisions. New York: McGraw-Hill. pp. 69--104.
ISBN 978-1-260-45277-8.
