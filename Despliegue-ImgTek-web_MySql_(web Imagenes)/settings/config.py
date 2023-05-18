import os


# La variable “SECRET_KEY” definida como ajuste único es una parte  importante de las aplicaciones 
# de Flask. Flask y algunas de sus extensiones utilizan el valor de la variable como llave criptográfica,
# útil para generar firmas y tokens. 
# 
# La extension Flask-WTF la usa para proteger los formularios de
# ataques de hackers como CSRF (acrónimo de Cross-Site Request Forgery que significa Falsificación 
# de solicitudes entre sitios). Como su nombre lo dice, SECRET_KEY (en español, llave secreta) debe 
# ser secreta, ya que la fuerza de los tokens y firmas generadas dependen de que nadie fuera del
#  equipo de desarrollo la sepa.

class configuracion(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'contraseña'

# El valor de la clave secreta es definido como una expresión con dos términos, 
# unidos por un or. El primer termino busca el valor en una variable de entorno, 
# llamada también SECRET_KEY. El segundo termino es un string normal. 
# Este patrón es muy utilizado en la definición de ajustes. 
# La idea es que el valor de la variable de entorno tenga mayor precedencia, 
# pero si no está definida, entonces el valor del string es utilizado en su lugar

# Hay varios formatos para que la aplicación especifique sus ajustes. 
# La solución mas básica, es definirlos en app.config