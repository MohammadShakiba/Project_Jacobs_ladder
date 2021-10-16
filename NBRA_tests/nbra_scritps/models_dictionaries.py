"""
Ths file contains all parameter dictionaries for the models being investigated.

"""


couplings = [ [0.0, 0.001],
              [0.001, 0.0] ]

params_h_shift = [{"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 4],
                "k_n":[0.002, 0.004],
                "V":couplings,
                "nstates":2},
                  {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.004],
                "V":couplings,
                "nstates":2},
                  {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5.5],
                "k_n":[0.002, 0.004],
                "V":couplings,
                "nstates":2},
                  {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 6],
                "k_n":[0.002, 0.004],
                "V":couplings,
                "nstates":2},
                  {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 6.5],
                "k_n":[0.002, 0.004],
                "V":couplings,
                "nstates":2},
                  {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 7],
                "k_n":[0.002, 0.004],
                "V":couplings,
                "nstates":2},
                  {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 8],
                "k_n":[0.002, 0.004],
                "V":couplings,
                "nstates":2},
                  {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 8.5],
                "k_n":[0.002, 0.004],
                "V":couplings,
                "nstates":2},
                  {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 9],
                "k_n":[0.002, 0.004],
                "V":couplings,
                "nstates":2}]

params_k = [{"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.0065],
                "V":couplings,
                "nstates":2},
            {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.006],
                "V":couplings,
                "nstates":2},
            {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.0055],
                "V":couplings,
                "nstates":2},
            {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.005],
                "V":couplings,
                "nstates":2},
            {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.0045],
                "V":couplings,
                "nstates":2},
            {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.004],
                "V":couplings,
                "nstates":2},
            {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.003],
                "V":couplings,
                "nstates":2},
            {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.0025],
                "V":couplings,
                "nstates":2},
            {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.002],
                "V":couplings,
                "nstates":2}]


couplings_list = [0.01, 0.0075, 0.005, 0.0025, 0.001, 0.00075, 0.0005, 0.00025, 0.0001]

couplings_0 = [ [0.0, couplings_list[0]],
              [couplings_list[0], 0.0] ]

couplings_1 = [ [0.0, couplings_list[1]],
              [couplings_list[1], 0.0] ]

couplings_2 = [ [0.0, couplings_list[2]],
              [couplings_list[2], 0.0] ]

couplings_3 = [ [0.0, couplings_list[3]],
              [couplings_list[3], 0.0] ]

couplings_4 = [ [0.0, couplings_list[4]],
              [couplings_list[4], 0.0] ]

couplings_5 = [ [0.0, couplings_list[5]],
              [couplings_list[5], 0.0] ]

couplings_6 = [ [0.0, couplings_list[6]],
              [couplings_list[6], 0.0] ]

couplings_7 = [ [0.0, couplings_list[7]],
              [couplings_list[7], 0.0] ]

couplings_8 = [ [0.0, couplings_list[8]],
              [couplings_list[8], 0.0] ]

params_energy_gaps = [{"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.004],
                "V":couplings_0,
                "nstates":2},
                {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.004],
                "V":couplings_1,
                "nstates":2},
                {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.004],
                "V":couplings_2,
                "nstates":2},
                {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.004],
                "V":couplings_3,
                "nstates":2},
                {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.004],
                "V":couplings_4,
                "nstates":2},
                {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.004],
                "V":couplings_5,
                "nstates":2},
                {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.004],
                "V":couplings_6,
                "nstates":2},
                {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.004],
                "V":couplings_7,
                "nstates":2},
                {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 5],
                "k_n":[0.002, 0.004],
                "V":couplings_8,
                "nstates":2},
                ]

couplings = [ [0.0, 0.001],
              [0.001, 0.0] ]
params_k_aligned = [{"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 3],
                "k_n":[0.002, 0.006],
                "V":couplings,
                "nstates":2},

                {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 3],
                "k_n":[0.002, 0.005],
                "V":couplings,
                "nstates":2},


              {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 3],
                "k_n":[0.002, 0.004],
                "V":couplings,
                "nstates":2},

              {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 3],
                "k_n":[0.002, 0.003],
                "V":couplings,
                "nstates":2},

              {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 3],
                "k_n":[0.002, 0.002],
                "V":couplings,
                "nstates":2},


              {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 3],
                "k_n":[0.002, 0.0045],
                "V":couplings,
                "nstates":2},

              {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 3],
                "k_n":[0.002, 0.0055],
                "V":couplings,
                "nstates":2},

              {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 3],
                "k_n":[0.002, 0.0025],
                "V":couplings,
                "nstates":2},


                {"model":3,
                "E_n":[0.0,  0.0],
                "x_n":[3, 3],
                "k_n":[0.002, 0.0065],
                "V":couplings,
                "nstates":2}
                ]