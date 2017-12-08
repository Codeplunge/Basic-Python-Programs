def remove_duplicates(list1):
  result=[]
  for index,x in enumerate(list1):
    if x not in list1[index+1:]:
      result.append(x)
  return result
