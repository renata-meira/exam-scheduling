from datetime import time
from uuid import UUID
from project.domain.exam_type_enum import ExamTypeEnum

class Clinic:
    def __init__(self, clinic_id: UUID, name: str, opening_time: time, closing_time: time, available_exams: list[ExamTypeEnum]):
        self.clinic_id = clinic_id
        self.name = name
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.available_exams = available_exams
        self.scheduled_exams = []
