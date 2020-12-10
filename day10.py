input = """99
151
61
134
112
70
75
41
119
137
158
50
167
60
116
117
62
82
31
3
72
88
165
34
8
14
27
108
166
71
51
42
135
122
140
109
1
101
2
77
85
76
143
100
127
7
107
13
148
118
56
159
133
21
154
152
130
78
54
104
160
153
95
49
19
69
142
63
11
12
29
98
84
28
17
146
161
115
4
94
24
126
136
91
57
30
155
79
66
141
48
125
162
37
40
147
18
20
45
55
83"""

adapters = sorted(list(map(int, input.split())))
adapters.insert(0, 0)
adapters.append(adapters[-1] + 3)

volt = 0
one_volts = 0
three_volts = 0

for adapter in adapters:
  if adapter - 1 == volt:
    one_volts += 1
  elif adapter - 3 == volt:
    three_volts += 1
  volt = adapter

print(one_volts * three_volts)

diffs = []

for i in range(1, len(adapters)):
  diffs.append(adapters[i] - adapters[i - 1])

def checkDiffArrangement(diff_seq):

  # there can only be one permutation of one value
  if len(diff_seq) <= 1:
    return 1

  # these sequences always result in 2 permutations
  if diff_seq in [[1, 1], [1, 2], [2, 1]]:
    return 2
  
  # sequences of diffs of double 2s at start or end
  # or a diff of 3 at the start or the end allow
  # us to immediately shrink the sub sequence,
  # because all chains will have to contain them
  # so it won't affect the number of permutations
  if diff_seq[0] == 2 and diff_seq[1] == 2:
    return checkDiffArrangement(diff_seq[2:])
  if diff_seq[-1] == 2 and diff_seq[-2] == 2:
    return checkDiffArrangement(diff_seq[:2])
  if diff_seq[0] == 3:
    return checkDiffArrangement(diff_seq[1:])
  if diff_seq[-1] == 3:
    return checkDiffArrangement(diff_seq[:-1])

  # same as above, but instead we know to check the
  # sub sequences around either [3] or [2, 2]
  for i in range(1, len(diff_seq)):
    if diff_seq[i] == 3:
      return checkDiffArrangement(diff_seq[0:i]) * checkDiffArrangement(diff_seq[i + 1:])
    if diff_seq[i] == 2 and diff_seq[i + 1] == 2:
      return checkDiffArrangement(diff_seq[0:i]) * checkDiffArrangement(diff_seq[i + 2:])


  # the math behind this is tricky and I don't fully
  # understand it, but basically the number of perms
  # available in any sequence (that doesn't match edge
  # cases above) can be reduced to the number of perms
  # of two separate new sub sequences -- one comprised of
  # all but the first value of the current sub sequence,
  # and the other comprised of the sum of the first two
  # differences of the current sub sequence appended to
  # the front of the rest of the current sub sequence.

  # i.e. checkDiffArrangement(1, 1, 2, 1, 2) is the same
  # as checkDiffArrangement(1, 2, 1, 2) + checkDiffArrangement(1 + 1, 2, 1, 2)

  # don't ask me how that works, I don't fully understand
  # the math involved, but that's the clue that originally
  # got me going down this path
  return checkDiffArrangement(diff_seq[1:]) + checkDiffArrangement([diff_seq[0] + diff_seq[1]] + diff_seq[2:])

print(checkDiffArrangement(diffs))
