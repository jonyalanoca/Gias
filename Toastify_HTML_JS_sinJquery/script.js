function $(id) {
    return document.getElementById(id);
}
$("boton").addEventListener("click", function() {
    $("body").style.color = "red";
    Toastify({
        text: "This is a toast",
        duration: 3000,
        // destination: "https://github.com/apvarun/toastify-js",
        // newWindow: true,
        close: true,
        gravity: "bottom", // `top` or `bottom`
        position: "right", // ` right`, `center` or `right`
        stopOnFocus: true, // Prevents dismissing of toast on hover
        style: {
          background: "linear-gradient(to right, #00b09b, #96c93d)",
        },
        escapeMarkup:true,
        onClick: function(){alert("asdf");} // Callback after click
      }).showToast();
});




