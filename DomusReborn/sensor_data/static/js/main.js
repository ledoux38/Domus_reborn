function toggleDetails(element) {
    var details = element.querySelector('.sensor-details');
    if (details.style.display === 'none') {
        details.style.display = 'block';
    } else {
        details.style.display = 'none';
    }
}