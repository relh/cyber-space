var page = require('webpage').create();
page.open('http://sogou.com/', function (status) {
    if (status !== 'success') {
        console.log('Unable to load the address!');
    } else {
        var height = 400;
        var width = 400;
        console.log('Crop to: '+width+"x"+height);

        page.clipRect = { top: 0, left: 0, width: width, height: height };
        window.setTimeout(function () {
            page.render('C:/Users/aqwin/Documents/cyberSpace/Assets/Resources/webpage.png');
            phantom.exit();
        }, 200);
    }
});