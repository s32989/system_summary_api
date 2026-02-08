
import app.services.system_info as sys_info

def eval_system_health():

    checks = {}
    reasons = []
    health = sys_info.system_health_check()
    cpu_percent = health.get("cpu_usage_percent")
    disk_percent = health.get("disk_usage_percent")
    memory_percent = health.get("memory_usage_percent")
    if cpu_percent > 90:
        checks["cpu"] = 'high'
        reasons.append(f'CPU usage > 90% ; {cpu_percent}%')
    else:
        checks["cpu"] = 'OK'

    if disk_percent > 90:
        checks["disk"] = 'high'
        reasons.append(f'Disk usage > 90% ; {disk_percent}%')
    else:
        checks["disk"] = 'OK'

    if memory_percent > 85:
        checks["memory"] = 'high'
        reasons.append(f'Memory usage > 85% ; {memory_percent}%')
    else:
        checks["memory"] = 'OK'

    healthy = len(reasons) == 0

    return {
        "healthy": healthy,
        "checks": checks,
        "reasons": reasons
    }