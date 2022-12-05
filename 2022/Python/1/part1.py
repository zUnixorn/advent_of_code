def solution(lines):
	max = 0
	total = 0
	for line in lines:
		if line == "\n":
			if total > max:
				max = total
			total = 0
			continue
		total += int(line)
	return max