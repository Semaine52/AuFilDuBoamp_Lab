def afficher_plan_html2(source=None):    
    from IPython.display import display, IFrame, HTML
    
    
    b = None
    c = None
    
    b = display(IFrame(src=source,  width='98%', height='400px'))
    
    
    c = display(HTML(f"""<p><strong>Cliquez sur les cercles contenus dans la figure pour ouvrir et refermer les niveaux.<br>    
                     L'image est zommable.<br><br>
                     <a href={source}> --> Ouvrir ce schéma en plein écran dans un nouvel onglet. </a></strong><br>
                     <em>Cliquez sur « Trust HTML » si le schéma n'apparaît pas de lui-même à l'ouverture du lien.</em></p>
                     """)
               )
    
   
    
    return b, c