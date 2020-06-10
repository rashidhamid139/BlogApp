
$(document).ready(function(){
    $("#id_username").change(function(){
        var username = $(this).val();
        $.ajax({
            type: 'GET',
            url: '/validate-username/',
            data: {
                username: username
            },
            success: function(data){
                if (data.is_taken){
                    var appendHtml = '<p id="appendWarningUsername" class="alert text-danger">' + data.message + "</p>" 
                    $("#id_username").addClass("is-invalid").parent("div").prepend(appendHtml)
                    // $("#id_username").parent("div").prepend(appendHtml)
                }
                else{
                    $("#appendWarningUsername").hide();  
                    $("#id_username").removeClass("is-invalid").addClass(" form-control is-valid");  
                }
            }
        });
    });
});

$(document).ready(function(){
    $("#id_email").change(function(){
        var email = $(this).val();
        $.ajax({
            type: 'GET',
            url: '/validate-email/',
            data: {
                email:email
            },
            success: function(data){
                if (data.is_taken){
                    var appendHtml = '<p id="appendWarningEmail" class="alert text-danger">' + data.message + "</p>" 
                    $("#id_email").addClass("is-invalid").parent("div").prepend(appendHtml)
              }
                else{
                    $("#appendWarningEmail").hide();
                    $("#id_email").removeClass("is-invalid").addClass("is-valid");    
                }
            }
        });
    })

});