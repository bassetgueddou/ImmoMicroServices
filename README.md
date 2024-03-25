# ImmoMicroServices
Real estate management microservice using Flask, enabling property creation, modification, and inquiry. Setup instructions in the README ..

ImmoMicroServices est une application web de gestion immobilière permettant aux utilisateurs de renseigner, consulter, et modifier des biens immobiliers.
# Prérequis
assurez-vous d'avoir installé :
Python 3.8 ou plus récent
pip (gestionnaire de paquets Python)
PostgreSQL
# Configuration de l'environnement
Clonez le dépôt Git :
git clone https://github.com/bassetgueddou/ImmoMicroServices.git puis accédez au dissier du projet "cd ImmoMicroServices" 

Configurez un environnement virtuel (facultatif mais recommandé) :
python -m venv venv 
Activez le :
Sur Windows : venv\Scripts\activate 
Sur Unix ou MacOS/ bash : source venv/bin/activate 

# Installez les dépendances :
pip install -r requirements.txt 
Configurez la base de données PostgreSQL :
Assurez-vous que PostgreSQL est installé et en cours d'exécution sur votre machine.
Créez une base de données pour l'application.

# Modifiez le fichier config.py avec les informations de connexion à votre base de données PostgreSQL.
Exemple de config.py :
class Config: 
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/nom_de_la_base' 
SQLALCHEMY_TRACK_MODIFICATIONS = False JWT_SECRET_KEY = 'votre_cle_secrete_ici' 

# Initialisez la base de données :
flask db upgrade 

# Lancement de l'application
Pour lancer l'application, exécutez la commande suivante dans le répertoire racine du projet :
flask run.py
L'application sera accessible à l'adresse http://localhost:5000/.

# Utilisation de l'API
Une fois l'application lancée, vous y accedez directemet à Swagger pour tester l'API à l'adresse suivante : http://localhost:5000/
Vous y trouverez la documentation des endpoints disponibles ainsi que la possibilité de les tester directement via l'interface.

