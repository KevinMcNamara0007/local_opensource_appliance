from modelthreads.modelthread import ModelThread

#  -------------------> Passthrough <-------------------
# Input gguf path and sample_question
#
path = r"C:\Users\TONY STARK\Desktop\Aplliance_stuff\local_opensource_appliance\model_files\mistral-7b-instruct-v0.1.Q2_K.gguf"
sample_question = "What is the distance between sun and moon?"

# --------------------------------------------------------

try:
    obj = ModelThread("test", path)
    print("[Load Success] ModelThread Loaded")
    res = obj.chat_completions(sample_question)
    print("[Response Success] Received Response from Model")
    print("<=== Chat ===>")
    print(" | Question | ".center(30, "-"))
    print(sample_question)
    print(" | Model Reponse | ".center(30, "-"))
    print(res)

except Exception as e:
    print(e)
