from datetime import datetime
from uuid import UUID

from project.exam_type_enum import ExamTypeEnum


class ExamSchedulerClass:
    def execute(self, employee_id: UUID, clinic_id: UUID, exam_type: ExamTypeEnum, exam_start: datetime) -> tuple[bool, str]:
        # TODO: your code goes here
        return True, "scheduled"