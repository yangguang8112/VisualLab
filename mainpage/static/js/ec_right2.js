var ec_right2 = echarts.init(document.getElementById('r2'));

var ec_right2_option = {
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'line',
            lineStyle: {
                color: 'rgba(0,0,0,0.2)',
                width: 1,
                type: 'solid'
            }
        }
    },

    legend: {
        data: ['Library Construction', 'Pooling', 'Make DNB', 'Load DNB', 'Sequencing', 'Analysis'],
        textStyle: {
            color: "rgba(228, 81, 81, 1)"
          } 
    },


    singleAxis: {
        top: 50,
        bottom: 50,
        axisTick: {},
        axisLabel: {},
        type: 'time',
        axisPointer: {
            animation: true,
            label: {
                show: true
            }
        },
        splitLine: {
            show: true,
            lineStyle: {
                type: 'dashed',
                opacity: 0.2
            }
        }
    },

    series: [
        {
            type: 'themeRiver',
            emphasis: {
                itemStyle: {
                    shadowBlur: 20,
                    shadowColor: 'rgba(0, 0, 0, 0.8)'
                }
            },
            data: [['2020/11/08',10,'Library Construction'],['2020/11/09',15,'Library Construction'],['2020/11/10',35,'Library Construction'],
            ['2020/11/11',38,'Library Construction'],['2020/11/12',22,'Library Construction'],['2020/11/13',16,'Library Construction'],
            ['2020/11/14',7,'Library Construction'],['2020/11/15',2,'Library Construction'],['2020/11/16',17,'Library Construction'],
            ['2020/11/17',33,'Library Construction'],['2020/11/18',40,'Library Construction'],['2020/11/19',32,'Library Construction'],
            ['2020/11/20',26,'Library Construction'],['2020/11/21',35,'Library Construction'],['2020/11/22',40,'Library Construction'],
            ['2020/11/23',32,'Library Construction'],['2020/11/24',26,'Library Construction'],['2020/11/25',22,'Library Construction'],
            ['2020/11/26',16,'Library Construction'],['2020/11/27',22,'Library Construction'],['2020/11/28',10,'Library Construction'],
            ['2020/11/08',35,'Pooling'],['2020/11/09',36,'Pooling'],['2020/11/10',37,'Pooling'],
            ['2020/11/11',22,'Pooling'],['2020/11/12',24,'Pooling'],['2020/11/13',26,'Pooling'],
            ['2020/11/14',34,'Pooling'],['2020/11/15',21,'Pooling'],['2020/11/16',18,'Pooling'],
            ['2020/11/17',45,'Pooling'],['2020/11/18',32,'Pooling'],['2020/11/19',35,'Pooling'],
            ['2020/11/20',30,'Pooling'],['2020/11/21',28,'Pooling'],['2020/11/22',27,'Pooling'],
            ['2020/11/23',26,'Pooling'],['2020/11/24',15,'Pooling'],['2020/11/25',30,'Pooling'],
            ['2020/11/26',35,'Pooling'],['2020/11/27',42,'Pooling'],['2020/11/28',42,'Pooling'],
            ['2020/11/08',21,'Make DNB'],['2020/11/09',25,'Make DNB'],['2020/11/10',27,'Make DNB'],
            ['2020/11/11',23,'Make DNB'],['2020/11/12',24,'Make DNB'],['2020/11/13',21,'Make DNB'],
            ['2020/11/14',35,'Make DNB'],['2020/11/15',39,'Make DNB'],['2020/11/16',40,'Make DNB'],
            ['2020/11/17',36,'Make DNB'],['2020/11/18',33,'Make DNB'],['2020/11/19',43,'Make DNB'],
            ['2020/11/20',40,'Make DNB'],['2020/11/21',34,'Make DNB'],['2020/11/22',28,'Make DNB'],
            ['2020/11/23',26,'Make DNB'],['2020/11/24',37,'Make DNB'],['2020/11/25',41,'Make DNB'],
            ['2020/11/26',46,'Make DNB'],['2020/11/27',47,'Make DNB'],['2020/11/28',41,'Make DNB'],
            ['2020/11/08',10,'Load DNB'],['2020/11/09',15,'Load DNB'],['2020/11/10',35,'Load DNB'],
            ['2020/11/11',38,'Load DNB'],['2020/11/12',22,'Load DNB'],['2020/11/13',16,'Load DNB'],
            ['2020/11/14',7,'Load DNB'],['2020/11/15',2,'Load DNB'],['2020/11/16',17,'Load DNB'],
            ['2020/11/17',33,'Load DNB'],['2020/11/18',40,'Load DNB'],['2020/11/19',32,'Load DNB'],
            ['2020/11/20',26,'Load DNB'],['2020/11/21',35,'Load DNB'],['2020/11/22',40,'Load DNB'],
            ['2020/11/23',32,'Load DNB'],['2020/11/24',26,'Load DNB'],['2020/11/25',22,'Load DNB'],
            ['2020/11/26',16,'Load DNB'],['2020/11/27',22,'Load DNB'],['2020/11/28',10,'Load DNB'],
            ['2020/11/08',10,'Sequencing'],['2020/11/09',15,'Sequencing'],['2020/11/10',35,'Sequencing'],
            ['2020/11/11',38,'Sequencing'],['2020/11/12',22,'Sequencing'],['2020/11/13',16,'Sequencing'],
            ['2020/11/14',7,'Sequencing'],['2020/11/15',2,'Sequencing'],['2020/11/16',17,'Sequencing'],
            ['2020/11/17',33,'Sequencing'],['2020/11/18',40,'Sequencing'],['2020/11/19',32,'Sequencing'],
            ['2020/11/20',26,'Sequencing'],['2020/11/21',35,'Sequencing'],['2020/11/22',4,'Sequencing'],
            ['2020/11/23',32,'Sequencing'],['2020/11/24',26,'Sequencing'],['2020/11/25',22,'Sequencing'],
            ['2020/11/26',16,'Sequencing'],['2020/11/27',22,'Sequencing'],['2020/11/28',10,'Sequencing'],
            ['2020/11/08',10,'Analysis'],['2020/11/09',15,'Analysis'],['2020/11/10',35,'Analysis'],
            ['2020/11/11',38,'Analysis'],['2020/11/12',22,'Analysis'],['2020/11/13',16,'Analysis'],
            ['2020/11/14',7,'Analysis'],['2020/11/15',2,'Analysis'],['2020/11/16',17,'Analysis'],
            ['2020/11/17',33,'Analysis'],['2020/11/18',4,'Analysis'],['2020/11/19',32,'Analysis'],
            ['2020/11/20',26,'Analysis'],['2020/11/21',35,'Analysis'],['2020/11/22',40,'Analysis'],
            ['2020/11/23',32,'Analysis'],['2020/11/24',26,'Analysis'],['2020/11/25',22,'Analysis'],
            ['2020/11/26',16,'Analysis'],['2020/11/27',22,'Analysis'],['2020/11/28',10,'Analysis']
        ],
        label: {
            color: "rgba(249, 247, 247, 1)",
            position: 'top'
        }
        }
    ]
};


ec_right2.setOption(ec_right2_option);


