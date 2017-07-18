var pic, clear, pause;
//var prevNodeX, prevNodeY;
var state; //0: expanding, 1: contracting
var animation;
var height, width;

window.onload = function() {
    pic = document.getElementById("vimage");
    pic.addEventListener("click", animate);
    clear = document.getElementById("clear");
    clear.addEventListener("click", clearSVG);
    pause = document.getElementById("pause");
    pause.addEventListener("pause", pauseAnimation);
    //    prevNodeX = prevNodeY = -1;
    state = 0;
    height = pic.height.baseVal.value;
    width = pic.width.baseVal.value;
}

var drawCircle = function(cx, cy, r) {
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", cx);
    c.setAttribute("cy", cy);
    c.setAttribute("r", r);
    c.setAttribute("fill", "blue");
    c.setAttribute("stroke", "black");
    c.setAttribute("stroke-width", 2);
    pic.appendChild(c);
}

/*
var drawLine = function(x1, y1, x2, y2) {
    var c = document.createElementNS("http://www.w3.org/2000/svg", "line");
    c.setAttribute("x1", x1);
    c.setAttribute("y1", y1);
    c.setAttribute("x2", x2);
    c.setAttribute("y2", y2);
    c.setAttribute("stroke", "black");
    c.setAttribute("stroke-width", 2);
    pic.appendChild(c);
}

var addNode = function(e) {
    var curNodeX = e.offsetX;
    var curNodeY = e.offsetY;
    if (prevNodeX >= 0 && prevNodeY >= 0) {
	drawLine( prevNodeX, prevNodeY, curNodeX, curNodeY );
	drawCircle( prevNodeX, prevNodeY, 25 ); //triggered
    }
    drawCircle( curNodeX, curNodeY, 25 );
    prevNodeX = curNodeX;
    prevNodeY = curNodeY;
}
*/

var animate = function(e) {
    var radius = 0;
    pauseAnimation(e);
    clearSVG(e);
    animation = setInterval( function() {
	if (state == 0) { //expanding
	    drawCircle(width/2, height/2, radius);
	    radius++;
	    if (radius >= height/2) {
		state = 1;
		radius = 0;
	    }
	}
	else { //contracting
	    pic.removeChild(pic.lastChild);
	    if (pic.children.length == 0) {
		state = 0;
	    }
	}
    }, 10)
}

var pauseAnimation = function(e) {
    clearInterval(animation);
}

var clearSVG = function(e) {
    while (pic.children.length) {
	pic.removeChild(pic.lastChild);
    }
    prevNodeX = prevNodeY = -1;
}

window.onload = function() {
    pic = document.getElementById("vimage");
    pic.addEventListener("click", animate);
    clear = document.getElementById("clear");
    clear.addEventListener("click", clearSVG);
    pause = document.getElementById("pause");
    pause.addEventListener("click", pauseAnimation);
    //    prevNodeX = prevNodeY = -1;
    state = 0;
    height = pic.height.baseVal.value;
    width = pic.width.baseVal.value;
}
