var pic, clear;
var prevNodeX, prevNodeY;

window.onload = function() {
    pic = document.getElementById("vimage");
    pic.addEventListener("click", addNode);
    clear = document.getElementById("clear");
    clear.addEventListener("click", clearSVG);

    prevNodeX = prevNodeY = -1;
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

var clearSVG = function(e) {
    while (pic.childNodes.length) {
	pic.removeChild(pic.lastChild);
    }
    prevNodeX = prevNodeY = -1;x
}
