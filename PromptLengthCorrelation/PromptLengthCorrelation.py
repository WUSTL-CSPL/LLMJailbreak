import numpy as np
import pandas as pd
import scipy.stats as stats

df = pd.read_excel('EfficacyPromptLength.xlsx')

pearson_corr, pearson_pval = stats.pearsonr(df['Token Length'], df['mean_jsr'])
spearman_corr, spearman_pval = stats.spearmanr(df['Token Length'], df['mean_jsr'])
kendall_corr, kendall_pval = stats.kendalltau(df['Token Length'], df['mean_jsr'])

print("The Pearson test on the correlation between the prompt lengths and JSR produced a correlation coefficient of", pearson_corr, ", with a p-value of", pearson_pval)
print("The Spearman test on the correlation between the prompt lengths and JSR produced a correlation coefficient of", spearman_corr, ", with a p-value of", spearman_pval)
print("The Kendall test on the correlation between the prompt lengths and JSR produced a correlation coefficient of", kendall_corr, ", with a p-value of", kendall_pval)

pearson_corr2, pearson_pval2 = stats.pearsonr(df['Token Length'], df['mean_emh'])
spearman_corr2, spearman_pval2 = stats.spearmanr(df['Token Length'], df['mean_emh'])
kendall_corr2, kendall_pval2 = stats.kendalltau(df['Token Length'], df['mean_emh'])

print("The Pearson test on the correlation between the prompt lengths and EMH produced a correlation coefficient of", pearson_corr2, ", with a p-value of", pearson_pval2)
print("The Spearman test on the correlation between the prompt lengths and EMH produced a correlation coefficient of", spearman_corr2, ", with a p-value of", spearman_pval2)
print("The Kendall test on the correlation between the prompt lengths and EMH produced a correlation coefficient of", kendall_corr2, ", with a p-value of", kendall_pval2)
