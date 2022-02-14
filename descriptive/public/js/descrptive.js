  $.fn.isInViewport = function() {
    var elementTop = $(this).offset().top;
    var elementBottom = elementTop + $(this).outerHeight();
    var viewportTop = $(window).scrollTop();
    var viewportBottom = viewportTop + $(window).height();
  
    return elementBottom > viewportTop && elementTop < viewportBottom;
  };



$(document).ready(function(){



 $('.descrptive-section h2').addClass('animate__fadeInUp');
 $('.descrptive-section p').addClass('animate__fadeInUp');
 $('.descrptive-section a').addClass('animate__backInUp');

  
  $('.ctabtn').click(function(){
      var activeFormid = $(this).parents('.chkform').data('id');
      var nextFormid = activeFormid + 1;
      var preFormid = activeFormid - 1;
      if(nextFormid == 7){
        $('.progessbar').addClass('hide');
        $('.cctext').addClass('hide');
      }
      $('.progessbar [data-process='+activeFormid+']').addClass('active verify');
      $('.progessbar [data-process='+nextFormid+']').addClass('active');
     $('.chkout .containerbox,.checkout .chkform').removeClass('showFlex');
     $('.chkout .step'+nextFormid+'Left.containerbox,.checkout .step'+nextFormid+'Right.chkform').addClass('showFlex');


  })

  $('.progess_dots').click(function(){
    var clickActive = $(this).data('process');
    processClick(clickActive);
  })
  
  
  $('.testimonial-slider').slick({
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    speed: 300,
    arrows: true,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          arrows: false,
        }
      },
      {
        breakpoint: 600,
        settings: {
          arrows: false,
        }
      },
      {
        breakpoint: 480,
        settings: {
          arrows: false,
        }
      }
    ]
  });

  
  $(window).scroll(function(event){
    var st = $(this).scrollTop();
    scrPercentage = (st * 2.5 /100);
    offX = 0,offY=0;
    one = 45;
    two = 45;
    three =70;
    
    if(st < 50) 
      $('.menu_wrapper').addClass('invert');
    else
      $('.menu_wrapper').removeClass('invert');

      if(st > 0 && st < 700){
        
        $('.allboxImg .box-sm-img.one').css('top',(one+scrPercentage)+'%');
        $('.allboxImg .box-sm-img.two').css('top',(two+scrPercentage)+'%');
        $('.allboxImg .box-sm-img.three').css('bottom',(three+scrPercentage)+'px');
        
      }
   
  });

  $('.dropdown .navlink').click(function(){
      $(this).parent().toggleClass('open');
  })  
  $('.hamburgermenu_icon').click(function(){
    $('body').toggleClass('oh');
    $(this).toggleClass('open');
    $('.navigation').toggleClass('open');
  });

  


});

function processClick(clickActive){
  $('.chkout .containerbox,.checkout .chkform').removeClass('showFlex');
  $('.chkout .step'+clickActive+'Left.containerbox,.checkout .step'+clickActive+'Right.chkform').addClass('showFlex');
}

var wwidth = $(window).width();
$(window).scroll(function(){
  if($('body').hasClass('home-landing')){
    if(wwidth > 1025){
      if($('.serviceblock').isInViewport()){
        $('.serviceblock').addClass('animate__fadeInUp');
        $('.hero-text').addClass('animate__fadeInBottomLeft');
      }else if($('.partnerlogo').isInViewport()){
        $('.partnerlogo').addClass('animate__fadeIn');
      }else if($('.industry-box').isInViewport()){
        $('.industry-type').addClass('animate__fadeInLeft');
        $('.circle-menu').addClass('animate__fadeIn');
      }else if($('.bg-experties').isInViewport()){
        $('.experties-container-left').addClass('animate__fadeInLeft');
        $('.experties-container-right').addClass('animate__fadeInRight');
      }else if($('.serviceblock-section').isInViewport()){
        $('.serviceblock-section').addClass('animate__fadeInUp');
      }else if($('.subfooter').isInViewport()){
        $('.col-50').addClass('animate__fadeInLeft');
        $('.col-50.ds').addClass('animate__fadeInRight');
      }
    }
  }
})