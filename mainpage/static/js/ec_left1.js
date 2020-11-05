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
	title: {
		text: "变异统计",
		textStyle: {
			 color: 'white',
		},
		left: 'left',
	},
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
        type: 'log',
        min: 1000,
        logBase: 100,
        axisLine: {
      		lineStyle: {
        		color: "rgba(255, 255, 255, 1)"
      		}
    	}
    },
    series: [
        {
            name: 'SNP',
            type: 'line',
            data: [37379830, 38379840, 35379840, 40079830, 33379800, 23780900, 32379830]
        },
        {
            name: 'INDEL',
            type: 'line',
            data: [9966730, 9320000, 9010000, 9340000, 1290000, 8330000, 8320000]
        },
        {
            name: 'CNV_DEL',
            type: 'line',
            data: [33020, 32000, 34000, 39000, 33000, 23000, 29000]
        },
        {
            name: 'CNV_DUP',
            type: 'line',
            data: [4500, 4800, 3500, 4000, 4200, 3300, 3100]
        },
        {
            name: 'SV',
            type: 'line',
            data: [4830, 3320, 4580, 4340, 3900, 3300, 3200]
        }
    ]
};

ec_left1.setOption(ec_left1_Option)
