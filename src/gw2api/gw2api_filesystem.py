import json

def __save_item_json(id, data):
    with open(f'item_{id}.json', 'w', encoding='UTF-16') as outfile:
        outfile.write(json.dumps(data, ensure_ascii=False))
    print(f'File item_{id}.json is saved.')


