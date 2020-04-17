import numpy as np


def linear_ecu(x, y, z):
    ecua1 = x - (3.*y) + (2.*z)
    ecua2 = (5.*x) + (6.*y) - z
    ecua3 = (4.*x) - y + (3.*z)
    return(ecua1, ecua2, ecua3)

def MSE(e1, e2, e3):
    mse = (np.power(-3. - e1, 2) + np.power(13. - e2, 2) + np.power(8. - e3, 2))/3.
    return (mse)

def fitness(x, y, z):
    x_f = bin2float(x)
    y_f = bin2float(y)
    z_f = bin2float(z)

    ec1, ec2, ec3 = linear_ecu(x_f, y_f, z_f)
    return MSE(ec1, ec2, ec3)
def bin2float(str_bin):
    # This function turn a binary string into a float with 3 digits of significance
    bin = 0
    if (str_bin[0] == '1'):
        sig = 1
    else:
        sig = -1
    for i in range(1, len(str_bin)):
        tmp = int(str_bin[i:i+1])
        bin = bin * 2 + tmp
    return(sig* (bin/1000))