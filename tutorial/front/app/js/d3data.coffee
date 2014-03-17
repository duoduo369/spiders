$( ->
  data = (Math.floor(Math.random() * 30) for i in [1..20])
  d3.select('.d3data').selectAll('div')
    .data(data)
    .enter()
    .append('div')
    .attr('class', 'bar')
    .style('height', (d) -> d*5 + 'px')
    .text((d) -> d)

)
