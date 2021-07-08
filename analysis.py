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
  with open('lopezobrador_.csv', 'r') as read_obj:
      # pass the file object to reader() to get the reader object
      csv_reader = reader(read_obj)
      # Iterate over each row in the csv using reader object
      for row in csv_reader:
          # row variable is a list that represents a row in csv
          # print(row)
          username = row[0]
          tweetText = row[4]

          # Keep track of number of tweets
          if not username in users_tweets_count:
            users_tweets_count[username] = 1.0
          else:
            users_tweets_count[username] += 1.0

            if users_tweets_count[username] > 30:
              continue

          # The higher, the more likely the tweet is fake
          fakeTweetFlags = 0.0

          if greaterThanFiveHashtagFlag(tweetText):
            fakeTweetFlags += 1.0
          
          if greaterThanOneURL(tweetText):
            fakeTweetFlags += 1.0

          if moreThan30PercentCharsAreCAPS(tweetText):
            fakeTweetFlags += 1.0

          if not username in users_fake_tweet_flags_count:
            users_fake_tweet_flags_count[username] = 0.0

          users_fake_tweet_flags_count[username] += fakeTweetFlags

      return users_fake_tweet_flags_count, users_tweets_count


def normalizeFakeTweetFlagsByNumberOfTweets(users_fake_tweet_flags_count, users_tweets_count):
  normalized = {}

  for username, fakeTweetFlagsCount in users_fake_tweet_flags_count.items():
    tweetsCount = users_tweets_count[username]
    averageFakeTweetFlags = fakeTweetFlagsCount / tweetsCount
    normalized[username] = averageFakeTweetFlags / NUMBER_OF_FAKE_TWEET_FLAGS
  
  return normalized


def buildFinalSuspiciousTweetsColumn(users_flags_dict):
  # open file in read mode
  with open('followers - lopezobrador_.csv', 'r') as read_obj:
      # pass the file object to reader() to get the reader object
      csv_reader = reader(read_obj)
      # Iterate over each row in the csv using reader object
      for row in csv_reader:
          # row variable is a list that represents a row in csv
          username = row[1]
          if username in users_flags_dict:
            print(users_flags_dict[username])
          else:
            print(0)

def main():
    users_fake_tweet_flags_count, users_tweets_count = processCSVFile()
    
    # print(users_fake_tweet_flags_count)
    # print(users_tweets_count)

    users_flags_dict_normalized = normalizeFakeTweetFlagsByNumberOfTweets(users_fake_tweet_flags_count, users_tweets_count)
    # print(users_flags_dict_normalized)
    buildFinalSuspiciousTweetsColumn(users_flags_dict_normalized)


if __name__ == "__main__":
    main()