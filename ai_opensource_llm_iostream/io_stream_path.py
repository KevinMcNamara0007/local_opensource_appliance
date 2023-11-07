import io
import json
import numpy as np
import requests
import path

class PathChatInterface:
    def __init__(self, model_weight_path):
        self.model = path.load_model(model_weight_path)

    def generate_response(self, prompt):
        """Generates a response to a prompt using the Path model."""

        # Encode the prompt as a NumPy array.
        prompt_encoded = np.array([path.encode_text(prompt)])

        # Generate the response.
        response_encoded = self.model.generate(prompt_encoded)

        # Decode the response from a NumPy array to text.
        response = path.decode_text(response_encoded[0])

        return response

    def chat(self, io_stream):
        """Chats with the user via the given io stream."""

        while True:
            # Get the user's input.
            user_input = io_stream.readline().strip()

            # If the user wants to quit, exit the chat loop.
            if user_input == '/quit':
                break

            # Generate the response to the user's input.
            response = self.generate_response(user_input)

            # Write the response to the io stream.
            io_stream.write(response + '\n')

if __name__ == '__main__':
    # Get the path to the Path model weight.
    model_weight_path = '/Users/loki/Desktop/worksurface/ai_lab/models/mistral_quantized/mistral-7b-instruct-v0.1.Q2_K.gguf'

    # Create a PathChatInterface object.
    chat_interface = PathChatInterface(model_weight_path)

    # Start the chat loop.
    chat_interface.chat(io.StringIO())
