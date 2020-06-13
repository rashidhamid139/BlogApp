
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
                        <button class="btn updateBtn"  onclick="updateRoomGet(this)" data-id="${room.id}">Update</button>
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
                $("#create").empty();
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
    $('#FormID').submit(function(e){
        e.preventDefault();
        var serializedData = $(this).serialize();

        $.ajax({
            type: 'POST',
            url: '/rooms/create/',
            data: serializedData,
            success: function(response){
                $('#FormID').hide();
                $('#myTable').focus();
                var instance = JSON.parse(response["instance"]);
                var fields = instance[0]["fields"];

                window.location.href = '/rooms/';
                
            }
        })
    })
};


function updateRoom(room_id){

    var room_id = room_id;
    $('#roomUpdateID').submit(function(e){
        e.preventDefault();
        var serializedData = $(this).serialize();

        $.ajax({
            type: 'POST',
            url: `/rooms/update/${room_id}/`,
            data: serializedData,
            success: function(response){
                $('#updateRoomID').hide();
                $('#myTable').focus();
                window.location.href = '/rooms/'
            }
        })
    })
}



function updateRoomGet(clicked_room){
    var room_id = clicked_room.getAttribute('data-id');
    $.ajax({
        type: 'GET',
        url: `/rooms/update/${room_id}/`,
        success: function(data){
            $("#create").empty();
            $("#create").append(data).addClass('mt-10');
        }
    })
}

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