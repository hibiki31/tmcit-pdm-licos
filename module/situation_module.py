import re

import spacy

import module.name_module as name
import module.status_module as status

dict = ["人狼","占い師","村人","狂人","狩人","霊能力者","霊能者"]

def CO_check(token):
  COTokenList = []

  for part in token:
    if part[0] == 'プロローグ':
      continue
    if part[2] != '':
      if '■' in part[3]:
        continue
      if '【' in part[3]:
        m = part[3].split('【')
        n = []
        for mpart in m:
          if '】' in mpart:
            n.append(mpart.split('】')[0].lower())
        for o in n:
          for role in dict:
            if role in o:
              if not 'ない' in o and not 'ません' in o:
                list = [part[1], part[2], o, role]
                COTokenList.append(list)
  nlp = spacy.load('ja_ginza')
  for COToken in COTokenList:
    reslist = name.token_part(COToken[2], nlp)
    if len(reslist) < 10:
      if COToken[1] == '狂人' and COToken[3] != '狂人':
        status.save(COToken[1], '偽る役職', COToken[3])
        status.save(COToken[1], '自身が偽COしているか', True)
      elif COToken[1] == COToken[3]:
        status.save(COToken[1], '自身がCOしているか', True)
