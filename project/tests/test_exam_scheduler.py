import unittest
from unittest.mock import Mock
from uuid import UUID, uuid4
from datetime import datetime, time, timedelta
from project.use_cases.exam_scheduler import ExamSchedulerClass
from project.domain.exam_type_enum import ExamTypeEnum

class TestExamSchedulerClass(unittest.TestCase):

    def setUp(self):
        # Mock ClinicRepository
        self.clinic_repository = Mock()

        # Simulate a Clinic instance
        clinic_id = UUID('87654321-4321-8765-4321-567843210987')
        clinic = Mock()
        clinic.clinic_id = clinic_id
        clinic.name = "Clinic A"
        clinic.opening_time = time(8, 0)
        clinic.closing_time = time(18, 0)
        clinic.available_exams = [ExamTypeEnum.GENERAL_CHECKUP, ExamTypeEnum.DENTAL_EXAM]
        clinic.scheduled_exams = []

        self.clinic_repository.get_clinic_by_id.return_value = clinic

        self.scheduler = ExamSchedulerClass(self.clinic_repository)

    def test_successful_exam_scheduling(self):
        clinic_id = UUID('87654321-4321-8765-4321-567843210987')
        result, message = self.scheduler.execute(
            employee_id=uuid4(),
            clinic_id=clinic_id,
            exam_type=ExamTypeEnum.GENERAL_CHECKUP,
            exam_start=datetime(2023, 10, 15, 14, 0)
        )
        self.assertTrue(result)
        self.assertEqual(message, "Exame agendado com sucesso")

    def test_exam_scheduling_outside_operating_hours(self):
        clinic_id = UUID('87654321-4321-8765-4321-567843210987')
        result, message = self.scheduler.execute(
            employee_id=uuid4(),
            clinic_id=clinic_id,
            exam_type=ExamTypeEnum.GENERAL_CHECKUP,
            exam_start=datetime(2023, 10, 15, 6, 0)
        )
        self.assertFalse(result)
        self.assertEqual(message, "Exame não pode ser agendado fora do horário de funcionamento")

    def test_exam_scheduling_with_conflict(self):
        clinic_id = UUID('87654321-4321-8765-4321-567843210987')
        self.scheduler.execute(
            employee_id=uuid4(),
            clinic_id=clinic_id,
            exam_type=ExamTypeEnum.GENERAL_CHECKUP,
            exam_start=datetime(2024, 8, 15, 14, 0)
        )
        result, message = self.scheduler.execute(
            employee_id=uuid4(),
            clinic_id=clinic_id,
            exam_type=ExamTypeEnum.GENERAL_CHECKUP,
            exam_start=datetime(2024, 8, 15, 14, 30)
        )
        self.assertFalse(result)
        self.assertEqual(message, "Exame não pode ser agendado devido a um conflito de horário")

if __name__ == '__main__':
    unittest.main()
