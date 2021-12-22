# Temperature Conversion Algorithm from Degree Celcius to Fahrenheit
import numpy as np

celcius = np.random.rand(1, 5)
print('The degree celcius is: ', celcius)
fahrenheit = celcius * 1.8 + 32
print('The fahrenheit is: ', fahrenheit)

