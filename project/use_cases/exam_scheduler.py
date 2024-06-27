from datetime import datetime, timedelta
from uuid import UUID
from project.interfaces.exam_scheduler_interface import ExamSchedulerInterface
from project.domain.scheduled_exam import ScheduledExam
from project.domain.exam_type_enum import ExamTypeEnum
from project.infrastructure.clinic_repository import ClinicRepository


class ExamSchedulerClass(ExamSchedulerInterface):
    def __init__(self, clinic_repository: ClinicRepository):
        self.clinic_repository = clinic_repository

    def execute(self, employee_id: UUID, clinic_id: UUID, exam_type: ExamTypeEnum, exam_start: datetime) -> tuple[bool, str]:
        clinic = self.clinic_repository.get_clinic_by_id(clinic_id)
        if not clinic:
            return False, "Clínica não encontrada"

        if exam_type not in clinic.available_exams:
            return False, "Tipo de exame não oferecido pela clínica"

        exam_end = exam_start + timedelta(hours=1)
        if not (clinic.opening_time <= exam_start.time() < clinic.closing_time and
                clinic.opening_time < exam_end.time() <= clinic.closing_time):
            return False, "Exame não pode ser agendado fora do horário de funcionamento"

        for scheduled_exam in clinic.scheduled_exams:
            if exam_start < scheduled_exam.exam_end and exam_end > scheduled_exam.exam_start:
                return False, "Exame não pode ser agendado devido a um conflito de horário"

        new_exam = ScheduledExam(employee_id, clinic_id, exam_type, exam_start, exam_end)
        clinic.scheduled_exams.append(new_exam)
        return True, "Exame agendado com sucesso"
