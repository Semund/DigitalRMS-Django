document.querySelector(".submit").addEventListener("click", function (e) {
        e.preventDefault();
        let room = document.getElementById("roomNumber").value;
        let passport = document.getElementById("passportDigits").value;

        const myForm = new FormData();
        myForm.append("csrfmiddlewaretoken", TOKEN);
        myForm.append("room", room)
        myForm.append("passport", passport)

        function registerGuest(data) {
            let xhr = new XMLHttpRequest();
                xhr.open("POST", REGISTRATION_API );

                xhr.setRequestHeader("Accept", "application/json");
                xhr.setRequestHeader("Content-Type", "application/json");
                xhr.setRequestHeader("X-CSRFToken", TOKEN);
                xhr.onload = () => console.log(xhr.responseText);

                xhr.send(JSON.stringify(data));
        }

        fetch(VALIDATION_API, {
            method: 'POST',
            body: myForm
        })

            .then(response => response.json())

            .then(data => {
                console.log(data)
                if (data["status"] === "Invalid data") {
                    alert("Incorrect room number or passport data")
                } else if (data["status"] === "Connection error") {
                    alert("No connection with server")
                } else {
                    registerGuest(data)
                }
            })

            .catch(error => {
                alert("Hotel service connection error")
            });

});