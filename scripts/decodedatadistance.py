import serial
import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
INFLUXDB_HOST = '192.168.76.68:8086'
INFLUXDB_PORT = 8086
INFLUXDB_TOKEN = 'your_secret_token'  
INFLUXDB_ORG = 'your_org'             
INFLUXDB_BUCKET = 'sensors'
client = InfluxDBClient(url=INFLUXDB_HOST , token=INFLUXDB_TOKEN, org=INFLUXDB_ORG,)
write_api = client.write_api()



# Configure the serial port
serial_port = 'COM17'
baud_rate = 115200
timeout = 5

ser = serial.Serial(serial_port, baud_rate, timeout=timeout)
N = 10
lastNNumbers = []


try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if "EC:E1:61:7B:1F:E9" in line:
            for i in range(3):
                line = ser.readline().decode('utf-8').strip()
                if i == 1:
                    print(f"{line}")
                    parts = line.split()
                    highPrecision = float(parts[3].split('=')[1])
                    ifft = float(parts[4].split('=')[1])
                    phaseSlope = float(parts[5].split('=')[1])
                    rssiOpenspace = float(parts[6].split('=')[1])
                    best = float(parts[7].split('=')[1])
                    lastNNumbers.append(best)
                    if len(lastNNumbers) > N:
                        lastNNumbers.pop(0)
                    if len(lastNNumbers) == N:
                        average = sum(lastNNumbers)/len(lastNNumbers)
                        print(f"average {average}")
                        measurement = "distance"
                        tags = {"farmer_1": "cow_1"}
                        point = (
                            Point(measurement)
                            .tag("farmer_1", "cow_1")
                            .field("value", average)
                        )
                        write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point)
                        print(f"Wrote data point: {point}")

except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()  # Make sure to close the serial port
    client.close()