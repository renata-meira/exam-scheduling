from datetime import datetime
from uuid import uuid4

from project.exam_scheduler import ExamSchedulerClass
from project.exam_type_enum import ExamTypeEnum


# Example of how this class could be called:
if __name__ == "__main__":
    scheduler = ExamSchedulerClass()

    # Example parameters
    employee_id = uuid4()
    clinic_id = uuid4()
    exam_type = ExamTypeEnum.GENERAL_CHECKUP
    exam_start = datetime(2023, 10, 15, 14, 0)  # October 15, 2023, 14:00

    result, message = scheduler.execute(employee_id, clinic_id, exam_type, exam_start)
    print(message)
