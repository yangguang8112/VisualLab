var ec_left1 = echarts.init(document.getElementById('l1'));

// var ec_left1_Option = {
// 	//标题样式
// 	title: {
// 		text: "全国累计趋势",
// 		textStyle: {
// 			// color: 'white',
// 		},
// 		left: 'left',
// 	},
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
// 		data: ['累计确诊', '现有疑似', "累计治愈", "累计死亡"],
// 		left: "right"
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
// 		data: []//['01.20', '01.21', '01.22']
// 	}],
// 	yAxis: [{
// 		type: 'value',
// 		//y轴字体设置
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
// 		//y轴线设置显示
// 		axisLine: {
// 			show: true
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
// 		name: "累计确诊",
// 		type: 'line',
// 		smooth: true,
// 		data: []//[260, 406, 529]
// 	}, {
// 		name: "现有疑似",
// 		type: 'line',
// 		smooth: true,
// 		data: []//[54, 37, 3935]
// 	},
// 		{
// 		name: "累计治愈",
// 		type: 'line',
// 		smooth: true,
// 		data: []//[25, 25, 25]
// 	}, {
// 		name: "累计死亡",
// 		type: 'line',
// 		smooth: true,
// 		data: []//[6, 9, 17]
// 	}]
// };

ec_left1_Option = {
    // title: {
    //     text: '折线图堆叠'
    // },
    tooltip: {
        trigger: 'axis'
    },
    // legend: {
    //     data: ['邮件营销', '联盟广告', '视频广告', '直接访问', '搜索引擎']
    // },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    // toolbox: {
    //     feature: {
    //         saveAsImage: {}
    //     }
    // },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
        axisLine: {
      		lineStyle: {
        		color: "rgba(255, 255, 255, 1)"
      		}
    	}
    },
    yAxis: {
        type: 'value',
        axisLine: {
      		lineStyle: {
        		color: "rgba(255, 255, 255, 1)"
      		}
    	}
    },
    series: [
        {
            name: '邮件营销',
            type: 'line',
            stack: '总量',
            data: [120, 132, 101, 134, 90, 230, 210]
        },
        {
            name: '联盟广告',
            type: 'line',
            stack: '总量',
            data: [220, 182, 191, 234, 290, 330, 310]
        },
        {
            name: '视频广告',
            type: 'line',
            stack: '总量',
            data: [150, 232, 201, 154, 190, 330, 410]
        },
        {
            name: '直接访问',
            type: 'line',
            stack: '总量',
            data: [320, 332, 301, 334, 390, 330, 320]
        },
        {
            name: '搜索引擎',
            type: 'line',
            stack: '总量',
            data: [820, 932, 901, 934, 1290, 1330, 1320]
        }
    ]
};

ec_left1.setOption(ec_left1_Option)
