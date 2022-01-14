[![Lifecycle](https://img.shields.io/badge/Lifecycle-Experimental-orange.svg)](https://www.tidyverse.org/lifecycle/#experimental)
# Flight Delay Prediction

Our objective is to predict arrival delays of commercial flights. According to the [US Department of Transportation](https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp?20=E), about 21% of commercial flights scheduled between June 2003 and October 2021 have experienced some form of delay. It is critical for airlines to estimate flight delays as accurately as possible in order to improve customer satisfaction and optimize the income of airline agencies. This project will be evaluated on the basis of arrival delay prediction accuracy for flights 

## Contributors


  * Jordan Silke [![GitHub](https://img.shields.io/github/followers/jsilke?style=social)](https://github.com/jsilke)
  * Jonas Bacareza [![GitHub](https://img.shields.io/github/followers/jebacareza?style=social)](https://github.com/jebacareza)


### Understanding the problem
---
In an effort to understand some common causes of commercial flight delays, a number of sources were consulted including government agencies and flight-focused blog posts. A brief overview of findings can be found in the [Research](./Research) directory. These common causes will inform feature selection and engineering decisions.

### Data description
---
Data was sourced from a [LHL](https://github.com/lighthouse-labs/mid-term-project-I/blob/master/README.md) PostgreSQL database and [descriptions](./Data/descriptions) were provided for each table. We used a custom [script](./Scripts/feature_extraction.py) to extract the feature names from these description files and the raw data can be found [here](./Data/files). The rationale behind missing value processing can be reviewed and reproduced by reading and executing the [data_overview](./Exploration/data_overview.ipynb) notebook. The data from the flights table included in this repository is a [randomly sampled subset](./Scripts/queries.sql) of the source table.

### [Recommended](https://github.com/lighthouse-labs/mid-term-project-I/blob/master/exploratory_analysis.ipynb) exploration
---

|Task|Status|
|----|:----:|
|Test the hypothesis that the arrival delay is from Normal distribution and that mean of the delay is 0. Be careful about the outliers.|✅|
|Is average/median monthly delay different during the year? If so, which months have the biggest delays and what could be the reason?|✅|
|Does the weather affect the delay?|🧰|
|How are taxi times changing during the day? Does higher traffic lead to longer taxi times?|✅|
|What is the average percentage of delays that exist prior to departure (*i.e.* are arrival delays caused by departure delays)? Are airlines able to lower the delay during the flights?|✅|
|How many states cover 50% of US air traffic?|✅|
|Test the hypothesis that planes fly faster when there is a departure delay.|✅|
|When (which hour) do most 'LONG', 'SHORT', 'MEDIUM' haul flights take off?|🔳|
|Find the top 10 the bussiest airports. Does the greatest number of flights mean that the majority of passengers went through a given airport? How much traffic do these 10 airports cover?|🔳|
|Do bigger delays lead to bigger fuel consumption per passenger?|🔳|

🔳 - To do.  
✅ - Core task 'complete' (at least a first pass).  
🧰 - Work in progress.  

  
Exploration task results can be found [here](Exploration/recommended_exploration.ipynb)  

### Feature Selection & Engineering
---
The rationale behind the features we used was developed during [exploration](./Exploration) and is explained in further detail in [features](./Data/features). Ideally, we would explore more broadly to determine the feature space that generalizes our predictions the most effectively.

### Modelling
---
We use an ensemble approach to modelling that incorporates bagging, boosting, and stacking based on a classifier prediction in an attempt to mitigate our regression error and improve the generalization of our predictions. Our approach can be found [here](./Modelling)

### Wishlist
---
If we get more time it would be interesting to pursue:  

- Features from the other tables
- Time series analysis
- Further exploration of the data
- More rigourous modelling (cv, hyperparameter tuning, alternative models, etc.)
- Alternate pipelines (incorporating polynomial features, different dimensionality reduction approaches, etc.)