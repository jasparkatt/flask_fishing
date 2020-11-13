//create a leaflet map object
var mymap;
var lyrSatellite; //open street maps
var lyrRelief; //style layer from mapbox
var lyrCreek; //style layer from mapbox
var lyrSpotX; //geojson point data
var lyrLabels; //style layer from mapbox
var mrkCurrentLocation; //locate user
var ctlLayers;
var ctlBasemaps;
var ctlOverlays;

function myFunc() {
    return place
}

//get public access token
L.mapbox.accessToken = appConfig.access_token;
//create map and overlays
$(document).ready(function() {
    mymap = L.map('map', {
        center:myFunc(),
        zoom:7.5,
        zoomControl:false,
        attributionControl:false
    });
    lyrRelief = L.mapbox.styleLayer('mapbox://styles/budsuttree/cjxxen8yq5twc1cqaapjf1my9');
    lyrCreek = L.mapbox.styleLayer('mapbox://styles/budsuttree/cjxw63sdr03gj1cmy6y89ul89');
    lyrLabels = L.mapbox.styleLayer('mapbox://styles/budsuttree/cjxzb1lq71k3y1cob7ha24xw1');
    lyrSatellite = L.mapbox.styleLayer('mapbox://styles/mapbox/satellite-streets-v10');

    $("#btnLocate").click(function() {
        mymap.locate();
    });
    //do something with this below
    $("btnTrout").click()


    mymap.addLayer(lyrSatellite);

    objBasemaps = {
        "Hillshade":lyrRelief,
        "Satellite":lyrSatellite
    };

    objOverlays = {
        "Trout Streams":lyrCreek,
        "Labels":lyrLabels
    };

    ctlLayers = L.control.layers(objBasemaps, objOverlays).addTo(mymap); //{position:'bottomright'}

    mymap.on('locationfound', function(e) {
        console.log(e);
        if (mrkCurrentLocation) {
            mrkCurrentLocation.remove();
        }
        mrkCurrentLocation = L.circle(e.latlng, {radius:e.accuracy/2}).addTo(mymap);
        mymap.setView(e.latlng, 14);
    });

    mymap.on('locationerror', function(e) {
        console.log(e);
        alert("Location was not found");
    });

})

  //  https://api.mapbox.com/styles/v1/YOUR_USERNAME/YOUR_STYLE_ID/tiles/256/{z}/{x}/{y}?access_token={{'ACCESS_KEY'}}
