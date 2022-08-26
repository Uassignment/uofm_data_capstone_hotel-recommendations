import pandas as pd
import datetime
import time
import pickle
import numpy as np
import s3fs

#read in the data
url= "https://ralston-hotel-data-bucket.s3.amazonaws.com/Hotel_Reviews_Flask.csv"
hotel_sub_df = pd.read_csv(url)

s3 = s3fs.S3FileSystem(anon=True)
hotel_arr_s3 = np.load(s3.open("ralston-hotel-data-bucket/hotel_cos_data.npy"))

class ModelHelper():
    def __init__(self):
        pass

def recommendation_df(self, Hotel_Name):

    #variable reliant code
    indices = pd.Series(hotel_sub_df['Hotel_Name'])

    recommended_hotel = []
    recommended_hotel_address = []
    recommended_hotel_rating = []
    recommended_hotel_score = []

    idx = indices[indices == Hotel_Name].index[0]

    score_series = pd.Series(hotel_arr_s3[idx]).sort_values(ascending = False)

    top_10_indices = list(score_series.iloc[1:11].index)

    for i in top_10_indices:
        recommended_hotel.append(list(hotel_sub_df['Hotel_Name'])[i])
        recommended_hotel_address.append(list(hotel_sub_df['Hotel_Address'])[i])
        recommended_hotel_rating.append(list(hotel_sub_df['Average_Score'])[i])
        recommended_hotel_score.append(score_series[i])
    

    data = {'Hotel': recommended_hotel,
        'Address': recommended_hotel_address,
        'Rating': recommended_hotel_rating,
        'Score': recommended_hotel_score
        }

    rec_df = pd.DataFrame(data)
    rec_df = rec_df[(rec_df['Rating'] > 5)]

    rec_df
