def firstMorning(json_data):
  my_character = myCharacter(json_data)
  my_role = myRole(json_data)
  return {'phase': 'firstMorning', 'isMine': my_character, 'character': json_data.get('character'), 'role': json_data.get('role'), 'my_role': my_role}

def noon(json_data):
  my_character = myCharacter(json_data)
  my_role = myRole(json_data)
  return {'phase': 'noon', 'isMine': my_character, 'character': json_data['character'], 'role': json_data.get('role'), 'my_role': my_role}


def myCharacter(json_data):
  for character in json_data['character']:
    if character['isMine']:
      return character

def myRole(json_data):
  for role in json_data['role']:
    if role['isMine']:
      return role