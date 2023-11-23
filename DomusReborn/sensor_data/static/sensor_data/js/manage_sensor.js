document.getElementById('ping').addEventListener('click', function() {
    showModal('en cours');
    // Logique de connexion...
});

function showModal(status) {
    var banner = document.getElementById('notificationBanner');
    var background = document.getElementById('modalBackground');
    var message = document.getElementById('notificationMessage');

    switch(status) {
        case 'en cours':
            banner.className = 'notification-banner connexion-en-cours';
            message.textContent = 'Connexion en cours ...';
            break;
        case 'réussi':
            banner.className = 'notification-banner connexion-reussi';
            message.textContent = 'Connexion réussi';
            break;
        case 'échec':
            banner.className = 'notification-banner echec-connexion';
            message.textContent = 'Echec de la connexion';
            break;
    }

    banner.style.display = 'block';
    background.style.display = 'block';
}

// Pour fermer le modal après un certain temps
setTimeout(() => {
    document.getElementById('notificationBanner').style.display = 'none';
    document.getElementById('modalBackground').style.display = 'none';
}, 5000); // 5 secondes
