
$(document).ready(function () {
    size_li = $("#myList .project").size();
    x=8;
    $('#myList .project:lt('+x+')').show();
    $('#loadMore').click(function () {
        x= (x+4 <= size_li) ? x+4 : size_li;
        $('#myList .project:lt('+x+')').show();
         $('#showLess').show();
        if(x == size_li){
            $('#loadMore').hide();
        }
    });
    $('#showLess').click(function () {
        x=(x-4<0) ? 8 : x-4;
        $('#myList .project').not(':lt('+x+')').hide();
        $('#loadMore').show();
         $('#showLess').show();
        if(x == 8){
            $('#showLess').hide();
        }
    });
});

