import open3d as o3d
import numpy as np

def calculate_triangle_density(mesh):
    """Calcula a densidade de triângulos por unidade de área."""
    mesh_area = mesh.get_surface_area()
    num_triangles = len(mesh.triangles)
    return num_triangles / mesh_area

def visualize_edges(mesh):
    """Visualiza a malha mostrando suas arestas."""
    edges = o3d.geometry.LineSet.create_from_triangle_mesh(mesh)
    edges.paint_uniform_color([1, 0, 0])  # Arestas em vermelho
    o3d.visualization.draw_geometries([mesh, edges], window_name="Malha com Arestas")

def generate_topological_heatmap(original_mesh, simplified_mesh):
    """Gera um heatmap baseado nas mudanças de conexões de triângulos."""
    original_pcd = original_mesh.sample_points_uniformly(number_of_points=10000)
    simplified_pcd = simplified_mesh.sample_points_uniformly(number_of_points=10000)

    distances = np.array(simplified_pcd.compute_point_cloud_distance(original_pcd))
    simplified_pcd.colors = o3d.utility.Vector3dVector(
        np.array([[d, 1 - d, 0] for d in distances / max(distances)])
    )

    o3d.visualization.draw_geometries([simplified_pcd], window_name="Heatmap Topológico")

# Caminhos dos arquivos STL
path = "C:/Users/<seu_usuario>/<caminho_da_pasta>/data/models/Stylish Flexi Shark - 6828888/files/"
files = {
    "original": path + "Shark.stl",
    "25": path + "Shark_25.stl",
    "50": path + "Shark_50.stl",
    "75": path + "Shark_75.stl",
}

# Carregar malhas
original_mesh = o3d.io.read_triangle_mesh(files["original"])
simplified_25 = o3d.io.read_triangle_mesh(files["25"])
simplified_50 = o3d.io.read_triangle_mesh(files["50"])
simplified_75 = o3d.io.read_triangle_mesh(files["75"])

# Calcular densidades de triângulos
print("Densidade Original:", calculate_triangle_density(original_mesh))
print("Densidade 25%:", calculate_triangle_density(simplified_25))
print("Densidade 50%:", calculate_triangle_density(simplified_50))
print("Densidade 75%:", calculate_triangle_density(simplified_75))

# Visualizar arestas das malhas
print("Visualizando arestas da malha original...")
visualize_edges(original_mesh)

print("Visualizando arestas da malha simplificada (25%)...")
visualize_edges(simplified_25)

# Gerar heatmap topológico
print("Gerando heatmap topológico para malha simplificada (25%)...")
generate_topological_heatmap(original_mesh, simplified_25)
