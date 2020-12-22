import json
from pytorch_pretrained_bert import cached_path


# s3 bucket!!
url = "https://s3.amazonaws.com/datasets.huggingface.co/personachat/personachat_self_original.json"

# Writing some sample personas to txt file
file_name = "SamplePersona.txt"
fw = open(file_name, 'a')

# Download and load JSON dataset
personachat_file = cached_path(url)
print(personachat_file)
with open(personachat_file, "r", encoding="utf-8") as f:
    dataset = json.loads(f.read())
    
    for i, persona in enumerate(dataset['train']):
        if i <= 3:
            label = "PERSONA " + str(i)
            # write sample json to file
            fw.write(label + "\n")
            fw.writelines(persona['personality'])
            fw.write('\n')
            fw.writelines(persona['utterances'][0]['candidates'][:5])
            fw.write('\n')
        