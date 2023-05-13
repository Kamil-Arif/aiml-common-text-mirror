ROOT is an object-oriented computer program and library developed by
CERN. It was originally designed for particle physics data analysis and
contains several features specific to the field, but it is also used in
other applications such as astronomy and data mining. The latest minor
release is 6.28, as of 2023-02-03. Description CERN maintained the CERN
Program Library written in FORTRAN for many years. Its development and
maintenance were discontinued in 2003 in favour of ROOT, which is
written in the C++ programming language. ROOT development was initiated
by René Brun and Fons Rademakers in 1994. Some parts are published under
the GNU Lesser General Public License (LGPL) and others are based on GNU
General Public License (GPL) software, and are thus also published under
the terms of the GPL. It provides platform independent access to a
computer\'s graphics subsystem and operating system using abstract
layers. Parts of the abstract platform are: a graphical user interface
and a GUI builder, container classes, reflection, a C++ script and
command line interpreter (CINT in version 5, cling in version 6), object
serialization and persistence. The packages provided by ROOT include
those for Histogramming and graphing to view and analyze distributions
and functions, curve fitting (regression analysis) and minimization of
functionals, statistics tools used for data analysis, matrix algebra,
four-vector computations, as used in high energy physics, standard
mathematical functions, multivariate data analysis, e.g. using neural
networks, image manipulation, used, for instance, to analyze
astronomical pictures, access to distributed data (in the context of the
Grid), distributed computing, to parallelize data analyses, persistence
and serialization of objects, which can cope with changes in class
definitions of persistent data, access to databases, 3D visualizations
(geometry), creating files in various graphics formats, like PDF,
PostScript, PNG, SVG, LaTeX, etc. interfacing Python code in both
directions, interfacing Monte Carlo event generators. A key feature of
ROOT is a data container called tree, with its substructures branches
and leaves. A tree can be seen as a sliding window to the raw data, as
stored in a file. Data from the next entry in the file can be retrieved
by advancing the index in the tree. This avoids memory allocation
problems associated with object creation, and allows the tree to act as
a lightweight container while handling buffering invisibly. ROOT is
designed for high computing efficiency, as it is required to process
data from the Large Hadron Collider\'s experiments estimated at several
petabytes per year. As of 2009 ROOT is mainly used in data analysis and
data acquisition in particle physics (high energy physics) experiments,
and most current experimental plots and results in those subfields are
obtained using ROOT. The inclusion of a C++ interpreter (CINT until
version 5.34, Cling from version 6.00) makes this package very versatile
as it can be used in interactive, scripted and compiled modes in a
manner similar to commercial products like MATLAB. On July 4, 2012 the
ATLAS and CMS LHC\'s experiments presented the status of the Standard
Model Higgs search. All data plotting presented that day used ROOT.
Applications Several particle physics collaborations have written
software based on ROOT, often in favor of using more generic solutions
(e.g. using ROOT containers instead of STL). Some of the running
particle physics experiments using software based on ROOT ALICE ATLAS
BaBar experiment Belle Experiment (an electron positron collider at KEK
(Japan)) Belle II experiment (successor of the Belle experiment) BES III
CB-ELSA/TAPS CMS COMPASS experiment (Common Muon and Proton Apparatus
for Structure and Spectroscopy) CUORE (Cryogenic Underground Observatory
for Rare Events) D0 experiment GlueX Experiment GRAPES-3 (Gamma Ray
Astronomy PeV EnergieS) H1 (particle detector) at HERA collider at DESY,
Hamburg LHCb MINERνA (Main Injector Experiment for ν-A) MINOS (Main
injector neutrino oscillation search) NA61 experiment (SPS Heavy Ion and
Neutrino Experiment) NOνA OPERA experiment PHENIX detector PHOBOS
experiment at Relativistic Heavy Ion Collider SNO+ STAR detector
(Solenoidal Tracker at RHIC) T2K experiment Future particle physics
experiments currently developing software based on ROOT Mu2e Compressed
Baryonic Matter experiment (CBM) PANDA experiment (antiProton
Annihilation at Darmstadt (PANDA)) Deep Underground Neutrino Experiment
(DUNE) Hyper-Kamiokande (HK (Japan)) Astrophysics (X-ray and gamma-ray
astronomy, astroparticle physics) projects using ROOT AGILE Alpha
Magnetic Spectrometer (AMS) Antarctic Impulse Transient Antenna (ANITA)
ANTARES neutrino detector CRESST (Dark Matter Search) DMTPC
DEAP-3600/Cryogenic Low-Energy Astrophysics with Neon(CLEAN) Fermi
Gamma-ray Space Telescope ICECUBE HAWC High Energy Stereoscopic System
(H.E.S.S.) Hitomi (ASTRO-H) MAGIC Milagro Pierre Auger Observatory
VERITAS PAMELA POLAR PoGOLite Computational Neuroscience projects using
ROOT The MIIND Project Home Page Criticisms Criticisms of ROOT include
its difficulty for beginners, as well as various aspects of its design
and implementation. Frequent causes of frustration include extreme code
bloat, heavy use of global variables, and an overcomplicated class
hierarchy. From time to time these issues are discussed on the ROOT
users mailing list. While scientists dissatisfied with ROOT have in the
past managed to work around its flaws, some of the shortcomings are
regularly addressed by the ROOT team. The CINT interpreter, for example,
has been replaced by the Cling interpreter, and numerous bugs are fixed
with every release. See also Matplotlib -- a plotting and analysis
system for Python SciPy -- a scientific data analysis system for Python,
based on the NumPy classes Perl Data Language -- a set of array
programming extensions to the Perl programming language HippoDraw -- an
alternative C++-based data analysis system Java Analysis Studio -- a
Java-based AIDA-compliant data analysis system R programming language
AIDA (computing) -- open interfaces and formats for particle physics
data processing Geant4 -- a platform for the simulation of the passage
of particles through matter using Monte Carlo methods PAW IGOR Pro
Scientific Linux Scientific computing OpenDX OpenScientist CERN Program
Library -- legacy program library written in Fortran77, still available
but not updated References External links The ROOT System Home Page
Image galleries ROOT User\'s Guide ROOT Reference Guide ROOT Forum The
RooFit Toolkit for Data Modeling, an extension to ROOT to facilitate
maximum likelihood fits The Toolkit for Multivariate Data Analysis with
ROOT (TMVA) is a ROOT-integrated project providing a machine learning
environment for the processing and evaluation of multivariate
classification, both binary and multi class, and regression techniques
targeting applications in high-energy physics (here or here).
