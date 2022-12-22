
    var mymap;
    var marker;
    var lat = -2.356;
    var lng = -77.157;
    var utmLatLngProvider= new utmLatLng();

    function cargar_Coordenada(){

        let x=$('input[name="coord_x"]').val();
        let y=$('input[name="coord_y"]').val();
        try{
            x=parseFloat(x.toString().replace(",","."));
            y=parseFloat(y.toString().replace(",","."));
        }catch (e){
            x=$('span[name="coord_x"]').html();
            y=$('span[name="coord_y"]').html();
            try{
                x=parseFloat(x.toString().replace(",","."));
                y=parseFloat(y.toString().replace(",","."));
            }catch (e){}
        }

        let lt=$('input[name="latitud"]').val();
        let ln=$('input[name="longitud"]').val();
        try{
            lt=parseFloat(lt.toString().replace(",","."));
            ln=parseFloat(ln.toString().replace(",","."));

        }catch (e){
            lt=$('span[name="latitud"]').html();
            ln=$('span[name="longitud"]').html();

            try{
                lt=parseFloat(lt.toString().replace(",","."));
                ln=parseFloat(ln.toString().replace(",","."));
            }catch (e){}
        }

        console.info(x);
        console.info(y);
        console.info(lt);
        console.info(ln);


        let coordT;

        switch (true) {
            case (((lt!==0 && lt!==undefined && !isNaN(lt)) &&
                (ln!==0 && ln!==undefined && !isNaN(ln))) &&
                ((x!==0 && x!==undefined && !isNaN(x)) &&
                    (y!==0 && y!==undefined && !isNaN(y)))):{

                console.log("lat,lng,x,y");
                ubicar_Marcador(lt,ln);
                break;
            }
            case ((x!==0 && x!==undefined && !isNaN(x)) && (y!==0 && y!==undefined && !isNaN(y))):{

                console.log("x,y");
                coordT = utmLatLngProvider.convertUtmToLatLng(x, y, 17, 'S');
                lt = coordT.lat;
                ln = coordT.lng;
                ubicar_Marcador(lt, ln);
                try{
                    x=parseFloat(x.toString().replace(".",","));
                    y=parseFloat(y.toString().replace(".",","));
                }catch (e){
                    x=$('span[name="coord_x"]').html();
                    y=$('span[name="coord_y"]').html();
                    try{
                        x=parseFloat(x.toString().replace(".",","));
                        y=parseFloat(y.toString().replace(".",","));
                    }catch (e){}
                }
                llenar_Valores(lt, ln, x, y);

                break;
            }
            case ((lt!==0 && lt!==undefined && !isNaN(lt)) && (ln!==0 && ln!==undefined && !isNaN(ln))):{

                console.log("lat,lng");
                coordT = utmLatLngProvider.convertLatLngToUtm(lt, ln, 0);
                ubicar_Marcador(lt, ln);
                try{
                    lt=parseFloat(lt.toString().replace(".",","));
                    ln=parseFloat(ln.toString().replace(".",","));

                }catch (e){
                    lt=$('span[name="latitud"]').html();
                    ln=$('span[name="longitud"]').html();

                    try{
                        lt=parseFloat(lt.toString().replace(".",","));
                        ln=parseFloat(ln.toString().replace(".",","));
                    }catch (e){}
                }
                llenar_Valores(lt, ln, coordT.Easting, coordT.Northing);
                break;
            }

        }


    }

    function ubicar_Marcador(lt,ln){

        lat = lt;
        lng = ln;

        if (marker===undefined){
            marker = new L.Marker([lat, lng]);
            marker.addTo(mymap);
        }else{
            marker.setLatLng([lat, lng]);
        }
        mymap.flyTo([lat, lng], 18);

    }

    function llenar_Valores(lt, ln, x, y){

        $('input[name="coord_x"]').val(x);
        $('input[name="coord_x"]').trigger("change");
        $('input[name="coord_y"]').val(y);
        $('input[name="coord_y"]').trigger("change");

        //$('input[name="latitud"]').val(lat);
        $('input[name="latitud"]').val(lt.toString().replace(".",","));
        $('input[name="latitud"]').trigger("change");


        //$('input[name="longitud"]').val(lng);
        $('input[name="longitud"]').val(ln.toString().replace(".",","));
        $('input[name="longitud"]').trigger("change");

    }

    function encontrar_coordenada_Actual(){
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {

            /*console.info("Tu ubicación actual es:", position);*/

            ubicar_Marcador(position.coords.latitude,position.coords.longitude);


            let coordT = utmLatLngProvider.convertLatLngToUtm(lat, lng, 0);

            /*console.log(coordT);*/
            llenar_Valores(lat, lng, coordT.Easting, coordT.Northing);

          });
        } else {
          console.log("Tu navegador no soporta la API de Geolocalización.");
        }

    }

    function cargar_Mapa_Leaflet(){

      if ($('#mapid').length){

          let point = new L.LatLng(lat, lng);
          mymap = L.map('mapid', {zoomControl: false}).setView(point, 6);
          L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
              attribution: "Map data © <a href='http://openstreetmap.org'>OpenStreetMap</a> contributors"
          }).addTo(mymap);

          setTimeout(function () { mymap.invalidateSize() }, 400);
          console.log(mymap);

          marker=undefined;

          cargar_Coordenada();

      }

    }

    cargar_Mapa_Leaflet();

    $("#ubicar").on("click", function (ev) {
        console.info("Click para encontrar ubicación");
        encontrar_coordenada_Actual();
    });

    $("#presentar").on("click", function (ev) {
        console.info("Click para Verificacion de Coordenadas y ubicar en mapa");
        cargar_Coordenada();
    });

