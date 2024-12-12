from typing import Literal
from pydantic import BaseModel, validator
from shapely.geometry import shape, mapping, Polygon, MultiPolygon

class GeoJSON(BaseModel):
    type: Literal["Polygon", "MultiPolygon"]
    coordinates: list

    @validator('type')
    def validate_type(cls, v):
        if v not in ["Polygon", "MultiPolygon"]:
            raise ValueError('Only Polygon and MultiPolygon geometries are supported')
        return v

    def to_shape(self) -> Polygon | MultiPolygon:
        geom = shape(mapping(self))
        if not isinstance(geom, (Polygon, MultiPolygon)):
            raise ValueError("Invalid geometry type")
        return geom

    @validator('coordinates')
    def validate_coordinates(cls, v, values):
        if 'type' not in values:
            raise ValueError('Type must be specified before coordinates')
        
        if values['type'] == 'Polygon':
            if not isinstance(v, list) or not v or not isinstance(v[0], list):
                raise ValueError('Invalid Polygon coordinates format')
        elif values['type'] == 'MultiPolygon':
            if not isinstance(v, list) or not v or not isinstance(v[0], list) or not v[0]:
                raise ValueError('Invalid MultiPolygon coordinates format')
        
        return v