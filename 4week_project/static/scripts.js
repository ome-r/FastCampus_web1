$(document).ready(function () {
    $(".list-group-item-action").click(function () {
        let product_title = $(this).attr('id');
        $.get("http://127.0.0.1:5000/dang?title=" + product_title)
            .then(function (result) {
                $("#detailModalLabel").text(result.title);
                $("#detailModalContent").text(result.content);
                $("#detailModal").modal('show');
            });
    });
});