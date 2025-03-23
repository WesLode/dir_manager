import psutil
import time
import datetime

def get_system_metrics():
    """Retrieves CPU and memory usage."""
    # Get CPU usage as a percentage
    cpu_percent = psutil.cpu_percent(interval=1)  
    # Get memory usage as a percentage
    memory_percent = psutil.virtual_memory().percent  
    return cpu_percent, memory_percent

def log_metrics(cpu_percent, memory_percent, log_file="system_metrics.log"):
    """Logs the CPU and memory usage to a file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - CPU: {cpu_percent}%, Memory: {memory_percent}%\n"

    try:
        with open(log_file, "a") as f:
            f.write(log_entry)
        # Prints to console
        print(log_entry.strip()) 
    except IOError as e:
        print(f"Error writing to log file: {e}")

def monitor_system(interval=60):
    """Monitors system performance and logs metrics at specified intervals."""
    try:
        while True:
            cpu_percent, memory_percent = get_system_metrics()
            log_metrics(cpu_percent, memory_percent)
            time.sleep(interval)

    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Runs the monitoring with 60 second interval. 
    # to change the interval, use monitor_system(30) for example.
    monitor_system() 