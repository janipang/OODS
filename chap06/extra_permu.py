def permute(s):
  out = []
  if len(s) == 1:
    return s
  else:
    for i,let in enumerate(s):
      print(f"permute({s[:i]} + {s[i+1:]})")
      for perm in permute(s[:i] + s[i+1:]):
        out += [let + perm]
        print(f"let + perm = {let + perm}")
  return out

l = permute(['c','a','t'])
print(l)