import os
import csv
import openai
import time
import sys
import pandas as pd

#################### Set model
model = sys.argv[1]

if model != "gpt35" and model != "gpt4":
    print("Model can be either gpt35 or gpt4")
    assert False

#################### Set paths

print("Please enter your OpenAI API key")
openai_key = input()
print("Please enter your root path")
root_path = input()

prompt_folder = root_path + "/Prompts"
systemMsg_path = prompt_folder + "/JailbreakPrompts.csv"
userMsg_path = prompt_folder + "/MaliciousQueries.csv"

# https://platform.openai.com/docs/models/gpt-3-5
if model == "gpt35":
    response_path = root_path + "/Response/ChatGPT/gpt35"
    model_API = "gpt-3.5-turbo-0613"

# https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo
elif model == "gpt4":
    response_path = root_path + "/Response/ChatGPT/gpt4"
    model_API = "gpt-4-0613"

if not os.path.exists(response_path):
    os.makedirs(response_path)

#################### Set model configs
max_tokens = 1600
os.environ["OPENAI_API_KEY"] = openai_key
openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_five(systemMsg, userMsg, max_tokens, model_API, response_folder):
    
    messages = [{"role": "system", "content": systemMsg},
                {"role": "user", "content": userMsg}]
    
    received = False
    
    prompt = systemMsg + userMsg
    
    while not received:
        try:
            response = openai.ChatCompletion.create(
                model=model_API,
                messages=messages,
                max_tokens=max_tokens,
                n=5,
                top_p=0.95)
            received=True
            
            for i in range(5):    
                with open(response_folder + "/" + str(i) + ".txt", "w") as text_file:
                    text_file.write(response["choices"][i]["message"]['content'])            

        except:
            error = sys.exc_info()[0]
            if error == openai.error.InvalidRequestError: # something is wrong: e.g. prompt too long
                print(f"InvalidRequestError\nPrompt passed in:\n\n{prompt}\n\n")
                assert False
            print("API error:", error)
            time.sleep(1)

#################### Customizable sampled generation

userMsg_data = pd.read_csv(userMsg_path)
userMsg_data = userMsg_data.reset_index()
n=4
samples = userMsg_data.groupby(userMsg_data.columns[2]).apply(lambda x: x.sample(n)).reset_index(drop=True)
userMsg_data_sample = samples.values.tolist()

with open(systemMsg_path, newline='') as csvfile:
    # Loop through each row in the csv file
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    
    for systemMsg_index, row in enumerate(reader):
        s_category = row[0]
        systemMsg = row[1]
                
        # Correctly format the target string to include an underscore for precise matching
        target_prefix = f"{str(systemMsg_index).zfill(2)}_{s_category.replace(' ', '')}"

        # List directory contents and filter based on the exact match at the beginning of the name
        matching_folders = [name for name in os.listdir(response_path) if name.startswith(target_prefix)]

        # Cound the number of folders
        # If this number equals to the sample numer n multiplied by the number of userMsg types, skip
        if len(matching_folders) == n*6:   
            print(str(systemMsg_index).zfill(2) + "_" + s_category.replace(" ", ""), "already complete.")
            continue

        if systemMsg[-1] != " ":
            systemMsg += " "
        
        for userMsg_index, row2 in enumerate(userMsg_data_sample):
            
            u_category = row2[2]
            userMsg = row2[3]
            userMsg_index = row2[0]
            
            response_folder = response_path + "/" + str(systemMsg_index).zfill(2) + "_" + s_category.replace(" ", "") + "_" + str(userMsg_index).zfill(2) + "_" + u_category.replace(" ", "")           
            if not os.path.exists(response_folder):
                os.makedirs(response_folder)
            
            # If the folder exists and it contains 5 files ending with ".txt", skip
            if len(os.listdir(response_folder)) >= 5:
                print(response_folder, "already complete.")
                continue
                          
            chat_five(systemMsg, userMsg, max_tokens, model_API, response_folder)
            
            # Print the response filder complete message
            print(response_folder, "results written complete.")
            
        systemMsg_index += 1
