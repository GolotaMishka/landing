function windowSize(){
    if ($(window).width() <= '992'){
        $('#profile_section').css({"display":"none"});
        $('#profile_section_min').css({"display":"block"});

        $('#review_section').css({"display":"none"});
        $('#review_section_min').css({"display":"block"});
    } else {
        $('#profile_section').css({"display":"block"});
        $('#profile_section_min').css({"display":"none"});

        $('#review_section').css({"display":"block"});
        $('#review_section_min').css({"display":"none"});
    }
}

$(window).resize(windowSize); 
$(window).load(windowSize); 
