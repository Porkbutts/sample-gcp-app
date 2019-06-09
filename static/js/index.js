function reloadPeople() {
    $.ajax('/api/recentPersons', {
        method: 'GET',
        success: function(data) {
            $('#people').empty();
            data.forEach(function(element) {
                let name = element.firstname + ' ' + element.lastname;
                let $row = $('<div class="row">' + name + '</div>');
                $('#people').append($row);
            });
        }
    });
}

$(document).ready(function() {
    reloadPeople();

    $('#createBtn').click(function(e) {
        $.ajax('/api/persons', {
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                firstname: $('#firstname').val(),
                lastname: $('#lastname').val()
            }),
            dataType: 'json',
            success: function(data) {
                reloadPeople();
            },
            error: function(xhr, ajaxOptions, thrownError) {
                alert("Status: " + xhr.status + ", Message: " + xhr.responseText);
            }
        });
    });
});