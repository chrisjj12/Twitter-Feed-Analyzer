### Twitter-Feed-Analyzer
Utilize both Twitter API and Google NLP API to create a program to analyze the sentiments of a tweet.

## Phase 1
This program will retrieve tweets from any valid twitter handle through json. Then it will parse into the text part of the json to then go through the sentiment analysis, where it will rate the tweet. This program can only analyze 20 tweets at a time so in the command line you have to type something like, "python3 phase_1.py --twitter_username realmadrid --num_tweets 2." The user will type in the twitter handle and the amount of tweets out of 20 to analyze. For example, I used the twitter handle, "realmadrid."

The outcome was:

Tweet 0
🌐 ¡Compromisos internacionales de nuestros madridistas en el día de hoy! 👇
🏆 Liga de Naciones de la UEFA

🇫🇷 Franci… https://t.co/rORg1uPUx2
Overall Sentiment: score of 0.4000000059604645 with magnitude of 1.7999999523162842
Tweet 1
🎾🏆 Nuestro socio de honor @RafaelNadal sigue agigantando su leyenda. Los madridistas de todo el mundo nos sentimos… https://t.co/Jh5mFGaEJI
Overall Sentiment: score of 0.5 with magnitude of 1.5

The two most recent tweets both have positive sentiments.

## Phase 2

The premise of this phase was to apply the sentiment analysis and build my own social media sentiment analyzer. 

MVP: Able to get gauge the sentiment of a given tweet topic (say from a hashtag)
positive or negative.
Who is your user: Twitter users/influencers
USER Stories: As a twitter influencer, I would like to see how certain hashtags are doing by their sentiments.
As a twitter user, I would like to see how popular a hashtag is and if it is 

I altered from phase 1 of analyzing tweets from a specific twitter analyzer to a hashtag. This social media analyzer is to gauge the sentiment of a hashtag at any point in time. This program can only analyze 20 tweets at a time so in the command line you have to type something like, "python3 phase_1.py --twitter_hashtag lakers --num_tweets 2." The user will type in the twitter handle and the amount of tweets out of 20 to analyze. For example, I used the hashtag, "lakers."

The outcome was:

Tweet 0
RT @marktuan: LETS GOO! 2020 CHAMPS! @Lakers
Overall Sentiment: score of 0.30000001192092896 with magnitude of 0.8999999761581421 for this hashtag
Tweet 1
RT @marktuan: Lakers brought it home today guys! #forkobe 💜💛
Overall Sentiment: score of 0.5 with magnitude of 1.0 for this hashtag

At this point of time the Lakers just won the NBA finals so there is a positive sentiment to the hashtags.
