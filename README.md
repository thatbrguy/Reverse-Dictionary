# Reverse Dictionary
A literal reverse english dictionary. Predicts the word for a given definition.

## How does it work?
We need to map a sequence of words (Our definition) to a target word. This can be done rather effectively using Recurrent Neural Networks, or its variants (Used cudNN-GRUs here).

We can build the RNN rather easily using Keras. The real nuisance is collecting and cleaning the data. The approach I chose was to gather a list of 3000 words from [here](https://www.ef.com/english-resources/english-vocabulary/top-3000-words/), and use `scrap_dict.py` (which uses bs4) to scrap the definitions. For convenience, i've included `dataset.txt`, which has the words and its corresponding definitions. The rest of the data processing, and the RNN is implemented in `ReverseDict.ipynb`.

## Requirements
- Keras
- BeautifulSoup (Only if you want to try scrapping data yourself).
- TensorFlow (Only if you want to use cudNN-GRU. Use your favourite backend otherwise).

## Disclaimer
The code works as intended. Maps a definition to a word. But, the output usually doesn't make sense (Gives the wrong word for the definition). Need a smarter way to feed data.

The reason I added this repo is that, it serves as a general experiment on seq2seq models. It can be generalised to several use cases. For example, you can make a chatbot using the same code, by just feeding the right data.
