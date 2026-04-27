# JDN AniDex — Guide complet

> **Toute la data des animés, en un seul endroit.**

---

## Structure des fichiers

```
jdn_anidex/
├── app.py              → Point d'entrée principal Flask
├── config.py           → Configuration (clés API, BDD, admin)
├── models.py           → Modèles de base de données
├── questions.py        → Banque de questions (ajoutez les vôtres ici)
├── requirements.txt    → Dépendances Python
│
├── templates/
│   ├── base.html       → Template de base (nav, styles)
│   ├── index.html      → Page d'accueil
│   ├── quiz.html       → Page quiz interactif
│   ├── survey.html     → Page sondage
│   └── admin/
│       ├── login.html  → Connexion admin
│       ├── dashboard.html → Gestion des questions
│       └── responses.html → Réponses et profils
│
└── static/
    ├── css/style.css   → Tous les styles (couleurs, layout)
    └── js/main.js      → JavaScript global
```

---

## Installation et lancement

### 1. Prérequis
- Python 3.10 ou supérieur
- pip

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Configurer la clé API
Ouvrez `config.py` et remplacez `VOTRE_CLE_API_ICI` par votre clé Anthropic :
```python
ANTHROPIC_API_KEY = 'sk-ant-...'
```
Ou via variable d'environnement :
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

### 4. Lancer l'application
```bash
python app.py
```
Ouvrez votre navigateur sur : **http://localhost:5000**

---

## Hébergement en ligne

### Option A — Railway (recommandé, gratuit)
1. Créez un compte sur https://railway.app
2. Connectez votre dépôt GitHub
3. Ajoutez la variable d'environnement `ANTHROPIC_API_KEY`
4. Railway détecte Flask automatiquement

### Option B — Render
1. Créez un compte sur https://render.com
2. "New Web Service" → connectez votre repo
3. Build command : `pip install -r requirements.txt`
4. Start command : `python app.py`

### Option C — PythonAnywhere
1. Créez un compte sur https://www.pythonanywhere.com
2. Uploadez vos fichiers
3. Configurez le WSGI pour Flask

---

## Modifications courantes

### Changer les couleurs fluorescentes
Ouvrez `static/css/style.css` et modifiez les variables CSS en haut :
```css
:root {
  --f1: #bf00ff;   /* violet électrique → changez ici */
  --f4: #00ccff;   /* cyan → changez ici */
  --f5: #ff00cc;   /* magenta → changez ici */
}
```

### Ajouter des questions au quiz
Ouvrez `questions.py` et ajoutez un dictionnaire à `QUESTION_BANK` :
```python
{
    'cat':  'Shōnen',
    'text': 'Votre question ?',
    'opts': ['Option A', 'Option B', 'Option C', 'Option D'],
    'ans':  'Option A',  # Doit être identique à une option
    'expl': 'Explication affichée après réponse.'
},
```
Puis supprimez `instance/jdn_anidex.db` et relancez `app.py`.

### Changer les identifiants admin
Dans `config.py` :
```python
ADMIN_USERNAME = 'votre_identifiant'
ADMIN_PASSWORD = 'votre_mot_de_passe_securise'
```

### Modifier le nombre de questions par partie
Dans `config.py` :
```python
QUIZ_QUESTIONS_COUNT = 15  # 15 questions au lieu de 10
```
Et dans `app.py`, ligne `random.sample(...)`, changez `10` en `15`.

### Changer le nom/slogan
Dans `templates/base.html`, cherchez :
```html
<span class="logo-jdn">JDN</span>
<span class="logo-anidex">AniDex</span>
```

### Modifier les profils possibles
Dans `app.py`, cherchez le prompt et modifiez la liste :
```python
"profil": "Otaku Hardcore, Expert Animé, Fan Shōnen, Fan Casual, ou Débutant"
```

---

## Accès admin
- URL : http://localhost:5000/admin
- Identifiant par défaut : `admin`
- Mot de passe par défaut : `admin123`

**⚠️ Changez ces identifiants avant de mettre en ligne !**

---

## Export des données
Dans l'espace admin → cliquez sur "Export CSV" pour télécharger toutes les réponses.
