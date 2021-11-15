"""Manages system data and operations

Model gets file from Controller as Attribute"""
from Controller import *
import os, datetime, time, collections
import pandas as pd
class Model(Controller):
    def __init__(self):
        super().__init__()
        print(f"Welcome, today is the {time.gmtime().tm_mday}.{time.gmtime().tm_mon}.{time.gmtime().tm_year} \
and its {time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}")
        print(f"Running process with PID {os.getpid()}, on {sys.platform}")
        

    def tupleForVis(self, file):
        pass


