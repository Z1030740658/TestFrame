"""
Returns data source from csv file.
"""
import csv


def read_from_csv(data_file):
    test_data = []
    with open(data_file, mode='r', newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
# data = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC) # this tells that extracted is numeric type
        # next(data)  #this skips header row
        for row in data:
            test_data.append(row)
    return test_data
