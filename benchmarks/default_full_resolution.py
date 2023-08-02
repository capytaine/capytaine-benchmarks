# Full resolution of a BEM problem using Capytaine default settings.
# Should be compatible with v1.3 or higher of Capytaine.

import numpy as np
import xarray as xr
import capytaine as cpt

#############################################

def timeraw_setup_default_solver():
    return """import capytaine as cpt; solver = cpt.BEMSolver()"""
    # solver = cpt.BEMSolver(engine=cpt.BasicMatrixEngine(), green_function=cpt.Delhommeau())

#############################################

class RigidBarge:
    params = ([10.0, np.infty],)
    param_names = ["water_depth",]

    def setup(self, wd):
        self.solver = cpt.BEMSolver()

        self.barge = cpt.RectangularParallelepiped(
                size=(1.0, 1.0, 1.0),
                resolution=(15, 15, 15),
                reflection_symmetry=False,
                translational_symmetry=False,
                )
        self.barge.keep_immersed_part()
        self.barge.add_all_rigid_body_dofs()

        self.test_matrix = xr.Dataset(coords={
            'omega': np.linspace(0.1, 4.0, 20),
            'wave_direction': [0.0, np.pi/4],
            'radiating_dof': list(self.barge.dofs.keys()),
            'water_depth': [wd]
        })

    def time_resolution(self, wd):
        self.solver.fill_dataset(self.test_matrix, [self.barge])

#############################################
