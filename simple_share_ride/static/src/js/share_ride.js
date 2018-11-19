function initMap() {
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: {
            lat: 25.084,
            lng: 121.562,
        }
    });
    directionsDisplay.setMap(map);

    var onChangeHandler = function () {
        calculateAndDisplayRoute(directionsService, directionsDisplay);
    };
    document.getElementById('start').addEventListener('change', onChangeHandler);
    document.getElementById('end').addEventListener('change', onChangeHandler);
}

function calculateAndDisplayRoute(directionsService, directionsDisplay) {
    directionsService.route({
        origin: {
            lat: parseFloat($('#start option:selected').data('lat')),
            lng: parseFloat($('#start option:selected').data('lng')),
        },
        destination: {
            lat: parseFloat($('#end option:selected').data('lat')),
            lng: parseFloat($('#end option:selected').data('lng')),
        },
        // origin: document.getElementById('start').value,
        // destination: document.getElementById('end').value,
        travelMode: 'DRIVING'
    }, function (response, status) {
        if (status === 'OK') {
            directionsDisplay.setDirections(response);
        } else {
            window.alert('Directions request failed due to ' + status);
        }
    });
}