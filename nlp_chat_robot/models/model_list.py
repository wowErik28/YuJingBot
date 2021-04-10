from nlp_chat_robot.models.model_node import *

'''
We use strategy pattern here.
'''
class base_model_list(base_node):

    def __init__(self, head_node, next_node=None,name=None):
        super().__init__(next_node,name)
        self.head_node = head_node

    def _process_node_list(self, node_list):
        head_node = None
        current_node = None
        for node in node_list:
            if head_node is None:
                #the first node
                current_node = node
                head_node = node
            else:
                current_node.set_next(node)
                current_node = node
        return head_node

    def add_node(self, node):
        last_node = self._get_last_node()
        last_node.set_next(node)

    def _get_last_node(self):
        current_node = self.head_node
        if current_node is None:
            return None
        while 1:
             if current_node.get_next() is None:
                break
             else:
                 current_node = current_node.get_next()
        return current_node

    def remove_node(self, idx):
        #remove the head_node
        if idx ==0:
            self.head_node = self.head_node.get_next() if self.head_node is not None else None
            return self.head_node
        pre_node = self.head_node
        pre_node_idx = 0
        #if pre_node is None, then it is the last one
        while pre_node_idx < idx-1 and pre_node is not None:
            pre_node = pre_node.get_next()
            pre_node_idx +=1
        #pre_node_idx = idx-1
        if pre_node is None:
            return None
        if pre_node.get_next() is None:
            return None

        current_node = pre_node.get_next()
        temp_node = current_node.get_next()
        pre_node.set_next(temp_node)
        return current_node


    def __len__(self):
        current_node = self.head_node
        if current_node is None:
            return 0
        count = 1
        while 1:
            if current_node.get_next() is None:
                break
            else:
                current_node = current_node.get_next()
                count +=1
        return count

    def get_response(self, raw_msg, res_dict):
        current_node = self.head_node

        while current_node is not None:
            current_node.get_response(raw_msg,res_dict)
            current_node = current_node.get_next()

def get_eng_emotion_model_list(name=None):
    node = emotion_cls_node(None)
    head_node = eng_gen_node(node)
    model_list = base_model_list(head_node,name=name)
    return model_list

def get_poem_model_list(name=None):
    node = random_emotion_cls_node(None, int_range_list=['POSITIVE','NEGTIVE'])
    head_node = poem_gen_node(node)
    model_list = base_model_list(head_node,name=name)
    return model_list

if __name__ == '__main__':
    import pyttsx3
    import ffmpeg

    # file_name = '2.mp3'
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)
    node = emotion_cls_node(None)
    head_node = eng_gen_node(node)
    model_list = base_model_list(head_node)
    while 1:
        raw_msg = input('You:')

        res_dict = {}
        model_list.get_response(raw_msg, res_dict)

        msg = res_dict['msg']
        print('Bot: ',msg)
        engine.say(msg)
        engine.runAndWait()

    #
    # model_list = get_poem_model_list('poem')
    # raw_msg = '振东天天想语凭'
    # i = 0
    #
    # while 1:
    #     raw_msg = input('You:')
    #     file_name ='{}.mp3'.format(i)
    #     res_dict = {}
    #     model_list.get_response(raw_msg, res_dict)
    #
    #     msg = res_dict['msg']
    #
    #     engine.say(msg)
    #     engine.runAndWait()
    #     engine.save_to_file(msg,file_name)
    #     i+=1