FROM gethue/hue:latest

# Passer en mode root pour copier la config
USER root

# Dossier de travail
WORKDIR /usr/share/hue

RUN apt update && apt upgrade

# Copier le fichier hue.ini dans le bon répertoire
COPY conf/hue.ini /usr/share/hue/desktop/conf/hue.ini

# Droits (au besoin)
RUN chown -R hue:hue /usr/share/hue/desktop/conf/hue.ini

# Revenir à l'utilisateur hue pour l'exécution
USER hue
