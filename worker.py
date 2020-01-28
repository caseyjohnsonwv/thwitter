import re

def make_thread(text):
    """
    text: str
    return: List[str]
    """
    thread = []
    tweet = ""
    punc = "([\.\-,;:\s!\?]+)"
    words = re.split(punc, text)
    i,j,breakpoint = 0,0,0
    while i < len(words):
        #record for frequent use
        j = len(tweet)
        # record punctuation marks as tweet breakpoints
        if re.match(punc, words[i]):
            breakpoint = j + len(words[i])
        # add word to tweet if length permits
        if j + len(words[i]) < 240:
            tweet += words[i]
        # tweet is full - try to break at last punctuation
        elif breakpoint > 0:
            tweet = tweet[:breakpoint]
            thread.append(tweet.strip())
            tweet = words[i]
            breakpoint = 0
        # no previous punctuation - break with elipsis between words
        elif j <= 237:
            tweet += "..."
            thread.append(tweet.strip())
            tweet = words[i]
        # cannot break between words; break mid-word
        else:
            pass
        #next word
        i += 1
    #append leftovers to thread
    thread.append(tweet.strip())
    return thread

#text = "this is for rachel you big fat white nasty smelling fat bitch, why you took me off the motherfuckin schedule with your trifflin dirty white racist ass you big fat oompa loompa body ass bitch. I'm coming up there and I'm gonna beat the fuck out of you bitch and don't even call the police today 'cause I'm gonna come up there unexpected and wait on your motherfuckin ass bitch."
text = "ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
th = make_thread(text)
for tweet in th:
    print(tweet)
    print("---")
