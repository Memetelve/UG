from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import tokenize

# Co to jest za gowno
from text2emotion import get_emotion

sid = SentimentIntensityAnalyzer()

good_opinion = "The apartment has modern furniture and amenities, presenting a very pleasant atmosphere. We were provided with bottles of water, as well as tea and coffee for our convenience. The cleanliness of the place was impeccable, and its location, a mere 10-minute walk from the city center, was ideal. Additionally, finding free parking near the apartment was also hassle-free. Very positive experience!"
bad_opinion = "I wrote that i like a quiet room and i got so so so noisy room 331 if you not a heavy sleeper so dont take it  .. was not possible to leave the bed from my side as it was so near to the window no place to put legs on the floor  .when you take a shower suddenly the water be so cold suddenly so hot .. the chair is so dirty as some places on the Curtain ..not good wifi ..we didnt try the breakfast so no comment about it"

good_opinion_sent = tokenize.sent_tokenize(good_opinion)
bad_opinion_sent = tokenize.sent_tokenize(bad_opinion)

sentences = list(good_opinion_sent) + list(bad_opinion_sent)

for sentence in sentences:

    print(f"Sentence: {sentence}")
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print("{0}: {1}, ".format(k, ss[k]), end="")
    print()


print(get_emotion(good_opinion))
print(get_emotion(bad_opinion))
# Za przeproszeniem kompletny sciek
