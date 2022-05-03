# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:13:08 2022

@author: bubri
"""

import pandas as pd
import os


# change_data_size
results_dir = "C://Users//bubri//OneDrive//Desktop//thesis//final//new//change_batch_size//"
results = "//results.csv"

results_df_1 = pd.read_csv(results_dir + '100000_10_10000_1' + results)
results_df_1['batch_size'] = 1

results_df_100 = pd.read_csv(results_dir + '100000_10_10000_100' + results)
results_df_100['batch_size'] = 100

results_df_200 = pd.read_csv(results_dir + '100000_10_10000_200' + results)
results_df_200['batch_size'] = 200

results_df_300 = pd.read_csv(results_dir + '100000_10_10000_300' + results)
results_df_300['batch_size'] = 300

results_df_400 = pd.read_csv(results_dir + '100000_10_10000_400' + results)
results_df_400['batch_size'] = 400

results_df_500 = pd.read_csv(results_dir + '100000_10_10000_500' + results)
results_df_500['batch_size'] = 500

results_df_600 = pd.read_csv(results_dir + '100000_10_10000_600' + results)
results_df_600['batch_size'] = 600

results_df_700 = pd.read_csv(results_dir + '100000_10_10000_700' + results)
results_df_700['batch_size'] = 700

results_df_800 = pd.read_csv(results_dir + '100000_10_10000_800' + results)
results_df_800['batch_size'] = 800

results_df_900 = pd.read_csv(results_dir + '100000_10_10000_900' + results)
results_df_900['batch_size'] = 900

results_df_1000 = pd.read_csv(results_dir + '100000_10_10000_1000' + results)
results_df_1000['batch_size'] = 1000


frames = [results_df_1, results_df_100, results_df_200, results_df_300, results_df_400]

combined_small_df = pd.concat(frames)


frames = [results_df_100, results_df_200, results_df_300, results_df_400, results_df_500,
          results_df_600, results_df_700, results_df_800, results_df_900, results_df_1000]

combined_df = pd.concat(frames)

print(combined_df)



# statistics

for results_df in frames:
    for test_case_tuple in results_df[["hbase", "rondb", "rondb_cluster", "action"]].groupby(['action']):
        print(f"{test_case_tuple[0]}: {results_df.iloc[0]['batch_size']}")
        print(test_case_tuple[1].describe())
    print(f"{test_case_tuple[0]}")
    print(results_df.describe())




# make df friendly for visualization

def prepare_for_visualization(df):
    implementations = ["hbase", "rondb", "rondb_cluster"]
    
    new_df = pd.DataFrame()
    for implementation in implementations:
        implementation_df = df[[implementation, "batch_size", "action"]]
        implementation_df.rename({implementation:'time'}, axis=1, inplace=True)
        implementation_df["implementation"] = implementation
        new_df = new_df.append(implementation_df, ignore_index=True)
        
    new_df['implementation'].replace('rondb','rondb_jdbc', inplace=True)
    new_df['implementation'].replace('rondb_cluster','rondb_clusterj', inplace=True)
    
    return new_df


#visualize

import matplotlib.pyplot as plt
import seaborn as sns


def data_size_line_plot():
    df = prepare_for_visualization(combined_df)
    df['batch_size'] = df['batch_size'].astype(str)

    for test_case_tuple in df.groupby(['action']):
        ax = sns.lineplot(data=test_case_tuple[1], x="batch_size", y="time", hue="implementation", palette=["C2", "C3", "C4"])
        #ax.set_title(f"Time for {test_case_tuple[0]} execution depending on the total number of entries")
        ax.set_ylabel(f"time (s)")
        ax.set_xlabel(f"batch size")
        plt.show()
        print(test_case_tuple[0])
    
data_size_line_plot()






















# make df friendly for visualization

def prepare_for_visualization(df):
    implementations = ["rondb", "rondb_cluster"]
    
    new_df = pd.DataFrame()
    for implementation in implementations:
        implementation_df = df[[implementation, "batch_size", "action"]]
        implementation_df.rename({implementation:'time'}, axis=1, inplace=True)
        implementation_df["implementation"] = implementation
        new_df = new_df.append(implementation_df, ignore_index=True)
        
    new_df['implementation'].replace('rondb','rondb_jdbc', inplace=True)
    new_df['implementation'].replace('rondb_cluster','rondb_clusterj', inplace=True)
    
    return new_df


#visualize

import matplotlib.pyplot as plt
import seaborn as sns


def data_size_line_plot():
    df = prepare_for_visualization(combined_small_df)
    df['batch_size'] = df['batch_size'].astype(str)

    for test_case_tuple in df.groupby(['action']):
        ax = sns.lineplot(data=test_case_tuple[1], x="batch_size", y="time", hue="implementation", palette=["C3", "C4"])
        #ax.set_title(f"Time for {test_case_tuple[0]} execution depending on the total number of entries")
        ax.set_ylabel(f"time (s)")
        ax.set_xlabel(f"batch size")
        plt.show()
        print(test_case_tuple[0])
    
data_size_line_plot()