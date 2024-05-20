# Project Brief: Employee Exam Scheduling System

## Objective
Develop the `execute` method within the `ExamSchedulerClass` to schedule health exams at specific clinics. The method should ensure no overlapping exams, verify correct exam types, and adhere to clinic working hours. The class will be instantiated at the entry point, and the `execute` method will follow this signature:

```
    def execute(employee_id: UUID, clinic_id: UUID, exam_type: ExamTypeEnum, exam_start: datetime) -> tuple[bool, str]
```

## Core Functionality

### System Setup
- An entry point is provided in the `main.py` file that calls `ExamSchedulerClass.execute()`.
- **Architecture Flexibility**: The project files are initially unstructured with regard to software architecture. You are encouraged to implement any architectural style or design pattern that you believe best suits the project’s needs. Feel free to reorganize, refactor, and structure the codebase to showcase your architectural expertise and coding proficiency.

### ExamSchedulerClass
- **Method**: `execute`
  - **Inputs**: Employee ID, Clinic ID, Exam Type, Desired Exam Time
  - **Outputs**: Boolean and message if scheduling is not possible.

### Assumptions
- **Exam Duration**: All health exams are assumed to have a fixed duration of 1 hour.

### Constraints and Validations
- **Exam Type Validation**: Ensure the clinic offers the required exam type.
- **Schedule Conflict Check**: Prevent overlapping exams at the same clinic.
- **Working Hours Validation**: Confirm scheduling within clinic operating hours.

### Data Structures
- **Clinics**: Include working hours, available exams, and scheduled exams.
- **Employees**: Contain necessary details for exam scheduling.

## Technologies
- **Backend Language**: Python
- **Data Handling**: Utilize in-memory or simple file-based storage.
- Feel free to use additional technologies to facilitate project organization, build, or execution.

## Assessment Criteria
- **Code Quality**: Focus on readability and maintainability.
- **Algorithm Design**: Assess efficiency and correctness.
- **Error Handling**: Evaluate robustness in handling edge cases and providing feedback.

## Project Duration
1 week

## Submission Requirements
- Provide source code for `ExamSchedulerClass`.
- Include a README with instructions for running the project, example inputs and outputs, and a detailed method explanation.
