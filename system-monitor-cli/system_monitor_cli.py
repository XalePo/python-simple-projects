import psutil
from typing import Tuple


def main():
    system_info = {
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage(),
        "battery": get_battery_percentage(),
        "system": get_system_uptime(),
    }

    display_report(system_info)


def get_cpu_usage():
    return f"{psutil.cpu_percent(interval=0.1)}"


def get_memory_usage():
    mem = psutil.virtual_memory()
    mem_total, mem_available, mem_perc, mem_used, mem_free, *_ = mem

    mem_data = tuple(map(bytes_to_gigabytes, (mem_total, mem_available, mem_used, mem_free))) 

    return mem_data + (mem_perc,)


def get_disk_usage():
    disk = psutil.disk_usage("/")
    disk_total, disk_used, disk_free, disk_perc = disk

    disk_data = tuple(map(bytes_to_gigabytes, (disk_total, disk_used, disk_free,)))

    return disk_data + (disk_perc,)


def get_battery_percentage():
    ...


def get_system_uptime():
    ...


def bytes_to_gigabytes(byte_val) -> Tuple[float, ...]:
        return round(byte_val / 1073741824, 2)


def display_report(system_info) -> None:
    print(system_info["cpu"])
    print(system_info["memory"])
    print(system_info["disk"])
if __name__ == "__main__":
    main()


