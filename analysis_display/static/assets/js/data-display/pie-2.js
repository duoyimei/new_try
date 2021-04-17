MapContainer = document.getElementById('pie-2');
myChart = echarts.init(MapContainer);
let age_item = JSON.parse(document.getElementById("age_item").textContent);
let age_num = JSON.parse(document.getElementById("age_num").textContent);
let age_SeriesData = Series_data(age_num);
let age_SelectData = Select_data(age_item);

option = {
    title : {
        text: '年龄统计',
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
        data: age_item,
        selected: age_SelectData
    },
    series : [
        {
            name: '年龄（人）',
            type: 'pie',
            radius : '55%',
            center: ['40%', '50%'],
            data: age_SeriesData,
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


function Series_data(age_num){
    var age_SeriesData=[];
    for(var key in age_num){
        age_SeriesData.push({
            name:key,
            value:age_num[key]
            });
    }
    return age_SeriesData;
}

function Select_data(age_item){
    var age_SelectData={};
    for(var i=0;i<age_item.length;i++){
        age_SelectData[age_item[i]]=i<6;
    }
    return age_SelectData;
}

myChart.setOption(option);
MapSize = document.getElementById("pie-2");
MapWidth = MapSize.clientWidth||MapSize.offsetWidth;
MapContainer.style.width = MapWidth+'px';
MapContainer.style.height = MapWidth+'px';
myChart.resize();