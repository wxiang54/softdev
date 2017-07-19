window.onload = function () {

    //data format: [<year>, <revenue in trils>, <spending in trils>]
    var myData = [
        {
            "year": 1933,
            "revenue": 0.027,
            "spending": 0.0621
        },
        {
            "year": 2016,
            "revenue": 2.99,
            "spending": 3.54
        }
];

    var wrapper = d3.select(".chart")
        .selectAll("div")
        .data(myData)
        .enter()
        .append("div").classed("bar-wrapper", true);

    wrapper.append("div").classed("bar-left", true)
        .style("height", function (d) {
            return 50 * d["revenue"] + 10 + "px";
        })
        .text(function (d) {
            return "$" + d["revenue"];
        });

    wrapper.append("div").classed("bar-right", true)
        .style("height", function (d) {
            return 50 * d["spending"] + 10 + "px";
        })
        .text(function (d) {
            return "$" + d["spending"];
        });

    wrapper.append("label")
        .text(function (d) {
            return d["year"];
        });


    var trans = function (mult, dur) {
        var wrapper = d3.select(".chart")
            .data(myData)
            .transition()
            .duration(dur)
            .selectAll(".bar-wrapper");

        wrapper.selectAll(".bar-left")
            .style("height", function (d) {
                return mult * (50 * d["revenue"] + 10) + "px";
            });


        wrapper.selectAll(".bar-right")
            .style("height", function (d) {
                return mult * (50 * d["spending"] + 10) + "px";
            });
    };

    document.getElementById("trans")
        .addEventListener("click", function() {
            trans( 
                document.getElementById("scale").value, document.getElementById("dur").value
            );
    });

    /*

    var r2 = d3.selectAll("#r2");
    var r2Update = r2.selectAll("td").data(yr2).enter().append("td");
    r2Update.text(function (d) {
        return d;
    });


    var tab = d3.selectAll(".tab");

    var tableGrow = function (m, dur) {

        tab.selectAll("th")
            .transition()
            .duration(dur)
            .style("font-size", function () {
                return m * 16 + "px";
            });

        r1
            .data(yr1)
            .transition()
            .duration(dur)
            .style("font-size", function () {
                return m * 16 + "px";
            });

        r2
            .data(yr2)
            .transition()
            .duration(dur)
            .style("font-size", function () {
                return m * 16 + "px";
            });

    };

    var activTabGrow = function () {
        var scale = document.getElementById("scale").value;
        var dur = document.getElementById("dur").value;
        tableGrow(scale, dur);
    }

 document.getElementById("tab_grow").addEventListener("click", activTabGrow);
*/

}