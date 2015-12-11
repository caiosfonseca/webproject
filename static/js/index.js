$(document).ready(function() {
    $.each($(".slider_recommendation"), function(){
        var recom_type = $(this).children().eq(1).attr('recom_type');
        jQuery('.'+recom_type).lbSlider({
            leftBtn: '.'+recom_type+'-left', // left button selector
            rightBtn: '.'+recom_type+'-right', // right button selector
            visible: 5, // visible elements quantity
            autoPlay: true, // autoscroll
            autoPlayDelay: 10 // delay of autoscroll in seconds
        });
    });
});

