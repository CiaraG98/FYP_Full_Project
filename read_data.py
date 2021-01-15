import pandas as pd
import os
import random

celebs = "./celeb_data"
"""
dataset = {'train': [[{'personality': [...], 'utterances': [{'candidates': [...], 
	'history': [...]}, {'candidates': [...], 'history': [...]}]}]], 
	'valid': ...}
"""
"""
    Procedure:
    personality sentences - may need to write them by hand, however only need around 5
    utterances: 7 dicts, each with 20 candidate sentences and anywhere between 1 - 13 history sentences

"""
# testing reading in tweets
df = pd.read_csv('celeb_data/ArianaGrande_tweets.csv')
data = df.to_dict('records')

#testing building dataset
test_persona = ['i was on tv', 'i have red hair', 'i love long jumpers', 'my favourite thing to do is cook', 
'i have two dogs']
history_appends = 2
candidates_len = 20
history_len = 13
number_of_dicts = 7
utterances = []
candidates = []
history = ['hi! how are you doing?']

for i in range(number_of_dicts):
    for i in range(candidates_len):
        candidates.append(data[i]['text'])
    
    data = data[candidates_len:]
    
    if i > 0:
        this_history = []
        for tweet in data[:history_appends]:
            this_history.append(tweet['text'])
        history.extend(this_history)
    data = data[history_appends:]

    this_utterance = {'candidates': candidates, 'history': history}
    utterances.append(this_utterance)

this_persona = [{'personality': test_persona, 'utterances': utterances}]
print(this_persona)


dialog_dataset = {'train': [], 'valid': []}
# Loop through files
for file in sorted(os.listdir(celebs)):
    pass
