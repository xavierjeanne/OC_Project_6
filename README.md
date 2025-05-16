# OC_Project_6
Ce projet fait partie du cours de développement Python d'OpenClassrooms. Le but de ce projet est de résoudre des problèmes en utlisant des algorithmes en Python.

## Description
Concevoir un algorithme qui maximisera le profit réalisé par les clients après deux ans d'investissement.
Les contraintes sont les suivantes :    
- Le budget total ne doit pas dépasser 500€ / client.
- Impossible d'acheter des fractions d'action.
- Chaque action ne peut être acheté qu'une fois.

le programme essaie toutes les différentes combinaisons d'actions qui correspondent aux contraintes, et choisit le meilleur résultat. Le programme doit donc lire un fichier contenant des informations sur les actions, explorer toutes les combinaisons possibles et afficher le meilleur investissement.

Dans un premier temps, le programme utilise la méthode brute force pour trouver la meilleure combinaison d'actions. La méthode brute force consiste à explorer toutes les combinaisons possibles d'actions et à choisir la meilleure combinaison qui correspond aux contraintes.

## Prérequis

- Python 3.x
- Git

## Installation

1. Clonez ce dépôt :
   Dans un terminal, exécuter la commande suivante : 
   git clone https://github.com/xavierjeanne/OC_Project_6.git

2. Accéder au répertoire du projet :
   cd Oc_project_6

   
3. Créer un environnement virtuel, l'activer puis installer les dépendances :
   python -m venv env
   source env\Scripts\activate
   pip install -r requirements.txt

4. Executer le script :
   python bruteforce.py