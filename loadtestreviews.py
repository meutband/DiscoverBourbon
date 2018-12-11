import os
import pandas as pd
import sqlite3

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mainapp.settings")

import django
django.setup()

from bourbonsite.models import Review


def save_review_from_row(row):

    review = Review()

    review.RatingID = row[0]
    review.Bourbon_id = row[1]
    review.Pub_Date = row[2]
    review.User_Name = row[3]
    review.Comment = row[4]
    review.Rating = row[5]

    review.save()


if __name__ == "__main__":

    print("Reading from file data/testreviews.csv")

    review_df = pd.read_csv("data/testreviews.csv", sep=';')
    review_df.apply(save_review_from_row, axis=1)

