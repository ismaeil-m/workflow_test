import numpy as np

def addition(var1, var2):
    output = var1 + var2
    print("output: ", output )
    return output

if __name__ == "__main__":
    val1 = np.array([1, 2, 3])
    val2 = np.array([3, 2, 3])
    add_output = addition(val1, val2)