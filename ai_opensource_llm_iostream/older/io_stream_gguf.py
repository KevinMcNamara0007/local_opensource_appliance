import io
import json
import numpy as np
import requests
import pickle

with open(model_weight_path, 'rb') as file:
    pickled_data = pickle.load(file)


class MiSTralChatInterface:
    def __init__(self, model_weight_path):
        self.model = np.load(model_weight_path, allow_pickle=True)[0]
        self.model = pickled_data[0]

    def generate_response(self, prompt):
        """Generates a response to a prompt using the MiSTral model."""

        # Encode the prompt as a NumPy array.
        prompt_encoded = np.array([prompt])

        # Generate the response.
        response_encoded = self.model.predict(prompt_encoded)

        # Decode the response from a NumPy array to text.
        response = response_encoded[0]

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
    # Get the path to the MiSTral model weight.
    model_weight_path = "/Users/loki/Desktop/worksurface/ai_lab/models/mistral_quantized/mistral-7b-instruct-v0.1.Q2_K.gguf"

    # Create a MiSTralChatInterface object.
    chat_interface = MiSTralChatInterface(model_weight_path)

    # Start the chat loop.
    chat_interface.chat(io.StringIO())
