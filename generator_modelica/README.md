# Generator Modelica

Генератор с использованием PyFMI

* [Setup](#step1)
* [Usage](#step2)
* [Arguments](#step3)

<a name = "step1"></a>
# Setup
1. Установка Conda
2. Создание conda environment
```
conda create --name venv python=3.9 
```
3. Устанавить необходимые зависимости для корректной работы PyFmi
```
conda install -c conda-forge pyfmi
```
4. Run the code (like in [Usage](#step2))

<a name = "step2"></a>
# Usage
```python
from simulator import *
if __name__ == "__main__":
  MODEL_PATH = './models/Modelica.Fluid.Examples.PumpingSystem.fmu'
  simulator = Simulator(model_path=MODEL_PATH)
  input_values = {
        'reservoir.crossArea': 50
    }
    initialize_params = {"ncp": 99}
    simulator.run_demo(plot=True, state_to_plot=['pipe.flowModel.m_flows[1]'] 
              input_params=input_values, initialize_params=initialize_params)
```
<a name = "step3"></a>
# Arguments
| Method | Arguments |Description |
| :---         |     :---:      |          :--- |
| `__init__` | model_path=`'./'` | путь к модели |
| `run_demo` | plot=True | | Рисовать ли графики |
| `run_demo` | start_time=`0` | Время начала симуляции |
| `run_demo` | final_time=`0` | Время завершения симуляции |
| `run_demo` | steps=`100` | Количество шагов по времени |
| `run_demo` | input_params=`{key: value}` | Фиксированные начальные значения симуляции |
| `run_demo` | control_params=`[]` | Меняющиеся начальные значения симуляции |
| `run_demo` | state_to_plot=`[]` | Состояния, для которых отрисовывать графики |
| `run_demo` | initialize_params=`[]` | Параметры инициализации симуляции |
| `get_model` | - | Получение модели, готовой к симуляции в PyFmi |
| `get_simulation` | - | Получение последней симуляции модели |
| `get_initialize_parameters` | - | Получение инициализированных параметры симуляции |
| `get_data_by_name` | name | Получение результатов симуляции по имени исследуемого параметра |
| `get_attributes` | - | Получение переменных, участвующих в вычислении физической модели |
| `get_attributes_by_classname` | classname | Получение данных о переменных для модели |
