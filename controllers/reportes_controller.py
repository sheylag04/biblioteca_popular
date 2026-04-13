from models.reportes_model import prestamos_activos,prestamos_vencidos,materiales_mas_prestados

def pres_activos():
    return prestamos_activos()

def pres_vencidos():
    return prestamos_vencidos()

def mate_mas_prestados():
    return materiales_mas_prestados()