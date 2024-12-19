import csv

def disk_output(data, filename):
    with open(filename, mode='w') as csv_file:  
        writer = csv.writer(csv_file)
        writer.writerow(data.keys())
        writer.writerow(data.values())

    print(f"{filename} has been created.")
