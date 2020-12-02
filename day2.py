input = """""" # input goes here

password_list = input.split("\n")

p1_num_valid = 0
p2_num_valid = 0

for entry in password_list:
  elements = entry.split(" ")
  password = elements[2]
  vals = elements[0].split("-")
  first_val = int(vals[0])
  second_val = int(vals[1])
  check_char = elements[1][0]

  # part 1
  count = password.count(check_char)
  if count >= first_val and count <= second_val:
    p1_num_valid += 1

  # part 2
  first_pos_check = password[first_val - 1] == check_char
  second_pos_check = password[second_val - 1] == check_char
  if first_pos_check:
    if not second_pos_check:
      p2_num_valid += 1
  elif second_pos_check:
    p2_num_valid += 1

print(p1_num_valid, p2_num_valid)
