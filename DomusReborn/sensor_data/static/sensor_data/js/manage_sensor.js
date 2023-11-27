    document.getElementById('pingButton').addEventListener('click', function() {
        updateModalStatus('pending'); // Mettre à jour l'état de la modal à 'en cours'
        document.getElementById('connectionModal').style.display = 'block'; // Afficher la modal
        // Ici, ajoutez le code pour effectuer le ping et mettre à jour la modal en conséquence
    });

    // Assurez-vous que ce code est bien placé et que l'élément avec l'id 'closeModal' existe dans votre HTML si vous souhaitez l'utiliser
    // document.getElementById('closeModal').addEventListener('click', function() {
    //     document.getElementById('connectionModal').style.display = 'none';
    // });

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