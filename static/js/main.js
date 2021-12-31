// const card = document.querySelector(".map-card");
// const cardBody = card.querySelector(".card-body");

// card.addEventListener("click", () => {
//   cardBody.classList.toggle("closed");
// });

$(document).ready(function () {
  $(".package-btn").on("click", function (e) {
    $(this).siblings().removeClass("btn-secondary");
    $(this).addClass("btn-secondary");
    $(".package-description").css("display", "block");
    $(".addtocart").removeClass("d-none");
    let id = $(this).attr("data-package_id");
    $.ajax({
      data: { packageid: id },
      type: "GET",
      url: "/activity/packagedescription/",
      success: function (response) {
        $(".package-description").html(response.description);
        let design = ``;
        let quantity = "";
        let totalprice = 0;
        response.packageprice.map((item, index) => {
          quantity = `<div class="bg-light row p-4 my-2">
                <div class="col-md-6 d-flex align-items-center">
                  <h6>${item.name}</h6>
                </div>
                <div
                  class="col-md-6 d-flex align-items-center justify-content-end"
                >
                  <span class="mx-1 item-total-${index}" >${item.price}</span>

                  <button type="button" class="btn btn-num-product-down" data-price="${item.price}" data-minusquantity="${index}">
                    <i class="fas fa-minus"></i>
                  </button>

                    <input class="mx-2 form-control" min="1" type="number" readonly value="1" name="${item.id}" style="width:60px;text-align:center;border:none"/>

                  <button type="button" class="btn btn-num-product-up" data-price="${item.price}" data-addquantity="${index}">
                    <i class="fas fa-plus"></i>
                  </button>
                </div>
              </div>`;
          totalprice = totalprice + parseInt(item.price);
          design += quantity;
        });

        $(".quantity-list").html(design);
        $(".cart-total").text(totalprice);
      },
    });
  });

  $(document).on("click", ".btn-num-product-down", function () {
    var numProduct = Number($(this).next().val());
    if (numProduct > 0) {
      $(this)
        .next()
        .val(numProduct - 1);
      let itemnumber = $(this).attr("data-minusquantity");
      let productprice = $(this).attr("data-price");
      itemtotal(itemnumber, numProduct - 1, productprice);
      let total = $(".cart-total").text();
      let price = parseInt(total) - parseInt(productprice);
      carttotal(price);
    }
  });

  $(document).on("click", ".btn-num-product-up", function () {
    var numProduct = Number($(this).prev().val());
    $(this)
      .prev()
      .val(numProduct + 1);
    let itemnumber = $(this).attr("data-addquantity");
    let productprice = $(this).attr("data-price");
    itemtotal(itemnumber, numProduct + 1, productprice);
    let total = $(".cart-total").text();
    let price = parseInt(total) + parseInt(productprice);
    carttotal(price);
  });

  let itemtotal = (count, quantity, price) => {
    $(".item-total-" + count).html(quantity * price);
  };

  let carttotal = (price) => {
    $(".cart-total").text(price);
    if (price == 0) {
      $(".addtocart").addClass("d-none");
    }
    if (price > 0) {
      $(".addtocart").removeClass("d-none");
    }
  };

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  const csrftoken = getCookie("csrftoken");

  $(".addtocartform").submit(function (e) {
    e.preventDefault();
    var formValues = $(this).serializeArray();
    $.ajax({
      data: formValues,
      headers: { "X-CSRFToken": csrftoken },
      type: "POST",
      url: "/activity/addtocart/",
      success: function (response) {
        keys = Object.keys(response);
        let htmldesign = ``;
        keys.forEach((item) => {
          data = Object.values(response[item]);
          if (data[3] == "error") {
            htmldesign += `<p>${data[2]} for ${item} is <span class="text-info">${data[0]} </span></p>`;
          } else {
            htmldesign += `<p>${data[2]} for ${item} is <span class="text-success"> ${data[0]}</span></p>`;
          }
        });

        maindiv = document.createElement("div");
        maindiv.innerHTML = htmldesign;

        swal({
          content: maindiv,
        });
      },
    });
  });

  $(".book-now").on("click", function (e) {
    res = $(".addtocartform").submit();
    window.location.replace("/activity/book-now/");
  });

  // login before adding into cart
  $(".cart-icon-nologin").on("click", function (e) {
    e.preventDefault();
    swal("Please login before adding product into cart");
  });

  $(".select-country").on("change", function () {
    let country = this.value;
    $(".tourcountry-search").attr("href", `/tour/theme/?country=${country}`);
  });

  $(".select-country-theme").on("change", function () {
    let url_string = window.location.href;
    let url = new URL(url_string);
    let country = url.searchParams.get("country");
    let category = this.value;
    $(".tourtheme-search").attr(
      "href",
      `/tour/theme/?country=${country}&theme=${category}`
    );
  });

  $(".staycation-select-country").on("change", function () {
    let country = this.value;
    $(".staycationcountry-search").attr(
      "href",
      `/staycation/theme/?country=${country}`
    );
  });

  $(".select-staycation-theme").on("change", function () {
    let url_string = window.location.href;
    let url = new URL(url_string);
    let country = url.searchParams.get("country");
    let category = this.value;
    $(".staycationtheme-search").attr(
      "href",
      `/staycation/theme/?country=${country}&theme=${category}`
    );
  });


  $(".select-activity-country").on("change", function () {
    let country = this.value;
    $(".activitycountry-search").attr(
      "href",
      `/activity/theme/?country=${country}`
    );
  });

   $(".select-activity-theme").on("change", function () {
     let url_string = window.location.href;
     let url = new URL(url_string);
     let country = url.searchParams.get("country");
     let category = this.value;
     $(".activitytheme-search").attr(
       "href",
       `/activity/theme/?country=${country}&theme=${category}`
     );
   });


        var today = new Date();
        var dd = String(today.getDate()).padStart(2, "0");
        var mm = String(today.getMonth() + 1).padStart(2, "0"); //January is 0!
        var yyyy = today.getFullYear();

        // today = mm + "/" + dd + "/" + yyyy;
        today = `${dd} + "/" + ${mm} + "/" + ${yyyy}`;

      $('input[name="tourdates"]').daterangepicker({
        minDate: today,
        locale: {
          cancelLabel: "Clear",
          format: "DD/MM/YYYY",
        },
      });

});
