$( ->
    data = (Math.floor(Math.random() * 30) for i in [1..20])
    w = 500
    h = 200
    xscale = d3.scale.linear().domain([0, 30]).range([0, 500])
    yscale = d3.scale.linear().domain([0, 900]).range([0, 200])
    svg = d3.select('.axiss').append('svg').attr({'width': w, 'height': h, })
    svg.selectAll('circle')
       .data(data)
       .enter()
       .append('circle')
       .attr({
         'cx': (d) -> xscale(d),
         'cy': (d) -> yscale(d * Math.floor(Math.random() * 30)),
         'r': 10,
         'fill': 'red'})

    x_axis = d3.svg.axis()
                .scale(xscale)
                .orient('bottom')
    svg.append('g')
       .attr('class', 'axis')
       .attr("transform", "translate(0," + (h - 30) + ")")
       .call(x_axis)


)
