var mouseX, mouseY;
var reset = false;

window.onload = function() {
    var c = document.getElementById("slate");
    c.addEventListener("click", addNode);

    var b = document.getElementById("clear");
    b.addEventListener("click", clearCanvas);
};

/*************************************
            HOMEWORK 5
*************************************/
var drawRect = function(e) {
    var ctx = this.getContext("2d");
    ctx.fillStyle = 	
'#'+Math.floor(Math.random()*16777215).toString(16);
    ctx.fillRect(e.offsetX, e.offsetY, 100, 200);
    console.log(e.offsetX);
    console.log(e.offsetY);
}

/*************************************
            HOMEWORK 6
*************************************/
var addNode = function(e) {
    var ctx = this.getContext("2d");
    //ctx.globalAlpha = 1;
    drawLine(ctx, e.offsetX, e.offsetY);
    
    if (!reset) { //draw the old circle again
        ctx.beginPath();
        drawCircle(ctx, mouseX, mouseY, 20);
    }
    reset = false;
      
    mouseX = e.offsetX;
    mouseY = e.offsetY;
    ctx.beginPath();
    drawCircle(ctx, mouseX, mouseY, 20);
}
 
var drawLine = function(ctx, x, y) {
    ctx.lineTo(x, y);
    ctx.stroke();
}

var drawCircle = function(ctx, x, y, radius) {
    ctx.fillStyle = "#00F"
    ctx.arc(x, y, 20, 0, 2*Math.PI);
    ctx.fill();
    ctx.stroke();
    ctx.moveTo(mouseX, mouseY);
}

var clearCanvas = function(e) {
    var c = document.getElementById("slate");
    var ctx = c.getContext("2d");
    ctx.fillStyle = "#FFF";
    ctx.clearRect(0, 0, c.width, c.height);
    ctx.beginPath();
    reset = true;
}
