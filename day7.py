input = """"""

bag_rules = input.split("\n")
# for part 1
bags_with_gold = set()
# for part 2
rule_dict = {}

# process input
for bag_rule in bag_rules:
  split_bag_rule = bag_rule.split(" bags contain ")

  # part 1, build list of bags that directly contain gold bags
  if "shiny gold" in split_bag_rule[1]:
    bags_with_gold.add(split_bag_rule[0])

  # part 2, build dictionary of what contains what
  if split_bag_rule[1] == "no other bags.":
    rule_dict[split_bag_rule[0]] = [(False)]
  else:
    bags_contained = split_bag_rule[1].split(", ")
    for bag_type in bags_contained:
      split_bag_type = bag_type.split()
      number = int(split_bag_type[0])
      color = " ".join(split_bag_type[1:3])
      if split_bag_rule[0] in rule_dict:
        rule_dict[split_bag_rule[0]].append((number, color))
      else:
        rule_dict[split_bag_rule[0]] = [(number, color)]

# part 1
# my approach here is a recursive function that constantly builds a list of bags that, at some point, contain a gold bag
# basically working backwards from the initial list above and expanding it each time the function is run.
# the function returns a boolean so I know when to stop checking for new bags

def run_check(rules):
  # assume I'll find no bags to add to my list of bags that ultimately have a gold bag in them
  all_checked = True
  new_bags = set()
  for bag_rule in rules:
    split_bag_rule = bag_rule.split(" bags contain ")
    # check if I already know about this bag
    if split_bag_rule[0] not in bags_with_gold:
      # check if this bag contains any bags that are known to contain gold bags
      for bag in bags_with_gold:
        if bag in split_bag_rule[1]:
          # if I find a lineage of gold bags, add this bag to the set and change my boolean flag so I know to recheck for bags containing this bag
          new_bags.add(split_bag_rule[0])
          all_checked = False
  # add all new bags found to contain gold to the set for next time
  bags_with_gold.update(new_bags)
  return all_checked

# run it til it breaks
while True:
  if run_check(bag_rules):
    break

print(len(bags_with_gold))

# part 2
# let's count these bags!! with recursion!!!
bags_inside_gold = 0

def count_inner(bag_color):
  # every bag has at least itself
  count = 1
  contents = rule_dict[bag_color]
  # if it's empty, return
  if contents == [False]:
    return count
  # if it's not empty, count what one would contain and add n of that bag's count to our total
  for bag_type in contents:
    count += count_inner(bag_type[1]) * bag_type[0]
  return count

# starting with all the bags contained in a gold bag, let's get countin'
for req in rule_dict["shiny gold"]:
  count = count_inner(req[1]) * req[0]
  bags_inside_gold += count

print(bags_inside_gold)
