"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError
from ..enums import eLoadDistributedDir, eLoadDistributedType


class N_FrameObj:
    """Wrapper para SapModel.FrameObj."""

    def __init__(self, raw):
        self._raw = raw

    def AddByCoord(self, xi: float, yi: float, zi: float, xj: float, yj: float, zj: float, PropName: str = 'Default', UserName: str = '', CSys: str = 'Global'):
        """This function adds a new frame object whose end points are at the specified coordinates. The
        function returns zero if the frame object is successfully added, otherwise it
        returns a nonzero value.
    
        Name (output): This is the name that the program ultimately assigns for the frame
            object. If no UserName is specified, the program assigns a default name to the
            frame object. If a UserName is specified and that name is not used for another
            frame, cable or tendon object, the UserName is assigned to the frame object,
            otherwise a default name is assigned to the frame object.
        PropName (input): This is Default, None, or the name of a defined frame section
            property. If it is Default, the program assigns a default section property to
            the frame object. If it is None, no section property is assigned to the frame
            object. If it is the name of a defined frame section property, that property is
            assigned to the frame object.
        UserName (input): This is an optional user specified name for the frame object. If a
            UserName is specified and that name is already used for another frame object,
            the program ignores the UserName.
        CSys (input): The name of the coordinate system in which the frame object end point
            coordinates are defined.
        """
        _r = self._raw.AddByCoord(xi, yi, zi, xj, yj, zj, "", PropName, UserName, CSys)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.AddByCoord falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def AddByPoint(self, Point1: str, Point2: str, PropName: str = 'Default', UserName: str = ''):
        """This function adds a new frame object whose end points are specified by name. The function
        returns zero if the frame object is successfully added, otherwise it returns a
        nonzero value.
    
        Point1 (input): The name of a defined point object at the I-End of the added frame
            object.
        Point2 (input): The name of a defined point object at the J-End of the added frame
            object.
        Name (output): This is the name that the program ultimately assigns for the frame
            object. If no UserName is specified, the program assigns a default name to the
            frame object. If a UserName is specified and that name is not used for another
            frame, cable or tendon object, the UserName is assigned to the frame object,
            otherwise a default name is assigned to the frame object.
        PropName (input): This is Default, None, or the name of a defined frame section
            property. If it is Default, the program assigns a default section property to
            the frame object. If it is None, no section property is assigned to the frame
            object. If it is the name of a defined frame section property, that property is
            assigned to the frame object.
        UserName (input): This is an optional user specified name for the frame object. If a
            UserName is specified and that name is already used for another frame object,
            the program ignores the UserName.
        """
        _r = self._raw.AddByPoint(Point1, Point2, "", PropName, UserName)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.AddByPoint falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def ChangeName(self, Name: str, NewName: str):
        """The function returns zero if the new name is successfully applied, otherwise it returns a
        nonzero value.
    
        Name (input): The existing name of a defined frame object.
        NewName (input): The new name for the frame object.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self, MyType: str = 'All'):
        """This function returns a count of the frame objects in the model. Depending on the value of
        the MyType item, the count may be of all frame objects in the model, just the
        straight frame objects in the model or just the curved frame objects in the model.
    
        MyType (input): This is All, Straight, or Curved. All returns a count of all frame
            objects in the model, including both straight and curved frame objects. Straight
            returns a count of all straight frame objects in the model. Curved returns a
            count of all curved frame objects in the model.
        """
        _r = self._raw.Count(MyType)
        return _r

    def DeleteFireproofing(self, Name: str, ItemType: int = 0):
        """This function deletes the fireproofing assignments for frame objects. The function returns
        zero if the fireproofing assignments are successfully deleted, otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the
            fireproofing assignments are deleted for the frame object specified by the Name
            item. If this item is Group, the fireproofing assignments are deleted for all
            frame objects in the group specified by the Name item. If this item is
            SelectedObjects, the fireproofing assignments are deleted for all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.DeleteFireproofing(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.DeleteFireproofing falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLateralBracing(self, Name: str, MyType: int = 3, ItemType: int = 0):
        """This function deletes the lateral bracing assignments for frame objects. The function
        returns zero if the assignments are successfully deleted; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        MyType (input): This is 1, 2 or 3, indicating the bracing to be deleted. 1 = Delete
            point bracing 2 = Delete uniform bracing 3 = Delete both point and uniform
            bracing
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the lateral
            bracing assignments are deleted for the frame object specified by the Name item.
            If this item is Group, the lateral bracing assignments are deleted for all frame
            objects in the group specified by the Name item. If this item is SelectedObjects
            then the lateral bracing assignments are deleted for all selected frame objects,
            and the Name item is ignored.
        """
        _r = self._raw.DeleteLateralBracing(Name, MyType, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.DeleteLateralBracing falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadDeformation(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the deformation load assignments to the specified frame objects for
        the specified load pattern. The function returns zero if the load assignments are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the frame object specified by the Name item. If this
            item is Group, the load assignments are deleted for all frame objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected frame objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadDeformation(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.DeleteLoadDeformation falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadDistributedWithGUID(self, Name: str, GUID: str):
        """This function deletes the distributed load assignment with the specified global unique ID
        for the frame objects for the specified frame object. The function returns zero if
        the load assignments are successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        GUID (input): The global unique ID of one of the distributed loads on that frame
            object.
        """
        _r = self._raw.DeleteLoadDistributedWithGUID(Name, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.DeleteLoadDistributedWithGUID falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadDistributed(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the distributed load assignments to the specified frame objects for
        the specified load pattern. The function returns zero if the load assignments are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the frame object specified by the Name item. If this
            item is Group, the load assignments are deleted for all frame objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected frame objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadDistributed(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.DeleteLoadDistributed falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadGravity(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the gravity load assignments to the specified frame objects for the
        specified load pattern. The function returns zero if the load assignments are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object,the load
            assignments are deleted for the frame object specified by the Name item. If this
            item is Group, the load assignments are deleted for all frame objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected frame objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadGravity(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.DeleteLoadGravity falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadPoint(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the point load assignments to the specified frame objects for the
        specified load pattern. The function returns zero if the load assignments are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the frame object specified by the Name item. If this
            item is Group, the load assignments are deleted for all frame objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected frame objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadPoint(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.DeleteLoadPoint falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadPointWithGUID(self, Name: str, GUID: str):
        """This function deletes the point load assignment with the specified global unique ID for the
        specified frame object. The function returns zero if the load assignment is
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        GUID (input): The global unique ID for one of the point loads on that frame object.
        """
        _r = self._raw.DeleteLoadPointWithGUID(Name, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.DeleteLoadPointWithGUID falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadStrain(self, Name: str, LoadPat: str, DOF: int, ItemType: int = 0):
        """This function deletes the strain load assignments to the specified frame objects, for the
        specified load pattern, for the specified degree of freedom. The function returns
        zero if the load assignments are successfully deleted, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        DOF (input): This is 1, 2, 3, 4, 5 or 6, indicating the degree of freedom to which
            the strain load is applied. 1 = Strain11 2 = Strain12 3 = Strain13 4 =
            Curvature1 5 = Curvature2 6 = Curvature3
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the frame object specified by the Name item. If this
            item is Group, the load assignments are deleted for all frame objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected frame objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadStrain(Name, LoadPat, DOF, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.DeleteLoadStrain falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadTargetForce(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the target force assignments to the specified frame objects for the
        specified load pattern. The function returns zero if the target force assignments
        are successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the frame object specified by the Name item. If this
            item is Group, the load assignments are deleted for all frame objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected frame objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadTargetForce(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.DeleteLoadTargetForce falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteLoadTemperature(self, Name: str, LoadPat: str, ItemType: int = 0):
        """This function deletes the temperature load assignments to the specified frame objects for
        the specified load pattern. The function returns zero if the load assignments are
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the load
            assignments are deleted for the frame object specified by the Name item. If this
            item is Group, the load assignments are deleted for all frame objects in the
            group specified by the Name item. If this item is SelectedObjects, the load
            assignments are deleted for all selected frame objects, and the Name item is
            ignored.
        """
        _r = self._raw.DeleteLoadTemperature(Name, LoadPat, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.DeleteLoadTemperature falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteMass(self, Name: str, ItemType: int = 0):
        """This function deletes the frame mass assignments for frame objects. The function returns
        zero if the mass assignments are successfully deleted, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the frame mass
            assignments are deleted for the frame object specified by the Name item. If this
            item is Group, the frame mass assignments are deleted for all frame objects in
            the group specified by the Name item. If this item is SelectedObjects, the frame
            mass assignments are deleted for all selected frame objects and the Name item is
            ignored.
        """
        _r = self._raw.DeleteMass(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.DeleteMass falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteModifiers(self, Name: str, ItemType: int = 0):
        """This function deletes the frame modifier assignments for frame objects. The function returns
        zero if the modifier assignments are successfully deleted, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the frame
            modifier assignments are deleted for the frame object specified by the Name
            item. If this item is Group, the frame modifier assignments are deleted for all
            frame objects in the group specified by the Name item. If this item is
            SelectedObjects, the frame modifier assignments are deleted for all selected
            frame objects, and the Name item is ignored.
        """
        _r = self._raw.DeleteModifiers(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.DeleteModifiers falhou (ret={_r})".format(_r=_r))
        return None

    def DeletePDeltaForce(self, Name: str, ItemType: int = 0):
        """This function deletes the P-Delta force assignments for frame objects. The function returns
        zero if the assignments are successfully deleted, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the frame
            modifier assignments are deleted for the frame object specified by the Name
            item. If this item is Group, the frame modifier assignments are deleted for all
            frame objects in the group specified by the Name item. If this item is
            SelectedObjects, the frame modifier assignments are deleted for all selected
            frame objects, and the Name item is ignored.
        """
        _r = self._raw.DeletePDeltaForce(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.DeletePDeltaForce falhou (ret={_r})".format(_r=_r))
        return None

    def DeleteSpring(self, Name: str, ItemType: int = 0):
        """This function deletes all spring assignments for the specified frame objects. The function
        returns zero if the assignments are successfully deleted, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the frame
            spring assignments are deleted for the frame object specified by the Name item.
            If this item is Group, the frame spring assignments are deleted for all frame
            objects in the group specified by the Name item. If this item is
            SelectedObjects, the frame spring assignments are deleted for all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.DeleteSpring(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.DeleteSpring falhou (ret={_r})".format(_r=_r))
        return None

    def Delete(self, Name: str, ItemType: int = 0):
        """The function deletes frame objects. The function returns zero if the frame object is
        successfully deleted, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the frame
            object specified by the Name item is deleted. If this item is Group, all of the
            frame objects in the group specified by the Name item are deleted. If this item
            is SelectedObjects, all selected frame objects are deleted, and the Name item is
            ignored.
        """
        _r = self._raw.Delete(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetAutoMesh(self, Name: str, AutoMesh: bool, AutoMeshAtPoints: bool, AutoMeshAtLines: bool, NumSegs: int, AutoMeshMaxLength: float):
        """This function retrieves the automatic meshing assignments to frame objects. The function
        returns zero if the meshing assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        AutoMesh (input): This item is True if the frame object is to be automatically
            meshed by the program when the analysis model is created.
        AutoMeshAtPoints (input): This item is applicable only when the AutoMesh item is
            True. If this item is True, the frame object is automatically meshed at
            intermediate joints along its length.
        AutoMeshAtLines (input): This item is applicable only when the AutoMesh item is
            True. If this item is True, the frame object is automatically meshed at
            intersections with other frames, area object edges and solid object edges.
        NumSegs (input): This item is applicable only when the AutoMesh item is True. It is
            the minimum number of elements into which the frame object is automatically
            meshed. If this item is zero, the number of elements is not checked when the
            automatic meshing is done.
        AutoMeshMaxLength (input): This item is applicable only when the AutoMesh item is
            True. It is the maximum length of auto meshed frame elements. If this item is
            zero, the element length is not checked when the automatic meshing is done. [L]
        """
        _r = self._raw.GetAutoMesh(Name, AutoMesh, AutoMeshAtPoints, AutoMeshAtLines, NumSegs, AutoMeshMaxLength)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetAutoMesh falhou (ret={_r})".format(_r=_r))
        return None

    def GetCurved_1(self):
        """This function retrieves definition data for all curved frame objects and returns the data in
        arrays. The function returns zero if the curved frame object data is successfully
        retrieved, otherwise it returns a nonzero value.
    
        NumberItems (output): The number of curved frame objects returned.
        MyName (output): This is a one-dimensional array of frame object names. The MyName
            array is created as a dynamic, zero-based, array by the APIuser: Dim MyName() as
            String The array is dimensioned to (NumberNames 1) inside the Sap2000 program,
            filled with the names, and returned to the APIuser
        MyType (output): This is an array that includes a numeric value indicating the
            curved frame type. The type is 1, 2, 3, 4, or 5. 1 = Circular Arc Specified by a
            Third Point Name 2 = Circular Arc Specified by Third Point Coordinates 3 =
            Circular Arc Specified by Planar Point Coordinates and Radius 4 = Parabolic Arc
            Specified by a Third Point Name 5 = Parabolic Arc Specified by Third Point
            Coordinates MyTypes 1, 2, 4, and 5 all define the curve by three points. The
            three points are the two end point of the frame object and a third point defined
            by naming an existing point object or specifying point coordinates. MyType 3
            defines a circular curved frame by it end points, the coordinates of another
            point that lies in the plane of the curve but not necessarily on the curved
            frame, and a curve radius.
        PointName (output): This is an array that includes the name of the point object that
            is the third point on the curved frame. This item applies for MyType 1 and 4. It
            does not apply for MyType 2, 3 and 5.
        Radius (output): This is an array of the radii of the circular curved frame. This
            item only applies for MyType 3. [L]
        NumSegs (output): This is an array that includes the number of segments into which
            the program internally divides the curved frame.
        """
        _r = self._raw.GetCurved_1(None, "", [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetCurved_1 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDesignProcedure(self, Name: str):
        """This function retrieves the design procedure for a frame object. The function returns zero
        if the design procedure is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing frame object.
        MyType (output): This is 1, 2, 7, 8 or 9, indicating the design procedure for the
            specified frame object. 1 = Steel 2 = Concrete 7 = Aluminum 8 = Cold Formed 9 =
            No Design
        """
        _r = self._raw.GetDesignProcedure(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetDesignProcedure falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetElm(self, Name: str):
        """This function retrieves the names of the frame elements (analysis model lines) associated
        with a specified frame object in the object-based model. It also retrieves
        information about the location of the frame elements along the frame object. This
        function returns zero if the frame element information is successfully returned;
        otherwise it returns nonzero. An error occurs if the analysis model does not exist.
    
        Name (input): The name of an existing frame object.
        nelm (output): The number of line elements created from the specified frame object.
        Elm (output): An array that includes the name of a frame element created from the
            specified frame object.
        RDI (output): An array that includes the relative distance along the frame object to
            the I-End of the frame element.
        RDJ (output): An array that includes the relative distance along the line object to
            the J-End of the frame element.
        """
        _r = self._raw.GetElm(Name, 0, [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetElm falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetEndLengthOffset(self, Name: str, AutoOffset: bool):
        """This function retrieves the frame object end offsets along the 1-axis of the object. The
        function returns zero if the offsets are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        AutoOffset (input): If this item is True, the end length offsets are automatically
            determined by the program from object connectivity.
        Length1 (output): The offset length along the 1-axis of the frame object at the
            I-End of the frame object. [L]
        Length2 (output): The offset along the 1-axis of the frame object at the J-End of
            the frame object. [L]
        rz (output): The rigid zone factor. This is the fraction of the end offset length
            assumed to be rigid for bending and shear deformations.
        """
        _r = self._raw.GetEndLengthOffset(Name, AutoOffset, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetEndLengthOffset falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetEndSkew(self, Name: str):
        """This function retrieves frame object end skew assignments. The function returns zero if the
        end skew data is successfully retrieved, otherwise it returns a nonzero value. End
        skew assignments are only applicable to straight frame objects. An error is returned
        if skew data is requested for a curved frame object. End skew data is only used in
        the program to plot the extruded view of bridge objects that have been updated as
        spine models.
    
        Name (input): The name of an existing frame object.
        SkewI (output): The angle in degrees measured counter clockwise from the positive
            local 3-axis to a line parallel to the I-End of the frame object (-90 < SkewI <
            90). [deg]
        SkewJ (output): The angle in degrees measured counter clockwise from the positive
            local 3-axis to a line parallel to the J-End of the frame object (-90 < SkewJ <
            90). [deg]
        """
        _r = self._raw.GetEndSkew(Name, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetEndSkew falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetFireProofing_1(self, Name: str, tf: bool, IncludeInSelfWeight: bool, IncludeInGravityLoads: bool, IncludeInThisLoadPattern: str):
        """This function gets the fireproofing assignment to an existing frame object. The function
        returns zero if the fireproofing assignment is successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        MyType (output): This is 1, 2 or 3, indicating the type of fireproofing assigned. 1
            = Sprayed on - program calculate section perimeter 2 = Sprayed on - user
            provides section perimeter 3 = Concrete encased
        Thickness (output): When MyType = 1 or MyType = 2 this is the thickness of the
            sprayed on fireproofing. When MyType = 3 this is the concrete cover dimension.
            [L]
        Perimeter (output): This item applies only when MyType = 2. It is the length of
            fireproofing applied measured around the perimeter of the frame object cross-
            section. [L]
        Density (output): This is the weight per unit volume of the fireproofing material.
            [F/L3]
        tf (input): This item applies only when MyType = 1 or MyType = 3. If this item is
            True, the fireproofing is assumed to be applied to the top flange of the
            section. If it is False, the program assumes no fireproofing is applied to the
            section top flange. This flag applies for I, channel and double channel
            sections.
        IncludeInSelfWeight (input): If this item is True the fireproofing is included in
            the structure self weight.
        IncludeInGravityLoads (input): If this item is True the fireproofing is included
            gravity loads applied in the X, Y and Z directions.
        IncludeInThisLoadPattern (input): This item is either None or the name of an
            existing load pattern. If it is the name of a load pattern then the weight of
            the fireproofing is applied as a distributed load in the global Z direction in
            the load pattern.
        """
        _r = self._raw.GetFireProofing_1(Name, 0, 0.0, 0.0, 0.0, tf, IncludeInSelfWeight, IncludeInGravityLoads, IncludeInThisLoadPattern)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetFireProofing_1 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetGUID(self, name: str):
        """This function retrieves the GUID for the specified frame object. This function returns zero
        if the frame object GUID is successfully retrieved; otherwise it returns nonzero.
    
        GUID (output): The GUID (Global Unique ID) for the specified frame object.
        """
        _r = self._raw.GetGUID(name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetGUID falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetGroupAssign(self, Name: str):
        """This function retrieves the names of the groups to which a specified frame object is
        assigned. The function returns zero if the group assignments are successfully
        retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        NumberGroups (output): The number of group names retrieved.
        Groups (output): The names of the groups to which the frame object is assigned.
        """
        _r = self._raw.GetGroupAssign(Name, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetGroupAssign falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetHingeAssigns(self, Name: str):
        """This function reports the hinge assignments for a specified frame object. The function
        returns zero if the assignment data is successfully obtained; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing frame object.
        NumberHinges (output): The number of hinge assignments on the specified frame
            object.
        HingeNum (output): An array that includes the hinge number for each hinge on the
            frame object.
        Prop (output): An array that includes the name of the generated hinge property for
            each hinge on the frame object.
        MyType (output): An array that specifies the type of hinge for each hinge on the
            frame object. It is one of the following: 1 = Axial P 2 = Shear V2 3 = Shear V3
            4 = Torsion T 5 = Moment M2 6 = Moment M3 7 = Interacting P-M2 8 = Interacting
            P-M3 9 = Interacting M2-M3 10 = Interacting P-M2-M3 11 = Fiber P-M2-M3
        Behavior (output): An array that specifies the behavior of the hinge for each hinge
            on the frame object. It is one of the following: 1 = Force controlled 2 =
            Deformation controlled
        Source (output): An array that indicates the source of the generated hinge property
            for each hinge on the frame object. The source is either Auto or the name of a
            defined (not generated) hinge property.
        RD (output): An array that indicates the relative distance of each hinge along the
            frame object.
        """
        _r = self._raw.GetHingeAssigns(Name, 0, [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetHingeAssigns falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetInsertionPoint(self, Name: str, Mirror2: bool, StiffTransform: bool):
        """This function retrieves frame object insertion point assignments. The assignments include
        the cardinal point and end joint offsets. The function returns zero if the insertion
        point data is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        CardinalPoint (output): This is a numeric value from 1 to 11 that specifies the
            cardinal point for the frame object. The cardinal point specifies the relative
            position of the frame section on the line representing the frame object. 1 =
            bottom left 2 = bottom center 3 = bottom right 4 = middle left 5 = middle center
            6 = middle right 7 = top left 8 = top center 9 = top right 10 = centroid 11 =
            shear center
        Mirror2 (input): If this item is True, the frame object section is assumed to be
            mirrored (flipped) about its local 2-axis.
        StiffTransform (input): If this item is True, the frame object stiffness is
            transformed for cardinal point and joint offsets from the frame section
            centroid.
        Offset1 (output): This is an array of three joint offset distances, in the
            coordinate directions specified by CSys, at the I-End of the frame object. [L]
            Offset1(0) = Offset in the 1-axis or X-axis direction Offset1(1) = Offset in the
            2-axis or Y-axis direction Offset1(2) = Offset in the 3-axis or Z-axis direction
        Offset2 (output): This is an array of three joint offset distances, in the
            coordinate directions specified by CSys, at the J-End of the frame object. [L]
            Offset2(0) = Offset in the 1-axis or X-axis direction Offset2(1) = Offset in the
            2-axis or Y-axis direction Offset2(2) = Offset in the 3-axis or Z-axis direction
        CSys (output): This is either Local or the name of a defined coordinate system. It
            is the coordinate system in which the Offset1 and Offset2 items are specified.
        """
        _r = self._raw.GetInsertionPoint(Name, 0, Mirror2, StiffTransform, [], [], "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetInsertionPoint falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLateralBracing(self, Name: str):
        """This function retrieves the lateral bracing location assignments for frame objects. The
        function returns zero if the assignments are successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        NumberItems (output): The total number of bracing assignments retrieved for the
            specified frame objects.
        FrameName (output): This is an array that includes the name of the frame object
            associated with each bracing assignment.
        MyType (output): This is an array that includes 1 or 2, indicating the bracing type
            assigned. 1 = Point bracing 2 = Uniform bracing
        Loc (output): This is an array that includes 1, 2 or 3; indicating the bracing
            location. 1 = Top 2 = Bottom 3 = All (top and bottom)
        RD1 (output): This is an array that includes the relative location of the point
            bracing (when MyType = 1) or the relative location of the start of the uniform
            bracing (when MyType = 2).
        RD2 (output): This is an array that includes the relative location of the start of
            the uniform bracing (when MyType = 2). This item does not apply for point
            bracing (when MyType = 1).
        Dist1 (output): This is an array that includes the actual location of the point
            bracing (when MyType = 1) or the actual location of the start of the uniform
            bracing (when MyType = 2). [L]
        Dist2 (output): This is an array that includes the actual location of the start of
            the uniform bracing (when MyType = 2). [L] This item does not apply for point
            bracing (when MyType = 1).
        """
        _r = self._raw.GetLateralBracing(Name, 0, [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetLateralBracing falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadDeformation(self, Name: str, ItemType: int = 0):
        """This function retrieves the deformation load assignments to frame objects. The function
        returns zero if the load assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of deformation loads retrieved for the
            specified frame objects.
        FrameName (output): This is an array that includes the name of the frame object
            associated with each deformation load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each deformation load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the frame object specified by the Name item. If this item is
            Group, the assignments are retrieved for all frame objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected frame objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadDeformation(Name, 0, [], [], [], [], [], [], [], [], [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetLoadDeformation falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadDistributedWthGUID(self, Name: str, ItemType: int = 0):
        """This function is identical to GetLoadDistributed but it includes an extra return parameter,
        which includes the global unique IDs of the retrieved distributed loads. The
        function returns zero if the load assignments are successfully retrieved, otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of distributed loads retrieved for the
            specified frame objects.
        FrameName (output): This is an array that includes the name of the frame object
            associated with each distributed load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the distributed loads are specified.
        MyType (output): This is an array that includes 1 or 2, indicating the type of
            distributed load. 1 = Force 2 = Moment
        CSys (output): This is an array that includes the name of the coordinate system in
            which each distributed load is defined. It may be Local or the name of a defined
            coordinate system.
        Dir (output): This is an array that includes an integer between 1 and 11, indicating
            the direction of the load. 1 = Local 1 axis (only applies when CSys is Local) 2
            = Local 2 axis (only applies when CSys is Local) 3 = Local 3 axis (only applies
            when CSys is Local) 4 = X direction (does not apply when CSys is Local) 5 = Y
            direction (does not apply when CSys is Local) 6 = Z direction (does not apply
            when CSys is Local) 7 = Projected X direction (does not apply when CSys is
            Local) 8 = Projected Y direction (does not apply when CSys is Local) 9 =
            Projected Z direction (does not apply when CSys is Local) 10 = Gravity direction
            (only applies when CSys is Global) 11 = Projected Gravity direction (only
            applies when CSys is Global) The positive gravity direction (see Dir = 10 and
            11) is in the negative Global Z direction.
        RD1 (output): This is an array that includes the relative distance from the I-End of
            the frame object to the start of the distributed load.
        RD2 (output): This is an array that includes the relative distance from the I-End of
            the frame object to the end of the distributed load.
        Dist1 (output): This is an array that includes the actual distance from the I-End of
            the frame object to the start of the distributed load. [L]
        Dist2 (output): This is an array that includes the actual distance from the I-End of
            the frame object to the end of the distributed load. [L]
        Val1 (output): This is an array that includes the load value at the start of the
            distributed load. [F/L] when MyType is 1 and [FL/L] when MyType is 2
        Val2 (output): This is an array that includes the load value at the end of the
            distributed load. [F/L] when MyType is 1 and [FL/L] when MyType is 2
        GUID (output): This is an array that includes the global unique ID of the
            distributed load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the frame object specified by the Name item. If this item is
            Group, the assignments are retrieved for all frame objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected frame objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadDistributedWthGUID(Name, 0, [], [], [], [], [], [], [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetLoadDistributedWthGUID falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadDistributed(self, Name: str, ItemType: int = 0):
        """This function retrieves the distributed load assignments to frame objects. The function
        returns zero if the load assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of distributed loads retrieved for the
            specified frame objects.
        FrameName (output): This is an array that includes the name of the frame object
            associated with each distributed load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the distributed loads are specified.
        MyType (output): This is an array that includes 1 or 2, indicating the type of
            distributed load. 1 = Force 2 = Moment
        CSys (output): This is an array that includes the name of the coordinate system in
            which each distributed load is defined. It may be Local or the name of a defined
            coordinate system.
        Dir (output): This is an array that includes an integer between 1 and 11, indicating
            the direction of the load. 1 = Local 1 axis (only applies when CSys is Local) 2
            = Local 2 axis (only applies when CSys is Local) 3 = Local 3 axis (only applies
            when CSys is Local) 4 = X direction (does not apply when CSys is Local) 5 = Y
            direction (does not apply when CSys is Local) 6 = Z direction (does not apply
            when CSys is Local) 7 = Projected X direction (does not apply when CSys is
            Local) 8 = Projected Y direction (does not apply when CSys is Local) 9 =
            Projected Z direction (does not apply when CSys is Local) 10 = Gravity direction
            (only applies when CSys is Global) 11 = Projected Gravity direction (only
            applies when CSys is Global) The positive gravity direction (see Dir = 10 and
            11) is in the negative Global Z direction.
        RD1 (output): This is an array that includes the relative distance from the I-End of
            the frame object to the start of the distributed load.
        RD2 (output): This is an array that includes the relative distance from the I-End of
            the frame object to the end of the distributed load.
        Dist1 (output): This is an array that includes the actual distance from the I-End of
            the frame object to the start of the distributed load. [L]
        Dist2 (output): This is an array that includes the actual distance from the I-End of
            the frame object to the end of the distributed load. [L]
        Val1 (output): This is an array that includes the load value at the start of the
            distributed load. [F/L] when MyType is 1 and [FL/L] when MyType is 2
        Val2 (output): This is an array that includes the load value at the end of the
            distributed load. [F/L] when MyType is 1 and [FL/L] when MyType is 2
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the frame object specified by the Name item. If this item is
            Group, the assignments are retrieved for all frame objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected frame objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadDistributed(Name, 0, [], [], [], [], [], [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetLoadDistributed falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadGravity(self, Name: str, ItemType: int = 0):
        """This function retrieves the gravity load assignments to frame objects. The function returns
        zero if the load assignments are successfully retrieved, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of gravity loads retrieved for the specified
            frame objects.
        FrameName (output): This is an array that includes the name of the frame object
            associated with each gravity load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the gravity load multipliers are specified.
        CSys (output): This is an array that includes the name of the coordinate system
            associated with each gravity load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the frame object specified by the Name item. If this item is
            Group, the assignments are retrieved for all frame objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected frame objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadGravity(Name, 0, [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetLoadGravity falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadPoint(self, Name: str, ItemType: int = 0):
        """This function retrieves the point load assignments to frame objects. The function returns
        zero if the load assignments are successfully retrieved, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        NumberItems (output): The total number of point loads retrieved for the specified
            frame objects.
        FrameName (output): This is an array that includes the name of the frame object
            associated with each point load.
        LoadPat (output): This is an array that includes the name of the coordinate system
            in which the point loads are specified.
        MyType (output): This is an array that includes 1 or 2, indicating the type of point
            load. 1 = Force 2 = Moment
        CSys (output): This is an array that includes the name of the coordinate system in
            which each point load is defined. It may be Local or the name of a defined
            coordinate system.
        Dir (output): This is an array that includes an integer between 1 and 11 indicating
            the direction of the load. 1 = Local 1 axis (only applies when CSys is Local) 2
            = Local 2 axis (only applies when CSys is Local) 3 = Local 3 axis (only applies
            when CSys is Local) 4 = X direction (does not apply when CSys is Local) 5 = Y
            direction (does not apply when CSys is Local) 6 = Z direction (does not apply
            when CSys is Local) 7 = Projected X direction (does not apply when CSys is
            Local) 8 = Projected Y direction (does not apply when CSys is Local) 9 =
            Projected Z direction (does not apply when CSys is Local) 10 = Gravity direction
            (only applies when CSys is Global) 11 = Projected Gravity direction (only
            applies when CSys is Global) The positive gravity direction (see Dir = 10 and
            11) is in the negative Global Z direction.
        RelDist (output): This is an array that includes the relative distance from the
            I-End of the frame object to the location where the point load is applied.
        Dist (output): This is an array that includes the actual distance from the I-End of
            the frame object to the location where the point load is applied. [L]
        Val (output): This is an array that includes the value of the point load. [F] when
            MyType is 1 and [FL] when MyType is 2
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the frame object specified by the Name item. If this item is
            Group, the assignments are retrieved for all frame objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected frame objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadPoint(Name, 0, [], [], [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetLoadPoint falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadStrain(self, Name: str, ItemType: int = 0):
        """This function retrieves the strain load assignments to frame objects. The function returns
        zero if the strain load assignments are successfully retrieved, otherwise it returns
        a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of strain loads retrieved for the specified
            frame objects.
        FrameName (output): This is an array that includes the name of the frame object
            associated with each strain load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each strain load.
        DOF (output): This is an array that includes 1, 2, 3, 4, 5 or 6, indicating the
            degree of freedom associated with each strain load. 1 = Strain11 2 = Strain12 3
            = Strain13 4 = Curvature1 5 = Curvature2 6 = Curvature3
        Val (output): This is an array that includes the strain value. [L/L] for DOF = 1, 2
            and 3 and [1/L] for DOF = 4, 5 and 6
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the strain load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the frame object specified by the Name item. If this item is
            Group, the assignments are retrieved for all frame objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected frame objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadStrain(Name, 0, [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetLoadStrain falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadTargetForce(self, Name: str, ItemType: int = 0):
        """This function retrieves the target force assignments to frame objects. The function returns
        zero if the target force assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of deformation loads retrieved for the
            specified frame objects.
        FrameName (output): This is an array that includes the name of the frame object
            associated with each target force.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each target force.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the frame object specified by the Name item. If this item is
            Group, the assignments are retrieved for all frame objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected frame objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadTargetForce(Name, 0, [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetLoadTargetForce falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLoadTemperature(self, Name: str, ItemType: int = 0):
        """This function retrieves the temperature load assignments to frame objects. The function
        returns zero if the load assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The total number of temperature loads retrieved for the
            specified frame objects.
        FrameName (output): This is an array that includes the name of the frame object
            associated with each temperature load.
        LoadPat (output): This is an array that includes the name of the load pattern
            associated with each temperature load.
        MyType (output): This is an array that includes 1, 2 or 3, indicating the type of
            temperature load. 1 = Temperature 2 = Temperature gradient along local 2 axis 3
            = Temperature gradient along local 3 axis
        Val (output): This is an array that includes the temperature load value. [T] for
            MyType= 1 and [T/L] for MyType= 2 and 3
        PatternName (output): This is an array that includes the joint pattern name, if any,
            used to specify the temperature load.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignments
            are retrieved for the frame object specified by the Name item. If this item is
            Group, the assignments are retrieved for all frame objects in the group
            specified by the Name item. If this item is SelectedObjects, assignments are
            retrieved for all selected frame objects, and the Name item is ignored.
        """
        _r = self._raw.GetLoadTemperature(Name, 0, [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetLoadTemperature falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocalAxesAdvanced(self, Name: str):
        """This function retrieves the advanced local axes assignments to frame objects. The function
        returns zero if the advanced local axes assignments are successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        Active (output): This is True if advanced local axes exist.
        Plane2 (output): This is 12 or 13, indicating that the local plane determined by the
            plane reference vector is the 1-2 plane or the 1-3 plane. This item applies only
            when the Active item is True.
        PlVectOpt (output): This is 1, 2, or 3, indicating the plane reference vector
            option. This item applies only when the Active item is True. 1 = Coordinate
            direction 2 = Two joints 3 = User vector
        PlCSys (output): The coordinate system used to define the plane reference vector
            coordinate directions and the plane user vector. This item applies when the
            Active item is True and the PlVectOpt item is 1 or 3.
        PlDir (output): This is an array dimensioned to 1 (2 integers), indicating the plane
            reference vector primary and secondary coordinate directions, PlDir(0) and
            PlDir(1) respectively, taken at the object center in the specified coordinate
            system and used to determine the plane reference vector. This item applies when
            the Active item is True and the PlVectOpt item is 1. Possible coordinate
            direction values are: 1 = +X -1 = -X 2 = +Y -2 = -Y 3 = +Z -3 = -Z 4 = +CR -4 =
            -CR 5 = +CA -5 = -CA 6 = +CZ -6 = -CZ 7 = +SR -7 = -SR 8 = +SA -8 = -SA 9 = +SB
            -9 = -SB
        PlPt (output): This is an array dimensioned to 1 (2 strings), indicating the labels
            of two joints that define the plane reference vector. Either of these joints may
            be specified as None to indicate the center of the specified object. If both
            joints are specified as None, they are not used to define the plane reference
            vector. This item applies when the Active item is True and the PlVectOpt item is
            2.
        PlVect (output): This is an array dimensioned to 2 (3 doubles) that defines the
            plane reference vector. This item applies when the Active item is True and the
            PlVectOpt item is 3.
        """
        _r = self._raw.GetLocalAxesAdvanced(Name, False, 0, 0, "", [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetLocalAxesAdvanced falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLocalAxes(self, Name: str, Advanced: bool):
        """This function retrieves the frame local axis angle assignment for frame objects. The
        function returns zero if the assignment is successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        Ang (output): This is the angle that the local 2 and 3 axes are rotated about the
            positive local 1 axis, from the default orientation or, if the Advanced item is
            True, from the orientation determined by the plane reference vector. The
            rotation for a positive angle appears counter clockwise when the local +1 axis
            is pointing toward you. [deg]
        Advanced (input): This item is True if the line object local axes orientation was
            obtained using advanced local axes parameters.
        """
        _r = self._raw.GetLocalAxes(Name, 0.0, Advanced)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetLocalAxes falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetMass(self, Name: str, MassOverL: float):
        """This function retrieves the frame mass per unit length assignment for frame objects. The
        function returns zero if the mass assignment is successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        MassOverL (input): The mass per unit length assigned to the frame object. [M/L]
        """
        _r = self._raw.GetMass(Name, MassOverL)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetMass falhou (ret={_r})".format(_r=_r))
        return None

    def GetMatTemp(self, Name: str, Temp: float):
        """This function retrieves the material temperature assignments to frame objects. The function
        returns zero if the material temperature assignments are successfully retrieved,
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        Temp (input): This is the material temperature value assigned to the frame object.
            [T]
        PatternName (output): This is blank or the name of a defined joint pattern. If it is
            blank, the material temperature for the frame object is uniform along the object
            at the value specified by Temp. If PatternName is the name of a defined joint
            pattern, the material temperature for the frame object may vary from one end to
            the other. The material temperature at each end of the object is equal to the
            specified temperature multiplied by the pattern value at the joint at the end of
            the frame object.
        """
        _r = self._raw.GetMatTemp(Name, Temp, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetMatTemp falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetMaterialOverwrite(self, Name: str):
        """This function retrieves the material overwrite assigned to a frame object, if any. It
        returns None if there is no material overwrite assignment. The function returns zero
        if the material overwrite assignment is successfully retrieved, otherwise it returns
        a nonzero value.
    
        Name (input): The name of a defined frame object.
        PropName (output): This is None, indicating that no material overwrite exists for
            the specified frame object, or it is the name of an existing material property.
        """
        _r = self._raw.GetMaterialOverwrite(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetMaterialOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetModifiers(self, Name: str):
        """This function retrieves the frame modifier assignment for frame objects. The default value
        for all modifiers is one. The function returns zero if the modifier assignments are
        successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        Value (output): This is an array of eight unitless modifiers. Value(0) = Cross
            sectional area modifier Value(1) = Shear area in local 2 direction modifier
            Value(2) = Shear area in local 3 direction modifier Value(3) = Torsional
            constant modifier Value(4) = Moment of inertia about local 2 axis modifier
            Value(5) = Moment of inertia about local 3 axis modifier Value(6) = Mass
            modifier Value(7) = Weight modifier
        """
        _r = self._raw.GetModifiers(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetModifiers falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameList(self):
        """This function retrieves the names of all defined frame objects. The function returns zero if
        the names are successfully retrieved, otherwise it returns nonzero.
    
        NumberNames (output): The number of frame object names retrieved by the program.
        MyName (output): This is a one-dimensional array of frame object names. The MyName
            array is created as a dynamic, zero-based, array by the APIuser: Dim MyName() as
            String The array is dimensioned to (NumberNames 1) inside the Sap2000 program,
            filled with the names, and returned to the APIuser.
        """
        _r = self._raw.GetNameList(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetOutputStations(self, Name: str, NoOutPutAndDesignAtElementEnds: bool, NoOutPutAndDesignAtPointLoads: bool):
        """This function retrieves frame object output station data. The function returns zero if the
        data is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        MyType (output): This is either 1 or 2 indicating how the output stations are
            specified. 1 = maximum segment size, that is, maximum station spacing 2 =
            minimum number of stations
        MaxSegSize (output): The maximum segment size, that is, the maximum station spacing.
            This item applies only when MyType = 1. [L]
        MinSections (output): The minimum number of stations. This item applies only when
            MyType = 2.
        NoOutPutAndDesignAtElementEnds (input): If this item is True, no additional output
            stations are added at the ends of line elements when the frame object is
            internally meshed.
        NoOutPutAndDesignAtPointLoads (input): If this item is True, no additional output
            stations are added at point load locations.
        """
        _r = self._raw.GetOutputStations(Name, 0, 0.0, 0, NoOutPutAndDesignAtElementEnds, NoOutPutAndDesignAtPointLoads)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetOutputStations falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPDeltaForce(self, Name: str, NumberForces: int, PDeltaForce: list[float]):
        """This function retrieves the P-Delta force assignments to frame objects. P-Delta forces do
        not apply to curved frame objects. If you request data for a curved frame, an error
        is returned. The function returns zero if the assignments are successfully
        retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing straight frame object.
        NumberForces (input): The number of P-Delta forces assigned to the frame object.
        PDeltaForce (input): This is an array of the P-Delta force values assigned to the
            frame object. [F]
        Dir (output): This is an array that contains 0, 1, 2 or 3, indicating the direction
            of each P-Delta force assignment. 0 = Frame object local 1-axis direction 1 =
            Projected X direction in CSys coordinate system 2 = Projected Y direction in
            CSys coordinate system 3 = Projected Z direction in CSys coordinate system
        CSys (output): This is an array that contains the name of the coordinate system in
            which each projected P-Delta force is defined. This item is blank when the Dir
            item is zero, that is, when the P-Delta force is defined in the frame object
            local 1-axis direction.
        """
        _r = self._raw.GetPDeltaForce(Name, NumberForces, PDeltaForce, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetPDeltaForce falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPoints(self, Name: str):
        """This function retrieves the names of the point objects at each end of a specified frame
        object. The function returns zero if the point names are successfully retrieved,
        otherwise it returns a nonzero value.
    
        Name (input): The name of a defined frame object.
        Point1 (output): The name of the point object at the I-End of the specified frame
            object.
        Point2 (output): The name of the point object at the J-End of the specified frame
            object.
        """
        _r = self._raw.GetPoints(Name, "", "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetPoints falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetReleases(self, Name: str):
        """This function retrieves the frame object end release and partial fixity assignments. The
        function returns zero if the assignments are successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        """
        _r = self._raw.GetReleases(Name, [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetReleases falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSectionNonPrismatic(self, Name: str, PropName: str):
        """This function retrieves the nonprismatic frame section property data assigned to a frame
        object. The function returns zero if the nonprismatic frame object property data is
        successfully retrieved, otherwise it returns a nonzero value. The function returns
        an error if the section property assigned to the frame object is not a nonprismatic
        property.
    
        Name (input): The name of a defined frame object.
        PropName (input): The name of the nonprismatic frame section property assigned to
            the frame object.
        sVarTotalLength (output): This is the total assumed length of the nonprismatic
            section. Enter 0 for this item to indicate that the section length is the same
            as the frame object length.
        sVarRelStartLoc (output): This is the relative distance along the nonprismatic
            section to the I-End (start) of the frame object. This item is ignored when the
            sVarTotalLengthitem is 0.
        """
        _r = self._raw.GetSectionNonPrismatic(Name, PropName, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetSectionNonPrismatic falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSection(self, Name: str, PropName: str, SAuto: str):
        """This function retrieves the frame section property assigned to a frame object. The function
        returns zero if the frame object property is successfully retrieved, otherwise it
        returns a nonzero value.
    
        Name (input): The name of a defined frame object.
        PropName (input): If no auto select list is assigned to the frame object, this is
            the name of the frame section property assigned to the frame object. If an auto
            select list is assigned to the frame object, this is the name of the frame
            section property, within the auto select list, which is currently being used as
            the analysis property for the frame object. If this item is None, no frame
            section property is assigned to the frame object.
        SAuto (input): This is the name of the auto select list assigned to the frame
            object, if any. If this item is returned as a blank string, no auto select list
            is assigned to the frame object.
        """
        _r = self._raw.GetSection(Name, PropName, SAuto)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetSection falhou (ret={_r})".format(_r=_r))
        return None

    def GetSelected(self, Name: str):
        """This function retrieves the selected status for a frame object. The function returns zero if
        the selected status is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        Selected (output): This item returns True if the specified frame object is selected,
            otherwise it returns False.
        """
        _r = self._raw.GetSelected(Name, False)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetSelected falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetSpring(self, Name: str, LinkProp: list[str]):
        """This function retrieves the spring assignments to a frame object. The function returns zero
        if the assignments are successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        NumberSprings (output): The number of springs assignments made to the specified
            frame object.
        MyType (output): Each value in this array is either 1 or 2, indicating the spring
            property type. 1 = Simple spring 2 = Link property
        s (output): Each value in this array is the simple spring stiffness per unit length
            of the frame object. This item applies only when the corresponding MyType = 1.
            [F/L 2 ]
        SimpleSpringType (output): Each value in this array is 1, 2 or 3, indicating the
            simple spring type. This item applies only when the corresponding MyType = 1. 1
            = Spring resists tension and compression 2 = Spring resists compression only 3 =
            Spring resists tension only
        LinkProp (input): Each value in this array is the name of the link property assigned
            to the spring. This item applies only when the corresponding MyType = 2.
        SpringLocalOneType (output): Each value in this array is 1, 2 or 3, indicating the
            method used to specify the spring positive local 1-axis orientation. 1 =
            Parallel to frame object local axis 2 = In the frame object 2-3 plane 3 = User
            specified direction vector
        Dir (output): Each value in this array is 1, 2, 3, -1, -2 or -3, indicating the
            frame object local axis that corresponds to the positive local 1-axis of the
            spring. This item applies only when the corresponding SpringLocalOneType = 1.
        Plane23Angle (output): Each value in this array is the angle in the frame object 2-3
            plane measured counter clockwise from the frame positive 2-axis to the spring
            positive 1-axis. This item applies only when the corresponding
            SpringLocalOneType = 2. [deg]
        VecX (output): Each value in this array is the X-axis or frame local 1-axis
            component (depending on the CSys specified) of the user specified direction
            vector for the spring local 1-axis. The direction vector is in the coordinate
            system specified by the CSys item. This item applies only when the corresponding
            SpringLocalOneType = 3.
        VecY (output): Each value in this array is the Y-axis or frame local 2-axis
            component (depending on the CSys specified) of the user specified direction
            vector for the spring local 1-axis. The direction vector is in the coordinate
            system specified by the CSys item. This item applies only when the corresponding
            SpringLocalOneType = 3.
        VecZ (output): Each value in this array is the X-axis or frame local 3-axis
            component (depending on the CSys specified) of the user specified direction
            vector for the spring local 1-axis. The direction vector is in the coordinate
            system specified by the CSys item. This item applies only when the corresponding
            SpringLocalOneType = 3.
        CSys (output): Each value in this array is Local (meaning the frame object local
            coordinate system) or the name of a defined coordinate system. This item is the
            coordinate system in which the user specified direction vector, Vec, is
            specified. This item applies only when the corresponding SpringLocalOneType = 3.
        Ang (output): Each value in this array is the angle that the link local 2-axis is
            rotated from its default orientation. This item applies only when the
            corresponding MyType = 2. [deg]
        """
        _r = self._raw.GetSpring(Name, 0, [], [], [], LinkProp, [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetSpring falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTCLimits(self, Name: str, LimitCompressionExists: bool, LimitTensionExists: bool):
        """This function retrieves the tension/compression force limit assignments to frame objects.
        The function returns zero if the assignments are successfully retrieved, otherwise
        it returns a nonzero value. Note that the tension and compression limits are used
        only in nonlinear analyses.
    
        Name (input): The name of an existing frame object.
        LimitCompressionExists (input): This item is True if a compression force limit
            exists for the frame object.
        LimitCompression (output): The compression force limit for the frame object. [F]
        LimitTensionExists (input): This item is True if a tension force limit exists for
            the frame object.
        LimitTension (output): The tension force limit for the frame object. [F]
        """
        _r = self._raw.GetTCLimits(Name, LimitCompressionExists, 0.0, LimitTensionExists, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetTCLimits falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTransformationMatrix(self, Name: str, IsGlobal: bool = True):
        """The function returns zero if the frame object transformation matrix is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        Value (output): Value is an array of nine direction cosines that define the
            transformation matrix. The following matrix equation shows how the
            transformation matrix is used to convert items from the frame object local
            coordinate system to the global coordinate system. In the equation, c0 through
            c8 are the nine values from the transformation array, (Local1, Local2, Local3)
            are an item (such as a load) in the object local coordinate system, and
            (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate system.
            The transformation from the local coordinate system to the present coordinate
            system is the same as that shown above for the global system if you substitute
            the present system for the global system.
        IsGlobal (input): If this item is True, the transformation matrix is between the
            Global coordinate system and the frame object local coordinate system. If this
            item is False, the transformation maxtrix is between the present coordinate
            system and the frame object local coordinate system.
        """
        _r = self._raw.GetTransformationMatrix(Name, [], IsGlobal)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetTransformationMatrix falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetTypeOAPI(self, Name: str):
        """This function retrieves the type of frame object (straight or curved). The function returns
        zero if the frame object type is successfully retrieved, otherwise it returns a
        nonzero value.
    
        Name (input): The name of a defined frame object.
        MyType (output): This is Straight or Curved, indicating the type of frame object.
        """
        _r = self._raw.GetTypeOAPI(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.FrameObj.GetTypeOAPI falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetAutoMesh(self, Name: str, AutoMesh: bool, AutoMeshAtPoints: bool, AutoMeshAtLines: bool, NumSegs: int, AutoMeshMaxLength: float, ItemType: int = 0):
        """This function makes automatic meshing assignments to frame objects. The function returns
        zero if the meshing options are successfully assigned, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        AutoMesh (input): This item is True if the frame object is to be automatically
            meshed by the program when the analysis model is created.
        AutoMeshAtPoints (input): This item is applicable only when the AutoMesh item is
            True. If this item is True, the frame object is automatically meshed at
            intermediate joints along its length.
        AutoMeshAtLines (input): This item is applicable only when the AutoMesh item is
            True. If this item is True, the frame object is automatically meshed at
            intersections with other frames, area object edges and solid object edges.
        NumSegs (input): This item is applicable only when the AutoMesh item is True. It is
            the minimum number of elements into which the frame object is automatically
            meshed. If this item is zero, the number of elements is not checked when the
            automatic meshing is done.
        AutoMeshMaxLength (input): This item is applicable only when the AutoMesh item is
            True. It is the maximum length of auto meshed frame elements. If this item is
            zero, the element length is not checked when the automatic meshing is done. [L]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetAutoMesh(Name, AutoMesh, AutoMeshAtPoints, AutoMeshAtLines, NumSegs, AutoMeshMaxLength, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetAutoMesh falhou (ret={_r})".format(_r=_r))
        return None

    def SetCurved(self, Name: str, MyType: int, x: float, y: float, z: float, PointName: str, Radius: float, NumSegs: int, CSys: str = 'Global'):
        """This function changes the curve data for a curved frame object and sets straight frame
        objects to be curved. The function returns zero if the frame object type is
        successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of a defined curved frame object.
        MyType (input): This is 1, 2, 3, 4, or 5, indicating the curved frame type. 1 =
            Circular Arc Specified by a Third Point Name 2 = Circular Arc Specified by Third
            Point Coordinates 3 = Circular Arc Specified by Planar Point Coordinates and
            Radius 4 = Parabolic Arc Specified by a Third Point Name 5 = Parabolic Arc
            Specified by Third Point Coordinates MyTypes 1, 2, 4, and 5 all define the curve
            by three points. The three points are the two end point of the frame object and
            a third point defined by naming an existing point object or specifying point
            coordinates. MyType 3 defines a circular curved frame by it end points, the
            coordinates of another point that lies in the plane of the curve but not
            necessarily on the curved frame, and a curve radius.
        PointName (input): This is the name of the point object that is the third point on
            the curved frame. This item applies for MyType 1 and 4. It does not apply for
            MyType 2, 3 and 5.
        Radius (input): The radius of the circular curved frame. This item only applies for
            MyType 3. [L]
        NumSegs (input): This is the number of segments into which the program internally
            divides the curved frame.
        CSys (input): This is the coordinate system in which the coordinates x, y and z are
            defined.
        """
        _r = self._raw.SetCurved(Name, MyType, x, y, z, PointName, Radius, NumSegs, CSys)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetCurved falhou (ret={_r})".format(_r=_r))
        return None

    def SetDesignProcedure(self, Name: str, MyType: int, ItemType: int = 0):
        """This function sets the design procedure for frame objects. The function returns zero if the
        design procedure is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        MyType (input): This is 1 or 2, indicating the design procedure type desired for the
            specified frame object. 1 = Default from material 2 = No design
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 Selection = 2 If this item is Object, the assignment is
            made to the frame object specified by the Name item. If this item is Group, the
            assignment is made to all frame objects in the group specified by the Name item.
            If this item is Selection, assignment is made to all selected frame objects and
            the Name item is ignored.
        """
        _r = self._raw.SetDesignProcedure(Name, MyType, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetDesignProcedure falhou (ret={_r})".format(_r=_r))
        return None

    def SetEndLengthOffset(self, Name: str, AutoOffset: bool, Length1: float, Length2: float, rz: float, ItemType: int = 0):
        """This function assigns frame object end offsets along the 1-axis of the object. The function
        returns zero if the offsets are successfully assigned, otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        AutoOffset (input): If this item is True, the end length offsets are automatically
            determined by the program from object connectivity, and the Length1, Length2 and
            rz items are ignored.
        Length1 (input): The offset length along the 1-axis of the frame object at the I-End
            of the frame object. [L]
        Length2 (input): The offset along the 1-axis of the frame object at the J-End of the
            frame object. [L]
        rz (input): The rigid zone factor. This is the fraction of the end offset length
            assumed to be rigid for bending and shear deformations.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetEndLengthOffset(Name, AutoOffset, Length1, Length2, rz, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetEndLengthOffset falhou (ret={_r})".format(_r=_r))
        return None

    def SetEndSkew(self, Name: str, SkewI: float, SkewJ: float, ItemType: int = 0):
        """This function assigns frame object end skew data. End skew data is used in the program to
        plot the extruded view of bridge objects that have been updated as spine models
        only. The function returns zero if the end skew data is successfully assigned,
        otherwise it returns a nonzero value. End skew assignments are applicable only to
        straight frame objects.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        SkewI (input): The angle in degrees measured counter clockwise from the positive
            local 3-axis to a line parallel to the I-End of the frame object (-90 < SkewI <
            90). [deg]
        SkewJ (input): The angle in degrees measured counter clockwise from the positive
            local 3-axis to a line parallel to the J-End of the frame object (-90 < SkewJ <
            90). [deg]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetEndSkew(Name, SkewI, SkewJ, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetEndSkew falhou (ret={_r})".format(_r=_r))
        return None

    def SetFireProofing_1(self, Name: str, MyType: int, Thickness: float, Perimeter: float, Density: float, tf: bool, IncludeInGravityLoads: bool, IncludeInThisLoadPattern: str = 'None', ItemType: int = 0):
        """This function sets the fireproofing assignments to existing frame objects. The function
        returns zero if the fireproofing assignments are successfully set, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame object.
        MyType (input): This is 1, 2 or 3, indicating the type of fireproofing assigned. 1 =
            Sprayed on - program calculate section perimeter 2 = Sprayed on - user provides
            section perimeter 3 = Concrete encased
        Thickness (input): When MyType = 1 or MyType = 2 this is the thickness of the
            sprayed on fireproofing. When MyType = 3 this is the concrete cover dimension.
            [L]
        Perimeter (input): This item applies only when MyType = 2. It is the length of
            fireproofing applied measured around the perimeter of the frame object cross-
            section. [L]
        Density (input): This is the weight per unit volume of the fireproofing material.
            [F/L3]
        tf (input): This item applies only when MyType = 1 or MyType = 3. If this item is
            True, the fireproofing is assumed to be applied to the top flange of the
            section. If it is False, the program assumes no fireproofing is applied to the
            section top flange. This flag applies for I, channel and double channel
            sections.
        IncludeInGravityLoads (input): If this item is True the fireproofing is included
            gravity loads applied in the X, Y and Z directions.
        IncludeInThisLoadPattern (input): This item is either None or the name of an
            existing load pattern. If it is the name of a load pattern then the weight of
            the fireproofing is applied as a distributed load in the global Z direction in
            the load pattern.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetFireProofing_1(Name, MyType, Thickness, Perimeter, Density, tf, IncludeInGravityLoads, IncludeInThisLoadPattern, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetFireProofing_1 falhou (ret={_r})".format(_r=_r))
        return None

    def SetGUID(self, Name: str, GUID: str = ''):
        """This function sets the GUID for the specified frame object. If the GUID is passed in as a
        blank string, the program automatically creates a GUID for the object. This function
        returns zero if the frame object GUID is successfully set; otherwise it returns
        nonzero.
    
        Name (input): The name of an existing frame object.
        GUID (input): The GUID (Global Unique ID) for the specified frame object.
        """
        _r = self._raw.SetGUID(Name, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetGUID falhou (ret={_r})".format(_r=_r))
        return None

    def SetGroupAssign(self, Name: str, GroupName: str, Remove: bool, ItemType: int = 0):
        """This function adds or removes frame objects from a specified group. The function returns
        zero if the group assignment is successful, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        GroupName (input): The name of an existing group to which the assignment is made.
        Remove (input): If this item is False, the specified frame objects are added to the
            group specified by the GroupName item. If it is True, the frame objects are
            removed from the group.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the frame
            object specified by the Name item is added or removed from the group specified
            by the GroupName item. If this item is Group, all frame objects in the group
            specified by the Name item are added or removed from the group specified by the
            GroupName item. If this item is SelectedObjects, all selected frame objects are
            added or removed from the group specified by the GroupName item, and the Name
            item is ignored.
        """
        _r = self._raw.SetGroupAssign(Name, GroupName, Remove, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetGroupAssign falhou (ret={_r})".format(_r=_r))
        return None

    def SetInsertionPoint(self, Name: str, CardinalPoint: int, Mirror2: bool, StiffTransform: bool, Offset1: list[float], Offset2: list[float], CSys: str = 'Local', ItemType: int = 0):
        """This function assigns frame object insertion point data. The assignments include the
        cardinal point and end joint offsets. The function returns zero if the insertion
        point data is successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        CardinalPoint (input): This is a numeric value from 1 to 11 that specifies the
            cardinal point for the frame object. The cardinal point specifies the relative
            position of the frame section on the line representing the frame object. 1 =
            bottom left 2 = bottom center 3 = bottom right 4 = middle left 5 = middle center
            6 = middle right 7 = top left 8 = top center 9 = top right 10 = centroid 11 =
            shear center
        Mirror2 (input): If this item is True, the frame object section is assumed to be
            mirrored (flipped) about its local 2-axis.
        StiffTransform (input): If this item is True, the frame object stiffness is
            transformed for cardinal point and joint offsets from the frame section
            centroid.
        Offset1 (input): This is an array of three joint offset distances, in the coordinate
            directions specified by CSys, at the I-End of the frame object. [L] Offset1(0) =
            Offset in the 1-axis or X-axis direction Offset1(1) = Offset in the 2-axis or
            Y-axis direction Offset1(2) = Offset in the 3-axis or Z-axis direction
        Offset2 (input): This is an array of three joint offset distances, in the coordinate
            directions specified by CSys, at the J-End of the frame object. [L] Offset2(0) =
            Offset in the 1-axis or X-axis direction Offset2(1) = Offset in the 2-axis or
            Y-axis direction Offset2(2) = Offset in the 3-axis or Z-axis direction
        CSys (input): This is Local or the name of a defined coordinate system. It is the
            coordinate system in which the Offset1 and Offset2 items are specified.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetInsertionPoint(Name, CardinalPoint, Mirror2, StiffTransform, Offset1, Offset2, CSys, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetInsertionPoint falhou (ret={_r})".format(_r=_r))
        return None

    def SetLateralBracing(self, Name: str, MyType: int, Loc: int, MyDist1: float, MyDist2: float, RelDist: bool = True, ItemType: int = 0):
        """This function assigns a lateral bracing location to frame objects. The function returns zero
        if the location is successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        MyType (input): This is 1 or 2, indicating the bracing type assigned. 1 = Point
            bracing 2 = Uniform bracing
        Loc (input): This is 1, 2 or 3, indicating the bracing location. 1 = Top 2 = Bottom
            3 = All (top and bottom)
        MyDist1 (input): When MyType = 1 this is the location of the point bracing. When
            MyType = 2 this is the location of the start of the uniform bracing. [L] when
            RelDist = False
        MyDist2 (input): This item is not used when MyType = 1. When MyType = 2 this is the
            location of the end of the uniform bracing. [L] when RelDist = False
        RelDist (input): If this item is True, MyDist1 and MyDist2 are relative distances;
            otherwise they are actual distances.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLateralBracing(Name, MyType, Loc, MyDist1, MyDist2, RelDist, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetLateralBracing falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadDeformation(self, Name: str, LoadPat: str, DOF: list[bool], d: list[float], ItemType: int = 0):
        """This function assigns deformation loads to frame objects. The function returns zero if the
        loads are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        DOF (input): This is a array of boolean values indicating if the considered degree
            of freedom has a deformation load. DOF(1) = U1 DOF(2) = U2 DOF(3) = U3 DOF(4) =
            R1 DOF(5) = R2 DOF(6) = R3
        d (input): This is a array of deformation load values. The deformations specified
            for a given degree of freedom are applied only if the corresponding DOF item for
            that degree of freedom is True. d(1) = U1 deformation [L] d(2) = U2 deformation
            [L] d(3) = U3 deformation [L] d(4) = R1 deformation [rad] d(5) = R2 deformation
            [rad] d(6) = R3 deformation [rad]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetLoadDeformation(Name, LoadPat, DOF, d, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetLoadDeformation falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadDistributed(self, Name: str, LoadPat: str, MyType: eLoadDistributedType, Dir: eLoadDistributedDir, Dist1: float, Dist2: float, Val1: float, Val2: float, CSys: str = 'Global', RelDist: bool = True, Replace: bool = True, ItemType: int = 0):
        """This function assigns distributed loads to frame objects. The function returns zero if the
        loads are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        MyType (input): This is 1 or 2, indicating the type of distributed load. 1 = Force
            per unit length 2 = Moment per unit length
        Dir (input): This is an integer between 1 and 11, indicating the direction of the
            load. 1 = Local 1 axis (only applies when CSys is Local) 2 = Local 2 axis (only
            applies when CSys is Local) 3 = Local 3 axis (only applies when CSys is Local) 4
            = X direction (does not apply when CSys is Local) 5 = Y direction (does not
            apply when CSys is Local) 6 = Z direction (does not apply when CSys is Local) 7
            = Projected X direction (does not apply when CSys is Local) 8 = Projected Y
            direction (does not apply when CSys is Local) 9 = Projected Z direction (does
            not apply when CSys is Local) 10 = Gravity direction (only applies when CSys is
            Global) 11 = Projected Gravity direction (only applies when CSys is Global) The
            positive gravity direction (see Dir = 10 and 11) is in the negative Global Z
            direction.
        Dist1 (input): This is the distance from the I-End of the frame object to the start
            of the distributed load. This may be a relative distance (0 <= Dist1 <= 1) or an
            actual distance, depending on the value of the RelDist item. [L] when RelDist is
            False
        Dist2 (input): This is the distance from the I-End of the frame object to the end of
            the distributed load. This may be a relative distance (0 <= Dist2 <= 1) or an
            actual distance, depending on the value of the RelDist item. [L] when RelDist is
            False
        Val1 (input): This is the load value at the start of the distributed load. [F/L]
            when MyType is 1 and [FL/L] when MyType is 2
        Val2 (input): This is the load value at the end of the distributed load. [F/L] when
            MyType is 1 and [FL/L] when MyType is 2
        CSys (input): This is Local or the name of a defined coordinate system. It is the
            coordinate system in which the loads are specified.
        RelDist (input): If this item is True, the specified Dist item is a relative
            distance, otherwise it is an actual distance.
        Replace (input): If this item is True, all previous distributed loads, if any,
            assigned to the specified frame object(s), in the specified load pattern, are
            deleted before making the new assignment.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadDistributed(Name, LoadPat, MyType, Dir, Dist1, Dist2, Val1, Val2, CSys, RelDist, Replace, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetLoadDistributed falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadGravity(self, Name: str, LoadPat: str, x: float, y: float, z: float, Replace: bool = True, CSys: str = 'Global', ItemType: int = 0):
        """This function assigns gravity load multipliers to frame objects. The function returns zero
        if the loads are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        Replace (input): If this item is True, all previous gravity loads, if any, assigned
            to the specified frame object(s), in the specified load pattern, are deleted
            before making the new assignment.
        CSys (input): The coordinate system in which the x, y and z multipliers are
            specified.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadGravity(Name, LoadPat, x, y, z, Replace, CSys, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetLoadGravity falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadPoint(self, Name: str, LoadPat: str, MyType: int, Dir: int, Dist: float, Val: float, CSys: str = 'Global', RelDist: bool = True, Replace: bool = True, ItemType: int = 0):
        """This function assigns point loads to frame objects. The function returns zero if the loads
        are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        MyType (input): This is 1 or 2, indicating the type of point load. 1 = Force 2 =
            Moment
        Dir (input): This is an integer between 1 and 11, indicating the direction of the
            load. 1 = Local 1 axis (only applies when CSys is Local) 2 = Local 2 axis (only
            applies when CSys is Local) 3 = Local 3 axis (only applies when CSys is Local) 4
            = X direction (does not apply when CSys is Local) 5 = Y direction (does not
            apply when CSys is Local) 6 = Z direction (does not apply when CSys is Local) 7
            = Projected X direction (does not apply when CSys is Local) 8 = Projected Y
            direction (does not apply when CSys is Local) 9 = Projected Z direction (does
            not apply when CSys is Local) 10 = Gravity direction (only applies when CSys is
            Global) 11 = Projected Gravity direction (only applies when CSys is Global) The
            positive gravity direction (see Dir = 10 and 11) is in the negative Global Z
            direction.
        Dist (input): This is the distance from the I-End of the frame object to the load
            location. This may be a relative distance (0 <= Dist <= 1) or an actual
            distance, depending on the value of the RelDist item. [L] when RelDist is False
        Val (input): This is the value of the point load. [F] when MyType is 1 and [FL] when
            MyType is 2
        CSys (input): This is Local or the name of a defined coordinate system. It is the
            coordinate system in which the loads are specified.
        RelDist (input): If this item is True, the specified Dist item is a relative
            distance, otherwise it is an actual distance.
        Replace (input): If this item is True, all previous loads, if any, assigned to the
            specified frame object(s), in the specified load pattern, are deleted before
            making the new assignment.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadPoint(Name, LoadPat, MyType, Dir, Dist, Val, CSys, RelDist, Replace, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetLoadPoint falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadStrain(self, Name: str, LoadPat: str, DOF: int, Val: float, Replace: bool = True, PatternName: str = '', ItemType: int = 0):
        """This function assigns strain loads to frame objects. The function returns zero if the loads
        are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        DOF (input): This is 1, 2, 3, 4, 5 or 6, indicating the degree of freedom to which
            the strain load is applied. 1 = Strain11 2 = Strain12 3 = Strain13 4 =
            Curvature1 5 = Curvature2 6 = Curvature3
        Val (input): This is the strain load value. [L/L] for DOF = 1, 2 and 3 and [1/L] for
            DOF = 4, 5 and 6
        Replace (input): If this item is True, all previous strain loads, if any, assigned
            to the specified frame object(s), in the specified load pattern, for the
            specified degree of freedom, are deleted before making the new assignment.
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the strain load for the frame object is uniform along the object at the
            value specified by Val. If PatternName is the name of a defined joint pattern,
            the strain load for the frame object is based on the specified strain value
            multiplied by the pattern value at the joints at each end of the frame object.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadStrain(Name, LoadPat, DOF, Val, Replace, PatternName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetLoadStrain falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadTargetForce(self, Name: str, LoadPat: str, DOF: list[bool], f: list[float], RD: list[float], ItemType: int = 0):
        """This function assigns target forces to frame objects. The function returns zero if the
        target forces are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        DOF (input): This is a array of boolean values indicating if the considered degree
            of freedom has a target force. DOF(1) = P DOF(2) = V2 DOF(3) = V3 DOF(4) = T
            DOF(5) = M2 DOF(6) = M3
        f (input): This is a array of target force values. The target forces specified for a
            given degree of freedom are applied only if the corresponding DOF item for that
            degree of freedom is True. f(1) = P [F] f(2) = V2 [F] f(3) = V3 [F] f(4) = T
            [FL] f(5) = M2 [FL] f(6) = M3 [FL]
        RD (input): This is a array of relative distances along the frame objects where the
            target force values apply. The relative distances specified for a given degree
            of freedom are applicable only if the corresponding DOF item for that degree of
            freedom is True. The relative distance must be between 0 and 1, 0 <= RD <=1.
            RD(1) = relative location for P target force RD(2) = relative location for V2
            target force RD(3) = relative location for V3 target force RD(4) = relative
            location for T target force RD(5) = relative location for M2 target force RD(6)
            = relative location for M3 target force
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadTargetForce(Name, LoadPat, DOF, f, RD, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetLoadTargetForce falhou (ret={_r})".format(_r=_r))
        return None

    def SetLoadTemperature(self, Name: str, LoadPat: str, MyType: int, Val: float, PatternName: str = '', Replace: bool = True, ItemType: int = 0):
        """This function assigns temperature loads to frame objects. The function returns zero if the
        loads are successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        LoadPat (input): The name of a defined load pattern.
        MyType (input): This is 1, 2 or 3, indicating the type of temperature load. 1 =
            Temperature 2 = Temperature gradient along local 2 axis 3 = Temperature gradient
            along local 3 axis
        Val (input): This is the temperature change value. [T] for MyType = 1 and [T/L] for
            MyType = 2 and 3
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank the temperature load for the frame object is uniform along the object at
            the value specified by Val. If PatternName is the name of a defined joint
            pattern, the temperature load for the frame object is based on the specified
            temperature value multiplied by the pattern value at the joints at each end of
            the frame object.
        Replace (input): If this item is True, all previous temperature loads, if any,
            assigned to the specified frame object(s), in the specified load case, are
            deleted before making the new assignment.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLoadTemperature(Name, LoadPat, MyType, Val, PatternName, Replace, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetLoadTemperature falhou (ret={_r})".format(_r=_r))
        return None

    def SetLocalAxesAdvanced(self, Name: str, Active: bool, Plane2: int, PlVectOpt: int, PlCSys: str, PlDir: list[int], PlPt: list[str], PlVect: list[float], ItemType: int = 0):
        """This function assigns advanced local axes to frame objects. The function returns zero if the
        advanced local axes assignments are assigned successfully; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Active (input): This is True if advanced local axes exist.
        Plane2 (input): This is 12 or 13, indicating that the local plane determined by the
            plane reference vector is the 1-2 plane or the 1-3 plane. This item applies only
            when the Active item is True.
        PlVectOpt (input): This is 1, 2, or 3, indicating the plane reference vector option.
            This item applies only when the Active item is True. 1 = Coordinate direction 2
            = Two joints 3 = User vector
        PlCSys (input): The coordinate system used to define the plane reference vector
            coordinate directions and the plane user vector. This item applies when the
            Active item is True and the PlVectOpt item is 1 or 3.
        PlDir (input): This is an array dimensioned to 1 (2 integers), indicating the plane
            reference vector primary and secondary coordinate directions, PlDir(0) and
            PlDir(1) respectively, taken at the object center in the specified coordinate
            system and used to determine the plane reference vector. This item applies when
            the Active item is True and the PlVectOpt item is 1. Possible coordinate
            direction values are: 1 = +X -1 = -X 2 = +Y -2 = -Y 3 = +Z -3 = -Z 4 = +CR -4 =
            -CR 5 = +CA -5 = -CA 6 = +CZ -6 = -CZ 7 = +SR -7 = -SR 8 = +SA -8 = -SA 9 = +SB
            -9 = -SB
        PlPt (input): This is an array dimensioned to 1 (2 strings), indicating the labels
            of two joints that define the plane reference vector. Either of these joints may
            be specified as None to indicate the center of the specified object. If both
            joints are specified as None, they are not used to define the plane reference
            vector. This item applies when the Active item is True and the PlVectOpt item is
            2.
        PlVect (input): This is an array dimensioned to 2 (3 doubles) that defines the plane
            reference vector. This item applies when the Active item is True and the
            PlVectOpt item is 3.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 Selection = 2 If this item is Object, the assignment is
            made to the frame object specified by the Name item. If this item is Group, the
            assignment is made to all frame objects in the group specified by the Name item.
            If this item is Selection, assignment is made to all selected frame objects and
            the Name item is ignored.
        """
        _r = self._raw.SetLocalAxesAdvanced(Name, Active, Plane2, PlVectOpt, PlCSys, PlDir, PlPt, PlVect, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetLocalAxesAdvanced falhou (ret={_r})".format(_r=_r))
        return None

    def SetLocalAxes(self, Name: str, Ang: float, ItemType: int = 0):
        """This function assigns a local axis angle to frame objects. The function returns zero if the
        local axis angle is successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Ang (input): This is the angle that the local 2 and 3 axes are rotated about the
            positive local 1 axis, from the default orientation or, if the Advanced item is
            True, from the orientation determined by the plane reference vector. The
            rotation for a positive angle appears counter clockwise when the local +1 axis
            is pointing toward you. [deg]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetLocalAxes(Name, Ang, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetLocalAxes falhou (ret={_r})".format(_r=_r))
        return None

    def SetMass(self, Name: str, MassOverL: float, Replace: bool = False, ItemType: int = 0):
        """This function assigns mass per unit length to frame objects. The function returns zero if
        the mass is successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        MassOverL (input): The mass per unit length assigned to the frame object. [M/L]
        Replace (input): If this item is True, all existing mass assignments to the frame
            object are removed before assigning the specified mas. If it is False, the
            specified mass is added to any existing mass already assigned to the frame
            object.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetMass(Name, MassOverL, Replace, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetMass falhou (ret={_r})".format(_r=_r))
        return None

    def SetMatTemp(self, Name: str, Temp: float, PatternName: str = '', ItemType: int = 0):
        """This function assigns material temperatures to frame objects. The function returns zero if
        the material temperatures are successfully assigned, otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Temp (input): This is the material temperature value assigned to the frame object.
            [T]
        PatternName (input): This is blank or the name of a defined joint pattern. If it is
            blank, the material temperature for the frame object is uniform along the object
            at the value specified by Temp. If PatternName is the name of a defined joint
            pattern, the material temperature for the frame object may vary from one end to
            the other. The material temperature at each end of the object is equal to the
            specified temperature multiplied by the pattern value at the joint at the end of
            the frame object.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetMatTemp(Name, Temp, PatternName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetMatTemp falhou (ret={_r})".format(_r=_r))
        return None

    def SetMaterialOverwrite(self, Name: str, PropName: str, ItemType: int = 0):
        """This function sets the material overwrite assignment for frame objects. The function returns
        zero if the material overwrite assignment is successfully assigned, otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        PropName (input): This is None or a blank string, indicating that any existing
            material overwrites assigned to the specified frame objects are to be removed,
            or it is the name of an existing material property.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetMaterialOverwrite(Name, PropName, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetMaterialOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetModifiers(self, Name: str, Value: list[float], ItemType: int = 0):
        """This function sets the frame modifier assignment for frame objects. The default value for
        all modifiers is one. The function returns zero if the modifier assignments are
        successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Value (input): This is an array of eight unitless modifiers. Value(0) = Cross
            sectional area modifier Value(1) = Shear area in local 2 direction modifier
            Value(2) = Shear area in local 3 direction modifier Value(3) = Torsional
            constant modifier Value(4) = Moment of inertia about local 2 axis modifier
            Value(5) = Moment of inertia about local 3 axis modifier Value(6) = Mass
            modifier Value(7) = Weight modifier
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetModifiers(Name, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetModifiers falhou (ret={_r})".format(_r=_r))
        return None

    def SetOutputStations(self, Name: str, MyType: int, MaxSegSize: float, MinSections: int, NoOutPutAndDesignAtElementEnds: bool = False, NoOutPutAndDesignAtPointLoads: bool = False, ItemType: int = 0):
        """This function assigns frame object output station data. The function returns zero if the
        data is successfully assigned, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        MyType (input): This is 1 or 2, indicating how the output stations are specified. 1
            = maximum segment size, that is, maximum station spacing 2 = minimum number of
            stations
        MaxSegSize (input): The maximum segment size, that is, the maximum station spacing.
            This item applies only when MyType = 1. [L]
        MinSections (input): The minimum number of stations. This item applies only when
            MyType = 2.
        NoOutPutAndDesignAtElementEnds (input): If this item is True, no additional output
            stations are added at the ends of line elements when the frame object is
            internally meshed.
        NoOutPutAndDesignAtPointLoads (input): If this item is True, no additional output
            stations are added at point load locations.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetOutputStations(Name, MyType, MaxSegSize, MinSections, NoOutPutAndDesignAtElementEnds, NoOutPutAndDesignAtPointLoads, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetOutputStations falhou (ret={_r})".format(_r=_r))
        return None

    def SetPDeltaForce(self, Name: str, PDeltaForce: float, Dir: int, Replace: bool, CSys: str = 'Global', ItemType: int = 0):
        """This function assigns P-Delta forces to straight frame objects. P-Delta force assignments do
        not apply to curved frames. The function returns zero if the assignments are
        successfully applied, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        PDeltaForce (input): The P-Delta force assigned to the frame object. [F]
        Dir (input): This is 0, 1, 2 or 3, indicating the direction of the P-Delta force
            assignment. 0 = Frame object local 1-axis direction 1 = Projected X direction in
            CSys coordinate system 2 = Projected Y direction in CSys coordinate system 3 =
            Projected Z direction in CSys coordinate system
        Replace (input): If this item is True, all existing P-Delta force assignments to the
            frame object are removed before assigning the specified P-Delta force. If it is
            False, the specified P-Delta force is added to any existing P-Delta forces
            already assigned to the frame object.
        CSys (input): This is the name of the coordinate system in which the projected X, Y
            or Z direction P-Delta forces are defined. This item does not apply if the Dir
            item is zero (frame object local 1-axis direction).
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetPDeltaForce(Name, PDeltaForce, Dir, Replace, CSys, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetPDeltaForce falhou (ret={_r})".format(_r=_r))
        return None

    def SetReleases(self, Name: str, ii: list[bool], jj: list[bool], StartValue: list[float], EndValue: list[float], ItemType: int = 0):
        """This function makes end release and partial fixity assignments to frame objects. The
        function returns zero if the assignments are successfully retrieved, otherwise it
        returns a nonzero value. Partial fixity assignments are made to degrees of freedom
        that have been released only. Some release assignments would cause instability in
        the model. An error is returned if this type of assignment is made. Unstable release
        assignments include the following: U1 released at both ends U2 released at both ends
        U3 released at both ends R1 released at both ends R2 released at both ends and U3 at
        either end R3 released at both ends and U2 at either end
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetReleases(Name, ii, jj, StartValue, EndValue, ItemType)
        if _r[4] != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetReleases falhou (ret={_r})".format(_r=_r))
        return None

    def SetSection(self, name: str, PropName: str, ItemType: int = 0, sVarRelStartLoc: float = 0, sVarTotalLength: float = 0):
        """This function assigns a frame section property to a frame object. The function returns zero
        if the frame section property data is successfully assigned, otherwise it returns a
        nonzero value.
    
        PropName (input): This is None or the name of a frame section property to be
            assigned to the specified frame object(s).
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        sVarRelStartLoc (input): This is the relative distance along the nonprismatic
            section to the I-End (start) of the frame object. This item is ignored when the
            sVarTotalLengthitem is 0. This item is applicable only when the assigned frame
            section property is a nonprismatic section, and the sVarTotalLengthitem is
            greater than zero.
        sVarTotalLength (input): This is the total assumed length of the nonprismatic
            section. Enter 0 for this item to indicate that the section length is the same
            as the frame object length. This item is applicable only when the assigned frame
            section property is a nonprismatic section.
        """
        _r = self._raw.SetSection(name, PropName, ItemType, sVarRelStartLoc, sVarTotalLength)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetSection falhou (ret={_r})".format(_r=_r))
        return None

    def SetSelected(self, Name: str, Selected: bool, ItemType: int = 0):
        """This function sets the selected status for a frame object. The function returns zero if the
        selected status is successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Selected (input): This item is True if the specified frame object is selected,
            otherwise it is False.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the selected
            status is set for the frame object specified by the Name item. If this item is
            Group, the selected status is set for all frame objects in the group specified
            by the Name item. If this item is SelectedObjects, the selected status is set
            for all selected frame objects, and the Name item is ignored.
        """
        _r = self._raw.SetSelected(Name, Selected, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetSelected falhou (ret={_r})".format(_r=_r))
        return None

    def SetSpring(self, Name: str, MyType: int, s: float, SimpleSpringType: int, LinkProp: str, SpringLocalOneType: int, Dir: int, Plane23Angle: float, Vec: list[float], Ang: float, Replace: bool, CSys: str = 'Local', ItemType: int = 0):
        """This function makes spring assignments to frame objects. The function returns zero if the
        assignments are successfully applied, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        MyType (input): This is 1 or 2, indicating the spring property type. 1 = Simple
            spring 2 = Link property
        s (input): The simple spring stiffness per unit length of the frame object. This
            item applies only when MyType = 1. [F/L 2 ]
        SimpleSpringType (input): This is 1, 2 or 3, indicating the simple spring type. This
            item applies only when MyType = 1. 1 = Spring resists tension and compression 2
            = Spring resists compression only 3 = Spring resists tension only
        LinkProp (input): The name of the link property assigned to the spring. This item
            applies only when MyType = 2.
        SpringLocalOneType (input): This is 1, 2 or 3, indicating the method used to specify
            the spring positive local 1-axis orientation. 1 = Parallel to frame object local
            axis 2 = In the frame object 2-3 plane 3 = User specified direction vector
        Dir (input): This is 1, 2, 3, -1, -2 or -3, indicating the frame object local axis
            that corresponds to the positive local 1-axis of the spring. This item applies
            only when SpringLocalOneType = 1.
        Plane23Angle (input): This is the angle in the frame object 2-3 plane measured
            counter clockwise from the frame positive 2-axis to the spring positive 1-axis.
            This item applies only when SpringLocalOneType = 2. [deg]
        Vec (input): This is an array of three values that define the direction vector of
            the spring positive local 1-axis. The direction vector is in the coordinate
            system specified by the CSys item. This item applies only when
            SpringLocalOneType = 3.
        Ang (input): This is the angle that the link local 2-axis is rotated from its
            default orientation. This item applies only when MyType = 2. [deg]
        Replace (input): If this item is True, all existing spring assignments to the frame
            object are removed before assigning the specified spring. If it is False, the
            specified spring is added to any existing springs already assigned to the frame
            object.
        CSys (input): This is Local (meaning the frame object local coordinate system) or
            the name of a defined coordinate system. This item is the coordinate system in
            which the user specified direction vector, Vec, is specified. This item applies
            only when SpringLocalOneType = 3.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetSpring(Name, MyType, s, SimpleSpringType, LinkProp, SpringLocalOneType, Dir, Plane23Angle, Vec, Ang, Replace, CSys, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetSpring falhou (ret={_r})".format(_r=_r))
        return None

    def SetStraight(self, Name: str):
        """This function sets a curved frame object straight. The function returns zero if the frame
        object type is successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of a defined curved frame object.
        """
        _r = self._raw.SetStraight(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetStraight falhou (ret={_r})".format(_r=_r))
        return None

    def SetTCLimits(self, Name: str, LimitCompressionExists: bool, LimitCompression: float, LimitTensionExists: bool, LimitTension: float, ItemType: int = 0):
        """This function makes tension/compression force limit assignments to frame objects. The
        function returns zero if the assignments are successfully applied, otherwise it
        returns a nonzero value. Note that the tension and compression limits are only used
        in nonlinear analyses.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        LimitCompressionExists (input): This item is True if a compression force limit
            exists for the frame object.
        LimitCompression (input): The compression force limit for the frame object. [F]
        LimitTensionExists (input): This item is True if a tension force limit exists for
            the frame object.
        LimitTension (input): The tension force limit for the frame object. [F]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetTCLimits(Name, LimitCompressionExists, LimitCompression, LimitTensionExists, LimitTension, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.FrameObj.SetTCLimits falhou (ret={_r})".format(_r=_r))
        return None


