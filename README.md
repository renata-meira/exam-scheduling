# Descrição do Projeto: Sistema de Agendamento de Exames para Funcionários

## Objetivo
Desenvolver o método `execute` dentro da `ExamSchedulerClass` para agendar exames de saúde em clínicas específicas. O método deve garantir que não haja sobreposição de exames, verificar os tipos de exames corretos e aderir ao horário de funcionamento das clínicas. A classe será instanciada no ponto de entrada, e o método `execute` seguirá esta assinatura:

```python
def execute(employee_id: UUID, clinic_id: UUID, exam_type: ExamTypeEnum, exam_start: datetime) -> tuple[bool, str]
```

## Funcionalidade Principal

### Configuração do Sistema
- Um ponto de entrada é fornecido no arquivo `main.py` que chama `ExamSchedulerClass.execute()`.
- **Flexibilidade de Arquitetura**: Os arquivos do projeto estão inicialmente desestruturados em relação à arquitetura de software. Você é encorajado a implementar qualquer estilo arquitetônico ou padrão de design que julgue mais adequado às necessidades do projeto. Sinta-se à vontade para reorganizar, refatorar e estruturar o código para demonstrar sua expertise arquitetônica e proficiência em codificação.

### ExamSchedulerClass
- **Método**: `execute`
  - **Entradas**: ID do Funcionário, ID da Clínica, Tipo de Exame, Hora Desejada para o Exame
  - **Saídas**: Booleano e mensagem caso o agendamento não seja possível.

### Premissas
- **Duração do Exame**: Todos os exames de saúde têm uma duração fixa de 1 hora.

### Restrições e Validações
- **Validação do Tipo de Exame**: Garantir que a clínica ofereça o tipo de exame requerido.
- **Verificação de Conflito de Agenda**: Prevenir sobreposição de exames na mesma clínica.
- **Validação de Horário de Funcionamento**: Confirmar o agendamento dentro do horário de funcionamento da clínica.

### Exemplos de Funcionalidade para `ExamSchedulerClass.execute()`

Os exemplos a seguir ilustram como o método `ExamSchedulerClass.execute()` processa vários cenários de agendamento. Esses exemplos ajudam os desenvolvedores a entender os comportamentos esperados e testar o sistema em diferentes condições.

#### 1. Agendamento de Exame com Sucesso
**Entrada:**
- **ID do Funcionário**: `UUID('12345678-1234-5678-1234-567812345678')`
- **ID da Clínica**: `UUID('87654321-4321-8765-4321-567843210987')`
- **Tipo de Exame**: `ExamTypeEnum.GENERAL_CHECKUP`
- **Hora de Início do Exame**: `datetime(2023, 10, 15, 14, 0)`

**Saída:**
- **Resultado**: `True`
- **Mensagem**: `"Exame agendado com sucesso"`

**Descrição**: Este teste verifica se o sistema pode agendar um exame com sucesso quando não há conflitos e todas as condições para um agendamento válido são atendidas.

#### 2. Agendamento de Exame Fora do Horário da Clínica
**Entrada:**
- **ID do Funcionário**: `UUID('12345678-1234-5678-1234-567812345678')`
- **ID da Clínica**: `UUID('87654321-4321-8765-4321-567843210987')`
- **Tipo de Exame**: `ExamTypeEnum.GENERAL_CHECKUP`
- **Hora de Início do Exame**: `datetime(2023, 10, 15, 6, 0)`  // 6h da manhã, antes da clínica abrir

**Saída:**
- **Resultado**: `False`
- **Mensagem**: `"Exame não pode ser agendado fora do horário de funcionamento"`

**Descrição**: Este cenário testa a capacidade do sistema de impor os horários operacionais da clínica ao rejeitar um exame agendado antes da abertura da clínica.

#### 3. Agendamento de Exame com Conflito de Horário
**Entrada:**
- **ID do Funcionário**: `UUID('12345678-1234-5678-1234-567812345678')`
- **ID da Clínica**: `UUID('87654321-4321-8765-4321-567843210987')`
- **Tipo de Exame**: `ExamTypeEnum.GENERAL_CHECKUP`
- **Hora de Início do Exame**: `datetime(2023, 10, 15, 14, 30)`  // Sobreposição com outro exame agendado

**Saída:**
- **Resultado**: `False`
- **Mensagem**: `"Exame não pode ser agendado devido a um conflito de horário"`

**Descrição**: Este exemplo verifica a capacidade do sistema de detectar agendamentos sobrepostos e evitar a dupla reserva na mesma clínica.

### Resumo

Estes exemplos foram projetados para fornecer cenários de teste claros e acionáveis para os desenvolvedores, garantindo que a `ExamSchedulerClass` se comporte conforme o esperado sob várias restrições operacionais. Eles também servem como guias práticos para o desenvolvimento e testes de QA, assegurando uma validação completa da funcionalidade de agendamento.

### Estruturas de Dados
- **Clínicas**: Incluem horários de funcionamento, exames disponíveis e exames agendados.
- **Funcionários**: Contêm os detalhes necessários para o agendamento de exames.

## Tecnologias
- **Linguagem Backend**: Python
- **Manipulação de Dados**: Utilize armazenamento em memória ou baseado em arquivos simples.
- Sinta-se à vontade para usar tecnologias adicionais para facilitar a organização, construção ou execução do projeto.

## Critérios de Avaliação
- **Qualidade do Código**: Foco na legibilidade e manutenibilidade.
- **Desenho do Algoritmo**: Avaliar eficiência e correção.
- **Tratamento de Erros**: Avaliar a robustez no tratamento de casos extremos e fornecimento de feedback.

## Duração do Projeto
1 semana

## Requisitos de Submissão
- Fornecer o código-fonte da `ExamSchedulerClass`.
- Incluir um README com instruções para executar o projeto, exemplos de entradas e saídas, e uma explicação detalhada do método.
