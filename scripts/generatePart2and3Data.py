import pandas as pd

def main():
    df = pd.read_csv("csv-data/stagedData_Main.csv")
    
    df = df[df['path'].notna()]
    df = df.iloc[: , 1:]
    # df2 = df[(df['path'].str.contains('test'))].reset_index(drop=True)
    df2 = df.loc[~df['path'].str.contains("test", case=False)]
    df3 = df.loc[~df['path'].str.contains("test", case=False)]
    del df2["DEBUG"]

    df.to_csv('csv-data/AssertFiles.csv')
    df.to_csv('csv-data/ProductionAssertFiles.csv')
    print("------------done------------")

main()