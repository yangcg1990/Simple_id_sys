function time() {
        dt = new Date();

        //获取年月日
        var y=dt.getYear()+1900;
        var mm=dt.getMonth()+1;
        var d=dt.getDate();

        //获取星期
        var weekday=["星期日","星期一","星期二","星期三","星期四","星期五","星期六"];
        var day=dt.getDay();

        //得到时分秒
        var h=dt.getHours();
        var m=dt.getMinutes();
        var s=dt.getSeconds();

        //时间统一两位数显示
        if(h<10){h="0"+h;}
        if(m<10){m="0"+m;}
        if(s<10){s="0"+s;}

        //向ID=timeShow的地方插入时间内容
        document.getElementById("timeShow").innerHTML = y+"年"+mm+"月"+d+"日"+" "+weekday[day]+
            " "+h+":"+m+":"+s+"";

        setTimeout(time,1000);//设定定时器，循环执行
    }