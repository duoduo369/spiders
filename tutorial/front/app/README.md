d3.js
===

data enter
---
    data = [1..10]
    d3.select('body')
      .selectAll('div')
      .data(data)
      .enter()
      .append('div')
      .text((d)->d)

    1. 使用selectAll选出一堆可能不存在的数据
    2. data绑定数据(虽然根本没有这些dom)
    3. enter是个magic方法，使绑定data的selectAll(实际是空的)可以操作
    4. append加入dom
    5. 此时可以有回调,第一个参数是data里面的数据，第二个参数是下标
        (d) -> d || (d, i) -> d

bar图倒置
---
    画bar图的时候需要对y和height做特殊处理，因为默认左上角是坐标原点
        y = svg::height - 倍数 * d
        height = 倍数 * d

    svg.selectAll('bar')
       .data(data)
       .enter()
       .append('rect')
       .attr({
         x: (d, i)-> i * (w / data.length),
         y: (d) -> h - 4 * d,
         width: w / data.length - bar_padding,
         height: (d) -> 4 * d,
       })

scale
---
    scale.linear().domain([100, 500]).range([20, 50]);

    矢量转换
        input domain        ->   ouput rage
        [100, 500]          ->   [20,50]
        input区间100~500    ->   ouput区间按比例缩放为20~50

    定义scale后可以更新domain等
        x_scale.domain([0, d3.max(_data, (d) -> d[0])])
        y_scale.domain([0, d3.max(_data, (d) -> d[1])])


Ordinal
---

Ordinal scales are typically used for ordinal data, typically
categories with some inherent order to them, such as:

    * freshman, sophomore, junior, senior
    * grade B, grade A, grade AA
    * strongly dislike, dislike, neutral, like, strongly like

    scale.ordinal().domain([100, 500]).rangeBands([20, 50], 0.05);
    scale.ordinal().domain([100, 500]).rangeRoundBands([20, 50], 0.05);
    第三个参赛是指两个区间之间有多大的空白，单位%

动画
---
    用在select后，attr前
    .transition()
    .delay(1000)  # 延迟
    .duration(1000) # 动画转换时间
    .ease('elastic')  # 渐变方式 https://github.com/mbostock/d3/wiki/Transitions#d3_ease

    svg.selectAll("circle")
       .data(dataset)
       .transition()
       .duration(1000)
       .each("start", function() {      // <-- Executes at start of transition
           d3.select(this)
             .attr("fill", "magenta")
             .attr("r", 3);
       })
       .attr("cx", function(d) {
            return xScale(d[0]);
       })
       .attr("cy", function(d) {
            return yScale(d[1]);
       })
       .each("end", function() {        // <-- Executes at end of transition
           d3.select(this)
             .attr("fill", "black")
             .attr("r", 2);
       });
    each start中不能内嵌transition, 而end可以，d3在处理transition的时候
    同一个元素只能有一组动画，因此start中的transition会中断后来的动画，
    而end则不同，因为end的时候其他的动画早已结束
