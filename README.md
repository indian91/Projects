#corona_update1.py
In this file I create a graphical application using python. modules are used in this projects are following:
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import requests
import time
import random
from tkinter import *

In this project I update a live data of corona update for differenr countries which is available on a site which is:
 'www.worldometer.info/coronavirus/'
 
 We have four details in this project which is avialbel in tkinter label as a button
 (i) Total Deaths
 (ii)Total Cases
 (iii)New Deaths
 (iv)New Cases
 Above all option after clicking will show a graph of live data which is show on that particular website.
 
 Two more option is available there:
 First is refresh data which takes new live data every time when clicked on that button
 Another button is for exit from application
