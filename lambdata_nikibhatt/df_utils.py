""" Helpfer functions"""
from time import strptime
import pandas as pd


def addmore(df, num):
    for x in num:
        df = df.append(df.iloc[x])


def checknulls(df):
    num_nulls = df.isnull().sum()
    return('you have ' + num_nulls + 'nulls')


class splitdate(str):

    def print_month(self):
        self.d_list = str.split("/")
        return('Month: ' + self.d_list[0])
