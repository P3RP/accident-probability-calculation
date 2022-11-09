function getLocation() {
    if (navigator.geolocation) { // GPS를 지원하면
        navigator.geolocation.getCurrentPosition(function(position) {
            document.getElementById('gps-lat').value = position.coords.latitude;
            document.getElementById('gps-lng').value = position.coords.longitude;
            document.getElementById('gps-t').value = position.timestamp;
        }, function(error) {
          console.error(error);
        }, {
          enableHighAccuracy: false,
          maximumAge: 0,
          timeout: Infinity
        });
    } else {
        alert('GPS를 지원하지 않습니다');
    }
}

// 주기적 GPS 실행
setInterval(function(){
    getLocation();

    axios.post('http://localhost:5000/gps', {
        lat: document.getElementById('gps-lat').value,
        lng: document.getElementById('gps-lng').value,
        timestamp: document.getElementById('gps-t').value
    }).then((result) => {
        console.log('GPS OK');
    }).catch(() => {
        console.log('GPS NOT OK');
    })

}, 2000);


// 주기적 사고 확률 불러오기
setInterval(function(){
    axios.get('http://localhost:5000/probability', {
    }).then((result) => {
        console.log(result);
        console.log(result.data);

        // 확률 갱신
        document.getElementById('probability').value = result.data.prob;

    }).catch(() => {
        console.log('Probability Not Ok');
    })

}, 2000);
