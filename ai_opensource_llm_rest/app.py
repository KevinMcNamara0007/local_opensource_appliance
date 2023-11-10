from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from llama_cpp import Llama

# Model paths
model_paths = [
    "/Users/loki/Desktop/worksurface/ai_lab/models/mistral_quantized/mistral-7b-instruct-v0.1.Q2_K.gguf",
    "/Users/loki/Desktop/worksurface/ai_lab/models/zephyr_quantized/zephyr-7b-alpha.Q2_K.gguf",
    "/Users/loki/Desktop/worksurface/ai_lab/models/zephyr_quantized/zephyr-7b-alpha.Q2_K.gguf",
]

# Create a list of LLMs
llms = []
for model_path in model_paths:
    llm = Llama(
        model_path=model_path,
        n_ctx=8192,
        n_batch=512,
        n_threads=7,
        n_gpu_layers=2,
        verbose=True,
        seed=42,
    )
    llms.append(llm)

# Create a Flask app
app = Flask(__name__)
api = Api(app)
CORS(app)  # Enable CORS for the API

# Create a namespace for the API
ns = api.namespace('mistral', description='Text conv with mistral')

@ns.route('/process_message', methods=['POST'])
class ProcessMessage(Resource):
    @ns.doc(params={'message': 'Text to be passed to model', 'model': 'Model number'})
    #@api.expect(input_model, validate=True)
    def post(self):
        # Parse the input data
        #data = request.json
        message = request.args.get('message', request.form.get('message', ''))
        model = request.args.get('model', request.form.get('model', '0'))
        print("request form -------->", request)
        print("I am printing this guy --------> ", message, model)

        # Select an LLM
        llm = llms[int(model)]

        # Generate a response
        output = llm(message, echo=True, stream=False, max_tokens=4096)
        print(f"-------- output from mistral: {output['choices'][0]['text']} -------")

        return {
            "result": output['choices'][0]['text']
        }


# Start the API server
if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
