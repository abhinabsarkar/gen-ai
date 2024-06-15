# Large Language Models (LLM)
Large language models (LLM) are very large [deep learning](neuralnetwork-deeplearning--readme.md#deep-learning) models that generate human-like language using [Transformer Neural Network Architecture](https://www.youtube.com/watch?v=SZorAJ4I-sA) pre-trained on vast amounts of text data (in the order of Terabytes).

LLMs work by predicting the next word given an input. They do this by learning the statistical patterns in massive datasets of text. They don't understand the word per se, they have learned the weights for what is probably the next word given the context in which this word has been found.

## What's special about LLMs?
> For one, they are used in *ChatGPT* which has brought in the AI storm to masses.

Since 2012, technology made significant advances in analyzing images & vision problems like identifying objects in photos, recognizing faces, and reading handwritten digits using `Convolution Neural Networks (CNNs)`. But when it came to `Natural Language Processing (NLP)` tasks like translation, text summarization, text generation, then existing models `Recurrent Neural Network (RNN)` had limited success. The RNN model would process inputs sequentially without the context of words around it. For e.g. *The bank of the river* vs *Money in the bank* has different context for the same word *bank*. Refer [Attention in Language Models - Explained with an example](https://txt.cohere.com/what-is-attention-in-language-models/)

Here comes `Transformers` which does the magic! 

Unlike earlier recurrent neural networks (RNN) that sequentially process inputs, transformers process entire sequences in `parallel`. This allows the data scientists to use GPUs for training transformer-based LLMs, significantly reducing the training time.

## Transformers
`Transformer` is a set of [neural networks](neuralnetwork-deeplearning--readme.md#neural-network--deep-learning) that consist of an `encoder` and a `decoder` with `self-attention` capabilities. The encoder and decoder extract meanings from a sequence of text and understand the relationships between words and phrases in it.

Transformer LLMs are capable of performing self-learning. It is through this process that transformers learn to understand basic grammar, languages, and knowledge. 

## References
* [What are Large Language Models? - AWS](https://aws.amazon.com/what-is/large-language-model/)
* [Transformers, explained in video](https://www.youtube.com/watch?v=SZorAJ4I-sA)
    * [Transformers, explained in blog](https://daleonai.com/transformers-explained)
* [Transformers explained in details - video ](https://www.youtube.com/watch?si=PN-ARp297J-DcKo5&v=TQQlZhbC5ps&feature=youtu.be)
* [Attention in Language Models - Explained with an example](https://txt.cohere.com/what-is-attention-in-language-models/)