from structure import BaseModel, SimpleField, ListField


class Lojas(BaseModel):
    name = SimpleField(str)
    per_cent_motoboy = SimpleField(int)


class LojasList(BaseModel):
    lojas = ListField(SimpleField(Lojas))


class Pedidos(BaseModel):
    name = SimpleField(str)
    loja = SimpleField(str)
    price = SimpleField(int)


class PedidosList(BaseModel):
    pedidos = ListField(SimpleField(Lojas))


class Motoboy(BaseModel):
    name = SimpleField(str)
    loja = SimpleField(list)
    fixed_cost = SimpleField(int)


class MotoboyList(BaseModel):
    motoboys = ListField(SimpleField(Motoboy))