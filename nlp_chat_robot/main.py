from nlp_chat_robot.robot.robot import get_response

if __name__ == '__main__':
    # import warnings
    #
    # warnings.filterwarnings("ignore")
    # import pyttsx3
    # import ffmpeg
    #
    # # file_name = '2.mp3'
    # engine = pyttsx3.init()
    # while 1:
    #     raw_msg = input('You:')
    #     res_dict = get_response(raw_msg)
    #     print('Robot', res_dict['msg'])
    #     engine.say(res_dict['msg'])
    #     engine.runAndWait()
    while 1:
        raw_msg = input('You:')
        res_dict = get_response(raw_msg)
        print('Robot', res_dict['msg'])