def combine_dicts(dict1, dict2):

  combined_dict = {}
  for key, value in dict1.items():
    combined_dict[key] = value
  for key, value in dict2.items():
    if key not in combined_dict:
      combined_dict[key] = value
    else:
      combined_dict[key] += value
  return combined_dict
