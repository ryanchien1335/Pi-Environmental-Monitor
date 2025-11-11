import csv, time, random

# Simulates logging data collected from sensors and pastes them on a CSV file
# This code will be the backbone of the actual code used to log the real environmental data

with open("data.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Time", "Temp"])
    
    for i in range(5):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        temperature = 20 + random.random()*5
        writer.writerow([timestamp, temperature])
        print(f"Logged {temperature:.2f}°C at {timestamp}")
        time.sleep(1)
