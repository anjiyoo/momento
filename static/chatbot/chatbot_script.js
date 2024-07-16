document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('submitButton').addEventListener('click', function() {
        var userQuery = document.getElementById('userInput').value;
        if (!userQuery.trim()) {
            // 입력 필드가 비어있을 경우 메시지 표시
            document.getElementById('chat-messages').innerText = "질문을 입력해주세요.";
            return; // 함수 실행 중지
        }
        // 서버에 /chatbot/response/ 엔드포인트로 POST 요청 보냄 (JSON 형식 데이터 포함)
        fetch('/chatbot/response/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_query: userQuery })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('chat-messages').innerText = "서버에서 오류가 발생했습니다: " + data.error;
            } else {
                // 서버에서 반환된 응답
                if (data.message && data.message.trim() !== "") {
                    document.getElementById('chat-messages').innerText = data.message;
                } 
                //서버에서 반환된 메시지가 없거나 빈 문자열인 경우에 실행
                else { 
                    document.getElementById('chat-messages').innerText = "질문하신 내용의 정보가 업데이트 되지 않았습니다.";
                }
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('chat-messages').innerText = "통신 오류가 발생했습니다.";
        });
    });
});
