$('#searchForm').submit(function (event) {
    var hotel = $('#hotel').val();
    console.log('%s ', hotel);
    $.ajax({
        url: '/',
        type: 'POST',
        data: JSON.stringify({ hotel: hotel, address: address, rating: rating, score:score}),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (data) {
            //render the result as table
            console.table(data);
            $("#hotelTemplate").tmpl(data.hotels).appendTo("#hotelTable");
        }
    });
    event.preventDefault();
});