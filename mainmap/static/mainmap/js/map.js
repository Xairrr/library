var map = L.map("map", { zoomControl:false }).setView(ll, zoom);

L.esri.basemapLayer("Gray").addTo(map);


var geojsonOptions = {
    radius: 20,
    fillColor: "rgb(255,120,120)",
    color: "#000000",
    weight: 5,
    opacity: 0.5,
    fillOpacity: 0.8
};

function onEachFeature(feature, layer) {
    if (feature) {
           layer.bindPopup(feature.properties.name.toString()+'<br>'+
           feature.properties.year.toString()+'<br>'+
           feature.properties.description.toString()+'<br>'+
           "<b>Image: </b><a href='"+feature.properties.image.toString()+"' target=\"_blank\">"+"<br><img src='"+feature.properties.image.toString()+"' width='200' </img></a>"
           );
       }
   };

var pointlayer = L.geoJSON(json,{onEachFeature: onEachFeature,
    pointToLayer: function (feature, latlng) {
        return L.circle(latlng,geojsonOptions);
    }
    });
pointlayer.addTo(map);


var searchSubmitButton = document.getElementById("searchSubmitButton");

searchSubmitButton.onclick = function(){
    center = map.getBounds().getCenter();
    zoom = map.getZoom();
    center_coordinaes = [center.lat, center.lng];
    document.getElementById('latLong').value = center_coordinaes;
    document.getElementById('zoom').value = zoom;


    };
