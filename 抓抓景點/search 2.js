var mysql = require('mysql');

var tempLng,tempLat,tempdis; //暫時的經緯度距離計算
var distance=100000000000000;
var name;
function searching(latitude,longtitude){
    latitude=latitude+0.0000001;
    longtitude=longtitude+0.0000001;
    console.log(latitude,longtitude,"helel");


    var con = mysql.createConnection({
        host: "localhost",
        user: "root",
        password: "",
        database: "place"
    });
    con.connect(function (err) {
        if (err) throw err;
        // console.log("Connected!");
    });
    con.query("SELECT * FROM attraction", function (err, result, fields) {
        if (err) throw err;
        // console.log(result);

        // var temp=new String(result[2].lng);
        // console.log(temp);
        // a=parseFloat(result[2].lng);
        // console.log(a);

        function placeSearch(){
            for(var i=0;i<1419;i++){
                tempLat=parseFloat(result[i].lat); //抓取景點lat
                tempLng=parseFloat(result[i].lng); //抓取景點lng
                tempdis=CoolWPDistance(longtitude,latitude,tempLng,tempLat); //距離計算

                if (distance>tempdis){ //相比距離，如果找到更小就取而代之
                    distance=tempdis;
                    name=(result[i].aName);
                }

            }
            console.log("距離最近景點為：",name); //output會近景點
            return;
        }

        function CoolWPDistance(lng1,lat1,lng2,lat2){
            var f = getRad((lat1 + lat2)/2);
            var g = getRad((lat1 - lat2)/2);
            var l = getRad((lng1 - lng2)/2);
            var sg = Math.sin(g);
            var sl = Math.sin(l);
            var sf = Math.sin(f);
            var s,c,w,r,d,h1,h2;
            var a = 6378137.0;//The Radius of eath in meter.
            var fl = 1/298.257;
            sg = sg*sg;
            sl = sl*sl;
            sf = sf*sf;
            s = sg*(1-sl) + (1-sf)*sl;
            c = (1-sg)*(1-sl) + sf*sl;
            w = Math.atan(Math.sqrt(s/c));
            r = Math.sqrt(s*c)/w;
            d = 2*w*a;
            h1 = (3*r -1)/2/c;
            h2 = (3*r +1)/2/s;
            s = d*(1 + fl*(h1*sf*(1-sg) - h2*(1-sf)*sg));
            // if(s >= 1000 && s <= 99000){
            //     var kilometer = s/1000;
            //     s = kilometer.toFixed(1) + "km";
            // }else if(s > 99000){
            //     s = ">99km";
            // }else{
            //     s = Math.round(s) + "m";
            // }
            // s = s/1000;
            // s = s.toFixed(2);//指定小數點後的位數。
            return s;
        }
        function getRad(d){
            var PI = Math.PI;
            return d*PI/180.0;
        }

        // placeSearch();
    });
}



