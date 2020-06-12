

$(document).ready(function(){
    $('.likebutton').click(function(){
        var id;
        id = $(this).attr('data-catid');
        $.ajax(
            {
                type: 'GET', 
                url: 'like', 
                data: {
                    post_id: id
                },
                success: function(data){
                    $('#like'+id).text("Like " + data.likeCount)
                    $('#like'+ id).removeClass('btn btn-primary btn-sm');
                    $('#like'+ id).addClass('btn btn-success btn-sm');
                }
            }
        )
    });
});

function deleteComment(comment_id){
    alert(comment_id)
    $.ajax({
        type:'GET',
        url: '/comment-delete/',
        data:{
            comment_id: comment_id,
        },
        success: function(data){
            if (data.status){
                $("#"+comment_id).parent().parent().hide();
            }
        }
    });
};



function getCookie(name){
    var cookieValue = null;
    if (document.cookie && document.cookie !== ''){
        var cookies = document.cookie.split(';');
        for (i=0; i<cookies.length; i++){
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length+1) === (name +'=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length +1));

            }
        }
    }
    return cookieValue;
};
