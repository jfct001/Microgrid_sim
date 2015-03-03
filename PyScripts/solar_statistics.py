# ------------------------------------------------------------------------------
# A statistical model of solar radiations
# ------------------------------------------------------------------------------
#
# File:         solar_statistics.py
# Author:       Hongwei Jin
# Created:      03/03/2015
# Modified:


import os
from datetime import datetime, timedelta
from collections import defaultdict, Counter, OrderedDict
import csv
import itertools


def read_data(folder, filename):
    """
    Read all columns to dictionary in a inner varaiable _COLUMNS, sorted with keys
    """
    with open(os.path.join(DATA_FOLDER, filename)) as infile:
        reader = csv.DictReader(infile)  # read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():  # go over each column name and value
                _COLUMNS[k].append(v)  # append the value into the appropriate list
    # sorted _COLUMNS by keys
    sorted(_COLUMNS, key=_COLUMNS.get)


def reduce_solar_csv():
    """
    Reduce solar data file into reduced column numbers
    """
    with open(os.path.join(DATA_FOLDER, "reduce_20_years_solar_with_weathear.csv"), "w") as outfile:
        outfile.write("YYYY-MM-DD,HH:MM (LST),METSTAT Glo (Wh/m^2),Conditions,MaxRadi (Wh/m^2),Cindex,CCindex" + "\n")
        for i in range(len(_COLUMNS["YYYY-MM-DD"])):
            outfile.write(
                _COLUMNS["YYYY-MM-DD"][i] + "," +
                _COLUMNS["HH:MM (LST)"][i] + "," +
                _COLUMNS["METSTAT Glo (Wh/m^2)"][i] + "," +
                _COLUMNS["Conditions"][i] + "," +
                _COLUMNS["MaxRadi (Wh/m^2)"][i] + "," +
                _COLUMNS["Cindex"][i] + "," +
                _COLUMNS["CCindex"][i] + "\n")


def main():
    """
    Process start here
    """
    read_data(DATA_FOLDER, FILENAME)
    reduce_solar_csv()
    pass

if __name__ == '__main__':
    CURRENT_FOLDER = os.path.dirname(os.path.realpath(__file__))
    DATA_FOLDER = os.path.join(CURRENT_FOLDER, "..", "Data\\solar_data")
    FILENAME = "total_20_years_solar_with_weather (backup).csv"
    _COLUMNS = defaultdict(list)
    main()
