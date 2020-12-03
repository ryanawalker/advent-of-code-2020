input = """""" # input goes here

rows = input.split()
row_size = len(rows[0])
trees_total = 1
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

for slope in slopes:
  x_inc = slope[0]
  y_inc = slope[1]
  trees, x, y = 0, 0, 0

  while True:
    x += x_inc
    y += y_inc
    x %= row_size

    if y >= len(rows):
      trees_total *= trees
      break
    elif rows[y][x] == "#":
      trees += 1
  
  print(slope, trees) # for part 1

print(trees_total) # for part 2
