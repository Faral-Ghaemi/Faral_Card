let startTime;
let timerInterval;

$(document).ready(function() {
    $('#startButton').on('click', function() {
        startWork();
    });

    $('#endButton').on('click', function() {
        $('#reportPopup').show();
    });

    $('#submitReport').on('click', function() {
        const report = $('#reportText').val();
        endWork(report);
        $('#reportPopup').hide();
        $('#reportText').val('');
    });
});

function startWork() {
    // ارسال درخواست به بک‌اند برای شروع کار
    $.post('/start-work/', { /* داده‌های لازم */ }, function(data) {
        console.log(data);
    });

    startTime = new Date();
    $('#startButton').hide();
    $('#endButton').show();
    timerInterval = setInterval(updateTimer, 1000);
}

function endWork(report) {
    // ارسال درخواست به بک‌اند برای پایان کار
    $.post('/end-work/', { report: report, /* سایر داده‌های لازم */ }, function(data) {
        console.log(data);
    });

    clearInterval(timerInterval);
    $('#endButton').hide();
    $('#startButton').show();
    $('#timer').text('00:00:00');
}

function updateTimer() {
    let currentTime = new Date();
    let elapsed = new Date(currentTime - startTime);
    let hours = elapsed.getUTCHours();
    let minutes = elapsed.getUTCMinutes();
    let seconds = elapsed.getUTCSeconds();
    $('#timer').text(`${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`);
}
