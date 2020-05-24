$(document).on('click', '#close-preview', function(){
    $('.image-preview').popover('hide');
    // Hover befor close the preview
    $('.image-preview').hover(
        function () {
           $('.image-preview').popover('show');
        },
         function () {
           $('.image-preview').popover('hide');
        }
    );
});

$(function() {
    // Create the close button
    var closebtn = $('<button/>', {
        type:"button",
        text: 'x',
        id: 'close-preview',
        style: 'font-size: initial;',
    });
    closebtn.attr("class","close pull-right");
    // Set the popover default content
    $('.image-preview').popover({
        trigger:'manual',
        html:true,
        title: "<strong>Preview</strong>"+$(closebtn)[0].outerHTML,
        content: "",
        placement:'bottom'
    });
    // Clear event
    $('.image-preview-clear').click(function(){
        $('.image-preview').attr("data-content","").popover('hide');
        $('.image-preview-filename').val("");
        $('.image-preview-clear').hide();
        $(".image-preview-run").hide();
        $('.image-preview-input input:file').val("");
        $(".image-preview-input-title").text("Browse");
    });
    // Create the preview image
    $(".image-preview-input input:file").change(function (){
        var img = $('<img/>', {
            id: 'id',
            width:500,
            height:350
        });
        var file = this.files[0];
        var reader = new FileReader();
        // Set preview image into the popover data-content
        reader.onload = function (e) {
            $(".image-preview-input-title").text("Change");
            $(".image-preview-clear").show();
            $(".image-preview-run").show();
            $(".image-preview-filename").val(file.name);
            img.attr('src', e.target.result);
            //console.log(e.target.result);
            var imageData = e.target.result; //image data
            window.localStorage.setItem("image", imageData);
            $(".image-preview").attr("data-content",$(img)[0].outerHTML).popover("show");
        }
        reader.readAsDataURL(file);
    });

    // Run
    $(".image-preview-run").click(function (){
        $(".image-preview-clear").prop('disabled', true);
        $(".image-preview-run").prop('disabled', true);
        $(".image-preview-input").prop('disabled', true);

        imageData = window.localStorage.getItem("image");

        $.ajax({
            type: "POST",
            url: "/runCode",
            data: {
                text: imageData },
            success: function (){
                console.log("Success");
                window.location.replace('/result');
                //$(location).attr('href', '/result');
            },
            error: function (e) {
                console.log("ERROR : ", e);
            }
        });
    });
});