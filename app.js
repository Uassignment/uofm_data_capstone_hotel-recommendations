$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        Search();
    });
});


// call Flask API endpoint
function Search() {
    var Hotel = $("#Hotel").val();
    


    // check if inputs are valid

    // create the payload
    var payload = {
        "Hotel": Hotel
        
    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/Search",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);

            $('#output > tbody').empty();

            for (let i=0; i<returnedData.recommendation.length; i++){
                let data = returnedData.recommendation[i];

                let row = "<tr>";
                row += `<td>${data.Hotel}</td>`;
                row += `<td>${data.Address}</td>`;
                row += `<td>${data.Rating}</td>`;
                row += `<td>${data.Score}</td>`;
                $('#output > tbody').append(row);
            }

        },
        //error: function(XMLHttpRequest, textStatus, errorThrown) {
           //alert("Status: " + textStatus);
            //alert("Error: " + errorThrown);
        error: function(XMLHttpRequest) {
            alert("Unknown Hotel Name: Please see Tableau Visual page for list of hotels!");
        }
    });

}