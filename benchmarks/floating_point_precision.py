import numpy as np
import xarray as xr
import capytaine as cpt


class FloatingPointPrecision:
    params = (["float32", "float64"], [30, 60])
    param_names = ["floating_point_precision", "resolution"]

    def setup(self, fp, resolution):
        self.sphere = cpt.Sphere(
                radius=1.0, center=(0, 0, 0),
                ntheta=resolution, nphi=resolution,
                axial_symmetry=False,
                )
        self.sphere.keep_immersed_part()
        self.sphere.add_translation_dof(name="Heave")

        self.test_matrix = xr.Dataset(coords={
            'omega': [1.0],
            'radiating_dof': ["Heave"]
        })
        green_function = cpt.Delhommeau(floating_point_precision=fp)
        self.solver = cpt.BEMSolver(green_function=green_function)

    def time_resolution(self, fp, resolution):
        self.solver.fill_dataset(self.test_matrix, self.sphere)

    def peakmem_resolution(self, fp, resolution):
        self.solver.fill_dataset(self.test_matrix, self.sphere)

