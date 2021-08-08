//별점 마킹 모듈 프로토타입으로 생성
function Rating1(){};
Rating1.prototype.rate1 = 0;
Rating1.prototype.setRate = function(newrate){
    //별점 마킹 - 클릭한 별 이하 모든 별 체크 처리
    this.rate = newrate;
    let items = document.querySelectorAll('.rate_radio_m');
    items.forEach(function(item, idx){
        if(idx < newrate){
            item.checked = true;
        }else{
            item.checked = false;
        }
    });
}
let ratingM = new Rating1();//별점 인스턴스 생성

document.addEventListener('DOMContentLoaded', function(){
    //별점선택 이벤트 리스너
    document.querySelector('.rating').addEventListener('click',function(e){
        let elem = e.target;
        if(elem.classList.contains('rate_radio_m')){
            ratingM.setRate(parseInt(elem.value));
        }
    })
});

//별점 마킹 모듈 프로토타입으로 생성
function Rating2(){};
Rating2.prototype.rate2 = 0;
Rating2.prototype.setRate = function(newrate){
    //별점 마킹 - 클릭한 별 이하 모든 별 체크 처리
    this.rate = newrate;
    let items = document.querySelectorAll('.rate_radio_d');
    items.forEach(function(item, idx){
        if(idx < newrate){
            item.checked = true;
        }else{
            item.checked = false;
        }
    });
}
let ratingD = new Rating2();//별점 인스턴스 생성