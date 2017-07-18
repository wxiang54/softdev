//to know what to switch back on mouseout
var header_inital = document.getElementById("h").innerHTML;

//fxn to change header
var changeHead = function (text) {
    var header = document.getElementById("h");
    header.innerHTML = text;
};

var addItem = function (n) {
    var newitem = document.createElement("li");
    var list;
    if (typeof n == 'undefined') {
	newitem.innerHTML = "new thing!";
	list = document.getElementById("thelist");
    } else {
	newitem.innerHTML = n;
	list = document.getElementById("fiblist");
    }
    addListEventListeners(newitem);
    list.appendChild(newitem);
};

//helper fxn to add event listeners to list item
var addListEventListeners = function (target) {
    target.addEventListener(
        "mouseover",
        function () {
            changeHead(this.innerHTML);
        }
    );

    target.addEventListener(
        "mouseout",
        function () {
            changeHead(header_inital);
        }
    );

    target.addEventListener(
        "click",
        function () {
            this.remove();
        }
    );
}

var fib = function(n) {
    var term1 = 0;
    var term2 = 1;
    while (n > 0) {
	var tmp = term2;
	term2 += term1;
	term1 = tmp;
	n--;
    }
    return term1;
}

var button = document.getElementById("b1"); //add item button
button.addEventListener(
    "click", 
    function() {
	addItem();
    }
);

button = document.getElementById("b2"); //fib button
button.addEventListener(
    "click", 
    function() {
	var seq = document.getElementById("fiblist");
	addItem( fib( seq.childElementCount ) );
    }
);

var items = document.getElementById("thelist").getElementsByTagName("li");
for (var i = 0; i < items.length; i++) {
    addListEventListeners(items[i]);
};
