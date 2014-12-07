(function(){
var current=3,
	selected=0,
	pics = $('#slide-pic').children('li'),
	sides = $('#slide-sidebar').children('li'),
	lowerbars = $('#slide-lowerbar').children('li'),
	dropping = 0,
	accel = 45,
	drop_fade_time = 400,
	reveal_time = 600;

for (var i = 0; i < 4; i++) {
	$('#slide-sidebar').children('li').eq(i).data('n', i).data('origin', i);
};

$('#slide-sidebar').children('li').eq(0).css('background-color', 'rgba(0, 0, 0, 0.1)');
$('#slide-sidebar').children('li').eq(1).css('background-color', 'rgba(0, 0, 0, 0.25)');
$('#slide-sidebar').children('li').eq(2).css('background-color', 'rgba(0, 0, 0, 0.5)');
$('#slide-sidebar').children('li').eq(3).css('background-color', 'rgba(0, 0, 0, 0.75)');



function select_slide(){
	pics.eq(current).hide(200);
	pics.eq(selected).show(200);
	lowerbars.eq(current).fadeOut(200);
	lowerbars.eq(selected).fadeIn(200);
	current = selected;
}

function drop_side(n){
	dropping = 1;
	if(n == 0){
		var side0 = $('#slide-sidebar').children('li').eq(1).clone(true)
					.css('height', 0).css('opacity', 0).css('background-color', 'rgba(0, 0, 0, 0.1)'),
			side1 = $('#slide-sidebar').children('li').eq(2).clone(true)
					.css('height', 0).css('opacity', 0).css('background-color', 'rgba(0, 0, 0, 0.25)'),
			side2 = $('#slide-sidebar').children('li').eq(3).clone(true)
					.css('height', 0).css('opacity', 0).css('background-color', 'rgba(0, 0, 0, 0.5)'),
			down1 = $('#slide-sidebar').children('li').eq(1),
			down2 = $('#slide-sidebar').children('li').eq(2),
			down3 = $('#slide-sidebar').children('li').eq(3),
			t = 0.00,
			x = 0.00;

		side0.data('n', 0);
		side1.data('n', 1);
		side2.data('n', 2);
		$('#slide-sidebar').children('li').eq(0).data('n', 3).animate({backgroundColor: 'rgba(0, 0, 0, 0.75)'}, 400);
		down1.css('height', 93).animate({opacity: 0}, drop_fade_time);
		down2.css('height', 93).animate({opacity: 0}, drop_fade_time);
		down3.css('height', 93).animate({opacity: 0}, drop_fade_time);
		$('#slide-sidebar').prepend(side2);
		$('#slide-sidebar').prepend(side1);
		$('#slide-sidebar').prepend(side0);

		var	shrink3 = setInterval(function(){
				t += 0.1;
				x = accel / 3 * t * t
				h = 93 - x;
				if (h < 0) {
					console.log(t);
					clearInterval(shrink3);
					down1.remove();
					down2.remove();
					down3.remove();
					x = 97;
					side0.delay(300).animate({opacity: 1}, reveal_time, function(){dropping = 0});
					side1.delay(150).animate({opacity: 1}, reveal_time);
					side2.delay(0).animate({opacity: 1}, reveal_time);
				}
				down1.css('height', h);
				down2.css('height', h);
				down3.css('height', h);
				side0.css('height', x);
				side1.css('height', x);
				side2.css('height', x);
		}, 10);

	}
	else if(n == 1){
		var side0 = $('#slide-sidebar').children('li').eq(2).clone(true)//continue
					.css('height', 0).css('opacity', 0).css('background-color', 'rgba(0, 0, 0, 0.1)'),
			side1 = $('#slide-sidebar').children('li').eq(3).clone(true)//continue
					.css('height', 0).css('opacity', 0).css('background-color', 'rgba(0, 0, 0, 0.25)'),
			down2 = $('#slide-sidebar').children('li').eq(2),
			down3 = $('#slide-sidebar').children('li').eq(3),
			t = 0.00,
			x = 0.00;

		side0.data('n', 0);
		side1.data('n', 1);
		$('#slide-sidebar').children('li').eq(0).data('n', 2).animate({backgroundColor: 'rgba(0, 0, 0, 0.5)'}, 400);
		$('#slide-sidebar').children('li').eq(1).data('n', 3).animate({backgroundColor: 'rgba(0, 0, 0, 0.75)'}, 400);
		down2.css('height', 93).animate({opacity: 0}, drop_fade_time);
		down3.css('height', 93).animate({opacity: 0}, drop_fade_time);
		$('#slide-sidebar').prepend(side1);
		$('#slide-sidebar').prepend(side0);

		var	shrink3 = setInterval(function(){
				t += 0.1;
				x = accel / 2 * t * t
				h = 93 - x;
				if (h < 0) {
					console.log(t);
					clearInterval(shrink3);
					down2.remove();
					down3.remove();
					x = 97;
					side0.delay(200).animate({opacity: 1}, reveal_time, function(){dropping = 0});
					side1.delay(0).animate({opacity: 1}, reveal_time);
				}
				down2.css('height', h);
				down3.css('height', h);
				side0.css('height', x);
				side1.css('height', x);
		}, 10);
	}
	else if(n == 2){
		var side0 = $('#slide-sidebar').children('li').eq(3).clone(true) // continue
					.css('height', 0).css('opacity', 0).css('background-color', 'rgba(0, 0, 0, 0.1)'),
			down3 = $('#slide-sidebar').children('li').eq(3),
			t = 0.00,
			x = 0.00;

		side0.data('n', 0);
		$('#slide-sidebar').children('li').eq(0).data('n', 1).animate({backgroundColor: 'rgba(0, 0, 0, 0.25)'}, 400);
		$('#slide-sidebar').children('li').eq(1).data('n', 2).animate({backgroundColor: 'rgba(0, 0, 0, 0.5)'}, 400);
		$('#slide-sidebar').children('li').eq(2).data('n', 3).animate({backgroundColor: 'rgba(0, 0, 0, 0.75)'}, 400);
		down3.css('height', 93).animate({opacity: 0}, drop_fade_time);
		$('#slide-sidebar').prepend(side0);

		var	shrink3 = setInterval(function(){
				t += 0.1;
				x = accel * t * t
				h = 93 - x;
				if (h < 0) {
					console.log(t);
					clearInterval(shrink3);
					down3.remove();
					//side0.fadeIn(600);
					x = 97;
					side0.delay(0).animate({opacity: 1}, reveal_time, function(){dropping = 0});
				}
				down3.css('height', h);
				side0.css('height', x);
		}, 10);

	}
}



function sliderTiming () {
	// for pic
	if(current == 0){
		selected = 3;
		select_slide();
		drop_side(2);
	}
	else{
		selected = current - 1;
		select_slide();
		drop_side(2);
	}
}
	
var timingRun = setInterval(function() { sliderTiming(); },3000);

function resetTiming() {
    clearInterval(timingRun);
    timingRun = setInterval(function() { sliderTiming(); },3000);
}

$('.side-list').on('click', function(){
	//console.log($(this).data("n"));
	if(!dropping){
		$this = $(this);
		selected = $this.data('origin');
		resetTiming();
		if($this.data('n') == 3) return;
		setTimeout(function(){
			select_slide();
			drop_side($this.data('n'));
		}, 200);
		resetTiming();
	}
});

var list, ink, d, x, y;
$("#slide-sidebar li").click(function(e) {
	list = $(this);
	if(list.find(".ink").length == 0) list.prepend('<span class = "ink"></span>');

	ink = list.find('.ink');

	ink.removeClass('animate');

	if(!ink.height() && !ink.width()){
		d = Math.max(list.outerWidth(), list.outerHeight());
		ink.css({
			height: d,
			width: d
		});
	}

	x = e.pageX - list.offset().left - ink.width()/2;
	y = e.pageY - list.offset().top - ink.height()/2;

	ink.css({
		top: y + 'px',
		left: x + 'px'
	}).addClass('animate');
});

})();