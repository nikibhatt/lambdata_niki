""" Helpfer functions"""
from time import strptime
import pandas as pd

class splitdate(str):

    def print_month(self):
        self.d_list = str.split("/")
        return('Month: ' + self.d_list[0])
