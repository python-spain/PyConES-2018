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
  if (window.innerWidth < 768) {
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
  var $emailSuccessMessage = $('.js-email-success-message').val();
  var jqXHR = null;

  setUpScrollify();

  $emailSendBtn.on('click', function () {
    var email = $emailInput.val().toLowerCase();

    $emailWidget.removeClass('success error');

    if (isValidEmail(email)) {
      $emailSendBtn.prop('disabled', true);
      $emailSendBtn.find('img').addClass('animated infinite tada');

      if (jqXHR !== null) {
        jqXHR.abort();
      }

      jqXHR = $.ajax({ url: "/newsletter/subscribers/", type: "POST", data: { email:  email}})
        .done(function () {
          $emailInput.val($emailSuccessMessage);
          $emailWidget.addClass('success');
        })
        .fail(function () {
          $emailWidget.addClass('error');
        })
        .always(function () {
          jqXHR = null;
          $emailSendBtn.find('img').removeClass('animated');
          $emailSendBtn.prop('disabled', false);
        })
    } else {
      $emailWidget.addClass('error');
    }
  });

  $emailInput.on('focus', function () {
    if ($emailInput.hasClass('success')) {
      $emailInput.val('');
    }
    $emailWidget.removeClass('success error');
  });

  $emailInput.keyup(function (event) {
    if (event.keyCode === 13) {
        $emailSendBtn.click();
    }
});
});

