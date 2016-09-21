var isPlaying = false;

function playPause(audioTag) {
    if (isPlaying) {
        pauseAudioD(audioTag);
    } else {
        playAudioD(audioTag);
    }
}

function playAudioD(audioTag) {
    audioTag.play();
    audioTag.onplaying = function () {
        isPlaying = true;
    };
    audioTag.addEventListener("ended", nextSlide);
}

function pauseAudioD(audioTag) {
    audioTag.pause();
    audioTag.onpause = function () {
        isPlaying = false;
    };
    audioTag.removeEventListener("ended", nextSlide);
}

function getAudioTagD() {
    var audioData = $('.active > a').data('audio');
    return document.getElementById(audioData);
}

function nextSlide() {
    $('.carousel').carousel('next');
}

$('.item > a').click(function () {
    playPause(getAudioTagD());
});

$('#audio-carousel').on('slide.bs.carousel', function () {
    pauseAudioD(getAudioTagD());
});

$('#audio-carousel').on('slid.bs.carousel', function () {
    playAudioD(getAudioTagD());
});
