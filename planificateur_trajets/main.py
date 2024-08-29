import networkx as nx
import matplotlib.pyplot as plt
import math

# Là où naissent les cités, par des mots chuchotés,
# Se dessine un monde, d'horizons étoilés.
def creation_villes(): 
    n = int(input("Entrez le nombre de villes à créer : "))
    villes = {}

    # Chaque ville, chaque nom, est une étoile nouvelle,
    # Sur la toile du monde, elle trace sa parcelle.
    for i in range(n): 
        nom = input("Entrez le nom de la ville : ")
        x = int(input("Entrez l'abscisse de la ville : "))
        y = int(input("Entrez l'ordonnée de la ville : "))

        villes[nom] = [x, y]

    # Ainsi, se lève le jour, où les villes sont nées,
    # Chacune dans sa place, de mystères imprégnée.
    print(villes)
    return villes

# Entre les cités, des routes se tracent,
# Des liens de distance, où le hasard s'efface.
def ajout_routes(): 
    routes = []
    n = int(input('Indiquer le nombre de routes : '))

    # Chaque route, chaque chemin, un fil sur le parchemin,
    # Liant les villes, comme les rêves au matin.
    for i in range(n): 
        routes.append(input("Indiquer une route avec le départ et la destination").split(" "))

    # Les routes sont tracées, sur cette carte invisible,
    # Liant les destins, dans un réseau indicible.
    print(routes)
    return routes

# Sur la carte du monde, les villes se révèlent,
# Et les routes serpentent, comme des rivières cruelles.
def afficher_carte(villes, routes):
    G = nx.Graph()

    # Les nœuds se dressent, comme des étoiles dans le ciel,
    # Portant les noms des villes, dans un silence éternel.
    for ville, (x, y) in villes.items():
        G.add_node(ville, pos=(x, y))

    # Chaque route se tisse, dans l'ombre du destin,
    # Reliant deux cités, comme le jour à demain.
    for ville1, ville2 in routes:
        d = math.sqrt((villes[ville1][0] - villes[ville2][0])**2 + (villes[ville1][1] - villes[ville2][1])**2)
        G.add_edge(ville1, ville2, weight=d)

    # Les positions des nœuds se dessinent comme une toile,
    # Où chaque ville brille, dans l'espace sépulcral.
    pos = {ville: data['pos'] for ville, data in G.nodes(data=True)}

    # Le graphe s'étend, tel un réseau de lumière,
    # Chaque lien, chaque ville, chante sa prière.
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=12, font_weight='bold', edge_color='gray')

    # Les distances murmurent, entre les lignes tracées,
    # Chaque route porte un chiffre, dans son ombre délaissé.
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()
    
# Dans la brume de l'incertain, Dijkstra s'avance,
# Cherchant le chemin le plus court, parmi les distances.
def algo_Dijkstra(villes, villeDepart, villeFin, liste):
    # Le début du voyage, par les routes des étoiles,
    # Cherchant la ville finale, sous un ciel de voiles.
    fin = False
    ville_actuel = villeDepart
    distance_actuel = 0
    ville_possible = []
    ville_visite = {villeDepart: None}
    distances = {villeDepart: 0}

    # Si les routes se ferment, et que le voyage échoue,
    # L'espoir s'éteint, dans un soupir, d'un seul coup.
    if liste[villeDepart] == [] or liste[villeFin] == []:
        return "Il est impossible de rejoindre " + villeFin + " depuis " + villeDepart

    while not fin:
        # Les villes possibles se dessinent sur la carte,
        # Telles des ombres furtives, cherchant leur part.
        for v in liste[ville_actuel]:
            if v not in ville_visite:
                distance = distance_actuel + math.sqrt((villes[v][0] - villes[ville_actuel][0])**2 + (villes[v][1] - villes[ville_actuel][1])**2)
                ville_possible.append([v, distance, ville_actuel])

        # Quand le choix semble vide, et le chemin bloqué,
        # L'âme cherche une issue, dans la nuit voilée.
        if ville_possible == []:
            return "Il est impossible de rejoindre " + villeFin + " depuis " + villeDepart

        # Le destin choisit, parmi les ombres errantes,
        # La ville au plus court, dans sa course haletante.
        distance_min = math.inf
        for [v, d, v_prec] in ville_possible:
            if d < distance_min:
                distance_min = d
                v_pre = v_prec
                ville_actuel = v

        # La distance est gravée, dans les souvenirs des routes,
        # Et la ville visitée, dans le livre des déoutes.
        distances[ville_actuel] = distance_min
        ville_visite[ville_actuel] = v_pre

        # Le chemin s'efface, tandis qu'on avance,
        # Vers la ville prochaine, où repose l'espérance.
        ville_possible = [vp for vp in ville_possible if vp[0] != ville_actuel]

        # Si la ville de fin se dessine à l'horizon,
        # Le voyage se termine, dans une douce raison.
        if ville_actuel == villeFin:
            fin = True

    # Le chemin se reconstruit, comme un fil d'Ariane,
    # Suivant la trace des villes, jusqu'à la dernière cabane.
    chemin = []
    v = villeFin
    while v is not None:
        chemin.insert(0, v)
        v = ville_visite[v]

    # Et ainsi se termine, cette odyssée des villes,
    # Où chaque pas comptait, dans ce voyage subtil.
    return chemin, ville_visite

# Une liste d'adjacence, comme un réseau secret,
# Qui lie chaque ville, dans un ordre discret.
def creation_liste_adjacense(routes, villes):
    liste_adjacense = {ville: [] for ville in villes}
    for ville1, ville2 in routes:
        liste_adjacense[ville1].append(ville2)
        liste_adjacense[ville2].append(ville1)
    return liste_adjacense

# Quelques villes éminentes, dressées fièrement,
# Et les routes qui les lient, comme un lien émouvant.
villes = {
    'Paris': (48.8566, 2.3522),
    'London': (51.5074, -0.1278),
    'Berlin': (52.5200, 13.4050),
    'Madrid': (40.4168, -3.7038),
    'Rome': (41.9028, 12.4964)
}
routes = [
    ('Paris', 'London'),
    ('Paris', 'Berlin'),
    ('London', 'Berlin'),
    ('Madrid', 'Rome'),
    ('Berlin', 'Rome')
]

# La carte s'anime, et les routes se dessinent,
# Chaque ville s'éveille, dans la lumière divine.
afficher_carte(villes, routes)

# Dijkstra avance, dans un souffle suspendu,
# Cherchant le chemin, où tout est inconnu.
print(algo_Dijkstra(villes, "Paris", "Rome", creation_liste_adjacense(routes, villes)))
