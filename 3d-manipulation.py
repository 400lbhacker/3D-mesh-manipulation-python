import open3d as o3d
import numpy as np
if __name__ == "__main__":



    print("Testing IO for textured meshes ...")
    textured_mesh = o3d.io.read_triangle_mesh("r.stl")
    print(textured_mesh)
    o3d.io.write_triangle_mesh("copy_of_crate.obj",
                               textured_mesh,
                               write_triangle_uvs=True)
    copy_textured_mesh = o3d.io.read_triangle_mesh('copy_of_crate.obj')
    print(copy_textured_mesh)





    print(f'Input mesh has {len(textured_mesh.vertices)} vertices and {len(textured_mesh.triangles)} triangles')
    o3d.visualization.draw_geometries([textured_mesh], mesh_show_wireframe=True)

    voxel_size = max(textured_mesh.get_max_bound() - textured_mesh.get_min_bound()) / 32
    print(f'voxel_size = {voxel_size:e}')
    mesh_smp = textured_mesh.simplify_vertex_clustering(
    voxel_size=voxel_size,
    contraction=o3d.geometry.SimplificationContraction.Average)
    print(f'Simplified mesh has {len(mesh_smp.vertices)} vertices and {len(mesh_smp.triangles)} triangles')
    o3d.visualization.draw_geometries([mesh_smp], mesh_show_wireframe=True)
    o3d.io.write_triangle_mesh("copy_of_crate2.obj",
                               textured_mesh,
                               write_triangle_uvs=True)




    mesh_smp = textured_mesh.simplify_quadric_decimation(target_number_of_triangles=6500)
    print(f'Simplified mesh has {len(mesh_smp.vertices)} vertices and {len(mesh_smp.triangles)} triangles')
    o3d.visualization.draw_geometries([mesh_smp], mesh_show_wireframe=True)
    
    mesh_smp = textured_mesh.simplify_quadric_decimation(target_number_of_triangles=1700)
    print(f'Simplified mesh has {len(mesh_smp.vertices)} vertices and {len(mesh_smp.triangles)} triangles')
    o3d.visualization.draw_geometries([mesh_smp], mesh_show_wireframe=True)
    
    
    
    mesh = textured_mesh
    mesh.compute_vertex_normals()
    o3d.visualization.draw_geometries([mesh])
    pcd = mesh.sample_points_uniformly(number_of_points=700)
    o3d.visualization.draw_geometries([pcd])
    o3d.io.write_triangle_mesh("copy_of_crate65.obj",
                               textured_mesh,
                               write_triangle_uvs=True)



    mesh = textured_mesh.subdivide_midpoint(number_of_iterations=2)
    vert = np.asarray(mesh.vertices)
    min_vert, max_vert = vert.min(axis=0), vert.max(axis=0)
    for _ in range(30):
        cube = o3d.geometry.TriangleMesh.create_box()
        cube.scale(0.05, center=cube.get_center())
        cube.translate(
            (
                np.random.uniform(min_vert[0], max_vert[0]),
                np.random.uniform(min_vert[1], max_vert[1]),
                np.random.uniform(min_vert[2], max_vert[2]),
            ),
            relative=False,
        )
    mesh += cube
    mesh.compute_vertex_normals()
    print("Show input mesh")
    o3d.visualization.draw_geometries([mesh], mesh_show_wireframe=True)
    mesh = mesh.subdivide_midpoint(number_of_iterations=1)


    print("Testing IO for images ...")
    img = o3d.io.read_image("outImgPy.png")
    print(img)
    o3d.io.write_image("copy_of_lena_color.jpg", img)