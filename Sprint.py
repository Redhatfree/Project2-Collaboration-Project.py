# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 17:36:34 2025

@author: Rouzbeh
"""
import pandas as pd
df = pd.read_csv(r'C:\Users\Rouzbeh\Desktop\python\Sprint_data.csv')

print(df)
print("--"*30)


# Calculating Velocity (points for tasks which are "Done")
velocity = df[df["Status"] =="Done"]["Story_Points"].sum()

# Calculating remaining work (point for everything which has not been done for example everything in reviivew, to do or in progress) 
backlog_points = df[df["Status"]!= "Done" ]["Story_Points"].sum()

# Resource analysis (How many points Linda is handling?)
Linda_load = df[df["Assignee"] == "Linda"]["Story_Points"].sum()
print(f"\n Sprint insights")
print(f"Current Velocity: {velocity} points") 
print(f"Remaining Backlog: {backlog_points]} points")
