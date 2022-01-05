import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')
nyc.columns = ['Date', 'Temperature', 'Anomaly']
nyc.Date = nyc.Date.floordiv(100)
linear_regression = stats.linregress(x=nyc.Date, y=nyc.Temperature)
axes = sns.regplot(x=nyc.Date, y=nyc.Temperature)
sns.set_style('whitegrid')
axes.set_ylim(5, 80)
axes.set_xlim(2000, 2022)
plt.show()
