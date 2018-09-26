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
    $('.navbar-nav .nav-item.dropdown').hover(function(){
        console.log("hover");
        $(this).find('.dropdown-toggle').dropdown('toggle');
    });
    // store filter for each group
    var filters = {};

    $('.filter li a').on( 'click', function( event ) {
        var $button = $( event.currentTarget );
        $button.toggleClass('is-checked');
        var isChecked = $button.hasClass('is-checked');
        // get group key
        var $buttonGroup = $button.parents('.button-group');
        var filterGroup = $buttonGroup.attr('data-filter-group');
        // set filter for group
        if ( isChecked ) {
            addFilter( filterGroup, $button.attr('data-filter') );
          } else {
            removeFilter( filterGroup, $button.attr('data-filter') );
        }
        console.log(filters);
        // combine filters
        var filterValue = concatValues( filters );
        // set filter for Isotope
        console.log(filterValue);
        $grid.isotope({ filter: filterValue });
    });

    // flatten object by concatting values
    function concatValues( obj ) {
        var value = '';
        for ( var prop in obj ) {
            value += obj[ prop ].join('');
        }
        return value;
    }

    function addFilter( group, filter ) {
        var group_filters = filters[group];
        if (group_filters===undefined) {
            group_filters = [];
        }
        if ( group_filters.indexOf( filter ) == -1 ) {
            group_filters.push( filter );
        }
        filters[group] = group_filters;
    }

    function removeFilter( group, filter ) {
        var group_filters = filters[group];
        var index = group_filters.indexOf( filter);
        if ( index != -1 ) {
            group_filters.splice( index, 1 );
        }
        filters[group] = group_filters;
    }

})
$(window).scroll(function(){
    switch_menu(this);
});