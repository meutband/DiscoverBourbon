import pandas as pd
from .models import Bourbon, Review, SimilarBourbons, SimilarReviews
# from django.contrib.auth.models import User
from sklearn import preprocessing
from sklearn.metrics.pairwise import cosine_similarity, cosine_distances, euclidean_distances, manhattan_distances


def saveSimilarities(row):

    similarBourbons = SimilarBourbons()

    similarBourbons.Bourbon = row['Bourbon']
    similarBourbons.BourbonID = row['BourbonID']

    similarBourbons.save()


def findSimilarBourbons(BourbonID):

    ''' This recommendation is finding similar bourbons not from the same distillery '''

    bourbons = pd.DataFrame(list(Bourbon.objects.all().values()))

    # Remove all bourbons with the same distillery (keep BourbonID)
    distillery = bourbons.loc[bourbons['BourbonID'] == BourbonID]['Distillery'].values[0]
    bourbons = bourbons.loc[(bourbons['BourbonID'] == BourbonID) | (bourbons['Distillery'] != distillery)]

    # Remove items not being used for similarities (Bourbon Name, Distillery(we have location), Website, Description, id(from sqlite))
    final = bourbons.drop(['Bourbon','Distillery','Website','Description','id'], axis=1).set_index('BourbonID')

    # Encode the categorical data values
    le = preprocessing.LabelEncoder()
    final['Style'] = le.fit_transform(final['Style'])
    final['Type'] = le.fit_transform(final['Type'])
    final['Location'] = le.fit_transform(final['Location'])

    # Calculate the different distance similarity calculations (rank by average of each rank)
    cosine = cosine_distances(final.values)
    cosine = pd.DataFrame(cosine, columns=final.index.values, index=final.index)[BourbonID]

    euclidean = euclidean_distances(final.values)
    euclidean = pd.DataFrame(euclidean, columns=final.index.values, index=final.index)[BourbonID]

    manhattan = manhattan_distances(final.values)
    manhattan = pd.DataFrame(manhattan, columns=final.index.values, index=final.index)[BourbonID]

    allSimilarities = pd.concat([cosine, euclidean, manhattan], axis=1)
    allSimilarities.columns =['Cosine Distance', 'Euclidean Distance', 'Manhattan Distance']

    allRank = allSimilarities.rank(axis=0)
    finalRank = allRank.mean(axis=1)

    bourbons['SimilaritiesRank'] = list(finalRank.values)
    bourbons = bourbons.sort_values(by="SimilaritiesRank")

    # For each recommendation, remove recurring distilleries (so I dont get bourbons from the same distillery)
    bourbons = bourbons[bourbons['BourbonID'] != BourbonID]
    for index, row in bourbons.iterrows():
        if row['BourbonID'] in bourbons['BourbonID'].tolist():
            distillery = bourbons.loc[bourbons['BourbonID'] == row['BourbonID']]['Distillery'].values[0]
            bourbons = bourbons.loc[(bourbons['BourbonID'] == row['BourbonID']) | (bourbons['Distillery'] != distillery)]


    topBourbons = bourbons.head()

    topBourbons.apply(saveSimilarities, axis=1)



def saveRecommendations(row):

    similarReviews = SimilarReviews()

    similarReviews.Bourbon = row['Bourbon']
    similarReviews.BourbonID = row['BourbonID']
    similarReviews.AvgRating = row['AvgRating']
    similarReviews.PredRating = row['PredRating']

    similarReviews.save()


def findBourbonsFromUsers(username):

    print(username)

    # Reviews only has the id of the bourbon database, so we need to add 'Bourbon' and 'BourbonID' to reviews.
    bourbons = pd.DataFrame(list(Bourbon.objects.all().values()))
    reviews = pd.DataFrame(list(Review.objects.all().values()))

    if reviews.shape[0] < 10:
        return False

    reviews['Bourbon'] = bourbons['Bourbon'][reviews['Bourbon_id']].tolist()
    reviews['BourbonID'] = bourbons['BourbonID'][reviews['Bourbon_id']].tolist()

    # Get the average of the reviews by bourbonid
    averages = reviews.groupby('BourbonID').mean()['Rating']
    # print(averages)

    # Create table of users and ratings.
    data = reviews.pivot_table(index=['BourbonID'], columns=['User_Name'], values='Rating')

    # Calculate the cosine similarity values for the data
    user = data[username]
    cosine = data.corrwith(user)

    # Get the bourbons of users that were not rated by username
    ratings = reviews[user[reviews['BourbonID']].isnull().values & (reviews['User_Name'] != username)]

    # Predict the ratings of bourbons for username. If there is an error, return False for no recommendations.
    # (Not enough info)
    try:
        ratings['similarity'] = ratings['User_Name'].map(cosine.get)
        ratings['sim_rating'] = ratings['similarity'] * ratings['Rating']
        recommendation = ratings.groupby('BourbonID').apply(lambda s: s.sim_rating.sum() / s.similarity.sum()).sort_index()
    except:
        return False

    # Create final dataframe of recommendations with average and predicted ratings
    final = bourbons[bourbons['BourbonID'].isin(recommendation.index.values)].sort_values('BourbonID')
    avgs = averages[averages.index.isin(recommendation.index.values)].sort_index()
    final['AvgRating'] = avgs.values
    final['PredRating'] = recommendation.values

    final.apply(saveRecommendations, axis=1)

    return True
