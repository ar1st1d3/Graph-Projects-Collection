import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
import math

# Initialisation des données globales
villes = {}
routes = []

def ajouter_ville():
    """Ajoute une ville à la liste des villes."""
    # Par la main de l'homme, la ville se dessine,
    # Sur la carte du monde, un éclat, une vitrine.
    nom = entry_nom.get()
    print(f"Tentative d'ajout de la ville: {nom}")  # Pour explorer les ombres où l'erreur s'imagine
    try:
        x = int(entry_x.get())
        y = int(entry_y.get())
        print(f"Coordonnées saisies: ({x}, {y})")  # Chaque nombre invoqué d'un abîme s'illumine
        if nom in villes:
            print(f"Erreur: La ville '{nom}' existe déjà.")  # Le chaos surgit, les destins se devinent
            messagebox.showerror("Erreur", "Cette ville existe déjà.")
        else:
            villes[nom] = (x, y)
            print(f"Ville ajoutée: {nom} -> ({x}, {y})")  # Une étoile nouvelle dans l'obscur se devine
            messagebox.showinfo("Succès", f"Ville '{nom}' ajoutée avec succès.")
            entry_nom.delete(0, tk.END)
            entry_x.delete(0, tk.END)
            entry_y.delete(0, tk.END)
    except ValueError:
        print("Erreur: Les coordonnées doivent être des nombres entiers.")  # Une faille insondable, où le sens s'exténue
        messagebox.showerror("Erreur", "Les coordonnées doivent être des nombres entiers.")

def afficher_carte():
    """Affiche la carte des villes et des routes."""
    # Par l'art de l'image, les cités s'enlacent,
    # Dans un réseau fragile, leur lien s'efface.
    print("Affichage de la carte des villes et des routes.")  # Les rouages du monde se révèlent, tenaces
    if not villes:
        print("Erreur: Aucune ville disponible.")  # L'ombre murmure : aucun lieu ne prend place
        messagebox.showerror("Erreur", "Aucune ville n'est disponible pour afficher la carte.")
        return

    G = nx.Graph()

    # Chaque ville brille, une étoile dans l'ombre,
    # Posée sur la carte où les mystères sombrent.
    for ville, (x, y) in villes.items():
        G.add_node(ville, pos=(x, y))

    # Les routes sinueuses relient l'infini,
    # Chaque fil tissé tremble, au bord de la nuit.
    for ville1, ville2 in routes:
        d = math.sqrt((villes[ville1][0] - villes[ville2][0])**2 + (villes[ville1][1] - villes[ville2][1])**2)
        G.add_edge(ville1, ville2, weight=d)

    pos = {ville: data['pos'] for ville, data in G.nodes(data=True)}
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=12, font_weight='bold', edge_color='gray')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
    print("Carte affichée avec succès.")  # La vision s'accomplit, le futur s'entrelace

def ajouter_route():
    """Ajoute une route entre deux villes existantes."""
    # Dans les ténèbres, un chemin est tracé,
    # Reliant deux mondes que tout semblait séparer.
    ville1 = entry_ville1.get()
    ville2 = entry_ville2.get()

    print(f"Tentative d'ajout de route entre: {ville1} et {ville2}")  # Des liens inachevés se tissent dans l'éthéré
    if ville1 not in villes or ville2 not in villes:
        print("Erreur: L'une des villes spécifiées n'existe pas.")  # Un gouffre sans fond, où l'idée se jetait
        messagebox.showerror("Erreur", "L'une des villes spécifiées n'existe pas.")
    elif ville1 == ville2:
        print("Erreur: Une route doit relier deux villes différentes.")  # Une boucle insensée, où l'ordre s'arrêtait
        messagebox.showerror("Erreur", "Une route doit relier deux villes différentes.")
    else:
        routes.append((ville1, ville2))
        print(f"Route ajoutée entre {ville1} et {ville2}")  # Un pont invisible, que le destin créait
        messagebox.showinfo("Succès", f"Route entre '{ville1}' et '{ville2}' ajoutée avec succès.")
        entry_ville1.delete(0, tk.END)
        entry_ville2.delete(0, tk.END)

def calculer_plus_court_chemin():
    """Calcule le plus court chemin entre deux villes avec l'algorithme de Dijkstra."""
    # Sur les sentiers perdus, entre l'ombre et le feu,
    # Dijkstra s'avance, brisant le silence affreux.
    ville_depart = entry_chemin_depart.get()
    ville_arrivee = entry_chemin_arrivee.get()

    print(f"Calcul du plus court chemin entre: {ville_depart} et {ville_arrivee}")  # La quête d'une lumière dans les recoins hideux
    if ville_depart not in villes or ville_arrivee not in villes:
        print("Erreur: L'une des villes spécifiées n'existe pas.")  # Une impasse nocturne où l'esprit est fiévreux
        messagebox.showerror("Erreur", "L'une des villes spécifiées n'existe pas.")
        return

    G = nx.Graph()
    for ville, (x, y) in villes.items():
        G.add_node(ville, pos=(x, y))
    for ville1, ville2 in routes:
        d = math.sqrt((villes[ville1][0] - villes[ville2][0])**2 + (villes[ville1][1] - villes[ville2][1])**2)
        G.add_edge(ville1, ville2, weight=d)

    try:
        chemin = nx.shortest_path(G, source=ville_depart, target=ville_arrivee, weight='weight')
        distance = nx.shortest_path_length(G, source=ville_depart, target=ville_arrivee, weight='weight')
        print(f"Chemin trouvé: {chemin} avec une distance de {distance}")  # Une étoile guide, le destin sinueux
        messagebox.showinfo("Résultat", f"Plus court chemin: {' -> '.join(chemin)}\nDistance: {distance:.2f}")
    except nx.NetworkXNoPath:
        print("Erreur: Aucun chemin trouvé.")  # La lumière s'éteint, le néant tumultueux
        messagebox.showerror("Erreur", "Aucun chemin trouvé entre ces deux villes.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Gestion des Villes et Routes")

# Interface pour ajouter des villes
frame_villes = tk.LabelFrame(root, text="Ajouter une ville")
frame_villes.pack(padx=10, pady=10, fill="x")

label_nom = tk.Label(frame_villes, text="Nom de la ville :")
label_nom.pack(anchor="w")
entry_nom = tk.Entry(frame_villes)
entry_nom.pack(fill="x")

label_x = tk.Label(frame_villes, text="Coordonnée X :")
label_x.pack(anchor="w")
entry_x = tk.Entry(frame_villes)
entry_x.pack(fill="x")

label_y = tk.Label(frame_villes, text="Coordonnée Y :")
label_y.pack(anchor="w")
entry_y = tk.Entry(frame_villes)
entry_y.pack(fill="x")

btn_ajouter_ville = tk.Button(frame_villes, text="Ajouter la ville", command=ajouter_ville)
btn_ajouter_ville.pack(pady=5)

# Interface pour ajouter des routes
frame_routes = tk.LabelFrame(root, text="Ajouter une route")
frame_routes.pack(padx=10, pady=10, fill="x")

label_ville1 = tk.Label(frame_routes, text="Ville de départ :")
label_ville1.pack(anchor="w")
entry_ville1 = tk.Entry(frame_routes)
entry_ville1.pack(fill="x")

label_ville2 = tk.Label(frame_routes, text="Ville d'arrivée :")
label_ville2.pack(anchor="w")
entry_ville2 = tk.Entry(frame_routes)
entry_ville2.pack(fill="x")

btn_ajouter_route = tk.Button(frame_routes, text="Ajouter la route", command=ajouter_route)
btn_ajouter_route.pack(pady=5)

# Interface pour le calcul du plus court chemin
frame_chemin = tk.LabelFrame(root, text="Calculer le plus court chemin")
frame_chemin.pack(padx=10, pady=10, fill="x")

label_chemin_depart = tk.Label(frame_chemin, text="Ville de départ :")
label_chemin_depart.pack(anchor="w")
entry_chemin_depart = tk.Entry(frame_chemin)
entry_chemin_depart.pack(fill="x")

label_chemin_arrivee = tk.Label(frame_chemin, text="Ville d'arrivée :")
label_chemin_arrivee.pack(anchor="w")
entry_chemin_arrivee = tk.Entry(frame_chemin)
entry_chemin_arrivee.pack(fill="x")

btn_calculer_chemin = tk.Button(frame_chemin, text="Calculer", command=calculer_plus_court_chemin)
btn_calculer_chemin.pack(pady=5)

# Bouton pour afficher la carte
btn_afficher_carte = tk.Button(root, text="Afficher la carte", command=afficher_carte)
btn_afficher_carte.pack(pady=10)

# Lancement de l'application
root.mainloop()

