import psutil
from typing import Tuple


def main():
    cpu_usage = get_cpu_usage()
    mem_total, mem_available, mem_used, mem_free, mem_perc = get_memory_usage()
    disk_total, disk_used, disk_free, disk_perc = get_disk_usage()
    battery_perc = get_battery_percentage()
    sys_uptime = get_sys_uptime()
    
    print()


def get_cpu_usage():
    return f"{psutil.cpu_percent(interval=0.1)}"


def get_memory_usage():
    mem = psutil.virtual_memory()
    
    return (*map(bytes_to_gigabytes, (mem.total, mem.available, mem.used, mem.free)), mem.percent)


def get_disk_usage():
    disk = psutil.disk_usage("/System/Volumes/Data")
    print(disk)
    
    return (*map(bytes_to_gigabytes, (disk.total, disk.used, disk.free)), disk.percent)


def get_battery_percentage():
    pass


def get_sys_uptime():
    pass


def bytes_to_gigabytes(byte_val) -> Tuple[float, ...]:
        return round(byte_val / 1073741824, 2)


def display_report(system_info) -> None:
    pass


if __name__ == "__main__":
    main()


