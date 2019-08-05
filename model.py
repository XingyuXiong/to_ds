#
import random
from topic import recognize_topics
from scrape_news import News


def random_select(enum):
    if isinstance(enum,list):
        rint=random.randint(0,len(enum))
        return enum[rint]

class Model():
    news=News()

    def init_conversation(self):
        self.news.read_default_news()


    def response_on_topic(self,sentence):
        topics=recognize_topics(sentence)
        #print(topics)
        return self.generate_content(self.select_topic(topics))


    def select_topic(self,topic_sequence):
        return random_select(topic_sequence)


    def select_article(self,article_sequence):
        return random_select(article_sequence)


    def select_sentence_from_content(self,content):
        return content


    def generate_content(self,topic):
        articles=self.news.read_news(topic)
        content=self.select_article(articles)['content']
        response_sentence=self.select_sentence_from_content(content)
        return response_sentence