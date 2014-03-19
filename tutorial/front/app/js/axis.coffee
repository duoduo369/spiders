$( ->
    random = (range) ->
      Math.floor(Math.random() * range)

    data = []
    x_range = Math.random() * 1000
    y_range = Math.random() * 1000
    for i in [0...50]
      data.push([random(x_range), random(y_range)])

    w = 500
    h = 200
    console.log data
    xscale = d3.scale.linear().domain([0, 1000]).range([0, w])
    yscale = d3.scale.linear().domain([0, 1000]).range([h, 0])
    svg = d3.select('.axiss').append('svg').attr({'width': w, 'height': h, })
    svg.selectAll('circle')
       .data(data)
       .enter()
       .append('circle')
       .attr({
         'cx': (d) -> xscale(d[0]),
         'cy': (d) -> yscale(d[1]),
         'r': 10,
         'fill': 'red'})

    x_axis = d3.svg.axis()
                .scale(xscale)
                .orient('bottom')

    y_axis = d3.svg.axis()
                .scale(yscale)
                .orient('left')
                .ticks(5)

    svg.append('g')
       .attr('class', 'axis')
       .attr("transform", "translate(30," + (h-20) + ")")
       .call(x_axis)

    svg.append('g')
       .attr('class', 'axis')
       .attr("transform", "translate(30, -20)")
       .call(y_axis)


)
