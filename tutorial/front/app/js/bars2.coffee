$(
  ->
   data = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13, 11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ]
   w = 600
   h = 250
   bar_padding = 1

   x_scale = d3.scale
               .ordinal()
               .domain(d3.range(data.length))
               .rangeRoundBands([0, w], 0.05)

   svg = d3.select('.bars2')
           .append('svg')
           .attr({ width: w, height: h, })

   svg.selectAll('rect')
      .data(data)
      .enter()
      .append('rect')
      .attr(
        width: x_scale.rangeBand(),
        height: (d) -> 4 * d,
        fill: (d) -> 'rgb(0 ,0, ' + d * 10 +')',
        x: (d, i) -> (w / data.length + 1) * i,
        y: (d) -> h - 4 * d,
      )
   svg.selectAll('text')
      .data(data)
      .enter()
      .append('text')
      .text((d) -> d)
      .attr("text-anchor", "middle")
      .attr("x", (d, i) ->
          i * (w / data.length + 1) + (w / data.length) / 2
      )
      .attr("y", (d) -> h - (d * 4) + 14)
      .attr("font-family", "sans-serif")
      .attr("font-size", "11px")
      .attr("fill", "white")

)
