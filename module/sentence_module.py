# -*- coding: utf-8 -*-
from . import status_module as status
import random

def sentence_moddule(role_name):
	uid_dict = {1:'ならず者ディーター',2:'シスターフレーデル'}
	ans_dict = {True:'白',False:'黒'}

	if role_name == '占い師' :

		if status.load(role_name,'自身がCOしているか') == False:
			status.save(role_name,'自身がCOしているか',True)
			return '私は占い師です。'

		elif status.load(role_name,'占いを既に言ったか',) == False:
			status.save(role_name,'占いを既に言ったか',True)
			uid = status.load(role_name,'スキル対象')
			ans = status.load(role_name,'スキル結果')
			return ('%sは%sでした。' %(uid_dict[uid],ans_dict[ans]))

		elif status.load(role_name,'占い先を指定されたか') == True:
			status.save(role_name,'占い先を指定されたか',False)
			uid = status.load(role_name,'占い先指定')
			return ('%sさんを占います。' %(uid_dict[uid]))

		else:
			return ('今日もいい天気。明日は%sかな' %(otenki()))

	elif role_name == '霊能者':
		if status.load(role_name,'自身がCOしているか') == False:
			status.save(role_name,'自身がCOしているか',True)
			return '私は霊能者です。'

		elif status.load(role_name,'霊能を既に言ったか',) == False:
			status.save(role_name,'霊能を既に言ったか',True)
			uid = status.load(role_name,'スキル対象')
			ans = status.load(role_name,'スキル結果')
			return ('%sは%sでした。' %(uid_dict[uid],ans_dict[ans]))

		else:
			return ('今日もいい天気。明日は%sかな' %(otenki()))

	elif role_name == '狂人':
		if status.load(role_name,'偽る役職') == '占い師':
			if status.load(role_name,'自身が偽COしているか') == False:
				status.save(role_name,'自身が偽COしているか',True)
				return '私は占い師です。'

			elif status.load(role_name,'偽占いを既に言ったか',) == False:
				status.save(role_name,'偽占いを既に言ったか',True)
				uid = status.load(role_name,'偽スキル対象')
				ans = status.load(role_name,'偽スキル結果')
				return ('%sは%sでした。' %(uid_dict[uid],ans_dict[ans]))

			elif status.load(role_name,'偽占い先を指定されたか') == True:
				status.save(role_name,'偽占い先を指定されたか',False)
				uid = status.load(role_name,'占い先指定')
				return ('%sさんを占います。' %(uid_dict[uid]))

		elif status.load(role_name,'偽る役職') == '霊能者':
			if status.load(role_name,'自身が偽COしているか') == False:
				status.save(role_name,'自身が偽COしているか',True)
				return '私は霊能者です。'

			elif status.load(role_name,'偽霊能を既に言ったか',) == False:
				status.save(role_name,'偽霊能を既に言ったか',True)
				uid = status.load(role_name,'偽スキル対象')
				ans = status.load(role_name,'偽スキル結果')
				return ('%sは%sでした。' %(uid_dict[uid],ans_dict[ans]))

		else:
			return ('今日もいい天気。明日は%sかな' %(otenki()))

	elif role_name == '狩人':
		if status.load(role_name,'自身がCOしているか') == False:
			if status.load(role_name,'他人がCOしているか') == True:
				uid = status.load(role_name,'対抗先')
				status.save(role_name,'自身がCOしているか',True)
				return ('私が狩人です。%sさんは偽物ですね。' %(uid_dict[uid]))
			elif status.load(role_name,'自身へ吊り指定') == True:
				return '私が狩人です。'
			else:
				return ('今日もいい天気。明日は%sかな' %(otenki()))

		else:
			return ('今日もいい天気。明日は%sかな' %(otenki()))

	elif role_name == '共有者':
		if status.load(role_name,'自身がCOしているか') == False:
			status.save(role_name,'自身がCOしているか',True)
			uid = status.load(role_name,'相方')
			return ('共有者です。相方は%sさんです' %(uid_dict[uid]))

		else:	
			return ('今日もいい天気。明日は%sかな' %(otenki()))

	elif role_name == '村人':
		return ('今日もいい天気。明日は%sかな' %(otenki()))

	elif role_name == '人狼':
		if status.load(role_name,'自身への吊り指定') == True:
			status.save(role_name,'偽る役職','狩人')
			return '自分は狩人です'
		return ('今日もいい天気。明日は%sかな' %(otenki()))


	else:
		return

def otenki():
	wet = ['晴','雨','曇り','雪','嵐']
	return random.choice(wet)



def main():
	while True:
		print('Input:role name')
		text = input()
		print('Output:sentences ')
		print(sentence_moddule(text))
		if text == '':
			break


if __name__ == "__main__":
    main()
	