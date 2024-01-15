frequency = 0
f = open("2018/Day01/input", "r")
frequency_changes = f.readlines()

i = 0
while i < len(frequency_changes):
    frequency_changes[i] = int(frequency_changes[i])
    frequency = frequency + frequency_changes[i]
    i += 1
    
print(frequency)