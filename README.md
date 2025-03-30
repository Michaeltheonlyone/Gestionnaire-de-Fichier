<h1>Membres Du Groupe:</h1><br/>
1- ELEKWA Michael(Responsable du groupe)<br/>
2-HOUENOU Fabrice(Adjoint du responsable)<br/>
3-HOUNNOUGBO Stephane<br/>
4-KAKPO Mirabelle<br/>
5-KOTY K.Igor Zaky<br/>

<h1>Explorateur de Fichiers</h1> <br/>

<h2>Description du projet</h2><br/>

Ce projet est un explorateur de fichiers développé en Python avec Tkinter. Il permet aux utilisateurs de naviguer dans leurs fichiers et dossiers, d'ouvrir des fichiers et de réaliser plusieurs opérations comme le marquage en favoris, la recherche et l'affichage des détails des fichiers.<br/>

<h3>Fonctionnalités principales</h3>
Veuillez consulter le dossier "SCREENSHOTS" pour acceder aux screenshots associes a chaque numero

1-Navigation : Explorer les fichiers et dossiers en double-cliquant dessus.<br/> 
![SCREENSHOT](./SCREENSHOTS/1NAVIGATION.png)<br/>
2-Barre de chemin : Modifier manuellement le chemin pour accéder à un dossier.<br/>
![SCREENSHOT](./SCREENSHOTS/2BARREDECHEMININTERAGIBLE.png)<br/>
3-Affichage dynamique : Les fichiers et dossiers s'affichent avec leurs icônes respectives.<br/>
![SCREENSHOT](./SCREENSHOTS/3ICONES.png)<br/>
DES ICONES ONT ETE DEFINIS POUR LES IMAGES, DOSSIERS, FICHIERS TXT ET PDF TOUT AUTRE ELEMENT SERA REPRESENTE AVEC L'ICONE AYANT LE POINT D'INTERROGATION <br/>
4-Panneau latéral (LHS) : Affiche les catégories suivantes :<br/>
  ![SCREENSHOT](./SCREENSHOTS/4PANNNEAULATERAL.png)<br/>
  Local Disk : Accès au disque local.<br/>
  Computer : Affiche tous les disques connectés.<br/>
  Recent : Affiche les fichiers récemment ouverts.<br/>
  Tags : Fonctionnalité non définie.<br/>
  Nouveau dossier:creation de nouveau dossier<br/>
  Actualiser: rafrachir<br/>
  Filtrer: Afficher les elements en fontion d'un critere d'extension entree par l'utilisateur<br/>
  ![SCREENSHOT](./SCREENSHOTS/EXTENSION.png)<br/>
5-Menu contextuel (clic droit) : Permet d’ouvrir, renommer et supprimer un fichier ou un dossier.<br/>
 ![SCREENSHOT](./SCREENSHOTS/5MENUCONTEXTUEL.png)<br/>
6-Marquage en favoris : Ajout/suppression des fichiers et dossiers favoris.<br/>
    1-L'OPTION D'AJOUTER AU FAVORI APPARAIT DANS LE MENU CONTEXTUEL<br/>
     ![SCREENSHOT](./SCREENSHOTS/FAVORI1.png)<br/>
    2-SI VOUS N'AJOUTEZ PAS D'ELEMENT A LA LISTE DES FAVORIS UN MESSAGE D'ERREUR S'AFFICHE<br/>
    ![SCREENSHOT](./SCREENSHOTS/FAVORI2.png)<br/>
    3-Une fois un element est ajoute au favori un message d'alerte s'affiche<br/>
    ![SCREENSHOT](./SCREENSHOTS/FAVORI3.png)<br/>
7-Recherche : Trouver rapidement un fichier ou un dossier.<br/>
 ![SCREENSHOT](./SCREENSHOTS/7RECHERCHER.png)<br/>
8-Détails des fichiers : Affichage de la taille, date de création et autres métadonnées.<br/>
     1-L'OPTION D'AFFICHER LES DETAILS APPARAIT DANS LE MENU CONTEXTUEL<br/>
     ![SCREENSHOT](./SCREENSHOTS/DETAIL1.png)<br/>
     2-DETAILS DU FICHIER "FIFA 18"<br/>
     ![SCREENSHOT](./SCREENSHOTS/DETAIL2.png)<br/>
9-Gestion des erreurs : Messages d’erreur en cas d’accès refusé ou de problème d’ouverture.<br/>
     EXEMPLE: On n'a rien implemente pour l'option "TAG" du panneau laterale alors un message d'erreur s'afffiche<br/>
     ![SCREENSHOT](./SCREENSHOTS/9MESSAGED'ERREUR.png)<br/>

Installation et utilisation<br/>
Cloner le dépôt :<br/>
 git clone  https://github.com/Michaeltheonlyone/Gestionnaire-de-Fichier.git<br/>

 cd Gestionnaire-de-Fichier<br/>

Installer les dépendances :<br/>
 pip install pillow<br/>

Lancer l’application :<br/>
 python main.py<br/>
