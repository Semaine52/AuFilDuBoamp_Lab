qr_page = '''


<html>

<title>AuFilDuBoamp_Lab par Semaine52, les Questions-Réponses</title>

<meta name="viewport" content="width=device-width, initial-scale=1">

<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">



<body>

<div class="w3-container">
<p style='font-size:30px;'>BOAMP 2021 - DataMining </p>
<p style='font-size:14px;margin-top:-40px'>(Tags --> 2021)</p>
   <div><img class="w3-animate-right" src="images/QetR_SVG2.svg" alt="AuFilDuBoamp_Lab: les Questions-Réponses" title="AuFilDuBoamp_Lab: les Questions-Réponses" style="width:25%; heigth:auto">
   </div>
</div>
        
        
    </div>
    
</div>

</body>

</html>

 '''

def afdb_qr_page():
    from IPython.display import display, HTML
    chart = HTML(qr_page)    
    display(chart)

afdb_qr_page()