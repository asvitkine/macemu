#!/usr/bin/python

import sys

files = sys.argv[1:]
for filename in files:
  print(filename)
  with open(filename) as file:
    lines = file.readlines()

  with open(filename, "w") as file:
    last_include_index = 0
    i = 0
    for line in lines:
      if line.strip().startswith('#include'):
        last_include_index = i
      i = i + 1
    i = 0
    for line in lines:    
      file.write(line)
      if i == last_include_index:
        file.write('\nnamespace SS {\n')
      if i == len(lines) - 1:
        file.write('\n}  // namespace SS\n')
      i = i + 1
