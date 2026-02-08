import time

import psutil


def system_health_check():
    return {"cpu_usage_percent": check_cpu_usage_percent_over_five_seconds(),
            "disk_usage_percent": check_disk_usage()[3],
            "memory_usage_percent": check_memory_usage()}

def get_system_processes(by, limit):
    procs = list(psutil.process_iter())

    # prime the cpu_percent call for each process
    for p in procs:
        try:
            p.cpu_percent(None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    time.sleep(0.2)  # measure window is 0.2 seconds

    processes = []
    for p in procs:

        try:
            name = p.name()
            if name.lower() != 'system idle process':  # omit system idle process
                processes.append({
                    "name": name,
                    "status": p.status(),
                    "cpu_percent": p.cpu_percent(None),
                    "mem_percent": p.memory_percent()
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    if by == 'cpu':
        processes.sort(key=lambda x: x["cpu_percent"], reverse=True)
    elif by == 'mem':
        processes.sort(key=lambda x: x["mem_percent"], reverse=True)

    return processes[:limit]

def check_cpu_usage_percent_over_five_seconds():
    return psutil.cpu_percent(interval=5)


def check_disk_usage():
    return psutil.disk_usage('/')


def check_memory_usage():
    return psutil.virtual_memory().percent
