import pandas as pd
import numpy as np
import datetime as dt
from pathlib import Path
import seaborn as sns
%matplotlib inline

# Reading whale returns
whale_df = pd.read_csv("whale_returns.csv", index_col = "Date", infer_datetime_format = True, parse_dates=True)
whale_df.sort_index(ascending=True, inplace=True)

# Count nulls
whale_df.isnull().sum()
whale_df.isnull().sum() / len(whale_df) * 100

# Drop nulls
whale_df.dropna(inplace = True)
whale_df.isnull().sum()

# Check data types make sure they are int/float
whale_df.dtypes

# Reading algorithmic returns
algo_df = pd.read_csv("algo_returns.csv", index_col = 'Date', infer_datetime_format = True, parse_dates = True)
algo_df.sort_index(ascending=True, inplace=True)

# Count nulls
algo_df.isnull()
algo_df.isnull().sum()/ len(algo_df) * 100

# Drop nulls
algo_df.dropna(inplace = True)

# Checking null is dropped
algo_df.isnull()
algo_df.isnull().sum() / len(algo_df) * 100

# Check data types make sure they are int/float
algo_df.dtypes

# Reading S&P 500 Closing Prices, sorting index
sp500_df = pd.read_csv("sp500_history.csv", index_col = 'Date', infer_datetime_format = True, parse_dates = True)
sp500_df.sort_index(ascending=True, inplace=True)

# Ince "Close" has $, leads me to believe that its a string rather than int... Check data types
sp500_df.dtypes

# Get rid of $ in order to turn them into integers
sp500_df['Close'] = sp500_df['Close'].str.replace('$', '')

# Convert close price string to inter
sp500_df['Close'] = sp500_df['Close'].astype('float')

# Check Data Types
sp500_df.isnull()
sp500_df.isnull().sum() / len(sp500_df) * 100

# Fix Data Types
sp500_df.dropna(inplace = True)

# Calculate Daily Returns
daily_returns_sp500 = sp500_df.pct_change()

# Drop nulls
daily_returns_sp500.dropna(inplace = True)

# Rename Column
daily_returns_sp500.rename(columns = {'Close':'Daily Returns'}, inplace = True)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat([whale_df, algo_df, daily_returns_sp500], axis = 1, join = 'inner')
print (combined_df.head())

# Plot daily returns
print (combined_df.plot(figsize=(25,10), title = "Daily Returns of Portfolios"))

# Plot cumulative returns
combined_cumulative_returns = (1 + combined_df).cumprod() - 1
print (combined_cumulative_returns.plot(kind = 'line', figsize=(25,10), title = "Cumulative Returns of Portfolios"))

# Box plot to visually show risk
correlation_combiend_df = combined_df.corr()
print (sns.heatmap(correlation_combiend_df, cmap = 'Greens_r'))

# Daily Standard Deviations
# Calculate the standard deviation for each portfolio. Which portfolios are riskier than the S&P 500?
combined_standard_deviation = combined_df.std()
combined_standard_deviation



