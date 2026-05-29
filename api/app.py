import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Charger les données depuis le fichier JSON
with open("lignes_ddd.json", "r", encoding="utf-8") as f:
    lignes = json.load(f)


# Route d'accueil
@app.route("/")
def accueil():
    return jsonify({
        "message": "Bienvenue sur l’API SenTransport !",
        "endpoints": [
            "/lignes",
            "/lignes/<id>",
            "/arrets",
            "/stats",
            "/lignes/recherche?q=motcle"
        ]
    })


# Retourner toutes les lignes
@app.route("/lignes")
def get_lignes():
    return jsonify(lignes)


# Retourner une ligne par son ID
@app.route("/lignes/<int:ligne_id>")
def get_ligne(ligne_id):

    ligne = next(
        (l for l in lignes if l["id"] == ligne_id),
        None
    )

    if ligne is None:
        return jsonify({
            "erreur": "Ligne non trouvée"
        }), 404

    return jsonify(ligne)



with open("arrets.json", "r") as f:
    arrets = json.load(f)
@app.route("/arrets")
def get_arrets():
    return jsonify(arrets)

# Exercice 2 : Statistiques
@app.route("/stats")
def get_stats():

    nombre_lignes = len(lignes)

    total_arrets = sum(
        len(ligne["listeArrets"])
        for ligne in lignes
    )

    moyenne_arrets = (
        total_arrets / nombre_lignes
        if nombre_lignes > 0
        else 0
    )

    return jsonify({
        "nombre_lignes": nombre_lignes,
        "total_arrets": total_arrets,
        "moyenne_arrets": round(moyenne_arrets, 2)
    })


# Exercice 3 : Recherche
@app.route("/lignes/recherche")
def rechercher_ligne():

    q = request.args.get("q", "").lower()

    resultat = []

    for ligne in lignes:

        numero = ligne["numero"].lower()
        depart = ligne["depart"].lower()
        arrivee = ligne["arrivee"].lower()

        if (
            q in numero
            or q in depart
            or q in arrivee
        ):
            resultat.append(ligne)

    return jsonify(resultat)


# Lancement du serveur
if __name__ == "__main__":
    app.run(debug=True, port=5000)