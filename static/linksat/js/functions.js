$(document).ready(function(){ 
  $('#sliderOne .cBr').click(function() {
  	$('#sliderOne .mCSB_dragger').animate({left: '+=40'+"px"}, 100);
  });
  $('#sliderOne .cBr').click(function() {
    $('#sliderOne .mis-next').click();
  });
});
$(document).ready(function(){ 
  $('#sliderOne .cBl').click(function() {
    $('#sliderOne .mis-prev').click();
  });
  $('#sliderOne .cBr').click(function() {
    $('#sliderOne .mis-next').click();
  });
});
$(document).ready(function(){
	$("#menuIco").toggle(function() {
		$("#navR #hide").slideDown();
	}, function() {
		$("#navR #hide").slideUp();
	});
});
$(document).ready(function(){ 
  $('#navR ul.head li').toggle(function() {
    $(this).addClass('active').find('ul.sec').slideDown(function() {

    });

  }, function() {
	$(this).find('ul.sec').slideUp();
  });
});