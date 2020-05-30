$(document).ready(function() {
    $('.btn_class').on('click', function() {
        var btn_property = $(this)
        var row = $(this).closest('tr');
        var roll = row.find('.cls_roll').text();
        var cls = row.find('.cls_class').text();

        var api_url = 'http://localhost:8000/api/attendance/' + cls + '/' + roll 

        $.ajax({
            url: api_url,
            method: "GET",
            success: function(data){
                btn_property.addClass('btn btn-success');
            },
            error: function(err){
                alert(err.status);
            } 
        })

    })
    
})