from typing import Tuple, Optional, List


class UserThread:
    """
    Low Level Manager Component for every User Connection.

    Attributes:
        _identifier(Tuple[str, int])    : Identifier for every Connection
        _chat_model_name(str)           : Preferred Model Name Connection
        _chat_list(list[str])           : Chat History for Current Connection
    """

    def __init__(self, identifier: Tuple[str, int]):
        self._identifier = identifier
        self._chat_model_name: Optional[str] = None
        self._chat_list: List[str] = []
        self.chat_terms: dict = {
            "User": "Question",
            "Agent": "Answer"
        }

    @property
    def identifier(self) -> Tuple[str, int]:
        """
        Getter method for user identifier
        :return: Tuple of identifier . Default (User_Address , User_Port)
        """
        return self._identifier

    @property
    def chat_model_name(self) -> Optional[str]:
        """
        Getter method for User Preferred Model Name
        :return: Model Name String
        """
        return self._chat_model_name

    @chat_model_name.setter
    def chat_model_name(self, preferred_model_name) -> None:
        """
        Setter method for Chat Model Name
        :param preferred_model_name: preferred model name to set
        :return: None
        """
        if not (isinstance(preferred_model_name, str)):
            raise TypeError('Preferred Model Name should be string')
        else:
            self._chat_model_name = preferred_model_name

    @property
    def chat_list(self) -> Optional[List[str]]:
        """
        Chat History for Current Connection
        :return: List of each chat
        """
        return self._chat_list

    def append_chat_list(self, text: str, msg_type: str) -> bool:
        """
        Append a new chat to existing chat history.
        :param text: new chat to append
        :param msg_type: Type of chat
        :return: True if append successful,False otherwise
        """
        try:
            formatted = f"{self.chat_terms[msg_type]}: {text}"
            self._chat_list.append(formatted)
            return True
        except Exception as e:
            print("[Exception] Occurred")
            print(e)
            return False

    def user_message_with_chat_history(self, message: str):
        current_history = self._chat_list[:]
        formatted = f'{self.chat_terms.get("User")}: {message}'
        current_history.append(formatted)
        formatted = f'{self.chat_terms.get("Agent")}: '
        current_history.append(formatted)
        result = "\n".join(current_history)
        return result

    def clear_chat(self):
        self._chat_list.clear()

    def __str__(self):
        """
        A String representation of UserThread for Logging if required
        :return: a string representation of UserThread object
        """
        ans = [
            ' User Details '.center(35, '-'),
            self._identifier[0],
            str(self._identifier[1]),
            self._chat_model_name,
            *self._chat_list,
            ''.center(35, '-')
        ]
        return '\n'.join(ans)
