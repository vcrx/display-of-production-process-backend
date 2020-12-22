import logging
import sys
from typing import Optional, Type, Union

from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED, JobExecutionEvent
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from flask import Flask
from loguru import logger
from pytz import utc

from .pull import migrate_into
from .pull.models import KLDTags, Z1Tags, Z2Tags

logging.getLogger("apscheduler").setLevel(logging.INFO)
executors = {
    "default": ThreadPoolExecutor(3),
}
job_defaults = {"coalesce": False, "max_instances": 1}

scheduler = BackgroundScheduler(
    executors=executors,
    job_defaults=job_defaults,
    timezone=utc,
)


def scheduler_wrapper(app: Flask, _from):
    with app.app_context():
        result = migrate_into(_from)
        return result.strip()


def get_color(tablename):
    return {
        "Z1Tags": "m",
        "Z2Tags": "e",
        "KLDTags": "g",
    }.get(tablename, "c")


logger.add(
    "sched.log",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{message}</level>",
    filter=__name__,
)

sched_logger = logger.opt(colors=True)


def sched_listener(event: JobExecutionEvent):
    c = get_color(event.job_id)
    for msg in str(event.retval or "").strip().split("\n"):
        sched_logger.log("INFO", f"<{c}>{event.job_id}</{c}> | " + msg)
    if event.exception:
        sched_logger.exception(event.exception)


scheduler.add_listener(sched_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
trigger = IntervalTrigger(seconds=10)


def init_scheduler(app: Flask):
    def add_job(Table: Type[Union[Z1Tags, Z2Tags, KLDTags]]):
        scheduler.add_job(
            scheduler_wrapper,
            args=(app, Table),
            id=Table.__tablename__,
            trigger=trigger,
            replace_existing=True,
        )

    add_job(Z1Tags)
    add_job(Z2Tags)
    add_job(KLDTags)

    if not scheduler.running:
        scheduler.start()
        print("scheduler started.")
    else:
        print("scheduler is running.")
