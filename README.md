# intro-to-nlp-datacamp

This repo contains the notes and exercises from the Introduction to Natural Language Processing course I am completing in Datacamp.

## Chapter 1 - Regular Expressions and Word Tokenisation

## Regex

- use the `re` library
- Format is always the pattern first, followed by the string:

``` python
(re.split(sentence_endings, my_string))
```

### Useful methods

`Findall`
`split`
`search`
`match`

## Tokenize

- used to remove unwanted tokens.
- determine meaning from text.
- import the `nltk` library.
- `word_tokenize` - add description here.
- `sent_tokenize` - the sent_tokenize function will split a document into individual sentences.
- The `regexp_tokenize` - uses regular expressions to tokenize the string, giving more granular control over the process.
- `tweettokenizer` - recognises hashtags, mentions and punctuation symbols following a sentence.

## Chapter 2 - Simple Topic Identification

## Bag-of-words

`from collections import Counter`

### nltk ... not installed errors

When running code dependent on the nltk package, certain methods will bring up a "not installed error".
To fix these errors, in the python interactive shell run:

``` python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
```

## Preprocessing

- Tokenisation
- Lowercasing words
- Lemmatisation/Stemming - shorten words to their root stems
- Remove "the", punctuation and other filler tokens
- Good to experiment with different preprocessing examples to best suit individual needs.

`from nltk.corpus import stopwords`

- Use list comprehension to lower words

``` python
tokens = [w for w in word_tokenize(text.lower())
                  if w.isalpha()]
```

`isalpha` will return alphabetical characters only. It will strip out numbers/punctuation.

``` python
no_stops = [t for t in tokens
                  if t not in stopwords.words('english')]
```

Then can use Counter to return the most common words:

``` python
Counter(no_stops).most_common(2)
```

## gensim

- open-source NLP package
- corpus - set of text used to perform NLP tasks
- `from genism.corpora.dictionary import Dictionary`

### Creating a gensim corpus

``` python
corpus = [dictionary.doc2bow(doc) for doc in tokenized_docs]
```

The above code snippet produces a list of lists where each list item represents one document. Each document a series of tuples, the first item representing the token ID from the dictionary and the second item representing the token frequency in the document.

`gensim` model can be saved/updated/reused.

## tf-idf

Term frequency - inverse document frequency (tf-idf)
keep document specific words weighted high

Wi,j = TFi,j * log (N/DFi)

Where:

wi,j is the tf-idf weight for token i in document j.
TFi,j is the number of occurrences of i in document j.
DFi is the number of documents containing the term i.
N is the total number of documents in the corpus.

Words that occur across many or all documents will have a very low tf-idf weight. On the contrary, if the word only occurs in a few documents, that logarithm will return a higher number.

``` python
from gensim.models.tfidfmodel import TfidfModel
tfidf = TfidfModel(corpus)
tfidf[corpus[1]]
```

## Chapter 3 - Named Entity Recognition

- Stanford coreNLP library

`pos_tag()` method
`nltk.ne_chunk(sentence)` to create a tree with leaves.

### SpaCy

- Similar to `gensim`
- `import spacy`
- Easy pipeline creation
- informal language corpora
- is growing fast

``` python
nlp = spacy.load('en')
nlp.entity
# load doc 
doc = nlp(""" Berlin....""")
# output the key entities
doc.ents 
print(doc.ents[0], doc.ents[0].label_)
```

### polygot

- NLP library using word vectors
- Has word vectors for more than over 130 languages
- `from polyglot.text import Text`
- infers the language from the text

## Chapter 4 - Classifying fake news using supervised learning with NLP

### Supervised Learning Steps

- Collect and preprocess data
- Determine a label (e.g. Pop Music genre)
- Split data into a training and test set, keep test data separate until it is time to see how well the training data performs
- Extract features from the test to help predict the label
  - bag-of-words vector built into `scikit-learn`
- Evaluate trained model using the test set, or k-fold cross validation.

### Naive Bayes Classifier

- commonly used for testing NLP classification problems

``` python
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

nb_classifier = MultimomialNB()
nb_classifier.fit(count_train, y_train)
pred = nb_classifier.predict(count_test)
metrics.accuracy_score(y_test, pred)
metrics.confusion_matrix(y_test, pred, labels=[0,1])
```

