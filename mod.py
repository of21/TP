import psutil
import time


# Fonction pour collecter les données CPU et mémoire
def collect_data(interval=5):
    data_log = []  # Pour stocker les données collectées

    while True:
        # Collecte des informations sur l'utilisation du CPU et de la mémoire
        cpu_usage = psutil.cpu_percent(interval=1)
        mem_usage = psutil.virtual_memory().percent
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

        # Ajout des données collectées au journal
        data_log.append({'timestamp': timestamp, 'cpu_usage': cpu_usage, 'mem_usage': mem_usage})

        # Vérification des seuils et envoi de notifications si dépassés
        if cpu_usage > cpu_threshold:
            notify(f"CPU threshold exceeded! Usage: {cpu_usage}%")

        if mem_usage > mem_threshold:
            notify(f"Memory threshold exceeded! Usage: {mem_usage}%")

        # Pause pour respecter l'intervalle de collecte
        time.sleep(interval)

# Fonction pour notifier l'utilisateur (exemple ici avec un print)
def notify(message):
    print(f"Notification: {message}")


# Configurations initiales
cpu_threshold = 10  # Seuil CPU en pourcentage
mem_threshold = 60  # Seuil mémoire en pourcentage

# Début de la collecte de données en temps réel
collect_data(interval=5)

