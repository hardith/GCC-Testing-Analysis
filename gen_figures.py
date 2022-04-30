import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype


def generateExtensionPlot():
    df = pd.read_csv("csv-data/ExtensionsData.csv")
    language_data = df.get("Language")
    count_data = df.get("Count")
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
    explode = (0, 0, 0, 0,0,0.2)  
    patches, texts = plt.pie(count_data,explode=explode)
    plt.legend(patches, language_data, loc='center left', bbox_to_anchor=(-0.1, 1.))
    plt.axis('equal')
    plt.title("Types of languages in GCC")
    # plt.show()
    plt.savefig('figures/extension.png', bbox_inches='tight')


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
changesPerWeek()
topContributers()
quarterlyData()
