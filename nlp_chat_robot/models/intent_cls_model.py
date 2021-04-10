from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer,Interpreter
from rasa_nlu import config

import os, pickle

class intent_cls_model(object):
    def __init__(self, model_dir):
        self.model_dir = model_dir
        self.interpreter = Interpreter.load(model_dir)
    @staticmethod
    def is_contain_ch(raw_msg):
        for ch in raw_msg:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
    def get_intent(self, raw_msg):
        if intent_cls_model.is_contain_ch(raw_msg):
            return 'poem'
        raw_res = self.get_all_res(raw_msg)
        intent_string = raw_res['intent']['name']
        return intent_string
    def get_all_res(self, raw_msg):
        return self.interpreter.parse(raw_msg)

# file_path = 'model_file/cls_intent_v1/'
# config_path = os.path.join(file_path, "config_spacy.yml")
# training_data_path = os.path.join(file_path, 'demo-rasa.json')
# # Create a trainer thatthis c# trainer = Trainer(config.load("/content/Conversational-software/config_cy.yml")).
# trainer = Trainer(config.load(config_path))
#
# # Load the train# ing data
# training_data = load_data(training_data_path)
#
# # Create an interpreter by training the model
# interpreter = trainer.train(training_data)
# with open(file_path+'modelv1.pkl','wb') as file:
#     pickle.dump(interpreter,file)
# interpreter_s = pickle.dumps(interpreter)
# interpreter = Interpreter.load('model_file/cls_intent_v1/default/model_20210310-095544')
# print(interpreter.parse('I want to create poems'))

# with open('model_file/cls_intent_v1modelv1.pkl','rb') as file:
#     load_model = pickle.load(file)
# print(load_model.parse('I want to create poems.'))

# {'intent': {'name': 'create_poem', 'confidence': 0.3844450011778312},
#  'entities': [],
#  'intent_ranking': [
#      {'name': 'create_poem', 'confidence': 0.3844450011778312},
#      {'name': 'restaurant_search', 'confidence': 0.20787460036012215},
#      {'name': 'goodbye', 'confidence': 0.152222641139383},
#      {'name': 'affirm', 'confidence': 0.11264914088749077},
#      {'name': 'greet', 'confidence': 0.06173540677131722},
#      {'name': 'hotel_search', 'confidence': 0.04231083802069471},
#      {'name': 'location', 'confidence': 0.03876237164316099}],
#  'text': 'I want to create poems'}

if __name__ == '__main__':
    model = intent_cls_model('model_file/cls_intent_v2/bot/model_true_v2')
    question_list=['hello','我想写诗句','I want to write poem','I want to create poems',
                   '我喜欢写诗句','你好']
    for q in question_list:

        raw_msg = q
        intent_string = model.get_intent(raw_msg)
        print(intent_string)
        print(model.get_all_res(raw_msg))