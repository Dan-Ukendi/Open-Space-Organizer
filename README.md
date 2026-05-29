# 🪑 OpenSpace Organiser

Un outil CLI en Python pour organiser automatiquement le placement de collègues dans un open space, avec gestion des contraintes de voisinage.

---

## 📁 Structure du projet

```
openspace-organiser/
├── main.py
├── utils/
│   ├── openspace.py
│   └── tables.py
├── txt/
│   └── new_colleagues.txt
└── seating_arrangement.txt
```

---

## ▶️ Utilisation

```bash
python main.py
```

Le programme te guidera étape par étape via des questions interactives :

1. **Chemin vers le fichier** de noms des collègues
2. **Nombre de tables** et **taille de chaque table**
3. Possibilité d'**ajouter des personnes** manuellement
4. Vérification automatique qu'il y a **assez de places** (sinon, ajout de tables possible)
5. **Placement aléatoire** des collègues
6. Consultation du nombre de places libres, de personnes et de sièges totaux
7. Application de **contraintes** :
   - Personne seule à une table → déplacée automatiquement
   - Deux personnes **ne peuvent pas** être ensemble
   - Deux personnes **doivent** être ensemble
8. **Sauvegarde** du placement dans `seating_arrangement.txt` et affichage

---

## 📄 Format du fichier de noms

Le fichier d'entrée doit contenir **un nom par ligne**, par exemple :

```
Alice
Bob
Charlie
Diana
```

---

## 🧩 Architecture

### `Seat`
Représente un siège, lié à une table. Attributs : `free` (booléen), `occupant` (nom).

### `Table`
Tableau de `Seat`. Gère l'assignation, la libération et le déplacement d'occupants.

### `OpenSpace`
Tableau de `Table`. Orchestre le placement aléatoire, les contraintes de voisinage et la sauvegarde.

---

## ⚙️ Prérequis

- Python 3.x
- Aucune dépendance externe

---

## 📝 Exemple de sortie (`seating_arrangement.txt`)

```
Alice, Table 0
Bob, Table 0
Charlie, Table 1
Diana, Table 1
```