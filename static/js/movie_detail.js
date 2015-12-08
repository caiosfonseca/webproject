$(document).ready(function() {
    jQuery('.slider_similar').lbSlider({
        leftBtn: '.similar_sa-left', // left button selector
        rightBtn: '.similar_sa-right', // right button selector
        visible: 5, // visible elements quantity
        autoPlay: true, // autoscroll
        autoPlayDelay: 10 // delay of autoscroll in seconds
    });
});