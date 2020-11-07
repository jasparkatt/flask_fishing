//create a leaflet map object
var mymap;
var lyrSatellite; //open street maps
var lyrRelief; //style layer from mapbox
var lyrCreek; //style layer from mapbox
var lyrSpotX; //geojson point data
var lyrLabels; //style layer from mapbox
var ctlLayers;
var ctlBasemaps;
var ctlOverlays;

//get public access token
//L.mapbox.accessToken ='{{access_token}}';
L.mapbox.accessToken=''
//create map and overlays
$(document).ready(function() {
    lyrRelief = L.mapbox.styleLayer('mapbox://styles/budsuttree/cjxxen8yq5twc1cqaapjf1my9');
    lyrCreek = L.mapbox.styleLayer('mapbox://styles/budsuttree/cjxw63sdr03gj1cmy6y89ul89');
    lyrLabels = L.mapbox.styleLayer('mapbox://styles/budsuttree/cjxzb1lq71k3y1cob7ha24xw1');
    lyrSatellite = L.mapbox.styleLayer('mapbox://styles/mapbox/satellite-streets-v10');  
    
    mymap = L.map('map', {
        center:[43.602222, -90.780278],
        zoom:11,
        zoomControl:false,
        attributionControl:false,
        layers: [lyrCreek,lyrLabels]
    });

    mymap.addLayer(lyrRelief);

    objBasemaps = {
        "Hillshade":lyrRelief,
        "Satellite":lyrSatellite
    };

    objOverlays = {
        "Trout Streams":lyrCreek,
        "Labels":lyrLabels
    };

    ctlLayers = L.control.layers(objBasemaps, objOverlays).addTo(mymap); //{position:'bottomright'}
})

  //  https://api.mapbox.com/styles/v1/YOUR_USERNAME/YOUR_STYLE_ID/tiles/256/{z}/{x}/{y}?access_token={{'ACCESS_KEY'}}
