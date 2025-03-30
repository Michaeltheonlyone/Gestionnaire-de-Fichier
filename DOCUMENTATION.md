<h1>Problèmes rencontrés et solutions apportées</h1></br></br></br>

<h2>1. Disposition des icônes</h2></br>
   <h3>Problème1:</h3> Les icônes ne remplissaient pas la ligne avant de passer à la suivante, ce qui rendait l'affichage désorganisé.</br>
   <h3>Solution1 :</h3> Ajustement de la logique d'affichage pour que les icônes occupent toute la largeur avant de passer à la ligne suivante. Cette solution ne s'applique pas en plein ecran, le probleme persiste toujours</br>
   <h3>Problème2:</h3>  Les elements/icones se surperposent parfois entre eux</br>
   <h3>Solution2: </h3> Aucune solution trouvee</br>

<h2> Affichage de la fenêtre (Fullscreen et boutons de contrôle)</h2></br>
  <h3>Problème</h3> : L'application était initialement en plein écran sans les boutons classiques (fermer, réduire, agrandir).</br>
  <h3>Solution </h3>: Modification pour adopter une apparence similaire à l'explorateur de fichiers Windows, avec les boutons fonctionnels.</br>

<h2> Problèmes liés à la barre latérale gauche (LHS) </h2></br>
  <h3>Problème:</h3> Cliquer sur "Ordinateur" ou "Favoris" entraînait des erreurs (chemins non trouvés, fonctions non définies).</br>
  <h3>Solution:</h3>  Correction des fonctions show_favorites() et load_folders() pour assurer un chargement correct des dossiers et disques.</br>

<h2> Recherche de fichiers</h2></br>
  <h3>Problème:</h3> Le bouton "Rechercher" ne fonctionnait pas et affichait une erreur (search_files() not defined).</br>
  <h3>Solution :</h3> Ajout et intégration de la fonction search_files().</br>

<h2> Création de dossiers</h2></br>
  <h3>Problème:</h3> Le bouton "Nouveau Dossier" causait une erreur (create_new_folder not defined).</br>
  <h3>Solution:</h3>  Définition et intégration de la fonction create_new_folder().</br>

<h2>Fonctionnalité des clics</h2>
   <h3>Problème</h3> : Le clic pour ouvrir des fichiers ou des dossiers ne fonctionne pas toujours. Parfois, il répond correctement, mais la majorité du temps, il ne fait rien. Nous n'avons pas encore trouvé la cause exacte. De meme pour les clics droits pour acceder au menu contextuel</br>
   <h3>Solution</h3> : Aucune solution définitive pour l'instant, il faudra approfondir le problème. Soyez patient et cliquez a plusieurs reprises</br>

<h2> Fatigue et paresse extrême </h2></br>
    <h3>Problème:</h3>  La fatigue et la paresse ont ralenti l'avancement du projet, impactant la concentration et la rapidité de résolution des bugs.</br>
    <h3>Solution:</h3>  Aucun remède trouvé, à part des pauses café et une bonne dose de motivation. </br>
