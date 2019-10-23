import numpy as np
import pandas as pd

def main():
    features_data = pd.read_csv('features_data_with_chunked.csv')
    """
    for col in features_data.columns:
        a = set(features_data[col])
        print(a)
        print('___________________________________________________________')
    """

    any_dict = {
        'risk_tolerance' : {
            'low_risk_tolerance' : -1,
            'med_risk_tolerance' : 0,
            'high_risk_tolerance' : 1
        },
        'investment_experience' : {
            'no_investment_exp' : 0,
            'limited_investment_exp' : 1,
            'good_investment_exp' : 2,
            'extensive_investment_exp':3
        },
        'liquidity_needs' : {
            'not_important_liq_need' : 0,
            'somewhat_important_liq_need': 1,
            'very_important_liq_need' : 2,
        },
        'platform' : {
            'Android' : -1,
            'both' : 0,
            'iOS' : 1,
        },
        'instrument_type_first_traded' : {
            '0' : 0,
            'wrt' : 1,
            'stock' : 2,
            'mlp' : 3,
            'tracking' : 4,
            'etp' : 5,
            'rlt' : 6,
            'adr' : 7,
            'reit' : 8,
            'lp' : 9,
            'cef' : 10
        },
        'time_horizon' : {
            'short_time_horizon' : 0,
            'med_time_horizon' : 1,
            'long_time_horizon' : 2
        }}

    #print(any_dict)

    headers = features_data.columns
    for header in headers:
        if header in any_dict:
            for key in any_dict[header]:
                features_data.loc[(features_data[header] == key), header] =  any_dict[header][key]




    features_data.to_csv(r"features_data_with_numbers.csv")

if __name__ == '__main__':
    main()