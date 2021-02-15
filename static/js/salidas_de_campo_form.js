var lista_componentes_estacion = "";

$.get('/api/Componente_Estacion/', function (result) {
    lista_componentes_estacion = result;
});

var lista_componentes = "";

$.get('/api/Componente/', function (result) {
    lista_componentes = result;
});

var lista_sensores_estacion = "";

$.get('/api/Sensor_Estacion/', function (result) {
    lista_sensores_estacion = result;
    console.log(lista_sensores_estacion);

});

var lista_sensores = "";

$.get('/api/Sensor/', function (result) {
    lista_sensores = result;
    console.log(lista_sensores);
});

// ----------- Select de estación -------------------
var estacion_selecta = "";
$('#select_estacion').on('select2:select', function (e) {
    document.getElementById("select_componente").innerHTML = "<option selected='selected' disabled='disabled'>Selecciona un componente</option>";
    document.getElementById('nombre_componente').innerHTML = '<i class="fas fa-tools"></i> Componente';
    document.getElementById("select_sensor").innerHTML = "<option selected='selected' disabled='disabled'>Selecciona un sensor</option>";
    document.getElementById('nombre_sensor').innerHTML = '<i class="fas fa-cloud-sun-rain"></i> Sensor';
    var data = e.params.data;
    estacion_selecta = data.id;
    document.getElementById('nombre_estacion').innerHTML = '<i class="fas fa-broadcast-tower"></i> ' + data.text;
    // Se recorren todas las posiciones del vector que contiene a los componente
    for (i = 0; i < lista_componentes_estacion.length; i++) {
        if (lista_componentes_estacion[i].ubicacion == estacion_selecta) {
            for (j = 0; j < lista_componentes.length; j++) {
                if (lista_componentes[j].id == lista_componentes_estacion[i].componente) {
                    // Se crea un elemento tipo option
                    let z = document.createElement("option");
                    // Al cual se le asigna el valor de la variable
                    z.setAttribute("value", lista_componentes[j].id);
                    // Y se le asigna al valor a mostrar
                    let t = document.createTextNode(lista_componentes[j].nombre + " (" + lista_componentes[j].referencia + ")");
                    z.appendChild(t);
                    // Luego se añade al html
                    document.getElementById("select_componente").appendChild(z);
                }
            }
        }
    }
    for (i = 0; i < lista_sensores_estacion.length; i++) {
        if (lista_sensores_estacion[i].ubicacion == estacion_selecta) {
            for (j = 0; j < lista_sensores.length; j++) {
                if (lista_sensores[j].id == lista_sensores_estacion[i].sensor) {
                    // Se crea un elemento tipo option
                    let z = document.createElement("option");
                    // Al cual se le asigna el valor de la variable
                    z.setAttribute("value", lista_sensores[j].id);
                    // Y se le asigna al valor a mostrar
                    let t = document.createTextNode(lista_sensores[j].nombre + " (" + lista_sensores[j].unidad + ")");
                    z.appendChild(t);
                    // Luego se añade al html
                    document.getElementById("select_sensor").appendChild(z);
                }
            }
        }
    }
});


$('#select_componente').on('select2:select', function (e) {
    var data = e.params.data;
    componente_selecto = data.id;
    document.getElementById('nombre_componente').innerHTML = '<i class="fas fa-tools"></i> ' + data.text;
});

$('#select_sensor').on('select2:select', function (e) {
    var data = e.params.data;
    componente_selecto = data.id;
    document.getElementById('nombre_sensor').innerHTML = '<i class="fas fa-cloud-sun-rain"></i> ' + data.text;
});


// var d1 = document.getElementById('Prueba');
// $("#addSensor").click(function () {
//     let htmlx = "";
//     htmlx += '<div id="vidas" class="row">';
//     htmlx += '<button type="button" class="btn btn-dark swalOK"><i class="fas fa-plus-circle"></i> Agregar sensor</button>';
//     htmlx += '</div>';

//     // document.getElementById("Prueba").innerHTML = htmlx;
//     d1.insertAdjacentHTML('afterend', htmlx);

//     // $("#Prueba").innerHTML(htmlx);
// });