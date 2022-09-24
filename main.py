from twitter import get_twitter_text
from analyser import my_sentiment_analyser


options = {
  "mobile": ["display","battery","price"],
  "laptop": ["display","battery","RAM","graphic card","price"],
  "vehicle": ["mileage","price","engine","lights"],
  "college": ["faculty","placement","campus","fee"],
  "others":[]
}

s=input("type keyword:- ")
print("\n\noptions:-")
for i in options.keys():
    print(i)

o=input("type option:- ")
mylist=options.get(o)
if(len(mylist)==0):
    df=get_twitter_text(s)
    if df.shape[0]!=0:
        print("twitter rates: ",s,str(my_sentiment_analyser(df))+"/5")
else:
    for i in mylist:

        df=get_twitter_text(s+" AND "+i)
        if df.shape[0]==0:
            continue
        print("twitter rates: ",i,str(my_sentiment_analyser(df))+"/5")
