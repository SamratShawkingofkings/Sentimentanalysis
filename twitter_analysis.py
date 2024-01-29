import string
from collections import Counter
import matplotlib.pyplot as plt
import snscrape.modules.twitter as sntwitter
import time

def get_tweets():
    # Introduce a delay before making the request
    time.sleep(1)

    query = 'CoronaOutbreak since:2020-01-01 until:2020-04-01'
    max_tweets = 1000

    # Fetching tweets
    tweets = list(sntwitter.TwitterSearchScraper(query).get_items())[:max_tweets]

    # Creating list of chosen tweet data
    text_tweets = [[tweet.content] for tweet in tweets]
    return text_tweets

# Fetching tweets
text_tweets = get_tweets()

# Rest of the code remains the same...


# Rest of the code remains the same...


# Rest of the code remains the same...

# Concatenating tweets into a single string
text = " ".join(tweet[0] for tweet in text_tweets)

# Converting to lowercase
lower_case = text.lower()

# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Splitting text into words
tokenized_words = cleaned_text.split()

# List of stop words
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Removing stop words from the tokenized words list
final_words = [word for word in tokenized_words if word not in stop_words]

# Get emotions text
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)

# Count emotions
w = Counter(emotion_list)
print(w)

# Plotting
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
