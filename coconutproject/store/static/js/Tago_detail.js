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
     //photo = storeINFO_list[10]
     console.log(storeINFO_list)
     console.log(storeINFO_list.length)
     photos = []
     for(var i=10 ; i<storeINFO_list.length;i++){
         photos.push(storeINFO_list[i])
     }
     console.log(photos)
var storeid = document.getElementById("storeid")
storeid.value = storename

function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
    results = regex.exec(location.search);
    return results == null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
};

var title = document.getElementsByClassName("detail_storename");
title[0].innerHTML = storename;

var storeContents = document.getElementsByClassName("detail_storecontents");

function storeinform() {
    return "<p>"+"주소 : "+address+"</p>"
    +"<p>"+"리뷰점수 : "+review_score+"</p>"
    +"<p>"+"pickcount : "+pick_count+"</p>"
    +"<p>"+"전화번호 : "+phonenumber+"</p>"
    +"<p>"+"영업시간 : "+operationtime+"</p>"
    +"<p>"+"카테고리 : "+category+"</p>"
    +"<p>"+"용기 종류 : "+container_type+"</p>"
    +"<p>"+"주차 : "+parking+"</p>"
    +"<p>"+"메뉴 : "+menu+"</p>"
};
storeContents[0].innerHTML = storeinform();

var storePictures = document.getElementsByClassName("detail_storepictures");

for(i in photos){
    console.log(photos[i])
    var photoDIV = document.createElement("div")
    photoDIV.innerHTML = "<img src="+photos[i]+" height='180' width='180'"+">"+"&nbsp;&nbsp;&nbsp;&nbsp;"
    photoDIV.setAttribute("class","detail_store_photo")
    storePictures[0].appendChild(photoDIV)
}    



review = getParameterByName('review')
review_list = review.split(',')
console.log(review_list)
review_final = []
temp = []
for(i in review_list){
    if(review_list[i]=='review'){
        review_final.push(temp)
        temp = []
        continue
    }
    temp.push(review_list[i])
}
console.log(review_final)

var writeReview = document.getElementsByClassName("detail_write_review");
writeReview[0].innerHTML= '<button onclick='+"\"location.href= \'" +'http://127.0.0.1:8000/store/review'+'?storename='+storename+  " \'\" "+'>리뷰쓰기</button >';
for(var i=1;i< review_final.length;i++){
    writer = review_final[i][0]
    store = review_final[i][1]
    product_review_score = review_final[i][2]
    takeout_review_score = review_final[i][3]
    write_date = review_final[i][4]
    content = review_final[i][5]

    
    photos_review = []
    for(var j=6 ; j<review_final[i].length;j++){
        photos_review.push(review_final[i][j])
    }

    console.log(photos_review.length)
    var reviewBox = document.getElementsByClassName("detail_review_box");
    var reviewLine = document.getElementsByClassName("detail_review_line");
    if(store == storename){
        var informDIV = document.createElement("div")
        informDIV.innerHTML = "<p>"+"작성자 : "+writer+"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;날짜 : "+write_date+"</p>"+"<p>"+"제품 리뷰 점수 : "+product_review_score+"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+"포장 리뷰 점수 : "+takeout_review_score+"</p>"
        informDIV.setAttribute("class","detail_review_inform")
        

        for(j in photos_review){
            console.log(photos_review[i])
            var photoRDIV = document.createElement("div")
            photoRDIV.innerHTML = "<img src="+photos_review[i]+" height='90' width='90'"+">"+"&nbsp;&nbsp;&nbsp;&nbsp;"
            photoRDIV.setAttribute("class","detail_review_pictures")
            
        }
        var contentsDIV = document.createElement("div")
        contentsDIV.innerHTML = "<p>"+"내용 : "+content+"</p>"
        contentsDIV.setAttribute("class","detail_review_content")

        var BoxDIV = document.createElement("div")
        BoxDIV.setAttribute("class","review_box")
        BoxDIV.append(informDIV,photoRDIV,contentsDIV)
        reviewBox[0].append(BoxDIV)
    }
    
}

