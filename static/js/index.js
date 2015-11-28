$(document).ready(function() {
    jQuery('.slider_recommended').lbSlider({
        leftBtn: '.recommended_sa-left', // left button selector
        rightBtn: '.recommended_sa-right', // right button selector
        visible: 5, // visible elements quantity
        autoPlay: true, // autoscroll
        autoPlayDelay: 10 // delay of autoscroll in seconds
    });
    jQuery('.slider_top').lbSlider({
        leftBtn: '.top_sa-left', // left button selector
        rightBtn: '.top_sa-right', // right button selector
        visible: 5, // visible elements quantity
        autoPlay: true, // autoscroll
        autoPlayDelay: 10 // delay of autoscroll in seconds
    });
});

