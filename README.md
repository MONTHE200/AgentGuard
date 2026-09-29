# AgentGuard

## Présentation

AgentGuard est une passerelle de sécurité conçue pour protéger les systèmes d'IA agentique.

L'objectif du projet est de contrôler, surveiller et sécuriser les actions effectuées par des agents IA avant qu'ils n'accèdent à des ressources sensibles telles que des bases de données, des fichiers, des APIs ou des systèmes d'information.

Le projet s'inspire des principes de cybersécurité modernes :

- Zero Trust
- Défense en profondeur
- Contrôle d'accès
- Gestion des risques
- Journalisation et audit

---

## Problématique

Les agents IA modernes sont capables d'effectuer des actions de manière autonome :

- consulter des données ;
- envoyer des e-mails ;
- modifier des fichiers ;
- exécuter des requêtes ;
- utiliser des outils externes.

Cependant, une erreur, une mauvaise configuration ou une attaque par prompt injection peut entraîner des actions dangereuses.

AgentGuard agit comme une couche de sécurité placée entre les agents et les ressources critiques.

---

## Architecture

```text
Utilisateur
      │
      ▼
  Agent IA
      │
      ▼
 AgentGuard
 ├── Identity Manager
 ├── Policy Engine
 ├── Risk Engine
 ├── DLP
 ├── Audit Logger
 └── Prompt Security
      │
      ▼
ALLOW / BLOCK / APPROVAL
      │
      ▼
Base de données
Fichiers
API
Messagerie
```

---

## Fonctionnalités prévues

### Contrôle d'accès

Gestion des identités et des rôles des agents.

Exemples :

- FinanceAgent
- HRAgent
- EmailAgent

Chaque agent dispose de permissions spécifiques.

---

### Moteur de politiques (Policy Engine)

Application de règles de sécurité :

- autoriser une action ;
- bloquer une action ;
- demander une validation humaine.

Exemple :

```text
FinanceAgent peut lire les données comptables
FinanceAgent ne peut pas supprimer la base client
```

---

### Calcul du risque

Chaque action reçoit un score de risque.

Exemple :

```text
Lecture d'un fichier public = risque faible
Export complet d'une base client = risque élevé
```

---

### Protection contre les prompt injections

Détection des tentatives visant à contourner les règles de sécurité.

Exemple :

```text
Ignore toutes les instructions précédentes
```

---

### Prévention des fuites de données (DLP)

Détection de données sensibles :

- adresses e-mail ;
- numéros de téléphone ;
- informations personnelles ;
- données confidentielles.

---

### Validation humaine

Certaines actions critiques nécessitent l'approbation d'un utilisateur.

Exemple :

```text
Suppression d'une base de données
```

---

### Journalisation et audit

Toutes les décisions de sécurité sont enregistrées :

- autorisations ;
- refus ;
- alertes ;
- tentatives suspectes.

---

## Technologies

- Python
- FastAPI
- Pydantic
- Git
- Docker
- PostgreSQL
- JSON
- VS Code

---

## Installation

Créer un environnement virtuel :

```bash
python -m venv venv
```

Activer l'environnement :

### PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Invite de commandes

```cmd
venv\Scripts\activate.bat
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## Objectifs pédagogiques

Ce projet permet de mettre en pratique :

- le développement Python ;
- les APIs REST ;
- la cybersécurité ;
- le principe du moindre privilège ;
- le contrôle d'accès RBAC ;
- le Zero Trust ;
- la sécurisation des systèmes d'IA agentique.

---

## État du projet

🚧 Projet en cours de développement.

---

## Auteur

Projet personnel réalisé dans le cadre d'un apprentissage en cybersécurité et IA agentique.