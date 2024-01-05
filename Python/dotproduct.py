def cdot(list1, list2):
  # yay so many errors to handle
  if len(list1) != len(list2):
    elist1 = str(len(list1))
    elist2 = str(len(list2))
    raise ValueError("List lengths are different! {elist1} != {elist2}")
  if len(list1) == 0 or len(list2) == 0:
    raise ValueError("One list has a length of 0!")
  dotprod = 0
  for i in range(len(list1)):
    dotprod += (list1[i]*list2[i])
  return dotprod
