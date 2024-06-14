import numpy as np

noise = np.random.random([15]*4) - 2

print(noise)

feature = np.arange(6,21)
label = feature*3 + 4.0
print(label)

label = label + noise
print(label)