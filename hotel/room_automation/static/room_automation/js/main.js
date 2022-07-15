const ws = new WebSocket("ws://127.0.0.1:8001/ws/room/");

ws.onmessage = function (e) {
    const data = JSON.parse(e.data);
    if (data.action !== "subscribe_instance") {
        document.getElementById('room_content').classList.remove('d-none')
        document.getElementById('room_number').textContent = 'Номер ' + data.data['number']

        for (light_source in data.data['light']) {
            let value = data.data['light'][light_source]
            let id_light_selector = 'light_' + light_source
            if (light_source === 'blinds') {
                document.getElementById(id_light_selector).textContent = value ? 'Открыты' :
                    'Закрыты'
            } else {
                document.getElementById(id_light_selector).textContent = value + "%"
            }
        }

        for (climate_parameter in data.data['climate']) {
            let value = data.data['climate'][climate_parameter]
            let id_climate_selector = 'climate_' + climate_parameter
            if (climate_parameter === 'fan_on_off') {
                document.getElementById(id_climate_selector).textContent = value ? 'Включен' : 'Отключен'
            } else if (climate_parameter === 'fan_auto_mode') {
                document.getElementById(id_climate_selector).textContent = value ? 'Автоматический' : 'Ручной'
            } else if (climate_parameter === 'temp_sp') {
                document.getElementById(id_climate_selector).textContent = value + "℃"
            } else {
                document.getElementById(id_climate_selector).textContent = value + "%"
            }
        }
    }
}

document.getElementById("id_number").onchange = function (e) {
    ws.send(JSON.stringify({
        action: "retrieve",
        request_id: new Date().getTime(),
        pk: document.getElementById("id_number").value
    }))

    ws.send(JSON.stringify({
        action: "subscribe_instance",
        request_id: new Date().getTime(),
        pk: document.getElementById("id_number").value
    }))

}
