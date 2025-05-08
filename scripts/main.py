import requests
import pandas as pd

def get_nombre_evenements():
    url = "https://api.archives-ouvertes.fr/search/?q=language_s:fr+AND+docType_s:COMM&rows=0&wt=json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data['response']['numFound']

def sauvegarder_csv(nombre, chemin_fichier="nombre_evenements_francophones.csv"):
    df = pd.DataFrame([{
        "filtre": "language_s:fr AND docType_s:COMM",
        "nombre_evenements": nombre
    }])
    df.to_csv(chemin_fichier, index=False)
    print(f"✔️ Données enregistrées dans {chemin_fichier}")

def main():
    print("📡 Requête en cours vers l’API HAL...")
    nombre = get_nombre_evenements()
    print(f"✅ Nombre total d’événements scientifiques francophones : {nombre}")
    sauvegarder_csv(nombre)

if __name__ == "__main__":
    main()
