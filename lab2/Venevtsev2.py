import csv
import time
import matplotlib.pyplot as plt

filename = input("Enter the path to the csv file: ")
ip = input("Enter the IP address to check: ")

rows = []
fields = []
input_time = []
output_time = []
input_traffic = []
output_traffic = []
k = 1.0
bonus = 1000.0
inp = 0
out = 0

with open(filename, 'r') as file:
    reader = csv.reader(file)
    fields = next(reader)
    for row in reader:
        rows.append(row)
        
def inp_trf():
    global inp
    for row in rows[:reader.line_num]:
        if ip in row[4]:
            inp += int(row[12])
            input_time.append(row[0])
            input_traffic.append(inp)
            
    return inp

def out_trf():
    global out
    for row in rows[:reader.line_num]:
        if ip in row[3]:
            out += int(row[12])
            output_time.append(row[0])
            output_traffic.append(out)
    return out
traf_sum_mb = (inp_trf() + out_trf()) / 1048576
All = (traf_sum_mb - bonus)*k
while All<0:
    bonus /= 1024
    All = (traf_sum_mb - bonus)*k
print(All, " Rubles to pay")

input_time.sort()
input_traffic.sort()
output_traffic.sort()
output_time.sort()

if len(output_traffic) == 0: 
	print("The input and total traffic graphs are the same, since the output traffic is 0")
	plt.plot(input_time,input_traffic, label='Graph of input and total traffic')
elif len(input_traffic) == 0:
	print("The output and total traffic graphs are the same, since the input traffic is 0")
	plt.plot(output_time,output_traffic, label='Output and total traffic graph')
else:
	plt.plot(input_time,[x+y for x, y in zip(input_traffic, output_traffic)], label='Total traffic')
	plt.plot(input_time,input_traffic, label='Input trafficê')
	plt.plot(output_time,output_traffic, label='Output traffic')
plt.xlabel('Time')
plt.ylabel('Traffic size')
plt.title('The graphs of traffic consumption from time to time\n')
plt.legend()