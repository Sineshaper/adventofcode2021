from pathlib import Path
import timeit

# def compare(p1, p2):
#     if p1 > p2: 
#         return p1
#     else:
#         return p2
def extractValue (data):
    return [int(s) for s in data.split() if s.isdigit()]

#Task: How many measurements are larger than the previous measurement?
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
depth = 0
distance = 0
orientation = [ "forward", "down", "up"]
navigationplan = []
# for example C:\\yourrepo\\file.txt
pathtofile = "path\\AOC_2021_day2_input.txt"
reader = open(pathtofile, "r")
for line in reader:
    line.replace(" ", "_")
    navigationplan.append(line.rstrip("\n"))
reader.close()

for point in navigationplan:
    if point.startswith(tuple(orientation)): 
        position = point.split(' ',1 )
        print(position)
        if position[0] == orientation[0]:
            distance += int(position[1])#extractValue(point)
        elif position[0] == orientation[1]:
            depth += int(position[1])
        elif position[0] == orientation[2]:
            depth -= int(position[1])
        else:
            print("nothing to do")
    else:
        print("nothing happend")

print ("distance:\t" + str(distance) + "\ndepth:\t" + str(depth))
print("Goal: " + str(distance * depth))
print("Executiontime:" + str(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)))