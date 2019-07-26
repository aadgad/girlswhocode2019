import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import matplotlib.pyplot as plot
import matplotlib.pyplot as scat
import matplotlib.pyplot as plt2
from wordcloud import WordCloud


#Get the JSON data
tweetFile = open("tweetdata.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
subj = []
polarity = []
bigtweet = ""

for i in tweetData:
    tweet = i["text"]
    tweettext = TextBlob(tweet)
    polarity.append(tweettext.sentiment.polarity)
    subj.append(tweettext.sentiment.subjectivity)

    bigtweet+=tweet

bigblob = TextBlob(bigtweet)
filteredwords = {}
notwanted = ["like", "the", "that", "but", "for", "https", "about", "etc", "you", "your", "our", "what", "who", "got", "else", "did", "were", "where", "are", "was", "too", "not", "will",
"see", "from", "can", "could", "with", "say", "out", "out", "and", "they", "how"]

wordsList = bigblob.words
for word in wordsList:
    word2 = word.lower()
    if not word2.isalpha():
        continue
    if len(word2) < 3:
        continue
    if word2  in notwanted:
        continue
    filteredwords[word2] = bigblob.word_counts[word2]

wc = WordCloud().generate_from_frequencies(filteredwords)
plt2.figure()
plt2.imshow(wc, interpolation = "bilinear")
plt2.axis("off")
plt2.show()
print(filteredwords)



#calculates average for polarity
polarsum = 0
polaravg = 0
count = 0
for polar in polarity:
    polarsum+=polar
    count+=1
    polaravg = polarsum/count
print("The average polarity is  ")
print(polaravg)

print(len(polarity))


#calculates average for subjectivity
subjsum = 0
subjavg = 0
count2 =0
for subject in subj:
    subjsum+=subject
    count2+=1
    subjavg = subjsum/count2
print("The average subjectivity is  ")
print(subjavg)


plt.ylabel("number of tweets")
plt.xlabel("polarity values")
plt.title("histogram of polarities")
plt.hist(polarity, bins = [-1.1, -.75, -0.5, -.25, 0, 0.25, 0.5, 0.75, 1.1])
plt.axis([-1, 1, 0, 75])

plt.grid(True)
plt.show()


plot.ylabel("number of tweets")
plot.xlabel("subjectivity values")
plot.title("histogram of subjectivities")
plot.hist(subj, bins = [ 0, 0.25, 0.5, 0.75, 1.1])
plot.axis([ 0, 1, 0, 75])

plot.grid(True)
plot.show()

scat.ylabel("subjectivity values")
scat.xlabel("polarity values")
scat.title("histogram of subjectivity vs polarity")
scat.scatter(polarity, subj)
#scat.show()
