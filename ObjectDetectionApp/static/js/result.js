$(document).ready(function(){

    $.ajax({
            type: "GET",
            url: "/getCode",
            data: "",
            success: function (data){
                //console.log('data:image/jpeg;base64,' + data);

                imageData = window.localStorage.getItem("image");
                var img1 = document.getElementById('img1');
                img1.src = imageData;

                var img2 = document.getElementById('img2');
                img2.src = 'data:image/jpeg;base64,' + data;
            },
            error: function (e) {
                console.log("ERROR : ", e);
            }
    });
});