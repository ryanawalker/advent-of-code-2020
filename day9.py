input = """"""

datastream = list(map(int, input.split("\n")))

# part 1

def is_valid_sum(num_list, target):
  for i in range(len(num_list) - 1):
    for j in range(i + 1, len(num_list)):
      if num_list[i] + num_list[j] == target:
        return True
  return False

def part1():
  for idx in range(25, len(datastream)):
    if not is_valid_sum(datastream[idx - 25:idx], datastream[idx]):
      return datastream[idx]

# part 2

p2_target = part1()

def part2():
  for i in range(len(datastream)):
    acc = datastream[i]
    acc_pointer = i
    set_vals = {datastream[i]}
    while not acc >= p2_target:
      acc_pointer += 1
      if acc_pointer >= len(datastream):
        break
      acc += datastream[acc_pointer]
      set_vals.add(datastream[acc_pointer])
    if acc == p2_target:
      return min(set_vals) + max(set_vals)

print(p2_target, part2())
