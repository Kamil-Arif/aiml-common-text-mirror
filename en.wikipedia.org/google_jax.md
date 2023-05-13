Google JAX is a machine learning framework for transforming numerical
functions. It is described as bringing together a modified version of
autograd (automatic obtaining of the gradient function through
differentiation of a function) and TensorFlow\'s XLA (Accelerated Linear
Algebra). It is designed to follow the structure and workflow of NumPy
as closely as possible and works with various existing frameworks such
as TensorFlow and PyTorch. The primary functions of JAX are: grad:
automatic differentiation jit: compilation vmap: auto-vectorization
pmap: SPMD programming grad The below code demonstrates the grad
function\'s automatic differentiation. The final line should outputː jit
The below code demonstrates the jit function\'s optimization through
fusion. The computation time for jit_cube (line no.17) should be
noticeably shorter than that for cube (line no.16). Increasing the
values on line no. 7, will increase the difference. vmap The below code
demonstrates the vmap function\'s vectorization. The GIF on the right of
this section illustrates the notion of vectorized addition. pmap The
below code demonstrates the pmap function\'s parallelization for matrix
multiplication. The final line should print the valuesː Libraries using
Jax Several python libraries use Jax as a backend, including: Flax, a
high level neural network library initially developed by Google Brain.
Haiku, an object-oriented library for neural networks developed by
DeepMind. Equinox, a library that revolves around the idea of
representing parameterised functions (including neural networks) as
PyTrees. It was created by Patrick Kidger. Optax, a library for gradient
processing and optimisation developed by DeepMind. RLax, a library for
developing reinforcement learning agents developed by DeepMind. See also
NumPy TensorFlow PyTorch CUDA Automatic differentiation Just-in-time
compilation Vectorization Automatic parallelization External links
Documentationː jax.readthedocs.io Colab (Jupyter/iPython) Quickstart
Guideː
colab.research.google.com/github/google/jax/blob/main/docs/notebooks/quickstart.ipynb
TensorFlow\'s XLAː www.tensorflow.org/xla (Accelerated Linear Algebra)
Intro to JAX: Accelerating Machine Learning research on YouTube Original
paperː mlsys.org/Conferences/doc/2018/146.pdf == References ==
