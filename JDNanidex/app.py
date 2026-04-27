"""
╔══════════════════════════════════════════════════════════════╗
║              JDN AniDex — Application Flask                 ║
║     Toute la data des animés, en un seul endroit.           ║
╚══════════════════════════════════════════════════════════════╝

Structure du projet :
    jdn_anidex/
    ├── app.py              ← CE FICHIER (point d'entrée principal)
    ├── config.py           ← Configuration (clés, BDD, etc.)
    ├── models.py           ← Modèles de base de données
    ├── questions.py        ← Banque de questions (1000+ animés)
    ├── requirements.txt    ← Dépendances Python
    ├── templates/
    │   ├── base.html       ← Template de base (nav, styles)
    │   ├── index.html      ← Page d'accueil (hero)
    │   ├── quiz.html       ← Page quiz
    │   ├── survey.html     ← Page sondage
    │   ├── results.html    ← Page résultats
    │   ├── admin/
    │   │   ├── login.html  ← Connexion admin
    │   │   ├── dashboard.html ← Tableau de bord
    │   │   └── responses.html ← Réponses & profils
    └── static/
        ├── css/style.css   ← Styles globaux
        └── js/main.js      ← JavaScript global

COMMENT LANCER :
    pip install -r requirements.txt
    python app.py

COMMENT MODIFIER :
    - Ajouter des questions   → questions.py
    - Changer les couleurs    → static/css/style.css
    - Modifier l'apparence    → templates/
    - Changer la config       → config.py
"""

from flask import (
    Flask, render_template, request, jsonify,
    session, redirect, url_for, flash
)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import random
import os

from config import Config
from models import db, Response, Question
from questions import QUESTION_BANK

# ──────────────────────────────────────────────
# Initialisation de l'application
# ──────────────────────────────────────────────
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# ──────────────────────────────────────────────
# Création des tables au démarrage
# ──────────────────────────────────────────────
with app.app_context():
    db.create_all()
    # Pré-remplir la BDD avec les questions si elle est vide
    if Question.query.count() == 0:
        for q in QUESTION_BANK:
            question = Question(
                category=q['cat'],
                text=q['text'],
                option_a=q['opts'][0],
                option_b=q['opts'][1],
                option_c=q['opts'][2],
                option_d=q['opts'][3],
                correct_answer=q['ans'],
                explanation=q['expl']
            )
            db.session.add(question)
        db.session.commit()
        print(f"✓ {len(QUESTION_BANK)} questions importées en base de données.")


# ══════════════════════════════════════════════
#  ROUTES PUBLIQUES (Espace Fan)
# ══════════════════════════════════════════════

@app.route('/')
def index():
    """Page d'accueil avec les deux modes."""
    return render_template('index.html')


@app.route('/quiz')
def quiz():
    """Page du quiz — 10 questions aléatoires."""
    # Tirer 10 questions aléatoires depuis la BDD
    all_questions = Question.query.all()
    selected = random.sample(all_questions, min(10, len(all_questions)))

    # Mélanger les options de chaque question
    questions_data = []
    for q in selected:
        opts = [q.option_a, q.option_b, q.option_c, q.option_d]
        random.shuffle(opts)
        questions_data.append({
            'id':   q.id,
            'cat':  q.category,
            'text': q.text,
            'opts': opts,
            'ans':  q.correct_answer,
            'expl': q.explanation
        })

    # Stocker en session pour validation côté serveur
    session['quiz_questions'] = [q['id'] for q in questions_data]

    return render_template('quiz.html', questions=questions_data)


@app.route('/survey')
def survey():
    """Page du sondage fan."""
    return render_template('survey.html')


@app.route('/api/analyze', methods=['POST'])
def analyze():
    """
    Route API — Analyse locale sans clé API.
    Le profil et les recommandations sont générés à partir des réponses,
    sans aucun appel à un service externe.
    """
    data = request.get_json()
    mode = data.get('mode', 'quiz')
    score = data.get('score', 0)
    survey_data = data.get('survey_data', {})

    # ── Catalogue de recommandations par genre ──
    CATALOGUE = {
        "Shōnen": [
            {"titre": "Demon Slayer", "genre": "Shōnen"},
            {"titre": "My Hero Academia", "genre": "Shōnen"},
            {"titre": "Naruto Shippuden", "genre": "Shōnen"},
            {"titre": "Black Clover", "genre": "Shōnen"},
            {"titre": "Bleach", "genre": "Shōnen"},
            {"titre": "One Piece", "genre": "Shōnen"},
            {"titre": "Jujutsu Kaisen", "genre": "Shōnen"},
        ],
        "Action": [
            {"titre": "Attack on Titan", "genre": "Action"},
            {"titre": "Chainsaw Man", "genre": "Action"},
            {"titre": "Hunter x Hunter", "genre": "Action"},
            {"titre": "Vinland Saga", "genre": "Action"},
            {"titre": "Dororo", "genre": "Action"},
        ],
        "Science-Fiction": [
            {"titre": "Steins;Gate", "genre": "Science-Fiction"},
            {"titre": "Psycho-Pass", "genre": "Science-Fiction"},
            {"titre": "Neon Genesis Evangelion", "genre": "Science-Fiction"},
            {"titre": "Trigun Stampede", "genre": "Science-Fiction"},
            {"titre": "Vivy: Fluorite Eye's Song", "genre": "Science-Fiction"},
        ],
        "Isekai": [
            {"titre": "Re:Zero", "genre": "Isekai"},
            {"titre": "That Time I Got Reincarnated as a Slime", "genre": "Isekai"},
            {"titre": "KonoSuba", "genre": "Isekai"},
            {"titre": "Overlord", "genre": "Isekai"},
            {"titre": "Made in Abyss", "genre": "Isekai"},
        ],
        "Drame": [
            {"titre": "Violet Evergarden", "genre": "Drame"},
            {"titre": "A Silent Voice", "genre": "Drame"},
            {"titre": "Clannad After Story", "genre": "Drame"},
            {"titre": "Your Lie in April", "genre": "Drame"},
            {"titre": "Anohana", "genre": "Drame"},
        ],
        "Aventure": [
            {"titre": "Fullmetal Alchemist Brotherhood", "genre": "Aventure"},
            {"titre": "Magi: The Labyrinth of Magic", "genre": "Aventure"},
            {"titre": "Sword Art Online", "genre": "Aventure"},
            {"titre": "Fairy Tail", "genre": "Aventure"},
            {"titre": "The Rising of the Shield Hero", "genre": "Aventure"},
        ],
        "Romance": [
            {"titre": "Toradora!", "genre": "Romance"},
            {"titre": "Oregairu", "genre": "Romance"},
            {"titre": "Horimiya", "genre": "Romance"},
            {"titre": "Kaguya-sama: Love is War", "genre": "Romance"},
            {"titre": "Fruits Basket", "genre": "Romance"},
        ],
        "Fantastique": [
            {"titre": "Mushishi", "genre": "Fantastique"},
            {"titre": "Moribito", "genre": "Fantastique"},
            {"titre": "The Ancient Magus' Bride", "genre": "Fantastique"},
            {"titre": "Inuyasha", "genre": "Fantastique"},
            {"titre": "Noragami", "genre": "Fantastique"},
        ],
    }
    ALL_ANIMES = [a for lst in CATALOGUE.values() for a in lst]

    def pick_recos(genre_pref=None, exclude=None, n=3):
        pool = CATALOGUE.get(genre_pref, []) if genre_pref else []
        pool = [a for a in pool if a['titre'] != exclude]
        if len(pool) < n:
            extras = [a for a in ALL_ANIMES if a not in pool and a['titre'] != exclude]
            random.shuffle(extras)
            pool += extras
        return pool[:n]

    # ── Analyse QUIZ ──
    if mode == 'quiz':
        if score >= 9:
            profil, emoji, confiance = "Otaku Hardcore", "🔥", random.randint(93, 99)
            resume = f"Score parfait de {score}/10 ! Votre maîtrise de l'univers des animés est absolument impressionnante. Vous êtes une véritable encyclopédie vivante."
            tags = ["otaku", "expert", "encyclopédie", "hardcore"]
            score_msg = "Légendaire ! Très peu atteignent ce niveau."
            recos = pick_recos("Science-Fiction", n=3)
        elif score >= 7:
            profil, emoji, confiance = "Expert Animé", "⭐", random.randint(85, 92)
            resume = f"Excellent score de {score}/10 ! Votre culture animé est solide et variée. Vous pouvez conseiller n'importe quel fan autour de vous."
            tags = ["expert", "culture", "anime", "connaisseur"]
            score_msg = "Impressionnant ! Vous faites partie des meilleurs."
            recos = pick_recos("Action", n=3)
        elif score >= 5:
            profil, emoji, confiance = "Fan Shōnen", "🌊", random.randint(78, 87)
            resume = f"Score de {score}/10 — vous avez de bonnes bases ! Votre passion pour les shōnens et l'action est évidente. Continuez à explorer."
            tags = ["shōnen", "fan", "action", "passionné"]
            score_msg = "Bonne performance ! Quelques classiques à découvrir encore."
            recos = pick_recos("Shōnen", n=3)
        elif score >= 3:
            profil, emoji, confiance = "Fan Casual", "🌸", random.randint(75, 82)
            resume = f"Score de {score}/10 — vous débutez dans l'univers des animés. Chaque série regardée vous rapprochera du niveau expert !"
            tags = ["casual", "découverte", "anime", "débutant"]
            score_msg = "Bon début ! L'aventure ne fait que commencer."
            recos = pick_recos("Aventure", n=3)
        else:
            profil, emoji, confiance = "Débutant", "🌱", random.randint(75, 80)
            resume = f"Score de {score}/10 — bienvenue dans le monde des animés ! Chaque grand otaku a commencé ici. Les plus belles découvertes vous attendent."
            tags = ["débutant", "nouveau", "anime", "curiosité"]
            score_msg = "Bienvenue ! Votre aventure animé commence maintenant."
            recos = pick_recos("Drame", n=3)

    # ── Analyse SONDAGE ──
    else:
        genre = survey_data.get('genre', '')
        freq  = survey_data.get('freq', '')
        rate  = int(survey_data.get('rate', 5))
        fav   = survey_data.get('fav', '')

        # Déterminer le profil selon fréquence + passion
        if freq in ['Tous les jours', 'Chaque semaine'] and rate >= 8:
            profil, emoji, confiance = "Otaku Hardcore", "🔥", random.randint(88, 97)
            resume = "Vous regardez des animés presque quotidiennement avec une passion intense. L'anime est clairement au cœur de votre vie culturelle."
            tags = ["otaku", "passionné", "quotidien", "hardcore"]
            score_msg = "Un vrai otaku de cœur !"
        elif rate >= 7:
            profil, emoji, confiance = "Expert Animé", "⭐", random.randint(82, 91)
            resume = "Votre amour pour les animés est profond et sincère. Vous avez une culture solide et des goûts affirmés qui vous définissent."
            tags = ["expert", "culture", "passionné", "connaisseur"]
            score_msg = "Un fan accompli et passionné !"
        elif freq in ['Quelques fois par mois']:
            profil, emoji, confiance = "Fan Casual", "🌸", random.randint(78, 86)
            resume = "Vous appréciez les animés à votre rythme, en sélectionnant soigneusement vos séries. Qualité avant quantité — c'est votre philosophie."
            tags = ["casual", "sélectif", "qualité", "fan"]
            score_msg = "Un fan équilibré et sélectif !"
        else:
            profil, emoji, confiance = "Débutant", "🌱", random.randint(75, 82)
            resume = "Vous découvrez l'univers des animés avec curiosité. Un monde extraordinaire de récits et de personnages inoubliables vous attend."
            tags = ["débutant", "curieux", "découverte", "nouveau"]
            score_msg = "Bienvenue dans l'univers des animés !"

        recos = pick_recos(genre if genre in CATALOGUE else None, exclude=fav, n=3)

    result = {
        "profil": profil,
        "emoji": emoji,
        "confiance": confiance,
        "resume": resume,
        "tags": tags,
        "recommandations": recos,
        "scoreMsg": score_msg,
    }

    # ── Enregistrement en base de données ──
    try:
        response = Response(
            mode=mode,
            score=score if mode == 'quiz' else None,
            profile=result.get('profil'),
            summary=result.get('resume'),
            tags=json.dumps(result.get('tags', [])),
            recommendations=json.dumps(result.get('recommandations', [])),
            survey_data=json.dumps(survey_data) if survey_data else None,
            created_at=datetime.utcnow()
        )
        db.session.add(response)
        db.session.commit()
    except Exception as e:
        print(f"Erreur BDD : {e}")

    return jsonify(result)


@app.route('/community')
def community():
    """Page publique — Observatoire statistique communautaire."""
    return render_template('community.html')


@app.route('/results')
def results():
    """Page résultats (rendu côté serveur si besoin)."""
    return render_template('results.html')


# ══════════════════════════════════════════════
#  ROUTES ADMIN (protégées par session)
# ══════════════════════════════════════════════

def admin_required(f):
    """Décorateur : redirige vers login si non connecté."""
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated


@app.route('/admin')
@admin_required
def admin_dashboard():
    """Tableau de bord admin — questions et statistiques."""
    questions = Question.query.all()
    total_responses = Response.query.count()
    avg_score = db.session.query(
        db.func.avg(Response.score)
    ).filter(Response.score.isnot(None)).scalar()

    # Distribution des profils
    profiles = db.session.query(
        Response.profile,
        db.func.count(Response.profile).label('count')
    ).group_by(Response.profile).all()

    stats = {
        'total_questions': len(questions),
        'total_responses': total_responses,
        'avg_score': round(avg_score, 1) if avg_score else 0,
        'profiles': {p.profile: p.count for p in profiles}
    }

    return render_template('admin/dashboard.html',
                           questions=questions, stats=stats)


@app.route('/admin/responses')
@admin_required
def admin_responses():
    """Page des réponses et profils."""
    responses = Response.query.order_by(Response.created_at.desc()).all()
    # Parser les JSON
    for r in responses:
        r.tags_list = json.loads(r.tags) if r.tags else []
        r.recos_list = json.loads(r.recommendations) if r.recommendations else []

    return render_template('admin/responses.html', responses=responses)


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """Connexion admin."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if (username == app.config['ADMIN_USERNAME'] and
                password == app.config['ADMIN_PASSWORD']):
            session['admin_logged_in'] = True
            session.permanent = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Identifiants incorrects.', 'error')
    return render_template('admin/login.html')


@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))


# ── Page Analyse Statistique ──
@app.route('/admin/statistics')
@admin_required
def admin_statistics():
    """Page d'analyse statistique avancée."""
    return render_template('admin/statistics.html')


# ── API Admin : données statistiques ──
@app.route('/admin/api/statistics')
@admin_required
def admin_api_statistics():
    """Retourne toutes les statistiques en JSON pour les graphiques."""
    import math
    from collections import Counter
    from datetime import timedelta

    responses = Response.query.all()
    total = len(responses)

    # Distribution des modes
    mode_dist = Counter(r.mode for r in responses)

    # Distribution des profils
    profiles = Counter(r.profile for r in responses if r.profile)
    top_profile = profiles.most_common(1)[0][0] if profiles else None

    # Stats sur les scores (quiz uniquement)
    scores = [r.score for r in responses if r.score is not None]
    score_dist = {str(i): 0 for i in range(11)}
    for s in scores:
        if 0 <= s <= 10:
            score_dist[str(s)] += 1

    def mean(lst): return round(sum(lst)/len(lst), 2) if lst else None
    def median(lst):
        if not lst: return None
        s = sorted(lst)
        n = len(s)
        return s[n//2] if n % 2 else round((s[n//2-1]+s[n//2])/2, 1)
    def std(lst):
        if len(lst) < 2: return None
        m = mean(lst)
        return round(math.sqrt(sum((x-m)**2 for x in lst)/len(lst)), 2)

    score_stats = {
        'mean':   mean(scores),
        'median': median(scores),
        'std':    std(scores),
        'min':    min(scores) if scores else None,
        'max':    max(scores) if scores else None,
    }

    # Tendance 7 derniers jours
    today = datetime.utcnow().date()
    trend = []
    for i in range(6, -1, -1):
        day = today - timedelta(days=i)
        count = sum(
            1 for r in responses
            if r.created_at and r.created_at.date() == day
        )
        trend.append({'date': day.strftime('%d/%m'), 'count': count})

    # Genres les plus recommandés
    genre_counter = Counter()
    for r in responses:
        if r.recommendations:
            try:
                recos = json.loads(r.recommendations)
                for reco in recos:
                    g = reco.get('genre', '').strip()
                    if g:
                        genre_counter[g] += 1
            except Exception:
                pass
    top_genres = genre_counter.most_common(10)

    # Top animés recommandés
    anime_counter = {}
    for r in responses:
        if r.recommendations:
            try:
                recos = json.loads(r.recommendations)
                for reco in recos:
                    title = reco.get('titre', '').strip()
                    genre = reco.get('genre', '').strip()
                    if title:
                        if title not in anime_counter:
                            anime_counter[title] = {'count': 0, 'genre': genre}
                        anime_counter[title]['count'] += 1
            except Exception:
                pass
    top_animes = sorted(anime_counter.items(), key=lambda x: x[1]['count'], reverse=True)[:10]

    return jsonify({
        'total': total,
        'mode_distribution': dict(mode_dist),
        'profiles': dict(profiles),
        'top_profile': top_profile,
        'score_distribution': score_dist,
        'score_stats': score_stats,
        'trend': trend,
        'top_genres': top_genres,
        'top_animes': top_animes,
    })


# ── API Admin : ajouter une question ──
@app.route('/admin/api/questions', methods=['POST'])
@admin_required
def admin_add_question():
    data = request.get_json()
    q = Question(
        category=data.get('category', 'Divers'),
        text=data.get('text'),
        option_a=data.get('option_a'),
        option_b=data.get('option_b'),
        option_c=data.get('option_c'),
        option_d=data.get('option_d'),
        correct_answer=data.get('correct_answer'),
        explanation=data.get('explanation', '')
    )
    db.session.add(q)
    db.session.commit()
    return jsonify({'success': True, 'id': q.id})


# ── API Admin : supprimer une question ──
@app.route('/admin/api/questions/<int:qid>', methods=['DELETE'])
@admin_required
def admin_delete_question(qid):
    q = Question.query.get_or_404(qid)
    db.session.delete(q)
    db.session.commit()
    return jsonify({'success': True})


# ── API Admin : export CSV ──
@app.route('/admin/export/csv')
@admin_required
def export_csv():
    import csv
    import io
    from flask import make_response

    responses = Response.query.order_by(Response.created_at.desc()).all()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['#', 'Date', 'Mode', 'Score', 'Profil', 'Résumé', 'Recommandations'])

    for i, r in enumerate(responses, 1):
        recos = json.loads(r.recommendations) if r.recommendations else []
        recos_str = ', '.join([x.get('titre', '') for x in recos])
        writer.writerow([
            i,
            r.created_at.strftime('%d/%m/%Y %H:%M'),
            r.mode,
            r.score if r.score is not None else '—',
            r.profile,
            r.summary,
            recos_str
        ])

    resp = make_response(output.getvalue())
    resp.headers['Content-Type'] = 'text/csv; charset=utf-8'
    resp.headers['Content-Disposition'] = 'attachment; filename=jdn_anidex_responses.csv'
    return resp


# ──────────────────────────────────────────────
# Lancement
# ──────────────────────────────────────────────
if __name__ == '__main__':
    print("=" * 60)
    print("  JDN AniDex — Serveur Flask")
    print("  http://localhost:5000")
    print("  Admin : http://localhost:5000/admin")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)
