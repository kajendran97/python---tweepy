import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
from wordcloud import ImageColorGenerator

data = pd.read_csv("covid19.csv")

tweet_text = data.loc[: ,"tweet_text"]
tweet_text = tweet_text.dropna()
cleaned_tweet_text = ''

for tweet in tweet_text:
    # print(tweet)
    # cleaned_tweet_text += re.sub('[\(\[].*?[\)\]]', ' ', tweet)
    cleaned_tweet_text += re.sub(pattern='[^a-zA-Z0-9.]', repl='  ', string=tweet)
    # pattern = r'[^a-zA-Z0-9\s]'
    # cleaned_tweet_text += re.sub(pattern, '', cleaned_tweet_text)
    # print(cleaned_tweet_text.lower())

stopword_list = set(nltk.corpus.stopwords.words('english'))
# t = 'https', 'httpsd','xe3', 'x83', 'xbc19','b'
stopword_list.add('https')

# tweet_stopword = ['https','//','b',',','Do','nt','?','!']
# for i in tweet_stopword:
#     stopword_list.append(i)

tokens = nltk.word_tokenize(cleaned_tweet_text)
tokens = [token.strip() for token in tokens]
' '.join([token for token in tokens if token not in stopword_list])

tokens = list(dict.fromkeys(tokens))
print(" without dic ", tokens)

wordcloud_text = ''
for token in tokens:
    wordcloud_text += ' '+token

print(tokens)

char_mask = np.array(Image.open("wallpaper.jpg"))
image_colors = ImageColorGenerator(char_mask)

wc = WordCloud(background_color="white", max_words=160, width=400, height=400, mask=char_mask, random_state=1).generate(wordcloud_text)
# to recolour the image
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
plt.show()