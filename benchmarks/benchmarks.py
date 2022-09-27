import numpy as np
import xarray as xr
import capytaine as cpt
from threadpoolctl import ThreadpoolController

def time_simple_solve():
    controller = ThreadpoolController()
    with controller.limit(limits=1, user_api='blas'):
        with controller.limit(limits=1, user_api='openmp'):
            sphere = cpt.Sphere(
                    radius=1.0, center=(0, 0, 0),
                    ntheta=20, nphi=20,
                    name="sphere"
                    )
            sphere.keep_immersed_part()
            sphere.add_translation_dof(name="Heave")

            test_matrix = xr.Dataset(coords={
                'omega': np.linspace(1.0, 3.0, 20),
                'radiating_dof': ["Heave"]
            })
            engine = cpt.BasicMatrixEngine(linear_solver='direct')
            ds = cpt.BEMSolver().fill_dataset(test_matrix, sphere)
