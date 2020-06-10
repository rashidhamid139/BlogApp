
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
    $.ajax({
        type:'GET',
        url: '/comment-delete/',
        data:{
            comment_id: comment_id,
        },
        success: function(data){
            if (data.status){
                // $(this).closest(".media-body, .bg-olive").remove();
                $("div#"+comment_id).parents(".media-body, .bg-olive").remove();
                
            }
        }
    });
}


