import serial
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import time

INFLUXDB_HOST = 'localhost'
INFLUXDB_PORT = 8086
INFLUXDB_TOKEN = 'your_secret_token'  
INFLUXDB_ORG = 'your_org'             
INFLUXDB_BUCKET = 'sensors'           

def connect_to_influxdb():
    """Create connection to InfluxDB"""
    client = InfluxDBClient(
        url=f"http://{INFLUXDB_HOST}:{INFLUXDB_PORT}",
        token=INFLUXDB_TOKEN,
        org=INFLUXDB_ORG
    )
    return client

def process_serial_data(data_str):
    """Process serial data in format ID:measurement:value"""
    try:

        # Format ID:type:value
        sensor_id, measurement, value = data_str.strip().split(':')
        try:
            value = float(value)
        except ValueError:
            # Keep as string if not convertible to float
            pass

        
        # Create a Point object for InfluxDB 2.x
        point = Point(measurement)\
            .tag("sensor_id", sensor_id)\
            .field("value", value)
        
        return point
    except Exception as e:
        print(f"Error processing data: {e}")
        return None

def main():
    # Connect to InfluxDB
    influx_client = connect_to_influxdb()
    write_api = influx_client.write_api(write_options=SYNCHRONOUS)
    
    # Configure serial connection
    ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate=9600,
        timeout=1
    )


    
    print("Starting serial data collection...")
    
    try:
        while True:
            if ser.in_waiting:
                # Read line from serial port
                line = ser.readline().decode('utf-8').strip()
                
                if line:
                    print(line)
                    # Process the data
                    data_point = process_serial_data(line)
                    
                    if data_point:
                        # Write to InfluxDB
                        write_api.write(bucket=INFLUXDB_BUCKET, record=data_point)
                        print(f"Wrote data point: {data_point}")
            
            time.sleep(0.1) 
            
    except KeyboardInterrupt:
        print("\nStopping data collection...")
    finally:
        ser.close()
        influx_client.close()

if __name__ == "__main__":
    main()

