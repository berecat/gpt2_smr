# README #

Text summarization using **GPT2** and the **TransformerSummarizer** from [Hugging Face](https://huggingface.co/).

### Requirements ###

*	**transformers**

    pip3 install transformers

*	**bert-extractive-summarizer**

    pip3 install bert-extractive-summarizer

*	**sentencepiece**

    pip3 install sentencepiece

### How to Run ###

    python3 gpt2_summarizer.py -f [file path] -min [min length] -max [max length]

*	-f: file path.
*	-min: minimum summary length.
*	-max: maximum summary length (float).
