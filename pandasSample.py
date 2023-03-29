import pandas as pd
import numpy as np


songs = {
    'Artist': ['Michael Jackson', 'AC/DC', 'Pink Floyd', 'Whitney Houston', 'Meat Loaf', 'Eagles', 'Bee Gees', 'Fleetwood Mac'],
    'Album': ['Thriller', 'Black in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell', 'Their Greatest Hits(1971-1975)', 'Saturday Night Fever', 'Rumours'],
    'Released': [1982, 1980, 1973, 1992, 1977, 1976, 1977, 1977],
    'Length': ['00:42:19', '00:42:11', '00:42:49', '00:57:44', '00:43:33', '0:43:08', '1:15:54', '0:40:01'],
    'Genre': ['pop, rock, R&B', 'hard rock', 'progressive rock', 'R&B, soul, pop', 'hard rock, progressive rock', 'rock, soft rock, folk rock', 'disco', 'soft rock'],
    'Music Recording Sales (millions)': [46.0, 26.1, 24.2, 27.4, 20.6, 32.2, 20.6, 27.9],
    'Claimed Sales (millions)': [65, 50, 45, 44, 43, 42, 40, 40],
    'Released.1': ['30-Nov-82', '25-Jul-80', '01-Mar-73', '17-Nov-92', '21-Oct-77', '17-Feb-76', '15-Nov-77', '04-Feb-77'],
    'Soundtrack': ['Nan', 'Nan', 'Nan', 'Y', 'Nan', 'Nan', 'Y', 'Nan'],
    'Rating': [10.0, 9.5, 9.0, 8.5, 8.0, 7.5, 7.0, 6.5]
}

df = pd.DataFrame(songs)
# print(df)
# print(df[['Album', 'Released']])
# new_df = df[df['Released'] >= 1980]
# print(new_df)
# new_df.to_csv('new_songs.csv')

print(df.iloc[2:5], 'Album')
print(df.loc[2:5], 'Album')
print(df.iloc[2:6, 1])
# print(df.loc[2:5, 1])


X=np.array([[1,0],[0,1]])
Y=np.array([[2,2],[2,2]])
Z=np.dot(X,Y)
print(f"Z = {Z}")