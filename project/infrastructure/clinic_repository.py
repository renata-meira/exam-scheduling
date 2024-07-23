from uuid import UUID
from project.domain.clinic import Clinic
from project.domain.exam_type_enum import ExamTypeEnum
from datetime import time

class ClinicRepository:
    def __init__(self):
        self.clinics = []
        self._initialize_clinics()

    def _initialize_clinics(self):
        clinic = Clinic(
            clinic_id=UUID('87654321-4321-8765-4321-567843210987'),
            name="Clínica A",
            opening_time=time(8, 0),
            closing_time=time(18, 0),
            available_exams=[ExamTypeEnum.GENERAL_CHECKUP, ExamTypeEnum.DENTAL_EXAM]
        )
        self.clinics.append(clinic)

    def get_clinic_by_id(self, clinic_id: UUID):
        return next((clinic for clinic in self.clinics if clinic.clinic_id == clinic_id), None)
