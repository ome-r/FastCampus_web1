const listViewRootElem = document.getElementById("list-view-root");

//* 서버(DB)로 부터 가져와야되는 데이터;
const dataList = [
  { title: "장난감A", price: 20000, location: "성수동" },
  { title: "장난감B", price: 20000, location: "강남구" },
  { title: "장난감C", price: 20000, location: "강서구" },
  { title: "장난감D", price: 20000, location: "영동구" },
  { title: "장난감D", price: 20000, location: "영동구" },
  { title: "장난감D", price: 20000, location: "영동구" },
  { title: "장난감D", price: 20000, location: "영동구" },
  { title: "장난감D", price: 20000, location: "영동구" },
];
//* const : string, number, undefined 등등 원시타입은 재할당이 불가능하지만
//*         Array, Object 같은 참조타입의 자료형들은 재할당이 가능합니다.

//* 1) 원본 데이터를 가져온다
//* 2) 사용자가 '가격'을 수정함
//* 3) DB에 데이터 변경
//* 4) 다시 변경된 데이터를 가져온다.

// //* ES6(2015년 자바스크립트 버전 ~ ) 화살표 함수
// const setItem = () => {};

//* ES5(2009년 자바스크립트 버전 ~ ) 함수
//역할: 하나의 개별 아이템 템플릿을 만들어주는 함수
function setItem({ title, price, location }) {
  return `
            <div class='item-wrapper'>
                <div>${title}</div>
                <div>${price}</div>
                <div>${location}</div>
            </div>
            `;
}

let addedItem = "";
for (let i = 0; i < dataList.length; i++) {
  addedItem = addedItem + setItem(dataList[i]);
}

listViewRootElem.innerHTML = addedItem;
