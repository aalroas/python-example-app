$(document).on("submit", "#new_product_form", function (e) {
    e.preventDefault();
  var formData = new FormData(this);
      formData.append("csrfmiddlewaretoken", $("input[name=csrfmiddlewaretoken]").val());
      formData.append("action", "post");
  $.ajax({
    type: "POST",
    url: "",
    data: formData,
    // {
    //   customer_id: $("#customer_id").val(),
    //   customer_name: $("#customer_name").val(),
    //   product_name: $("#product_name").val(),
    //   product_price: $("#product_price").val(),
    //   product_description: $("#product_description").val(),
    //   csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
    //   action: "post",
    // },
    cache: false,
    processData: false,
    contentType: false,
    success: function (json) {
      document.getElementById("new_product_form").reset();
      
      document.getElementById("alert_span").style.display = "block";
        setTimeout(function () {
            document.getElementById("alert_span").style.display = "none";
        }, 5000);
    },
    error: function (xhr, errmsg, err) {
      console.log(xhr.status + ": " + xhr.responseText);
    },
  });
});
