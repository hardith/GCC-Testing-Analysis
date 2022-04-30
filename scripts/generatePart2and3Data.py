import pandas as pd

extension_map = {
    ".c":"C",
    ".cc":"CPP",
    ".f90":"Fortran",
    ".go":"Go",
    ".m":"Objective C",
    ".mm":"Objective CPP"
}

def main():
    df = pd.read_csv("csv-data/stagedData_Main.csv")
    
    df = df[df['path'].notna()]
    df = df.iloc[: , 1:]
    # df2 = df[(df['path'].str.contains('test'))].reset_index(drop=True)
    df2 = df.loc[df['path'].str.contains("test", case=False)]
    df3 = df.loc[~df['path'].str.contains("test", case=False)]
    del df2["DEBUG"]

    df2.to_csv('csv-data/AssertFiles.csv')
    df3.to_csv('csv-data/ProductionAssertFiles.csv')

    df_C = df[(df['path'].str.match( r'.*\.c$'))].reset_index(drop=True)
    df_CC = df[(df['path'].str.match( r'.*\.cc$'))].reset_index(drop=True)
    df_F = df[(df['path'].str.contains('.f90'))].reset_index(drop=True)
    df_GO = df[(df['path'].str.contains('.go'))].reset_index(drop=True)
    df_M = df[(df['path'].str.match( r'.*\.m$'))].reset_index(drop=True)
    df_MM = df[(df['path'].str.contains('.mm'))].reset_index(drop=True)

    df_C_count = df_C[df_C.columns[0]].count()
    df_CC_count = df_CC[df_CC.columns[0]].count()
    df_F_count = df_F[df_F.columns[0]].count()
    df_GO_count = df_GO[df_GO.columns[0]].count()
    df_M_count = df_M[df_M.columns[0]].count()
    df_MM_count = df_MM[df_MM.columns[0]].count()

    listCount = [df_C_count,df_CC_count,df_F_count,df_GO_count,df_M_count,df_MM_count]
    language_list = ["C","CPP","Fortran","Go","Objective C","Objective CPP"]
    df5 = pd.DataFrame(list(zip(language_list, listCount)),
               columns =['Name', 'Count'])
    df5 = df5[df5.Count != 0]

    df5.to_csv('csv-data/LanguageTestFiles.csv')

    df4 = df3[df3.DEBUG != 0]

    df4_C = df4[(df4['path'].str.match( r'.*\.c$'))].reset_index(drop=True)
    df4_CC = df4[(df4['path'].str.match( r'.*\.cc$'))].reset_index(drop=True)
    df4_F = df4[(df4['path'].str.contains('.f90'))].reset_index(drop=True)
    df4_GO = df4[(df4['path'].str.contains('.go'))].reset_index(drop=True)
    df4_M = df4[(df4['path'].str.match( r'.*\.m$'))].reset_index(drop=True)
    df4_MM = df4[(df4['path'].str.contains('.mm'))].reset_index(drop=True)

    df4_C_count = df4_C[df4_C.columns[0]].count()
    df4_CC_count = df4_CC[df4_CC.columns[0]].count()
    df4_F_count = df4_F[df4_F.columns[0]].count()
    df4_GO_count = df4_GO[df4_GO.columns[0]].count()
    df4_M_count = df4_M[df4_M.columns[0]].count()
    df4_MM_count = df4_MM[df4_MM.columns[0]].count()

    listCount_d = [df4_C_count,df4_CC_count,df4_F_count,df4_GO_count,df4_M_count,df4_MM_count]
    language_list_d = ["C","CPP","Fortran","Go","Objective C","Objective CPP"]
    df6 = pd.DataFrame(list(zip(language_list_d, listCount_d)),
               columns =['Name', 'Count'])
    df6 = df6[df6.Count != 0]

    df6.to_csv('csv-data/LanguageDebugFiles.csv')

    print("------------done------------")

main()