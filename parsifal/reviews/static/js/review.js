$(function () {
  var RETURN = 13;
  var ESC = 27;
  var is_editing = false;

  $.fn.addSettings = function () {
    $(this).blur(function () {
      var author = $(this).val();
      var parent = $(this).closest('li');
      var id = $('#review-id').val();
      if (author == "") {
        parent.remove();
        is_editing = false;
      }
      else {
        $.ajax({
            url: '/reviews/add_author/',
            data: { id: id, username: author },
            type: 'get',
            cache: false,
            success: function (data) {
              parent.remove();
              $('.authors').append(data);
              $('.remove-author').unbind('click').bind('click', removeAuthor);
            },
            complete: function () {
              is_editing = false;
            }
        });
      }
    });

    $(this).keyup(function (evt) {
      var keyCode = evt.which?evt.which:evt.keyCode; 
      if (keyCode == RETURN) {
        $(this).blur();
      }
      else if (keyCode == ESC) {
        $(this).closest('li').remove();
        is_editing = false;
      }
    });
  };

  var removeAuthor = function () {
    var review_id = $('#review-id').val();
    var parent = $(this).closest('li');
    var author_id = parent.attr("author-id");
    $.ajax({
      url: '/reviews/remove_author/',
      data: { review_id: review_id, author_id: author_id },
      type: 'get',
      cache: false,
      success: function (data) {
        parent.remove();
      }
    });
  };

  $('.add-author').click(function () {
    if (is_editing) {
      return false;
    }
    else {
      is_editing = true;
      $('.authors').append('<li class="add-author-input"><input type="text" class="input-author"> <span>(please inform the author\'s username or email and then press <strong>Enter</strong> to confirm or <strong>Esc</strong> to cancel)</span></li>');
      $('.input-author').focus();
      $('.input-author').addSettings();
    }
  });

  $('.remove-author').unbind('click').bind('click', removeAuthor);

});