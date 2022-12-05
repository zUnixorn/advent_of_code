def solution(lines):
	values = []
	total = 0
	for line in lines:
		if line == "\n":
			values.append(total)
			total = 0
			continue
		total += int(line)
	values.sort(reverse=True)
	return sum(values[0:3])