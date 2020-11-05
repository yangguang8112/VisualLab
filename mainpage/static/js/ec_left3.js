var ec_left3 = echarts.init(document.getElementById('l3'));

var ec_left3_Option = {
    tooltip: {
        formatter: '{a} <br/>{b} : {c}%'
    },
    toolbox: {
        feature: {
            restore: {},
            saveAsImage: {}
        }
    },
    series: [
        {
            name: '业务指标',
            type: 'gauge',
            detail: {formatter: '{value}%'},
            data: [{value: 50, name: '内存利用率', }],
            markPoint:{  //图表标注
                symbol:'circle', //'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'
                symbolSize:5,
                data:[
                    //跟你的仪表盘的中心位置对应上，颜色可以和画板底色一样
                    {x:'center',y:'center',itemStyle:{color:'#FFF'}}
                ]
            },
            
            title : {               //设置仪表盘中间显示文字样式
                textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                    fontSize: 13,
                    color:"white"
                }
            },

        }
    ]
};

setInterval(function () {
    option.series[0].data[0].value = (Math.random() * 100).toFixed(2) - 0;
    myChart.setOption(option, true);
},2000);

ec_left3.setOption(ec_left3_Option)