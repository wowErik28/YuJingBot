from transformers import pipeline,TextGenerationPipeline,BertTokenizer, TFGPT2LMHeadModel

import nlp_chat_robot.config as config
import random
class base_node(object):

    def __init__(self, next_node, name =None):
        self.next_node = next_node
        self.name = name
    def set_next(self, next_node):
        self.next_node = next_node
    def get_next(self):
        return self.next_node

    def get_response(self, raw_msg, res_dict):
        '''
        :param raw_msg: unprocessed message string
        :param res_dict: a dict
        :return:
        '''
        pass

class eng_gen_node(base_node):
    def __init__(self, next_node):
        super().__init__(next_node)
        self.text_generate = pipeline("text-generation")

    def get_response(self, raw_msg, res_dict):

        res= self.text_generate(\
            raw_msg, max_length=20, do_sample=True, num_return_sequences=1)[0]['generated_text']

        if res.find(raw_msg)!=-1:
            res.replace(raw_msg,'',1)
        res_dict['msg'] = res

class emotion_cls_node(base_node):

    def __init__(self, next_node):
        super().__init__(next_node)
        self.emotion_classification = pipeline("sentiment-analysis")

    def get_response(self, raw_msg, res_dict):
        res_dict['emotion'] = self.emotion_classification(raw_msg)[0]['label']

class random_emotion_cls_node(base_node):
    def __init__(self, next_node, int_range_list):
        super().__init__(next_node)
        self.int_range_list = int_range_list

    def get_response(self, raw_msg, res_dict):
        res_dict['emotion'] = random.choice(self.int_range_list)

class poem_gen_node(base_node):

    def __init__(self, next_node):
        super().__init__(next_node)
        # self.dir_path = r'D:\BaiduNetdiskDownload\huggingface\gpt2-chinese-poem'
        # self.dir_path = r'D:\python\nlp_chat_robot\models\model_file\gpt2-chinese-poem'
        self.dir_path = config.poem_gen_node_dir_path
        self.tokenizer = BertTokenizer.from_pretrained(self.dir_path)
        self.model = TFGPT2LMHeadModel.from_pretrained(self.dir_path)

        self.text_generator = TextGenerationPipeline(self.model, self.tokenizer)

    def get_response(self, raw_msg, res_dict):
        '''
        :param raw_msg: we recommend the raw_msg is 'ABCDE'
        :param res_dict:
        :return: None
        '''
        raw_list = list(raw_msg)
        if '，' not in raw_list and ',' not in raw_list:
            raw_list.append('，')
        processed_msg = ' '.join(raw_list)
        #If it processing successfully, raw_list is ['A','B',...,'，']
        #max_length = len(raw_msg)+generate_message
        #every sentence of the generate_msg is 8token
        num = len(raw_list)
        random_num = 8*3 if random.random()<0.8 else 8*7
        total_num = num + random_num

        msg = self.text_generator(processed_msg, max_length=total_num, do_sample=True)[0]['generated_text']
        res_dict['msg'] = msg

if __name__ == '__main__':
    import  os
    print(os.getcwd())