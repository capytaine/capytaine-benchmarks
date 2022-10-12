import numpy as np
import xarray as xr
import capytaine as cpt


def time_heaving_hemisphere_with_circulant_matrix():
    sphere = cpt.Sphere(
            radius=1.0, center=(0, 0, 0),
            ntheta=50, nphi=50,
            axial_symmetry=True,
            )
    sphere.keep_immersed_part()
    sphere.add_translation_dof(name="Heave")

    test_matrix = xr.Dataset(coords={
        'omega': np.linspace(0.1, 4.0, 10),
        'radiating_dof': ["Heave"]
    })
    engine = cpt.HierarchicalToeplitzMatrixEngine()
    green_function = cpt.Delhommeau()
    solver = cpt.BEMSolver(engine=engine, green_function=green_function)

    ds = solver.fill_dataset(test_matrix, sphere)

def time_rigid_barge_with_toeplitz_matrix():
    barge = cpt.RectangularParallelepiped(
            size=(1.0, 1.0, 1.0),
            resolution=(20, 20, 20),
            reflection_symmetry=False,
            translational_symmetry=True,
            )
    barge.keep_immersed_part()
    barge.add_all_rigid_body_dofs()

    test_matrix = xr.Dataset(coords={
        'omega': np.linspace(0.1, 4.0, 10),
        'radiating_dof': list(barge.dofs.keys()),
    })
    engine = cpt.HierarchicalToeplitzMatrixEngine()
    green_function = cpt.Delhommeau()
    solver = cpt.BEMSolver(engine=engine, green_function=green_function)

    ds = solver.fill_dataset(test_matrix, barge)
