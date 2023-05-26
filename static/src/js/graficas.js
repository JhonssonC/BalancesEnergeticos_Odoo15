
new Chart(document.getElementById('general'), {
    type: 'doughnut',
    data: {
    labels: [
        'Eficacia ['+($("span[name='eficacia']:first").text().slice(0, -1)).replace(",",".")+'%]', 
        'Error ['+($("span[name='error']:first").text().slice(0, -1)).replace(",",".")+'%]'
    ],
    datasets: [{
        label: '%',
        data: [
            ($("span[name='eficacia']:first").text().slice(0, -1)).replace(",","."),
            ($("span[name='error']:first").text().slice(0, -1)).replace(",",".")
        ],
        backgroundColor: [
            '#52BE80',
            '#FADBD8'
        ],
        borderWidth: 1
    }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Analisis de Consumos Generales de Red en Porcentajes'
            }
        }
    }                             
});


new Chart( document.getElementById('especifico'), {
    type: 'doughnut',
    data: {
    labels: [
        'Clientes ['+($("span[name='consumo_clientes']:first").text()).replace(",",".")+'Kw]', 
        'Luminarias ['+($("span[name='consumo_luminarias']:first").text()).replace(",",".")+'Kw]', 
        'Semáforos ['+($("span[name='consumo_semaforos']:first").text()).replace(",",".")+'Kw]', 
        'Cámaras ['+($("span[name='consumo_camaras']:first").text()).replace(",",".")+'Kw]', 
        'Servicios Convenidos ['+($("span[name='consumo_otros']:first").text()).replace(",",".")+'Kw]', 
        'Perdida ['+($("span[name='perdidas_comerciales_dias']:first").text()).replace(",",".")+'Kw]'
    ],
    datasets: [{
        label: 'Kw Consumidos',
        data: [
            ($("span[name='consumo_clientes']:first").text()).replace(",","."), 
            ($("span[name='consumo_luminarias']:first").text()).replace(",","."),
            ($("span[name='consumo_semaforos']:first").text()).replace(",","."),
            ($("span[name='consumo_camaras']:first").text()).replace(",","."),
            ($("span[name='consumo_otros']:first").text()).replace(",","."),
            ($("span[name='perdidas_comerciales_dias']:first").text()).replace(",",".")
        ],
        backgroundColor: [
            '#76D7C4',
            '#BB8FCE',
            '#F8C471',
            '#85C1E9',
            '#D7DBDD',
            '#FADBD8'
        ],
        borderWidth: 1
    }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Analisis de Consumos Específicos de Red por Tipo de Consumidor'
            }
        }
    }                                     
});

new Chart(document.getElementById('enkw'), {
    type: 'doughnut',
    data: {
    labels: [
        'Clientes ('+$("span[name='cant_clientes']:first").text().replace(",",".")+')', 
        'Luminarias ('+$("span[name='cant_luminarias']:first").text().replace(",",".")+')', 
        'Semáforos ('+$("span[name='cant_semaforos']:first").text().replace(",",".")+')', 
        'Cámaras ('+$("span[name='cant_camaras']:first").text().replace(",",".")+')', 
        'Servicios Convenidos ('+$("span[name='cant_otros']:first").text().replace(",",".")+')'
    ],
    datasets: [{
        label: 'Cantidad',
        data: [
            $("span[name='cant_clientes']:first").text().replace(",","."), 
            $("span[name='cant_luminarias']:first").text().replace(",","."),
            $("span[name='cant_semaforos']:first").text().replace(",","."),
            $("span[name='cant_camaras']:first").text().replace(",","."),
            $("span[name='cant_otros']:first").text().replace(",",".")
        ],
        backgroundColor: [
            '#76D7C4',
            '#BB8FCE',
            '#F8C471',
            '#85C1E9',
            '#D7DBDD'
        ],
        borderWidth: 1
    }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Cantidades de Tipos de Consumidores en la Red'
            }
        }
    }                                
});

new Chart(document.getElementById('generalkw'), {
    type: 'doughnut',
    data: {
    labels: [
        'Energía Registrada ['+$("span[name='energia_registrada_dias']:first").text().replace(",",".")+'Kw]', 
        'Pérdidas ['+$("span[name='perdidas_comerciales_dias']:first").text().replace(",",".")+'Kw]'
    ],
    datasets: [{
        label: 'Kw Consumidos',
        data: [
            $("span[name='energia_registrada_dias']:first").text().replace(",","."), 
            $("span[name='perdidas_comerciales_dias']:first").text().replace(",",".")
        ],
        backgroundColor: [
            '#52BE80',
            '#FADBD8'
        ],
        borderWidth: 1
    }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Analisis de Consumos Generales de Red en Kw'
            }
        }
    }                                      
});