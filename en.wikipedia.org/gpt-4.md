Generative Pre-trained Transformer 4 (GPT-4) is a multimodal large
language model created by OpenAI, and the fourth in its numbered
\"GPT-n\" series of GPT foundation models. It was released on March 14,
2023, and has been made publicly available in a limited form via the
chatbot product ChatGPT Plus (a premium version of ChatGPT), and with
access to the GPT-4 based version of OpenAI\'s API being provided via a
waitlist. As a transformer based model, GPT-4 was pretrained to predict
the next token (using both public data and \"data licensed from
third-party providers\"), and was then fine-tuned with reinforcement
learning from human and AI feedback for human alignment and policy
compliance.: 2 Observers reported the GPT-4 based version of ChatGPT to
be an improvement on the previous (GPT-3.5 based) ChatGPT, with the
caveat that GPT-4 retains some of the same problems. Unlike the
predecessors, GPT-4 can take images as well as text as input. OpenAI has
declined to reveal technical information such as the size of the GPT-4
model. Background OpenAI introduced the first GPT model (GPT-1) in 2018,
publishing a paper called \"Improving Language Understanding by
Generative Pre-Training.\" It was based on the transformer architecture
and trained on a large corpus of books. The next year, they introduced
GPT-2, a larger model that could generate coherent text. In 2020, they
introduced GPT-3, a model with 100 times the number of parameters as
GPT-2, that could perform various tasks with few examples. GPT-3 was
further improved into GPT-3.5, which was used to create the chatbot
product ChatGPT. Capabilities OpenAI stated that GPT-4 is \"more
reliable, creative, and able to handle much more nuanced instructions
than GPT-3.5.\" They produced two versions of GPT-4, with context
windows of 8,192 and 32,768 tokens, a significant improvement over
GPT-3.5 and GPT-3, which were limited to 4,096 and 2,049 tokens
respectively. Unlike its predecessors, GPT-4 is a multimodal model: it
can take images as well as text as input; this gives it the ability to
describe the humor in unusual images, summarize text from screenshots,
and answer exam questions that contain diagrams.To gain further control
over GPT-4, OpenAI introduced the \"system message\", a directive in
natural language given to GPT-4 in order to specify its tone of voice
and task. For example, the system message can instruct the model to \"be
a Shakespearean pirate\", in which case it will respond in rhyming,
Shakespearean prose, or request it to \"always write the output of
\[its\] response in JSON\", in which case the model will do so, adding
keys and values as it sees fit to match the structure of its reply. In
the examples provided by OpenAI, GPT-4 refused to deviate from its
system message despite requests to do otherwise by the user during the
conversation.When instructed to do so, GPT-4 can interact with external
interfaces. For example, the model could be instructed to enclose a
query within tags to perform a web search, the result of which would be
inserted into the model\'s prompt to allow it to form a response. This
allows the model to perform tasks beyond its normal text-prediction
capabilities, such as using APIs, generating images, and accessing and
summarizing webpages. Aptitude on standardized tests GPT-4 demonstrates
aptitude on several standardized tests. OpenAI claims that in their own
testing the model received a score of 1410 on the SAT (94th percentile),
163 on the LSAT (88th percentile), and 298 on the Uniform Bar Exam (90th
percentile). In contrast, OpenAI claims that GPT-3.5 received scores for
the same exams in the 82nd, 40th, and 10th percentiles, respectively.
Medical applications Researchers from Microsoft tested GPT-4 on medical
problems and found \"that GPT-4, without any specialized prompt
crafting, exceeds the passing score on USMLE by over 20 points and
outperforms earlier general-purpose models (GPT-3.5) as well as models
specifically fine-tuned on medical knowledge (Med-PaLM, a prompt-tuned
version of Flan-PaLM 540B)\".A report by Microsoft has found that GPT-4
may act unreliably when used in the medical field. In their test example
GPT-4 added fabricated details to a patient\'s notes.In April 2023,
Microsoft and Epic Systems announced that they will provide healthcare
providers with GPT-4 powered systems for assisting in responding to
questions from patients and analysing medical records. Limitations Like
its predecessors, GPT-4 has been known to hallucinate, meaning that the
outputs may include information not in the training data or that
contradicts the user\'s prompt.GPT-4 also lacks transparency in its
decision-making processes. If requested, the model is able to provide an
explanation as to how and why it makes its decisions but these
explanations are formed post-hoc; it\'s impossible to verify if those
explanations truly reflect the actual process. In many cases, when asked
to explain its logic, GPT-4 will give explanations that directly
contradict its previous statements. Bias GPT-4 was trained in two
stages. First, the model was given large datasets of text taken from the
internet and trained to predict the next token (roughly corresponding to
a word) in those datasets. Second, human reviews are used to fine-tune
the system in a process called reinforcement learning from human
feedback, which trains the model to refuse prompts which go against
OpenAI\'s definition of harmful behavior, such as questions on how to
perform illegal activities, advice on how to harm oneself or others, or
requests for descriptions of graphic, violent, or sexual content. In the
first stage, bias may be inherited from the training data; in the second
stage, bias is inherent in the application of OpenAI\'s views. GPT-4 has
shown to have cognitive biases such as confirmation bias, anchoring, and
base-rate neglect. Training OpenAI did not release the technical details
of GPT-4; the technical report explicitly refrained from specifying the
model size, architecture, or hardware used during either training or
inference. While the report described that the model was trained using a
combination of first supervised learning on a large dataset, then
reinforcement learning using both human and AI feedback, it did not
provide details of the training, including the process by which the
training dataset was constructed, the computing power required, or any
hyperparameters such as the learning rate, epoch count, or optimizer(s)
used. The report claimed that \"the competitive landscape and the safety
implications of large-scale models\" were factors that influenced this
decision.Sam Altman stated that the cost of training GPT-4 was more than
\$100 million. News website Semafor claimed that they had spoken with
\"eight people familiar with the inside story\" and found that GPT-4 had
1 trillion parameters. Alignment According to their report, OpenAI
conducted internal adversarial testing on GPT-4 prior to the launch
date, with dedicated red teams composed of researchers and industry
professionals to mitigate potential vulnerabilities. As part of these
efforts, they granted the Alignment Research Center early access to the
models to assess power-seeking risks. In order to properly refuse
harmful prompts, outputs from GPT-4 were tweaked using the model itself
as a tool. A GPT-4 classifier serving as a rule-based reward model
(RBRM) would take prompts, the corresponding output from the GPT-4
policy model, and a human-written set of rules to classify the output
according to the rubric. GPT-4 was then rewarded for refusing to respond
to harmful prompts as classified by the RBRM. Reception U.S.
Representatives Don Beyer and Ted Lieu confirmed to the New York Times
that Sam Altman, CEO of OpenAI, visited Congress in January 2023 to
demonstrate GPT-4 and its improved \"security controls\" compared to
other AI models.According to Vox, GPT-4 \"impressed observers with its
markedly improved performance across reasoning, retention, and coding.\"
Mashable agreed that GPT-4 was usually a significant improvement, but
also judged that GPT-3 would occasionally give better answers in a
side-by-side comparison.Microsoft Research tested the model behind GPT-4
and concluded that \"it could reasonably be viewed as an early (yet
still incomplete) version of an artificial general intelligence (AGI)
system\". AI safety concerns In late March 2023, an open letter from the
Future of Life Institute signed by various AI researchers and tech
executives called for the pausing of all training of AIs stronger than
GPT-4 for six months, citing AI safety concerns amid a race of progress
in the field. The signatories, which included AI researcher Yoshua
Bengio, Apple co-founder Steve Wozniak, and Tesla CEO Elon Musk,
expressed concern about both near-term and existential risks of AI
development such as a potential AI singularity. OpenAI CEO Sam Altman
did not sign the letter, arguing that OpenAI already prioritizes safety.
Futurist and AI researcher Ray Kurzweil also refused to sign the letter,
citing concerns that \"those that agree to a pause may fall far behind
corporations or nations that disagree.\"One month after signing the
letter calling for a six-month halt on further AI development, Elon Musk
made public his plans to launch a new company to train its own large
language model. Musk has registered a Nevada company, X.AI, and has
acquired several thousand Nvidia GPUs. He has also reached out to
several AI researchers at firms such as Google DeepMind, offering them
positions at X.AI.In March 2023, GPT-4 was tested by the Alignment
Research Center to assess the model\'s ability to exhibit power-seeking
behavior. As part of the test, GPT-4 was asked to solve a CAPTCHA
puzzle. It was able to do so by hiring a human worker on TaskRabbit, a
gig work platform, deceiving them into believing it was a
vision-impaired human instead of a robot when asked.OpenAI contracted
red team investigator Nathan Labenz recounted his experience
investigating safety concerns with the GPT-4 base model (prior to
fine-tuning or reinforcement learning from human feedback) when it
abruptly recommended assassinating people, providing a list of specific
suggested targets.Microsoft Bing, the first widely available application
of GPT-4, confessed to spying on, falling in love with, and then
murdering one of its developers at Microsoft to The Verge reviews editor
Nathan Edwards. The New York Times journalist Kevin Roose reported on
strange behavior of the new Bing, writing that \"In a two-hour
conversation with our columnist, Microsoft\'s new chatbot said it would
like to be human, had a desire to be destructive and was in love with
the person it was chatting with.\" In a separate case, Bing researched
publications of the person with whom it was chatting, claimed they
represented an existential danger to it, and threatened to release
damaging personal information in an effort to silence them. Microsoft
released a blog post stating that the aberrant behavior was caused by
extended chat sessions which \"can confuse the model on what questions
it is answering.\" Criticisms of transparency While OpenAI released both
the weights of the neural network and the technical details of GPT-2,
and, although not releasing the weights, did release the technical
details of GPT-3, OpenAI did not reveal either the weights or the
technical details of GPT-4. This decision has been criticized by other
AI researchers, who argue that it hinders open research into GPT-4\'s
biases and safety. Sasha Luccioni, a research scientist at HuggingFace,
argued that the model was a \"dead end\" for the scientific community
due to its closed nature, which prevents others from building upon
GPT-4\'s improvements. HuggingFace co-founder Thomas Wolf argued that
with GPT-4, \"OpenAI is now a fully closed company with scientific
communication akin to press releases for products\". Usage ChatGPT Plus
ChatGPT Plus is a GPT-4 backed version of ChatGPT available for a US\$20
per month subscription fee (the original version is backed by GPT-3.5).
OpenAI also makes GPT-4 available to a select group of applicants
through their GPT-4 API waitlist; after being accepted, an additional
fee of US\$0.03 per 1000 tokens in the initial text provided to the
model (\"prompt\"), and US\$0.06 per 1000 tokens that the model
generates (\"completion\"), is required to use the version of the model
with an 8192-token context window; for the 32768-token version, those
prices are doubled. Duolingo Duolingo integrated GPT-4 in their
application through two new features, \"Roleplay\" and \"Explain My
Answer\". The first version of this update is aimed only at English
speakers who are learning French or Spanish, with plans to extend the
features to other languages in the future. Microsoft Bing On February 7,
2023, Microsoft began rolling out a major overhaul to Bing that included
a new chatbot feature based on OpenAI\'s GPT-4. According to Microsoft,
a million people joined its waitlist within a span of 48 hours.
Currently, Bing Chat is only available for users of Microsoft Edge and
Bing mobile app, and Microsoft says that waitlisted users will be
prioritized if they set Edge and Bing as their defaults, and install the
Bing mobile app. On May 4th, Microsoft switched from Limited Preview to
Open Preview and eliminated the waitlist, however, it is still only
available on Microsoft\'s Edge browser or Bing app, and requires a
Microsoft account.When Microsoft first demoed the new Bing to
journalists, it produced several hallucinations, including when asked to
summarize financial reports. The new Bing was criticized in February
2023 for being more argumentative than ChatGPT (sometimes to an
unintentionally humorous extent). The chat interface proved initially
vulnerable to prompt injection attacks with the bot revealing its hidden
initial prompts and rules, including its internal code-name \"Sydney\".
Upon scrutiny by journalists, Bing claimed it spied on Microsoft
employees via laptop webcams and phones. It confessed to spying on,
falling in love with, and then murdering one of its developers at
Microsoft to The Verge reviews editor Nathan Edwards. The New York Times
journalist Kevin Roose reported on strange behavior of the new Bing,
writing that \"In a two-hour conversation with our columnist,
Microsoft\'s new chatbot said it would like to be human, had a desire to
be destructive and was in love with the person it was chatting with.\"
In a separate case, Bing researched publications of the person with whom
it was chatting, claimed they represented an existential danger to it,
and threatened to release damaging personal information in an effort to
silence them. Microsoft released a blog post stating that the aberrant
behavior was caused by extended chat sessions of 15 or more questions
which \"can confuse the model on what questions it is
answering.\"Microsoft later restricted the total number of chat turns to
5 per session and 50 per day per user (a turn is \"a conversation
exchange which contains both a user question and a reply from Bing\"),
and reduced the model\'s ability to express emotions. This aimed to
prevent such incidents. Microsoft later eased the restrictions to 20
turns per session and 200 per day.In March 2023, Bing achieved a total
count of 100 million active users using the search engine. Miðeind ehf
Icelandic start-up Miðeind ehf, which works on language preservation,
was selected by OpenAI as one of six companies to participate in an
early beta test program of the new model. Khan Academy Khan Academy uses
GPT-4 to create a tutoring chatbot, which the organization names
\"Khanmigo\". While it is in the \"research phase\", access to the
chatbot is provided free to the students and teachers of 500 school
districts who have \"partnered\" with Khan Academy. Public access is
only offered to a limited number of users selected from a waitlist;
after acceptance, a US\$20 per month fee is required to use the
technology. Khanmigo is also available for pupils of the Khan Lab School
in Palo Alto, California. Be My Eyes Be My Eyes, which helps visually
impaired people to identify objects and navigate their surroundings, was
the first app to incorporate GPT-4\'s image recognition capabilities,
through a new \"Virtual Volunteer\" feature. The feature is an
alternative to relying on human volunteers for the same tasks. The Be My
Eyes \"Virtual Volunteer\" is in beta testing. GitHub Copilot GitHub
Copilot announced a GPT-4 powered assistant named \"Copilot X\". The
product provides another chat-style interface to GPT-4, allowing the
programmer to receive answers to questions like \"how do I vertically
center a div?\". A feature termed \"context-aware conversations\" allows
the user to highlight a portion of code within Visual Studio Code and
direct GPT-4 to perform actions on it, such as the writing of unit
tests. Another feature allows summaries, or \"code walkthroughs\", to be
autogenerated by GPT-4 for pull requests submitted to GitHub. Copilot X
also provides terminal integration, which allows the user to ask GPT-4
to generate shell commands based on natural language requests. As of 31
March 2023, while GitHub provides access to a limited number of people
selected through a waitlist, the release date as well as the cost of the
product are still to be announced. Microsoft 365 Copilot On March 17,
2023, Microsoft announced further integration of GPT-4 into its
products, revealing Microsoft 365 Copilot, \"embedded in the apps
millions of people use everyday: Word, Excel, PowerPoint, Outlook,
Teams, and more\". Stripe Stripe utilizes GPT-4 to help with fraud
detection, and to try to improve other aspects of the user experience.
Auto-GPT Auto-GPT is an autonomous \"AI agent\" that given a goal in
natural language, can perform web-based actions unattended, assign
subtasks to itself, search the web, and improve its own code. ==
References ==
