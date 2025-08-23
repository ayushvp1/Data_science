emo={"happy":"😄","sad":"😔","love":"🥰🥰"}
res=[]
def emoji():
    ask = input("Enter the statement: ")
        
    for word in ask.split(" "):
        if word in emo:
                res.append(emo[word].lower())
        else:
                res.append(word+" ")
                
    print(" ".join(res))

emoji()