import time
import datetime
import os

# Time to sleep the PC
SLEEP_TIME = "16:13"

# Time to wake the PC
WAKE_HOUR = 16
WAKE_MINUTE = 13

while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")

    if current_time == SLEEP_TIME:

        print("Setting wake timer...")

        # Create wake time
        wake_time = now.replace(
            hour=WAKE_HOUR,
            minute=WAKE_MINUTE,
            second=0,
            microsecond=0
        )

        # If wake time already passed today, set for tomorrow
        if wake_time <= now:
            wake_time += datetime.timedelta(days=1)

        wake_time_str = wake_time.strftime("%H:%M")

        # Create scheduled task that wakes computer
        os.system(
            f'schtasks /create /sc once /tn "WakePC" '
            f'/tr "cmd /c exit" /st {wake_time_str} /ru SYSTEM /f'
        )

        print(f"PC will wake at {wake_time_str}")

        # Put PC to sleep
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        break

    time.sleep(30)
