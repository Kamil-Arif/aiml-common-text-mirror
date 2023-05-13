The proper generalized decomposition (PGD) is an iterative numerical
method for solving boundary value problems (BVPs), that is, partial
differential equations constrained by a set of boundary conditions, such
as the Poisson\'s equation or the Laplace\'s equation. The PGD algorithm
computes an approximation of the solution of the BVP by successive
enrichment. This means that, in each iteration, a new component (or
mode) is computed and added to the approximation. In principle, the more
modes obtained, the closer the approximation is to its theoretical
solution. Unlike POD principal components, PGD modes are not necessarily
orthogonal to each other. By selecting only the most relevant PGD modes,
a reduced order model of the solution is obtained. Because of this, PGD
is considered a dimensionality reduction algorithm. Description The
proper generalized decomposition is a method characterized by a
variational formulation of the problem, a discretization of the domain
in the style of the finite element method, the assumption that the
solution can be approximated as a separate representation and a
numerical greedy algorithm to find the solution. Variational formulation
The most implemented variational formulation in PGD is the
Bubnov-Galerkin method, although other implementations exist. Domain
discretization The discretization of the domain is a well defined set of
procedures that cover (a) the creation of finite element meshes, (b) the
definition of basis function on reference elements (also called shape
functions) and (c) the mapping of reference elements onto the elements
of the mesh. Separate representation PGD assumes that the solution u of
a (multidimensional) problem can be approximated as a separate
representation of the form where the number of addends N and the
functional products X1(x1), X2(x2), \..., Xd(xd), each depending on a
variable (or variables), are unknown beforehand. Greedy algorithm The
solution is sought by applying a greedy algorithm, usually the fixed
point algorithm, to the weak formulation of the problem. For each
iteration i of the algorithm, a mode of the solution is computed. Each
mode consists of a set of numerical values of the functional products
X1(x1), \..., Xd(xd), which enrich the approximation of the solution.
Due to the greedy nature of the algorithm, the term \'enrich\' is used
rather than \'improve\', since some modes may actually worsen the
approach. The number of computed modes required to obtain an
approximation of the solution below a certain error threshold depends on
the stop criterium of the iterative algorithm. Features PGD is suitable
for solving high-dimensional problems, since it overcomes the
limitations of classical approaches. In particular, PGD avoids the curse
of dimensionality, as solving decoupled problems is computationally much
less expensive than solving multidimensional problems. Therefore, PGD
enables to re-adapt parametric problems into a multidimensional
framework by setting the parameters of the problem as extra coordinates:
where a series of functional products K1(k1), K2(k2), \..., Kp(kp), each
depending on a parameter (or parameters), has been incorporated to the
equation. In this case, the obtained approximation of the solution is
called computational vademecum: a general meta-model containing all the
particular solutions for every possible value of the involved
parameters. Sparse Subspace Learning The Sparse Subspace Learning (SSL)
method leverages the use of hierarchical collocation to approximate the
numerical solution of parametric models. With respect to traditional
projection-based reduced order modeling, the use of a collocation
enables non-intrusive approach based on sparse adaptive sampling of the
parametric space. This allows to recover the lowdimensional structure of
the parametric solution subspace while also learning the functional
dependency from the parameters in explicit form. A sparse low-rank
approximate tensor representation of the parametric solution can be
built through an incremental strategy that only needs to have access to
the output of a deterministic solver. Non-intrusiveness makes this
approach straightforwardly applicable to challenging problems
characterized by nonlinearity or non affine weak forms. == References ==
