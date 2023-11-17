import io
import numpy as np
import pickle

def custom_persistent_load(file_path):
    # Load the model from the file.
    with open(file_path, "rb") as file:
        model = pickle.load(file)
    # Do any necessary post-loading processing.
    return model

class BinChatInterface:
    def __init__(self, model_weight_path, persistent_load_func=None):
        self.model = None
        self.model_weight_path = model_weight_path
        self.persistent_load_func = persistent_load_func

    def load_model(self):
        if self.persistent_load_func:
            self.model = self.persistent_load_func(self.model_weight_path)
        else:
            with open(self.model_weight_path, "rb") as f:
                self.model = pickle.load(f)

    def generate_response(self, prompt):
        """Generates a response to a prompt using the Bin model."""

        # Load the model if it is not already loaded.
        if self.model is None:
            self.load_model()

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
    # Get the path to the .bin model weight.
    model_weight_path = '/Users/loki/Desktop/worksurface/ai_lab/models/mistral_unquantized/pytorch_model-00001-of-00002.bin'

    # Create a BinChatInterface object.
    chat_interface = BinChatInterface(model_weight_path, custom_persistent_load)

    # Start the chat loop.
    chat_interface.chat(io.StringIO())
