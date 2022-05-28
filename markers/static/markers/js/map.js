const map = L.map('map').setView([50.083333, 14.416667], 14);
map.invalidateSize()
const photoIcon = L.icon({
    iconUrl: 'static/markers/img/photo-icon.svg',

    iconSize: [30, 30], // size of the icon
    iconAnchor: [15, 15], // point of the icon which will correspond to marker's location
    popupAnchor: [0, -20] // point from which the popup should open relative to the iconAnchor
});

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

const markers = L.markerClusterGroup({
    showCoverageOnHover: false,
    iconCreateFunction: function (cluster) {
        return L.divIcon({
            html: '<div class="cluster">'+ cluster.getChildCount() +'</div>',
            className: 'marker-cluster',
            iconSize: [50, 50],
            iconAnchor: [25, 25]
        });
    },
});

map.addLayer(markers);

let jump_to_marker = null
fetch("/markers/?format=json").then(r => {
    if (r.ok) {
        r.json().then(data => {
            data.forEach(val => {
                let marker = L.marker([val.lat, val.lng], {icon: photoIcon})
                    .bindPopup(val.title)
                    .on('click', function (e) {
                        reset()
                        document.getElementById('title-of-comparison').innerHTML = val["title"]
                        fetch("/markers/"+val.id+"/?format=json").then(r => {
                            r.json().then(details => {
                                document.getElementById('description').innerText = details.description
                                window.top.location.hash = '#bod'+val.id
                                details.marker_images.sort(function(img1, img2) {
                                    return img1.year - img2.year
                                })
                                for(let i = 0; i < details.marker_images.length-1; i++) {
                                    let callback;
                                    if (i === 0) {
                                        callback = function () { // only scroll after first images are loaded
                                            document.getElementById('title-of-comparison').scrollIntoView({
                                                block: 'start',
                                                behavior: 'smooth'
                                            });
                                        }
                                    } else {
                                        callback = null
                                    }
                                    compare(details.marker_images[i], details.marker_images[i+1], callback)
                                }
                            });
                        });
                    })
                markers.addLayer(marker);
                if ('#bod'+val.id === window.top.location.hash) {
                    jump_to_marker = marker
                }
            })
            if (jump_to_marker !== null) {
                jump_to_marker.fire('click')
            }
        });
    }
});
window.dispatchEvent(new Event('resize'))
