function setUpScrollify() {
  $.scrollify({
    section : '.js-scroll-section',
    setHeights: false
  });
}

function isValidEmail(email) {
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

$(window).resize(function() {
  var $main = $('.js-main');
  var $nav = $('.js-nav');
  if (window.innerWidth < 800) {
    $main.find('section').addClass('js-scroll-section');
    $nav.addClass('js-scroll-section');
  } else {
    $main.find('section').removeClass('js-scroll-section');
    $main.find('section:even').addClass('js-scroll-section');
    $nav.removeClass('js-scroll-section');
  }

  $.scrollify.update();
});

$(function () {
  var $emailWidget = $('.js-email-widget');
  var $emailSendBtn = $('.js-email-send-btn');
  var $emailInput = $('.js-email-input');

  setUpScrollify();

  $emailSendBtn.on('click', function () {
    var email = $emailInput.val().toLowerCase();

    $emailWidget.removeClass('success error');

    if (isValidEmail(email)) {
      $.ajax({
          headers: { "Accept": "application/json" },
          url: "https://xw5s3m0p1l.execute-api.eu-west-1.amazonaws.com/latest?email=" + email,
          type: "GET",
          crossDomain: true,
          success: function (response) {
            console.log(response);
            $emailInput.val('Got it!');
            $emailWidget.addClass('success');
          }
      });
    } else {
      $emailWidget.addClass('error');
    }
  });

  $emailInput.on('focus', function () {
    $emailInput.val('');
    $emailWidget.removeClass('success error');
  });

  $emailInput.on('focus', function () {
    $emailInput.val('');
    $emailWidget.removeClass('success error');
  });

  $emailInput.keyup(function (event) {
    if (event.keyCode === 13) {
        $emailSendBtn.click();
    }
});
});

