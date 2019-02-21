# Formation-flask

## La nécéssité d'un environnement virtuel

 Python est un langage qui possède de nombreuses librairies. Il peut arriver que vous travailliez sur plusieurs projets à la fois nécessitant chacun des librairies de version différente. Parfois, il y a aussi le soucis de "reproductibilité". Imaginez le scénario suivant : vous travaillez sur un projet sur votre ordinateur et vous souhaitez après le déployer sur un serveur. Si vous n'avez pas noté les librairies à installer quelque part, vous aller perdre du temps. De plus, si jamais une librairie a changé de version et que vous avez besoin d'une version précise, vous allez devoir désinstallé la librairie existante puis mettre l'ancienne version etc. Ce n'est pas du tout viable pour du long terme.
 
Une solution existe : travailler avec un environnement virtuel.

L'objectif est simple : créer un environnement qui ne possède aucune libraire de base et rajouter uniquement les libraires que nous avons besoin. Traditionnellement, on remplit un fichier texte et on installe les librairies grâce à l'outil pip dans notre environnement virtual.

Un autre avantage : l'environnement est un simple dossier que nous pouvons déplacer ! Vous pouvez donc sauvegarder vos librairies de cette manière.

## Virtualenv


Tout ceci est rendu possible grâce au packet virtualenv. Vous retrouverez les instructions d'installations dans le dossier 00_Install. 

```bash
cd 00_Install; bash install.sh
```

Pour activer votre environnement virtuel, tapez la commande suivante :

```bash
source venv/bin/activate
```

Pour le désactiver :
```bash
deactivate
```
