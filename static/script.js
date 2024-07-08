document.addEventListener("DOMContentLoaded", function() {
    // Récupérer le formulaire et les éléments de formulaire
    const form = document.querySelector('form');
    const startupUrlInput = document.getElementById('startup_url');
    const errorContainer = document.getElementById('error-container');
    
    // Ajouter un écouteur d'événement sur la soumission du formulaire
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Empêcher la soumission par défaut du formulaire
        
        // Valider l'URL de la startup
        const startupUrl = startupUrlInput.value.trim();
        if (!isValidUrl(startupUrl)) {
            showError('Veuillez entrer une URL valide pour la startup.');
            return;
        }
        
        // Soumettre le formulaire si l'URL est valide
        form.submit();
    });
    
    // Fonction pour valider une URL
    function isValidUrl(url) {
        // Vous pouvez implémenter une logique de validation plus avancée ici si nécessaire
        return url.startsWith('http://') || url.startsWith('https://');
    }
    
    // Fonction pour afficher un message d'erreur
    function showError(message) {
        errorContainer.innerText = message;
        errorContainer.style.display = 'block';
    }
});
