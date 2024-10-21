import json, csv

def disk_output(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Question", "Answer"])

        # Write the header
        writer.writeheader()

        for row in data:
                writer.writerow(row)
                
    print(f"{filename} has been created.")