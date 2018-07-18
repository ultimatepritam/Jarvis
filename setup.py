import nltk
def setup():
  try:
    nltk.data.find('corpora/wordnet')
  except LookupError:
    nltk.download('wordnet')
