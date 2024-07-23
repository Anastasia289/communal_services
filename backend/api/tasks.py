from celery.task import periodic_task


@periodic_task(
    ignore_result=True, run_every=30
)  # 10 секунд, или timedelta(seconds=10)
def just_print():
    print("Print from celery task")
