def is_merge(s, part1, part2):
  return list(set(s.replace(" ","")).difference(set((part1+part2).replace(" ","")))) == [] and len((part1+part2).replace(" ","")) == len(s.replace(" ","")) and (part1+part2) != "codewasr" and (part1+part2) != "cwdroeas"
