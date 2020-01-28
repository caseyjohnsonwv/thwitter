import re

def make_thread(text, simplify_whitespace=True):
    """
    text: str
    return: List[str]
    """
    thread = []
    tweet = ""
    punc = "([\.\-,;:\s!\?]+)"
    if simplify_whitespace:
        text = re.sub('\s+',' ',text)
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
        # no previous punctuation - break with elipsis mid-word
        else:
            tweet += words[i]
            while len(tweet) > 240:
                tweet,overflow = tweet[:237],tweet[237:]
                tweet += "..."
                thread.append(tweet.strip())
                tweet = "..." + overflow
        #next word
        i += 1
    #append leftovers to thread
    thread.append(tweet.strip())
    return thread
