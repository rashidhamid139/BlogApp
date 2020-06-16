

$(document).ready(function(){
    $('.likebutton').click(function(e){
        e.preventDefault();
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
                    if (data.status){
                        $('#like'+ id).removeClass('btn btn-primary btn-sm');
                        $('#like'+ id).addClass('btn btn-success btn-sm');
                    }
                    else{
                        $('#like'+ id).removeClass('btn btn-success btn-sm');
                        $('#like'+ id).addClass('btn btn-primary btn-sm');
                    }
                }
            }
        )
    });
});

function updateComment(comment_id){
    alert("Comment ")
    $.ajax({
        type:'GET',
        url: `/comment-update/${comment_id}/`,
        data : getCookie('csrftoken'),
        success: function(response){
            $('#include').empty()
            $('#include').append(response);
            $('#updComment').click();

        }
        

    })
};

function commentUpdate(comment_id){

    $.ajax({
        type:'POST',
        url: `/comment-update/${comment_id}/`,
        data : {csrfmiddlewaretoken: getCookie('csrftoken'),  },
        success: function(response){
            $('#myModal').hide();
            window.location.href = `/post/${response.post_id}`

        }

    })
}
function deleteComment(comment_id){

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



$(document).ready(function(){
    $('#id_recipe_name').click(function(){
        recipe_name = $(this).val()
        var csrftoken = getCookie('csrftoken')
       $.ajax({
           type: 'POST',
           url: '/nondynamic/',
           data:{
               recipe_name: recipe_name
           }  ,
       })
    });
});

