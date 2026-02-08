import time

stats = {
    "health": 0,
    "metrics/call_count" : 0,
    "metrics/run_time" : 0,
    "system/info" : 0,
    "system/top": 0
}

start_time = time.time()

def get_runtime():
    elapsed = int(time.time() - start_time)

    hours = elapsed // 3600
    minutes = (elapsed % 3600) // 60
    seconds = elapsed % 60

    return { "run_time" : f"{hours:02}:{minutes:02}:{seconds:02}" }

def get_call_count():
    return stats