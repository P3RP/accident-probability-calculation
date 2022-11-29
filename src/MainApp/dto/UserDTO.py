import dataclasses as dc


@dc.dataclass(unsafe_hash=True)
class UserDTO:
    id: str = ''
    sex: int = 0
    age: int = 0
    expr: int = 0
