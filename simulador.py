class Task:
    def __init__(self, task_id, cpu_demand, requires_low_latency):
        self.task_id = task_id
        self.cpu_demand = cpu_demand
        self.requires_low_latency = requires_low_latency

class Node:

    def __init__(self, name, node_type, max_capacity, latency_ms):
        self.name = name
        self.node_type = node_type
        self.max_capacity = max_capacity
        self.latency_ms = latency_ms
        self.current_load = 0
        self.tasks = []

    def can_accept(self, task):
        return (self.current_load + task.cpu_demand) <= self.max_capacity

    def assign_task(self, task):
        self.current_load += task.cpu_demand
        self.tasks.append(task.task_id)

class EdgeCloudSimulator:
    def __init__(self):

        self.nodes = [
            Node("Borda 1", "edge", max_capacity=50, latency_ms=10),
            Node("Borda 2", "edge", max_capacity=50, latency_ms=10),
            Node("Nuvem", "cloud", max_capacity=1000, latency_ms=100)
        ]

    def allocate(self, tasks):
        for task in tasks:
            allocated = False
            
            if task.requires_low_latency:
                for node in self.nodes:
                    if node.node_type == "edge" and node.can_accept(task):
                        node.assign_task(task)
                        allocated = True
                        print(f"✅ [Tarefa {task.task_id}] (Rápida) -> {node.name} | Tempo de Resposta: {node.latency_ms}ms")
                        break
            
            if not allocated:
                cloud_node = next(n for n in self.nodes if n.node_type == "cloud")
                if cloud_node.can_accept(task):
                    cloud_node.assign_task(task)
                    
                    status = "Transbordo" if task.requires_low_latency else "Geral"
                    print(f"☁️ [Tarefa {task.task_id}] ({status}) -> {cloud_node.name} | Tempo de Resposta: {cloud_node.latency_ms}ms")

    def print_status(self):
        print("\n--- Status Final e Impacto na Rede ---")
        for node in self.nodes:
            uso_percentual = (node.current_load / node.max_capacity) * 100
            print(f"{node.name} ({node.node_type.upper()}): Uso {uso_percentual:.1f}% ({node.current_load}/{node.max_capacity}) | Tarefas: {node.tasks}")

if __name__ == "__main__":
    sim = EdgeCloudSimulator()
    
    tarefas = [
        Task(1, 20, True),
        Task(2, 40, True),
        Task(3, 200, False),
        Task(4, 10, True),
        Task(5, 150, True)
    ]
    
    print("Iniciando o roteamento de tarefas...\n")
    sim.allocate(tarefas)
    sim.print_status()