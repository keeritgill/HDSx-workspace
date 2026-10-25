# Visual Audit Note

Issues

a) Interpretation - Caption asserts a causal claim that low income is a cause of obesity, despite this not being supported by the plot.

b) Design - Scale that spans 4 BMI points exaggerates the differences in BMI between the different income groups and cycles, creating a misleading comparsion.

c) Correctness - Title claims that the plot is consists of BMI data of 20-80 year olds from nhanes from each cycle from 1999-2023, however only the endpoint cycles (1999-2000, 2022-2023) are shown and all ages are shown becasue no age filtering was done

Significance

a) The claim being made by the plot is not supported by the data that is shown. It is overstating the influence of income on BMI that is available from the data, and thus miscontrues and misrepresents the data to those who see this graph.

b) The BMI scale is set to only show between 24 and 28, despite the possible range of values being much larger. The exaggeration of differences in BMI between income groupsand cycles misrepresents the true change observed.

c) The data that the title claims that the plot shows is false, as not all the nhanes cycles for which the data is avilable between the time periods shown are shown and the filtering for adults between the ages of 20-80 was not done so the BMI of younger and older people is also included. This inclusion can skew the data and result in misrepresentation of the age groups and the omitting of cycles in between does not show the actual trend in BMI values cycle to cycle.

Corrected approach

a) Rewrite the caption to not make the claim that low-income has a casual relationship with higher BMI and include that the summary is unweighted and can't be used as a population estimate.

b) Expand the scale to show values beginning at 0 to show a more accurate representation of the variation/trend in BMI between income groups and cycles.

c) Rewrite the code to correctly include all the nhanes cycles between the 1999-2000 and 2022-2023 periods and add a filtering step to only include data from those between ages 20-80.