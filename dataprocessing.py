import xmltodict
import sklearn
from textblob import TextBlob
import nltk

# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()


f = open("all.review",'rb')

data = f.readlines()

textList = []
rateList = []
# print(data)
for i in range(len(data)):
    if data[i].strip() == b'<review_text>':
        textList.append(data[i+1])
    if data[i].strip() == b'<rating>':
        rateList.append(data[i+1])

tf = open("text.txt","w+")
rf = open("rate.txt","w+")

# print(len(textList)==len(rateList))
pcount = 0
ncount = 0

for i in range(len(textList)):
    # break
    if rateList[i] == b'3.0\n':
        continue
    if rateList[i] == b'4.0\n':
        rf.write(str(1))
        rf.write('\n')
        pcount = pcount + 1
    if rateList[i] == b'5.0\n':
        rf.write(str(1))
        rf.write('\n')
        pcount = pcount + 1
    if rateList[i] == b'2.0\n':
        rf.write(str(0))
        rf.write('\n')
        ncount = ncount + 1
    if rateList[i] == b'1.0\n':
        rf.write(str(0))
        rf.write('\n')
        ncount = ncount + 1
    text = textList[i]
    text = text.decode(errors = 'ignore')
    blob = TextBlob(text)
    # blob = blob.sentences
    # sum = 0.0
    # count = 0
    # for sentence in blob:
    #     sum = sentence.sentiment.polarity
    #     count = count + 1
    # if count == 0: 
    #     count = 1
    # sentiValue = sum/count
    # blob1 = TextBlob("I want to start by saying Fred Flare- shipped this product very fast!!")
    # print(blob1.sentiment.polarity)
    # blob2 = TextBlob("I want to start by saying Fred Flare- shipped this product very fast!! And the transaction itself was very smooth. I do however, have extreme problems with the product itself. The product is not leather, its nylon, and it sort of looks cheap? The inside material is sued, but that's only the lining for the base of the wallet. Also, The wallet part is very hard to use. You cant really put too much in the wallet- The credit card slots are a little too snug, and there is no place for my I.D. The wallet included a small 'note book' but it also doesn't fit in the wallet? I was very excited about this product, but now I feel duped. The pictures made the wallet seem like it was of higher quality, and that it was user friendly, but it's not. I do not recommend this product")
    # print(blob2.sentiment.polarity)
    # break

    sentiValue = blob.sentiment.polarity
    sentisub = blob.sentiment.subjectivity
    # if(sentiValue==0):
    #     print(blob)
    tf.write(str(sentiValue))
    tf.write(',')
    tf.write(str(sentisub))
    tf.write('\n')
    # tf.write('\n')
    # rate = (rateList[i].decode())
    # rf.write(rate)
    # rf.write('\n')


# tf.write(textList.decode())
# rf.write(rateList.decode())




print(pcount/(pcount+ncount))


tf.close()
rf.close()
f.close()

# print(data)
