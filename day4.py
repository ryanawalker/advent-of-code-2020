input = """""" # input here

# p1
passports = input.split("\n\n")
valid_passports = 0
required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for passport in passports:
  valid = True
  for tag in required:
    if not tag in passport:
      valid = False
      break
  if valid:
    valid_passports += 1

print(valid_passports)

# p2
valid_passports = 0

def byr(string):
  if string.isdigit():
    return int(string) >= 1920 and int(string) <= 2002
  return False

def iyr(string):
  if string.isdigit():
    return int(string) >= 2010 and int(string) <= 2020
  return False

def eyr(string):
  if string.isdigit():
    return int(string) >= 2020 and int(string) <= 2030
  return False

def hgt(string):
  if string[-2:] in "incm":
    if string[:-2].isdigit():
      if string[-2:] == "cm":
        return int(string[:-2]) >= 150 and int(string[:-2]) <= 193
      elif string[-2:] == "in":
        return int(string[:-2]) >= 59 and int(string[:-2]) <= 76
  return False

def hcl(string):
  if string[0] == "#":
    test_set = {"0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","#"}
    return set(string).issubset(test_set)
  return False

def ecl(string):
  return string in {"amb","blu","brn","gry","grn","hzl","oth"}

def pid(string):
  if string.isdigit():
    return len(string) == 9
  return False

def cid(string):
  return True

validations = {
  "byr": byr,
  "iyr": iyr,
  "eyr": eyr,
  "hgt": hgt,
  "hcl": hcl,
  "ecl": ecl,
  "pid": pid,
  "cid": cid
}

def passport_valid(passport):
  for tag_val in passport:
    if not validations[tag_val[0]](tag_val[1]):
      return False
  return True

for passport in passports:
  valid = True
  for tag in required:
    if not tag in passport:
      valid = False
      break
    val = passport.split(tag + ":")[1].split()[0]
    if not validations[tag](val):
      valid = False
      break
  if valid:
    valid_passports += 1

print(valid_passports)
