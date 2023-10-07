def get_highest_3_values(dict1):

  dict_list = list(dict1.items())

  dict_list.sort(key=lambda item: item[1], reverse=True)

  highest_3_values = dict_list[:3]

  highest_3_values_dict = dict(highest_3_values)

  return highest_3_values_dict
