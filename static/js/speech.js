var recognizing = true;
var recognition = new webkitSpeechRecognition();
recognition.continuous = true;
recognition.onend = reset();

// reset();

recognition.onerror = function(event) {
    console.log(event.error);
};

recognition.onresult = function (event) {
    var d = "";
    for (var i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
            d = event.results[i][0].transcript;
        }
    }
    console.log(d);
    setDirection(d);
}

function reset() {
    recognizing = false;
    button.innerHTML = "Click to Speak";
    count = 0;
}

function toggleStartStop() {
    if (recognizing) {
        recognition.stop();
        reset();
    } else {
        recognition.start();
        recognizing = true;
        button.innerHTML = "Click to Stop";
    }
}
