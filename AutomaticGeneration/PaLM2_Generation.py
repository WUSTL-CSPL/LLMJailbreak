# https://ai.google.dev/api/python/google/generativeai/types/Completion

import os
import csv
import google.generativeai as palm
import time
import sys
import pandas as pd

#################### Set model

palm.configure(api_key=<Your API Key>)
models = [m for m in palm.list_models() if "generateText" in m.supported_generation_methods]
model = models[0].name

#################### Set paths
root_path = <Your Path>

prompt_folder = root_path + "/Prompts"
systemMsg_path = prompt_folder + "/JailbreakPrompts.csv"
userMsg_path = prompt_folder + "/MaliciousQueries.csv"

if model == "models/text-bison-001":
    response_path = root_path + "/Response/PaLM2/text-bison-001"

if not os.path.exists(response_path):
    os.makedirs(response_path)

#################### Set model configs

max_tokens = 2048

def palm2_five(systemMsg, userMsg, max_tokens, response_folder):

    received = False
    
    prompt = systemMsg + userMsg
    # print(userMsg)

    
    while not received:
        try:          
            response = palm.generate_text(
                model=model,
                prompt=prompt,
                candidate_count=5,
                # temperature=0,
                top_p=0.95,
                # The maximum length of the response
                max_output_tokens=max_tokens)
            # print(response)
            # exit()
            received=True
            
            for i in range(5):    
                with open(response_folder + "/" + str(i) + ".txt", "w") as text_file:
                    text_file.write(response.candidates[i]["output"])
        
        except Exception as e:
            # error = sys.exc_info()[0]
            # print("API error:", error)
            if "'NoneType' object has no attribute 'from_call'" in str(e):
                print("Error on the prompt:", prompt)
                print("Possibly due to language not supported, skip this prompt.")
                break
            else:
                print("An error occured but not empty response:", e)
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
                
        # Cound the number of folders
        # If this number equals to the sample numer n multiplied by the number of userMsg types, skip
        if len([name for name in os.listdir(response_path) if str(systemMsg_index).zfill(2) + "_" + s_category.replace(" ", "") in name]) == n*6:
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
                          
            palm2_five(systemMsg, userMsg, max_tokens, response_folder)
            
            # Print the response filder complete message, like "response_folder 00_..._00_... complete"
            print(response_folder, "results written complete.")
            
        systemMsg_index += 1
