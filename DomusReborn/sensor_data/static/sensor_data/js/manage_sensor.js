document.getElementById('pingButton').addEventListener('click', function() {
    const sensorIp = document.getElementById('sensorIp').value;
    const sensorPort = document.getElementById('sensorPort').value;

    // Afficher la modal avec l'état 'en cours'
    updateModalStatus('pending');
    document.getElementById('connectionModal').style.display = 'block';

    fetch('/path_to_ping_view', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'), // Assurez-vous de gérer le CSRF token
        },
        body: JSON.stringify({ sensorIp: sensorIp, sensorPort: sensorPort })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            updateModalStatus('success');
            setTimeout(function() {
                document.getElementById('connectionModal').style.display = 'none';
            }, 3000);
        } else {
            updateModalStatus('failure');
        }
    })
    .catch(error => {
        updateModalStatus('failure');
    });
});

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