import codecs
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()

setup(
  name = 'vadernew',
  #packages = ['vadernew'], # this must be the same as the name above
  packages = find_packages(exclude=['tests*']), # a better way to do it than the line above -- this way no typo/transpo errors
  include_package_data=True,
  version = '2.0',
  description = 'Pacchetto contentente 4 dizionari che fungono da miglioramento di Vader per argomanti specifici, quali recensioni di cibi, finanza, recensioni Disneyland e recensioni di prodotti elettronici. Il pacchetto è creato a partire da quello cjhutto (https://github.com/cjhutto/vaderSentiment)',
  author = ['Vittorio Haardt','Luca Porcelli','Riccardo Fossato'],
  author_email = 'vittoriohaardt@gmail.com',
  license = 'MIT License: http://opensource.org/licenses/MIT',
  url = 'https://github.com/Lucaa00/Vader_new', # use the URL to the github repo
  install_requires = ['requests'],
  keywords = ['vader', 'sentiment', 'analysis', 'opinion', 'mining', 'nlp', 'text', 'data',
              'text analysis', 'opinion analysis', 'sentiment analysis', 'text mining', 'twitter sentiment',
              'opinion mining', 'social media', 'twitter', 'social', 'media'], # arbitrary keywords
  classifiers = ['Development Status :: 4 - Beta', 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License', 'Natural Language :: English',
                 'Programming Language :: Python :: 3.5', 'Topic :: Scientific/Engineering :: Artificial Intelligence',
                 'Topic :: Scientific/Engineering :: Information Analysis', 'Topic :: Text Processing :: Linguistic',
                 'Topic :: Text Processing :: General'],
)
