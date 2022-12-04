with open("number") as file:
	content = file.readlines()

values = []
total = 0
for line in content:
	if line == "\n":
		values.append(total)
		total = 0
		continue
	total += int(line)
values.sort(reverse=True)
print(sum(values[0:3]))
