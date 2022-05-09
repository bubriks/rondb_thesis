# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:13:08 2022

@author: bubri
"""

import pandas as pd
import os


# change_data_size
results_dir = "C://Users//bubri//OneDrive//Desktop//thesis//final//new//change_test_size//"
results = "//results.csv"

results_df_1 = pd.read_csv(results_dir + '10000000_10_1' + results)
results_df_1['test_size'] = 1

results_df_10 = pd.read_csv(results_dir + '10000000_10_10' + results)
results_df_10['test_size'] = 10

results_df_1000 = pd.read_csv(results_dir + '10000000_10_100' + results)
results_df_1000['test_size'] = 100

results_df_10000 = pd.read_csv(results_dir + '10000000_10_1000' + results)
results_df_10000['test_size'] = 1000

results_df_100000 = pd.read_csv(results_dir + '10000000_10_10000' + results)
results_df_100000['test_size'] = 10000

#results_df_1000000 = pd.read_csv(results_dir + '100000_10_100000' + results)
#results_df_1000000['test_size'] = 100000


frames = [results_df_1, results_df_10, results_df_1000, results_df_10000, results_df_100000]

combined_df = pd.concat(frames)

print(combined_df)



# statistics

for results_df in frames:
    for test_case_tuple in results_df[["bloom", "simple", "hbase", "rondb", "rondb_cluster", "action"]].groupby(['action']):
        print(f"{test_case_tuple[0]}: {results_df.iloc[0]['test_size']}")
        print(test_case_tuple[1].describe())
    print(f"{test_case_tuple[0]}")
    print(results_df.describe())




# make df friendly for visualization

def prepare_for_visualization(df):
    implementations = ["bloom", "simple", "hbase", "rondb", "rondb_cluster"]
    
    new_df = pd.DataFrame()
    for implementation in implementations:
        implementation_df = df[[implementation, "test_size", "action"]]
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
    df['test_size'] = df['test_size'].astype(str)

    for test_case_tuple in df.groupby(['action']):
        ax = sns.lineplot(data=test_case_tuple[1], x="test_size", y="time", hue="implementation")
        #ax.set_title(f"Time for {test_case_tuple[0]} execution depending on the total number of entries")
        ax.set_ylabel(f"time (s)")
        ax.set_xlabel(f"number of entries")
        plt.show()
        print(test_case_tuple[0])
    
data_size_line_plot()

















'''

# make df friendly for visualization

def prepare_for_visualization(df):
    implementations = ["bloom", "simple", "hbase", "rondb", "rondb_cluster"]
    
    new_df = pd.DataFrame()
    for implementation in implementations:
        implementation_df = df[[implementation, "action", "run_nr"]]
        implementation_df.rename({implementation:'time'}, axis=1, inplace=True)
        implementation_df["implementation"] = implementation
        new_df = new_df.append(implementation_df, ignore_index=True)
        
    new_df['implementation'].replace('rondb','rondb_jdbc', inplace=True)
    new_df['implementation'].replace('rondb_cluster','rondb_clusterj', inplace=True)
    
    return new_df


def data_size_line_plot():
    df = prepare_for_visualization(results_df_100000)

    for test_case_tuple in df.groupby(['action']):
        ax = sns.lineplot(data=test_case_tuple[1], x="run_nr", y="time", hue="implementation")
        #ax.set_title(f"Time for {test_case_tuple[0]} execution depending on the total number of entries")
        ax.set_ylabel(f"time (s)")
        ax.set_xlabel(f"run #")
        plt.show()
        print(test_case_tuple[0])
    
data_size_line_plot()
'''