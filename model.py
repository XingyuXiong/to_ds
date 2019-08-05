#
import random
from scrape_news import generate_content
from topic import recognize_topics


def response_on_topic(sentence):
    topics=recognize_topics(sentence)
    print(topics)
    generate_content(select_topic(topics))


def select_topic(topic_sequence):
    return random_select(topic_sequence)


def random_select(enum):
    rint=random.randint(0,len(enum))
    if isinstance(enum,list):
        return enum[rint]