from app.database.models.event import Event, EventTags


class FilterService:
    def __init__(self, filter_spec):
        self.model_class = Event
        self.field = filter_spec["field"]
        self.op = filter_spec.get("op", "==")
        self.value = filter_spec.get("value")

    def to_expression(self):
        field = getattr(self.model_class, self.field)
        if self.op == "==":
            if isinstance(self.value, EventTags):
                self.value = self.value.value
            return field == self.value
        elif self.op == "!=":
            if isinstance(self.value, EventTags):
                self.value = self.value.value
            return field != self.value
        elif self.op == ">":
            return field > self.value
        elif self.op == ">=":
            return field >= self.value
        elif self.op == "<":
            return field < self.value
        elif self.op == "<=":
            return field <= self.value
        elif self.op == "like":
            return field.like(self.value)
        elif self.op == "ilike":
            return field.ilike(self.value)
        elif self.op == "is_null":
            return field.is_(None)
        elif self.op == "is_not_null":
            return field.isnot(None)
        elif self.op == "in":
            if isinstance(self.value, list) and all(
                isinstance(val, EventTags) for val in self.value
            ):
                self.value = [val.value for val in self.value]
            return field.in_(self.value)
        else:
            raise ValueError(f"Unknown operator {self.op}")
