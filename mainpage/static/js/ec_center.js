// var ec_center = echarts.init(document.getElementById('c2'), "dark");

// var mydata = [{'name': '上海', 'value': 318}, {'name': '云南', 'value': 162}]

// var ec_center_option = {
//     title: {
//         text: '',
//         subtext: '',
//         x: 'left'
//     },
//     tooltip: {
//         trigger: 'item'
//     },
//     //左侧小导航图标
//     visualMap: {
//         show: true,
//         x: 'left',
//         y: 'bottom',
//         textStyle: {
//             fontSize: 8,
//         },
//         splitList: [{ start: 1,end: 9 },
//             {start: 10, end: 99 }, 
// 			{ start: 100, end: 999 },
//             {  start: 1000, end: 9999 },
//             { start: 10000 }],
//         color: ['#8A3310', '#C64918', '#E55B25', '#F2AD92', '#F9DCD1']
//     },
//     //配置属性
//     series: [{
//         name: '累计确诊人数',
//         type: 'map',
//         mapType: 'china',
//         roam: false, //拖动和缩放
//         itemStyle: {
//             normal: {
//                 borderWidth: .5, //区域边框宽度
//                 borderColor: '#009fe8', //区域边框颜色
//                 areaColor: "#ffefd5", //区域颜色
//             },
//             emphasis: { //鼠标滑过地图高亮的相关设置
//                 borderWidth: .5,
//                 borderColor: '#4b0082',
//                 areaColor: "#fff",
//             }
//         },
//         label: {
//             normal: {
//                 show: true, //省份名称
//                 fontSize: 8,
//             },
//             emphasis: {
//                 show: true,
//                 fontSize: 8,
//             }
//         },
//         data:[] //mydata //数据
//     }]
// };
// ec_center.setOption(ec_center_option)

var ec_center = echarts.init(document.getElementById('c2'));

// ec_center_option = {
//     tooltip: {
//         trigger: 'item',
//         formatter: '{a} <br/>{b}: {c} ({d}%)'
//     },
//     legend: {
//         orient: 'vertical',
//         left: 10,
//         bottom: 40,
//         data: ['累积生产', '待生产', '生产中'],
//         textStyle: {
//             color: "rgba(255, 255, 255, 1)"
//         }
//     },
//     series: [
//         {
//             name: '生产任务',
//             type: 'pie',
//             radius: ['50%', '70%'],
//             avoidLabelOverlap: false,
//             label: {
//                 show: false,
//                 position: 'center'
//             },
//             emphasis: {
//                 label: {
//                     show: true,
//                     fontSize: '30',
//                     fontWeight: 'bold'
//                 }
//             },
//             labelLine: {
//                 show: false
//             },
//             data: [
//                 {value: 335, name: '累积生产'},
//                 {value: 310, name: '待生产'},
//                 {value: 234, name: '生产中'}
//             ]
//         }
//     ]
// };


ec_center_option = {
    // title: {
    //     text: '南丁格尔玫瑰图',
    //     left: 'center'
    // },
    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b} : {c} ({d}%)'
    },
    // legend: {
    //     left: 'center',
    //     top: 'bottom',
    //     data: ['累积生产', '待生产', '生产中']
    // },
    // toolbox: {
    //     show: true,
    //     feature: {
    //         mark: {show: true},
    //         dataView: {show: true, readOnly: false},
    //         magicType: {
    //             show: true,
    //             type: ['pie', 'funnel']
    //         },
    //         restore: {show: true},
    //         saveAsImage: {show: true}
    //     }
    // },
    series: [

        {
            name: '面积模式',
            type: 'pie',
            radius: [30, 200],
            center: ['50%', '50%'],
            roseType: 'area',
            data: [
                {value: 23, name: '生产中'},
                {value: 32, name: '待生产'},
                {value: 328, name: '累积生产'}
            ]
        }
    ]
};


ec_center.setOption(ec_center_option)