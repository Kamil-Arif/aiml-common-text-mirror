LLaMA (Large Language Model Meta AI) is a large language model (LLM)
released by Meta AI in February 2023. A variety of model sizes were
trained ranging from 7 billion to 65 billion parameters. LLaMA\'s
developers reported that the 13 billion parameter model\'s performance
on most NLP benchmarks exceeded that of the much larger GPT-3 (with 175
billion parameters) and that the largest model was competitive with
state of the art models such as PaLM and Chinchilla. Whereas the most
powerful LLMs have generally been accessible only through limited APIs
(if at all), Meta released LLaMA\'s model weights to the research
community under a noncommercial license. Within a week of LLaMA\'s
release, its weights were leaked to the public on 4chan via BitTorrent.
Architecture and training LLaMA uses the transformer architecture, the
standard architecture for language modelling since 2018. LLaMA\'s
developers focused their effort on scaling the model\'s performance by
increasing the volume of training data, rather than the number of
parameters, reasoning that the dominating cost for LLMs is from doing
inference on the trained model rather than the computational cost of the
training process. LLaMA was trained on 1.4 trillion tokens, drawn from
publicly available data sources, including: Webpages scraped by
CommonCrawl Open source repositories of source code from GitHub
Wikipedia in 20 different languages Public domain books from Project
Gutenberg The LaTeX source code for scientific papers uploaded to ArXiv
Questions and answers from Stack Exchange websites Release and leak
LLaMA was announced on February 23, 2023, via a blog post and a paper
describing the model\'s training, architecture, and performance. The
code used to train the model was publicly released under the open-source
GPL 3 license. Access to the model\'s weights was managed by an
application process, with access to be granted \"on a case-by-case basis
to academic researchers; those affiliated with organizations in
government, civil society, and academia; and industry research
laboratories around the world\".On March 2, 2023, a torrent containing
LLaMA\'s weights was uploaded, with a link to the torrent shared on the
4chan imageboard and subsequently spreading through online AI
communities. That same day, a pull request on the main LLaMA repository
was opened, requesting to add the magnet link to the official
documentation. On March 4, a pull request was opened to add links to
HuggingFace repositories containing the model. On March 6, Meta filed
takedown requests to remove the HuggingFace repositories linked in the
pull request, characterizing it as \"unauthorized distribution\" of the
model. HuggingFace complied with the requests. On March 20, Meta filed a
DMCA takedown request for copyright infringement against a repository
containing a script that downloaded LLaMA from a mirror, and GitHub
complied the next day. As of March 25, Facebook has not responded to the
pull request containing the magnet link.Reactions to the leak varied.
Some speculated that the model would be used for malicious purposes,
such as more sophisticated spam. Some have celebrated the model\'s
accessibility, as well as the fact that smaller versions of the model
can be run relatively cheaply, suggesting that this will promote the
flourishing of additional research developments. Multiple commentators,
such as Simon Willison, compared LLaMA to Stable Diffusion, a
text-to-image model which, unlike comparably sophisticated models which
preceded it, was openly distributed, leading to a rapid proliferation of
associated tools, techniques, and software. Open Sourcing/Reproduction
On April 17, 2023, Together launched a project named RedPajama to
reproduce and distribute an open source version of the LLaMA dataset.
The dataset has approximately 1.2 trillion tokens and is publicly
available for download. Applications The Stanford University Institute
for Human-Centered Artificial Intelligence (HAI) Center for Research on
Foundation Models (CRFM) released Alpaca, a training recipe based on the
LLaMA 7B model that uses the \"Self-Instruct\" method of instruction
tuning to acquire capabilities comparable to the OpenAI GPT-3.5 series
text-davinci-003 model at a modest cost. Multiple open source projects
are continuing this work of finetuning LLaMA with Alpaca dataset. ==
References ==
