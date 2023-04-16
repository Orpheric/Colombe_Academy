#--------------------------------------------------------------------------------------#
#                     DASHBOARD DATA & IA COLOMBE ACADEMY TECHNOLOGIE                  #
#--------------------------------------------------------------------------------------#

# importer les librairies.
import streamlit as st
import streamlit_authenticator as stauth
       
import yaml
from yaml.loader import SafeLoader


# occuper tous l'ecran.
st.set_page_config(layout="wide")

# l'image à afficher.
st.image("cat.jfif", width=200)

    
# afficher le titre.
st.title("Licence Data Science & IA dashboard")


with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
with st.expander("Se connecter"):
    name, authentication_status, username = authenticator.login('Login', 'main')
    if st.session_state["authentication_status"] == False:
      st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] == None:
     st.warning('Please enter your username and password')
    
if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{st.session_state["name"]}*')


    
# trois colonnes pour la progression et les modules
progression, niveau, module, professeur = st.columns(4)
#---------------------------------------------------------------------------------------------#
#                                    Licence 3                                                 #
#---------------------------------------------------------------------------------------------#
# le niveau de la filiere.

if st.session_state["authentication_status"]:
    progress = False
else:
    progress = True
with niveau:
    select_niveau = st.selectbox(
        "Merci de selectionner le niveau d'étude",
        ("Master 1 Data & IA","Master 2 Data & IA", "Licence Data & IA"),)
    if select_niveau == "Licence Data & IA":
        with module:
            select_module = st.selectbox(
                "Merci de selectionner le module",
                ("Introduction Python","Statistique Descriptive", "Algorithme"),)
            if  select_module == "Introduction Python":
                with progression:
                    progression_percentage = st.slider(
                        "Estimation de la progression du cours.",
                        min_value = 0.0,
                        max_value = 100.0,
                        value = 90.0,
                        disabled = progress,
                        format = "%d%%")
                with st.expander("Compte rendu du module selectionné"):
                  st.markdown('''
                        - objectifs du modules identifiés.
                        - installation de pycharme
                        - base de python(variales, boucles, fonctions,condtions etc)
                        - programme arithmetique (soustraction, addition, multiplication et division)
                        - fonction avancéé
                        - programmation orienté object
                        - creer un questionnaire
                        - programme qui evalue la note d'un utlisateur
                        - programme qui permet de trouver le conducteur le plus proche
                        - Python et les bases de données
                        - connexion base de données depuis python (creation de base de données, de tables,insertion des données et requetes etc)
                        -
                        ''')
                with professeur:
                    nom_professeur = st.selectbox(
                        "Le professeur chargé du cours",
                        ("Chamsedine AIDARA",""),disabled = progress,)
                        
            if  select_module == "Statistique Descriptive":
                with progression:
                    progression_percentage = st.slider(
                        "Estimation de la progression du cours.",
                        min_value = 0.0,
                        max_value = 100.0,
                        value = 60.0,
                        disabled = progress,
                        format = "%d%%")
                with st.expander("Compte rendu du module selectionné"):
                  st.markdown('''
                        - Manipulation des données.
                        - Representation graphique des données
                        - Les caracteristiques de position et de dispersion
                        - distribution statistiques à deux caracteres
                        ''')  
                with professeur:
                    nom_professeur = st.selectbox(
                        "Le professeur chargé du cours",
                        ("Wahab DIOP", " "),disabled = progress,)
                    
            if  select_module == "Algorithme":
                with progression:
                    progression_percentage = st.slider(
                        "Estimation de la progression du cours.",
                        min_value = 0.0,
                        max_value = 100.0,
                        value = 50.0,
                        disabled = progress,
                        format = "%d%%")
                with st.expander("Compte rendu du module selectionné"):
                  st.markdown('''
                        - Prise de contact
                        - Structure des données
                        - Les Pointeurs
                        - Les Modules
                        - Liste Mono directionnelle
                        - Decouvert des librairies.
                        ''') 
                with professeur:
                    nom_professeur = st.selectbox(
                        "Le professeur chargé du cours",
                        ("Serge Alexandre Boissy", " "),disabled = progress,)
  
    
#---------------------------------------------------------------------------------------------#
#                                   DIVERS                                                    #
#---------------------------------------------------------------------------------------------#
                    
# presentation dashboard.
st.sidebar.header('A Propos du Dashboard')
st.sidebar.markdown('''
                    Ce dashboard a été realisé dans le but d'avoir un meilleur suivi des differents modules 
                    effectués par les enseignants. Il permet d' avoir une estimation sur chaque module. Chaque cours sera ponctué par 
                    un compte rendu. Le dashboard est mis à jours chaque fin de semaine.
                    ''')

st.sidebar.image("image-ia.jfif")

 

                    
# A propos de moi.
if st.checkbox("By"):
        st.caption("Aidara Chamsedine")
        st.caption("Consultant Chargé du programme Data Science & IA à CAT")
        st.caption("Mentor OpenClassrooms sur les Parcours Data Analyst & Data Scientist")
        st.caption("Supervisor Data Scientist Expresso Télécom")
        st.caption("c.aidara@cat.sn")
        st.caption("aidarachamsedine10@gmail.com")
        
