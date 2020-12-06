input = """"""

groups = input.split("\n\n")
total_p1, total_p2 = 0, 0

for group in groups:
  # part 1
  total_p1 += len(set(group.replace("\n", "")))
  # part 2
  passengers = group.split("\n")
  if len(passengers) == 1:
    total_p2 += len(passengers[0])
  else:
    answer_sets = list(map(set, passengers))
    for answer in answer_sets[0]:
      all_yes = True
      for answer_set in answer_sets[1:]:
        if answer not in answer_set:
          all_yes = False
          break # should make it slightly faster
      if all_yes:
        total_p2 += 1       

print(total_p1, total_p2)
