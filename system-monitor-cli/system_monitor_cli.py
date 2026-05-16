from typing import Dict
import psutil
import time


def main():
    sys_info = {
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage(),
        "battery": get_battery_percentage(),
        "sys_uptime": get_sys_uptime(),
    }
    
    display_report(sys_info)


def get_cpu_usage() -> float:
    return psutil.cpu_percent(interval=1)


def get_memory_usage() -> Dict:
    mem = psutil.virtual_memory()
    
    mem_total, mem_available, mem_used, mem_free = tuple(map(bytes_to_gigabytes, (mem.total, mem.available, mem.used, mem.free)))

    return {
        "total": mem_total,
        "available": mem_available,
        "percent": mem.percent,
        "used": mem_used,
        "free": mem_free,
    }


def get_disk_usage() -> Dict:
    disk = psutil.disk_usage("/System/Volumes/Data")

    disk_total, disk_used, disk_free = tuple(map(bytes_to_gigabytes, (disk.total, disk.used, disk.free)))

    return {
        "total": disk_total,
        "used": disk_used,
        "free": disk_free,
        "percent": disk.percent,
    }


def get_battery_percentage() -> float | str:
    battery = psutil.sensors_battery()

    if battery is None:
        return "Not available"

    return battery.percent


def get_sys_uptime() -> Dict:
    boot_time = psutil.boot_time()
    current_time = time.time()
    uptime_sec = current_time - boot_time

    hours = int(uptime_sec // 3600)
    minutes = int((uptime_sec % 3600) // 60)

    return {
        "hours": hours,
        "minutes": minutes,
    }


def bytes_to_gigabytes(byte_val) -> float:
    return round(byte_val / 1073741824, 2)


def display_report(sys_info) -> None:
    print("System Monitoring Report")
    print("-----------------------")
    print(f"CPU Usage: {sys_info['cpu']}%")

    print("\nMemory:")
    print(f"Total: {sys_info['memory']['total']} GB")
    print(f"Used: {sys_info['memory']['used']} GB")
    print(f"Available: {sys_info['memory']['available']} GB")
    print(f"Free: {sys_info['memory']['free']} GB")
    print(f"Usage: {sys_info['memory']['percent']}%")

    print("\nDisk:")
    print(f"Total: {sys_info['disk']['total']} GB")
    print(f"Used: {sys_info['disk']['used']} GB")
    print(f"Free: {sys_info['disk']['free']} GB")
    print(f"Usage: {sys_info['disk']['percent']}%")

    battery = sys_info["battery"]
    if isinstance(battery, str):
        print(f"\nBattery: {battery}")
    else:
        print(f"\nBattery: {battery}%")
    print(f"System Uptime: {sys_info['sys_uptime']['hours']} hours and {sys_info['sys_uptime']['minutes']} minutes")


if __name__ == "__main__":
    main()


