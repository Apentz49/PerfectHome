$(document).ready(function () {

	// List - Grid Swticher
	$("a.switcher").bind("click", function(e){
		e.preventDefault();
		
		var theid = $(this).attr("id");
		var thewrapper = $("#product-list");
		var classNames = $(this).attr('class').split(' ');

		
		if($(this).hasClass("active")) {
			// if currently clicked button has the active class
			// then we do nothing!
			return false;
		} else {
			// otherwise we are clicking on the inactive button
			// and in the process of switching views!

  			if(theid == "gridview") {
				$(this).addClass("active");
				$("#listview").removeClass("active");

				// remove the list class and change to grid
				thewrapper.removeClass("list-layout");
				thewrapper.addClass("grid-layout");
			}
			
			else if(theid == "listview") {
				$(this).addClass("active");
				$("#gridview").removeClass("active");
					
				// remove the grid view and change to list
				thewrapper.removeClass("grid-layout")
				thewrapper.addClass("list-layout");

			} 
		}

	});

    $('.panel-all-collapse').collapse({
        toggle: false
    });

	// Initiate Bootstrap Select
	$('.selectpicker').selectpicker();

    // Initiate Bootstrap Checkbox using FontAwesome
    $('input[type="checkbox"]').checkbox({
        checkedClass: 'fa fa-check-square',
        uncheckedClass: 'fa fa-square-o'
    });

    // Initiate Bootstrap File Input
    $('input[type=file]').bootstrapFileInput();

	// Film Strip
    $('#filmstrip').filmstrip({
        interval: 3000
    });

    // Popover Demo
	$('.popover-demo a').popover();
	$('.popover-demo a').on('click', function(e) {e.preventDefault(); return true;});

    // Tooltip
	$('.link-action a').tooltip();
    $('.btn-icon').tooltip();
	$('.social-media a').tooltip();
    $('.filter-gridlist a').tooltip();

	// Initiate Advanced Search
	$('.adv-link').click(function() {
		
		$('.btn-search').toggleClass("switch");

		var $lefty = $('.advanced-search');
		$lefty.animate({
		left: parseInt($lefty.css('left'),10) == 0 ? - $lefty.outerWidth() : 0
		});
		
		return false
	});

    // Toggle Off-Canvas
    $('[data-toggle=offcanvas-sm]').click(function () {
        $('.row-offcanvas-sm').toggleClass('active');
        $('[data-toggle=offcanvas-sm]').toggleClass('active');
        $('.sidebar-offcanvas-sm').toggleClass('active');
    });

    $('[data-toggle=offcanvas]').click(function () {
        $('.site-row.row-offcanvas').toggleClass('active');
        $('[data-toggle=offcanvas]').toggleClass('active');
        $('.sidebar-offcanvas').toggleClass('active');
    });

});