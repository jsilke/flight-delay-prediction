[![Lifecycle](https://img.shields.io/badge/Lifecycle-Experimental-orange.svg)](https://www.tidyverse.org/lifecycle/#experimental)
# Flight Delay Prediction

Our objective is to predict arrival delays of commercial flights. According to the [US Department of Transportation](https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp?20=E), about 21% of commercial flights scheduled between June 2003 and October 2021 have experienced some form of delay. It is critical for airlines to estimate flight delays as accurately as possible in order to improve customer satisfaction and optimize the income of airline agencies.

## Contributors


  * Jordan Silke [![GitHub](https://img.shields.io/github/followers/jsilke?style=social)](https://github.com/jsilke)
  * Jonas Bacareza [![GitHub](https://img.shields.io/github/followers/jebacareza?style=social)](https://github.com/jebacareza)


### Understanding the problem
---
In an effort to understand some common causes of commercial flight delays, a number of sources were consulted including government agencies and flight-focused blog posts. A brief overview of findings can be found in the [Research](./Research) directory. These common causes will inform feature selection and engineering decisions.

### Data description
---
Data was sourced from a [LHL](https://github.com/lighthouse-labs/mid-term-project-I/blob/master/README.md) database and [descriptions](./Data/descriptions) were provided for each table. We used a custom [script](./Scripts/feature_extraction.py) to extract the feature names from these description files and the raw data can be found [here](./Data/files). The rationale behind missing value processing can be reviewed and reproduced by reading and executing the [data_overview](./Exploration/data_overview.ipynb) notebook.

