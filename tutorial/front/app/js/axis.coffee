$( ->
  random = (range) ->
    Math.floor(Math.random() * range)

  data = []
  max_range = Math.random() * 1000
  for i in [0...50]
    data.push([random(max_range), random(max_range)])

  w = 500
  h = 300
  padding = 30
  x_scale = d3.scale.linear()
    .domain([0, d3.max(data, (d) -> d[0])]).range([padding, w - padding * 2])
  y_scale = d3.scale.linear()
    .domain([0, d3.max(data, (d) -> d[1])]).range([h - padding, padding])

  x_axis = d3.svg.axis()
    .scale(x_scale)
    .orient('bottom')
    .ticks(5)

  y_axis = d3.svg.axis()
    .scale(y_scale)
    .orient('left')
    .ticks(5)

  svg = d3.select('.axiss').append('svg').attr({'width': w, 'height': h, })
  svg.selectAll('circle')
    .data(data)
    .enter()
    .append('circle')
    .transition()
    .duration(1000)
    .attr({
      'cx': (d) -> x_scale(d[0]),
      'cy': (d) -> y_scale(d[1]),
      'r': 2,
      'fill': 'red'})


  svg.append('g')
    .attr('class', 'x axis')
    .attr("transform", "translate(0," + (h-padding) + ")")
    .call(x_axis)

  svg.append('g')
    .attr('class', 'y axis')
    .attr("transform", "translate(" + padding + ", 20)")
    .call(y_axis)

  svg.on('click', ->
    nums = data.length
    max_range = Math.random() * 1000
    _data = []
    for i in [0...nums]
      _data.push([random(max_range), random(max_range)])
    console.log _data
    x_scale.domain([0, d3.max(_data, (d) -> d[0])])
    y_scale.domain([0, d3.max(_data, (d) -> d[1])])
    svg.selectAll('circle')
      .data(_data)
      .transition()
      .delay((d,i) -> i / data.length * 1000)
      .each('start', ->
        d3.select(@)
          .attr
            fill: 'magenta'
            r: 3
      )
      .duration(1000)
      .attr(
        'cx': (d) -> x_scale(d[0]),
        'cy': (d) -> y_scale(d[1]),
      )
      .each('end', ->
        d3.select(@)
          .attr
            fill: 'red'
            r: 2
      )
    svg.select('.x.axis').transition().duration(1000).call(x_axis)
    svg.select('.y.axis').transition().duration(1000).call(y_axis)

  )

)
