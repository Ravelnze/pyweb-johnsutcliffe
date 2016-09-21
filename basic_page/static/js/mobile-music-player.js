var isPlaying = false;

function playAudioM(audioTag) {
    audioTag.play();
    audioTag.onplaying = function () {
        isPlaying = true;
    };
    audioTag.addEventListener("ended", hidePanel);
}

function pauseAudioM(audioTag) {
    audioTag.pause();
    audioTag.onpause = function () {
        isPlaying = false;
    };
    audioTag.removeEventListener("ended", hidePanel);
}

function getAudioTagM() {
    var audioData = $('a.audio-target').data('audio');
    return document.getElementById(audioData);
}

function hidePanel() {
    $('div.panel-collapse.collapse').collapse('hide');
}

$('div.panel-collapse.collapse').on('hide.bs.collapse', function () {
    pauseAudioM(getAudioTagM());
    var getHeader = $(this).siblings();
    $(getHeader[0]).find("a").removeClass('audio-target');
});

$('div.panel-collapse.collapse').on('shown.bs.collapse', function () {
    var getHeader = $(this).siblings();
    $(getHeader[0]).find("a").addClass('audio-target');
    playAudioM(getAudioTagM());
});