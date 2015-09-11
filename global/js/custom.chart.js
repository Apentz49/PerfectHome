$(document).ready(function () {

//-- FLOT Chart -- //
	
	// Bar Chart
	$(function () {
		
        var data = [[0, 16],[1, 14],[2, 12],[3, 12],[4, 11],[5, 10]];
        var dataset = [{ label: "Price in '00,000' ($)", data: data, color: "#e74c3c" }];
        var ticks = [[0, "Bungalow"], [1, "Semi-Detached"], [2, "Linked / Terrace"], [3, "Town House"],[4, "Condominium"], [5, "Apartment"]];
 
        var options = {
            series: {
                bars: {
                    show: true
                }
            },
            bars: {
                align: "center",
                barWidth: 0.6
            },
            xaxis: {
                axisLabel: "Type of Property",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 14,
                //axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 10,
                ticks: ticks
            },
            yaxis: {
                axisLabel: "($)",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 14,
                //axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 3,
                tickFormatter: function (v, axis) {
                   return "$" + v;
                }
            },
            legend: {
                noColumns: 0,
                labelBoxBorderColor: "#f1f2f2",
                position: "nw"
            },
            grid: {
                hoverable: true,
                borderWidth: 0,
                backgroundColor: { colors: ["#f1f2f2", "#f9f9f9"] }
            }
        };
 
        function gd(year, month, day) {
            return new Date(year, month, day).getTime();
        }
 
        var previousPoint = null, previousLabel = null;
 
        $.fn.UseTooltip = function () {
            $(this).bind("plothover", function (event, pos, item) {
                if (item) {
                    if ((previousLabel != item.series.label) || (previousPoint != item.dataIndex)) {
                        previousPoint = item.dataIndex;
                        previousLabel = item.series.label;
                        $("#tooltip").remove();
 
                        var x = item.datapoint[0];
                        var y = item.datapoint[1];
 
                        var color = item.series.color;
 
                        //console.log(item.series.xaxis.ticks[x].label);               
 
                        showTooltip(item.pageX,
                        item.pageY,
                        color,
                        "<strong>Average Price ($)</strong><br>" + item.series.xaxis.ticks[x].label + " : <strong>$" + y + "</strong>0,000");
                    }
                } else {
                    $("#tooltip").remove();
                    previousPoint = null;
                }
            });
        };
 
        function showTooltip(x, y, color, contents) {
            $('<div id="tooltip">' + contents + '</div>').css({
                position: 'absolute',
                display: 'none',
                top: y - 70,
                left: x - 80,
               // border: '1px solid ' + color,
                padding: '8px',
                color: '#fff',
                'font-size': '14px',
                'border-radius': '3px',
                'background-color': 'rgba(0,0,0,.6)',
               // 'font-family': 'Verdana, Arial, Helvetica, Tahoma, sans-serif',
            }).appendTo("body").fadeIn(200);
        }

        $.plot($("#flot-placeholder"), dataset, options);
        $("#flot-placeholder").UseTooltip();

	});

});