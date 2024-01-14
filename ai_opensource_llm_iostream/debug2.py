from modelthreads.modelthread import ModelThread
from dotenv import find_dotenv, dotenv_values

obj = ModelThread("test",
                  r"C:\Users\TONY STARK\Desktop\Aplliance_stuff\local_opensource_appliance\model_files\mistral-7b-instruct-v0.1.Q2_K.gguf")
print("Loaded ModelThread")
res = obj.chat_completions("What is the distance between sun and moon?")
print(res)

