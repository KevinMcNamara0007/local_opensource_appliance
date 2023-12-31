from enum import Enum


class MessageStore(Enum):
    MODEL_NOT_SET = '''
            You don't seem to have a preferred model.
            Choose one by typing :
            !MODEL <Your_Preferred_Model>
            
            Available Models: {}
            '''
    MODEL_PARSE_ERROR = '''
            Unable to parse you preferred model. Please try again.
            Available Models: {}
            Type:!MODEL <Your_Preferred_Model>
            '''

    MODEL_SET_SUCCESS = '''
            [SUCCESS] Preferred Model Set to {}
            '''

    MODEL_SET_FAIL = '''
            [FAILED] Preferred Model Set to {}
            '''
