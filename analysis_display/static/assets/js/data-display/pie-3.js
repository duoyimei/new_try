MapContainer = document.getElementById('pie-3')
myChart = echarts.init(MapContainer);
let place_item = JSON.parse(document.getElementById("place_item").textContent);
let place_num = JSON.parse(document.getElementById("place_num").textContent);
let place_SeriesData = Series_data(place_num);
let place_SelectData = Select_data(place_item);
option = {
            title: {
                text: "地区统计",
                x: 'center'
            },
            tooltip: { //tooltip提示框，鼠标悬浮交互时的信息提示
                trigger: 'item' //触发类型，默认数据触发，见下图，可选为：'item' | 'axis'
            },
            legend: { //legend图例
                orient: 'vertical', //布局方式，默认为水平布局，可选为：'horizontal' | 'vertical'
                x: 'left',
                data: ['地区人数'] //图例内容数组
            },
            dataRange: { //dataRange值域选择
                min: 0, //指定的最小值，eg: 0，默认无，必须参数，唯有指定了splitList时可缺省min。
                max: 400,
                x: 'left', //水平安放位置，默认为全图左对齐，可选为：'center' | 'left' | 'right' | {number}（x坐标，单位px）
                y: 'bottom', //垂直安放位置，默认为全图底部，可选为：'top' | 'bottom' | 'center' | {number}（y坐标，单位px）
                text: ['高', '低'], // 文本，默认为数值文本
                calculable: true //是否启用值域漫游，启用后无视splitNumber和splitList，值域显示为线性渐变
            },
            toolbox: { //toolbox
                show: true,
                orient: 'vertical', //布局方式，默认为水平布局，可选为：'horizontal' | 'vertical'
                x: 'right',
                y: 'center',
                feature: {
                    mark: {
                        show: true
                    },
                    dataView: {
                        show: true,
                        readOnly: false
                    },
                    restore: {
                        show: true
                    },
                    saveAsImage: {
                        show: true
                    }
                }
            },
            roamController: { //缩放漫游组件
                show: true,
                x: 'right',
                mapTypeControl: { //必须，指定漫游组件可控地图类型，如：{ china: true }
                    'china': true
                }
            },
            //series : eval("[" + dataStr + "]")
            series: [ //通用,驱动图表生成的数据内容数组，数组中每一项为一个系列的选项及数据，其中个别选项仅在部分图表类型中有效
                {
                    name: '地区人数',
                    type: 'map',
                    mapType: 'china',
                    itemStyle: {
                        normal: {
                            label: {
                                show: true
                            }
                        },
                        emphasis: {
                            label: {
                                show: true
                            }
                        }
                    },
                    data: place_SeriesData,
                }
            ]
};

function Series_data(place_num){
    var place_SeriesData=[];
    for(var key in place_num){
        place_SeriesData.push({
            name:key,
            value:place_num[key]
            });
    }
    return place_SeriesData;
}

myChart.setOption(option);
MapSize = document.getElementById("pie-3");
MapWidth = MapSize.clientWidth||MapSize.offsetWidth;
MapContainer.style.width = MapWidth+'px';
MapContainer.style.height = MapWidth+'px';
myChart.resize();