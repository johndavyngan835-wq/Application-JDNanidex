/* ════════════════════════════════════════════════
   main.js — JavaScript global JDN AniDex
   Gère l'écran de traitement et l'affichage des résultats
   Utilisé par quiz.html et survey.html
   ════════════════════════════════════════════════ */

/* ── ÉCRAN DE TRAITEMENT ── */
function showProc() {
  let proc = document.getElementById('proc-screen');
  if (!proc) {
    proc = document.createElement('div');
    proc.id = 'proc-screen';
    proc.className = 'proc-screen';
    document.querySelector('main').appendChild(proc);
  }
  proc.innerHTML = `
    <div class="proc-orb-wrap">
      <div class="ring1"></div><div class="ring2"></div>
      <div class="ring3"></div>
      <div class="ring-core">🎌</div>
    </div>
    <div class="proc-title">Analyse en cours…</div>
    <div class="proc-sub">JDN AniDex construit votre profil de fan unique.</div>
    <div class="proc-steps">
      <div class="proc-step done" id="ps1"><div class="step-dot"></div>Données enregistrées</div>
      <div class="proc-step run"  id="ps2"><div class="step-dot"></div>Analyse des réponses</div>
      <div class="proc-step"      id="ps3"><div class="step-dot"></div>Classification du profil</div>
      <div class="proc-step"      id="ps4"><div class="step-dot"></div>Génération des recommandations</div>
    </div>`;
  proc.style.display = 'block';

  // Animer les étapes
  setTimeout(() => setPS(2,'done'), 800);
  setTimeout(() => setPS(3,'run'),  900);
  setTimeout(() => setPS(3,'done'), 1800);
  setTimeout(() => setPS(4,'run'),  1900);
}

function setPS(n, s) {
  const e = document.getElementById('ps' + n);
  if (e) e.className = 'proc-step ' + s;
}

/* ── AFFICHAGE DES RÉSULTATS ── */
const PS_MAP = {
  'Otaku Hardcore': 'pp-otaku',
  'Expert Animé':   'pp-expert',
  'Fan Shōnen':     'pp-shonen',
  'Fan Casual':     'pp-casual',
  'Débutant':       'pp-newbie'
};

function showResults(data, mode, score) {
  // Masquer l'écran de traitement
  const proc = document.getElementById('proc-screen');
  if (proc) proc.style.display = 'none';

  // Créer ou trouver l'écran de résultats
  let rs = document.getElementById('result-screen');
  if (!rs) {
    rs = document.createElement('div');
    rs.id = 'result-screen';
    rs.className = 'result-screen';
    document.querySelector('main').appendChild(rs);
  }

  const profil   = data.profil  || 'Fan Casual';
  const emoji    = data.emoji   || '🎌';
  const confiance= data.confiance || 80;
  const resume   = data.resume  || '';
  const tags     = data.tags    || [];
  const recos    = data.recommandations || [];
  const scoreMsg = data.scoreMsg || '';
  const pillCls  = PS_MAP[profil] || 'pp-casual';

  const scoreHTML = (mode === 'Quiz' && score !== null)
    ? `${score}<span>/10</span>`
    : `<span style="font-size:1rem">${profil}</span>`;

  rs.innerHTML = `
    <div class="res-top">
      <span class="res-emoji">${emoji}</span>
      <div class="res-title">${profil.toUpperCase()}</div>
      <div class="res-score">${scoreHTML}</div>
      <div class="res-msg">${scoreMsg}</div>
    </div>

    <div class="res-card">
      <div class="rc-head">
        <span class="rc-label">✦ VOTRE PROFIL FAN</span>
      </div>
      <div class="prof-row">
        <span class="prof-pill ${pillCls}">${emoji} ${profil}</span>
        <div class="conf-block">
          <div class="conf-lbl">Correspondance</div>
          <div class="conf-trk">
            <div class="conf-fill" id="conf-fill" style="width:0%"></div>
          </div>
        </div>
      </div>
      <div class="res-summary">${resume}</div>
      <div class="res-tags">${tags.map(t => `<span class="res-tag">#${t}</span>`).join('')}</div>
    </div>

    <div class="res-card" style="border-color:rgba(0,204,255,.2)">
      <div class="rc-head">
        <span class="rc-label blue">✦ ANIMÉS RECOMMANDÉS POUR VOUS</span>
      </div>
      <div class="reco-grid">
        ${recos.map(r => `
          <div class="reco-item">
            <div class="reco-title">🎌 ${r.titre}</div>
            <div class="reco-genre">${r.genre}</div>
          </div>`).join('')}
      </div>
    </div>

    <a href="/" class="retry-btn">↩ Recommencer</a>`;

  rs.classList.add('active');
  rs.style.display = 'block';

  // Animer la barre de confiance
  setTimeout(() => {
    const fill = document.getElementById('conf-fill');
    if (fill) fill.style.width = confiance + '%';
  }, 400);
}
