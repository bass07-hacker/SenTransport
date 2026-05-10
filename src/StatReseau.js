import './StatReseau.css';

function StatReseau({ lignes }) {
  const nbLignes = lignes.length;
  const totalArrets = lignes.reduce((total, ligne) => total + ligne.arrets, 0);
  const ligneMaxArrets = lignes.reduce((max, ligne) => 
    ligne.arrets > max.arrets ? ligne : max
  , lignes[0]);

  return (
    <div className="stat-reseau">
      <h3>Stats du réseau</h3>
      <div className="stats-container">
        <div className="stat-card">
          <div className="stat-valeur">{nbLignes}</div>
          <div className="stat-label">Lignes</div>
        </div>
        <div className="stat-card">
          <div className="stat-valeur">{totalArrets}</div>
          <div className="stat-label">Arrêts totaux</div>
        </div>
        <div className="stat-card">
          <div className="stat-valeur">Ligne {ligneMaxArrets.numero}</div>
          <div className="stat-label">{ligneMaxArrets.arrets} arrêts (max)</div>
        </div>
      </div>
    </div>
  );
}

export default StatReseau;