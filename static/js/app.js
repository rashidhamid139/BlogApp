
$(document).ready(function(){
    $.ajax({
        url: '/rooms/list/',
        type: 'GET',
        dataType: 'json',
        success: function(data){
            let rows = '';
            data.rooms.forEach(room => {
                rows += `
                <tr>
                    <td>${ room.name }</td>
                    <td>${ room.room_number }</td>
                    <td>${ room.nobeds }</td>
                    <td>${ room.room_type }</td>
                    <td>
                        <button class="btn deleteBtn" data-id="${room.id}">Delete</button>
                        <button class="btn updateBtn" data-id="${room.id}">Update</button>
                    </td>
                </tr>`;
            });

            $('#myTable > tbody:last-child').append(rows);
            $('.deleteBtn').each((i, elm) => {
                $(elm).on("click", (e) =>{
                    deleteRoom($(elm));
                })
            })
        }
    })
});

$(document).ready(function(){
    $('#createRoom').click(function(){
        $.ajax({
            type: 'GET',
            url: '/rooms/create/',
            success: function(data){
                $("#create").append(data).addClass('mt-10');
            }
        })
    })
})


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

function createRoom(){
    $("#FormID").on('submit', function(e){
        e.preventDefault();
        $.ajax({
            url: '/rooms/create/', 
            type: "POST",
            data: {
            csrfmiddlewaretoken: getCookie('csrftoken'),
            name: $('#id_name').val(),
            status: $('#id_status').val(),
            room_number: $('#id_room_number').val(),
            nobeds: $('#id_nobeds').val(),
            room_type: $('#id_room_type').val()
            },

            headers: {Accept: 'application/json'},
            success: function(data){
                if(data.message){
                window.location.href = '/rooms/'
                }
                else{
                    alert(data.error)
                }
            },
            error: function(xhr, errmsg, err){
                alert(xhr, err, errmsg);
                alert("sdsgvdg")
            }
        })
    });
};


function  deleteRoom(el){
    roomId  =  $(el).data('id')
    $.ajax({
        url:  `/rooms/delete/${roomId}/`,
        type:  'post',
        dataType:  'json',
        data: { },
        success:  function (data) {
            $(el).parents()[1].remove()
        }
    });
};