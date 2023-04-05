import pandas as pd

if __name__ == "__main__":
    path = "creditcard.csv"
    df = pd.read_csv(path)
    print(df.describe())
    print(df.head(4))
    print(df.dtypes)
    target_names = {0: "NOT FRAUD", 1:"FRAUD"}
    dict_reponse = df.Class.value_counts().rename(index= target_names).to_dict()
    print(dict_reponse)
