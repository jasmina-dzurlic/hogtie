
# An example of using a random numpy array and visualize results using 
# toyplot as a test dataset for visualizing regions on HGT. 

import numpy as np
import pandas as pd
import toyplot
from scipy import stats


# Create test dataset

data = np.random.uniform(low=0.0, high=1.0, size=1000)

df = pd.DataFrame(data)

df['rollingmean']=df.rolling(50,win_type='triang').mean()


# Compute rolling mean as 'z_score'

df['z_score']=stats.zscore(df['rollingmean'],nan_policy='omit')

scores = list(df['z_score'])


def def_see_genome_(data):
    """"
     Likelihood scores in a pandas dataframe are computed as a 
    rolling window mean of likelihoods then plotted along
    linear genome. 

    """
    data['rollingmean']=data.rolling(50,win_type='triang').mean()
    data['z_score']=stats.zscore(data['rollingav'],nan_policy='omit')
    
    plot = toyplot.plot(
        data['rollingav'],
        width = 500,
        height=500,
        color = numpy.random.random(series.shape),
        palette = toyplot.color.brewer.map("Oranges"),
        size = [16, 9]

    );
    return plot


