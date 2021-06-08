var storeForm = document.getElementById("new_product_form");

storeForm.addEventListener("submit", function (event) {
  event.preventDefault();

  var formData = new FormData(storeForm),
    result = {};

  for (var entry of formData.entries()) {
    result[entry[0]] = entry[1];
  }

  result = JSON.stringify(result);

  storeForm.reset();

  document.getElementById("alert_span").style.display = "block";

  setTimeout(function () {
    document.getElementById("alert_span").style.display = "none";
  }, 5000);

  console.log(result);
});
