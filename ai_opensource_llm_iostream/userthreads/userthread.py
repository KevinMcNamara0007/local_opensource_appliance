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

    def append_chat_list(self, text: str) -> bool:
        """
        Append a new chat to existing chat history.
        :param text: new chat to append
        :return: True if append successful,False otherwise
        """
        try:
            self._chat_list.append(text)
            return True
        except Exception as e:
            print("[Exception] Occurred")
            print(e)
            return False

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
