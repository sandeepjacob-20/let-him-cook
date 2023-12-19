import google.generativeai as genai
import os
import time

module_st = time.time()
# Load the JSON file
# with open("config.json") as f:
#     data = json.load(f)
# GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

# Configure the API key
genai.configure(api_key="AIzaSyCLWXaRPPyyzLuzUYrtGGyjEQ_rMWOaTMk")

# Create the model
model = genai.GenerativeModel('gemini-pro-vision')

def generate_recipe(img):
  prompt_st = time.time()
  response = model.generate_content(['''what is this and generate the recipe to cook it ? and 
                                     if it is not food then give an error message
                                     ''',img],stream=True)
  response.resolve()
  prompt_et = time.time()

  with open("log.txt","a") as f:
    f.write("---NEW LOG---\n")
    f.write("Prompt Generation Time: "+str(prompt_et-prompt_st)+" seconds\n")
    f.write("Module Loading Time: "+str(prompt_st-module_st)+" seconds\n")
    f.write("Total Time: "+str(prompt_et-module_st)+" seconds\n")

  result = {}
  result["recipe"] = response.text
  result["prompt_generation_time"] = prompt_et-prompt_st
  return result