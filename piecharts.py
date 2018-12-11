import pandas as pd
import matplotlib.pyplot as plt
import os.path

filepath = 'bourbonsite/static/images/pie_charts/'

data = pd.read_csv('data/bourbonslist.csv', sep=';')
data = data[['BourbonID', 'Bourbon', 'Corn', 'Rye', 'Barley', 'Wheat']].set_index('BourbonID')

for index, row in data.iterrows():

    if os.path.exists(filepath+'{}.png'.format(index)):
        continue
    else:
        plt.figure(figsize=(4, 4), facecolor='#666666')
        df = row[['Corn', 'Rye', 'Barley', 'Wheat']].values

        if df[0] == 0:
            continue

        plt.pie(df, colors=['blue', 'maroon', 'orange', 'green'], labels=['Corn', 'Rye', 'Barley', 'Wheat'],
                    autopct='%1.0f%%', textprops={'color':'#ffffff', 'family':'sans-serif'})
        plt.title('Percent of Ingredients in \n{}'.format(data['Bourbon'][index]), color='#ffffff', family='sans-serif')
        plt.savefig(filepath+'{}.png'.format(index), facecolor='#666666')
