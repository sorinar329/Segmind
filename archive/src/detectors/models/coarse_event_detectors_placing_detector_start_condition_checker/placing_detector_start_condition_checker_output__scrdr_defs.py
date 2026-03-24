from typing_extensions import Type
from segmind.datastructures.events import EventWithOneTrackedObject, SupportEvent
from archive.src.detectors.coarse_event_detectors import PlacingDetector


def conditions_124701724059586364685260806439568356831(case) -> bool:
    def conditions_for_placing_detector_start_condition_checker(cls_: Type[PlacingDetector], event: EventWithOneTrackedObject, output_: bool) -> bool:
        """Get conditions on whether it's possible to conclude a value for PlacingDetector_start_condition_checker.output_  of type ."""
        return isinstance(event, SupportEvent)
    return conditions_for_placing_detector_start_condition_checker(**case)


def conclusion_124701724059586364685260806439568356831(case) -> bool:
    def placing_detector_start_condition_checker(cls_: Type[PlacingDetector], event: EventWithOneTrackedObject, output_: bool) -> bool:
        """Get possible value(s) for PlacingDetector_start_condition_checker.output_  of type ."""
        return True
    return placing_detector_start_condition_checker(**case)


