$(document).ready(function () {

    // Location
    var LocsA = [
        {
            lat: 3.077475,
            lon: 101.493553,
            title: 'Semi-Detached House',
            html: [
                '<h3>Semi-Detached House</h3>',
                '<p>4 amenities nearby</p>'
            ].join('')
        },
        {
            lat: 3.077040,
            lon: 101.485135,
            title: 'A) Kindergarten',
            html: [
                '<h3>Kindergarten</h3>',
                '<p>Tootsie roll toffee sweet brownie icing danish jelly beans cookie.</p>'
            ].join(''),
            icon: 'http://maps.google.com/mapfiles/markerA.png'
        },
        {
            lat: 3.042888,
            lon: 101.449689,
            title: 'B) KTM Komuter',
            html: [
                '<h3>KTM Komuter</h3>',
                '<p>Tootsie roll toffee sweet brownie icing danish jelly beans cookie.</p>'
            ].join(''),
            icon: 'http://maps.google.com/mapfiles/markerB.png'
        },
        {
            lat: 3.069681,
            lon: 101.501859,
            title: 'C) UiTM',
            html: [
                '<h3>Higher Education Institute</h3>',
                '<p>Tootsie roll toffee sweet brownie icing danish jelly beans cookie.</p>'
            ].join(''),
            icon: 'http://maps.google.com/mapfiles/markerC.png'
        },
        {
            lat: 3.087710,
            lon: 101.521520,
            title: 'D) Secondary School',
            html: [
                '<h3>Secondary School</h3>',
                '<p>Tootsie roll toffee sweet brownie icing danish jelly beans cookie.</p>'
            ].join(''),
            icon: 'http://maps.google.com/mapfiles/markerD.png'
        }
    ];

    //Initiating map
     $("#map-link").on('shown.bs.tab', function(){
        new Maplace({
            locations: LocsA,
            map_div: '#gmap-menu',
            controls_type: 'list',
            controls_on_map: true
        }).Load(); 
     })

});