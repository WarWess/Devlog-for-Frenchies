# Devlog-for-Frenchies
Fan-based french translation for DevLog : A Post Modern College Experience

## TODO : TRADUCTIONS A FAIRE POUR LA 0.2

Pour travailler sur le projet:
1. créer une branche feat/{quelque chose} depuis la branche develop
2. faire ses modifs et push
3. sur Github, aller sur "Pull requests" et effectuer une pull request vers develop
4. On vérifie les modifs et on valide
5. Un fois que develop a toutes les modifs validées pour une version de Devlog, je fais une MR sur main. 
6. La version finale de la traduction (prête pour le jeu) sera toujours sur main.

**NOTES** : J'ai pas fait de Git depuis longtemps, et c'est la première fois que je met des règles de sécurité sur les branches dans GitHub. **L'organisation git n'est donc pas parfaite**, mais la règle en place c'est **une fois les modifs de la branche feat/ mergées avec develop, la branche feat/ doit être supprimée**.

Pour faire fonctionner la traduction (en plein test) : 
+ Cloner le repo quelque part
+ Vous mettre sur la branche voulue (develop pour dev ou main si c'est juste avoir la traduction)
+ Coller tous les fichiers du jeu de base dans le repo
+ S'il y a des fichiers à écraser, les écraser puis `git pull` pour reprendre les fichiers de trad (ca concernera surtout des fichiers n'étant pas dans `/game/tl/`)

S'il y a des erreurs lors du chargement du jeu, vérifier qu'il n'y ait pas de fichier .rpyc dans les traductions. De ce que j'en comprend, c'est re-généré lors du lancement du jeu, donc on peut les dégager.

si des gens sont plus doués que moi en VSCode-ing et proposent des améliorations de ce git, faites :).