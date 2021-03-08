import csv
with open('height-weight.csv',newline = '')as f:
    reader = csv.reader(f)
    file_data = list(reader)
    #print(file_data)
file_data.pop(0) 
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append((n_num))
n = len(new_data)
new_data.sort()
print("sorted data: "+ str(new_data))
print("length of list: " + str(n))
if n%2 == 0:
    median1 = float(new_data[n//2])
    print("n//2"+str(n//2))
    median2 = float(new_data[n//2-1])
    print("n//2-1"+str(n//2-1))
    print("median1: "+ str(median1))
    print("median2: "+ str(median2))
    median = (median1+median2)/2
else:
    median = new_data[n//2]
print("median is: "+str(median))