import pytest
from pydantic import ValidationError

from adh.wbs.airframe.airframe_geometry import (
    Airfoil,
    Body,
    Boolean,
    CrossSection,
    Float,
    Integer,
    LiftingSurface,
    Loft,
    Mesh,
    Metadata,
    Point,
    Polyline,
    Spline,
    String,
)


class TestPydanticModels:
    def test_cross_section(self):
        # Test valid data
        points = [
            Point(x=0.0, y=0.0, z=0.0),
            Point(x=0.1, y=0.1, z=0.1),
            Point(x=0.5, y=0.5, z=0.5),
            Point(x=0.8, y=0.8, z=0.8),
            Point(x=1.0, y=1.0, z=1.0),
        ]
        upper_curve = Spline(points=points)
        lower_curve = Spline(points=points)
        data = {"station": 0.5, "upper_curve": upper_curve, "lower_curve": lower_curve}
        model = CrossSection(**data)
        assert model.station == 0.5
        assert model.upper_curve == upper_curve
        assert model.lower_curve == lower_curve

        # Test missing both curves
        data = {"station": 0.5}
        with pytest.raises(ValidationError):
            CrossSection(**data)  # pyright: ignore[reportArgumentType]

    def test_body_geometry(self):
        # Test valid data
        points = [
            Point(x=0.0, y=0.0, z=0.0),
            Point(x=0.1, y=0.1, z=0.1),
            Point(x=0.5, y=0.5, z=0.5),
            Point(x=0.8, y=0.8, z=0.8),
            Point(x=1.0, y=1.0, z=1.0),
        ]
        reference_axis = Spline(points=points)
        cross_section = CrossSection(station=0.5, upper_curve=Spline(points=points))
        data = {"reference_axis": reference_axis, "cross_sections": [cross_section]}
        model = Body(**data)
        assert model.reference_axis == reference_axis
        assert model.cross_sections == [cross_section]

        # Test missing cross_sections
        data["cross_sections"] = []
        with pytest.raises(ValidationError):
            Body(**data)

    def test_lifting_surface_geometry(self):
        # Test valid data
        points = [
            Point(x=0.0, y=0.0, z=0.0),
            Point(x=0.1, y=0.1, z=0.1),
            Point(x=0.5, y=0.5, z=0.5),
            Point(x=0.8, y=0.8, z=0.8),
            Point(x=1.0, y=1.0, z=1.0),
        ]
        leading_edge_spline = Spline(points=points)
        trailing_edge_spline = Spline(points=points)
        airfoil_section = Airfoil(spline=Spline(points=points))
        data = {
            "leading_edge_spline": leading_edge_spline,
            "trailing_edge_spline": trailing_edge_spline,
            "airfoil_sections": [airfoil_section],
        }
        model = LiftingSurface(**data)
        assert model.leading_edge_spline == leading_edge_spline
        assert model.trailing_edge_spline == trailing_edge_spline
        assert model.airfoil_sections == [airfoil_section]

        # Test missing airfoil_sections
        data["airfoil_sections"] = []
        with pytest.raises(ValidationError):
            LiftingSurface(**data)


class TestPoint:
    def test_point_creation(self):
        point = Point(x=1.0, y=2.0, z=3.0)
        assert point.x == 1.0
        assert point.y == 2.0
        assert point.z == 3.0

    def test_point_distance(self):
        point1 = Point(x=0.0, y=0.0, z=0.0)
        point2 = Point(x=1.0, y=1.0, z=1.0)
        assert point1.distance_to(point2) == pytest.approx(1.732, abs=1e-3)


class TestPolyline:
    def test_polyline_creation(self):
        points = [Point(x=0.0, y=0.0, z=0.0), Point(x=1.0, y=1.0, z=1.0)]
        polyline = Polyline(points=points)
        assert len(polyline.points) == 2

    def test_polyline_length(self):
        points = [Point(x=0.0, y=0.0, z=0.0), Point(x=1.0, y=1.0, z=1.0)]
        polyline = Polyline(points=points)
        assert polyline.length() == pytest.approx(1.732, abs=1e-3)

    def test_polyline_simplify(self):
        points = [
            Point(x=0.0, y=0.0, z=0.0),
            Point(x=0.5, y=0.5, z=0.5),
            Point(x=1.0, y=1.0, z=1.0),
        ]
        polyline = Polyline(points=points)
        simplified_polyline = polyline.simplify(tolerance=0.1)
        assert len(simplified_polyline.points) == 2


class TestMesh:
    def test_mesh_creation(self):
        points = [Point(x=0.0, y=0.0, z=0.0), Point(x=1.0, y=1.0, z=1.0)]
        polyline = Polyline(points=points)
        mesh = Mesh(polylines=[polyline])
        assert len(mesh.polylines) == 1

    # TODO: Fix Issue with unexpected is_manifold() results
    # def test_mesh_is_manifold(self):
    #     points = [
    #         Point(x=0.0, y=0.0, z=0.0),
    #         Point(x=1.0, y=0.0, z=0.0),
    #         Point(x=1.0, y=1.0, z=0.0),
    #         Point(x=0.0, y=1.0, z=0.0)
    #     ]
    #     polyline = Polyline(points=points)
    #     mesh = Mesh(polylines=[polyline])
    #     self.assertTrue(mesh.is_manifold())

    def test_mesh_calculate_volume(self):
        points = [
            Point(x=0.0, y=0.0, z=0.0),
            Point(x=1.0, y=0.0, z=0.0),
            Point(x=1.0, y=1.0, z=0.0),
            Point(x=0.0, y=1.0, z=0.0),
        ]
        polyline = Polyline(points=points)
        mesh = Mesh(polylines=[polyline])
        assert mesh.calculate_volume() == pytest.approx(0.0, abs=1e-3)


class TestSpline:
    def test_spline_creation(self):
        points = [
            Point(x=0.0, y=0.0, z=0.0),
            Point(x=1.0, y=1.0, z=1.0),
            Point(x=2.0, y=2.0, z=2.0),
            Point(x=3.0, y=3.0, z=3.0),
        ]
        spline = Spline(points=points, degree=3)
        assert len(spline.points) == 4
        assert spline.degree == 3

    def test_spline_validation(self):
        points = [Point(x=0.0, y=0.0, z=0.0)]
        with pytest.raises(ValidationError):
            Spline(points=points, degree=3)


class TestLoft:
    def test_loft_creation(self):
        points1 = [
            Point(x=0.0, y=0.0, z=0.0),
            Point(x=1.0, y=1.0, z=1.0),
            Point(x=2.0, y=2.0, z=2.0),
            Point(x=3.0, y=3.0, z=3.0),
        ]
        points2 = [
            Point(x=0.0, y=0.0, z=1.0),
            Point(x=1.0, y=1.0, z=2.0),
            Point(x=2.0, y=2.0, z=3.0),
            Point(x=3.0, y=3.0, z=4.0),
        ]
        spline1 = Spline(points=points1, degree=4)
        spline2 = Spline(points=points2, degree=4)
        loft = Loft(splines=[spline1, spline2], num_samples=10)
        assert len(loft.splines) == 2
        assert loft.num_samples == 10

    def test_loft_calculate_surface(self):
        points1 = [
            Point(x=0.0, y=0.0, z=0.0),
            Point(x=1.0, y=1.0, z=1.0),
            Point(x=2.0, y=2.0, z=2.0),
            Point(x=3.0, y=3.0, z=3.0),
        ]
        points2 = [
            Point(x=0.0, y=0.0, z=1.0),
            Point(x=1.0, y=1.0, z=2.0),
            Point(x=2.0, y=2.0, z=3.0),
            Point(x=3.0, y=3.0, z=4.0),
        ]
        spline1 = Spline(points=points1, degree=4)
        spline2 = Spline(points=points2, degree=4)
        loft = Loft(splines=[spline1, spline2], num_samples=10)
        surface = loft.calculate_surface()
        assert len(surface) == 40  # 2 splines * 10 samples


class TestString:
    def test_string_creation(self):
        metadata = Metadata(key="example_key", value="example_value")
        string = String(value="test", default="default", metadata=metadata)
        assert string.value == "test"
        assert string.default == "default"

    def test_string_validation(self):
        with pytest.raises(ValidationError):
            String(value="")


class TestBoolean:
    def test_boolean_creation(self):
        metadata = Metadata(key="example_key", value="example_value")
        boolean = Boolean(value=True, default=False, metadata=metadata)
        assert boolean.value is True
        assert boolean.default is False

    def test_boolean_validation(self):
        with pytest.raises(ValidationError):
            Boolean(value="not a boolean")  # pyright: ignore[reportArgumentType]


class TestFloat:
    def test_float_creation(self):
        metadata = Metadata(key="example_key", value="example_value")
        float_var = Float(value=1.23, default=0.0, metadata=metadata)
        assert float_var.value == pytest.approx(1.23)
        assert float_var.default == pytest.approx(0.0)

    def test_float_validation(self):
        with pytest.raises(ValidationError):
            Float(value="not a float")  # pyright: ignore[reportArgumentType]


class TestInteger:
    def test_integer_creation(self):
        metadata = Metadata(key="example_key", value="example_value")
        integer = Integer(value=123, default=0, metadata=metadata)
        assert integer.value == 123
        assert integer.default == 0

    def test_integer_validation(self):
        with pytest.raises(ValidationError):
            Integer(value="not an integer")  # pyright: ignore[reportArgumentType]
