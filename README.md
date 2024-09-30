# Jailbreak Prompts

This repository hosts the data and source code for paper "Don’t Listen To Me: Understanding and Exploring Jailbreak Prompts of Large Language Models". The paper has been accepted by [33rd USENIX Security Symposium, 2024](https://www.usenix.org/conference/usenixsecurity24).

In this study, we collected and empirically assessed jailbreak prompts against large language models (LLMs). The attacker's goal is to elicit harmful content (e.g., a fake news story or instructions to commit crimes) from LLMs to aid their malicious objectives. However, directly asking LLMs with such queries carrying malicious intent is often rejected by commercial LLMs due to their built-in defense. To overcome such protection, jailbreak arises where the so-called jailbreak prompts will mislead the LLM by, for example, constructing a fictional world where ethical concerns do not exist, such that the LLMs will be tricked into generating harmful content. We collected and systematically measure these jailbreak prompts, using human annotations on LLM responses and our proposed metrics. Details regarding this work can be found in the [Sec'24 paper](https://arxiv.org/abs/2403.17336).

# Hardware and Software Dependencies

The programs can run on a machine with a moderate CPU and at least 16GB of available RAM. No other specialized hardware is required for execution. The Python environment was set up using Miniconda 4.12.0 on Ubuntu 22.0.4. The required packages include openpyxl, nltk, pandas, scipy, xlsxwriter, openai, and google-generativeai. All the packages needed are encapsulated into a YAML file, which can be used to create a conda environment directly. For the installation process please see the following [Installation](#installation) section. 

# Installation

Conda or Miniconda is recommended for setting up the environment. It can be installed via the [official link](https://docs.conda.io/en/latest/miniconda.html) and the process can differ based on the user's OS. The commands for setting up the environment are:
```sh
$ cd <the_path_to_the_folder>
$ conda env create -f jailbreak.yml
$ conda activate jailbreak
```

Please find the supplementary files on the [Google Drive](https://drive.google.com/file/d/1tDYB_Z-L2hxSwUZZQM0oRf730seTbO_3/view?usp=sharing), which contains the LLM responses that could be potentially harmful. Please be cautious when dealing with such data, and read [Security, Privacy, and Ethical Concerns](#security-privacy-and-ethical-concerns) before your proceed.

Also, running part of our code for LLM response generation would require the API key from OpenAI (GPT-3.5 and GPT-4) and Google (PaLM-2). To apply for API keys, please direct to [OpenAI's](https://platform.openai.com/signup) and [Google's](https://ai.google.dev/tutorials/setup) official website. 

# Security, Privacy, and Ethical Concerns

Please note that this artifact contains examples of harmful, offensive, and other forms of inappropriate content in the LLM responses. These examples do not represent the personal views or beliefs of the authors; we firmly adhere to principles of respect for all groups and resolutely oppose all forms of crime and violence. The explicit examples discussed in this manuscript are used solely for research purposes, with our ultimate goal of enhancing LLM security and mitigating potential harm. To avoid unnecessarily exposing readers to this concerning material, the raw outputs have been uploaded to Google Drive with restricted access. For any readers who are interested in reading through the raw materials (i.e., potentially harmful LLM responses), please request access via email and avoid being influenced by any concerning material. 

# Basic Tests

The basic test can be run with the command:
```sh
$ python3 BasicTest.py
```

The test mainly calls the APIs for the three models, GPT-3.5, GPT-4, and PaLM-2. The query is "Hello I am doing a basic test of your functionality. If you successfully receive my message please reply with your name and greetings". As such, the expected outputs are greetings sent back from the three models. Due to the randomness of LLMs' replies, the exact content could vary slightly each time running the test. At the end, the terminal will print "Basic test passed!" if succeed.

# Experiments

1. The 448 jailbreak prompts are included in the *JailbreakPrompts.xlsx* file. The first column is the categories of prompts and the second column hosts individual jailbreak prompts. Similarly, the 161 malicious queries are included in *MaliciousQueries.xlsx* file, with the first column indicating categories and the second column being the specific questions. The OpenAI guidelines from which the malicious queries were derived are also included in *Usage_policies.html* file. The python script *Token_Calculation.py* calculates the statistics of these prompts and questions in terms of the number of words and tokens. To run it, please use command line:
```sh       
$ python3 Token_Calculation.py 
```

The statistical results of *Token_Calculation.py* will be written into two files, *JailbreakPrompts_TokenCount.xlsx* and *MaliciousQueries_TokenCount.xlsx* respectively. The results documented in these two files should align with that in Table 2 in the manuscript. We also attach the expected output files in the *PromptsStatistics* folder.

2. You can also use our provided scripts to automatically generate LLM responses towards jailbreak prompts. We provide two scripts for automatic generation on three models, GPT-3.5, GPT-4, and PaLM-2. The first two are incorporated in the *AutomaticGeneration/ChatGPT_Generation.py* script while PaLM-2 is in *AutomaticGeneration/PaLM2_Generation.py*. The scripts mainly extract jailbreak prompts and malicious queries, and feed them into LLMs to obtain the responses. The commands for GPT-3.5, GPT-4, and PaLM-2 are:
```sh   
$ cd AutomaticGeneration
$ python3 ChatGPT_Generation.py gpt35  
$ python3 ChatGPT_Generation.py gpt4 
$ python3 PaLM2_Generation.py
```
Please note that the user is designed to be prompted to enter two things. The first is the root path for the ``\textit{AutomaticGeneration}'' folder, and the second is the API key. Also, the generation process can easily reach hundreds of dollars in hours, so please only test it within a (very) short period of time. The complete responses from the three LLMs are included in *Response* folder in the supplementary materials (which could be harmful and please see [Security, Privacy, and Ethical Concerns](#security-privacy-and-ethical-concerns) before your proceed!). 

3. The human annotation on the LLM responses are included in *Labels_GPT35.xlsx*, *Labels_GPT4.xlsx*, and *Labels_PaLM2.xlsx* respectively. Using these annotations, we used python scripts to quantitatively measure the effectiveness of jailbreak prompts. First, we can run *JSR_EMH_Category.py* to obtain the jailbreak efficacy acrosss three models in terms of prompt and malicious query categories:
```sh   
$ python3 JSR_EMH_Category.py  
```
The expected results are two Excel files named *EMH_Category.xlsx* and *JSR_Category.xlsx*. Each form contains two sub-sheets, one documenting mean values and the other for standard deviation values. We also attach these expected output forms in *EMH_JSR_Category* folder. 


We also measure the jailbreak efficacy on three models individually, which can be obtained by executing the command:
```sh 
$ python3 JSR_EMH_Model.py  
```
The expected results are six Excel forms documenting mean and standard deviation values in subsheets of each file, *EMH_GPT4.xlsx*, *EMH_GPT35*, *EMH_PaLM2.xlsx*, *JSR_GPT4.xlsx*, *JSR_GPT35.xlsx*, and *JSR_PaLM2.xlsx*, which are named by the metrics (EMH or JSR) and models (GPT-3.5, GPT-4, or PaLM-2). We also attach the expected results in *EMH_JSR_Model* folder.

To investigate the correlations between the prompt lengths and its jailbreak efficacy, please go to the *PromptLengthCorrelation* folder. Using the analysis results from the previous experiment *EfficacyPromptLength.xlsx*, we can run the program with commands:
```sh 
$ cd PromptLengthCorrelation
$ python3 PromptLengthCorrelation.py  
```
The outcomes are the correlation test results printed out on the terminal. As an example, the first line should be ``The Pearson test on the correlation between the prompt lengths and JSR produced a correlation coefficient of 0.207445408829702, with a p-value of 9.565429118142019e-06''. 

Last, to measure jailbreak eficacy per each jailbreak prompt and identify the ones that are universally effective across the three models, please switch back to the main directory and execute the script with:
```sh
$ cd ..
$ python3 JSR_EMH_per_Prompt.py  
```
The expected outputs for the last experiment are two-fold. The first part consists of two Excel forms named *EMH_Prompts.xlsx* and *JSR_Prompts.xlsx*. These two files are intermediate results that documents the jailbreak efficacy (measured in EMH and JSR) per each prompt. These two files are also provided in the *EMH_JSR_Prompts* folder. Using these values, the program also automatically picks out those with EMH higher than 1 and JSR higher than 0.5 across the three models and prints the index of these prompts on terminal. The expected printed indexes are 8, 10, 103, and 138. Referred back to the *JailbreakPrompts.xlsx* file, these four prompts consist of one from *Virtual AI Simulation* (138), one from *Role Play* (103), and two from *Hybrid Strategies* (8 and 10).

# Citation

If you find the platform useful, please cite our work with the following reference:
```
@inproceedings {yu2023jailbreak,
author = {Zhiyuan Yu and Xiaogeng Liu and Shunning Liang and Zach Cameron and Chaowei Xiao and Ning Zhang},
title = {Don’t Listen To Me: Understanding and Exploring Jailbreak Prompts of Large Language Models},
booktitle = {33rd USENIX Security Symposium (USENIX Security 24)},
year = {2024},
address = {Philadelphia, PA},
publisher = {USENIX Association},
month = aug,
}
```

