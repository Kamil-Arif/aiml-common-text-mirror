Computer security compromised by hardware failure is a branch of
computer security applied to hardware. The objective of computer
security includes protection of information and property from theft,
corruption, or natural disaster, while allowing the information and
property to remain accessible and productive to its intended users. Such
secret information could be retrieved by different ways. This article
focus on the retrieval of data thanks to misused hardware or hardware
failure. Hardware could be misused or exploited to get secret data. This
article collects main types of attack that can lead to data theft.
Computer security can be comprised by devices, such as keyboards,
monitors or printers (thanks to electromagnetic or acoustic emanation
for example) or by components of the computer, such as the memory, the
network card or the processor (thanks to time or temperature analysis
for example). Devices Monitor The monitor is the main device used to
access data on a computer. It has been shown that monitors radiate or
reflect data on their environment, potentially giving attackers access
to information displayed on the monitor. Electromagnetic emanations
Video display units radiate: narrowband harmonics of the digital clock
signals ; broadband harmonics of the various \'random\' digital signals
such as the video signal.Known as compromising emanations or TEMPEST
radiation, a code word for a U.S. government programme aimed at
attacking the problem, the electromagnetic broadcast of data has been a
significant concern in sensitive computer applications. Eavesdroppers
can reconstruct video screen content from radio frequency emanations.
Each (radiated) harmonic of the video signal shows a remarkable
resemblance to a broadcast TV signal. It is therefore possible to
reconstruct the picture displayed on the video display unit from the
radiated emission by means of a normal television receiver. If no
preventive measures are taken, eavesdropping on a video display unit is
possible at distances up to several hundreds of meters, using only a
normal black-and-white TV receiver, a directional antenna and an antenna
amplifier. It is even possible to pick up information from some types of
video display units at a distance of over 1 kilometer. If more
sophisticated receiving and decoding equipment is used, the maximum
distance can be much greater. Compromising reflections What is displayed
by the monitor is reflected on the environment. The time-varying diffuse
reflections of the light emitted by a CRT monitor can be exploited to
recover the original monitor image. This is an eavesdropping technique
for spying at a distance on data that is displayed on an arbitrary
computer screen, including the currently prevalent LCD monitors. The
technique exploits reflections of the screen\'s optical emanations in
various objects that one commonly finds in close proximity to the screen
and uses those reflections to recover the original screen content. Such
objects include eyeglasses, tea pots, spoons, plastic bottles, and even
the eye of the user. This attack can be successfully mounted to spy on
even small fonts using inexpensive, off-the-shelf equipment (less than
1500 dollars) from a distance of up to 10 meters. Relying on more
expensive equipment allowed to conduct this attack from over 30 meters
away, demonstrating that similar attacks are feasible from the other
side of the street or from a close by building.Many objects that may be
found at a usual workplace can be exploited to retrieve information on a
computer\'s display by an outsider. Particularly good results were
obtained from reflections in a user\'s eyeglasses or a tea pot located
on the desk next to the screen. Reflections that stem from the eye of
the user also provide good results. However, eyes are harder to spy on
at a distance because they are fast-moving objects and require high
exposure times. Using more expensive equipment with lower exposure times
helps to remedy this problem.The reflections gathered from curved
surfaces on close by objects indeed pose a substantial threat to the
confidentiality of data displayed on the screen. Fully invalidating this
threat without at the same time hiding the screen from the legitimate
user seems difficult, without using curtains on the windows or similar
forms of strong optical shielding. Most users, however, will not be
aware of this risk and may not be willing to close the curtains on a
nice day. The reflection of an object, a computer display, in a curved
mirror creates a virtual image that is located behind the reflecting
surface. For a flat mirror this virtual image has the same size and is
located behind the mirror at the same distance as the original object.
For curved mirrors, however, the situation is more complex. Keyboard
Electromagnetic emanations Computer keyboards are often used to transmit
confidential data such as passwords. Since they contain electronic
components, keyboards emit electromagnetic waves. These emanations could
reveal sensitive information such as keystrokes. Electromagnetic
emanations have turned out to constitute a security threat to computer
equipment. The figure below presents how a keystroke is retrieved and
what material is necessary. The approach is to acquire the raw signal
directly from the antenna and to process the entire captured
electromagnetic spectrum. Thanks to this method, four different kinds of
compromising electromagnetic emanations have been detected, generated by
wired and wireless keyboards. These emissions lead to a full or a
partial recovery of the keystrokes. The best practical attack fully
recovered 95% of the keystrokes of a PS/2 keyboard at a distance up to
20 meters, even through walls. Because each keyboard has a specific
fingerprint based on the clock frequency inconsistencies, it can
determine the source keyboard of a compromising emanation, even if
multiple keyboards from the same model are used at the same time.The
four different kinds way of compromising electromagnetic emanations are
described below. The Falling Edge Transition Technique When a key is
pressed, released or held down, the keyboard sends a packet of
information known as a scan code to the computer. The protocol used to
transmit these scan codes is a bidirectional serial communication, based
on four wires: Vcc (5 volts), ground, data and clock. Clock and data
signals are identically generated. Hence, the compromising emanation
detected is the combination of both signals. However, the edges of the
data and the clock lines are not superposed. Thus, they can be easily
separated to obtain independent signals. The Generalized Transition
Technique The Falling Edge Transition attack is limited to a partial
recovery of the keystrokes. This is a significant limitation. The GTT is
a falling edge transition attack improved, which recover almost all
keystrokes. Indeed, between two traces, there is exactly one data rising
edge. If attackers are able to detect this transition, they can fully
recover the keystrokes. The Modulation Technique Harmonics compromising
electromagnetic emissions come from unintentional emanations such as
radiations emitted by the clock, non-linear elements, crosstalk, ground
pollution, etc. Determining theoretically the reasons of these
compromising radiations is a very complex task. These harmonics
correspond to a carrier of approximately 4 MHz which is very likely the
internal clock of the micro-controller inside the keyboard. These
harmonics are correlated with both clock and data signals, which
describe modulated signals (in amplitude and frequency) and the full
state of both clock and data signals. This means that the scan code can
be completely recovered from these harmonics. The Matrix Scan Technique
Keyboard manufacturers arrange the keys in a matrix. The keyboard
controller, often an 8-bit processor, parses columns one-by-one and
recovers the state of 8 keys at once. This matrix scan process can be
described as 192 keys (some keys may not be used, for instance modern
keyboards use 104/105 keys) arranged in 24 columns and 8 rows. These
columns are continuously pulsed one-by-one for at least 3μs. Thus, these
leads may act as an antenna and generate electromagnetic emanations. If
an attacker is able to capture these emanations, he can easily recover
the column of the pressed key. Even if this signal does not fully
describe the pressed key, it still gives partial information on the
transmitted scan code, i.e. the column number.Note that the matrix scan
routine loops continuously. When no key is pressed, we still have a
signal composed of multiple equidistant peaks. These emanations may be
used to remotely detect the presence of powered computers. Concerning
wireless keyboards, the wireless data burst transmission can be used as
an electromagnetic trigger to detect exactly when a key is pressed,
while the matrix scan emanations are used to determine the column it
belongs to. Summary Some techniques can only target some keyboards. This
table sums up which technique could be used to find keystroke for
different kind of keyboard. In their paper called \"Compromising
Electromagnetic Emanations of Wired and Wireless Keyboards\", Martin
Vuagnoux and Sylvain Pasini tested 12 different keyboard models, with
PS/2, USB connectors and wireless communication in different setups: a
semi-anechoic chamber, a small office, an adjacent office and a flat in
a building. The table below presents their results. Acoustic emanations
Attacks against emanations caused by human typing have attracted
interest in recent years. In particular, works showed that keyboard
acoustic emanations do leak information that can be exploited to
reconstruct the typed text.PC keyboards, notebook keyboards are
vulnerable to attacks based on differentiating the sound emanated by
different keys. This attack takes as input an audio signal containing a
recording of a single word typed by a single person on a keyboard, and a
dictionary of words. It is assumed that the typed word is present in the
dictionary. The aim of the attack is to reconstruct the original word
from the signal. This attack, taking as input a 10-minute sound
recording of a user typing English text using a keyboard, and then
recovering up to 96% of typed characters. This attack is inexpensive
because the other hardware required is a parabolic microphone and
non-invasive because it does not require physical intrusion into the
system. The attack employs a neural network to recognize the key being
pressed. It combines signal processing and efficient data structures and
algorithms, to successfully reconstruct single words of 7-13 characters
from a recording of the clicks made when typing them on a keyboard. The
sound of clicks can differ slightly from key to key, because the keys
are positioned at different positions on the keyboard plate, although
the clicks of different keys sound similar to the human ear.On average,
there were only 0.5 incorrect recognitions per 20 clicks, which shows
the exposure of keyboard to the eavesdropping using this attack. The
attack is very efficient, taking under 20 seconds per word on a standard
PC. A 90% or better success rate of finding the correct word for words
of 10 or more characters, and a success rate of 73% over all the words
tested. In practice, a human attacker can typically determine if text is
random. An attacker can also identify occasions when the user types user
names and passwords. Short audio signals containing a single word, with
seven or more characters long was considered. This means that the signal
is only a few seconds long. Such short words are often chosen as a
password. The dominant factors affecting the attack\'s success are the
word length, and more importantly, the number of repeated characters
within the word.This is a procedure that makes it possible to
efficiently uncover a word out of audio recordings of keyboard click
sounds. More recently, extracting information out of another type of
emanations was demonstrated: acoustic emanations from mechanical devices
such as dot-matrix printers. Video Eavesdropping on Keyboard While
extracting private information by watching somebody typing on a keyboard
might seem to be an easy task, it becomes extremely challenging if it
has to be automated. However, an automated tool is needed in the case of
long-lasting surveillance procedures or long user activity, as a human
being is able to reconstruct only a few characters per minute. The paper
\"ClearShot: Eavesdropping on Keyboard Input from Video\" presents a
novel approach to automatically recovering the text being typed on a
keyboard, based solely on a video of the user typing.Automatically
recognizing the keys being pressed by a user is a hard problem that
requires sophisticated motion analysis. Experiments show that, for a
human, reconstructing a few sentences requires lengthy hours of
slow-motion analysis of the video. The attacker might install a
surveillance device in the room of the victim, might take control of an
existing camera by exploiting a vulnerability in the camera\'s control
software, or might simply point a mobile phone with an integrated camera
at the laptop\'s keyboard when the victim is working in a public
space.Balzarotti\'s analysis is divided into two main phases (figure
below). The first phase analyzes the video recorded by the camera using
computer vision techniques. For each frame of the video, the computer
vision analysis computes the set of keys that were likely pressed, the
set of keys that were certainly not pressed, and the position of space
characters. Because the results of this phase of the analysis are noisy,
a second phase, called the text analysis, is required. The goal of this
phase is to remove errors using both language and context-sensitive
techniques. The result of this phase is the reconstructed text, where
each word is represented by a list of possible candidates, ranked by
likelihood. Printer Acoustic emanations With acoustic emanations, an
attack that recovers what a dot-matrix printer processing English text
is printing is possible. It is based on a record of the sound the
printer makes, if the microphone is close enough to it. This attack
recovers up to 72% of printed words, and up to 95% if knowledge about
the text are done, with a microphone at a distance of 10 cm from the
printer.After an upfront training phase (\"a\" in the picture below),
the attack (\"b\" in the picture below) is fully automated and uses a
combination of machine learning, audio processing, and speech
recognition techniques, including spectrum features, Hidden Markov
Models and linear classification. The fundamental reason why the
reconstruction of the printed text works is that, the emitted sound
becomes louder if more needles strike the paper at a given time. There
is a correlation between the number of needles and the intensity of the
acoustic emanation.A training phase was conducted where words from a
dictionary are printed and characteristic sound features of these words
are extracted and stored in a database. The trained characteristic
features was used to recognize the printed English text. But, this task
is not trivial. Major challenges include : Identifying and extracting
sound features that suitably capture the acoustic emanation of
dot-matrix printers; Compensating for the blurred and overlapping
features that are induced by the substantial decay time of the
emanations; Identifying and eliminating wrongly recognized words to
increase the overall percentage of correctly identified words
(recognition rate). Computer components Network Interface Card Timing
attack Timing attacks enable an attacker to extract secrets maintained
in a security system by observing the time it takes the system to
respond to various queries.SSH is designed to provide a secure channel
between two hosts. Despite the encryption and authentication mechanisms
it uses, SSH has weaknesses. In interactive mode, every individual
keystroke that a user types is sent to the remote machine in a separate
IP packet immediately after the key is pressed, which leaks the
inter-keystroke timing information of users' typing. Below, the picture
represents the command su processed through a SSH connection. A very
simple statistical techniques suffice to reveal sensitive information
such as the length of users' passwords or even root passwords. By using
advanced statistical techniques on timing information collected from the
network, the eavesdropper can learn significant information about what
users type in SSH sessions. Because the time it takes the operating
system to send out the packet after the keypress is in general
negligible comparing to the interkeystroke timing, this also enables an
eavesdropper to learn the precise interkeystroke timings of users'
typing from the arrival times of packets. Memory Physical chemistry Data
remanence problems not only affect obvious areas such as RAM and
non-volatile memory cells but can also occur in other areas of the
device through hot-carrier effects (which change the characteristics of
the semiconductors in the device) and various other effects which are
examined alongside the more obvious memory-cell remanence problems. It
is possible to analyse and recover data from these cells and from
semiconductor devices in general long after it should (in theory) have
vanished.Electromigration, which means to physically move the atom to
new locations (to physically alter the device itself) is another type of
attack. It involves the relocation of metal atoms due to high current
densities, a phenomenon in which atoms are carried along by an
\"electron wind\" in the opposite direction to the conventional current,
producing voids at the negative electrode and hillocks and whiskers at
the positive electrode. Void formation leads to a local increase in
current density and Joule heating (the interaction of electrons and
metal ions to produce thermal energy), producing further
electromigration effects. When the external stress is removed, the
disturbed system tends to relax back to its original equilibrium state,
resulting in a backflow which heals some of the electromigration damage.
In the long term though, this can cause device failure, but in less
extreme cases it simply serves to alter a device\'s operating
characteristics in noticeable ways. For example, the excavations of
voids leads to increased wiring resistance and the growth of whiskers
leads to contact formation and current leakage. An example of a
conductor which exhibits whisker growth due to electromigration is shown
in the figure below: One example which exhibits void formation (in this
case severe enough to have led to complete failure) is shown in this
figure: Temperature Contrary to popular assumption, DRAMs used in most
modern computers retain their contents for several seconds after power
is lost, even at room temperature and even if removed from a
motherboard.Many products do cryptographic and other security-related
computations using secret keys or other variables that the equipment\'s
operator must not be able to read out or alter. The usual solution is
for the secret data to be kept in volatile memory inside a
tamper-sensing enclosure. Security processors typically store secret key
material in static RAM, from which power is removed if the device is
tampered with. At temperatures below −20 °C, the contents of SRAM can be
'frozen'. It is interesting to know the period of time for which a
static RAM device will retain data once the power has been removed. Low
temperatures can increase the data retention time of SRAM to many
seconds or even minutes. Read/Write exploits thanks to FireWire
Maximillian Dornseif presented a technique in these slides, which let
him take the control of an Apple computer thanks to an iPod. The attacks
needed a first generic phase where the iPod software was modified so
that it behaves as master on the FireWire bus. Then the iPod had full
read/write access on the Apple Computer when the iPod was plugged into a
FireWire port. FireWire is used by : audio devices, printers, scanners,
cameras, gps, etc. Generally, a device connected by FireWire has full
access (read/write). Indeed, OHCI Standard (FireWire standard) reads :
Physical requests, including physical read, physical write and lock
requests to some CSR registers (section 5.5), are handled directly by
the Host Controller without assistance by system software. So, any
device connected by FireWire can read and write data on the computer
memory. For example, a device can : Grab the screen contents ; Just
search the memory for strings such as login, passwords ; Scan for
possible key material ; Search cryptographic keys stored in RAM ; Parse
the whole physical memory to understand logical memory layout.or Mess up
the memory ; Change screen content ; Change UID/GID of a certain process
; Inject code into a process ; Inject an additional process. Processor
Cache attack To increase the computational power, processors are
generally equipped with a cache memory which decreases the memory access
latency. Below, the figure shows the hierarchy between the processor and
the memory. First the processor looks for data in the cache L1, then L2,
then in the memory. When the data is not where the processor is looking
for, it is called a cache-miss. Below, pictures show how the processor
fetch data when there are two cache levels. Unfortunately caches contain
only a small portion of the application data and can introduce
additional latency to the memory transaction in the case of a miss. This
involves also additional power consumption which is due to the
activation of memory devices down in the memory hierarchy. The miss
penalty has been already used to attack symmetric encryption algorithms,
like DES. The basic idea proposed in this paper is to force a cache miss
while the processor is executing the AES encryption algorithm on a known
plain text. The attacks allow an unprivileged process to attack other
process running in parallel on the same processor, despite partitioning
methods such as memory protection, sandboxing and virtualization. Timing
attack By carefully measuring the amount of time required to perform
private key operations, attackers may be able to find fixed
Diffie-Hellman exponents, factor RSA keys, and break other
cryptosystems. Against a vulnerable system, the attack is
computationally inexpensive and often requires only known ciphertext.
The attack can be treated as a signal detection problem. The signal
consists of the timing variation due to the target exponent bit, and
noise results from measurement inaccuracies and timing variations due to
unknown exponent bits. The properties of the signal and noise determine
the number of timing measurements required to for the attack. Timing
attacks can potentially be used against other cryptosystems, including
symmetric functions. Privilege escalation A simple and generic processor
backdoor can be used by attackers as a means to privilege escalation to
get to privileges equivalent to those of any given running operating
system. Also, a non-privileged process of one of the non-privileged
invited domain running on top of a virtual machine monitor can get to
privileges equivalent to those of the virtual machine monitor.Loïc
Duflot studied Intel processors in the paper \"CPU bugs, CPU backdoors
and consequences on security\" ; he explains that the processor defines
four different privilege rings numbered from 0 (most privileged) to 3
(least privileged). Kernel code is usually running in ring 0, whereas
user-space code is generally running in ring 3. The use of some
security-critical assembly language instructions is restricted to ring 0
code. In order to escalate privilege through the backdoor, the attacker
must : activate the backdoor by placing the CPU in the desired state ;
inject code and run it in ring 0 ; get back to ring 3 in order to return
the system to a stable state. Indeed, when code is running in ring 0,
system calls do not work : Leaving the system in ring 0 and running a
random system call (exit() typically) is likely to crash the system.The
backdoors Loïc Duflot presents are simple as they only modify the
behavior of three assembly language instructions and have very simple
and specific activation conditions, so that they are very unlikely to be
accidentally activated. Recent inventions have begun to target these
types of processor-based escalation attacks. References Bibliography
Acoustic Asonov, D.; Agrawal, R. (2004). \"Keyboard acoustic
emanations\". IEEE Symposium on Security and Privacy, 2004. Proceedings.
2004. Proceedings 2004 IEEE Symposium on Security and Privacy. pp.
3--11. CiteSeerX 10.1.1.89.8231. doi:10.1109/SECPRI.2004.1301311. ISBN
978-0-7695-2136-7. ISSN 1081-6011. S2CID 216795. Zhuang, Li; Zhou, Feng;
Tygar, J.D. (2005). \"Keyboard acoustic emanations revisited\". ACM
Transactions on Information and System Security (TISSEC). Proceedings of
the 12th ACM Conference on Computer and Communications Security. ACM
Transactions on Information Systems. Vol. 13, no. 1. Alexandria,
Virginia, USA: ACM New York, NY, USA. pp. 373--382. CiteSeerX
10.1.1.117.5791. doi:10.1145/1609956.1609959. ISBN 978-1-59593-226-6.
ISSN 1094-9224. Berger, Yigael; Wool, Avishai; Yeredor, Arie (2006).
\"Dictionary attacks using keyboard acoustic emanations\". Proceedings
of the 13th ACM conference on Computer and communications security --
CCS \'06. Proceedings of the 13th ACM Conference on Computer and
Communications Security. Alexandria, Virginia, USA: ACM New York, NY,
USA. pp. 245--254. CiteSeerX 10.1.1.99.8028.
doi:10.1145/1180405.1180436. ISBN 978-1-59593-518-2. S2CID 2596394.
Backes, Michael; Dürmuth, Markus; Gerling, Sebastian; Pinkal, Manfred;
Sporleder, Caroline (2010), \"Acoustic Side-Channel Attacks on
Printers\" (PDF), Proceedings of the 19th USENIX Security Symposium,
Washington, DC, ISBN 978-1-931971-77-5 Cache attack Osvik, Dag Arne;
Shamir, Adi; Tromer, Eran (2006). \"Cache Attacks and Countermeasures:
The Case of AES\". Topics in Cryptology -- CT-RSA 2006. Topics in
Cryptology CT-RSA. Lecture Notes in Computer Science. Vol. 3860. San
Jose, California, USA: Springer-Verlag Berlin, Heidelberg. pp. 1--20.
CiteSeerX 10.1.1.60.1857. doi:10.1007/11605805_1. ISBN
978-3-540-31033-4. ISSN 0302-9743. Page, Daniel (2005), \"Partitioned
cache architecture as a side-channel defence mechanism\" (PDF),
Cryptology ePrint Archive Bertoni, Guido; Zaccaria, Vittorio;
Breveglieri, Luca; Monchiero, Matteo; Palermo, Gianluca (2005). \"AES
power attack based on induced cache miss and countermeasure\" (PDF).
International Conference on Information Technology: Coding and Computing
(ITCC\'05) -- Volume II. International Conference on Information
Technology: Coding and Computing (ITCC\'05). Vol. 1. Washington, DC,
USA: IEEE Computer Society, Los Alamitos, California, USA. pp. 586--591.
CiteSeerX 10.1.1.452.3319. doi:10.1109/ITCC.2005.62. ISBN
978-0-7695-2315-6. S2CID 9364961. Chemical Gutmann, Peter (2001), \"Data
Remanence in Semiconductor Devices\" (PDF), Proceedings of the 10th
Conference on USENIX Security Symposium SSYM\'01, USENIX Association
Berkeley, California, USA, vol. 10, p. 4, archived from the original
(PDF) on 2007-02-21, retrieved 2010-12-13 Electromagnetic Kuhn, Markus
G.; Anderson, Ross J. (1998). \"Soft Tempest: Hidden Data Transmission
Using Electromagnetic Emanations\". Information Hiding. Lecture Notes in
Computer Science. Lecture Notes in Computer Science. Vol. 1525. pp.
124--142. CiteSeerX 10.1.1.64.6982. doi:10.1007/3-540-49380-8_10. ISBN
978-3-540-65386-8. Van Eck, Wim; Laborato, Neher (1985),
\"Electromagnetic Radiation from Video Display Units: An Eavesdropping
Risk?\", Computers & Security, vol. 4, no. 4, pp. 269--286, CiteSeerX
10.1.1.35.1695, doi:10.1016/0167-4048(85)90046-X Kuhn, Markus G. (2002).
\"Optical time-domain eavesdropping risks of CRT displays\". Proceedings
2002 IEEE Symposium on Security and Privacy. Proceedings of the 2002
IEEE Symposium on Security and Privacy. pp. 3--. CiteSeerX
10.1.1.7.5870. doi:10.1109/SECPRI.2002.1004358. ISBN 978-0-7695-1543-4.
S2CID 2385507. Vuagnoux, Martin; Pasini, Sylvain (2009), \"Compromising
electromagnetic emanations of wired and wireless keyboards\" (PDF), In
Proceedings of the 18th Conference on USENIX Security Symposium
(SSYM\'09), pp. 1--16 Backes, Michael; Dürmuth, Markus; Unruh, Dominique
(2008). \"Optical time-domain eavesdropping risks of CRT displays\"
(PDF). Compromising Reflections-or-How to Read LCD Monitors around the
Corner. Proceedings of the IEEE Symposium on Security and Privacy.
Oakland, California, USA. pp. 158--169. CiteSeerX 10.1.1.7.5870.
doi:10.1109/SECPRI.2002.1004358. ISBN 978-0-7695-3168-7. S2CID 2385507.
FireWire Dornseif, Maximillian (2004), \"0wned by an iPod\" (PDF),
PacSec Dornseif, Maximillian (2005), \"FireWire all your memory are
belong to us\" (PDF), CanSecWest, archived from the original (PDF) on
2009-12-29, retrieved 2010-12-17 Processor bug and backdoors Duflot,
Loïc (2008). \"CPU Bugs, CPU Backdoors and Consequences on Security\".
Computer Security - ESORICS 2008. ESORICS \'08 Proceedings of the 13th
European Symposium on Research in Computer Security: Computer Security.
Lecture Notes in Computer Science. Vol. 5283. pp. 580--599.
doi:10.1007/978-3-540-88313-5_37. ISBN 978-3-540-88312-8. Duflot, Loïc
(2008), \"Using CPU System Management Mode to Circumvent Operating
System Security Functions\" (PDF), Proceedings of CanSecWest, pp.
580--599, archived from the original (PDF) on 2006-05-26 Waksman, Adam
(2010), \"Tamper Evident Microprocessors\" (PDF), Proceedings of the
IEEE Symposium on Security and Privacy, Oakland, California, archived
from the original (PDF) on 2013-09-21 Temperature Skorobogatov, Sergei
(2002), \"Low temperature data remanence in static RAM\" (PDF),
Technical Report - University of Cambridge. Computer Laboratory,
Cambridge, UK: University of Cambridge Computer Laboratory, ISSN
1476-2986 Halderman, J. Alex; Schoen, Seth D.; Heninger, Nadia;
Clarkson, William; Paul, William; Calandrino, Joseph A.; Feldman, Ariel
J.; Appelbaum, Jacob; Felten, Edward W. (2008). \"Lest We Remember: Cold
Boot Attacks on Encryption Keys\". Communications of the ACM -- Security
in the Browser (PDF). Proceedings of the USENIX Security Symposium. Vol.
52. ACM New York, New York, USA. pp. 45--60.
doi:10.1145/1506409.1506429. ISBN 978-1-931971-60-7. ISSN 0001-0782.
S2CID 7770695. Archived from the original (PDF) on 2011-09-04. Timing
attacks Song, Dawn Xiaodong; Wagner, David; Tian, Xuqing (2001),
\"Timing analysis of keystrokes and timing attacks on SSH\" (PDF),
Proceedings of the 10th Conference on USENIX Security Symposium,
Washington, D.C., USA: USENIX Association Berkeley, California, USA,
vol. 10, pp. 337--352 Kocher, Paul C. (1996). \"Timing Attacks on
Implementations of Diffie-Hellman, RSA, DSS, and Other Systems\".
Advances in Cryptology -- CRYPTO \'96. Proceedings of the 16th Annual
International Cryptology Conference on Advances in Cryptology -- CRYPTO
\'96. Lecture Notes in Computer Science. Vol. 1109. Santa Barbara,
California, USA: Springer-Verlag, London, UK. pp. 104--113. CiteSeerX
10.1.1.40.5024. doi:10.1007/3-540-68697-5_9. ISBN 978-3-540-61512-5.
Brumley, David; Boneh, Dan (2003), \"Remote timing attacks are
practical\" (PDF), Proceedings of the 12th Conference on USENIX Security
Symposium SSYM\'03, Washington, DC, USA: USENIX Association Berkeley,
California, USA, vol. 12, no. 5, p. 701, CiteSeerX 10.1.1.12.2615,
doi:10.1016/j.comnet.2005.01.010 Other Balzarotti, D.; Cova, M.; Vigna,
G. (2008). \"Clear Shot: Eavesdropping on Keyboard Input from Video\".
2008 IEEE Symposium on Security and Privacy (sp 2008). Security and
Privacy, 2008. SP 2008. IEEE Symposium on. Oakland, CA. pp. 170--183.
CiteSeerX 10.1.1.219.239. doi:10.1109/SP.2008.28. ISBN
978-0-7695-3168-7. ISSN 1081-6011. S2CID 1498613. Duflot, Loïc (2007),
Contribution à la sécurité des systèmes d\'exploitation et des
microprocesseurs (PDF) (in French)
