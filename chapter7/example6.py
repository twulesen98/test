import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')
nyc.columns = ['Date', 'Temperature', 'Anomaly']
linear_regression = stats.linregress(x=nyc.Date, y=nyc.Temperature)
linear_regression.slope
linear_regression.intercept
axes = sns.regplot(x=nyc.Date, y=nyc.Temperature)
sns.set_style('whitegrid')
plt.show()
