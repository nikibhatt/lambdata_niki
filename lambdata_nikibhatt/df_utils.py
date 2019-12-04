""" Helpfer functions"""
from time import strptime
import pandas as pd


def addmore(df, num):
    for x in range(1, num+1):
        df = df.append(df.iloc[x])
    return(df)


def split_date(str):
    d_list = str.split("/")
    return('Month: ' + d_list[0], 'Date: ' + d_list[1], 'Year: ' + d_list[2])
