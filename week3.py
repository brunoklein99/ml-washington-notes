import pandas as pd


frame = pd.read_csv('amazon_baby.csv')

selected_words = ['awesome', 'great', 'fantastic', 'amazing', 'love', 'horrible', 'bad', 'terrible', 'awful', 'wow', 'hate']

frame['words'] = frame['review'].value_counts()

print(frame['words'].tail())