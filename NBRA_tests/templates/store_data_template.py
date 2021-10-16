"""
This file reads data from the dynamics output files, calculates the different
comparison metrics (both raw and integrated), and repackages it into a new file
along with the time and reorganziation energy. Each new file contains the four
comparison metrics for each model of a specific set (i.e. all nine models in the
"h_shift" set) at specific initial conditions. Each file compares to NBRA of a
single type - either using adiabatic trajectories on the ground or excited state.
"""

import sys
import cmath
import math
import os
import h5py

sys.path.insert(1, '../../import_files')
import models_dictionaries
import comparison_functions

import numpy as np

if not os.path.isdir("../../data"):
    os.system("mkdir ../../data")

def store_nbra(filename, ref_names, test_names, ref_prefix, test_prefix, param_set):
    with h5py.File(f'{ref_prefix}{ref_names[0]}/mem_data.hdf', 'r') as f:
        time_list = list(f['time/data'])

    if os.path.isfile(f'{filename}.hdf5'):
        os.system(f'rm {filename}.hdf5')

    with h5py.File(f'{filename}.hdf5', 'w') as f:
        for i in range(len(ref_names)):
            population_integral = []
            population_integral_sum = 0
            coherence_integral = []
            coherence_integral_sum = 0
            coupling_integral = []
            coupling_integral_sum = 0
            energy_gap_integral = []
            energy_gap_integral_sum = 0

            params = {"ref_prefix": f'{ref_prefix}{ref_names[i]}',
                            "test_prefix": f'{test_prefix}{test_names[i]}'}

            population_metric = comparison_functions.population_metric(params)
            coherence_metric = comparison_functions.coherence_metric(params)
            coupling_metric = comparison_functions.coupling_metric(params)
            energy_gap_metric = comparison_functions.energy_gap_metric(params)

            for k in range(len(population_metric)):
                population_integral_sum += population_metric[k]
                population_integral.append(population_integral_sum)
                coherence_integral_sum += coherence_metric[k]
                coherence_integral.append(coherence_integral_sum)
                coupling_integral_sum += coupling_metric[k]
                coupling_integral.append(coupling_integral_sum)
                energy_gap_integral_sum += energy_gap_metric[k]
                energy_gap_integral.append(energy_gap_integral_sum)

            reorg_E = comparison_functions.reorg_energy(comparison_functions.compute_model, [ param_set[i] ], [0,1],-5, 5.0, 0.05)[1]
            coupling = comparison_functions.model_parameter_coupling(params)
            energy_gap = comparison_functions.model_parameter_energy_gap(params)
            coupling_modified = comparison_functions.model_parameter_coupling_modified(params)
            coupling_diabatic = comparison_functions.model_parameter_coupling_diabatic(params)
            energy_gap_fluctuations = comparison_functions.model_parameter_energy_gap_fluctuations(params, energy_gap)


            f.create_dataset(f'{i}/time', data = time_list)
            f.create_dataset(f'{i}/population_metric_raw', data = population_metric)
            f.create_dataset(f'{i}/population_metric_integrated', data = population_integral)
            f.create_dataset(f'{i}/coherence_metric_raw', data = coherence_metric)
            f.create_dataset(f'{i}/coherence_metric_integrated', data = coherence_integral)
            f.create_dataset(f'{i}/coupling_metric_raw', data = coupling_metric)
            f.create_dataset(f'{i}/coupling_metric_integrated', data = coupling_integral)
            f.create_dataset(f'{i}/energy_gap_metric_raw', data = energy_gap_metric)
            f.create_dataset(f'{i}/energy_gap_metric_integrated', data = energy_gap_integral)
            f.create_dataset(f'{i}/reorg', data = [reorg_E])
            f.create_dataset(f'{i}/coupling', data = [coupling])
            f.create_dataset(f'{i}/energy_gap', data = [energy_gap])
            f.create_dataset(f'{i}/coupling_modified', data = [coupling_modified])
            f.create_dataset(f'{i}/coupling_diabatic', data = [coupling_diabatic])
            f.create_dataset(f'{i}/energy_gap_fluctuations', data = [energy_gap_fluctuations])

    return

initial_states = ["ISTATE_REPLACE"]
sets = [0, 1, 2, 3, 4, 5, 6, 7, 8]
coords = [COORD_REPLACE]
trajs = [1200]
model_types = ["MODEL_TYPE_REPLACE"]
params_sets = [models_dictionaries.params_MODEL_TYPE_REPLACE]


for i in range(len(model_types)):
    for initial_state in initial_states:
        for coord in coords:
            for traj in trajs:
                model_type = model_types[i]
                if model_type == 'k_aligned' and coord == 6 or model_type == 'energy_gaps' and coord == 6:
                    continue
                param_set = params_sets[i]
                name = f'../../data/{model_type}_{initial_state}_coord_{coord}_ntraj_{traj}'
                name_mixed =  f'../../data/{model_type}_mixed_{initial_state}_coord_{coord}_ntraj_{traj}'
                all_names_fssh = []
                all_names_nbra_mixed = []
                for j in sets:
                    all_names_fssh.append(f'{model_type}_{initial_state}_coord_{coord}_set_{j}_ntraj_{traj}_number_1')
                    all_names_nbra_mixed.append(f'{model_type}_mixed_{initial_state}_coord_{coord}_set_{j}_ntraj_{traj}_number_1')
                store_nbra(name, all_names_fssh, all_names_fssh, f"../../out/fssh_", f"../../out/nbra_fssh_", param_set) # this stores non-mixed data
                store_nbra(name_mixed, all_names_fssh, all_names_nbra_mixed, f"../../out/fssh_", f"../../out/nbra_fssh_", param_set) # this stores mixed data
