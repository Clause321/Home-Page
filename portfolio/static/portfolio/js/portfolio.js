(function(){
	var cats = $('.catlog_x'),
		cat_w = $('#catlog_w'),
		catlog = $('#catlog'),
		$window = $(window),
       	elTop = catlog.offset().top,
       	progress = $('#progress_bar'),
       	el2Top = progress.offset().top,
       	el2Height = progress.height(),
       	state = 0,
       	$this;
       	
    $(".progress_pic img").each(function(){
        $this = $(this);
        $this.width($this.width() * 0.12);
        $this.css({left: (76 - $this.width()) / 2});
    });

    cats.each(function(index) {
    	 /* iterate through array or object */
    	 $(this).data("width", $(this).find('.catlog_middle').width());
    });
    
    $("#progress_long_bar").draggable ({
    	axis: "x",
    	containment: "parent",
    	//cursor: "-webkit-grabbing"
    });

    $("#progress_long_bar").mousedown(function(){ $(this).addClass('grabbing')});
    $('#progress_long_bar').mouseup(function(){ $(this).removeClass('grabbing')});

    // FIXING
    $window.scroll(function() {
        catlog.toggleClass('unfixed', $window.scrollTop() < elTop);
        catlog.toggleClass('fixed', $window.scrollTop() > elTop);
        progress.toggleClass('unfixed', $window.scrollTop() + $window.height() > el2Top + el2Height);
        progress.toggleClass('fixed', $window.scrollTop() + $window.height() < el2Top + el2Height);
        $("#progress_long_bar").css({
        	top: '0'
        });
    });

    // CATLOG
	catlog.on('mouseenter', function(event) {
		event.preventDefault();
		/* Act on the event */
		cat_w.stop(true, false).animate({opacity: 0}, 450);
		catlog.stop(true, false).animate({width: 198}, 300, "easeInOutQuart", function(){
			s = 2;
			cats.each(function(index) {
			 /* iterate through array or object */
			 $(this).stop(true, false).delay(index * 60).animate({opacity: 1}, 500);
			});
		})
	});

	catlog.on('mouseleave', function(event) {
		event.preventDefault();
		/* Act on the event */
		state = 0;
		cat_w.stop(true, false).animate({opacity: 1}, 800);
		catlog.stop(true, false).animate({width: 128}, 300, "easeInOutQuart", function(){
			s = 1;
		})
		cats.each(function(index) {
			 /* iterate through array or object */
			 $(this).stop(true, false).delay((2 - index) * 80).animate({opacity: 0}, 300);
		});
	});

	cats.on('mouseenter', function(event) {
		event.preventDefault();
		/* Act on the event */
		$this = $(this);
		if(state == 0){
			$this.find(".catlog_middle").stop(true, false).animate({width: "120px"});
			$this.children(".catlog_wrapper").stop(true, false)
				.animate({zoom: 1.2, fontWeight:'bold', color: "#000"}, 300);
		}
		else $this.children(".catlog_wrapper").stop(true, false)
				.animate({fontWeight:'bold', color: "#000"}, 300);
	});

	cats.on('mouseleave', function(event) {
		event.preventDefault();
		/* Act on the event */
		$this = $(this);
		//$this.find(".catlog_middle").filter(':not(:animated)').removeClass('catlog_bigger', 300);
		if(state == 0)
			$this.find(".catlog_middle").stop(true, false).animate({width: $this.data("width")}, 300);
		$this.children(".catlog_wrapper").stop(true, false)
			.animate({zoom: 1, color: "rgba(0, 0, 0, 0.4)"}, 300);
	});

	// JUMP
	$('.catlog_wrapper').on('click', function(event){
		event.preventDefault();
		/* Act on the event */
		state = 1;
	    $('html, body').animate({
	        scrollTop: $( $(this).attr('href') ).offset().top
	    }, 500, "easeInOutQuart");

	    cat_w.stop(true, false).animate({opacity: 1}, 800);
		catlog.stop(true, false).animate({width: 128}, 250, "easeInOutQuart", function(){
			s = 1;
		});

		$this.find(".catlog_middle").stop(true, false).animate({width: $this.data("width")}, 300);
		$this.children(".catlog_wrapper").stop(true, false)
			.animate({zoom: 1}, 260);

	    return false;
	});

	// TREE
	$('.real_tree').on('click', function(event){
		event.preventDefault();
		/* Act on the event */
		$('html, body').animate({
	        scrollTop: $( $(this).attr('href') ).offset().top
	    }, 500, "easeInOutQuart");
	});

	$('.real_tree').on('mouseenter', function(event){
		event.preventDefault();
		/* Act on the event */
		$(this).find('.progress_balloon').show();
	});

	$('.real_tree').on('mouseleave', function(event){
		event.preventDefault();
		/* Act on the event */
		$(this).find('.progress_balloon').hide();
	});
})();