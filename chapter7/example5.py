import pandas as pd
import matplotlib.pyplot as plt
titan = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')
pd.set_option('precision',2)
plt.title("Ages of Passengers on Titanic")
plt.xlabel("Age (in Years)")
plt.ylabel("Count")
plt.hist(titan['age'])
plt.show()
