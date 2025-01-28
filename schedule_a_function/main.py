from playsound import playsound
import sched
import time

def schedule_a_function(scheduled_time, audio_file_path, callable, *args):
    schedule = sched.scheduler(time.time, time.sleep)
    schedule.enterabs(scheduled_time, callable, argument=args)
    playsound(audio_file_path)
    schedule.run()
