var pic, clear, move, lineType;
var intervalID;
var height, width;
window.onload = function() {
    pic = document.getElementById("vimage");
    pic.addEventListener("click", drawCircle, true); //allow capture
    
    clear = document.getElementById("clear");
    clear.addEventListener("click", clearSVG);
    
    movepause = document.getElementById("movepause");
    movepause.addEventListener("click", animate);

    lineType = document.getElementById("lineType");	
    lineType.addEventListener("change", drawLine);
    
    height = pic.height.baseVal.value;
    width = pic.width.baseVal.value;
    drawLine(window.onload);
};

var getCircle = function(cx, cy, r) {
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", cx);
    c.setAttribute("cy", cy);
    c.setAttribute("r", r);
    c.setAttribute("fill", "blue");
    c.setAttribute("stroke", "black");
    c.setAttribute("stroke-width", 2);
    c.setAttribute("inSplitZone", false);
    
    var velocity = 1;
    var theta = Math.random() * 2 * Math.PI;
    c.setAttribute("dx", velocity * Math.cos(theta));
    c.setAttribute("dy", velocity * Math.sin(theta));
    
    //stage 0: blue, next click turns red
    //stage 1: red, next click makes it disappear
    c.setAttribute("state", 0);

    c.addEventListener("click", changeCircle);
    return c;
};

var getLine = function(x1, y1, x2, y2) {
    var l = document.createElementNS("http://www.w3.org/2000/svg", "line");
    l.setAttribute("x1", x1);
    l.setAttribute("y1", y1);
    l.setAttribute("x2", x2);
    l.setAttribute("y2", y2);
    l.setAttribute("stroke", "rgba(0, 0, 0, 0)");
    
    //graphics stuff
    l.setAttribute("A", y2-y1);
    l.setAttribute("B", x1-x2);
    l.setAttribute("C", (x2-x1) * (y1 - (y2-y1)/(x2-x1)*x1));
    console.log("A: " + (y2-y1));
    console.log("B: " + (x1-x2));
    console.log("C: " + ((x2-x1) * (y1 - (y2-y1)/(x2-x1)*x1)));
    return l;
}


var drawCircle = function(e) {
    if (this === e.target) {
	pic.append( getCircle(e.offsetX, e.offsetY, 25) );
    }
    
    //assume a circle is clicked
    else if (e.target.getAttribute("state") == 1) {
	pic.append( getCircle(Math.random() * width, Math.random() * height, 25) );
    }
};

var changeCircle = function(e) {
    if (this.getAttribute("state") == 0) {
	this.setAttribute("fill", "red");
	this.setAttribute("state", 1);
    }
    else {
	this.remove();
    }
    e.stopPropagation();
};

var splitCircle = function(c1) {
    var r = parseInt(c1.getAttribute("r"));
    if (r <= 2) c1.remove();
    
    var cx = parseFloat(c1.getAttribute("cx"));
    var cy = parseFloat(c1.getAttribute("cy"));
    var dx = parseFloat(c1.getAttribute("dx"));
    var dy = parseFloat(c1.getAttribute("dy"));
    var fill = c1.getAttribute("fill");
    c1.setAttribute("r", r/2);
    
    var c2 = getCircle(cx, cy, r/2);
    c2.setAttribute("dx", -dx);
    c2.setAttribute("dy", -dy);
    c2.setAttribute("fill", fill);
    c2.setAttribute("inSplitZone", true);
    pic.append(c2);
};

var isPointOnLine = function(px, py, line) {
    var A = parseFloat(line.getAttribute("A"));
    var B = parseFloat(line.getAttribute("B"));
    var C = parseFloat(line.getAttribute("C"));
    var threshold = 1000;
    if (isFinite(C)) {
	return Math.abs(A*px + B*py + C) < threshold; //boolean
    }
    return Math.abs(px - line.getAttribute("x1")) < 1; //boolean
};

var drawLine = function(e) {
    //assume one line only
    if (pic.getElementsByTagName("line").length)
	pic.getElementsByTagName("line")[0].remove();
    if (lineType.value == "lil_uzi") {
	pic.append( getLine(width/2, 0, width/2, height) );
    }
    else if (lineType.value == "ontal") {
	pic.append( getLine(0, height/2, width, height/2) );
    }
    else if (lineType.value == "knockturn") {
	pic.append( getLine(0, 0, width, height) );
    }
    else if (lineType.value == "random") {
	pic.append( getLine(Math.random()*width, Math.random()*height, Math.random()*width, Math.random()*height) );
    }
};

var animate = function(e) {
    drawLine();
    movepause.removeEventListener("click", animate);
    movepause.addEventListener("click", pauseAnimation);
    movepause.textContent = "Pause";
    
    intervalID = setInterval( function() {
	var circles = pic.getElementsByTagName("circle");
	for (var i = 0, len = circles.length; i < len; i++) {
	    var circ = circles[i];
	    var cx = parseFloat( circ.getAttribute("cx") );
	    var cy = parseFloat( circ.getAttribute("cy") );
	    var r = parseInt( circ.getAttribute("r") );
	    var dx = parseFloat( circ.getAttribute("dx") );
	    var dy = parseFloat( circ.getAttribute("dy") );
	    
	    if ( (cx - r) <= 0 || (cx + r) >= width ) { 
		dx = -dx;
	    }
	    else if ( (cy - r) <= 0 || (cy + r) >= height ) {
		dy = -dy;
	    }

	    var inSplitZone = circ.getAttribute("inSplitZone") == "true";

	    //assume one line
	    var line = pic.getElementsByTagName("line")[0];
	    
	    if (isPointOnLine(cx, cy, line)) {
		if (! inSplitZone) {
		    splitCircle(circ);
		    circ.setAttribute("inSplitZone", true);
		}
	    }
	    else {
		if ( inSplitZone )
		    circ.setAttribute("inSplitZone", false);
	    }

	    circ.setAttribute("cx", cx + dx);
	    circ.setAttribute("cy", cy + dy);
	    circ.setAttribute("dx", dx);
	    circ.setAttribute("dy", dy);
	}
    }, 15)
};

var pauseAnimation = function(e) {
    clearInterval(intervalID);
    movepause.removeEventListener("click", pauseAnimation);
    movepause.addEventListener("click", animate);
    movepause.textContent = "Move";
};


var clearSVG = function(e) {
    while (pic.children.length) {
	pic.removeChild(pic.lastChild);
    }
    prevNodeX = prevNodeY = -1;
};
