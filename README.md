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

### Functionality Examples for `ExamSchedulerClass.execute()`

The following examples illustrate how the `ExamSchedulerClass.execute()` method processes various scheduling scenarios. These examples help developers understand expected behaviors and test the system under different conditions.

#### 1. Successful Exam Scheduling
**Input:**
- **Employee ID**: `UUID('12345678-1234-5678-1234-567812345678')`
- **Clinic ID**: `UUID('87654321-4321-8765-4321-567843210987')`
- **Exam Type**: `ExamTypeEnum.GENERAL_CHECKUP`
- **Exam Start Time**: `datetime(2023, 10, 15, 14, 0)`

**Output:**
- **Result**: `True`
- **Message**: `"Exam scheduled successfully"`

**Description**: This test verifies that the system can successfully schedule an exam when no conflicts are present and all conditions for a valid appointment are met.

#### 2. Exam Scheduling Outside Clinic Hours
**Input:**
- **Employee ID**: `UUID('12345678-1234-5678-1234-567812345678')`
- **Clinic ID**: `UUID('87654321-4321-8765-4321-567843210987')`
- **Exam Type**: `ExamTypeEnum.GENERAL_CHECKUP`
- **Exam Start Time**: `datetime(2023, 10, 15, 6, 0)`  // 6 AM, before clinic opens

**Output:**
- **Result**: `False`
- **Message**: `"Exam cannot be scheduled outside working hours"`

**Description**: This scenario tests the system's ability to enforce clinic operational hours by rejecting an exam scheduled before the clinic opens.

#### 3. Exam Scheduling with Time Conflicts
**Input:**
- **Employee ID**: `UUID('12345678-1234-5678-1234-567812345678')`
- **Clinic ID**: `UUID('87654321-4321-8765-4321-567843210987')`
- **Exam Type**: `ExamTypeEnum.GENERAL_CHECKUP`
- **Exam Start Time**: `datetime(2023, 10, 15, 14, 30)`  // Overlaps with another scheduled exam

**Output:**
- **Result**: `False`
- **Message**: `"Exam cannot be scheduled due to a time conflict"`

**Description**: This example checks the system's capability to detect overlapping appointments and prevent double-booking within the same clinic.

### Summary

These examples are designed to provide clear and actionable test scenarios for developers to ensure the `ExamSchedulerClass` behaves as expected under various operational constraints. They also serve as practical guides for both development and QA testing, ensuring thorough validation of the scheduling functionality.


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
