import numpy as np
import pandas as pd

df = pd.DataFrame(data = np.random.randn(5, 4), columns = ['a', 'b', 'c', 'd'])

# .iloc[] - Access DataFrame or Series elements by integer position
# Index-based boolean indexing
print(df.iloc[0:2, 1:3])  # Slice rows and columns
print(df.iloc[[1, 2, 4], [0, 2]])  # Select specific rows and columns by their integer positions
print(df.iloc[:, -1])  # Select the last column
print(df.iloc[[1, 2, 4]])  # Select specific rows by their integer positions
print(df.iloc[:2, :])  # Select the first 2 rows
print(df.iloc[-2:, :])  # Select the last 2 rows
print(df.iloc[:, 0:3])  # Select the first 3 columns
print(df.iloc[0, 0])  # Select a single element by its row and column integer positions
