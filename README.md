# Chatbot de Support Client
## Introduction
Une brève introduction à votre projet de chatbot de support client, expliquant son objectif et ses fonctionnalités principales.

## Prérequis
Liste des éléments nécessaires pour exécuter le projet :
- Python 3.7+
- Un compte OpenAI avec une clé API valide
- Un fichier .env contenant votre clé API OpenAI
- Un fichier faq_fr.txt contenant les questions fréquentes et leurs réponses

## Installation
Instructions étape par étape pour installer et configurer le projet :

1. Cloner ce dépôt :
```bash
git clone https://github.com/votre-dépôt/chatbot-support-client.git
cd chatbot-support-client
```

2. Créer un environnement virtuel et l'activer :
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Installer les dépendances du projet :
```bash
pip install -r requirements.txt
```



## Utilisation
Instructions pour utiliser le projet :

- [1] Pour poser une question
- [2] Pour quitter

## Détails du Code
Explications sur les différentes sections du code :

- **Chargement des Variables d'Environnement** : Comment le fichier .env est utilisé pour charger la clé API OpenAI.
- **Configuration du Modèle** : Le modèle de langage utilisé (gpt-3.5-turbo).
- **Templates de Prompts** : Les templates utilisés pour formater les messages du système et de l'utilisateur.
- **Chargement et Traitement des Documents** : Comment les documents de FAQ sont chargés et découpés.
- **Chargement des Embeddings** : La création des embeddings pour permettre la recherche de similarités.
- **Génération de Réponses** : La chaîne de traitement pour générer des réponses basées sur les questions des utilisateurs et le contexte.
- **Fonction Principale** : Le menu principal du chatbot permettant de poser des questions ou de quitter l'application.
- **Fonction de Traitement des Questions** : Comment les questions des utilisateurs sont traitées et les réponses générées.

## Conclusion
Une brève conclusion sur l'utilité du projet et comment il peut être personnalisé pour répondre aux besoins spécifiques de votre support client.
