import pandas as pd


def load_data():
    filename = "files/olympics.csv"
    new_cols = ['Country_name_and_code', '# Summer', 'Gold', 'Silver', 'Bronze', 'Total', 'Winter', 'Gold', 'Silver', 'Bronze', 'Total.1', 'Games', 'Gold', 'Silver', 'Bronze', 'Combined total']
    df = pd.read_csv(filename, skiprows=[0,1], names=new_cols, header=None)
    #df.rename(columns={'01 !' : "Gold", '02 !': "Silver", '03 !' : "Bronze"}, inplace=True)
    df.Country_name_and_code =  df.Country_name_and_code.str.replace("\xc2\xa0", "")
    #only_country_names = [x[0].strip("\xc2\xa0") for x in df["Country_name_and_code"].str.split("(")]
    only_country_names = [x[0] for x in df["Country_name_and_code"].str.split("(")]
    df.index = only_country_names

    #Method 1
    #use_cols = [col for col in df.columns if col[:5] != "Total" ]
    #return df[use_cols]

    # If you want specified coulmns
    #return df.filter(like="Total", axis=1)  # df.filter(regex="Total", axis=1)

    return df[df.columns.drop(list(df.filter(regex="Total")))]


def first_country(df):
    return df.iloc[0]


def gold_medal(df):
    return df.iloc[:-1, [2]].idxmax()[0]


def biggest_difference_in_gold_medal(df):
    return (df.iloc[:-1,2] -  df.iloc[:-1,6]).abs().idxmax()


def get_points(df):
    df["Points"] = (df["Gold"] * 3) + (df['Silver'] * 2) + (df["Bronze"]) + (df["Gold.1"] * 3) + (df['Silver.1'] * 2) + (df["Bronze.1"])
    return df["Points"]


# df = load_data()
# print(first_country(df)["# Summer"])
# print(gold_medal(df))
# print(biggest_difference_in_gold_medal(df))
# print(get_points(df))
