function randomnum(smin, smax) {// 获取2个值之间的随机数
	var Range = smax - smin;
	var Rand = Math.random();
	return (smin + Math.round(Rand * Range));
}

function runzp() {
	var data = '[{"id":0,"prize":"特等奖：TCL32寸智能液晶电视","v":1.0},{"id":1,"prize":"一等奖：30元百业汇消费券","v":2.0},{"id":2,"prize":"二等奖：10元百业汇消费券","v":3.0},{"id":3,"prize":"三等奖：5元百业汇消费券","v":10.0},{"id":4,"prize":"幸运奖：3角移动话费","v":50.0}]';// 奖项json
	var obj = eval('(' + data + ')');
	var result = randomnum(1, 100);
	var line = 0;
	var temp = 0;
	var returnobj = "0";
	var index = 0;

	// alert("随机数"+result);
	for ( var i = 0; i < obj.length; i++) {
		var obj2 = obj[i];
		var c = parseFloat(obj2.v);
		temp = temp + c;
		line = 100 - temp;
		if (c != 0) {
			if (result > line && result <= (line + c)) {
				index = i;
				// alert(i+"中奖"+line+"<result"+"<="+(line + c));
				returnobj = obj2;
				break;
			}
		}
	}
	var angle = 330;
	var message = "";
	var myreturn = new Object;
	if (returnobj != "0") {// 有奖
		message = "\r\n恭喜您中奖！！";
		var angle0 = [ 170, 190 ];
		var angle1 = [ 350, 375 ];
		var angle2 = [ 115, 135 ];
		var angle3 = [ 220, 245 ];
		var angle4 = [ 55, 80 ];
		switch (index) {
		case 0:// 特等奖
			var r0 = randomnum(angle0[0], angle0[1]);
			angle = r0;
			break;
		case 1:// 一等奖
			var r1 = randomnum(angle1[0], angle1[1]);
			angle = r1;
			break;
		case 2:// 二等奖
			var r2 = randomnum(angle2[0], angle2[1]);
			angle = r2;
			break;
		case 3:// 三等奖
			var r3 = randomnum(angle3[0], angle3[1]);
			angle = r3;
			break;
		case 4:// 幸运奖
			var r4 = randomnum(angle4[0], angle4[1]);
			angle = r4;
			break;

		}
		myreturn.prize = returnobj.prize;
	} else {// 没有
		message = "再接再厉";
		var angle5 = [ 30, 40 ];
		var angle6 = [ 90, 100 ];
		var angle7 = [ 140, 160 ];
		var angle8 = [ 260, 330 ];
		var r = randomnum(5, 8);
		var angle;
		switch (r) {
		case 5:
			var r5 = randomnum(angle5[0], angle5[1]);
			angle = r5;
			break;
		case 6:
			var r6 = randomnum(angle6[0], angle6[1]);
			angle = r6;
			break;
		case 7:
			var r7 = randomnum(angle7[0], angle7[1]);
			angle = r7;
			break;
		case 8:
			var r8 = randomnum(angle8[0], angle8[1]);
			angle = r8;
			break;
		}
		myreturn.prize = "继续努力!";

	}
	myreturn.angle = angle;
	myreturn.message = message;
	return myreturn;
}// JavaScript Document