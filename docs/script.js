
//------------------------------//
// CODE FOR SCROLLYTELLING BELOW//
//------------------------------//


var scrolly = d3.select("#scrolly__section");
var chart = scrolly.select(".scrolly__chart");
var content = scrolly.select(".scrolly__content");
var step = content.selectAll(".step");

// initialize the scrollama
var scroller = scrollama();

// generic window resize listener event
  function handleResize() {
    // 1. update height of step elements
    var stepH = Math.floor(window.innerHeight * 1);
    step.style("height", stepH + "px");

    var figureHeight = window.innerHeight * 0.75;
    var figureMarginTop = (window.innerHeight - figureHeight) / 2;

    chart
      .style("height", figureHeight + "px")
      .style("top", figureMarginTop + "px");

    // 3. tell scrollama to update new element dimensions
    scroller.resize();
  }

  // set the default story ID (Delhi)
  let storyId = 1724565;

  // Check which HTML file is being loaded and set the story ID accordingly
  if (window.location.href.indexOf("bogota.html") >= 0) {
      storyId = 1762941;
  } else if (window.location.href.indexOf("jakarta.html") >= 0) {
      storyId = 1764236;
  } else if (window.location.href.indexOf("lagos.html") >= 0) {
      storyId = 1764230;
  }

  // scrollama event handlers
  function handleStepEnter(response) {
    const textblock = step.select(".text-block");

    // add color to current step only
    textblock.classed("is-active", function(d, i) {
      return i === response.index;
    });

    // update graphic based on step
    const linkHead = `https://flo.uri.sh/story/${storyId}/embed#slide-`;
    const slide = response.index
    
    d3.select('.scrolly__chart iframe')
      .attr('src', linkHead + slide);
  }

  function setupStickyfill() {
    d3.selectAll(".sticky").each(function() {
      Stickyfill.add(this);
    });
  }

  function init() {
    setupStickyfill();
    handleResize();
    scroller
      .setup({
        step: "#scrolly__section .scrolly__content .step",
        offset: 0.6,
        // Change this variable to true to enable guidelines lines
        debug: false
      })
      .onStepEnter(handleStepEnter);

    // setup resize event
    window.addEventListener("resize", handleResize);
  }



//-------------------------------//
// CODE FOR SCROLL POSITION BELOW//
//-------------------------------//


// Save the user's scroll position when they scroll the page
window.addEventListener('scroll', function() {
    var scrollPosition = window.scrollY;
    localStorage.setItem('scrollPosition', scrollPosition);
  });
  
  // Restore the user's scroll position when the page loads
  var savedScrollPosition = localStorage.getItem('scrollPosition');
  if (savedScrollPosition) {
    window.scrollTo(0, savedScrollPosition);
  }
  

//---------------------------//
// CODE FOR BACK TO TOP BELOW//
//---------------------------//


// Get a reference to the "Back to top" button
// var backToTopButton = document.getElementById("back-to-top");
var backToTopButton = document.getElementById("back-to-top-arrow");
 
// When the user scrolls down 200px from the top of the document, show the button
window.onscroll = function() {
  if (document.body.scrollTop > 1000 || document.documentElement.scrollTop > 1000) {
    backToTopButton.style.display = "block";
  } else {
    backToTopButton.style.display = "none";
  }
};

// When the user clicks on the button, scroll to the top of the document
backToTopButton.onclick = function() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
};



//-------------------------------//
// CODE FOR COMMON ELEMENTS BELOW//
//-------------------------------//

// Fetch the common content from the "common_header.html" file
fetch("common_header.html")
  .then(response => response.text())
  .then(html => {
    // Insert the common content into the "common_header" element
    document.getElementById("common_header").innerHTML = html;
  });
  

// Fetch the common content from the "common_intro.html" file
fetch("common_intro.html")
  .then(response => response.text())
  .then(html => {
    // Insert the common content into the "common_intro" element
    document.getElementById("common_intro").innerHTML = html;
  });


  // Fetch the common content from the "common_footer.html" file
fetch("common_footer.html")
.then(response => response.text())
.then(html => {
  // Insert the common content into the "common_footer" element
  document.getElementById("common_footer").innerHTML = html;
});

  // Fetch the common content from the "common_conclusion.html" file
fetch("common_conclusion.html")
.then(response => response.text())
.then(html => {
  // Insert the common content into the "common_conclusion" element
  document.getElementById("common_conclusion").innerHTML = html;
});


  init();
      
   