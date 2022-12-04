with open("number") as file:
	content = file.readlines()

max = 0
total = 0
for line in content:
	if line == "\n":
		if total > max:
			max = total
		total = 0
		continue
	total += int(line)

print(max)
