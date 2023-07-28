import numpy as np
import xarray as xr
import capytaine as cpt


# def time_heaving_hemisphere(fp):
#     sphere = cpt.Sphere(
#             radius=1.0, center=(0, 0, 0),
#             ntheta=50, nphi=50,
#             axial_symmetry=False,
#             )
#     sphere.keep_immersed_part()
#     sphere.add_translation_dof(name="Heave")
#
#     test_matrix = xr.Dataset(coords={
#         'omega': np.linspace(0.1, 4.0, 10),
#         'radiating_dof': ["Heave"]
#     })
#     green_function = cpt.Delhommeau(floating_point_precision=fp)
#     solver = cpt.BEMSolver(green_function=green_function)
#
#     ds = solver.fill_dataset(test_matrix, sphere)
#
# time_heaving_hemisphere.params = (["float32", "float64"],)
# time_heaving_hemisphere.param_names = ["floating_point_precision"]


# def time_rigid_barge(fp):
def time_rigid_barge():
    barge = cpt.RectangularParallelepiped(
            size=(1.0, 1.0, 1.0),
            resolution=(20, 20, 20),
            reflection_symmetry=False,
            translational_symmetry=False,
            )
    barge.keep_immersed_part()
    barge.add_all_rigid_body_dofs()

    test_matrix = xr.Dataset(coords={
        'omega': np.linspace(0.1, 4.0, 10),
        'radiating_dof': list(barge.dofs.keys()),
    })
    # green_function = cpt.Delhommeau(floating_point_precision=fp)
    # solver = cpt.BEMSolver(green_function=green_function)

    solver = cpt.BEMSolver()
    ds = solver.fill_dataset(test_matrix, [barge])

# time_rigid_barge.params = (["float64"],)
# time_rigid_barge.param_names = ["floating_point_precision"]
