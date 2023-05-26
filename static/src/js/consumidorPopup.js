odoo.define('module.consumidorPopup', function (require) {
    "use strict";

    var Dialog = require('web.Dialog');
    var ajax = require('web.ajax');
    var rpc = require('web.rpc');

    // var FormController = require('web.FormController');
    // var core = require('web.core');
    // var qweb = core.qweb;
    // var FormView = require('web.FormView');
    // var FieldMany2One = require('web.relational_fields').FieldMany2One;
    // var Widget = require('web.Widget');


    // var globalFieldMany2One=null;
    // var globalFormView=null;
    // var globalFormController=null;




    

    
    // FieldMany2One.include({
    //     init: function () {
    //         this._super.apply(this, arguments);
    //         if (this.name=="marca_medidor_id")
    //             globalFieldMany2One=this;
    //     },
    // });


    // FormController.include({
            
    //     init: function () {
    //         this._super.apply(this, arguments);

    //         console.log('widget',this);
    //         globalFormController=this
    //     },
    //     _onFieldChanged: function (event) {
    //         this._super.apply(this, arguments);
    //         var self = this;

    //         console.log('evento',event);
            
    //         if (event.data.changes.marca_medidor_id) {
    //             var my_field_value = event.data.changes.marca_medidor_id;
    //             if (my_field_value) {
    //                 // Do something when the value of the Many2one field changes
    //                 console.log("The value of the Many2one field has changed to: ", my_field_value);
    //                 console.log(event.target);
    //             }
    //         }
    //     },
    // });

    
    // FormView.include({
    //     init: function () {
    //         this._super.apply(this, arguments);
    //         globalFormView=this;
            
    //     },
    // });
    





    var dialog = null;



    $(document).on('click', '#buscar_codigo', function(){

        console.log("Click buscar_codigo");

        let codigo = $('input[name="codigo"]').val();


        $('input[name="marca_oculta"]').val('').trigger("change");
        $('input[name="medidor"]').val('').trigger("change");
        $('input[name="nombre"]').val('').trigger("change");
        $('input[name="direccion"]').val('').trigger("change");
        $('input[name="geo"]').val('').trigger("change");
        $('input[name="serie"]').val('').trigger("change");
        
        ajaxreqList(undefined, codigo);

    });




    $(document).on('click', '#buscar_medidor', function(){

        console.log("Click buscar_medidor");

        // console.log('globalglobalFormControllerwidget', globalFormController);
        // console.log('globalFormView', globalFormView);
        // console.log('globalFieldMany2One', globalFieldMany2One);
       
        let medidor = $('input[name="medidor"]').val();

        $('input[name="marca_oculta"]').val('').change();
        $('input[name="codigo"]').val('').trigger("change");
        $('input[name="nombre"]').val('').trigger("change");
        $('input[name="direccion"]').val('').trigger("change");
        $('input[name="geo"]').val('').trigger("change");
        $('input[name="serie"]').val('').trigger("change");
        

        ajaxreqList(medidor=medidor);












        // rpc.query({
        //     model: 'consumidor',
        //     method: 'update_marca_med_id',
        //     args: [{ 'marca_medidor_id': 43 }],
        // }).then(function (resultado) {
        //     // Manejo del resultado
        //     console.log('Eureka');
        // });


        //$('div[name="marca_medidor_id"] div div input:first').click();

        // $('div[name="marca_medidor_id"] div div input:first').trigger('focus');

        // $('div[name="marca_medidor_id"] div div input:first').val(41).trigger('input').trigger('change');

        // $('div[name="marca_medidor_id"] div div .ui-autocomplete-input').attr('value','FAE-FAE');


        // $('div[name="marca_medidor_id"] div div input:first').val('DIR-DIR').trigger('input').trigger($.Event('keydown', { keyCode: 13 }));


        // var many2oneField = $("*[name='marca_medidor_id']");
        // console.log(many2oneField);
        // Trigger the onchange event of the Many2one field
        
        // this.renderer.trigger_up('field_changed', {
        //     dataPointID: this.renderer.state.res_id,
        //     changes: {
        //         marca_medidor_id: {
        //             display_name: 'FAE-FAE',
        //             id: 42,  // Set the new value of the Many2one field
        //         },
        //     },
        // });
        
       //$('div[name="marca_medidor_id"] div div input:first').trigger("change");
       


        // let registro_id = $('span[name="id"]').html();
        // console.log(registro_id);
        // registro_id = parseInt(registro_id);
        // rpc.query({
        //     model: 'consumidor',
        //     method: 'onchange_marca_medidor_id',
        //     args: [
        //         [
        //             39
        //         ],
        //         {
        //             "marca_medidor_id": 41,
        //         },
        //         "marca_medidor_id",
        //         {
        //             "marca_medidor_id": "1",
        //         }
        //     ],
            
        // })
        // .then(function (partner_data) {
        //     console.log('final',partner_data);
        // })
        // .catch(function (error) {
        //     console.log('error',error);
        // });



        // // Obtener el objeto del campo many2one
        // var myField = $('div[name="marca_medidor_id"]').closest(".o_field_widget");
        // const my_record_id = $('span[name="id"]').html()
        // console.log(my_record_id);

        // // Actualizar el valor del campo many2one
        // myField.rpc({
        //     model: 'consumidor',
        //     method: 'write',
        //     args: [[my_record_id], { 'marca_medidor_id': 43 }],
        // }).then(function(result) {
        //     // El registro ha sido actualizado
        //     console.log('Eureka');
        // });



    });



    $(document).on('click', "#tblPup tr", function() {
        // Obtener el valor de la primera celda de la fila (el nombre)
        let code = $(this).find("td:first").text();

        // Mostrar el nombre en la consola
        console.log("Se hizo clic en la fila de " + code);

        if (dialog){
            dialog.close();
        }  

        if (code){

            $('#buscar_codigo').html('Espere...');
            $('#buscar_codigo').prop('disabled', true);
            $('#buscar_medidor').html('Espere...');
            $('#buscar_medidor').prop('disabled', true);

            $.ajax({
                type: 'GET',
                url: '/buscarCliente',
                data: { codigo: code }, 
                success: function(response) {
                    console.log('Respuesta Busqueda de cliente',response);
                    if(!(response[0][0]=='Error')){
                        $('input[name="codigo"]').val(response[1][0][0]);
                        $('input[name="codigo"]').trigger("change");
                        $('input[name="medidor"]').val(response[1][0][25]);
                        $('input[name="medidor"]').trigger("change");
                        $('input[name="nombre"]').val(response[1][0][9]+ " " + response[1][0][10]);
                        $('input[name="nombre"]').trigger("change");
                        $('input[name="direccion"]').val(response[1][0][1]+ " - " + response[1][0][6]);
                        $('input[name="direccion"]').trigger("change");
                        $('input[name="geo"]').val(response[1][0][5]);
                        $('input[name="geo"]').trigger("change");
                        $('input[name="serie"]').val(response[1][0][26]);
                        $('input[name="serie"]').trigger("change");
                        // $('input[name="marca"]').val(response[1][0][27]);
                        // $('input[name="marca"]').trigger("change");

                        let marc = (response[1][0][27]).toString().split('-');

                        ajax.jsonRpc('/marca/create', 'call', {
                            nomenclatura: marc[0],
                            descripcion: marc[1],
                        }).then(function (result) {
                            console.log('Registro creado:', result);

                            $('input[name="marca_oculta"]').val(marc[0]).trigger("change");

                        });

                    }else{
                        Dialog.alert(self, ""+response[1][0][0]+"", {
                            title: 'Error',
                        });
                    }
                },error: function(jqXHR, textStatus, errorThrown){
                    console.error(textStatus, errorThrown); // Muestra el error en la consola del navegador
                    Dialog.alert(self, ""+errorThrown+"", {
                        title: 'Error',
                    });
                },
                complete: function(jqXHR, textStatus){
                    $('#buscar_codigo').html('Buscar Código');
                    $('#buscar_codigo').prop('disabled', false);
                    $('#buscar_medidor').html('Buscar Medidor');
                    $('#buscar_medidor').prop('disabled', false);
                }
            });
        }

    });

    

    function ajaxreqList(medidor=undefined, codigo=undefined){

        $('#buscar_codigo').html('Espere...');
        $('#buscar_codigo').prop('disabled', true);
        $('#buscar_medidor').html('Espere...');
        $('#buscar_medidor').prop('disabled', true);

        let data = {}

        if (codigo){
            data = {codigo:codigo.toString()}
        }
        else if (medidor){
            data = {medidor:medidor.toString()}
        }

        console.log(data);

        $.ajax({
            type: 'GET',
            url: '/buscarCoincidencias',
            data: data, // Reemplaza '1' con el valor del id que deseas pasar como parámetro
            success: function(response) {

                console.log(response); // Muestra el resultado de la solicitud en la consola del navegador

                let cnt = '<div class="container"><div class="row"><div class="col-md-12"><table id="tblPup" class="table table-hover table-condensed table-striped" >';
                cnt+='<thead><tr>';
                response[0].forEach(element => {
                    cnt+='<th data-field="id_'+element+'" scope="col">'+element+'</th>';
                });
                cnt+='</tr></thead>';
                cnt+='<tbody>';
                response[1].forEach((element) => {
                    let d = element.join('</td><td>');
                    cnt+='<tr class="cursor-pointer" data-index="'+element[0]+'"><td>'+d+'</td></tr>';
                });
                cnt+='</tbody>';
                cnt +='</table></div></div></div>';

                showPopup(cnt);
                
            },
            error: function(xhr, textStatus, errorThrown) {
                console.error(textStatus, errorThrown); // Muestra el error en la consola del navegador
                Dialog.alert(self, ""+errorThrown+"", {
                    title: 'Error',
                });
            },
            complete: function(jqXHR, textStatus){
                $('#buscar_codigo').html('Buscar Código');
                $('#buscar_codigo').prop('disabled', false);
                $('#buscar_medidor').html('Buscar Medidor');
                $('#buscar_medidor').prop('disabled', false);
            }
        });

    }

    function showPopup(cntnt) {

        dialog = new Dialog(null, {
            title: 'Resultado',
            size: 'medium',
            $content: cntnt,
             buttons: []
        });
        
        dialog.open();
        
    }

    return {

        showPopup: showPopup,
    };
});