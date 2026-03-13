"""
Work Breakdown Structure Reference

1. [MIL-STD-881F Work Breakdown Structures for Defense Materiel Items](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=36026)
2. [SAWE RP A-8, 2015a: Weight and Balance Data Reporting Forms for Aircraft (including Rotorcraft and Air-Breathing Unmanned Aerial Vehicles)](https://www.sawe.org/product/sawe-rp-a-8-2015a/)

"""

from typing import Optional

from pydantic import ConfigDict, Field

from adh.msosa.architecture import Architecture
from adh.wbs.airframe.airframe import Component
from adh.wbs.propulsion.propulsion import Propulsion


class AircraftSystem(Architecture):
    wbs_no: Optional[str] = Field("1.0")

    model_config = ConfigDict(validate_assignment=True, extra="allow")

    class AircraftSystemIntegrationAssemblyTestAndCheckout(Architecture):
        wbs_no: Optional[str] = Field("1.1")

        model_config = ConfigDict(validate_assignment=True, extra="allow")

    class AirVehicle(Architecture):
        wbs_no: Optional[str] = Field("1.2")

        model_config = ConfigDict(validate_assignment=True, extra="allow")

        class AirVehicleIntegrationAssemblyTestAndCheckout(Architecture):
            wbs_no: Optional[str] = Field("1.2.1")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class Airframe(Architecture):
            wbs_no: Optional[str] = Field("1.2.2")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

            class AirframeIntegrationAssemblyTestAndCheckout(Architecture):
                wbs_no: Optional[str] = Field("1.2.2.1")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Fuselage(Architecture):
                wbs_no: Optional[str] = Field("1.2.2.2")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

                class BasicStructure(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.2.1")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                    class Skins(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.2.1.1")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Stringers(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.2.1.2")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Frames(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.2.1.3")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Clips(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.2.1.4")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Beams(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.2.1.5")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Floors(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.2.1.6")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Bulkheads(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.2.1.7")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Longerons(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.2.1.8")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Supports(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.2.1.9")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                class SecondaryStructure(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.2.2")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                    class Enclosures(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.2.2.1")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Flooring(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.2.2.2")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Partitions(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.2.2.3")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Windows(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.2.2.4")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Doors(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.2.2.5")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Ramps(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.2.2.6")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Panels(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.2.2.7")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Misc(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.2.2.8")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

            class Wing(Architecture):
                wbs_no: Optional[str] = Field("1.2.2.3")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

                class BasicStructure(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.3.1")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                    class CenterSection(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.3.1.1")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                        class Skins(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.3.1.1.1")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                        class Spars(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.3.1.1.2")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                        class Ribs(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.3.1.1.3")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                        class Stringers(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.3.1.1.4")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                        class Clips(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.3.1.1.5")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                    class IntermediatePanel(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.3.1.2")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                        class Skins(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.3.1.2.1")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                        class Spars(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.3.1.2.2")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                        class Ribs(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.3.1.2.3")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                        class Stringers(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.3.1.2.4")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                        class Clips(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.3.1.2.5")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                    class OuterPanel(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.3.1.3")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                        class Skins(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.3.1.3.1")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                        class Spars(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.3.1.3.2")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                        class Ribs(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.3.1.3.3")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                        class Stringers(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.3.1.3.4")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                        class Clips(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.3.1.3.5")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                class SecondaryStructure(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.3.2")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                    class AccessPanels(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.3.2.1")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                class Ailerons(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.3.3")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class Elevons(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.3.4")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class Spoilers(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.3.5")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class TrailingEdgeFlaps(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.3.6")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class LeadingEdgeFlaps(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.3.7")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class Slats(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.3.8")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Empennage(Architecture):
                wbs_no: Optional[str] = Field("1.2.2.4")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

                class Stabilizer(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.4.1")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                    class BasicStructure(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.4.1.1")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                        class CenterSection(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.4.1.1.1")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                            class Skins(Architecture):
                                wbs_no: Optional[str] = Field("1.2.2.4.1.1.1.1")

                                model_config = ConfigDict(
                                    validate_assignment=True, extra="allow"
                                )

                            class Spars(Architecture):
                                wbs_no: Optional[str] = Field("1.2.2.4.1.1.1.2")

                                model_config = ConfigDict(
                                    validate_assignment=True, extra="allow"
                                )

                            class Ribs(Architecture):
                                wbs_no: Optional[str] = Field("1.2.2.4.1.1.1.3")

                                model_config = ConfigDict(
                                    validate_assignment=True, extra="allow"
                                )

                            class Stringers(Architecture):
                                wbs_no: Optional[str] = Field("1.2.2.4.1.1.1.4")

                                model_config = ConfigDict(
                                    validate_assignment=True, extra="allow"
                                )

                            class Clips(Architecture):
                                wbs_no: Optional[str] = Field("1.2.2.4.1.1.1.5")

                                model_config = ConfigDict(
                                    validate_assignment=True, extra="allow"
                                )

                        class IntermediatePanel(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.4.1.1.2")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                            class Skins(Architecture):
                                wbs_no: Optional[str] = Field("1.2.2.4.1.1.2.1")

                                model_config = ConfigDict(
                                    validate_assignment=True, extra="allow"
                                )

                            class Spars(Architecture):
                                wbs_no: Optional[str] = Field("1.2.2.4.1.1.2.2")

                                model_config = ConfigDict(
                                    validate_assignment=True, extra="allow"
                                )

                            class Ribs(Architecture):
                                wbs_no: Optional[str] = Field("1.2.2.4.1.1.2.3")

                                model_config = ConfigDict(
                                    validate_assignment=True, extra="allow"
                                )

                            class Stringers(Architecture):
                                wbs_no: Optional[str] = Field("1.2.2.4.1.1.2.4")

                                model_config = ConfigDict(
                                    validate_assignment=True, extra="allow"
                                )

                            class Clips(Architecture):
                                wbs_no: Optional[str] = Field("1.2.2.4.1.1.2.5")

                                model_config = ConfigDict(
                                    validate_assignment=True, extra="allow"
                                )

                        class OuterPanel(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.4.1.1.3")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                            class Skins(Architecture):
                                wbs_no: Optional[str] = Field("1.2.2.4.1.1.3.1")

                                model_config = ConfigDict(
                                    validate_assignment=True, extra="allow"
                                )

                            class Spars(Architecture):
                                wbs_no: Optional[str] = Field("1.2.2.4.1.1.3.2")

                                model_config = ConfigDict(
                                    validate_assignment=True, extra="allow"
                                )

                            class Ribs(Architecture):
                                wbs_no: Optional[str] = Field("1.2.2.4.1.1.3.3")

                                model_config = ConfigDict(
                                    validate_assignment=True, extra="allow"
                                )

                            class Stringers(Architecture):
                                wbs_no: Optional[str] = Field("1.2.2.4.1.1.3.4")

                                model_config = ConfigDict(
                                    validate_assignment=True, extra="allow"
                                )

                            class Clips(Architecture):
                                wbs_no: Optional[str] = Field("1.2.2.4.1.1.3.5")

                                model_config = ConfigDict(
                                    validate_assignment=True, extra="allow"
                                )

                    class SecondaryStructure(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.4.2")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                        class AccessPanels(Architecture):
                            wbs_no: Optional[str] = Field("1.2.2.4.2.1")

                            model_config = ConfigDict(
                                validate_assignment=True, extra="allow"
                            )

                class Ailerons(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.4.3")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class Elevons(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.4.4")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class Spoilers(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.4.5")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class TrailingEdgeFlaps(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.4.6")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class LeadingEdgeFlaps(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.4.7")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class Slats(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.4.8")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Nacelle(Component):
                wbs_no: Optional[str] = Field("1.2.2.5")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

                class BasicStructure(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.5.1")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                    class Skins(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.5.1.1")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Stringers(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.5.1.2")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Frames(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.5.1.3")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Clips(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.5.1.4")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Beams(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.5.1.5")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Floors(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.5.1.6")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Bulkheads(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.5.1.7")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Longerons(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.5.1.8")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Supports(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.5.1.9")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                class SecondaryStructure(Architecture):
                    wbs_no: Optional[str] = Field("1.2.2.5.2")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                    class Enclosures(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.5.2.1")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Flooring(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.5.2.2")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Partitions(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.5.2.3")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Windows(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.5.2.4")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Doors(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.5.2.5")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Ramps(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.5.2.6")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Panels(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.5.2.7")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

                    class Misc(Architecture):
                        wbs_no: Optional[str] = Field("1.2.2.5.2.8")

                        model_config = ConfigDict(
                            validate_assignment=True, extra="allow"
                        )

        class Propulsion(Architecture):
            wbs_no: Optional[str] = Field("1.2.3")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Engine(Propulsion):
                wbs_no: Optional[str] = Field("1.2.3.1")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class EngineInstallation(Architecture):
                wbs_no: Optional[str] = Field("1.2.3.2")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class AccessoryGearBoxesAndDrive(Architecture):
                wbs_no: Optional[str] = Field("1.2.3.3")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class ExhaustSystem(Architecture):
                wbs_no: Optional[str] = Field("1.2.3.4")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class EngineCooling(Architecture):
                wbs_no: Optional[str] = Field("1.2.3.5")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class WaterInjection(Architecture):
                wbs_no: Optional[str] = Field("1.2.3.6")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class EngineControls(Architecture):
                wbs_no: Optional[str] = Field("1.2.3.7")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class StartingSystem(Architecture):
                wbs_no: Optional[str] = Field("1.2.3.8")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class PropellerOrFanInstallation(Architecture):
                wbs_no: Optional[str] = Field("1.2.3.9")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class LubricatingSystem(Architecture):
                wbs_no: Optional[str] = Field("1.2.3.10")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class FuelSystem(Architecture):
                wbs_no: Optional[str] = Field("1.2.3.11")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

                class ProtectedTanks(Architecture):
                    wbs_no: Optional[str] = Field("1.2.3.11.1")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class UnprotectedTanks(Architecture):
                    wbs_no: Optional[str] = Field("1.2.3.11.2")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class Plumbing(Architecture):
                    wbs_no: Optional[str] = Field("1.2.3.11.3")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class Etc(Architecture):
                    wbs_no: Optional[str] = Field("1.2.3.11.4")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

            class DriveSystem(Architecture):
                wbs_no: Optional[str] = Field("1.2.3.12")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

                class GearBoxes(Architecture):
                    wbs_no: Optional[str] = Field("1.2.3.12.1")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class LubSys(Architecture):
                    wbs_no: Optional[str] = Field("1.2.3.12.2")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class RtrBrk(Architecture):
                    wbs_no: Optional[str] = Field("1.2.3.12.3")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class TransmissionDrive(Architecture):
                    wbs_no: Optional[str] = Field("1.2.3.12.4")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class RotorShaft(Architecture):
                    wbs_no: Optional[str] = Field("1.2.3.12.5")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class GasDrive(Architecture):
                    wbs_no: Optional[str] = Field("1.2.3.12.6")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

        class VehicleSubsystems(Architecture):
            wbs_no: Optional[str] = Field("1.2.4")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

            class VehicleSubsystemIntegrationAssemblyTestAndCheckout(Architecture):
                wbs_no: Optional[str] = Field("1.2.4.1")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class FlightControlSubsystem(Architecture):
                wbs_no: Optional[str] = Field("1.2.4.2")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

                class CockpitControls(Architecture):
                    wbs_no: Optional[str] = Field("1.2.4.2.1")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class AutomaticFlightControlSystem(Architecture):
                    wbs_no: Optional[str] = Field("1.2.4.2.2")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class SystemControls(Architecture):
                    wbs_no: Optional[str] = Field("1.2.4.2.3")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

            class AuxiliaryPowerSubsystem(Architecture):
                wbs_no: Optional[str] = Field("1.2.4.3")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class HydraulicSubsystem(Architecture):
                wbs_no: Optional[str] = Field("1.2.4.4")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class ElectricalAntiIcingSystem(Architecture):
                wbs_no: Optional[str] = Field("1.2.4.5")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class CrewStationSubsystem(Architecture):
                wbs_no: Optional[str] = Field("1.2.4.6")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class EnvironmentalControlSubsystem(Architecture):
                wbs_no: Optional[str] = Field("1.2.4.7")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class FuelSubsystem(Architecture):
                wbs_no: Optional[str] = Field("1.2.4.8")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Instruments(Architecture):
                wbs_no: Optional[str] = Field("1.2.4.9")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class PneumaticSubsystem(Architecture):
                wbs_no: Optional[str] = Field("1.2.4.10")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class AntiIcingSubsystem(Architecture):
                wbs_no: Optional[str] = Field("1.2.4.11")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class VehicleSubsystemSoftware(Architecture):
                wbs_no: Optional[str] = Field("1.2.4.12")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class OtherSubsystems(Architecture):
                wbs_no: Optional[str] = Field("1.2.4.13")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

        class Avionics(Architecture):
            wbs_no: Optional[str] = Field("1.2.5")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

            class AvionicsIntegrationAssemblyTestAndCheckout(Architecture):
                wbs_no: Optional[str] = Field("1.2.5.1")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class CommunicationIdentification(Architecture):
                wbs_no: Optional[str] = Field("1.2.5.2")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class NavigationGuidance(Architecture):
                wbs_no: Optional[str] = Field("1.2.5.3")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class MissionComputerProcessing(Architecture):
                wbs_no: Optional[str] = Field("1.2.5.4")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class FireControl(Architecture):
                wbs_no: Optional[str] = Field("1.2.5.5")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class DataDisplayAndControls(Architecture):
                wbs_no: Optional[str] = Field("1.2.5.6")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Survivability(Architecture):
                wbs_no: Optional[str] = Field("1.2.5.7")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Reconnaissance(Architecture):
                wbs_no: Optional[str] = Field("1.2.5.8")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class ElectronicWarfare(Architecture):
                wbs_no: Optional[str] = Field("1.2.5.9")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class AutomaticFlightControl(Architecture):
                wbs_no: Optional[str] = Field("1.2.5.10")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class HealthMonitoringSystem(Architecture):
                wbs_no: Optional[str] = Field("1.2.5.11")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class StoresManagement(Architecture):
                wbs_no: Optional[str] = Field("1.2.5.12")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class AvionicsSoftwareRelease(Architecture):
                wbs_no: Optional[str] = Field("1.2.5.13")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class OtherAvionicsSubsystems(Architecture):
                wbs_no: Optional[str] = Field("1.2.5.14")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Installation(Architecture):
                wbs_no: Optional[str] = Field("1.2.5.15")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

        class ArmamentWeaponsDelivery(Architecture):
            wbs_no: Optional[str] = Field("1.2.6")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class AuxiliaryEquipment(Architecture):
            wbs_no: Optional[str] = Field("1.2.7")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class FurnishingsAndEquipment(Architecture):
            wbs_no: Optional[str] = Field("1.2.8")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

            class AccommodationForPersonnel(Architecture):
                wbs_no: Optional[str] = Field("1.2.8.1")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class MiscellaneousEquipment(Architecture):
                wbs_no: Optional[str] = Field("1.2.8.2")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Furnishings(Architecture):
                wbs_no: Optional[str] = Field("1.2.8.3")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class EmergencyEquipment(Architecture):
                wbs_no: Optional[str] = Field("1.2.8.4")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

        class AirVehicleSoftwareRelease(Architecture):
            wbs_no: Optional[str] = Field("1.2.9")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class LoadAndHandlingSystem(Architecture):
            wbs_no: Optional[str] = Field("1.2.10")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

            class AircraftHandling(Architecture):
                wbs_no: Optional[str] = Field("1.2.10.1")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class LoadHandling(Architecture):
                wbs_no: Optional[str] = Field("1.2.10.2")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

        class BallastGroup(Architecture):
            wbs_no: Optional[str] = Field("1.2.11")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class ManufacturingVariation(Architecture):
            wbs_no: Optional[str] = Field("1.2.12")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class Contingency(Architecture):
            wbs_no: Optional[str] = Field("1.2.13")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class OperatingItems(Architecture):
            wbs_no: Optional[str] = Field("1.2.14")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Crew(Architecture):
                wbs_no: Optional[str] = Field("1.2.14.1")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class UnusableFuel(Architecture):
                wbs_no: Optional[str] = Field("1.2.14.2")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class TrappedOil(Architecture):
                wbs_no: Optional[str] = Field("1.2.14.3")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class EngineOil(Architecture):
                wbs_no: Optional[str] = Field("1.2.14.4")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class AuxFuelTanks(Architecture):
                wbs_no: Optional[str] = Field("1.2.14.5")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class InternalFuelTanks(Architecture):
                wbs_no: Optional[str] = Field("1.2.14.6")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class ExternalFuelTanks(Architecture):
                wbs_no: Optional[str] = Field("1.2.14.7")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class WaterInjectionFluid(Architecture):
                wbs_no: Optional[str] = Field("1.2.14.8")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Baggage(Architecture):
                wbs_no: Optional[str] = Field("1.2.14.9")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class GunInstallations(Architecture):
                wbs_no: Optional[str] = Field("1.2.14.10")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

                class Guns(Architecture):
                    wbs_no: Optional[str] = Field("1.2.14.10.1")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

                class Supports(Architecture):
                    wbs_no: Optional[str] = Field("1.2.14.10.2")

                    model_config = ConfigDict(validate_assignment=True, extra="allow")

            class WeaponsProvisions(Architecture):
                wbs_no: Optional[str] = Field("1.2.14.11")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Chaff(Architecture):
                wbs_no: Optional[str] = Field("1.2.14.12")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Flares(Architecture):
                wbs_no: Optional[str] = Field("1.2.14.13")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class SurvivalKits(Architecture):
                wbs_no: Optional[str] = Field("1.2.14.14")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class LifeRafts(Architecture):
                wbs_no: Optional[str] = Field("1.2.14.15")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Oxygen(Architecture):
                wbs_no: Optional[str] = Field("1.2.14.16")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

        class Passengers(Architecture):
            wbs_no: Optional[str] = Field("1.2.15")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class Troops(Architecture):
            wbs_no: Optional[str] = Field("1.2.16")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class Cargo(Architecture):
            wbs_no: Optional[str] = Field("1.2.17")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class Ammunition(Architecture):
            wbs_no: Optional[str] = Field("1.2.18")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class Weapons(Architecture):
            wbs_no: Optional[str] = Field("1.2.19")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class InternalUsableFuel(Architecture):
            wbs_no: Optional[str] = Field("1.2.20")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class ExternalUsableFuel(Architecture):
            wbs_no: Optional[str] = Field("1.2.21")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class OtherAirVehicle(Architecture):
            wbs_no: Optional[str] = Field("1.2.22")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

    class PayloadMissionSystem(Architecture):
        wbs_no: Optional[str] = Field("1.3")

        model_config = ConfigDict(validate_assignment=True, extra="allow")

        class PayloadIntegrationAssemblyTestAndCheckout(Architecture):
            wbs_no: Optional[str] = Field("1.3.1")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class SurvivabilityPayload(Architecture):
            wbs_no: Optional[str] = Field("1.3.2")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class ReconnaissancePayload(Architecture):
            wbs_no: Optional[str] = Field("1.3.3")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class ElectronicWarfarePayload(Architecture):
            wbs_no: Optional[str] = Field("1.3.4")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class ArmamentWeaponsDeliveryPayload(Architecture):
            wbs_no: Optional[str] = Field("1.3.5")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class PayloadSoftwareRelease(Architecture):
            wbs_no: Optional[str] = Field("1.3.6")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class OtherPayload(Architecture):
            wbs_no: Optional[str] = Field("1.3.7")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

    class GroundHostSegment(Architecture):
        wbs_no: Optional[str] = Field("1.4")

        model_config = ConfigDict(validate_assignment=True, extra="allow")

        class GroundSegmentIntegrationAssemblyTestAndCheckout(Architecture):
            wbs_no: Optional[str] = Field("1.4.1")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class GroundControlSystems(Architecture):
            wbs_no: Optional[str] = Field("1.4.2")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class CommandAndControlSubsystem(Architecture):
            wbs_no: Optional[str] = Field("1.4.3")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class LaunchEquipment(Architecture):
            wbs_no: Optional[str] = Field("1.4.4")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class RecoveryEquipment(Architecture):
            wbs_no: Optional[str] = Field("1.4.5")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class TransportVehicles(Architecture):
            wbs_no: Optional[str] = Field("1.4.6")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class GroundSegmentSoftwareRelease(Architecture):
            wbs_no: Optional[str] = Field("1.4.7")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class OtherGroundHostSegment(Architecture):
            wbs_no: Optional[str] = Field("1.4.8")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

    class AircraftSystemSoftwareRelease(Architecture):
        wbs_no: Optional[str] = Field("1.5")

        model_config = ConfigDict(validate_assignment=True, extra="allow")

    class SystemsEngineering(Architecture):
        wbs_no: Optional[str] = Field("1.6")

        model_config = ConfigDict(validate_assignment=True, extra="allow")

        class SoftwareSystemsEngineering(Architecture):
            wbs_no: Optional[str] = Field("1.6.1")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class IntegratedLogisticsSupportSystemsEngineering(Architecture):
            wbs_no: Optional[str] = Field("1.6.2")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class CybersecuritySystemsEngineering(Architecture):
            wbs_no: Optional[str] = Field("1.6.3")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class CoreSystemsEngineering(Architecture):
            wbs_no: Optional[str] = Field("1.6.4")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class OtherSystemsEngineering(Architecture):
            wbs_no: Optional[str] = Field("1.6.5")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

    class ProgramManagement(Architecture):
        wbs_no: Optional[str] = Field("1.7")

        model_config = ConfigDict(validate_assignment=True, extra="allow")

        class SoftwareProgramManagement(Architecture):
            wbs_no: Optional[str] = Field("1.7.1")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class IntegratedLogisticsSupportProgramManagement(Architecture):
            wbs_no: Optional[str] = Field("1.7.2")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class CybersecurityManagement(Architecture):
            wbs_no: Optional[str] = Field("1.7.3")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class CoreProgramManagement(Architecture):
            wbs_no: Optional[str] = Field("1.7.4")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class OtherProgramManagement(Architecture):
            wbs_no: Optional[str] = Field("1.7.5")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

    class SystemTestAndEvaluation(Architecture):
        wbs_no: Optional[str] = Field("1.8")

        model_config = ConfigDict(validate_assignment=True, extra="allow")

        class DevelopmentalTestAndEvaluation(Architecture):
            wbs_no: Optional[str] = Field("1.8.1")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

            class SystemAcceptanceTest(Architecture):
                wbs_no: Optional[str] = Field("1.8.1.1")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class WindTunnelTests(Architecture):
                wbs_no: Optional[str] = Field("1.8.1.2")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class StructuralTests(Architecture):
                wbs_no: Optional[str] = Field("1.8.1.3")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class FlightTests(Architecture):
                wbs_no: Optional[str] = Field("1.8.1.4")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class GroundTests(Architecture):
                wbs_no: Optional[str] = Field("1.8.1.5")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class CybersecurityTestAndEvaluation(Architecture):
                wbs_no: Optional[str] = Field("1.8.1.6")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class OtherDTEtests(Architecture):
                wbs_no: Optional[str] = Field("1.8.1.7")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

        class OperationalTestAndEvaluation(Architecture):
            wbs_no: Optional[str] = Field("1.8.2")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

            class LimitedUserEvaluation(Architecture):
                wbs_no: Optional[str] = Field("1.8.2.1")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class InteroperabilityTesting(Architecture):
                wbs_no: Optional[str] = Field("1.8.2.2")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class FlightTests(Architecture):
                wbs_no: Optional[str] = Field("1.8.2.3")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class GroundTests(Architecture):
                wbs_no: Optional[str] = Field("1.8.2.4")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class CybersecurityTestAndEvaluation(Architecture):
                wbs_no: Optional[str] = Field("1.8.2.5")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class OtherOTEtests(Architecture):
                wbs_no: Optional[str] = Field("1.8.2.6")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

        class LiveFireTestAndEvaluation(Architecture):
            wbs_no: Optional[str] = Field("1.8.3")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class MockupsSystemIntegrationLabs(Architecture):
            wbs_no: Optional[str] = Field("1.8.4")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class TestAndEvaluationSupport(Architecture):
            wbs_no: Optional[str] = Field("1.8.5")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class TestFacilities(Architecture):
            wbs_no: Optional[str] = Field("1.8.6")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

    class Training(Architecture):
        wbs_no: Optional[str] = Field("1.9")

        model_config = ConfigDict(validate_assignment=True, extra="allow")

        class Equipment(Architecture):
            wbs_no: Optional[str] = Field("1.9.1")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

            class OperatorInstructionalEquipment(Architecture):
                wbs_no: Optional[str] = Field("1.9.1.1")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class MaintainerInstructionalEquipment(Architecture):
                wbs_no: Optional[str] = Field("1.9.1.2")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

        class Services(Architecture):
            wbs_no: Optional[str] = Field("1.9.2")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

            class OperatorInstructionalServices(Architecture):
                wbs_no: Optional[str] = Field("1.9.2.1")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class MaintainerInstructionalServices(Architecture):
                wbs_no: Optional[str] = Field("1.9.2.2")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

        class Facilities(Architecture):
            wbs_no: Optional[str] = Field("1.9.3")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class TrainingSoftware(Architecture):
            wbs_no: Optional[str] = Field("1.9.4")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

    class Data(Architecture):
        wbs_no: Optional[str] = Field("1.10")

        model_config = ConfigDict(validate_assignment=True, extra="allow")

        class DataDeliverables(Architecture):
            wbs_no: Optional[str] = Field("1.10.1")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class DataRepository(Architecture):
            wbs_no: Optional[str] = Field("1.10.2")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class DataRights(Architecture):
            wbs_no: Optional[str] = Field("1.10.3")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

    class PeculiarSupportEquipment(Architecture):
        wbs_no: Optional[str] = Field("1.11")

        model_config = ConfigDict(validate_assignment=True, extra="allow")

        class TestAndMeasurementEquipment(Architecture):
            wbs_no: Optional[str] = Field("1.11.1")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

            class AirframeHullVehicle(Architecture):
                wbs_no: Optional[str] = Field("1.11.1.1")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Propulsion(Architecture):
                wbs_no: Optional[str] = Field("1.11.1.2")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class ElectronicsAvionics(Architecture):
                wbs_no: Optional[str] = Field("1.11.1.3")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class OtherMajorSubsystems(Architecture):
                wbs_no: Optional[str] = Field("1.11.1.4")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

        class SupportAndHandlingEquipment(Architecture):
            wbs_no: Optional[str] = Field("1.11.2")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

            class AirframeHullVehicle(Architecture):
                wbs_no: Optional[str] = Field("1.11.2.1")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Propulsion(Architecture):
                wbs_no: Optional[str] = Field("1.11.2.2")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class ElectronicsAvionics(Architecture):
                wbs_no: Optional[str] = Field("1.11.2.3")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class OtherMajorSubsystems(Architecture):
                wbs_no: Optional[str] = Field("1.11.2.4")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

    class CommonSupportEquipment(Architecture):
        wbs_no: Optional[str] = Field("1.12")

        model_config = ConfigDict(validate_assignment=True, extra="allow")

        class TestAndMeasurementEquipment(Architecture):
            wbs_no: Optional[str] = Field("1.12.1")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

            class AirframeHullVehicle(Architecture):
                wbs_no: Optional[str] = Field("1.12.1.1")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Propulsion(Architecture):
                wbs_no: Optional[str] = Field("1.12.1.2")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class ElectronicsAvionics(Architecture):
                wbs_no: Optional[str] = Field("1.12.1.3")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class OtherMajorSubsystems(Architecture):
                wbs_no: Optional[str] = Field("1.12.1.4")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

        class SupportAndHandlingEquipment(Architecture):
            wbs_no: Optional[str] = Field("1.12.2")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

            class AirframeHullVehicle(Architecture):
                wbs_no: Optional[str] = Field("1.12.2.1")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class Propulsion(Architecture):
                wbs_no: Optional[str] = Field("1.12.2.2")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class ElectronicsAvionics(Architecture):
                wbs_no: Optional[str] = Field("1.12.2.3")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

            class OtherMajorSubsystems(Architecture):
                wbs_no: Optional[str] = Field("1.12.2.4")

                model_config = ConfigDict(validate_assignment=True, extra="allow")

    class OperationalSiteActivation(Architecture):
        wbs_no: Optional[str] = Field("1.13")

        model_config = ConfigDict(validate_assignment=True, extra="allow")

        class SystemAssemblyInstallationAndCheckoutOnSite(Architecture):
            wbs_no: Optional[str] = Field("1.13.1")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class ContractorTechnicalSupport(Architecture):
            wbs_no: Optional[str] = Field("1.13.2")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class SiteConstruction(Architecture):
            wbs_no: Optional[str] = Field("1.13.3")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class SiteShipVehicleConversion(Architecture):
            wbs_no: Optional[str] = Field("1.13.4")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class InterimContractorSupport(Architecture):
            wbs_no: Optional[str] = Field("1.13.5")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

    class ContractorLogisticsSupport(Architecture):
        wbs_no: Optional[str] = Field("1.14")

        model_config = ConfigDict(validate_assignment=True, extra="allow")

    class IndustrialFacilities(Architecture):
        wbs_no: Optional[str] = Field("1.15")

        model_config = ConfigDict(validate_assignment=True, extra="allow")

        class ConstructionConversionExpansion(Architecture):
            wbs_no: Optional[str] = Field("1.15.1")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class EquipmentAcquisitionOrModernization(Architecture):
            wbs_no: Optional[str] = Field("1.15.2")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

        class IndustrialFacilitiesMaintenance(Architecture):
            wbs_no: Optional[str] = Field("1.15.3")

            model_config = ConfigDict(validate_assignment=True, extra="allow")

    class InitialSparesAndRepairParts(Architecture):
        wbs_no: Optional[str] = Field("1.16")

        model_config = ConfigDict(validate_assignment=True, extra="allow")
