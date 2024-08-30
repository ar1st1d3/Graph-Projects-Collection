import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

# Fonction pour ajouter un nœud au graphe
def add_node():
    node_type = node_type_var.get()
    node_name = node_name_entry.get()
    if node_name and node_type:
        G.add_node(node_name, type=node_type)
        messagebox.showinfo("Succès", f"Nœud {node_name} ajouté avec succès.")
    else:
        messagebox.showwarning("Attention", "Veuillez entrer un nom de nœud et sélectionner un type.")

# Fonction pour ajouter une arête au graphe
def add_edge():
    node1 = node1_entry.get()
    node2 = node2_entry.get()
    capacity = capacity_entry.get()
    if node1 and node2 and capacity:
        G.add_edge(node1, node2, capacity=int(capacity))
        messagebox.showinfo("Succès", f"Arête entre {node1} et {node2} ajoutée avec succès.")
    else:
        messagebox.showwarning("Attention", "Veuillez entrer les noms des nœuds et la capacité.")

def remove_edge() : 
    node1 = node3_entry.get()
    node2 = node4_entry.get()
    if node1 and node2:
        G.remove_edge(node1, node2)
        messagebox.showinfo("Succès", f"Arête entre {node1} et {node2} retiré avec succès.")
    else:
        messagebox.showwarning("Attention", "Veuillez entrer les noms des nœuds.")

# Fonction pour visualiser le graphe
def visualize_graph():
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_weight='bold', edge_color='gray')
    labels = nx.get_edge_attributes(G, 'capacity')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title('Schéma du Réseau Électrique')
    plt.show()

# Créer le graphe
G = nx.Graph()

# Créer la fenêtre principale
root = tk.Tk()
root.title("Simulateur de Réseau Électrique")

# Créer les widgets pour ajouter des nœuds
node_frame = tk.Frame(root)
node_frame.pack(pady=10)

node_type_label = tk.Label(node_frame, text="Type de nœud:")
node_type_label.grid(row=0, column=0, padx=5)

node_type_var = tk.StringVar(value="centrale")
node_type_menu = tk.OptionMenu(node_frame, node_type_var, "centrale", "sous-station", "consommateur")
node_type_menu.grid(row=0, column=1, padx=5)

node_name_label = tk.Label(node_frame, text="Nom du nœud:")
node_name_label.grid(row=0, column=2, padx=5)

node_name_entry = tk.Entry(node_frame)
node_name_entry.grid(row=0, column=3, padx=5)

add_node_button = tk.Button(node_frame, text="Ajouter Nœud", command=add_node)
add_node_button.grid(row=0, column=4, padx=5)

# Créer les widgets pour ajouter des arêtes
edge_frame = tk.Frame(root)
edge_frame.pack(pady=10)

node1_label = tk.Label(edge_frame, text="Nœud 1:")
node1_label.grid(row=0, column=0, padx=5)

node1_entry = tk.Entry(edge_frame)
node1_entry.grid(row=0, column=1, padx=5)

node2_label = tk.Label(edge_frame, text="Nœud 2:")
node2_label.grid(row=0, column=2, padx=5)

node2_entry = tk.Entry(edge_frame)
node2_entry.grid(row=0, column=3, padx=5)

capacity_label = tk.Label(edge_frame, text="Capacité:")
capacity_label.grid(row=0, column=4, padx=5)

capacity_entry = tk.Entry(edge_frame)
capacity_entry.grid(row=0, column=5, padx=5)

add_edge_button = tk.Button(edge_frame, text="Ajouter Arête", command=add_edge)
add_edge_button.grid(row=0, column=6, padx=5)

# Creer les widget pour retirer des arretes

remove_edge_frame = tk.Frame(root)
remove_edge_frame.pack(pady=10)

node3_label = tk.Label(remove_edge_frame, text="Nœud 1:")
node3_label.grid(row=0, column=0, padx=5)

node3_entry = tk.Entry(remove_edge_frame)
node3_entry.grid(row=0, column=1, padx=5)

node4_label = tk.Label(remove_edge_frame, text="Nœud 2:")
node4_label.grid(row=0, column=2, padx=5)

node4_entry = tk.Entry(remove_edge_frame)
node4_entry.grid(row=0, column=3, padx=5)

remove_edge_button = tk.Button(remove_edge_frame, text="Retirer Arête", command=remove_edge)
remove_edge_button.grid(row=0, column=6, padx=5)

# Créer le bouton pour visualiser le graphe
visualize_button = tk.Button(root, text="Visualiser le Graphe", command=visualize_graph)
visualize_button.pack(pady=10)

# Lancer la boucle principale de Tkinter
root.mainloop()
