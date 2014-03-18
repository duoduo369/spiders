$( ->
    data = [32, 57, 112]
    w = 360
    h = 180
    x = d3.scale.ordinal().domain([57, 32, 112]).rangePoints([0, w], 1)
    y = d3.scale.ordinal().domain(data).rangePoints([0, h], 2)

    svg = d3.select('.circles').append('svg')
      .attr('width', w).attr('height', h)

    svg.selectAll('.little').data(data)
      .enter().append('circle')
      .attr('class', 'little')
      .attr('cx', x)
      .attr('cy', y)
      .attr('r', 12)

    svg.on("mouseenter", ->
      svg.selectAll('.select').remove()

      svg.selectAll('.select').data(data)
        .enter().append('circle')
        .attr('class', 'select')
        .attr('cx', x)
        .attr('cy', y)
        .attr('r', 60)
        .style('fill', 'none')
        .style('stroke', 'red')
        .style('stroke-opacity', '1e-6')
        .style('stroke-width', '3')
        .transition()
          .duration(750)
          .attr('r', 12)
          .style('stroke-opacity', '1')
    )
)
