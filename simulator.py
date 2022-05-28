import pyfmi as pf

from pyfmi import load_fmu


import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from cycler import cycler
mpl.rc('lines', linewidth=4, linestyle='-.')

class Simulator():
    
    def __init__(self,
                 model_path: str = 'Modelica.Fluid.Examples.PumpingSystem.fmu'):
        self.model = load_fmu(model_path)
        self.model_path = model_path
        
    def run_demo(self, plot:bool = False, start_time: int = 0, final_time: int = 10, steps: int = 100,
                 input_params: dict = {}, control_params = [], state_to_plot: list = [], initialize_params: list = []):
        assert len(input_params.keys()) == len(input_params.values()), "Check input conditions"
        t = np.linspace(start_time, final_time, steps)
        for key, value in input_params.items():
            self.model.set(key, value) 
        if len(initialize_params):
            if len(control_params):
                self.res = self.model.simulate(final_time=final_time,
                                               start_time=start_time,
                                               options=initialize_params,
                                               input=control_params)
            else:
                self.res = self.model.simulate(final_time=final_time, 
                                               start_time=start_time,
                                               options=initialize_params)
        else:
            if len(control_params):
                self.res = self.model.simulate(start_time=start_time, final_time=final_time, input=control_params)
            else:
                self.res = self.model.simulate(start_time=start_time, final_time=final_time)  
        if plot:
            assert len(state_to_plot) != 0, "If you want to plot something, then, please, give me what you need"
            plt.figure(figsize=(25,25))
            for name in state_to_plot:
                rb = min(len(t)-1, len(self.get_data_by_name(name=name))-1)
                plt.plot(t[:rb],
                         self.get_data_by_name(name=name)[:rb], label=name)
                plt.legend()
                plt.show()
        return self.res
                
    def get_model(self) -> pf.fmi.FMUModelME2:
        return self.model
    
    def get_simulation(self):# -> pf.fmi_algorithm_drivers.FMIResult:
        return self.res
    
    def get_model_parameters(self):
        return self.model.simulate_options()
    
    def get_data_by_name(self, name:str) -> list:
        return self.res[name]
    
    def get_attributes(self) -> list:
        return self.model.get_model_variables()
    
    def get_initialize_parameters(self) -> list:
        return self.model.simulate_options()
    
    def get_attributes_by_classname(self, classname:str = 'reservoir') -> list:
        return [name for name in self.get_attributes() if classname in name] 