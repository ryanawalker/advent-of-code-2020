input = """"""

passes = input.split()

# for part 1
biggest_id = 0
# for part 2
id_set = set()

for boarding_pass in passes:
  x_min = 0
  x_max = 127
  y_min = 0
  y_max = 7
  vert_inst = boarding_pass[0:7]
  hori_inst = boarding_pass[7:]
  
  for inst in vert_inst:
    if inst == "F":
      x_max -= round((x_max - x_min) / 2)
    else:
      x_min += (x_max - x_min) // 2 + 1
  for inst in hori_inst:
    if inst == "L":
      y_max -= round((y_max - y_min) / 2)
    else:
      y_min += (y_max - y_min) // 2 + 1
  
  seat_id = x_min * 8 + y_min
  if seat_id > biggest_id: # part 1
    biggest_id = seat_id
  id_set.add(seat_id) # part 2

print(biggest_id) # part 1

for id in range(min(id_set), max(id_set)):
  if id not in id_set:
    print(id) # part 2
