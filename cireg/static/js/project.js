/* Project specific Javascript goes here. */

/*
Formatting hack to get around crispy-forms unfortunate hardcoding
in helpers.FormHelper:

    if template_pack == 'bootstrap4':
        grid_colum_matcher = re.compile('\w*col-(xs|sm|md|lg|xl)-\d+\w*')
        using_grid_layout = (grid_colum_matcher.match(self.label_class) or
                             grid_colum_matcher.match(self.field_class))
        if using_grid_layout:
            items['using_grid_layout'] = True

Issues with the above approach:

1. Fragile: Assumes Bootstrap 4's API doesn't change (it does)
2. Unforgiving: Doesn't allow for any variation in template design
3. Really Unforgiving: No way to override this behavior
4. Undocumented: No mention in the documentation, or it's too hard for me to find
*/
$('.form-group').removeClass('row');
$('.rich-text a[href^="http://"]').attr('target', '_blank');
$('.rich-text a[href^="https://"]').attr('target', '_blank');
$(".project-diary .card").click(function() {
  window.location = $(this).find("a").attr("href"); 
  return false;
});
$(".case-studies .card").click(function() {
  window.location = $(this).find("a").attr("href"); 
  return false;
});
function switch_menu(body) {
    if ($(body).scrollTop() > 50) {
        $('header').addClass('medium');
        $('header').removeClass('large');
    } else {
        $('header').addClass('large');
        $('header').removeClass('medium');
    }
}
$(document).ready(function() {
    switch_menu(this);
    // init Isotope
    var $grid = $('.download-item-list').isotope({
      // options
    });

    // toggle dropdown on hover
    $('.navbar-main .nav-item.dropdown').on('hide.bs.dropdown', function (e) {
        return false;
    });
    $('.navbar-main .nav-item.dropdown').hover(function(){
        $(this).toggleClass('show');
        $(this).find('.dropdown-menu').toggleClass('show');
    });
    // store filter for each group
    var filters = [];
    $('.filter li a.is-checked').each(function(i, filter) {
        filters.push($(filter).attr('data-filter'));
    });
    console.log(filters);

    check_for_empty_result = function () {
        
    };

    $('.filter li:not(.show-all,.hide-all) a').on( 'click', function( event ) {
        $('.no-items-found').hide();
        var $button = $( event.currentTarget );
        $button.toggleClass('is-checked');

        var isChecked = $button.hasClass('is-checked');
        var filter = $button.attr('data-filter');
        if ( isChecked ) {
            filters.push(filter);
          } else {
            filters.splice(filters.indexOf(filter), 1);
        }
        console.log(filters);
        // combine filters
        var filterValue;
        if (filters.length == 0) {
            filterValue = '.xxxx';
        } else {
            filterValue = filters.join(',');
        }
        // set filter for Isotope
        console.log(filterValue);
        $grid.isotope({ filter: filterValue });
    });
    $('.filter .show-all').on('click', function( event ) {
        $('.no-items-found').hide();
        $('.filter .hide-all').show();
        $(this).hide();
        $('.filter li:not(.show-all,.hide-all) a:not(.is-checked)').addClass('is-checked');
        $grid.isotope({ filter: '*' });
    });
    $('.filter .hide-all').on('click', function( event ) {
        $('.filter .show-all').show();
        $(this).hide();
        $('.filter li:not(.show-all,.hide-all) a.is-checked').removeClass('is-checked');
        $grid.isotope({ filter: '.xxxx' });
    });
    $grid.on( 'layoutComplete', function( event, laidOutItems ) {
        if (laidOutItems.length == 0) {
           $('.no-items-found').show();
        } else {
            $('.no-items-found').hide();
        }
    } )

})
$(window).scroll(function(){
    switch_menu(this);
});

function createCookie(name, value, days) {
    var date = new Date(),
        expires = '';
    if (days) {
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    } else {
        expires = "";
    }
    document.cookie = name + "=" + value + expires + "; path=/";
}


$('#CookielawBanner button').click(function() {
    createCookie('cookielaw_accepted', '1', 10 * 365);
});
