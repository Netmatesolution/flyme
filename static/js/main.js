
$(document).ready(function () {
  $(".package-btn").on("click", function (e) {
    $(this).siblings().removeClass("btn-primary");
    $(this).addClass("btn-primary");
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

  $(document).on("click", ".btn-num-product-down1", function () {
    var numProduct = Number($(this).next().val());
    if (numProduct > 1) {
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

  $(".delete-cart").on("click", function () {
    let cartid = $(this).attr("data-cart-id");

    // alert(cartid)
    $.ajax({
      data: { cartid: cartid },
      headers: { "X-CSRFToken": csrftoken },
      type: "POST",
      url: "/activity/deleteitem/",
      success: function (response) {
        console.log(response.msg);
        swal(response.msg).then(() => {
          window.location.replace("/activity/cart/");
        });
      },
    });
  });

  $("#news-slider").owlCarousel({
    loop: true,
    margin: 10,
    autoplay:true,
    autoplaySpeed:500,
    // nav: true,
    responsiveClass: true,
    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 2,
      },
      1000: {
        items: 3,
      },
    },
  });

});


var countries = [
  "Jakarta",
  "Surabaya",
  "Bandung",
  "Bekasi",
  "Bali",
  "Tokyo",
  "Yokohama",
  "Osaka",
  "Nagoya",
  "Shanghai",
  "Beijing",
  "Wuhan",
  "Indonesia",
  "Japan",
  "China",
];

function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function (e) {
    var a,
      b,
      i,
      val = this.value;
    /*close any already open lists of autocompleted values*/
    closeAllLists();
    if (!val) {
      return false;
    }
    currentFocus = -1;
    /*create a DIV element that will contain the items (values):*/
    a = document.createElement("DIV");
    a.setAttribute("id", this.id + "autocomplete-list");
    a.setAttribute("class", "autocomplete-items");
    /*append the DIV element as a child of the autocomplete container:*/
    this.parentNode.appendChild(a);
    /*for each item in the array...*/
    for (i = 0; i < arr.length; i++) {
      /*check if the item starts with the same letters as the text field value:*/
      if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
        /*create a DIV element for each matching element:*/
        b = document.createElement("DIV");
        /*make the matching letters bold:*/
        b.innerHTML = "<i class='fas fa-map-marker  search__icon'></i> ";
        b.innerHTML += "<strong>" + arr[i].substr(0, val.length) + "</strong>";
        b.innerHTML += arr[i].substr(val.length);
        /*insert a input field that will hold the current array item's value:*/
        b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
        /*execute a function when someone clicks on the item value (DIV element):*/
        b.addEventListener("click", function (e) {
          /*insert the value for the autocomplete text field:*/
          inp.value = this.getElementsByTagName("input")[0].value;
          /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
          closeAllLists();
        });
        a.appendChild(b);
      }
    }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function (e) {
    var x = document.getElementById(this.id + "autocomplete-list");
    if (x) x = x.getElementsByTagName("div");
    if (e.keyCode == 40) {
      /*If the arrow DOWN key is pressed,
        increase the currentFocus variable:*/
      currentFocus++;
      /*and and make the current item more visible:*/
      addActive(x);
    } else if (e.keyCode == 38) {
      //up
      /*If the arrow UP key is pressed,
        decrease the currentFocus variable:*/
      currentFocus--;
      /*and and make the current item more visible:*/
      addActive(x);
    } else if (e.keyCode == 13) {
      /*If the ENTER key is pressed, prevent the form from being submitted,*/
      e.preventDefault();
      if (currentFocus > -1) {
        /*and simulate a click on the "active" item:*/
        if (x) x[currentFocus].click();
      }
    }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = x.length - 1;
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
    closeAllLists(e.target);
  });
}

autocomplete(document.getElementById("search-input"), countries);

