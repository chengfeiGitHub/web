// 和服务器进行数据通信绑定

console.log('创建wobsocket 通信')
var socket = io.connect('http://localhost:5000');

// 绑定和服务器连接成功信息
socket.on('connect', function() {
    socket.emit('connected replay', { data: 'I\'m connected!' });
});

// 头部数据
socket.on('header_data', function(data) {
    vm_title.title_cnt = data['data']
});


// 菜单数据
socket.on('menu_data', function(data) {
    vm_menu.menu_cnt = data['data']
});

// 主要内容数据
socket.on('main_data', function(data) {
    vm_main.main_cnt = data['data']
});

// 底部数据
socket.on('footer_data', function(data) {
    vm_footer.footer_cnt = data['data']
});

// 绑定要一个自定义事件 当接受到数据之后遍历打印出数据
socket.on('test event', function(data) {
    console.log(data)
});
page_data = ' 刷新http://localhost:5000 更新数据'