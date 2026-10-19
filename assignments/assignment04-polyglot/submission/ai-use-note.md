# AI-use note

I used AI to explain the pandas equivalents of my R dplyr steps (dropna, groupby, sort_values, and as_index=False), and to help write and fix syntax and indentation errors in summarize_mean_sd helper in helpers.py.

I verified the translation by comparing R and Python at each step: raw row count, column count, filtered row count, number of groups. group labels, and rounded mean and SD of BMI. All matched. When R displayed fewer decimal placed, I printed the stored values to confirm they matched instead of changing the R code. 