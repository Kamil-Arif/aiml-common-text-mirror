Approximate computing is an emerging paradigm for energy-efficient
and/or high-performance design. It includes a plethora of computation
techniques that return a possibly inaccurate result rather than a
guaranteed accurate result, and that can be used for applications where
an approximate result is sufficient for its purpose. One example of such
situation is for a search engine where no exact answer may exist for a
certain search query and hence, many answers may be acceptable.
Similarly, occasional dropping of some frames in a video application can
go undetected due to perceptual limitations of humans. Approximate
computing is based on the observation that in many scenarios, although
performing exact computation requires large amount of resources,
allowing bounded approximation can provide disproportionate gains in
performance and energy, while still achieving acceptable result
accuracy. For example, in k-means clustering algorithm, allowing only 5%
loss in classification accuracy can provide 50 times energy saving
compared to the fully accurate classification. The key requirement in
approximate computing is that approximation can be introduced only in
non-critical data, since approximating critical data (e.g., control
operations) can lead to disastrous consequences, such as program crash
or erroneous output. Strategies Several strategies can be used for
performing approximate computing. Approximate circuits Approximate
arithmetic circuits: adders, multipliers and other logical circuits can
reduce hardware overhead. For example, an approximate multi-bit adder
can ignore the carry chain and thus, allow all its sub-adders to perform
addition operation in parallel. Approximate storage and memory Instead
of storing data values exactly, they can be stored approximately, e.g.,
by truncating the lower-bits in floating point data. Another method is
to accept less reliable memory. For this, in DRAM and eDRAM, refresh
rate assignments can be lowered or controlled. In SRAM, supply voltage
can be lowered or controlled. Approximate storage can be applied to
reduce MRAM\'s high write energy consumption. In general, any error
detection and correction mechanisms should be disabled. Software-level
approximation There are several ways to approximate at software level.
Memoization can be applied. Some iterations of loops can be skipped
(termed as loop perforation) to achieve a result faster. Some tasks can
also be skipped, for example when a run-time condition suggests that
those tasks are not going to be useful (task skipping). Monte Carlo
algorithms and Randomized algorithms trade correctness for execution
time guarantees. The computation can be reformulated according to
paradigms that allow easily the acceleration on specialized hardware,
e.g. a neural processing unit. Approximate system In an approximate
system, different subsystems of the system such as the processor,
memory, sensor, and communication modules are synergistically
approximated to obtain a much better system-level Q-E trade-off curve
compared to individual approximations to each of the subsystems.
Application areas Approximate computing has been used in a variety of
domains where the applications are error-tolerant, such as multimedia
processing, machine learning, signal processing, scientific computing.
Therefore, approximate computing is mostly driven by applications that
are related to human perception/cognition and have inherent error
resilience. Many of these applications are based on statistical or
probabilistic computation, such as different approximations can be made
to better suit the desired objectives. One notable application in
machine learning is that Google is using this approach in their Tensor
processing units (TPU, a custom ASIC). Derived paradigms The main issue
in approximate computing is the identification of the section of the
application that can be approximated. In the case of large scale
applications, it is very common to find people holding the expertise on
approximate computing techniques not having enough expertise on the
application domain (and vice versa). In order to solve this problem,
programming paradigms have been proposed. They all have in common the
clear role separation between application programmer and application
domain expert. These approaches allow the spread of the most common
optimizations and approximate computing techniques. See also Artificial
neural network Metaheuristic PCMOS == References ==
