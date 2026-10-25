# Visual Audit Note

## Plot Question

What is the mean BMI of adults age 20-80 by income group through NHANES cycles?

## Issues Checked

| Issue | Category | Why it matters | Correction |
|---|---|---|---|
| Caption asserts a causal claim that low income is a cause of obesity | Interpretation | The claim being made by the plot is not supported by the data that is shown. It is overstating the influence of income on BMI that is available from the data, and thus miscontrues and misrepresents the data to those who see this graph. | Rewrite the caption to not make the claim that low-income has a casual relationship with higher BMI and include that the summary is unweighted and can't be used as a population estimate. |
| Y-axis scale only spans from 24-28 BMI points | Design | The exaggeration of differences in BMI between income groups and cycles misrepresents the actual trend. | Expand the scale to show values beginning at 0 to show a more accurate representation of the variation/trend in BMI between income groups and cycles. |
| Title claims that the plot is consists of BMI data of 20-80 year olds from nhanes from each cycle from 1999-2023 | Correctness | The data shown by the plot does not represent the subset that the title defines, as not all the nhanes cycles for which the data is avilable between the time periods shown are shown and the filtering for adults between the ages of 20-80 was not done so the BMI of younger and older people is also included. This inclusion can skew the data and result in misrepresentation of the age groups and the omitting of cycles in between does not show the actual trend in BMI values cycle to cycle. | Rewrite the code to correctly include all the nhanes cycles between the 1999-2000 and 2022-2023 periods that have sufficient data and add a filtering step to only include data from those between ages 20-80. |

## Final Caption

This figure shows BMI by Income Group across NHANES cycles using the prepared NHANES Health Equity classroom dataset. The summary is descriptive and unweighted. Records with missing BMI, Income Group, or Cycle  and groups with less than 30 records were excluded. The plot supports comparison of patterns, not causal claims or population-level estimates.

## AI-Use Check

AI was not used.
