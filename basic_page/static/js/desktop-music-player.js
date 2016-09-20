var isPlaying = false;

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

function getAudioTagD() {
    var audioData = $('.active > a').data('audio');
    return document.getElementById(audioData);
}

$('.item > a').click(function () {
    playPause(getAudioTagD());
});

$('#audio-carousel').on('slide.bs.carousel', function () {
    console.log('pause before transition');
    pauseAudio(getAudioTagD());
});

$('#audio-carousel').on('slid.bs.carousel', function () {
    console.log('playing after transition');
    playAudio(getAudioTagD());
});