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
#### a. (`if`) et (`else`)
DTL permet d'ajouter des conditions pour afficher certains contenus en fonction de critères.

#### Exemple :
```bash
{% for item in items %} 
{{ item.name }}
{% endfor %}
```
Cela affichera "Bienvenue sur votre profil!" si l'utilisateur est authentifié, sinon il affichera "Veuillez vous connecter."

#### b. Boucles (`for`)
DTL permet d'itérer sur des collections (comme des listes ou des dictionnaires) avec la balise for.

#### Exemple :
```bash
{% for item in items %} 
{{ item.name }}
{% endfor %} 
```
Cela générera une liste d'éléments avec leurs noms.

### 4. Filtres
Les filtres permettent de modifier ou formater les données avant leur affichage.

#### Exemple :
```bash
{{ user.email|lower }}
{{ person.active | yesno:"Active,Inactive" }} #person.active doit etre Boolean
```
Le filtre lower convertira l'email de l'utilisateur en minuscules avant de l'afficher.

### 5. Inclusions et héritage
#### a. Inclusions de templates
DTL permet d'inclure un autre template dans un template parent avec la balise (`{% include %}`).

#### Exemple :
```bash
{% include 'header.html' %}
```
Cela inclura le contenu du fichier (`header.html`) dans le template courant.

#### b. Héritage de templates
DTL permet d'étendre un template de base avec la balise (`{% block %}`) et (`{% extends %}`).

#### Exemple (template parent base.html) :
```bash
{% block header %}Header par défaut{% endblock %} 
{% block content %}Contenu principal{% endblock %}  
{% block footer %}Footer par défaut{% endblock %}
```
#### Exemple (template enfant home.html) :
```bash
{% extends 'base.html' %} 
{% block title %}Page d'Accueil{% endblock %} 
{% block header %}Bienvenue sur notre site{% endblock %} 
{% block content %}Bienvenue sur la page d'accueil{% endblock %}
```
Ce code hérite de (`base.html`) et remplace certains blocs avec des contenus personnalisés.

### 6. Sécurité
Django applique des mesures de sécurité par défaut dans les templates. Par exemple, l'échappement automatique des caractères spéciaux dans les variables pour prévenir les attaques Cross-site Scripting (XSS).

#### Exemple :
```bash
{{ user_input }}
```
Si (`user_input`) contient des balises HTML ou des scripts, Django les échappe automatiquement pour éviter l'exécution de code malveillant.

### 7. Chargement de fichiers statiques
DTL permet d'inclure facilement des fichiers CSS, JavaScript et images dans le template.

#### Exemple :
```bash
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'style.css' %}">
```
Cela inclut le fichier (`style.css`) depuis le dossier statique. 













