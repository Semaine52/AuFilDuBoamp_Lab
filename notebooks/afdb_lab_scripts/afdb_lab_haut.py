##### string html

haut_page = '''

<!DOCTYPE html>

<html>

<title>AuFilDuBoamp_Lab par Semaine52</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<script src='https://kit.fontawesome.com/a076d05399.js'></script>


<body>

<div class="w3-container">
   <div class="w3-padding  w3-white w3-small">
  
     <a href="https://github.com/Semaine52/AuFilDuBoamp_Lab" title="AuFilDuBoamp_Lab sur GitHub" alt="AuFilDuBoamp_Lab sur GitHub" class="w3-bar-item w3-button fas fa-share-square w3-small w3-white">&nbsp; AuFilDuBoamp_Lab sur GitHub</a>
     
     <a href="https://twitter.com/AuFilDuBoamp" title="AuFilDuBoamp sur Twitter" alt="AuFilDuBoamp sur Twitter" class="w3-bar-item w3-button fas fa-share-square w3-small w3-white">&nbsp; sur Twitter</a>
     
     <a href="https://www.data.gouv.fr/fr/organizations/aufilduboamp-1/" title="AuFilDuBoamp sur DataGouv.fr" alt="AuFilDuBoamp sur DataGouv.fr" class="w3-bar-item w3-button fas fa-share-square w3-small  w3-white">&nbsp; sur DataGouv.fr</a>
     
          <a href="https://mybinder.org/v2/gh/Semaine52/AuFilDuBoamp_Lab/master?urlpath=lab/tree/notebooks/_Sommaire.ipynb" title="AuFilDuBoamp_Lab sur Binder" alt="AuFilDuBoamp_Lab sur Binder" class="w3-bar-item w3-button fas fa-share-square w3-small  w3-white">&nbsp; sur Binder</a>
          
          <a href="https://teamopendata.org/u/semaine52_jmf/summary" title="Jean-Marie Falvet sur TeamOpenData" alt="Jean-Marie Falvet sur TeamOpenData" class="w3-bar-item w3-button fas fa-share-square w3-small  w3-white">&nbsp; chez TeamOpenData</a>
          
          
     
       
         <a href="https://www.data.gouv.fr/fr/datasets/boamp/" title="Le BOAMP sur DataGouv.fr" alt="Le BOAMP sur DataGouv.fr" class="w3-bar-item w3-button fas fa-share-square w3-small w3-white">&nbsp; Le BOAMP sur DataGouv.fr</a>
     
     <a href="https://www.boamp.fr/" title="BOAMP.fr" alt="BOAMP.fr"class="w3-bar-item w3-button fas fa-share-square w3-small  w3-white">BOAMP.fr</a>
     
     <a href="https://www.legifrance.gouv.fr/affichCode.do?cidTexte=LEGITEXT000037701019" title="Accueil" alt="Accueil"class="w3-bar-item w3-button fas fa-share-square w3-small  w3-white">&nbsp; Code de la commande publique (Légifrance)</a>  
    
   </div> 
      
 </div>

 <div class="w3-container">
   <div><img class="w3-animate-right" src="design/AFDB_DOTS.svg" alt="AuFilDuBoamp_Lab" title="AuFilDuBoamp_Lab" style="width:40%"></div>

   <div class="w3-padding w3-xlarge w3-white"> 
     
       
        
     <a href="_Sommaire.ipynb" alt="Sommaire général" title="Sommaire général" class="w3-bar-item w3-button fa fa-list w3-large w3-amber">&nbsp; Lien vers le Sommaire général</a>  
     <a href="https://mybinder.org/v2/gh/Semaine52/AuFilDuBoamp_Lab/master?urlpath=lab/tree/notebooks/_Sommaire.ipynb" alt="Lancer Binder" title="Lancer Binder" class="w3-bar-item w3-button fa fa-arrow-right w3-large w3-teal">&nbsp; Lancer Binder</a>  
     <p style="font-size:16px; margin-top:5px">N'oubliez pas <strong>« Run All Cells »</strong> du menu <strong>« Run »</strong> pour activer les pages une fois sur Binder.</p>
  </div>
  
 </div>

</body>

</html> 

 '''

##### Exécution et affichage de la string

def afdb_haut_page():
    from IPython.display import display, HTML
    chart = HTML(haut_page)    
    display(chart)

afdb_haut_page()