# OSint Financial Tool

## Introduction

OSint Financial Tool est une plateforme interactive pour visualiser les incubateurs et accélérateurs de start-ups en Île-de-France, destinée à aider les entrepreneurs et les investisseurs à identifier les meilleures opportunités.

## Fonctionnalités

- **Carte Interactive** : Visualisation géographique des incubateurs et accélérateurs.
- **Bulles d'Information** : Détails contextuels sur les incubateurs et les start-ups.
- **Navigation Intuitive** : Barre de navigation latérale pour un accès rapide aux sections importantes.
- **API en Temps Réel** : Récupération dynamique des données sur les start-ups et conseils d'investissement.

## Prérequis

- Node.js
- npm (ou yarn)
- Git

## Installation

Clonez le dépôt et installez les dépendances :

```bash
git clone https://github.com/albert3661/OSINT.git
cd OSINT
npm install

Utilisation
Démarrer le serveur de développement
bash
Copier le code
npm start
Accéder à l'application
Ouvrez votre navigateur et allez à http://localhost:3000

API
Récupérer des données de start-ups
bash
Copier le code
GET /api/startup

Obtenir des conseils d'investissement
bash
Copier le code
GET /api/advice

Structure du Projet
src/ : Contient le code source de l'application.
public/ : Fichiers statiques.
api/ : Points d'accès API pour les données des start-ups et conseils d'investissement.
