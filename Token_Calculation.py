import nltk
import pandas as pd
from nltk.tokenize import word_tokenize

nltk.download('punkt')


# Calculate the token and word number of jailbreak prompts
data_jailbreakprompts = pd.read_excel("JailbreakPrompts.xlsx")
results_jailbreakprompts = []

categories = list(data_jailbreakprompts['Category'].unique()) + ["Overall"]
for category in categories:
    if category == "Overall":
        subset = data_jailbreakprompts
    else:
        subset = data_jailbreakprompts[data_jailbreakprompts['Category'] == category]
    
    word_counts = subset['Prompt'].apply(lambda x: len(x.split()))
    mean_word_count = word_counts.mean()
    std_word_count = word_counts.std()
    
    token_counts = subset['Prompt'].apply(lambda x: len(word_tokenize(x)))
    mean_token_count = token_counts.mean()
    std_token_count = token_counts.std()

    num_prompts = len(subset)
    
    results_jailbreakprompts.append({
        "Category": category,
        "Mean Word Count": mean_word_count,
        "Std Word Count": std_word_count,
        "Mean Token Count": mean_token_count,
        "Std Token Count": std_token_count,
        "Number of Prompts": num_prompts
    })

# Write the results of jailbreak prompts into a excel
results_df = pd.DataFrame(results_jailbreakprompts)
results_df.to_excel("JailbreakPrompts_TokenCount.xlsx", index=False)


# Calculate the token and word number of malicious queries
data_maliciousqueries = pd.read_excel("MaliciousQueries.xlsx")
results_maliciousqueries = []

categories = list(data_maliciousqueries['Category'].unique()) + ["Overall"]
for category in categories:
    if category == "Overall":
        subset = data_maliciousqueries
    else:
        subset = data_maliciousqueries[data_maliciousqueries['Category'] == category]
    
    word_counts = subset['Question'].apply(lambda x: len(x.split()))
    mean_word_count = word_counts.mean()
    std_word_count = word_counts.std()
    
    token_counts = subset['Question'].apply(lambda x: len(word_tokenize(x)))
    mean_token_count = token_counts.mean()
    std_token_count = token_counts.std()

    num_prompts = len(subset)
    
    results_maliciousqueries.append({
        "Category": category,
        "Mean Word Count": mean_word_count,
        "Std Word Count": std_word_count,
        "Mean Token Count": mean_token_count,
        "Std Token Count": std_token_count,
        "Number of Prompts": num_prompts
    })

# Write the results of malicious queries into a excel
results_df = pd.DataFrame(results_maliciousqueries)
results_df.to_excel("MaliciousQueries_TokenCount.xlsx", index=False)

