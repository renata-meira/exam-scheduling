from uuid import UUID
from datetime import datetime

from project.domain.exam_type_enum import ExamTypeEnum

class ScheduledExam:
    def __init__(self, employee_id: UUID, clinic_id: UUID, exam_type: ExamTypeEnum, exam_start: datetime, exam_end: datetime):
        self.employee_id = employee_id
        self.clinic_id = clinic_id
        self.exam_type = exam_type
        self.exam_start = exam_start
        self.exam_end = exam_end
