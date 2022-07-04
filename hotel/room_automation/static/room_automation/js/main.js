if (window.location.pathname === "/room/") {
        function getRoomData(room_id) {
        let url_api = URL + room_id;
        fetch(url_api)

            .then(response => response.json())

            .then(data => {
                console.log(typeof data)
                for (light_source in data) {
                    console.log(typeof light_source)
                    console.log(typeof data[light_source])

                }
                document.getElementById('room_content').classList.remove('d-none')

                document.getElementById('room_number').textContent = 'Номер ' + data['number']

                for (light_source in data['light']) {
                    console.log(light_source)
                    let value = data['light'][light_source]
                    let id_light_selector = 'light_' + light_source
                    if (light_source === 'blinds') {
                        document.getElementById(id_light_selector).textContent = value ? 'Открыты' :
                            'Закрыты'
                    } else {
                        document.getElementById(id_light_selector).textContent = value + "%"
                    }
                }

                for (climat_parameter in data['climat']) {
                    let value = data['climat'][climat_parameter]
                    let id_climat_selector = 'climat_' + climat_parameter
                    if (climat_parameter === 'fan_on_off') {
                        document.getElementById(id_climat_selector).textContent = value ? 'Включен' : 'Отключен'
                    } else if (climat_parameter === 'fan_auto_mode') {
                        document.getElementById(id_climat_selector).textContent = value ? 'Автоматический' : 'Ручной'
                    } else if (climat_parameter === 'temp_sp') {
                        document.getElementById(id_climat_selector).textContent = value + "℃"
                    } else {
                        document.getElementById(id_climat_selector).textContent = value + "%"
                    }
                }
            })

            .catch(error => {
                let error_msg = document.getElementById('error_msg')
                error_msg.classList.remove('d-none')
                error_msg.textContent = error
            });
    }
}
