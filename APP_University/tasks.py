from datetime import datetime
from APP_University.funcs import GenerateReport
from Core.models import Task
from celery import shared_task


@shared_task
def GenerateReportTask(temp_task_id):
    task = Task.objects.get(temp_task_id=temp_task_id)
    result = GenerateReport(task.task_id)
    if result:
        task.status = Task.TaskStatus.finished
        task.date_finished = datetime.now()
    else:
        task.status = Task.TaskStatus.error
    task.save()
    return True
