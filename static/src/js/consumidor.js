function habilitarBotones(){
    if(!$('input[name="codigo"]').length){
        $('#buscar_codigo').hide();
    }

    if(!$('input[name="medidor"]').length){
        $('#buscar_medidor').hide();
    }
    console.log('Atendido');
}

habilitarBotones();