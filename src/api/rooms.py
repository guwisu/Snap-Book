from datetime import date

from fastapi import Body, Query, APIRouter

from src.exceptions import (
    HotelNotFoundHTTPException,
    RoomNotFoundHTTPException,
    RoomNotFoundException,
    HotelNotFoundException,
    FacilityNotFoundException,
    FacilityNotFoundHTTPException,
    ObjectNotFoundException,
    ObjectNotFoundHTTPException,
    RoomEmptyDataHTTPException,
    RoomEmptyDataException,
    HotelAndRoomNotRelatedException,
    HotelAndRoomNotRelatedHTTPException,
)
from src.schemas.rooms import RoomAddRequest, RoomPatchRequest
from src.api.dependencies import DBDep
from src.services.rooms import RoomService

router = APIRouter(prefix="/hotels", tags=["Rooms"])


@router.get("/{hotel_id}/rooms")
async def get_rooms(
    db: DBDep,
    hotel_id: int,
    date_from: date = Query(example="2025-03-07"),
    date_to: date = Query(example="2025-03-15"),
):
    try:
        return await RoomService(db).get_filtered_by_time(hotel_id, date_from, date_to)
    except HotelNotFoundException:
        raise HotelNotFoundHTTPException


@router.get("/{hotel_id}/rooms/{room_id}")
async def get_room_by_id(db: DBDep, hotel_id: int, room_id: int):
    try:
        return await RoomService(db).get_room(hotel_id, room_id)
    except ObjectNotFoundException:
        raise ObjectNotFoundHTTPException


@router.post("/{hotel_id}/rooms")
async def create_room(db: DBDep, hotel_id: int, room_data: RoomAddRequest = Body()):
    try:
        room = await RoomService(db).create_room(hotel_id, room_data)
    except HotelNotFoundException:
        raise HotelNotFoundHTTPException
    except FacilityNotFoundException:
        raise FacilityNotFoundHTTPException
    except RoomEmptyDataException:
        raise RoomEmptyDataHTTPException

    return {"status": "OK", "data": room}


@router.put("/{hotel_id}/rooms/{room_id}")
async def edit_room(db: DBDep, hotel_id: int, room_id: int, room_data: RoomAddRequest):
    try:
        room = await RoomService(db).edit_room(hotel_id, room_id, room_data)
        return {"status": "OK", "data": room}
    except RoomEmptyDataException:
        raise RoomEmptyDataHTTPException
    except FacilityNotFoundException:
        raise FacilityNotFoundHTTPException
    except HotelNotFoundException:
        raise HotelNotFoundHTTPException
    except RoomNotFoundException:
        raise RoomNotFoundHTTPException
    except HotelAndRoomNotRelatedException:
        raise HotelAndRoomNotRelatedHTTPException


@router.patch("/{hotel_id}/rooms/{room_id}")
async def patch_room(db: DBDep, hotel_id: int, room_id: int, room_data: RoomPatchRequest):
    try:
        room = await RoomService(db).partially_edit_room(hotel_id, room_id, room_data)
        return {"status": "OK", "data": room}
    except RoomEmptyDataException:
        raise RoomEmptyDataHTTPException
    except FacilityNotFoundException:
        raise FacilityNotFoundHTTPException
    except HotelNotFoundException:
        raise HotelNotFoundHTTPException
    except RoomNotFoundException:
        raise RoomNotFoundHTTPException
    except HotelAndRoomNotRelatedException:
        raise HotelAndRoomNotRelatedHTTPException


@router.delete("/{hotel_id}/rooms/{room_id}")
async def delete_room(db: DBDep, hotel_id: int, room_id: int):
    try:
        await RoomService(db).delete_room(hotel_id, room_id)
        return {"status": "OK"}
    except RoomNotFoundException:
        raise RoomNotFoundHTTPException
    except HotelNotFoundException:
        raise HotelNotFoundHTTPException
    except HotelAndRoomNotRelatedException:
        raise HotelAndRoomNotRelatedHTTPException
