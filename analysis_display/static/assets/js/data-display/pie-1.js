MapContainer = document.getElementById('pie-1');
myChart = echarts.init(MapContainer);
let sum_gender = JSON.parse(document.getElementById("sum_gender").textContent);
let sum_gender_num = JSON.parse(document.getElementById("sum_gender_num").textContent);
let gender_SeriesData = Series_data(sum_gender_num);
let gender_SelectData = Select_data(sum_gender);
// let weather_SelectData={"多云转阴": 0,
//     "阴转晴": 1,
//     "晴": 2,
//     "霾转多云": 3,
//     "晴转阴": 4,
//     "阴": 5
// };
option = {
    title : {
        text: '性别统计',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        type: 'scroll',
        orient: 'vertical',
        right: 10,
        top: 20,
        bottom: 20,
        data: sum_gender,
        selected:gender_SelectData
    },
    series : [
        {
            name: '性别',
            type: 'pie',
            radius : '55%',
            center: ['40%', '50%'],
            data: gender_SeriesData,
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};


function Series_data(sum_gender_num){
    var gender_SeriesData=[];
    for(var key in sum_gender_num){
        gender_SeriesData.push({
            name:key,
            value:sum_gender_num[key]
            });
    }
    return gender_SeriesData;
}

function Select_data(sum_gender){
    var gender_SelectData={};
    for(var i=0;i<sum_gender.length;i++){
        gender_SelectData[sum_gender[i]]=i<6;
    }
    return gender_SelectData;
}


myChart.setOption(option);
MapSize = document.getElementById("pie-1");
MapWidth = MapSize.clientWidth||MapSize.offsetWidth;
MapContainer.style.width = MapWidth+'px';
MapContainer.style.height = MapWidth+'px';
myChart.resize();