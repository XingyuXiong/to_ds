#
import pandas as pd
from stanfordcorenlp import StanfordCoreNLP
from nltk_ner import ner


test_sentence='I love Beijing'


def recognize_topics(sentence):
    return use_nltk(sentence)


def use_stanford(sentence):
    nlp=StanfordCoreNLP()
    print(nlp.ner(test_sentence))


def use_nltk(sentence):
    ner_frame=ner(sentence)
    return ner_frame['Entity Name'].values    
