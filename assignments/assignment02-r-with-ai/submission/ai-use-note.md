# AI-Use Note

## Audit trail
```{r}
# AI Prompt (Claude): I asked whether na.rm = TRUE in mean_with_n() 
#   was enough to handle missing values. Claude said yes (handles
#   missing BMI values) but suggested adding missing row summary to
#   see how many rows were excluded.
# Verified: Subtracted missing BMI rows from total rows and got 
#   same result as mean_with_n(nhanes$BMI); there were no missing
#   race values

# AI prompt (Claude): asked how to use mean_with_n() function inside the 
#   pipeline. Claude suggested calling it within summarise() - used below.
# Verified: checked what each line of code was passed and the output,
#   especially following through mean_with_n() argument in summarise().
# AI Prompt (Claude): I asked whether na.rm = TRUE in mean_with_n() 
#   was enough to handle missing values and replace filtering
#   step in pipe. Claude said it was for BMI, but not for Race, but to 
#   keep both filtering steps to be explicit about data filtering. 
# Verified: missing values chunk showed no missing Race values but many 
#   missing BMI values; kept filter in pipe to ensure data filtering
#   was explicit.
```


## What AI helped with
I used Claude to help me set up the submission folder in Codespaces, to explain
the starter code step by step, and debug my summary pipeline. Claude
suggested calling mean_with_n() inside summarise() and including the missing-values
chunk. Claude also helped draft this note. I asked GitHub Copilot Chat one question
about writing a function for BMI by race. 

## What I changed
I changed the summary from income group to race group by BMI. I also wrote the first
draft of the pipeline myself the used Clause to debug: missing bracket, group.by to group_by, 
fixed trying to call summary table as function. Copilot suggested a function with extra arguments
for the BMI and race columns, but it was too complicated for my understanding so I used
mean_with_n() instead. 

## How I verified the result
I checked that Race and BMI appeared in names(nhanes). I confirmed that 105626 total rows minus 9356 rows with missing BMI values equals the complete rows returned by mean_with_n(nhanes$BMI), which also confirmed that no rows were missing the Race value. I rendered the note and checked the output.