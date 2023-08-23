class Field:
    def validate(self, value):
        raise NotImplementedError("validate method must be implemented by subclasses")


class SimpleField(Field):
    def __init__(self, type_):
        self.type_ = type_

    def validate(self, value):
        if not isinstance(value, self.type_):
            raise ValueError(f"Expected value of type {self.type_}, but got {type(value)}")
        return value


class ListField(Field):
    def __init__(self, field: Field):
        self.field = field

    def validate(self, value):
        if not isinstance(value, list):
            raise ValueError(f"Expected a list, but got {type(value)}")

        return [self.field.validate(item) for item in value]


class ModelMeta(type):
    def __new__(cls, name, bases, dct):
        fields = {}
        for attr_name, attr_value in dct.items():
            if isinstance(attr_value, Field):
                fields[attr_name] = attr_value

        dct['_fields'] = fields
        return super().__new__(cls, name, bases, dct)


class BaseModel(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for field_name, field in self._fields.items():
            value = kwargs.get(field_name)
            if value is None:
                raise ValueError(f"Field {field_name} is required.")
            setattr(self, field_name, field.validate(value))
