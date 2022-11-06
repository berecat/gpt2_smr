import os
import sys

from optparse import OptionParser
from summarizer import TransformerSummarizer


def load_file_content(path):
    with open(path, "r") as fd:
        return fd.readlines()


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--file-path", dest="file_path")
    parser.add_option("-min", "--min-length", dest="min_length")
    parser.add_option("-max", "--max-length", dest="max-length")

    (options, args) = parser.parse_args()

    min_length = -0x1
    max_length = -0x1

    if options.file_path is None or not os.path.isfile(options.file_path):
        sys.stderr.write("Invalid Input\n")
        exit(0x1)

    try:
        min_length = int(options.min_length)
    except ValueError:
        sys.stderr.write("Invalid Min Length\n")
        exit(0x2)

    try:
        max_length = int(options.max_length)
    except ValueError:
        sys.stderr.write("Invalid Max Length\n")
        exit(0x3)

    text = load_file_content(options.file_path)

    gpt2_summarizer = TransformerSummarizer(transformer_type="GPT2",
                                            transformer_model_key="gpt2-large"
                                            )

    gpt2_summary = "".join(gpt2_summarizer(text,
                                           min_length=min_length,
                                           max_length=max_length))

    print(gpt2_summary)
