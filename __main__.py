from uuid import uuid4, UUID
from datetime import datetime
from project.use_cases.exam_scheduler import ExamSchedulerClass
from project.infrastructure.clinic_repository import ClinicRepository
from project.domain.exam_type_enum import ExamTypeEnum

if __name__ == "__main__":
    clinic_repository = ClinicRepository()
    scheduler = ExamSchedulerClass(clinic_repository)

    employee_id = uuid4()
    clinic_id = UUID('87654321-4321-8765-4321-567843210987')
    exam_type = ExamTypeEnum.GENERAL_CHECKUP
    exam_start = datetime(2024, 07, 15, 14, 0)

    result, message = scheduler.execute(employee_id, clinic_id, exam_type, exam_start)
    print(message)
