import json
from config import BASE_DIR
def read_json(filename):

    with open('{}/data/'.format(BASE_DIR)+filename,'r',encoding='utf-8') as f:
        err = list()
        for x in json.load(f).values():
            err.append(list(x.values()))

        return err

if __name__ == '__main__':
    print(read_json('login.json'))