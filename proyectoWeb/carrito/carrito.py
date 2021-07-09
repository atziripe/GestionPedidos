class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session 
        carrito = self.session.get("carrito")
        if not carrito:
            #El carrito es un diccionario
            carrito = self.session["carrito"] = {}
        else:
            self.carrito = carrito

    def agregar(self, prod):
        if str(prod.id) not in self.carrito.keys(): #verificar que el prodducto no exista ya en el carrito
            self.carrito[prod.id] = {
                "producto_id":prod.id,
                "nombre": prod.nombre,
                "precio": str(prod.precio),
                "cantidad": 1,
                "imagen": prod.imagen.url
            } 
        else:
            for key, value in self.carrito.items():
                if key == str(prod.id):
                    value["cantidad"] += 1
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carrito"] =  self.carrito
        self.session.modified = True #Modificar la sesion a true

    def eliminar_producto(self, prod):
        prod.id = str(prod.id)
        if prod.id in self.carrito:
            del self.carrito[prod.id] #Borramos el producto del diccionario
            self.guardar_carro()

    def restar_producto(self, prod):
        for key, value in self.carrito.items():
            if key == str(prod.id):
                value["cantidad"] -= 1
                if value["cantidad"] < 1:
                    self.eliminar_producto(prod)
                break
        self.guardar_carro() 
    
    def limpiar_carrito(self):
        self.session["carrito"] = {}
        self.session.modified = True