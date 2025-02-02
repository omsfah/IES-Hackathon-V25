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
lastNNumbers1 = []
lastNNumbers2 = []


try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if "EC:E1:61:7B:1F:E9" in line:
                    parts = line.split()
                    highPrecision = float(parts[4].split('=')[1])
                    ifft = float(parts[5].split('=')[1])
                    phaseSlope = float(parts[6].split('=')[1])
                    rssiOpenspace = float(parts[7].split('=')[1])
                    best = float(parts[8].split('=')[1])
                    lastNNumbers.append(best)
                    if len(lastNNumbers) > N:
                        lastNNumbers.pop(0)
                    if len(lastNNumbers) == N:
                        average = sum(lastNNumbers)/len(lastNNumbers)
                        print(f"average {average}")
                        measurement = "distance"
                        tags = {"Ola Nordmann": "cow_1"}
                        point = (
                            Point(measurement)
                            .tag("Ola Nordmann", "cow_1")
                            .field("distance [M]", average)
                        )
                        write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point)
                        print(f"Wrote data point: {point}")
        if "DF:1A:CF:EC:30:FE" in line:
                    parts1 = line.split()
                    highPrecision1 = float(parts1[4].split('=')[1])
                    ifft1 = float(parts1[5].split('=')[1])
                    phaseSlope1 = float(parts1[6].split('=')[1])
                    rssiOpenspace1 = float(parts1[7].split('=')[1])
                    best1 = float(parts1[8].split('=')[1])
                    lastNNumbers1.append(best1)
                    if len(lastNNumbers1) > N:
                        lastNNumbers1.pop(0)
                    if len(lastNNumbers1) == N:
                        average1 = sum(lastNNumbers1)/len(lastNNumbers1)
                        print(f"average {average1}")
                        measurement1 = "distance"
                        tags1 = {"Ola Nordmann": "cow_2"}
                        point1 = (
                            Point(measurement1)
                            .tag("Ola Nordmann", "cow_2")
                            .field("distance [M]", average1)
                        )
                        write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point1)
                        print(f"Wrote data point: {point1}")
        if "FB:5D:24:88:9E:61" in line:
            for i in range(3):
                    parts2 = line.split()
                    highPrecision2 = float(parts2[4].split('=')[1])
                    ifft2 = float(parts2[5].split('=')[1])
                    phaseSlope2 = float(parts2[6].split('=')[1])
                    rssiOpenspace2 = float(parts2[7].split('=')[1])
                    best2 = float(parts2[8].split('=')[1])
                    lastNNumbers2.append(best2)
                    if len(lastNNumbers2) > N:
                        lastNNumbers2.pop(0)
                    if len(lastNNumbers2) == N:
                        average2 = sum(lastNNumbers2)/len(lastNNumbers2)
                        print(f"average {average2}")
                        measurement2 = "distance"
                        tags2 = {"Ola Nordmann": "cow_3"}
                        point2 = (
                            Point(measurement2)
                            .tag("Ola Nordmann", "cow_3")
                            .field("distance [M]", average2)
                        )
                        write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point2)
                        print(f"Wrote data point: {point2}")

except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()  # Make sure to close the serial port
    client.close()