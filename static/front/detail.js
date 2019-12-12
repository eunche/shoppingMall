const EA = document.querySelector(".js-ea");
const TOTAL_PRICE = document.querySelector(".js-total_price");
const PRICE = document.querySelector(".js-price")

function modifyValue(event) {
    if(EA.value < 1) {
        alert("최소 주문량은 1개 입니다");
        EA.value = 1;
    }
    event.preventDefault();
    TOTAL_PRICE.innerText = `${EA.value*PRICE.innerText}원(${EA.value}개)`;
}

function init() {
    EA.addEventListener("click",modifyValue,false);
}

init();

