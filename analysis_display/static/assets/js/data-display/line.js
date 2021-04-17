let MapContainer = document.getElementById('line')
let myChart = echarts.init(MapContainer);
let name = JSON.parse(document.getElementById('name').textContent);
let data_line = JSON.parse(document.getElementById('data_line').textContent);
let sum_people_every_day = JSON.parse(document.getElementById('sum_people_every_day').textContent);
let sum_boy_every_day = JSON.parse(document.getElementById('sum_boy_every_day').textContent);
let sum_girl_every_day = JSON.parse(document.getElementById('sum_girl_every_day').textContent);
let name_list = ['签到人数分析', '总人数(人)','男生数(人)', '女生数(人)'];

option = {
    title: {
        text: name_list[0]
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        left:'20%',
        data: name_list,
    },
    xAxis: {
        type:'category',
        boundaryGap: false,
        data:data_line
    },
    yAxis: {
        splitLine: {
            show: false
        }
    },
    toolbox: {
        left: '80%',
        feature: {
            dataZoom: {
                yAxisIndex: 'none'
            },
            restore: {},
            saveAsImage: {}
        }
    },
    dataZoom: [{
        start: 0,
        end: 20
    }, {
        type: 'inside'
    }],
    visualMap: {
        top: 10,
        right: 10,
        pieces: [{
            lte: 0,
            color: '#0b0a44'
        },{
            gt: 0,
            lte: 10,
            color: '#0e0c4b'
        },{
            gt: 10,
            lte: 20,
            color: '#161180'
        }, {
            gt: 20,
            lte: 30,
            color: '#1c16d3'
        }, {
            gt: 30,
            lte: 40,
            color: '#2e2bff'
        }, {
            gt: 40,
            lte: 50,
            color: '#418cff'
        }, {
            gt: 50,
            lte: 60,
            color: '#3cb1e3'
        }, {
            gt: 60,
            lte: 70,
            color: '#57f2ff'
        }, {
            gt: 70,
            lte: 80,
            color: '#68ffc6'
        }, {
            gt: 80,
            lte: 90,
            color: '#28ff7e'
        },{
            gt: 90,
            lte: 100,
            color: '#80ff45'
        }, {
            gt: 100,
            lte: 110,
            color: '#c3ff65'
        }, {
            gt: 110,
            lte: 120,
            color: '#ffde33'
        }, {
            gt: 120,
            lte: 130,
            color:  '#ff9933'
        }, {
            gt: 130,
            lte: 140,
            color: '#ff9933'
        }, {
            gt: 140,
            color: '#cc0033'
        }],
        outOfRange: {
            color: '#999'
        }
    },
    series: [{
        type:'line',
        markLine: {
            silent: true,
            data: [{
                yAxis: 0
            },{
                yAxis: 10
            },{
                yAxis: 20
            }, {
                yAxis: 30
            }, {
                yAxis: 40
            }, {
                yAxis: 50
            }, {
                yAxis: 60
            },{
                yAxis: 70
            },{
                yAxis: 80
            },{
                yAxis: 90
            },{
                yAxis: 100
            },{
                yAxis: 110
            }, {
                yAxis: 120
            }, {
                yAxis: 130
            }, {
                yAxis: 140
            }]
        }
    },{
        name: name_list[1],
        itemStyle : {
            normal : {
                color:'#EE2C2C'
            }
        },
        type: 'line',
        data: sum_people_every_day,
        markLine: {
            silent: true
        }
    },{
        name: name_list[2],
        itemStyle : {
            normal : {
                color:'#CDCD00'
            }
        },
        type: 'line',
        data: sum_boy_every_day,
        markLine: {
            silent: true
        }
    },{
        name: name_list[3],
        itemStyle : {
            normal : {
                color:'#00FF00'
            }
        },
        type: 'line',
        data: sum_girl_every_day,
        markLine: {
            silent: true
        }
    }]
};

myChart.setOption(option);
let MapSize = document.getElementById("line");
let MapWidth = MapSize.clientWidth||MapSize.offsetWidth;
MapContainer.style.width = MapWidth*0.9+'px';
MapContainer.style.height = MapWidth*0.6+'px';
myChart.resize();