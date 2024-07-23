from celery.task import periodic_task

# from services.models import WaterMeterData


@periodic_task(
    ignore_result=True, run_every=30
)  # 10 секунд, или timedelta(seconds=10)
def just_print():
    # d = WaterMeterData.objects.filter
    print("Print from celery task")
