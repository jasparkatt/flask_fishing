//add some stuff...use any of the other maps as a template
//then create a list of the center[x,y] param for the mymap creation
//zoom to depends on page view...maybe use {{title}} jinja tag
//to handle that logic by title name e.g. <title>Central sands<title/> find that example that shows
//that title trick. 

//create a leaflet map object
var mymap;
var lyrSatellite; //open street maps
var lyrRelief; //style layer from mapbox
var lyrCreek; //style layer from mapbox
var lyrLabels; //style layer from mapbox
var ctlLayers;
var ctlBasemaps;
var ctlOverlays;



//get public access token
L.mapbox.accessToken = appConfig.access_token;

//create map and overlays
$(document).ready(function() {
    $('.header').height($(window).height());
    lyrRelief = L.mapbox.styleLayer('mapbox://styles/budsuttree/cjxxen8yq5twc1cqaapjf1my9');
    lyrCreek = L.mapbox.styleLayer('mapbox://styles/budsuttree/cjxw63sdr03gj1cmy6y89ul89');
    lyrLabels = L.mapbox.styleLayer('mapbox://styles/budsuttree/cjxzb1lq71k3y1cob7ha24xw1');
    lyrSatellite = L.mapbox.styleLayer('mapbox://styles/mapbox/satellite-streets-v10');
    lyrSpotx = L.geoJson(geo_json, {
        pointToLayer: L.mapbox.marker.style,
    });

    mymap = L.map('map', {
        center: place,
        zoom:zoom,
        zoomControl:false,
        attributionControl:false,
        tileSize: 512,
        zoomOffset: -1,
        layers: [lyrLabels,lyrSpotx]
    });

    mymap.addLayer(lyrRelief);

    objBasemaps = {
        "Hillshade":lyrRelief,
        "Satellite":lyrSatellite
    };

    objOverlays = {
        "Trout Streams":lyrCreek,
        "Labels":lyrLabels,
        "Fishin' Holes":lyrSpotx
    };

    ctlLayers = L.control.layers(objBasemaps, objOverlays).addTo(mymap); //{position:'bottomright'}

    /* for (var i = 0; i < marks.length; i++) {
        marker = new L.marker([marks[i][0],marks[i][1]])
            .addTo(mymap);
    } */



 /*    for (var i = 0; i < marks.length; i++) {
        circle = new L.circle([marks[i][0],marks[i][1]], {
        color: '#330033e3',
        fillColor: '#fcfcfc',
        fillOpacity: 0.35,
        radius: 600
        }).addTo(mymap).bindPopup('ju');
    } */
})