import logging
import os
import time

from app.pull.models import Z1Tags, Z2Tags
from app import create_app
from app.models import *
from app.pull import migrate_into

from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc


logging.basicConfig()
logging.getLogger("apscheduler").setLevel(logging.INFO)
app = create_app("db")

executors = {"default": ThreadPoolExecutor(20), "processpool": ProcessPoolExecutor(5)}
job_defaults = {"coalesce": False, "max_instances": 3}

scheduler = BackgroundScheduler(
    executors=executors, job_defaults=job_defaults, timezone=utc
)


def migrate_job():
    with app.app_context():
        r = migrate_into(Z1Tags)
        print(r)


def my_listener(event):
    if e := event.exception:
        print("The job crashed :(", e)
    else:
        print("The job worked :)")


scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)


def main():
    scheduler.add_job(
        migrate_job, "interval", seconds=3, replace_existing=True, id="migrate_job"
    )
    scheduler.start()
    print("Press Ctrl+{0} to exit".format("Break" if os.name == "nt" else "C"))

    try:
        while True:
            time.sleep(3)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


if __name__ == "__main__":
    main()
