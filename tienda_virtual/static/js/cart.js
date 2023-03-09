var btnagregarCarrito = document.getElementsByClassName('actualizar-carrito')

for(var i= 0; i < btnagregarCarrito.length; i++){
    btnagregarCarrito[i].addEventListener('click', function(){
        var producto_id = this.dataset.producto
        var accion = this.dataset.accion
        
        console.log('Id producto: ' , producto_id, 'Accion:', accion)

        console.log('Usuario: ', usuario)

        if(usuario == 'AnonymousUser'){
            // console.log('No se a logeado')
            agregarCookieItem(producto_id, accion)
        }
        else{
            // console.log('Usuario logeado, enviando información...')
            actulizar_pedido_usuario(producto_id, accion)
        }
    })
}

function agregarCookieItem(id_producto, accion){
    console.log('No se a logeado')

    if (accion == 'add'){
        if(cart[id_producto] == undefined){
            cart[id_producto] = {
                'cantidad': 1
            }
        }else{
            cart[id_producto]['cantidad'] += 1
        }
    }

    if (accion == 'remove'){
        cart[id_producto]['cantidad'] -= 1

        if(cart[id_producto]['cantidad']  <= 0){
            console.log("Item eliminado")
            delete cart[id_producto]
        }
    }

    console.log("Cart:", cart)
    document.cookie = 'cart='+ JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}

function actulizar_pedido_usuario(id_producto, accion){
    console.log('Usuario logeado, enviando información...')
    
    var url = '/actualizar_item'

    fetch(url, {
        method :'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'id_producto': id_producto, 'accion': accion})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}