import pandas as pd
import os
import random

"""
dataset = {'train': [[{'personality': [...], 'utterances': [{'candidates': [...], 
	'history': [...]}, {'candidates': [...], 'history': [...]}]}]], 
	'valid': ...}


    Procedure:
    personality sentences - may need to write them by hand, however only need around 5
    utterances: 7 dicts, each with 20 candidate sentences and anywhere between 1 - 13 history sentences

    removing links:
    import re
    text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)

"""

celebs = "./celeb_data"

# testing reading in tweets
df = pd.read_csv('celeb_data/ArianaGrande_tweets.csv')
data = df.to_dict('records')

# testing building dataset
test_persona = ['i was on tv', 'i have red hair', 'i love long jumpers', 'my favourite thing to do is cook', 
'i have two dogs']
history_appends = 2
candidates_len = 20
history_len = 13
number_of_dicts = 7
history = ['hi! how are you doing?']
utterances = []

for i in range(number_of_dicts):
    this_candidates = []
    this_history = []
    this_utterance = {'candidates': [], 'history': []}
    for t in range(candidates_len):
        this_candidates.append(data[t]['text'])
    
    data = data[candidates_len:]

    if i > 0:
        for i in range(history_appends):
            this_history.append(data[i]['text'])
    
        data = data[history_appends:]
    
    for it, x in enumerate(history):
        this_history.insert(it, x)
    
    history = this_history

    this_utterance['candidates'] = this_candidates
    this_utterance['history'] = this_history
    utterances.append(this_utterance)


this_persona = [{'personality': test_persona, 'utterances': utterances}]



dialog_dataset = {'train': [], 'valid': []}
# Loop through files
for file in sorted(os.listdir(celebs)):
    pass
