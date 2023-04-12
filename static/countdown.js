var timer1 = "0:11";
var interval = setInterval(function() {
    var timer = timer1.split(':');
    var minutes = parseInt(timer[0], 10);
    var seconds = parseInt(timer[1], 10);
    --seconds;
    minutes = (seconds < 0) ? --minutes : minutes;
    console.log(minutes, seconds);
    seconds = (seconds < 0) ? 59 : seconds;
    seconds = (seconds < 10) ? '0' + seconds : seconds;
    if (minutes < 0) {
        clearInterval(interval);
        fetch("/startOver", {
            method: "POST" 
        })
        location.reload();
    } else {
        $('.countdown').html(minutes + ':' + seconds);
        timer1 = minutes + ':' + seconds;
    } 
}, 1000);

