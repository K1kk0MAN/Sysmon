import psutil
from datetime import datetime

def cpu_usage():
    """Returns the CPU usage as a percentage."""
    return psutil.cpu_percent(interval=0.1,percpu=True)

def memory_usage():
    """Returns the memory usage as a percentage."""
    mem = psutil.virtual_memory()
    return {
        "total": mem.total,
        "used": mem.used,
        "percent": mem.percent,
    }

def all_partitions():
    """Returns all partitions."""
    partitions = []
    for partition in psutil.disk_partitions():
        partitions.append({
            'device': partition.device,
            'mountpoint': partition.mountpoint,
        })
    return partitions

def disk_usage():
    """Returns the disk usage as a percentage."""
    all = []
    for partition in all_partitions():
        try:
            disk = psutil.disk_usage(partition['mountpoint'])
            all.append({
                "name": partition["device"],
                "total": disk.total,
                "used": disk.used,
                "percent": disk.percent,
            })
        except (PermissionError, FileNotFoundError, OSError):
            continue
        
    return all

def uptime_total():
    """Returns the system uptime."""
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    now = datetime.now()
    uptime = now - boot_time
    return str(uptime).split('.')[0]