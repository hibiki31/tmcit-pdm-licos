import spacy

def token_part(sentence,nlp):
  doc = nlp(sentence)
  result_list = []
  for sent in doc.sents:
    for token in sent:
      info_dict = {}
      info_dict["num"]             = token.i             # トークン番号（複数文がある場合でも0に戻らず連番になる）
      info_dict["text"]         = token.orth_         # オリジナルテキスト
      info_dict["pos_"]          = token.pos_          # 品詞(UD)
      info_dict["inf"]         = token._.inf         # 活用情報
      info_dict["rank"]          = token.rank          # 頻度のように扱えるかも
      info_dict["is_oov"]        = token.is_oov        # 登録されていない単語か？
      info_dict["list(.lefts)"]   = list(token.lefts)   # 関連語まとめ(左)
      info_dict["list(.rights)"]  = list(token.rights)  # 関連語まとめ(右)
      info_dict["dep_"]          = token.dep_          # 係り受けの関係性
      info_dict["head.i"]        = token.head.i        # 係り受けの相手トークン番号
      info_dict["head.text"]     = token.head.text     # 係り受けの相手のテキスト
      result_list.append(info_dict)
  return result_list

def token(sentence):
  nlp = spacy.load('ja_ginza')
  for part in sentence:
    res = token_part(part[3], nlp)
    part.append(res)
  return sentence
