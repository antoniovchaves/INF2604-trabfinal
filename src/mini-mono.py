import open3d as o3d
import numpy as np

def simplify_mesh(input_path, output_path, reduction_factor):
    # Carrega a malha original
    mesh = o3d.io.read_triangle_mesh(input_path)
    mesh.compute_vertex_normals()

    # Realiza a simplificação da malha
    simplified_mesh = mesh.simplify_quadric_decimation(int(len(mesh.triangles) * reduction_factor))

    # Salva a malha simplificada
    o3d.io.write_triangle_mesh(output_path, simplified_mesh)

    return mesh, simplified_mesh

def compute_metrics(original_mesh, simplified_mesh):
    # Converte as malhas em nuvens de pontos
    original_pcd = original_mesh.sample_points_uniformly(number_of_points=10000)
    simplified_pcd = simplified_mesh.sample_points_uniformly(number_of_points=10000)

    # Número de triângulos
    original_triangles = len(original_mesh.triangles)
    simplified_triangles = len(simplified_mesh.triangles)

    # Erro geométrico (distância média entre as nuvens de pontos)
    distances = simplified_pcd.compute_point_cloud_distance(original_pcd)
    mean_error = np.mean(distances)

    return original_triangles, simplified_triangles, mean_error

def visualize_meshes(original_mesh, simplified_mesh):
    # Exibe as malhas original e simplificada
    o3d.visualization.draw_geometries([original_mesh], window_name="Malha Original")
    o3d.visualization.draw_geometries([simplified_mesh], window_name="Malha Simplificada")

if __name__ == "__main__":
    o3d.visualization.webrtc_server.enable_webrtc()

    # Caminho para o modelo 3D
    input_path = "C:/Users/<seu_usuario>/<caminho_da_pasta>/data/models/Stylish Flexi Shark - 6828888/files/Shark.stl"  # Substitua pelo caminho do seu modelo
    reduction_levels = [0.25, 0.5, 0.75]

    for level in reduction_levels:
        output_path = f"C:/Users/<seu_usuario>/<caminho_da_pasta>/data/models/Stylish Flexi Shark - 6828888/files/Shark_{int(level*100)}.stl"

        # Simplifica a malha
        original_mesh, simplified_mesh = simplify_mesh(input_path, output_path, level)

        # Calcula métricas
        original_triangles, simplified_triangles, mean_error = compute_metrics(original_mesh, simplified_mesh)

        print(f"\nSimplificação para {int(level*100)}% dos triângulos:")
        print(f"- Triângulos Originais: {original_triangles}")
        print(f"- Triângulos Simplificados: {simplified_triangles}")
        print(f"- Erro Geométrico Médio: {mean_error:.6f}")

        # Visualiza as malhas
        visualize_meshes(original_mesh, simplified_mesh)
