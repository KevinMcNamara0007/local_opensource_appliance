import json
import requests
from llama_cpp import Llama
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_swagger_ui import get_swaggerui_blueprint
from flask_restx import Api, Resource, fields
from flask_cors import CORS

# Instruction model
model = "/Users/loki/Desktop/worksurface/ai_lab/models/mistral_quantized/mistral-7b-instruct-v0.1.Q2_K.gguf"
#model = "/Users/loki/Desktop/worksurface/ai_lab/models/zephyr_quantized/zephyr-7b-alpha.Q2_K.gguf"

app = Flask(__name__)
api = Api(app)
api = CORS(app)

# Enable Cross-Origin Resource Sharing (CORS) for all routes and origins.
#CORS(app, resources={r"/*": {"origins": "*"}})

ns = api.namespace("mistral", description="mistralAI")

message_model = api.model("Message", {'message': fields.String(description="Input message")})

processed_model = api.model("ProcessedMessage", {"result": fields.String(description="Mistral output")})

llm = Llama(
    model_path=model,
    n_ctx=8192,
    n_batch=512,
    n_threads=7,
    n_gpu_layers=2,
    verbose=True,
    seed=42,
)

@app.route('/')
def index():
    return render_template("index.html")

@ns.route("/process_message")
class Generate(Resource):
    @api.expect(message_model)
    @api.marshal_with(processed_model)
    def post(self):
        message = request.json["message"]
        output = llm(message, echo=True, stream=False, max_tokens=4096)
        print(f"-------- output from mistral: {output['choices'][0]['text']} -------")

        return {
            "result": output['choices'][0]['text']
        }

# Start the API server
if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
