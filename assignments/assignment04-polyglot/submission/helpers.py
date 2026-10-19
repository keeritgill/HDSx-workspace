import pandas as pd

def summarize_mean_sd(data, value, group1, group2):
    """
    Returns the n, mean, and standard deviation of a value in a dataset, grouped by two columns.
    Drops rows missing any of the three columns, sorts by the groups, and rounds mean and SD to 2 decimals. 
    Python version of the R function summarise_mean_sd().
    """
    result = (
        data
        .dropna(subset=[value, group1, group2])
        .groupby([group1, group2], as_index=False)
        .agg
            (n=(value, 'count'), 
             mean_value =(value, 'mean'), 
             sd_value =(value, 'std')
        )
        .sort_values([group1, group2])
    )

    result["mean_value"] = result["mean_value"].round(2)
    result["sd_value"] = result["sd_value"].round(2)
    return result

   