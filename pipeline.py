import pandas as pd
import requests

def extract():
    df = pd.read_json("users.json")
    return df

def transform(df):
    df["city"] = df["address"].apply(

        lambda x: x["city"]
    )
    df["company"] = df["company"].apply(

        lambda x: x["name"]
    )
    df = df[["name", "email", "city", "company"]]

    users_per_city = df.groupby("city")["name"].count().reset_index(name="num_users")
    users_per_company = df.groupby("company")["name"].count().reset_index(name="num_users")
    most_common_city = users_per_city.loc[users_per_city["num_users"].idxmax()]

    return (
        df, users_per_city, users_per_company, most_common_city
    )

def load(df, users_per_city, users_per_company):
    df.to_csv("output\clean_users.csv",
        index=False)
    users_per_city.to_csv("output\\users_per_city.csv",
        index=False)
    users_per_company.to_csv("output\\users_per_company.csv",
        index=False)
    
def run_pipeline():

    df = extract()

    df, users_per_city, users_per_company, most_common_city = transform(df)

    load(df, users_per_city, users_per_company)

    print("Most Common City:")
    print(most_common_city)


if __name__ == "__main__":
    run_pipeline()
