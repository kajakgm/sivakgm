
(function() {
    //===== Prealoder
    
    
        /*=====================================
        Sticky
        ======================================= */
        window.onscroll = function () {
            var header_navbar = document.querySelector(".navbar-area");
            var sticky = header_navbar.offsetTop;
    
            if (window.pageYOffset > sticky) {
                header_navbar.classList.add("sticky");
            } else {
                header_navbar.classList.remove("sticky");
            }
    
    
    
            // show or hide the back-top-top button
         
        };
    
        // Get the navbar
    
    
        // for menu scroll 
      

    
    
        // WOW active
        new WOW().init();
    
    
        
        //====== counter up 
        var cu = new counterUp({
            start: 0,
            duration: 2000,
            intvalues: true,
            interval: 100,
            append: " ",
        });
        cu.start();
    
    })();