/* ---------------------------------------------------------------------------------
Setting
--------------------------------------------------------------------------------- */
baseUrl = 'http://127.0.0.1:5000'


/* ---------------------------------------------------------------------------------
Socket
--------------------------------------------------------------------------------- */
// Socket 연결
const socket = io.connect(baseUrl);

// Socket 연결 시 작동
socket.on('connect', () => {
    console.log('Socket Connected Success');
    console.log(socket);
    socket.emit( 'my event', {
        data: 'User Connected'
    })
    socket.emit('connected');
});

/* ---------- [ UI ]---------- */
// 실시간 속도
socket.on('ui_speed', function(speed) {
    // console.log(speed);
});

// 실시간 확률
socket.on('ui_prob', function(prob) {
    document.getElementById('probability').innerText = prob.prob;
});

// 운전자 영상
socket.on('ui_act_pic', function(data) {
    const frame = data['frame']
    document.getElementById('img-act').src = "data:image/;base64,"+frame;
});

// 정면 영상
socket.on('ui_front_pic', function(data) {
    const frame = data['frame']
    document.getElementById('img-front').src = "data:image/;base64,"+frame;
});

/* ---------------------------------------------------------------------------------
Functions
--------------------------------------------------------------------------------- */
/* ---------- [ GPS ]---------- */
function getLocation() {
    if (navigator.geolocation) { // GPS를 지원하면
        navigator.geolocation.getCurrentPosition(function(position) {
            socket.emit('gps', {
                'lat': position.coords.latitude,
                'lng': position.coords.longitude,
                'timestamp': position.timestamp
            });
        }, function(error) {
            console.error(error);
        }, {
            enableHighAccuracy: true,
            maximumAge: 0,
            timeout: Infinity
        });
    } else {
        alert('GPS를 지원하지 않습니다');
    }
}
var gpsInterval;


/* ---------- [ Start / Stop ]---------- */
async function start() {
    await axios.post(baseUrl + '/start', {
        'id': socket.id
    })

    // 주기적 GPS 실행
    gpsInterval = setInterval(async function(){
        getLocation();
    }, 100);
}

async function stop() {
    clearInterval(gpsInterval);     // GPS 확인 정지

    await axios.post(baseUrl + '/stop').then((response) => {
        console.log(response);
    });
}