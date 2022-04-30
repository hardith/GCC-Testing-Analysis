import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype
import numpy as np

def generateExtensionPlot():
    df = pd.read_csv("csv-data/ExtensionsData.csv")
    language_data = df.get("Language")
    count_data = df.get("Count")
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
    explode = (0, 0, 0, 0,0,0)  
    patches, texts = plt.pie(count_data,explode=explode)
    y = np.array(list(count_data))
    porcent = 100.*y/y.sum()
    labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(np.char.array(list(language_data)), porcent)]
    plt.legend(patches, labels, loc='center left', bbox_to_anchor=(-0.1, 1.),fontsize=8)
    plt.axis('equal')
    plt.title("Types of languages in GCC")
    plt.savefig('figures/extension.png', bbox_inches='tight')

def generateLanguageBasedTestFiles():
    df = pd.read_csv("csv-data/LanguageTestFiles.csv")
    name_data = df.get("Name")
    count_data = df.get("Count")

    # print(count_data)
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i], y[i], ha = 'center')

    df.plot(x="Name", y=["Count"], kind="bar", figsize=(9, 8))
    # plt.bar(list(name_data),list(count_data))
    plt.tight_layout()
    addlabels(list(name_data),list(count_data))
    plt.title("No of test files in each languages")
    plt.xlabel("Types of Languages")
    plt.ylabel("Count")
    plt.savefig('figures/LanguageTestFiles.png', bbox_inches='tight')

def generateLanguageBasedDebugFiles():
    df = pd.read_csv("csv-data/LanguageDebugFiles.csv")
    name_data = df.get("Name")
    count_data = df.get("Count")

    # print(count_data)
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i], y[i], ha = 'center')

    df.plot(x="Name", y=["Count"], kind="bar", figsize=(9, 8))
    # plt.bar(list(name_data),list(count_data))
    plt.tight_layout()
    addlabels(list(name_data),list(count_data))
    plt.title("No of Debug files in each languages")
    plt.xlabel("Types of Languages")
    plt.ylabel("Count")
    plt.savefig('figures/LanguageDebugFiles.png', bbox_inches='tight')


def generateAssertFilesPlot():
    df = pd.read_csv("csv-data/AssertFiles.csv")
    assertSum = int(df['Assert'].sum())
    gcc_assertSum = int(df['gcc_assert'].sum())
    gcc_checking_assertSum = int(df['gcc_checking_assert'].sum())
    ASSERT_ALWAYSSum = int(df['ASSERT_ALWAYS'].sum())
    FFI_ASSERTSum = int(df['FFI_ASSERT'].sum())
    CHECKSum = int(df['CHECK'].sum())
    _Static_assertSum = int(df['_Static_assert'].sum())
    VERIFYSum = int(df['VERIFY'].sum())

    assertCountlst = [assertSum,gcc_assertSum,gcc_checking_assertSum,ASSERT_ALWAYSSum,FFI_ASSERTSum,CHECKSum,_Static_assertSum,VERIFYSum]
    assertNamelst = ['Assert','gcc_assert','gcc_checking_assert','ASSERT_ALWAYS','FFI_ASSERT','CHECK','_Static_assert','VERIFY']
    labels = 'Assert','gcc_assert','ASSERT_ALWAYS','CHECK','_Static_assert','VERIFY'
    df2 = pd.DataFrame(list(zip(assertNamelst, assertCountlst)),
               columns =['Name', 'Count'])
    df2 = df2[df2.Count != 0]

    name_data = df2.get("Name")
    count_data = df2.get("Count")

    # print(count_data)
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i], y[i], ha = 'center')

    df2.plot(x="Name", y=["Count"], kind="bar", figsize=(9, 8))
    # plt.bar(list(name_data),list(count_data))
    plt.tight_layout()
    addlabels(list(name_data),list(count_data))
    plt.title("No of assert statements in test folders")
    plt.xlabel("Types of Assert Statements")
    plt.ylabel("Count")
    plt.savefig('figures/assert.png', bbox_inches='tight')

def generateAssertFilesProdPlot():
    df = pd.read_csv("csv-data/ProductionAssertFiles.csv")
    assertSum = int(df['Assert'].sum())
    gcc_assertSum = int(df['gcc_assert'].sum())
    gcc_checking_assertSum = int(df['gcc_checking_assert'].sum())
    ASSERT_ALWAYSSum = int(df['ASSERT_ALWAYS'].sum())
    FFI_ASSERTSum = int(df['FFI_ASSERT'].sum())
    CHECKSum = int(df['CHECK'].sum())
    _Static_assertSum = int(df['_Static_assert'].sum())
    VERIFYSum = int(df['VERIFY'].sum())
    DEBUGSum = int(df['DEBUG'].sum())

    assertCountlst = [assertSum,gcc_assertSum,gcc_checking_assertSum,ASSERT_ALWAYSSum,FFI_ASSERTSum,CHECKSum,_Static_assertSum,VERIFYSum,DEBUGSum]
    assertNamelst = ['Assert','gcc_assert','gcc_checking_assert','ASSERT_ALWAYS','FFI_ASSERT','CHECK','_Static_assert','VERIFY','DEBUG']
    
    df2 = pd.DataFrame(list(zip(assertNamelst, assertCountlst)),
               columns =['Name', 'Count'])

    # print (df2)
    name_data = df2.get("Name")
    count_data = df2.get("Count")

    # print(count_data)
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i], y[i], ha = 'center')

    df2.plot(x="Name", y=["Count"], kind="bar", figsize=(9, 8))
    # plt.bar(list(name_data),list(count_data))
    plt.tight_layout()
    addlabels(list(name_data),list(count_data))
    plt.title("No of assert and debug statements in production files")
    plt.xlabel("Types of Assert and Debug Statements")
    plt.ylabel("Count")
    plt.savefig('figures/assertProd.png', bbox_inches='tight')

def changesPerWeek():
    data = pd.read_csv("csv-data/changesperweek.csv")
    df = pd.DataFrame(data,columns=["Day", "Changes", "Commits", "Changes Per Commit"])

    cat_size_order = CategoricalDtype(
        ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday'],
        ordered=True
    )
    df['Day'] = df['Day'].astype(cat_size_order)
    df = df.sort_values('Day')
    df.plot(x="Day", y=["Changes", "Commits"], kind="bar",figsize=(9,8))
    df["Changes Per Commit"].plot(secondary_y=True,use_index=False,y='Changes Per Commit',color='green',legend='True')
    # plt.show()
    plt.title("Changes Per Week")
    plt.savefig('figures/changesPerWeek.png', bbox_inches='tight')


def topContributers():
    dataauthor = pd.read_csv("csv-data/authordata.csv")
    dfa = pd.DataFrame(dataauthor,columns=["author", "No of commits"])
    sorted_df = dfa.sort_values(["No of commits"], ascending=False)
    df2 = sorted_df[0:10]
    df2.plot(x="author", y=["No of commits"], kind="bar", figsize=(9, 8))
    plt.tight_layout()
    # plt.show()
    plt.title("Top Contributers")
    plt.savefig('figures/topContibuters.png', bbox_inches='tight')


def quarterlyData():
    df = pd.read_csv("csv-data/pydrillerData.csv")
    df3 = df.groupby(pd.to_datetime(df['added_date']).dt.to_period('Q'))['modified'].sum()
    df3.plot(x="added_date", y=["modified"], kind="bar", figsize=(9, 8))
    plt.tight_layout()
    # plt.show()
    plt.title("Quarterly Changes")
    plt.savefig('figures/quarterlyData.png', bbox_inches='tight')


generateExtensionPlot()
# changesPerWeek()
# topContributers()
# quarterlyData()
# generateAssertFilesPlot()
# generateAssertFilesProdPlot()
# generateLanguageBasedTestFiles()
# generateLanguageBasedDebugFiles()