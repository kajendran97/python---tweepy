import pandas as pd #importing pandas library
import re #importing re library
from gensim.parsing.preprocessing import remove_stopwords

#load the data using pandas
data = pd.read_csv("covid19.csv")

print(data)

tweet_text = data.loc[: ,"tweet_text"] #extract the tweet_text cloumn from csv
tweet_text = tweet_text.dropna()  #remove the blank columns and rows
cleaned_tweet_text = '' #creating the blank variable to load the data

tweet_no_stopword = []
for tweet in tweet_text:
    print("with stopword : ",tweet)
    remove_stop = remove_stopwords(tweet)
    print("without stopword : ",remove_stop)
    cleaned_tweet_text = re.sub(pattern='[^a-zA-Z0-9.]', repl='  ', string=remove_stop) #remove special charecters
    tweet_no_stopword.append(cleaned_tweet_text)

Data = {'words': tweet_no_stopword} #converting to the json format

df = pd.DataFrame(Data, columns=['words']) #defining the columns in dataframe

df.to_csv(r'export_dataframe.csv', index=False, header=True) #generate the csv

