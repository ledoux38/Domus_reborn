// Gestionnaire d'événements pour le bouton Ping
function handlePing() {
    const sensorGroupIp = document.getElementById('sensorGroupIp').value;
    const sensorGroupPort = document.getElementById('sensorGroupPort').value;
    const sensorGroupKey = document.getElementById('sensorGroupKey').value;

    // Afficher la modal avec l'état 'en cours'
    updateModalStatus('pending');
    document.getElementById('connectionModal').style.display = 'block';

    pingSensor(sensorGroupIp, sensorGroupPort, sensorGroupKey)
        .then(handlePingResponse)
        .catch(() => {
            updateModalStatus('failure');
            setTimeout(closeModal, 3000); // Fermer la modal après 3 secondes en cas d'échec
        });
}


// Envoi de la requête de ping
function pingSensor(ip, port, key) {
    return fetch('/sensor_data/ping', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({ sensorGroupIp: ip, sensorGroupPort: port,  sensorGroupKey:key})
    }).then(response => response.json());
}

// Gestion de la réponse du ping
function handlePingResponse(data) {
    if (data.success) {
        updateModalStatus('success');
    } else {
        updateModalStatus('failure');
    }
    setTimeout(closeModal, 3000); // Fermer la modal après 3 secondes, que ce soit un succès ou un échec
}

// Ajout de l'écouteur d'événements
document.getElementById('pingButton').addEventListener('click', handlePing);


function getCookie(name) {
    // Fonction pour récupérer le CSRF token
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Fonction pour fermer la modal
function closeModal() {
    document.getElementById('connectionModal').style.display = 'none';
}

// Ajout de l'écouteur d'événements
document.getElementById('pingButton').addEventListener('click', handlePing);


    function updateModalStatus(status) {
        const title = document.getElementById('modalTitle');
        const message = document.getElementById('modalMessage');

        switch(status) {
            case 'success':
                title.innerHTML = "Connexion réussie!";
                title.style.color = "#00ff00"; // Vert
                message.innerHTML = "La connexion au capteur a été établie.";
                break;
            case 'failure':
                title.innerHTML = "Connexion refusée!";
                title.style.color = "#ff0000"; // Rouge
                message.innerHTML = "Échec de la connexion au capteur.";
                break;
            case 'pending':
                title.innerHTML = "Connexion en cours...";
                title.style.color = "#ffff00"; // Jaune
                message.innerHTML = "Veuillez patienter pendant que nous établissons la connexion.";
                break;
        }
    }