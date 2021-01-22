import csv
import pickle
import pandas as pd

def make_pickle():

    """a_list = []

    with open("nhts_data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            a_list.append((row[0]))

    with open('nhts_data.pkl', 'wb') as output_file:
        pickle.dump(a_list[0], output_file)
        output_file.close()"""

    df = pd.read_csv("nhts_data.csv")
    df.to_pickle("nhts_data.pkl")


def read_pickle():

    df = pd.read_pickle('nhts_data.pkl')
    print(df.head())

if __name__ == "__main__":

    make_pickle()
    read_pickle()