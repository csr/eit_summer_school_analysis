from csv import reader

users = {}
users_number_of_tweets = {}

def greaterThanFiveHashtagFlag(text):
  return text.count("#") >= 5

def greaterThanOneURL(text):
  return text.count("https://") > 1

def moreThan30PercentCharsAreCAPS(text):
  return sum(1 for c in text if c.isupper()) >= (len(text) / 3)

# open file in read mode
with open('tweets.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        # print(row)
        userID = row[0]
        tweetID = row[1]
        createdAt = row[2]
        tweetText = row[3]

        # Keep track of number of tweets
        if not userID in users_number_of_tweets:
          users_number_of_tweets[userID] = 1
        else:
          users_number_of_tweets[userID] += 1

        # The higher, the more likely the tweet is fake
        fakeTweetFlags = 0

        if greaterThanFiveHashtagFlag(tweetText):
          fakeTweetFlags += 1
        
        if greaterThanOneURL(tweetText):
          fakeTweetFlags += 1

        if moreThan30PercentCharsAreCAPS(tweetText):
          fakeTweetFlags += 1

        if not userID in users:
          users[userID] = 0

        users[userID] += fakeTweetFlags

print(len(users.keys()))

# Normalize result by number of tweets