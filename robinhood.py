import pandas as pd
import numpy as np
def main():
    features_data = pd.read_csv('features_data.csv')
    equity_value_data = pd.read_csv('equity_value_data.csv')

    chunked_user_list = []
    current_user = equity_value_data['user_id'][0]
    count = 0
    for index in range(len(equity_value_data['user_id'])-1):
        if equity_value_data['user_id'][index] != current_user:
            if count >= 28:
                chunked_user_list.append(current_user)
            count = 0
            current_user = equity_value_data['user_id'][index]
        else:
            if equity_value_data['close_equity'][index] < 100:
                count += 1
            else:
                if count >= 28:
                    chunked_user_list.append(current_user)
                count = 0

    chunked_header_list = []

    for i in range(len(features_data['user_id'])):

        if features_data['user_id'][i] in chunked_user_list:
            chunked_header_list.append(1)
        else:
            chunked_header_list.append(0)
    print(chunked_header_list)

    features_data['chunked'] = chunked_header_list
    features_data.to_csv(r'features_data_with_chunked.csv')

if __name__ == '__main__':
    main()
