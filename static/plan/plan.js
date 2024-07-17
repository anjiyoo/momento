document.addEventListener('DOMContentLoaded', function() {
    const trip = '{{new_trip.id}}'
    const baseUrl ='{% url "plan:plan" %}?ajax=true'+'&trip_id=' + trip;
    fetch(baseUrl)
    .then(response => response.json())
    .then(data => {
    console.log(data)
    const spotsByDay = {};
    spotContainer=document.getElementById('spot-container')
    
       // 날짜별로 spot 데이터 정리
       data.forEach(spot => {
            if (!spotsByDay[spot.day]) {
                spotsByDay[spot.day] = [];
            }
            // 중복 체크
            const isDuplicate = spotsByDay[spot.day].some(existingSpot => 
                    existingSpot.spot === spot.spot && existingSpot.title === spot.title
                );
                if (!isDuplicate) {
                    spotsByDay[spot.day].push(spot);
                }
        });
        console.log(spotsByDay)
        // 각 날짜별 컨테이너에 spot 추가
        Object.keys(spotsByDay).forEach(day => {
                console.log(day)
                const dayContainer = document.querySelector(`.day-planner[data-date="${day}"] #spot-container`);
                if (dayContainer) {
                    spotsByDay[day].forEach(spot => {
                        
                        // 최상위 div 생성
                        const spotDiv = document.createElement('div');
                        spotDiv.className = 'mb-2';
                        spotDiv.style.cssText = 'border: 1px #E2E2E2 solid; width: 460px; height: 80px; display: flex; align-items: center;';
                        
                        // 내부 div 생성
                        const innerDiv = document.createElement('div');
                        innerDiv.className = 'mt-1';
                        
                        // 제목 div 생성
                        const titleDiv = document.createElement('div');
                        titleDiv.style.fontWeight = 'bold';
                        titleDiv.style.fontSize = '20px';
                        
                        titleDiv.textContent = spot.title;
                        const del = document.createElement('button');
                        del.textContent = 'x'
                        del.classList.add('ms-auto','del_btn')
                        // 주소 p 생성
                        const addressP = document.createElement('p');
                        addressP.textContent = `관광명소·${spot.address}`;
                        
                        // 요소들을 조립
                        innerDiv.appendChild(titleDiv);
                        innerDiv.appendChild(addressP);
                        spotDiv.appendChild(innerDiv);
                        spotDiv.appendChild(del);
                        
                        // 최종 구조를 컨테이너에 추가
                        dayContainer.appendChild(spotDiv);
                    });
                }
            });
    })
    
  .catch(error => console.error('Fetch 오류:', error));

   // 삭제 버튼에 대한 이벤트 리스너 추가
//    document.body.addEventListener('click', function(event) {
//         if (event.target.classList.contains('del_btn')) {
//             // 클릭된 버튼의 부모 요소(전체 박스)를 찾아 삭제
//             const boxToRemove = event.target.closest('.mb-2');
//             if (boxToRemove) {
//                 boxToRemove.remove();
                
//             }
//         }
//     });
})