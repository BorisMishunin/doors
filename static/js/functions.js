$(document).ready(function(){
  $('.bxslider').bxSlider({
  auto: true,
  autoControls: true
  });
    
 $('.good_card').on('click', function(){
      console.log('ddd');
     //alert(this.find('.good-desc').html());
  });
});