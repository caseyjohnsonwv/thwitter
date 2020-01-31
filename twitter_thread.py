import re

PUNCTUATION = {'.','-',',',';',':',' ','!','?'}

def make_thread(text, preserve_whitespace=False):
    """
    text: str
    return: List[str]
    """
    thread = []
    if not preserve_whitespace:
        text = re.sub('\s+',' ',text)
    start = 0
    while start + 280 < len(text):
        end = start + 279
        # if end points to multiple punctuation marks, don't break here- keep punctuation together
        while end > 0 and text[end] in PUNCTUATION:
            end -= 1
        # backtrack to next viable breakpoint
        while end > 0 and text[end] not in PUNCTUATION:
            end -= 1
        if end > 0:
            tweet = text[start:end+1]
        else:
            end = start+277
            tweet = text[start:end]+"..."
        thread.append(tweet)
        start = end
    # append leftover text to thread
    thread.append(text[start:])
    # strip ending whitespaces
    if not preserve_whitespace:
        thread = [tweet.strip() for tweet in thread]
    return thread
