🌿 Almanax Dofus – Guide Journalier
🎯 Objectif

Application desktop (Tkinter) permettant d’afficher rapidement :

l’offrande de l’Almanax du jour,

son bonus associé,

et un aperçu des jours suivants.

Elle interroge l’API publique dofusdu.de pour fournir les informations actualisées.

🚀 Démarrage

Prérequis :

Python 3.10+

requests installé (pip install requests)

Aucun secret/API key requis

Fonctionne sur Windows, Linux, macOS

Installation :

git clone <repository>
cd DOKAMAV1
pip install requests


Lancement :

python main.py


Variables d’environnement :
Aucune variable nécessaire.

Tests :
Pas encore implémentés (YAGNI pour l’instant).

🗂️ Structure
.
├── main.py                # Point d’entrée de l'application
├── ui.py                  # Interface graphique (Tkinter)
├── almanax_api.py         # Récupération des données via API
├── utils.py               # Fonctions utilitaires (formatage de date)

🧭 Conventions

Nommage Python PEP8

Style UI cohérent (Dofus-like) via Tkinter + ttk

Code formatté avec Black (recommandé)

Branches Git suggérées : main, feature/..., fix/...

PR courtes et isolées par fonctionnalité

📡 Observabilité

Logs d’erreurs réseau/API via print (simple mais suffisant pour une app locale)

Statut de mise à jour affiché en bas de l’UI

Pas de métriques internes (YAGNI)

🔐 Sécurité de base

Aucun secret géré

Validation légère sur parsing JSON

Gestion d’erreurs réseau (try / except)

Dépendances minimales (requests, Tkinter natif)

🧭 Limites & pistes

Ajouter des tests unitaires (mock API)

Faire un cache local pour réduire les appels API

Gérer mode sombre / clair automatiquement

Ajouter export PDF / capture des données

Ajouter un sélecteur de date custom

Passer à asyncio pour éviter le blocage UI

Internationalisation FR/EN