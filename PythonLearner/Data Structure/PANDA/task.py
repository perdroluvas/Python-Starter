import numpy as np
import pandas as pd
dados = np.random.randint(low= 0, high = 101, size = (3,4))
colunas = ['Eleanor', 'Chidi', 'Tahani', 'Jason']
df = pd.DataFrame(data = dados, columns = colunas)

print(df)

# Print the value in row #1 of the Eleanor column.
print("\nSecond row of the Eleanor column: %d\n" % df['Eleanor'][1])

# Create a column named Janet whose contents are the sum
# of two other columns.
df['Janet'] = df['Tahani'] + df['Jason']

# Print the enhanced DataFrame
print(df)