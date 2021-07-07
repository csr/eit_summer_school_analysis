from csv import reader


NUMBER_OF_FAKE_TWEET_FLAGS = 3


def greaterThanFiveHashtagFlag(text):
  return text.count("#") >= 5


def greaterThanOneURL(text):
  return text.count("https://") > 1


def moreThan30PercentCharsAreCAPS(text):
  return sum(1 for c in text if c.isupper()) >= (len(text) / 3)


def processCSVFile():
  users_fake_tweet_flags_count = {}
  users_tweets_count = {}

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
          if not userID in users_tweets_count:
            users_tweets_count[userID] = 1.0
          else:
            users_tweets_count[userID] += 1.0

          # The higher, the more likely the tweet is fake
          fakeTweetFlags = 0.0

          if greaterThanFiveHashtagFlag(tweetText):
            fakeTweetFlags += 1.0
          
          if greaterThanOneURL(tweetText):
            fakeTweetFlags += 1.0

          if moreThan30PercentCharsAreCAPS(tweetText):
            fakeTweetFlags += 1.0

          if not userID in users_fake_tweet_flags_count:
            users_fake_tweet_flags_count[userID] = 0.0

          users_fake_tweet_flags_count[userID] += fakeTweetFlags

      return users_fake_tweet_flags_count, users_tweets_count


def normalizeFakeTweetFlagsByNumberOfTweets(users_fake_tweet_flags_count, users_tweets_count):
  normalized = {}

  for userID, fakeTweetFlagsCount in users_fake_tweet_flags_count.items():
    tweetsCount = users_tweets_count[userID]
    averageFakeTweetFlags = fakeTweetFlagsCount / tweetsCount

    normalized[userID] = averageFakeTweetFlags / NUMBER_OF_FAKE_TWEET_FLAGS
  
  return normalized

def main():
    users_fake_tweet_flags_count, users_tweets_count = processCSVFile()
    
    print(users_fake_tweet_flags_count)
    print(users_tweets_count)

    users_flags_dict_normalized = normalizeFakeTweetFlagsByNumberOfTweets(users_fake_tweet_flags_count, users_tweets_count)
    print(users_flags_dict_normalized)


if __name__ == "__main__":
    main()