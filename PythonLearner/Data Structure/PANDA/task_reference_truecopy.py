import numpy as np
import pandas as pd

# Create a Python list that holds the names of the four columns.
column_names = ['Eleanor', 'Chidi', 'Tahani', 'Jason']

# Create a 3x4 numpy array, each cell populated with a random integer.
data = np.random.randint(low=0, high=101, size=(3, 4))

# Create a DataFrame.
df = pd.DataFrame(data=data, columns=column_names)

# Print the entire DataFrame
print(df)

# Print the value in row #1 of the Eleanor column.
print("\nSecond row of the Eleanor column: {}".format(df['Eleanor'][1]))

# Create a column named Janet whose contents are the sum
# of two other columns.
df['Janet'] = df['Tahani'] + df['Jason']

# Print the enhanced DataFrame
print(df)

# Create a reference and a true copy of the DataFrame.
reference_to_df = df
copy_of_df = df.copy()

# Modify a cell in df.
df.at[1, 'Jason'] += 5

# Print the updated DataFrame.
print("\nUpdated DataFrame:")
print(df)

# Print the reference DataFrame, which also got updated.
print("\nReference DataFrame:")
print(reference_to_df)

# Print the true copy of the DataFrame, which did not get updated.
print("\nTrue Copy DataFrame:")
print(copy_of_df)


