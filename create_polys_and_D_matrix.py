# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def transform_X_2_polyX(X):
    """

    :param X:
    :return:
    """
    poly = PolynomialFeatures(include_bias=False)
    poly_X = None
    poly_X = poly.fit_transform(X).reshape(2 * len(X), -1)
    poly_X = np.concatenate((poly_X, np.ones(shape=(len(X), 1))))
    return poly_X.astype(int)


def transform_Y_2_polyY(Y):
    """

    :param Y:
    :return:
    """
    poly =  PolynomialFeatures(include_bias=False)
    poly_Y = None
    poly_Y = poly.fit_transform(Y).reshape(2 * len(Y), -1)
    even_arr = None
    even_arr = np.array([a for a in np.transpose(poly_Y)[0].tolist() if (np.transpose(poly_Y).tolist()[0].index(a)%2 == 1)])
    filled_with_ones_arr = None
    filled_with_ones_arr = np.array([1 if (np.transpose(poly_Y)[0].tolist().index(x)%2 == 1) else x
                                     for x in np.transpose(poly_Y)[0].tolist()])
    poly_Y =  np.concatenate((np.transpose(filled_with_ones_arr), np.transpose(even_arr))).reshape(3 * len(Y),1)
    return poly_Y.astype(int)


def build_D(length):
    """

    :param length:
    :return:
    """
    d = []
    for i in range(length * 2):
        if i %2 == 0:
            d.append(-2)
        else:
            d.append(1)
    d = np.transpose(np.concatenate((np.array(d).reshape(length * 2, -1), np.ones(shape=(length, 1)))))[0]
    return np.diag(d).astype(int)


def matrix_to_txt(Mat, name):
    w = open(name + '.txt', 'w')
    for i in range(Mat.shape[0]):
        row = [str(x) for x in Mat[i, :]]
        w.write(' '.join(row) + '\n')
    w.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name1 = ['p', 'i', 'p', 'p', 'o']
    name2 = ['p', 'i', 'p', 'p', 'o']
    pol_X = transform_X_2_polyX(np.array([ord(elem) for elem in name1]).reshape(len(name1), -1))
    pol_Y = transform_Y_2_polyY(np.array([ord(elem) for elem in name2]).reshape(len(name2), -1))

    prefix = './data/'
    matrix_to_txt(np.transpose(pol_X), prefix + 'poly_X')
    matrix_to_txt(np.transpose(pol_Y),  prefix + 'poly_Y')
    matrix_to_txt(build_D(len(name1)),  prefix + 'D')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
