from pathlib import Path
import timeit
#Task: How many measurements are larger than the previous measurement?
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
previous_measurement_value = 0
counter_for_larger_previous_measurments = 0
sea_floor_measurements = open(".\AOC_2021_day1_input.txt", "r")
for line in sea_floor_measurements:
    current_value = int(line.rstrip("\n"))

    if current_value > previous_measurement_value:
        if previous_measurement_value == 0: #for initial value - does not count as higher measurment
            previous_measurement_value = current_value
            print("Inital value:" + str(current_value))
        else:
            print(str(current_value) + " (increased)")
            previous_measurement_value = current_value
            counter_for_larger_previous_measurments += 1 
    elif current_value < previous_measurement_value:
        print(str(current_value) + " (decreased)")
        previous_measurement_value  = current_value
    else:
        print(str(current_value) + " (increased)")
        counter_for_larger_previous_measurments += 1 
sea_floor_measurements.close()

print("There are " + str(counter_for_larger_previous_measurments) + " times higher measurments than the previous measurement.")
print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)) 