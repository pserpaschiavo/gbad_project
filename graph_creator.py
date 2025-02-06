import json
import random

def generate_graph_json(file_path, normal_nodes=10, normal_edges=15, anomaly_nodes=3, anomaly_edges=2):
    """
    Gera um grafo representando conexões normais e anômalas e salva no formato JSON esperado pelo Subdue.
    """
    graph = []
    node_id = 1
    nodes = set()
    
    # Criar nós normais
    for _ in range(normal_nodes):
        graph.append({"vertex": {
            "id": str(node_id),
            "attributes": {"label": "NormalNode"},
            "timestamp": "1"
        }})
        nodes.add(node_id)
        node_id += 1
    
    # Criar conexões normais
    edge_id = 1
    for _ in range(normal_edges):
        n1, n2 = random.sample(nodes, 2)
        graph.append({"edge": {
            "id": str(edge_id),
            "source": str(n1),
            "target": str(n2),
            "attributes": {"label": "NormalConnection"},
            "directed": "false",
            "timestamp": "1"
        }})
        edge_id += 1
    
    # Criar nós anômalos
    anomaly_node_ids = []
    for _ in range(anomaly_nodes):
        graph.append({"vertex": {
            "id": str(node_id),
            "attributes": {"label": "AnomalyNode"},
            "timestamp": "1"
        }})
        anomaly_node_ids.append(node_id)
        node_id += 1
    
    # Criar conexões anômalas
    for _ in range(anomaly_edges):
        n1 = random.choice(anomaly_node_ids)
        n2 = random.choice(list(nodes))  # Conectar a um nó normal
        graph.append({"edge": {
            "id": str(edge_id),
            "source": str(n1),
            "target": str(n2),
            "attributes": {"label": "AnomalyConnection"},
            "directed": "false",
            "timestamp": "1"
        }})
        edge_id += 1
    
    with open(file_path, 'w') as f:
        json.dump(graph, f, indent=4)
    
    print(f'Grafo salvo em {file_path}')

# Gerar e salvar o grafo em JSON
generate_graph_json('network_graph.json')
