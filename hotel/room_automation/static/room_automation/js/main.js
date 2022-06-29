if (window.location.pathname === "/room/") {
    document.querySelector(".submit").addEventListener("change", function (e) {
        e.preventDefault();
        room_number = document.getElementById("{{ room_select.room.id_for_label }}").value;

        const myForm = new FormData();
        myForm.append('csrfmiddlewaretoken', '{{ csrf_token }}');
        myForm.append('room', room_number)

        fetch('{% url "room" %}', {
            method: 'POST',
            body: myForm
        })

            .then(response => response.json())
        console.log('Success!')
        document.getElementById('room_content').classList.remove('d-none')

            .then(data => {
                let error_msg = document.getElementById('error_msg')
                error_msg.classList.remove('d-none')
                error_msg.value = '123'
            })

            .catch(error => {
                let error_msg = document.getElementById('error_msg')
                error_msg.classList.remove('d-none')
                error_msg.value = error
            });

    });
}
