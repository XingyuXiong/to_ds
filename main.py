#
from model import Model

end_word='bye'

model=Model()

def response(sentence):
    print(model.response_on_topic(sentence))


def init_model():
    print('Hello, this is a very simple chatbot')
    print('I am waiting for you to say something...')
    print('Whenever you want to end the conversation, type '+end_word)
    model.init_conversation()


if __name__=='__main__':
    init_model()
    while(True):
        receive_sentence=input();
        if receive_sentence==end_word:
            break
        response(receive_sentence)