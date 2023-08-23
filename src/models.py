from structure import BaseModel, SimpleField, ListField


class Lojas(BaseModel):
    name = SimpleField(str)
    per_cent_motoboy = SimpleField(float)


class LojasList(BaseModel):
    lojas = ListField(SimpleField(Lojas))

    def get_loja_by_name(self, name):
        for loja in self.lojas:
            if loja.name == name:
                return loja
        return None

class Pedidos(BaseModel):
    name = SimpleField(str)
    loja = SimpleField(str)
    price = SimpleField(int)


class PedidosList(BaseModel):
    pedidos = ListField(SimpleField(Pedidos))


class Motoboy(BaseModel):
    name = SimpleField(str)
    lojas = SimpleField(list)
    fixed_cost = SimpleField(int)


class MotoboyList(BaseModel):
    motoboys = ListField(SimpleField(Motoboy))
