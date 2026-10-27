import pandas as pd
import numpy as np
s = pd.Series(np.random.rand(10))
print("Original Series:")
print(s)
print("\nElement at index 3:")
print(s[3])
print("\nNumbers greater than 0.5:")
print(s[s > 0.5])
print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())
