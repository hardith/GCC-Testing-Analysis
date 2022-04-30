import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver

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
    plt.savefig('figures/extension.png', bbox_inches='tight')

# generateExtensionPlot()