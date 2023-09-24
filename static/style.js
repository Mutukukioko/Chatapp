 // JavaScript function to remove flash cards after a certain time
 document.addEventListener('DOMContentLoaded', function () {
    var flashContainer = document.getElementById('flash-container');
    setTimeout(function () {
        var flashCards = document.querySelectorAll('.flash-card');
        flashCards.forEach(function (card) {
            flashContainer.removeChild(card);
        });
    }, 5000); // Cards disappear after 5 seconds (adjust as needed)
});