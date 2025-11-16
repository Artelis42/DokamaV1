feat(ui): amélioration du thème et ajout d’un bouton de rafraîchissement

📘 Résumé

Cette PR améliore l’interface graphique de l’application Almanax en :

ajoutant un bouton de rafraîchissement manuel,

améliorant la palette de couleurs du thème,

rendant la lecture plus claire grâce à une meilleure hiérarchie visuelle.

Ces modifications n’impactent pas la logique métier, uniquement l’affichage et le confort d’utilisation.

🎯 Objectif

Améliorer l’expérience utilisateur en permettant de :

mettre à jour les données sans redémarrer l’application,

profiter d’un thème visuel plus cohérent avec l’univers Dofus,

rendre les informations clés plus lisibles.

🛠️ Modifications incluses
UI (ui.py)

Ajout d’un bouton : "🔄 Rafraîchir les données"

Refonte du thème personnalisé (couleurs, styles ttk)

Amélioration de la structuration des frames :

Aujourd’hui

Prochains jours

Ajout du timestamp “Mis à jour : …”

Harmonisation des polices et couleurs

API (almanax_api.py)

Pas de changements majeurs, uniquement :

meilleure gestion d’erreurs

commentaires clarifiés

Divers

Reformatage du code (PEP8)

Nettoyage mineur des imports

🔍 Avant / Après
Avant

Pas de bouton de refresh

Couleurs de thème moins homogènes

Certaines zones difficilement lisibles

Pas de timestamp de dernière mise à jour

Après

Bouton de rafraîchissement fonctionnel

Thème Dofus-like plus soigné

Meilleure visibilité sur les ressources et bonus

Timestamp affiché en bas de page

🧪 Tests effectués

Chargement correct des données du jour

Chargement correct des 6 prochains jours

Fonctionnement du bouton Refresh

Vérification de la gestion d’erreur API :

Timeout simulé

Mauvais format JSON

Vérification manuelle du rendu UI sous Windows & Linux

📸 Captures (suggestion à inclure dans le README)

(À ajouter si tu as des screenshots)

Aperçu de l’UI avant

Aperçu de l’UI après

Extrait du diff

Exemple de commentaire de reviewer

📋 Checklist

 Code PEP8

 Tests manuels effectués

 Aucun secret exposé

 Fonctionnel sous Windows

 Fonctionnel sous Linux

 Relecture par un contributeur

 Documentation mise à jour

💬 Commentaires du reviewer (exemple)

✔️ Très bon découpage des commits
✔️ Thème plus cohérent, lisible et propre
❗ Petite suggestion : externaliser les couleurs dans un fichier theme.py

Sinon c’est ready to merge 🎉

🔀 Squash & merge

Je recommande un squash pour garder un historique propre :

feat(ui): amélioration du thème et ajout du bouton Refresh