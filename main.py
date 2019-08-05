#
from model import response_on_topic


def response(sentence):
    return response_on_topic(sentence)


end_word='bye'
if __name__=='__main__':
    print('Hello, this is a very simple chatbot')
    print('I am waiting for you to say something...')
    print('Whenever you want to end the conversation, type '+end_word)
    while(True):
        receive_sentence=input();
        if receive_sentence==end_word:
            break
        response(receive_sentence)