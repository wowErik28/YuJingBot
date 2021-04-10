from nlp_chat_robot.models.model_list import *
from nlp_chat_robot.models.intent_cls_model import intent_cls_model

import nlp_chat_robot.config as config
class Robot(object):

    def __init__(self, model_list_dict, intent_cls_model_dir=None, greet_dict=None):
        self.model_list_dict = model_list_dict
        self.model_list = list(self.model_list_dict.values())[0]
        self.cls_intent = intent_cls_model(intent_cls_model_dir)
        self.greet_dict = greet_dict
    def update_model_list(self, str_order):
        self.model_list = self.model_list_dict[str_order]

    def get_response(self, raw_msg):
        res_dict = {}
        #switch model_list
        intent_string = self.cls_intent.get_intent(raw_msg)
        # print('current model_list:', self.model_list.name)
        # print('intent: ',intent_string)
        if intent_string != self.model_list.name:
            self.model_list=self.model_list_dict[intent_string]
            # the greet sentence
            res_dict['msg'] = self.greet_dict[intent_string]
        else:
            #get_response
            self.model_list.get_response(raw_msg, res_dict)
        return res_dict

'''
model_list_dict: the dict of model_list 
greet_dict: the response when it is the first time to use
'''

model_list_dict = {'en':get_eng_emotion_model_list('en'),
                   'poem':get_poem_model_list('poem')}
intent_cls_model_dir = config.intent_cls_model_dir

greet_dict = {'en':'Hello, I am YuJing, nice to meet you!',
              'poem':'你写一句诗，我给你添笔'}

def get_robot(model_list_dict, intent_cls_model_dir, greet_dict):
    return Robot(model_list_dict,intent_cls_model_dir=intent_cls_model_dir, greet_dict=greet_dict)

robot = get_robot(model_list_dict, intent_cls_model_dir, greet_dict)

def get_response(raw_msg):
    global robot
    return robot.get_response(raw_msg)

if __name__ == '__main__':

    import warnings
    warnings.filterwarnings("ignore")
    import pyttsx3
    import ffmpeg
    # file_name = '2.mp3'
    engine = pyttsx3.init()
    while 1:
        raw_msg = input('You:')
        res_dict = get_response(raw_msg)
        print('Robot',res_dict['msg'])
        engine.say(res_dict['msg'])
        engine.runAndWait()


