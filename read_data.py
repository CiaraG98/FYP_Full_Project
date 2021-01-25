import pandas as pd
import os
import random
import json
"""
dataset = {'train': [[{'personality': [...], 'utterances': [{'candidates': [...], 
	'history': [...]}, {'candidates': [...], 'history': [...]}]}]], 
	'valid': ...}


    Procedure:
    personality sentences - may need to write them by hand, however only need around 5.
    utterances: 7 dicts, each with 20 candidate sentences and anywhere between 1 - 13 history sentences.

    removing links:
    import re
    text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)

"""
celebs = "./celeb_data"
dialog_dataset = {'train': [], 'valid': []}
HISTORY_APPENDS = 2
CANDIDATES_LEN = 20
NUMBER_OF_DICTS = 7

# Loop through files
for file in sorted(os.listdir(celebs)):
    print("Working on", file)
    file = celebs + '/' + file
    # testing reading in tweets
    df = pd.read_csv(file)
    data = df.to_dict('records')

    # testing building dataset
    test_persona1 = ['i was on tv', 'i have red hair', 'i love long jumpers', 'my favourite thing to do is cook', 
    'i have two dogs']
    history = ['hi! how are you doing?']
    utterances = []

    for i in range(NUMBER_OF_DICTS):
        this_candidates = []
        this_history = []
        this_utterance = {'candidates': [], 'history': []}
        for t in range(CANDIDATES_LEN):
            this_candidates.append(data[t]['text'])
        
        data = data[CANDIDATES_LEN:]

        if i > 0:
            for i in range(HISTORY_APPENDS):
                this_history.append(data[i]['text'])
        
            data = data[HISTORY_APPENDS:]
        
        for it, x in enumerate(history):
            this_history.insert(it, x)
        
        history = this_history

        this_utterance['candidates'] = this_candidates
        this_utterance['history'] = this_history
        utterances.append(this_utterance)


    this_persona = [{'personality': test_persona1, 'utterances': utterances}]
    dialog_dataset['train'].append(this_persona)


with open("celebs_dialog_dataset.json", 'w', encoding='utf-8') as f:
    json.dump(dialog_dataset, f, ensure_ascii=False)

print("Done.")