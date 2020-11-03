var ec_left2 = echarts.init(document.getElementById('l2'));

// var ec_left2_Option = {
// 	tooltip: {
// 		trigger: 'axis',
// 		//指示器
// 		axisPointer: {
// 			type: 'line',
// 			lineStyle: {
// 				color: '#7171C6'
// 			}
// 		},
// 	},
// 	legend: {
// 		data: ['新增确诊', '新增疑似'],
// 		left: "right"
// 	},
// 	//标题样式
// 	title: {
// 		text: "全国新增趋势",
// 		textStyle: {
// 			color: 'white',
// 		},
// 		left: 'left'
// 	},
// 	//图形位置
// 	grid: {
// 		left: '4%',
// 		right: '6%',
// 		bottom: '4%',
// 		top: 50,
// 		containLabel: true
// 	},
// 	xAxis: [{
// 		type: 'category',
// 		//x轴坐标点开始与结束点位置都不在最边缘
// 		// boundaryGap : true,

// 		data: []
// 	}],
// 	yAxis: [{
// 		type: 'value',
// 		//y轴字体设置

// 		//y轴线设置显示
// 		axisLine: {
// 			show: true
// 		},
// 		axisLabel: {
// 			show: true,
// 			color: 'white',
// 			fontSize: 12,
// 			formatter: function(value) {
// 				if (value >= 1000) {
// 					value = value / 1000 + 'k';
// 				}
// 				return value;
// 			}
// 		},
// 		//与x轴平行的线样式
// 		splitLine: {
// 			show: true,
// 			lineStyle: {
// 				color: '#17273B',
// 				width: 1,
// 				type: 'solid',
// 			}
// 		}
// 	}],
// 	series: [{
// 		name: "新增确诊",
// 		type: 'line',
// 		smooth: true,
// 		data: []
// 	}, {
// 		name: "新增疑似",
// 		type: 'line',
// 		smooth: true,
// 		data: []
// 	}]
// };


var ec_left2_Option = {
    title: {
        // text: '世界人口总量',
        // subtext: '数据来自网络'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    // legend: {
    //     data: ['2011年', '2012年']
    // },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'value',
        boundaryGap: [0, 0.01],
        axisLine: {
      		lineStyle: {
        		color: "rgba(255, 255, 255, 1)"
      		}
    	}
    },
    yAxis: {
        type: 'category',
        data: ['巴西', '印尼', '美国', '印度', '中国', '世界人口(万)'],
        axisLine: {
      		lineStyle: {
        		color: "rgba(255, 255, 255, 1)"
      		}
    	}
    },
    series: [
        {
            name: '2011年',
            type: 'bar',
            data: [18203, 23489, 29034, 104970, 131744, 630230]
        },
        {
            name: '2012年',
            type: 'bar',
            data: [19325, 23438, 31000, 121594, 134141, 681807]
        }
    ]
};


ec_left2.setOption(ec_left2_Option)
