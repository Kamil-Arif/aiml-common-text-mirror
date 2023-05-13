In computer science, a library is a collection of non-volatile resources
used by computer programs, often for software development. These may
include configuration data, documentation, help data, message templates,
pre-written code and subroutines, classes, values or type
specifications. In IBM\'s OS/360 and its successors they are referred to
as partitioned data sets.A library is also a collection of
implementations of behavior, written in terms of a language, that has a
well-defined interface by which the behavior is invoked. For instance,
people who want to write a higher-level program can use a library to
make system calls instead of implementing those system calls over and
over again. In addition, the behavior is provided for reuse by multiple
independent programs. A program invokes the library-provided behavior
via a mechanism of the language. For example, in a simple imperative
language such as C, the behavior in a library is invoked by using C\'s
normal function-call. What distinguishes the call as being to a library
function, versus being to another function in the same program, is the
way that the code is organized in the system.Library code is organized
in such a way that it can be used by multiple programs that have no
connection to each other, while code that is part of a program is
organized to be used only within that one program. This distinction can
gain a hierarchical notion when a program grows large, such as a
multi-million-line program. In that case, there may be internal
libraries that are reused by independent sub-portions of the large
program. The distinguishing feature is that a library is organized for
the purposes of being reused by independent programs or sub-programs,
and the user only needs to know the interface and not the internal
details of the library. The value of a library lies in the reuse of
standardized program elements. When a program invokes a library, it
gains the behavior implemented inside that library without having to
implement that behavior itself. Libraries encourage the sharing of code
in a modular fashion and ease the distribution of the code. The behavior
implemented by a library can be connected to the invoking program at
different program lifecycle phases. If the code of the library is
accessed during the build of the invoking program, then the library is
called a static library. An alternative is to build the executable of
the invoking program and distribute that, independently of the library
implementation. The library behavior is connected after the executable
has been invoked to be executed, either as part of the process of
starting the execution, or in the middle of execution. In this case the
library is called a dynamic library (loaded at runtime). A dynamic
library can be loaded and linked when preparing a program for execution,
by the linker. Alternatively, in the middle of execution, an application
may explicitly request that a module be loaded. Most compiled languages
have a standard library, although programmers can also create their own
custom libraries. Most modern software systems provide libraries that
implement the majority of the system services. Such libraries have
organized the services which a modern application requires. As such,
most code used by modern applications is provided in these system
libraries. History The idea of a computer library dates back to the
first computers created by Charles Babbage. An 1888 paper on his
Analytical Engine suggested that computer operations could be punched on
separate cards from numerical input. If these operation punch cards were
saved for reuse then \"by degrees the engine would have a library of its
own.\" In 1947 Goldstine and von Neumann speculated that it would be
useful to create a \"library\" of subroutines for their work on the IAS
machine, an early computer that was not yet operational at that time.
They envisioned a physical library of magnetic wire recordings, with
each wire storing reusable computer code.Inspired by von Neumann, Wilkes
and his team constructed EDSAC. A filing cabinet of punched tape held
the subroutine library for this computer. Programs for EDSAC consisted
of a main program and a sequence of subroutines copied from the
subroutine library. In 1951 the team published the first textbook on
programming, The Preparation of Programs for an Electronic Digital
Computer, which detailed the creation and the purpose of the
library.COBOL included \"primitive capabilities for a library system\"
in 1959, but Jean Sammet described them as \"inadequate library
facilities\" in retrospect.JOVIAL had a Communication Pool (COMPOOL),
roughly a library of header files. Another major contributor to the
modern library concept came in the form of the subprogram innovation of
FORTRAN. FORTRAN subprograms can be compiled independently of each
other, but the compiler lacked a linker. So prior to the introduction of
modules in Fortran-90, type checking between FORTRAN subprograms was
impossible.By the mid 1960s, copy and macro libraries for assemblers
were common. Starting with the popularity of the IBM System/360,
libraries containing other types of text elements, e.g., system
parameters, also became common. Simula was the first object-oriented
programming language, and its classes were nearly identical to the
modern concept as used in Java, C++, and C#. The class concept of Simula
was also a progenitor of the package in Ada and the module of Modula-2.
Even when developed originally in 1965, Simula classes could be included
in library files and added at compile time. Linking Libraries are
important in the program linking or binding process, which resolves
references known as links or symbols to library modules. The linking
process is usually automatically done by a linker or binder program that
searches a set of libraries and other modules in a given order. Usually
it is not considered an error if a link target can be found multiple
times in a given set of libraries. Linking may be done when an
executable file is created (static linking), or whenever the program is
used at runtime (dynamic linking). The references being resolved may be
addresses for jumps and other routine calls. They may be in the main
program, or in one module depending upon another. They are resolved into
fixed or relocatable addresses (from a common base) by allocating
runtime memory for the memory segments of each module referenced. Some
programming languages use a feature called smart linking whereby the
linker is aware of or integrated with the compiler, such that the linker
knows how external references are used, and code in a library that is
never actually used, even though internally referenced, can be discarded
from the compiled application. For example, a program that only uses
integers for arithmetic, or does no arithmetic operations at all, can
exclude floating-point library routines. This smart-linking feature can
lead to smaller application file sizes and reduced memory usage.
Relocation Some references in a program or library module are stored in
a relative or symbolic form which cannot be resolved until all code and
libraries are assigned final static addresses. Relocation is the process
of adjusting these references, and is done either by the linker or the
loader. In general, relocation cannot be done to individual libraries
themselves because the addresses in memory may vary depending on the
program using them and other libraries they are combined with.
Position-independent code avoids references to absolute addresses and
therefore does not require relocation. Static libraries When linking is
performed during the creation of an executable or another object file,
it is known as static linking or early binding. In this case, the
linking is usually done by a linker, but may also be done by the
compiler. A static library, also known as an archive, is one intended to
be statically linked. Originally, only static libraries existed. Static
linking must be performed when any modules are recompiled. All of the
modules required by a program are sometimes statically linked and copied
into the executable file. This process, and the resulting stand-alone
file, is known as a static build of the program. A static build may not
need any further relocation if virtual memory is used and no address
space layout randomization is desired. Shared libraries A shared library
or shared object is a file that is intended to be shared by executable
files and further shared object files. Modules used by a program are
loaded from individual shared objects into memory at load time or
runtime, rather than being copied by a linker when it creates a single
monolithic executable file for the program. Shared libraries can be
statically linked during compile-time, meaning that references to the
library modules are resolved and the modules are allocated memory when
the executable file is created. But often linking of shared libraries is
postponed until they are loaded.Most modern operating systems can have
shared library files of the same format as the executable files. This
offers two main advantages: first, it requires making only one loader
for both of them, rather than two (having the single loader is
considered well worth its added complexity). Secondly, it allows the
executables also to be used as shared libraries, if they have a symbol
table. Typical combined executable and shared library formats are ELF
and Mach-O (both in Unix) and PE (Windows). In some older environments
such as 16-bit Windows or MPE for the HP 3000, only stack-based data
(local) was allowed in shared-library code, or other significant
restrictions were placed on shared-library code. Memory sharing Library
code may be shared in memory by multiple processes, and on disk. If
virtual memory is used, processes would execute the same physical page
of RAM that is mapped into the different address spaces of the
processes. This has advantages. For instance, on the OpenStep system,
applications were often only a few hundred kilobytes in size and loaded
quickly; most of their code was located in libraries that had already
been loaded for other purposes by the operating system.Programs can
accomplish RAM sharing by using position-independent code, as in Unix,
which leads to a complex but flexible architecture, or by using common
virtual addresses, as in Windows and OS/2. These systems ensure, by
various means, like pre-mapping the address space and reserving slots
for each shared library, that code has a high probability of being
shared. A third alternative is single-level store, as used by the IBM
System/38 and its successors. This allows position-dependent code, but
places no significant restrictions on where code can be placed or how it
can be shared. In some cases, different versions of shared libraries can
cause problems, especially when libraries of different versions have the
same file name, and different applications installed on a system each
require a specific version. Such a scenario is known as DLL hell, named
after the Windows and OS/2 DLL file. Most modern operating systems after
2001 have clean-up methods to eliminate such situations or use
application-specific \"private\" libraries. Dynamic linking Dynamic
linking or late binding is linking performed while a program is being
loaded (load time) or executed (runtime), rather than when the
executable file is created. A dynamically linked library (dynamic-link
library, or DLL, under Windows and OS/2; shareable image under OpenVMS;
dynamic shared object, or DSO, under Unix-like systems) is a library
intended for dynamic linking. Only a minimal amount of work is done by
the linker when the executable file is created; it only records what
library routines the program needs and the index names or numbers of the
routines in the library. The majority of the work of linking is done at
the time the application is loaded (load time) or during execution
(runtime). Usually, the necessary linking program, called a \"dynamic
linker\" or \"linking loader\", is actually part of the underlying
operating system. (However, it is possible, and not exceedingly
difficult, to write a program that uses dynamic linking and includes its
own dynamic linker, even for an operating system that itself provides no
support for dynamic linking.) Programmers originally developed dynamic
linking in the Multics operating system, starting in 1964, and the MTS
(Michigan Terminal System), built in the late 1960s. Optimizations Since
shared libraries on most systems do not change often, systems can
compute a likely load address for each shared library on the system
before it is needed and store that information in the libraries and
executables. If every shared library that is loaded has undergone this
process, then each will load at its predetermined address, which speeds
up the process of dynamic linking. This optimization is known as
prebinding or prelinking on macOS and Linux, respectively. IBM z/VM uses
a similar technique, called \"Discontinuous Saved Segments\" (DCSS).
Disadvantages of this technique include the time required to precompute
these addresses every time the shared libraries change, the inability to
use address space layout randomization, and the requirement of
sufficient virtual address space for use (a problem that will be
alleviated by the adoption of 64-bit architectures, at least for the
time being). Locating libraries at runtime Loaders for shared libraries
vary widely in functionality. Some depend on the executable storing
explicit paths to the libraries. Any change to the library naming or
layout of the file system will cause these systems to fail. More
commonly, only the name of the library (and not the path) is stored in
the executable, with the operating system supplying a method to find the
library on disk, based on some algorithm. If a shared library that an
executable depends on is deleted, moved, or renamed, or if an
incompatible version of the library is copied to a place that is earlier
in the search, the executable would fail to load. This is called
dependency hell, existing on many platforms. The (infamous) Windows
variant is commonly known as DLL hell. This problem cannot occur if each
version of each library is uniquely identified and each program
references libraries only by their full unique identifiers. The \"DLL
hell\" problems with earlier Windows versions arose from using only the
names of libraries, which were not guaranteed to be unique, to resolve
dynamic links in programs. (To avoid \"DLL hell\", later versions of
Windows rely largely on options for programs to install private
DLLs---essentially a partial retreat from the use of shared
libraries---along with mechanisms to prevent replacement of shared
system DLLs with earlier versions of them.) Microsoft Windows Microsoft
Windows checks the registry to determine the proper place to load DLLs
that implement COM objects, but for other DLLs it will check the
directories in a defined order. First, Windows checks the directory
where it loaded the program (private DLL); any directories set by
calling the SetDllDirectory() function; the System32, System, and
Windows directories; then the current working directory; and finally the
directories specified by the PATH environment variable. Applications
written for the .NET Framework (since 2002), also check the Global
Assembly Cache as the primary store of shared dll files to remove the
issue of DLL hell. OpenStep OpenStep used a more flexible system,
collecting a list of libraries from a number of known locations (similar
to the PATH concept) when the system first starts. Moving libraries
around causes no problems at all, although users incur a time cost when
first starting the system. Unix-like systems Most Unix-like systems have
a \"search path\" specifying file-system directories in which to look
for dynamic libraries. Some systems specify the default path in a
configuration file, others hard-code it into the dynamic loader. Some
executable file formats can specify additional directories in which to
search for libraries for a particular program. This can usually be
overridden with an environment variable, although it is disabled for
setuid and setgid programs, so that a user can\'t force such a program
to run arbitrary code with root permissions. Developers of libraries are
encouraged to place their dynamic libraries in places in the default
search path. On the downside, this can make installation of new
libraries problematic, and these \"known\" locations quickly become home
to an increasing number of library files, making management more
complex. Dynamic loading Dynamic loading, a subset of dynamic linking,
involves a dynamically linked library loading and unloading at runtime
on request. Such a request may be made implicitly or explicitly.
Implicit requests are made when a compiler or static linker adds library
references that include file paths or simply file names. Explicit
requests are made when applications make direct calls to an operating
system\'s API. Most operating systems that support dynamically linked
libraries also support dynamically loading such libraries via a run-time
linker API. For instance, Microsoft Windows uses the API functions
LoadLibrary, LoadLibraryEx, FreeLibrary and GetProcAddress with
Microsoft Dynamic Link Libraries; POSIX-based systems, including most
UNIX and UNIX-like systems, use dlopen, dlclose and dlsym. Some
development systems automate this process. Object libraries Although
originally pioneered in the 1960s, dynamic linking did not reach
operating systems used by consumers until the late 1980s. It was
generally available in some form in most operating systems by the early
1990s. During this same period, object-oriented programming (OOP) was
becoming a significant part of the programming landscape. OOP with
runtime binding requires additional information that traditional
libraries don\'t supply. In addition to the names and entry points of
the code located within, they also require a list of the objects they
depend on. This is a side-effect of one of OOP\'s core concepts,
inheritance, which means that parts of the complete definition of any
method may be in different places. This is more than simply listing that
one library requires the services of another: in a true OOP system, the
libraries themselves may not be known at compile time, and vary from
system to system. At the same time many developers worked on the idea of
multi-tier programs, in which a \"display\" running on a desktop
computer would use the services of a mainframe or minicomputer for data
storage or processing. For instance, a program on a GUI-based computer
would send messages to a minicomputer to return small samples of a huge
dataset for display. Remote procedure calls (RPC) already handled these
tasks, but there was no standard RPC system. Soon the majority of the
minicomputer and mainframe vendors instigated projects to combine the
two, producing an OOP library format that could be used anywhere. Such
systems were known as object libraries, or distributed objects, if they
supported remote access (not all did). Microsoft\'s COM is an example of
such a system for local use. DCOM, a modified version of COM, supports
remote access. For some time object libraries held the status of the
\"next big thing\" in the programming world. There were a number of
efforts to create systems that would run across platforms, and companies
competed to try to get developers locked into their own system. Examples
include IBM\'s System Object Model (SOM/DSOM), Sun Microsystems\'
Distributed Objects Everywhere (DOE), NeXT\'s Portable Distributed
Objects (PDO), Digital\'s ObjectBroker, Microsoft\'s Component Object
Model (COM/DCOM), and any number of CORBA-based systems. Class libraries
Class libraries are the rough OOP equivalent of older types of code
libraries. They contain classes, which describe characteristics and
define actions (methods) that involve objects. Class libraries are used
to create instances, or objects with their characteristics set to
specific values. In some OOP languages, like Java, the distinction is
clear, with the classes often contained in library files (like Java\'s
JAR file format) and the instantiated objects residing only in memory
(although potentially able to be made persistent in separate files). In
others, like Smalltalk, the class libraries are merely the starting
point for a system image that includes the entire state of the
environment, classes and all instantiated objects. Today most class
libraries are stored in a package repository (such as Maven Central for
Java). Client code explicitly declare the dependencies to external
libraries in build configuration files (such as a Maven Pom in Java).
Remote libraries Another library technique uses completely separate
executables (often in some lightweight form) and calls them using a
remote procedure call (RPC) over a network to another computer. This
maximizes operating system re-use: the code needed to support the
library is the same code being used to provide application support and
security for every other program. Additionally, such systems do not
require the library to exist on the same machine, but can forward the
requests over the network. However, such an approach means that every
library call requires a considerable amount of overhead. RPC calls are
much more expensive than calling a shared library that has already been
loaded on the same machine. This approach is commonly used in a
distributed architecture that makes heavy use of such remote calls,
notably client-server systems and application servers such as Enterprise
JavaBeans. Code generation libraries Code generation libraries are
high-level APIs that can generate or transform byte code for Java. They
are used by aspect-oriented programming, some data access frameworks,
and for testing to generate dynamic proxy objects. They also are used to
intercept field access. File naming Most modern Unix-like systems The
system stores libfoo.a and libfoo.so files in directories such as /lib,
/usr/lib or /usr/local/lib. The filenames always start with lib, and end
with a suffix of .a (archive, static library) or of .so (shared object,
dynamically linked library). Some systems might have multiple names for
a dynamically linked library. These names typically share the same
prefix and have different suffixes indicating the version number. Most
of the names are names for symbolic links to the latest version. For
example, on some systems libfoo.so.2 would be the filename for the
second major interface revision of the dynamically linked library
libfoo. The .la files sometimes found in the library directories are
libtool archives, not usable by the system as such. macOS The system
inherits static library conventions from BSD, with the library stored in
a .a file, and can use .so-style dynamically linked libraries (with the
.dylib suffix instead). Most libraries in macOS, however, consist of
\"frameworks\", placed inside special directories called \"bundles\"
which wrap the library\'s required files and metadata. For example, a
framework called MyFramework would be implemented in a bundle called
MyFramework.framework, with MyFramework.framework/MyFramework being
either the dynamically linked library file or being a symlink to the
dynamically linked library file in
MyFramework.framework/Versions/Current/MyFramework. Microsoft Windows
Dynamic-link libraries usually have the suffix \*.DLL, although other
file name extensions may identify specific-purpose dynamically linked
libraries, e.g. \*.OCX for OLE libraries. The interface revisions are
either encoded in the file names, or abstracted away using COM-object
interfaces. Depending on how they are compiled, \*.LIB files can be
either static libraries or representations of dynamically linkable
libraries needed only during compilation, known as \"import libraries\".
Unlike in the UNIX world, which uses different file extensions, when
linking against .LIB file in Windows one must first know if it is a
regular static library or an import library. In the latter case, a .DLL
file must be present at runtime. See also Code reuse -- Use of existing
software to build new software Linker (computing) -- Computer program
which combines multiple object files into a single file Loader
(computing) -- Part of an operating system Dynamic-link library --
Microsoft\'s implementation of the shared library concept in Windows and
OS/2 Object file -- File containing relocatable format machine code
Plug-in -- Software component that adds a specific feature to an
existing software application Prelink, also known as Prebinding Static
library -- set of routines, external functions and variables in computer
sciencePages displaying wikidata descriptions as a fallback Runtime
library -- set of routines that can be invoked by a compiled software
binary during its executionPages displaying wikidata descriptions as a
fallback Visual Component Library -- Visual Library (VCL) Component
Library for Cross Platform (CLX) C standard library -- Standard library
for the C programming language Java Class Library Framework Class
Library -- Standard library of Microsoft\'s .NET Framework Generic
programming -- Style of computer programming (used by the C++ Standard
Library) soname -- Field of data in a shared object file Method stub --
term in programmingPages displaying wikidata descriptions as a fallback
Notes References Further reading Levine, John R. (2000) \[October
1999\]. \"Chapter 9: Shared Libraries & Chapter 10: Dynamic Linking and
Loading\". Linkers and Loaders. The Morgan Kaufmann Series in Software
Engineering and Programming (1 ed.). San Francisco, USA: Morgan
Kaufmann. ISBN 1-55860-496-0. OCLC 42413382. Archived from the original
on 2012-12-05. Retrieved 2020-01-12. Code: \[1\]\[2\] Errata: \[3\]
Article Beginner\'s Guide to Linkers by David Drysdale Article Faster
C++ program startups by improving runtime linking efficiency by Léon
Bottou and John Ryland How to Create Program Libraries by Baris Simsek
BFD - the Binary File Descriptor Library 1st Library-Centric Software
Design Workshop LCSD\'05 Archived 2019-08-28 at the Wayback Machine at
OOPSLA\'05 2nd Library-Centric Software Design Workshop LCSD\'06 at
OOPSLA\'06 How to create shared library by Ulrich Drepper (with much
background info) Anatomy of Linux dynamic libraries at IBM.com
