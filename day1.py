input = """""" # input goes here

def process_input(prompt):
  split_input = input.split("\n")
  return [int(num) for num in split_input]

def part1(prompt):
  ledger = process_input(prompt)
  for i in range(len(ledger)):
    for j in range(i + 1, len(ledger)):
      if ledger[i] + ledger[j] == 2020:
        return ledger[i] * ledger[j]

def part2(prompt):
  ledger = process_input(prompt)
  for i in range(len(ledger)):
    for j in range(i + 1, len(ledger)):
      for k in range(j + 1, len(ledger)):
        if ledger[i] + ledger[j] + ledger[k] == 2020:
          return ledger[i] * ledger[j] * ledger[k]

print(part1(input))
print(part2(input))
