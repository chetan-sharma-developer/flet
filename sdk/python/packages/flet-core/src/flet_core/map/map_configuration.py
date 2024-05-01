import dataclasses
import json
from enum import Enum
from typing import Optional, Union

from flet_core import ControlEvent
from flet_core.control import OptionalNumber, Control
from flet_core.event_handler import EventHandler


@dataclasses.dataclass
class MapLatitudeLongitude:
    latitude: Union[float, int]
    longitude: Union[float, int]


class MapConfiguration(Control):
    def __init__(
        self,
        apply_pointer_translucency_to_layers: Optional[bool] = None,
        bgcolor: Optional[str] = None,
        initial_center: Optional[MapLatitudeLongitude] = None,
        initial_rotation: OptionalNumber = None,
        initial_zoom: OptionalNumber = None,
        keep_alive: Optional[bool] = None,
        max_zoom: OptionalNumber = None,
        min_zoom: OptionalNumber = None,
        on_tap=None,
        on_secondary_tap=None,
        on_long_press=None,
        on_init=None,
        on_event=None,
    ):
        Control.__init__(self)
        self.__on_tap = EventHandler(lambda e: TapEvent(**json.loads(e.data)))
        self._add_event_handler("tap", self.__on_tap.get_handler())

        self.__on_secondary_tap = EventHandler(lambda e: TapEvent(**json.loads(e.data)))
        self._add_event_handler("secondary_tap", self.__on_secondary_tap.get_handler())

        self.__on_long_press = EventHandler(lambda e: TapEvent(**json.loads(e.data)))
        self._add_event_handler("long_press", self.__on_long_press.get_handler())

        self.__on_event = EventHandler(lambda e: MapEvent(**json.loads(e.data)))
        self._add_event_handler("event", self.__on_event.get_handler())

        self.apply_pointer_translucency_to_layers = apply_pointer_translucency_to_layers
        self.bgcolor = bgcolor
        self.initial_center = initial_center
        self.initial_rotation = initial_rotation
        self.initial_zoom = initial_zoom
        self.keep_alive = keep_alive
        self.max_zoom = max_zoom
        self.min_zoom = min_zoom
        self.on_tap = on_tap
        self.on_secondary_tap = on_secondary_tap
        self.on_init = on_init
        self.on_long_press = on_long_press
        self.on_event = on_event

    def _get_control_name(self):
        return "mapconfiguration"

    def before_update(self):
        super().before_update()
        if isinstance(self.__initial_center, MapLatitudeLongitude):
            self._set_attr_json("initialCenter", self.__initial_center)

    # apply_pointer_translucency_to_layers
    @property
    def apply_pointer_translucency_to_layers(self) -> Optional[bool]:
        return self._get_attr("applyPointerTranslucencyToLayers", data_type="bool")

    @apply_pointer_translucency_to_layers.setter
    def apply_pointer_translucency_to_layers(self, value: Optional[bool]):
        self._set_attr("applyPointerTranslucencyToLayers", value)

    # bgcolor
    @property
    def bgcolor(self) -> Optional[str]:
        return self._get_attr("bgcolor")

    @bgcolor.setter
    def bgcolor(self, value: Optional[str]):
        self._set_attr("bgcolor", value)

    # initial_center
    @property
    def initial_center(self) -> Optional[MapLatitudeLongitude]:
        return self.__initial_center

    @initial_center.setter
    def initial_center(self, value: Optional[MapLatitudeLongitude]):
        self.__initial_center = value

    # initial_rotation
    @property
    def initial_rotation(self) -> OptionalNumber:
        return self._get_attr("initialRotation", data_type="float")

    @initial_rotation.setter
    def initial_rotation(self, value: OptionalNumber):
        self._set_attr("initialRotation", value)

    # initial_zoom
    @property
    def initial_zoom(self) -> OptionalNumber:
        return self._get_attr("initialZoom", data_type="float")

    @initial_zoom.setter
    def initial_zoom(self, value: OptionalNumber):
        self._set_attr("initialZoom", value)

    # keep_alive
    @property
    def keep_alive(self) -> Optional[bool]:
        return self._get_attr("keepAlive", data_type="bool")

    @keep_alive.setter
    def keep_alive(self, value: Optional[bool]):
        self._set_attr("keepAlive", value)

    # max_zoom
    @property
    def max_zoom(self) -> OptionalNumber:
        return self._get_attr("maxZoom", data_type="float")

    @max_zoom.setter
    def max_zoom(self, value: OptionalNumber):
        self._set_attr("maxZoom", value)

    # min_zoom
    @property
    def min_zoom(self) -> OptionalNumber:
        return self._get_attr("minZoom", data_type="float")

    @min_zoom.setter
    def min_zoom(self, value: OptionalNumber):
        self._set_attr("minZoom", value)

    # on_tap
    @property
    def on_tap(self):
        return self.__on_tap

    @on_tap.setter
    def on_tap(self, handler):
        self.__on_tap.subscribe(handler)
        self._set_attr("onTap", True if handler is not None else None)

    # on_secondary_tap
    @property
    def on_secondary_tap(self):
        return self.__on_secondary_tap

    @on_secondary_tap.setter
    def on_secondary_tap(self, handler):
        self.__on_secondary_tap.subscribe(handler)
        self._set_attr("onSecondaryTap", True if handler is not None else None)

    # on_long_press
    @property
    def on_long_press(self):
        return self.__on_long_press

    @on_long_press.setter
    def on_long_press(self, handler):
        self.__on_long_press.subscribe(handler)
        self._set_attr("onLongPress", True if handler is not None else None)

    # on_event
    @property
    def on_event(self):
        return self.__on_event

    @on_event.setter
    def on_event(self, handler):
        self.__on_event.subscribe(handler)
        self._set_attr("onEvent", True if handler is not None else None)

    # on_init
    @property
    def on_init(self):
        return self._get_event_handler("init")

    @on_init.setter
    def on_init(self, handler):
        self._add_event_handler("init", handler)
        self._set_attr("onInit", True if handler is not None else None)


class TapEvent(ControlEvent):
    def __init__(self, lat, long, gx, gy, lx, ly) -> None:
        self.local_x: Optional[float] = lx
        self.local_y: Optional[float] = ly
        self.global_x: float = gx
        self.global_y: float = gy
        self.location: MapLatitudeLongitude = MapLatitudeLongitude(lat, long)


class MapEventSource(Enum):
    MAP_CONTROLLER = "mapController"
    TAP = "tap"
    SECONDARY_TAP = "secondaryTap"
    LONG_PRESS = "longPress"
    DOUBLE_TAP = "doubleTap"
    DOUBLE_TAP_HOLD = "doubleTapHold"
    DRAG_START = "dragStart"
    ON_DRAG = "onDrag"
    DRAG_END = "dragEnd"
    MULTI_FINGER_GESTURE_START = "multiFingerGestureStart"
    ON_MULTI_FINGER = "onMultiFinger"
    MULTI_FINGER_GESTURE_END = "multiFingerEnd"
    FLING_ANIMATION_CONTROLLER = "flingAnimationController"
    DOUBLE_TAP_ZOOM_ANIMATION_CONTROLLER = "doubleTapZoomAnimationController"
    INTERACTIVE_FLAGS_CHANGED = "interactiveFlagsChanged"
    FIT_CAMERA = "fitCamera"
    CUSTOM = "custom"
    SCROLL_WHEEL = "scrollWheel"
    NON_ROTATED_SIZE_CHANGE = "nonRotatedSizeChange"
    CURSOR_KEYBOARD_ROTATION = "cursorKeyboardRotation"


class MapEvent(ControlEvent):
    def __init__(self, src, c_lat, c_long, zoom, rot) -> None:
        self.source: MapEventSource = MapEventSource(src)
        self.center: MapLatitudeLongitude = MapLatitudeLongitude(c_lat, c_long)
        self.zoom: float = zoom
        self.rotation: float = rot