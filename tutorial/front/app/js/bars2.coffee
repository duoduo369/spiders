change_bar = (svg, data, h, w, x_scale, y_scale) ->
  _data = []
  max_h = d3.max(data)
  for i in [0...data.length]
    _data.push(Math.floor(Math.random() * max_h))

  svg.selectAll('rect')
    .data(_data)
    .transition()
    .delay((d, i) -> i * 100)
    .duration(5000)
    .ease('elastic')
    .attr(
      height: (d) -> y_scale(d)
      y: (d) -> h - y_scale(d)
    )
  svg.selectAll('text')
    .data(_data)
    .transition()
    .delay((d, i) -> i * 100)
    .ease('linear')
    .text((d) -> d)
    .attr("y", (d) -> h - y_scale(d) + 14)

$(() ->
  data = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13, 11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ]
  w = 600
  h = 250
  bar_padding = 1

  x_scale = d3.scale
    .ordinal()
    .domain(d3.range(data.length))
    .rangeRoundBands([0, w], 0.05)

  y_scale = d3.scale
    .linear()
    .domain([0, d3.max(data)])
    .range([0, h])

  svg = d3.select('.bars2')
    .append('svg')
    .attr({ width: w, height: h, })

  svg.selectAll('rect')
    .data(data)
    .enter()
    .append('rect')
    .transition()
    .duration(5000)
    .ease('elastic')
    .attr(
      width: x_scale.rangeBand(),
      height: (d) -> y_scale(d),
      fill: (d) -> 'rgb(0 ,0, ' + d * 10 +')',
      x: (d, i) -> x_scale(i)
      y: (d) -> h - y_scale(d),
    )
  svg.selectAll('text')
    .data(data)
    .enter()
    .append('text')
    .text((d) -> d)
    .attr("text-anchor", "middle")
    .attr("x", (d, i) -> x_scale(i) + x_scale.rangeBand() / 2
    )
    .attr("y", (d) -> h - y_scale(d) + 14)
    .attr("font-family", "sans-serif")
    .attr("font-size", "11px")
    .attr("fill", "white")
  change_bar(svg, data, h, w, x_scale, y_scale)
  svg.on('click', -> change_bar(svg, data, h, w, x_scale, y_scale))

)
