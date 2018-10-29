import os
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mainapp.settings")

import django
django.setup()

from bourbonsite.models import Bourbon


def save_bourbon_from_row(row):

    bourbon = Bourbon()

    bourbon.BourbonID = row[0]
    bourbon.Bourbon = row[1]
    bourbon.Aged = row[2]
    bourbon.Proof = row[3]
    bourbon.Corn = row[4]
    bourbon.Rye = row[5]
    bourbon.Barley = row[6]
    bourbon.Wheat = row[7]
    bourbon.Type = row[8]
    bourbon.Style = row[9]
    bourbon.Price_Range = row[10]
    bourbon.Distillery = row[11]
    bourbon.Location = row[12]
    bourbon.Website = row[13]
    bourbon.Description = row[14]

    bourbon.save()


if __name__ == "__main__":

    print("Reading from file data/bourbonslist.csv")

    bourbon_df = pd.read_csv("data/bourbonslist.csv", sep=';')
    bourbon_df.apply(save_bourbon_from_row, axis=1)

