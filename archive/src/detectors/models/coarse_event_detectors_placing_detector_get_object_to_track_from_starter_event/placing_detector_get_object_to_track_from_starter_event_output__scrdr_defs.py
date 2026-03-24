from typing_extensions import Optional, Type, Union
from archive.src.detectors.coarse_event_detectors import PlacingDetector
from pycram.world_concepts.world_object import Object
from segmind.datastructures.mixins import HasPrimaryTrackedObject
from segmind.datastructures.events import CloseContactEvent
from types import NoneType


def conditions_157980724165316319734190707637955950660(case) -> bool:
    def conditions_for_placing_detector_get_object_to_track_from_starter_event(cls_: Type[PlacingDetector], starter_event: CloseContactEvent, output_: Union[NoneType, Object]) -> bool:
        """Get conditions on whether it's possible to conclude a value for PlacingDetector_get_object_to_track_from_starter_event.output_  of type Object."""
        return isinstance(starter_event, HasPrimaryTrackedObject)
    return conditions_for_placing_detector_get_object_to_track_from_starter_event(**case)


def conclusion_157980724165316319734190707637955950660(case) -> Optional[Object]:
    def placing_detector_get_object_to_track_from_starter_event(cls_: Type[PlacingDetector], starter_event: CloseContactEvent, output_: Union[NoneType, Object]) -> Union[NoneType, Object]:
        """Get possible value(s) for PlacingDetector_get_object_to_track_from_starter_event.output_  of type Object."""
        return starter_event.tracked_object
    return placing_detector_get_object_to_track_from_starter_event(**case)


