$( ->
    w = 500
    data = (i for i in [5...30] by 5)
    h = 50
    svg = d3.select('.circles2')
            .append('svg')
            .attr('width', w)
            .attr('height', h)

    svg.selectAll('circle')
       .data(data)
       .enter()
       .append('circle')
       .attr('cx', (d, i) -> i * 50 + 25)
       .attr('cy', h / 2)
       .attr('r', (d) -> d)

)
