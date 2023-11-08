import json
import requests
from llama_cpp import Llama
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_swagger_ui import get_swaggerui_blueprint
from flask_restx import Api, Resource, fields
from flask_cors import CORS

# Instruction model
model_mistralAI1_gguf = "C:/Users/Vamshi Krishna Gundu/Desktop/Vamshi/LnD/Data_Science/Projects/llm_models/mistral-7b-instruct-v0.1.Q2_K.gguf"
model_mistralAI2_gguf = "C:/Users/Vamshi Krishna Gundu/Desktop/Vamshi/LnD/Data_Science/Projects/llm_models/mistral-7b-instruct-v0.1.Q2_K.gguf"
#model = "/Users/loki/Desktop/worksurface/ai_lab/models/zephyr_quantized/zephyr-7b-alpha.Q2_K.gguf"

llm_mistralAI1 = Llama(
    model_path=model_mistralAI1_gguf,
    n_ctx=8192,
    n_batch=512,
    n_threads=7,
    n_gpu_layers=2,
    verbose=True,
    seed=42,
)


llm_mistralAI2 = Llama(
    model_path=model_mistralAI2_gguf,
    n_ctx=8192,
    n_batch=512,
    n_threads=7,
    n_gpu_layers=2,
    verbose=True,
    seed=42,
)

app = Flask(__name__)
api = Api(app)
CORS(app)  # Enable CORS for the API

# Create a namespace for the API
ns = api.namespace('mistral', description='Text conv with mistral')

# Define a model for the input data
input_model = api.model('InputModel', {'message': fields.String(description='Text to be passed to model')})

@ns.route('/mistralAI1/process_message')
class Model1ProcessMessage(Resource):
    @api.expect(input_model, validate=True)
    def post(self):
        # Parse the input data
        data = request.json
        message = data.get('message', '')
        
        output = llm_mistralAI1(message, echo=True, stream=False, max_tokens=4096)
        print(f"-------- output from mistral: {output['choices'][0]['text']} -------")

        return {
            "result": output['choices'][0]['text']
        }
    

@ns.route('/mistralAI2/process_message')
class Model2ProcessMessage(Resource):
    @api.expect(input_model, validate=True)
    def post(self):
        # Parse the input data
        data = request.json
        message = data.get('message', '')
        
        output = llm_mistralAI2(message, echo=True, stream=False, max_tokens=4096)
        print(f"-------- output from mistral: {output['choices'][0]['text']} -------")

        return {
            "result": output['choices'][0]['text']
        }
    

# Start the API server
if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
