input = """"""

instructions = input.split("\n")

def check_program(inst_arr):
  idx, acc = 0, 0
  seen_locations = set()
  inst_arr_len = len(inst_arr)

  while True:
    seen_locations.add(idx)
    instruction = inst_arr[idx].split()

    if instruction[0] == "acc":
      acc += int(instruction[1])
      idx += 1
    elif instruction[0] == "jmp":
      idx += int(instruction[1])
    else:
      idx += 1
    
    # part 1, also saves time in part 2
    if idx in seen_locations:
      return (False, acc)
    # part 2, part 1 will never reach here
    elif idx == inst_arr_len:
      return (True, acc)


# part 1
print(check_program(instructions)[1])

# part 2
def p2(inst):
  for idx, instruction in enumerate(inst):
    if instruction[0] != "acc":
      temp_list = list(instructions)
      if instruction[0] == "nop":
        temp_list[idx] = "jmp"
      else:
        temp_list[idx] = "nop"
      
      results = check_program(temp_list)
      if results[0]:
        return results[1]

print(p2(instructions))
