import argparse
import json
from typing import Optional

class JetParse:
    """
    JetParse Chat Conversation Parser

    This class is used to parse chat conversation input strings.

    Attributes:
        input_string (str): The input string to be parsed.
        flags (dict): A dictionary to store parsed flags and their values.
    """

    def __init__(self, chat_string: Optional[str]) -> None:
        """
        Initialize the JetParse object.

        Args:
            chat_string (str): The input string to be parsed.
        """
        self.input_string = chat_string
        self.flags = {}

        # Check if the string is valid
        if not self._is_valid_string():
            raise ValueError("Invalid input string")

        # Parse the input string using argparse
        try:
            self._parse_string()
        except argparse.ArgumentError as e:
            raise ValueError(f"Error parsing input string: {e}")

    def _is_valid_string(self) -> bool:
        """
        Check if the input string is valid.

        Returns:
            bool: True if the input string is valid, False otherwise.
        """
        return bool(self.input_string)

    def _parse_string(self) -> None:
        """
        Parse the input string using argparse and store the flags and their values.
        """
        parser = argparse.ArgumentParser()

        # Add custom flags
        parser.add_argument('--flag', type=str, help='Example flag with a value')
        parser.add_argument('-g', '--another-flag', action='store_true', help='some flag')
        parser.add_argument('-k', '--dict-flag', type=json.loads, help='Flag with a dictionary value')

        # Add the --help flag
        parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                            help='Show this help message and exit')

        # Parse the input string
        args = parser.parse_args(self.input_string.split())

        # Store parsed flags and values
        self.flags = {key: value for key, value in vars(args).items() if value is not None}

    def get_flags(self) -> dict:
        """
        Get the parsed flags and their values.

        Returns:
            dict: A dictionary containing parsed flags and their values.
        """
        return self.flags

    @classmethod
    def print_help(cls) -> None:
        """
        Print help information.
        """
        parser = argparse.ArgumentParser()

        # Add custom flags for help message
        parser.add_argument('--flag', type=str, help='Example flag with a value')
        parser.add_argument('-g', '--another-flag', action='store_true', help='Another example flag without a value')
        parser.add_argument('-k', '--dict-flag', type=json.loads, help='Flag with a dictionary value')

        # Automatically generate help message
        help_info = parser.format_help()
        print(help_info)


# Example Usage:
try:
    input_string = "--flag value -g -k {'key': 'value'}"
    jet_parser = JetParse(input_string)
    print("Flags:", jet_parser.get_flags())
except ValueError as e:
    print(f"Error: {e}")
