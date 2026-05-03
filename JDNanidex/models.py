"""
models.py — Modèles de base de données
═══════════════════════════════════════

Contient les deux tables principales :
    - Question  : banque de questions du quiz
    - Response  : réponses et profils des participants

COMMENT AJOUTER UN CHAMP :
    1. Ajouter la colonne dans la classe
    2. Supprimer le fichier instance/jdn_anidex.db
    3. Relancer app.py (les tables se recréent)
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Question(db.Model):
    """
    Table des questions du quiz.
    Chaque question a 4 options (A, B, C, D) et une bonne réponse.
    """
    __tablename__ = 'questions'

    id             = db.Column(db.Integer, primary_key=True)
    category       = db.Column(db.String(50),  nullable=False)  # Ex: "Shōnen", "Isekai"
    text           = db.Column(db.Text,         nullable=False)  # Texte de la question
    option_a       = db.Column(db.String(200),  nullable=False)
    option_b       = db.Column(db.String(200),  nullable=False)
    option_c       = db.Column(db.String(200),  nullable=False)
    option_d       = db.Column(db.String(200),  nullable=False)
    correct_answer = db.Column(db.String(200),  nullable=False)  # Doit correspondre à une option
    explanation    = db.Column(db.Text,         nullable=True)   # Explication après réponse
    created_at     = db.Column(db.DateTime,     default=datetime.utcnow)
    is_active      = db.Column(db.Boolean,      default=True)    # False = question désactivée

    def to_dict(self):
        return {
            'id':       self.id,
            'cat':      self.category,
            'text':     self.text,
            'opts':     [self.option_a, self.option_b, self.option_c, self.option_d],
            'ans':      self.correct_answer,
            'expl':     self.explanation or ''
        }

    def __repr__(self):
        return f'<Question {self.id}: {self.text[:50]}>'


class Response(db.Model):
    """
    Table des réponses des participants.
    Enregistre chaque soumission (quiz ou sondage) avec le profil généré.
    """
    __tablename__ = 'responses'

    id              = db.Column(db.Integer,    primary_key=True)
    mode            = db.Column(db.String(20), nullable=False)   # 'quiz' ou 'sondage'
    score           = db.Column(db.Integer,    nullable=True)    # Score /10 (quiz seulement)
    profile         = db.Column(db.String(50), nullable=True)    # Profil attribué
    summary         = db.Column(db.Text,       nullable=True)    # Résumé du profil
    tags            = db.Column(db.Text,       nullable=True)    # JSON: ["tag1","tag2"]
    recommendations = db.Column(db.Text,       nullable=True)    # JSON: [{"titre":...}]
    survey_data     = db.Column(db.Text,       nullable=True)    # JSON des réponses sondage
    created_at      = db.Column(db.DateTime,   default=datetime.utcnow)

    # ── Champs détaillés sondage (pour analyse statistique) ──
    age             = db.Column(db.String(30),  nullable=True)   # Tranche d'âge
    gender          = db.Column(db.String(30),  nullable=True)   # Genre
    freq            = db.Column(db.String(20),  nullable=True)   # Épisodes/semaine
    since           = db.Column(db.String(30),  nullable=True)   # Ancienneté
    platform        = db.Column(db.String(50),  nullable=True)   # Plateforme
    genre_pref      = db.Column(db.String(50),  nullable=True)   # Genre favori
    studio          = db.Column(db.String(50),  nullable=True)   # Studio favori
    passion_rate    = db.Column(db.Integer,     nullable=True)   # Note de passion 1–5
    convention      = db.Column(db.String(50),  nullable=True)   # Convention visitée
    merch           = db.Column(db.String(50),  nullable=True)   # Produits dérivés
    fav_anime       = db.Column(db.String(100), nullable=True)   # Animé préféré

    def __repr__(self):
        return f'<Response {self.id}: {self.mode} | {self.profile}>'
