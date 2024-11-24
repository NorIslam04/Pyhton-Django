# Django Template Language (DTL)

Le **Django Template Language (DTL)** est le moteur de templates intégré à **Django**, un framework web Python. Il permet de générer dynamiquement du contenu HTML en associant des données avec des templates HTML.

## Fonctionnalités principales

## Syntaxe simple
DTL utilise une syntaxe claire et facile à comprendre. Les balises sont délimitées par des accolades et des pourcentages (`{% %}`) pour les instructions, et des doubles accolades (`{{ }}`) pour l'affichage des variables.

### 1. Variables
Les variables passées depuis le contexte de la vue peuvent être affichées en les entourant de doubles accolades.

#### Exemple :
```bash
Bienvenue, {{ user.username }}
```
Si la vue passe une variable user.username, le nom d'utilisateur sera affiché dans la balise.

### 3. Balises conditionnelles et de contrôle de flux
#### a. if et else
DTL permet d'ajouter des conditions pour afficher certains contenus en fonction de critères.

#### Exemple :
```bash
{% for item in items %} 
{{ item.name }}
{% endfor %}
```
Cela affichera "Bienvenue sur votre profil!" si l'utilisateur est authentifié, sinon il affichera "Veuillez vous connecter."













