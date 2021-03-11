bas_page = '''


<html>
<div id="bas_page">.</div>

<title>AuFilDuBoamp_Lab par Semaine52</title>

<meta name="viewport" content="width=device-width, initial-scale=1">

<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">



<body>

<div class="w3-container">

    <div class="w3-bar w3-white">

        <a href="#haut_page2" alt="Remonter" title="Remonter" class="w3-bar-item w3-button fa fa-arrow-up w3-large">&nbsp; Remonter</a>
  
        
        
    </div>
    
</div>

</body>

</html>

 '''

def afdb_bas_page():
    from IPython.display import display, HTML
    chart = HTML(bas_page)    
    display(chart)

afdb_bas_page()