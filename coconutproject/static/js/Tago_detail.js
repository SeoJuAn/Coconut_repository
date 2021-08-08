console.log(location.search)
storeINFO = getParameterByName('store')
storeINFO_list = storeINFO.split(',')
storename = storeINFO_list[0]
address = storeINFO_list[1]
review_score = storeINFO_list[2]
pick_count = storeINFO_list[3]
phonenumber = storeINFO_list[4]
operationtime = storeINFO_list[5]
category = storeINFO_list[6]
menu = storeINFO_list[7]
container_type = storeINFO_list[8]
parking = storeINFO_list[9]
photo = storeINFO_list[10]
console.log(storeINFO_list)

document.write("<p>"+"가게이름 : "+storename+"</p>")
document.write("주소 : "+address+"</p>")
document.write("리뷰점수 : "+review_score+"</p>")
document.write("pickcount : "+pick_count+"</p>")
document.write("전화번호 : "+phonenumber+"</p>")
document.write("영업시간 : "+operationtime+"</p>")
document.write("카테고리 : "+category+"</p>")
document.write("메뉴 : "+menu+"</p>")
document.write("용기 종류 : "+container_type+"</p>")
document.write("주차 : "+parking+"</p>")
document.write('<button onclick='+"\"location.href=\'" +'http://127.0.0.1:8000/store/review'+'?storename='+storename+  " \'\" "+'>리뷰쓰기</button >')
if(photo!=null){
    document.write('<img src='+photo+'>'+'<br>')
}

function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
    results = regex.exec(location.search);
    return results == null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}
