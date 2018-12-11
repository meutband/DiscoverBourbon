import os
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mainapp.settings")

import django
django.setup()

from django.contrib.auth.models import User


def save_user_from_row(user_row):
    user = User()
    user.id = user_row[0]
    user.username = user_row[1]
    user.password = user_row[2]
    user.save()


if __name__ == "__main__":

    print("Reading from file data/testusesrs.csv")

    review_df = pd.read_csv("data/testusers.csv", sep=';')
    review_df.apply(save_user_from_row, axis=1)