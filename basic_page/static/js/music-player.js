var isPlaying = false;
var currentAudio = '';

function playPause(audioTag) {
    if (isPlaying) {
        console.log('toggle-pause');
        pauseAudio(audioTag)
    } else {
        console.log('toggle-play');
        playAudio(audioTag)
    }
}

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

function getAudioTag() {
    var audioData = $('.active > a').data('audio');
    return document.getElementById(audioData);
}

$('.active').click(function () {
    console.log(isPlaying);
    currentAudio = getAudioTag();
    playPause(currentAudio);
});

$('#audio-carousel').on('slide.bs.carousel', function () {
    console.log('pause before transition');
    playAudio(getAudioTag());
    pauseAudio(getAudioTag());
});

$('#audio-carousel').on('slid.bs.carousel', function () {
    console.log('playing after transition');
    playAudio(getAudioTag());
});