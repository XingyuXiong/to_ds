# -*- coding:gbk -*-

from newsapi import NewsApiClient
import pickle
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

global null
null=''

api_key='793110ecda064a68846a1510d0e7d0ae'
newsapi=NewsApiClient(api_key=api_key)

topic_stack={'France':1}
topic_content={}
max_topic=10


def solve_code_error(input_dict):
    for key,value in input_dict.items():
        try:
            solve_code_error(value)
        except AttributeError:
            if isinstance(value,str):
                print(value)
                value=value


def generate_content(topic):



class News():    
    def __init__(self):
        pass


    def __init__(self,topic_list):
        pass

    def write_default_news(self):
        for topic in topic_stack:
            print(topic)
            try:
                print(json.dumps(newsapi.get_everything(q='France'),ensure_ascii=False))
                topic_content[topic]=newsapi.get_everything(q=topic)
            except RuntimeError:
                pass
            else:
                break
        with open('pickle_topic_content','wb') as file:
            pickle.dump(topic_content,file)


    def read_default_news(self):
        with open('pickle_topic_content','rb') as file:
            topic_content=pickle.load(file)


    def add_topic(self,new_topics={}):
        for new_topic_name in new_topics:
            if topic_content.len()>max_topic:
                self._forget_topic()
            topic_stack[new_topic_name]=new_topics[new_topic_name]


    def _forget_topic(self):
        pass



    def read_news(self,topic=''):
        print(topic_content['France'])