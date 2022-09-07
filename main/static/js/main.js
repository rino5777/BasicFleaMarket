


(function($) {                                    // Используем $ в качестве имени переменной
    $.fn.accordion = function (speed) {        // Возвращает выборку jQuery
      this.on('click', '.accordion-control', function (e) {
        e.preventDefault();
        $(this)
          .next('.accordion-panel')
          .not(':animated')
          .slideToggle(speed);
      });
      return this;                                 // Возвращаем выборку jQuery
    };
  }(jQuery));    





  $( "id.menu" ).on({
    click: function() {
      $( this ).toggleClass( "active" );
    }, mouseenter: function() {
      $( this ).addClass( "inside" );
    }, mouseleave: function() {
      $( this ).removeClass( "inside" );
    }
  });