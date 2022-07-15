document.addEventListener('DOMContentLoaded', function () {
    fetch(URL_ROOM_API, {
        method: "GET",
        credentials: "same-origin",
        headers: {
            'x-csrftoken': TOKEN
        }
    })

        .then(response => response.json())

        .then(data => {
            for (light_source in data['light']) {
                let value = data['light'][light_source]
                let id_light_selector = 'light_' + light_source
                if (light_source === 'blinds') {
                    if (value) {
                        document.getElementById("light_blinds_open").checked = true
                    } else {
                        document.getElementById("light_blinds_close").checked = true
                    }
                } else {
                    document.getElementById(id_light_selector).value = value
                    document.getElementById(id_light_selector).nextElementSibling.value = value
                }
            }

            for (climate_parameter in data['climate']) {
                let value = data['climate'][climate_parameter]
                let id_climate_selector = 'climate_' + climate_parameter
                if (climate_parameter === 'fan_on_off') {
                    if (value) {
                        document.getElementById("climate_fan_on").checked = true
                    } else {
                        document.getElementById("climate_fan_off").checked = true
                    }
                } else if (climate_parameter === 'fan_auto_mode') {
                    if (value) {
                        document.getElementById("climate_fan_auto").checked = true
                        document.getElementById("climate_fan_man").checked = false
                    } else {
                        document.getElementById("climate_fan_auto").checked = false
                        document.getElementById("climate_fan_man").checked = true
                    }
                } else {
                    document.getElementById(id_climate_selector).value = value
                    document.getElementById(id_climate_selector).nextElementSibling.value = value
                }
            }
        })

        .catch(error => {
            alert("Ошибка связи с сервером")
        });
})

function updateRoomDataHotelServer() {
    let room_data = {
        number: GUEST_ROOM,
        light: {
            main: document.getElementById("light_main").value,
            supply: document.getElementById("light_supply").value,
            corridor: document.getElementById("light_corridor").value,
            bath: document.getElementById("light_bath").value,
            blinds: document.querySelector('input[name="light_blinds"]:checked').value === "true"
        },
        climate: {
            temp_sp: document.getElementById("climate_temp_sp").value,
            heat_valve: document.getElementById("climate_heat_valve").value,
            fan_speed: document.getElementById("climate_fan_speed").value,
            fan_on_off: document.querySelector('input[name="climate_fan_on_off"]:checked').value === "true",
            fan_auto_mode: document.querySelector('input[name="climate_fan_auto_mode"]:checked').value === "true"
        }
    }

    updateRoomData(room_data)
}

function updateRoomData(data) {
    let xhr = new XMLHttpRequest();
    xhr.open("PATCH", URL_ROOM_API);

    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", TOKEN);
    xhr.onload = () => console.log(xhr.responseText);
    xhr.send(JSON.stringify(data));
}
