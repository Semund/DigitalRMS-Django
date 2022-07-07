document.querySelector(".submit").addEventListener("click", function (e) {
        e.preventDefault();
        let room_number = document.getElementById("roomNumber").value;
        let passport_data = document.getElementById("passportDigits").value;

        const myForm = new FormData();
        myForm.append("csrfmiddlewaretoken", TOKEN);
        myForm.append("room_number", room_number)
        myForm.append("passport_data", passport_data)

        function sendGuestData(data) {
            let xhr = new XMLHttpRequest();
                xhr.open("POST", GUEST_API );

                xhr.setRequestHeader("Accept", "application/json");
                xhr.setRequestHeader("Content-Type", "application/json");
                xhr.setRequestHeader("X-CSRFToken", TOKEN);
                xhr.onload = () => console.log(xhr.responseText);

                xhr.send(JSON.stringify(data));
        }

        fetch(HOTEL_GUEST_DATA_API, {
            method: 'POST',
            body: myForm
        })

            .then(response => response.json())

            .then(data => {
                if (data["detail"] === "Not found.") {
                    alert("Incorrect room number or passport data")
                } else {
                    sendGuestData(data)
                }
            })

            .catch(error => {
                alert("Hotel service connection error")
            });

    });