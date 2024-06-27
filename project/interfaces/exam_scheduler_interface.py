from datetime import datetime
from uuid import UUID
from project.domain.exam_type_enum import ExamTypeEnum

class ExamSchedulerInterface:
    def execute(self, employee_id: UUID, clinic_id: UUID, exam_type: ExamTypeEnum, exam_start: datetime) -> tuple[bool, str]:
        raise NotImplementedError
