var isPlaying = false;

function playAudio(audioTag) {
    audioTag.play();
    audioTag.onplaying = function () {
        isPlaying = true;
    }
}

function pauseAudio(audioTag) {
    audioTag.pause();
    audioTag.onpause = function () {
        isPlaying = false;
    }
}

function getAudioTagM() {
    var audioData = $('a.audio-target').data('audio');
    console.log(audioData);
    return document.getElementById(audioData);
}

$('div.panel-collapse.collapse').on('hide.bs.collapse', function () {
    pauseAudio(getAudioTagM());
    var getHeader = $(this).siblings();
    $(getHeader[0]).find("a").removeClass('audio-target');
});

$('div.panel-collapse.collapse').on('shown.bs.collapse', function () {
    var getHeader = $(this).siblings();
    $(getHeader[0]).find("a").addClass('audio-target');
    playAudio(getAudioTagM());
});