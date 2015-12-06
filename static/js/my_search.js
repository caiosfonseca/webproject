$(document).on({
    input: function (event) {
        if (event.handled !== true) {
            event.handled = true;
            var input = $(this).val().toLowerCase();
            $.each($(".search_item_name"), function(){
                if($(this).html().toLowerCase().indexOf(input) > -1){
                    $(this).parent().parent().addClass("unhidden");
                    $(this).parent().parent().removeClass("hidden");
                }else{
                    $(this).parent().parent().addClass("hidden");
                    $(this).parent().parent().removeClass("unhidden");
                }
            });
        } 
        return false;     
    }
}, "#search_input");