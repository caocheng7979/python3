import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6,3))
print(df)
df.to_csv('numpppy.csv')