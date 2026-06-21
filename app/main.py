import numpy as np

def add(val_1, val_2):
    return np.add(val_1, val_2)

if __name__ == "__main__":
    print(add(1, 2))
    print(add(3.5,4.2)==6.7)