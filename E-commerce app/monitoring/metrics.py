import psutil

def get_metrics():
    metrics = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent,
    }
    return metrics

if __name__ == "__main__":
    print(get_metrics())