def afficher_plan_html(source=None):
    import ipywidgets as widgets
    from afdb_lab_scripts.afficher_plan_html2 import afficher_plan_html2
    out = widgets.Output(layout={'border': '3px solid #cccccc', 'max_width':'80%', 'margin':'20px 100px 20px 100px', 'padding':'10px' })
    
    with out:
        afficher_plan_html2(source=source)
        
    display(out)