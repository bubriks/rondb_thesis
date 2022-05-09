# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:13:08 2022

@author: bubri
"""

import pandas as pd
import os



# change_data_size
results_dir = "C://Users//bubri//OneDrive//Desktop//thesis//final//new//change_file_size//"
results = "//results.csv"

results_df_1mb = pd.read_csv(results_dir + '10000000_10_100_1mb' + results)
results_df_1mb['mb'] = 1

results_df_60mb = pd.read_csv(results_dir + '10000000_10_100_60mb' + results)
results_df_60mb['mb'] = 60

results_df_120mb = pd.read_csv(results_dir + '10000000_10_100_120mb' + results)
results_df_120mb['mb'] = 120

results_df_180mb = pd.read_csv(results_dir + '10000000_10_100_180mb' + results)
results_df_180mb['mb'] = 180


frames = [results_df_1mb, results_df_60mb, results_df_120mb, results_df_180mb]

combined_df = pd.concat(frames)

print(combined_df)



# statistics

for results_df in frames:
    for test_case_tuple in results_df[["bloom", "simple", "hbase", "rondb", "rondb_cluster", "action"]].groupby(['action']):
        print(f"{test_case_tuple[0]}: {results_df.iloc[0]['mb']}")
        print(test_case_tuple[1].describe())
    print(f"{test_case_tuple[0]}")
    print(results_df.describe())




# make df friendly for visualization

def prepare_for_visualization(df):
    implementations = ["bloom", "simple", "hbase", "rondb", "rondb_cluster"]
    
    new_df = pd.DataFrame()
    for implementation in implementations:
        implementation_df = df[[implementation, "mb", "action"]]
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
    df['mb'] = df['mb'].astype(str)

    for test_case_tuple in df.groupby(['action']):
        ax = sns.lineplot(data=test_case_tuple[1], x="mb", y="time", hue="implementation")
        #ax.set_title(f"Time for {test_case_tuple[0]} execution depending on the total number of entries")
        #ax.despine(left=False)
        ax.set_ylabel(f"time (s)")
        ax.set_xlabel("file size (mb)")
        plt.show()
        print(test_case_tuple[0])
    
data_size_line_plot()