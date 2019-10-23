import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def sigmoida(x):
    return 1 / (1 + math.e ** x)


def main():
    features_data = pd.read_csv('features_data_with_numbers.csv')
    del features_data['Unnamed: 0']
    del features_data['Unnamed: 0.1']
    del features_data['user_id']
    features_data['first_deposit_amount'] = (features_data['first_deposit_amount'])**
    features_data['time_spent'] = (features_data['time_spent'])**1.3
    # print(features_data.columns)
    data = np.zeros((len(features_data['risk_tolerance']), 10))

    index = 0
    for header in features_data.columns:
        data[:, index] = features_data[header][:]
        index += 1

    train_set = data[:-1000, :]
    test_set = data[-1000:, :]

    k = 101

    right = 0
    for y_index in range(test_set.shape[0]):
        if y_index % 100 == 0:
            print(y_index)

        distance_list = []
        for x_index in range(train_set.shape[0]):
            dist = evclidian_distance(test_set[y_index], train_set[x_index])
            distance_list.append([dist, train_set[x_index][-2]])

        distance_list = sorted(distance_list, key=lambda x: x[0], reverse=False)
        distance_list = distance_list[:k]

        real = test_set[y_index][-2]
        if sum([x[-1] for x in distance_list]) / k > 0.5:
            # print("predict chunked")
            if real == 1:
                right += 1
        else:
            # print("predict not chunked")
            if real == 0:
                right += 1
        """
        if  real == 1:
            print("real chunked")
        else:
            print("real not chunked")

        print("accuracity - ", right/(y_index+1))
        print("-------------------------------------------")
        """
    print("accuracity - ", right / (test_set.shape[0]))


def evclidian_distance(x, y):
    summ = 0
    # print("x = ", x)
    # print("y = ", y)
    for i in range(len(x) - 2):
        summ += (x[i] - y[i]) ** 2
    return summ ** 0.5


if __name__ == '__main__':
    main()