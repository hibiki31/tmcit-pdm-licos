import json
import requests
from pprint import pprint

import logging

import random


from module.test import main as module_test


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
        ld_swicher(json_data)


def dummy_client(json_data):
    pprint(json_data)


def ld_swicher(json_data):
    now_phase = json_data.get('phase')
    print(now_phase)

    if now_phase == 'flavor text':
        some_module(json_data)
    elif now_phase == 'noon':
        some_module(json_data)



def some_module(json_data):
    pass
    # pprint(json_data)
    # kokoni書いてちょ
if __name__ == "__main__":
    main()