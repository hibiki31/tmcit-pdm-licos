import json
import requests
from pprint import pprint

import logging

import random


from module.test import main as module_test
import module.sentence_module as sentence
import module.status_module as status
import module.io_module as io
import module.token_module as tokens
import module.situation_module as situation
import module.name_module as name
import module.parse_module as parse

def setup_logger(name, logfile=f'main.log'):
    logger = logging.getLogger(name)

    # ファイル出力設定
    fh = logging.FileHandler(logfile)
    fh_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(funcName)s - %(message)s')
    fh.setFormatter(fh_formatter)

    # コンソール出力設定
    ch = logging.StreamHandler()
    ch_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
    ch.setFormatter(ch_formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    # 全体のログレベル
    logger.setLevel(logging.DEBUG)
    # ファイル出力のログレベル
    fh.setLevel(logging.INFO)
    # コンソール出力のログレベル
    ch.setLevel(logging.DEBUG)

    return logger

logger = setup_logger(__name__)

def main():
    dummy_server()

def dummy_server():
    urls = [
        "https://werewolf.world/village/example/0.3/server2client/flavorText.jsonld",
        "https://werewolf.world/village/example/0.3/server2client/firstMorning.jsonld",
        "https://werewolf.world/village/example/0.3/server2client/morning.jsonld",
        "https://werewolf.world/village/example/0.3/server2client/noon.jsonld",
        "https://werewolf.world/village/example/0.3/server2client/night.jsonld",
        "https://werewolf.world/village/example/0.3/server2client/result.jsonld",
        "https://werewolf.world/village/example/0.3/server2client/myMessageOnChat.jsonld",
        "https://werewolf.world/village/example/0.3/server2client/theirMessageOnChat.jsonld",
        "https://werewolf.world/village/example/0.3/client2server/chat.jsonld",
        "https://werewolf.world/village/example/0.3/client2server/noonVote.jsonld",
        "https://werewolf.world/village/example/0.3/client2server/nightVote.jsonld",
    ]

    for url in urls:
        response = requests.get(url)
        json_data = response.json()
        res = ld_swicher(json_data)
        if res != {}:
          # fetch myRole
          target_role = res['my_role']['name']['ja']
          print(target_role)
          #output = bot(res, target_role)
          #print(output)



def dummy_client(json_data):
    pprint(json_data)


def ld_swicher(json_data):
    res = {}
    now_phase = json_data.get('phase')
    now_day = json_data.get('day')
    id = json_data.get('@id')
    print(now_day)
    print(now_phase)
    print(id)

    if now_phase == 'flavor text':
        some_module(json_data)
    elif now_phase == 'noon' and id == 'https://licos.online/state/0.3/village#3/voteMessage':
        some_module(json_data)
    elif now_phase == 'noon':
        res = parse.noon(json_data)
    elif now_phase == 'morning' and now_day == 1 and id == 'https://licos.online/state/0.3/village#3/systemMessage':
        res = parse.firstMorning(json_data)

    return res


def some_module(json_data):
    pass
    # pprint(json_data)
    # kokoni書いてちょ

def vote(json_data, id):
  for target in character_list:
    if target['id'] == id:
      json_data['character']['id'] = target['id']
      json_data['character']['name']['en'] = target['name']['en']
      json_data['character']['name']['ja'] = target['name']['ja']
      json_data['character']['image'] = target['image']

  return json.dumps(json_data)

# csv: [[日付,プレイヤー名,役職,発言],[日付,プレイヤー名,役職,発言],...]
# target_role: 自身のプレイヤー名
def bot(csv, target_role):
  if target_role == None:
      print("入力データが不正です")
      exit

  status.init()
  tokenize_csv = tokens.token(csv)

  names = name.name_setlist(csv)
  nicknames = name.nickname_setlist(tokenize_csv)
  names_dict = name.name_dict(name.name_similar_nickname(names,nicknames))

  for n in names:
    status.save("プレイヤー名ID",str(names.index(n)),n)
    status.save("プレイヤー名",n,str(names.index(n)))
    status.save("プレイヤーニックネーム",str(names.index(n)),names_dict[n][0])

  situation.CO_check(csv)
  output_sentence = sentence.sentence_moddule(target_role)

  return output_sentence

if __name__ == "__main__":
    main()
