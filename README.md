# Descrição do Projeto: Sistema de Agendamento de Exames para Funcionários

## Objetivo
Desenvolver o método `execute` dentro da `ExamSchedulerClass` para agendar exames de saúde em clínicas específicas. O método deve garantir que não haja sobreposição de exames, verificar os tipos de exames corretos e respeitar o horário de funcionamento das clínicas. A classe será instanciada no ponto de entrada e o método `execute` seguirá esta assinatura:

## Estrutura do Projeto

O projeto segue a arquitetura limpa (Clean Architecture) com a seguinte estrutura:

1. project/
   │
   ├── domain/
   │   ├── clinic.py
   │   ├── exam_type_enum.py
   │   └── scheduled_exam.py
   │
   ├── infrastructure/
   │   └── clinic_repository.py
   │
   ├── interfaces/
   │   └── exam_scheduler_interface.py
   │
   ├── use_cases/
   │   └── exam_scheduler.py
   │
   └── tests/
       └── test_exam_scheduler.py

### Arquivos e Funções Principais

- `exam_scheduler.py`: Contém a classe `ExamSchedulerClass` e o método `execute`.
- `clinic.py`: Define a entidade `Clinic`.
- `scheduled_exam.py`: Define a entidade `ScheduledExam`.
- `exam_scheduler_interface.py`: Define a interface `ExamSchedulerInterface`.
- `clinic_repository.py`: Implementa o repositório `ClinicRepository`.
- `exam_type_enum.py`: Define o enumerador `ExamTypeEnum`.
- `test_exam_scheduler.py`: Contém os testes unitários para a `ExamSchedulerClass`

## Como Executar o Projeto

## Metodo 'execute'

```
def execute(
    self,
    employee_id: UUID,
    clinic_id: UUID,
    exam_type: ExamTypeEnum,
    exam_start: datetime
) -> tuple[bool, str]:
```

## Descrição

  O método execute agenda um exame para um funcionário em uma clínica específica. Ele verifica a disponibilidade da clínica, o tipo de exame e o horário de funcionamento.

## Parâmetros

  ```
  employee_id (UUID): ID do funcionário.
  clinic_id (UUID): ID da clínica.
  exam_type (ExamTypeEnum): Tipo de exame.
  exam_start (datetime): Hora de início do exame.
  ```

## Retorno

  ```
  tuple[bool, str]: Retorna um booleano indicando o sucesso ou falha do agendamento, seguido de uma mensagem explicativa.
  ```

## Exemplos de Funcionalidade


### 1 - Agendamento de Exame com Sucesso

Entrada:

  ```
  employee_id = UUID('12345678-1234-5678-1234-567812345678')
  clinic_id = UUID('87654321-4321-8765-4321-567843210987')
  exam_type = ExamTypeEnum.GENERAL_CHECKUP
  exam_start = datetime(2023, 10, 15, 14, 0)
  ```

Saída:

  ```
  (True, "Exame agendado com sucesso")
  ```

### 2 - Agendamento de Exame Fora do Horário da Clínica

Entrada:

  ```
  employee_id = UUID('12345678-1234-5678-1234-567812345678')
  clinic_id = UUID('87654321-4321-8765-4321-567843210987')
  exam_type = ExamTypeEnum.GENERAL_CHECKUP
  exam_start = datetime(2023, 10, 15, 6, 0)
  ```

Saída:

  ```
  (False, "Exame não pode ser agendado fora do horário de funcionamento")
  ```
### 3 - Agendamento de Exame com Conflito de Horário

Entrada:
  ```
  employee_id = UUID('12345678-1234-5678-1234-567812345678')
  clinic_id = UUID('87654321-4321-8765-4321-567843210987')
  exam_type = ExamTypeEnum.GENERAL_CHECKUP
  exam_start = datetime(2023, 10, 15, 14, 30)
  ```

Saída:
  ```
  (False, "Exame não pode ser agendado devido a um conflito de horário")
  ```

### Pré-requisitos

- Python 3.9+

### Executar testes unitários

python -m unittest discover -s project/tests
