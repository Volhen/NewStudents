function initJournal() {
    var indicator = $('#ajax-progress-indicator');

    $('.day-box input[type = "checkbox"]').click(function(event) {
        /*alert('test');*/
        var box = $(this);
        $.ajax(box.data('url'), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'pk': box.data('student-id'),
                'date': box.data('date'),
                'present': box.is(':checked') ? '1' : '',
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            'beforeSend': function(xhr, settings) {
                indicator.show();
            },
            'error': function(xhr, status, error) {
                alert(error);
                indicator.hide();
            },
            'success': function(data, status, xhr) {
                indicator.hide();
            }
        });
    });
}

function initGroupSelector() {
    // look up select element with groups and attach our even handler
    // on field "change" event
    $('#group-selector select').change(function(event) {
        // get value of currently selected group option
        var group = $(this).val();
        if (group) {
            // set cookie with expiration date 1 year since now;
            // cookie creation function takes period in days
            $.cookie('current_group', group, { 'path': '/', 'expires': 365 });
        } else {
            // otherwise we delete the cookie
            $.removeCookie('current_group', { 'path': '/' });
        }
        // and reload a page
        location.reload(true);
        return true;
    });
}

moment.locale('ru');

function initDateFields() {
    $('input.dateinput').datetimepicker({
        format: 'MM-DD-YYYY'
    }).on('dp.hide', function(event) {
        $(this).blur();
    });
}
/*, input.datetimeinput*/
function initModal() {
    $('a.edit-form-link,a#add_btn.btn-primary').click(function(event) {
        var link = $(this);
        $.ajax({
            'url': link.attr('href'),
            'dataType': 'html',
            'type': 'get',
            'success': function(data, status, xhr) {
                // check if we got successfull response from the server
                if (status != 'success') {
                    alert('Ошибка на сервере. Попробуйте позже .');
                    return false;
                }

                // update modal window with arrived content from the server
                var modal = $('#myModal'),
                    html = $(data),
                    form = html.find('#content-column form');
                modal.find('.modal-title').html(html.find('#content-column h2').text());
                modal.find('.modal-body').html(form);

                // init our edit form
                initForm(form, modal);

                // setup and show modal window finally
                modal.modal({
                    'keyboard': false,
                    'backdrop': false,
                    'show': true
                });
            },
            'error': function() {
                alert('Ошибка на сервере. Попробуйте позже ');
                return false
            }
        });

        return false;
    });
}

function initForm(form, modal) {
    // attach datepicker
    initDateFields();

    var complete = true;

    // close modal window on Cancel button click
    form.find('input[name="cancel_button"]').click(function(event) {
        modal.modal('hide');
        return false;
    });
    // modal window on Cancel button click
    form.find('input[name="save_button"]').click(function(event) {
        modal.modal('hide');
    });

    // make form work in AJAX mode
    //if (complect) {
    form.ajaxForm({
        'dataType': 'html',
        'error': function() {
            alert('Ошибка на серве. Попробуйте позже');
            return false;
        },
        'success': function(data, status, xhr) {
            var html = $(data),
                newform = html.find('#content-column form');

            // copy alert to modal window
            modal.find('.modal-body').html(html.find('.alert'));

            // copy form to modal if we found it in server response
            if (newform.length > 0) {
                modal.find('.modal-body').append(newform);

                // initialize form fields and buttons
                initForm(newform, modal);
            } else {
                // if no form, it means success and we need to reload page
                // to get updated students list;
                // reload after 2 seconds, so that user can read success message
                //setTimeout(function() { location.reload(true); }, 500);
                location.reload(true);
            }
        }
    });
    //complete = false;
}
//}

$(document).ready(function() {
    initJournal();
    initGroupSelector();
    //initDateFields();
    initModal();
});