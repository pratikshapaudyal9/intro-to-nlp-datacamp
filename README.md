# intro-to-nlp-datacamp

This repo contains the notes and exercises from the Introduction to Natural Language Processing course I am completing in Datacamp.

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
- `sent_tokenize` The sent_tokenize function will split a document into individual sentences.
- The `regexp_tokenize` uses regular expressions to tokenize the string, giving more granular control over the process.
- `tweettokenizer` recognises hashtags, mentions and punctuation symbols following a sentence.
