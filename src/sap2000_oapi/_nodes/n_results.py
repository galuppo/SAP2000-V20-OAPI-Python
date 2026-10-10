"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_Results:
    """Wrapper para SapModel.Results."""

    def __init__(self, raw):
        self._raw = raw

    def AreaForceShell(self, name: str, ItemTypeElm: int):
        """This function reports the area forces for the specified area elements that are assigned
        shell section properties (not plane or asolid properties). Note that the forces
        reported are per unit of in-plane length. The function returns zero if the forces
        are successfully recovered, otherwise it returns a nonzero value. See Analysis
        Results Remarks for more information.
    
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the area elements corresponding to
            the area object specified by the Name item. If this item is Element, the result
            request is for the area element specified by the Name item. If this item is
            GroupElm, the result request is for the area elements corresponding to all area
            objects included in the group specified by the Name item. If this item is
            SelectionElm, the result request is for area elements corresponding to all
            selected area objects, and the Name item is ignored.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the area object name associated with
            each result, if any.
        Elm (output): This is an array that includes the area element name associated with
            each result.
        PointElm (output): This is an array that includes the name of the point element
            where the results are reported.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        F11 (output): The area element internal F11 membrane direct force per length
            reported in the area element local coordinate system. [F/L]
        F22 (output): The area element internal F22 membrane direct force per length
            reported in the area element local coordinate system. [F/L]
        F12 (output): The area element internal F12 membrane shear force per length reported
            in the area element local coordinate system. [F/L]
        FMax (output): The maximum principal membrane force per length. [F/L]
        FMin (output): The minimum principal membrane force per length. [F/L]
        FAngle (output): The angle measured counter clockwise (when the local 3 axis is
            pointing toward you) from the area local 1 axis to the direction of the maximum
            principal membrane force. [deg]
        FVM (output): The area element internal Von Mises membrane force per length. [F/L]
        M11 (output): The area element internal M11 plate bending moment per length reported
            in the area element local coordinate system. This item is only reported for area
            elements with properties that allow plate bending behavior. [FL/L]
        M22 (output): The area element internal M22 plate bending moment per length reported
            in the area element local coordinate system. This item is only reported for area
            elements with properties that allow plate bending behavior. [FL/L]
        M12 (output): The area element internal M12 plate twisting moment per length
            reported in the area element local coordinate system. This item is only reported
            for area elements with properties that allow plate bending behavior. [FL/L]
        MMax (output): The maximum principal plate moment per length. This item is only
            reported for area elements with properties that allow plate bending behavior.
            [FL/L]
        MMin (output): The minimum principal plate moment per length. This item is only
            reported for area elements with properties that allow plate bending behavior.
            [FL/L]
        MAngle (output): The angle measured counter clockwise (when the local 3 axis is
            pointing toward you) from the area local 1 axis to the direction of the maximum
            principal plate moment. This item is only reported for area elements with
            properties that allow plate bending behavior. [deg]
        V13 (output): The area element internal V13 plate transverse shear force per length
            reported in the area element local coordinate system. This item is only reported
            for area elements with properties that allow plate bending behavior. [F/L]
        V23 (output): The area element internal V23 plate transverse shear force per length
            reported in the area element local coordinate system. This item is only reported
            for area elements with properties that allow plate bending behavior. [F/L]
        VMax (output): The maximum plate transverse shear force. It is equal to the square
            root of the sum of the squares of V13 and V23. This item is only reported for
            area elements with properties that allow plate bending behavior. [F/L]
        VAngle (output): The angle measured counter clockwise (when the local 3 axis is
            pointing toward you) from the area local 1 axis to the direction of Vmax. This
            item is only reported for area elements with properties that allow plate bending
            behavior. [deg]
        """
        _r = self._raw.AreaForceShell(name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.AreaForceShell falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def AreaJointForcePlane(self, Name: str, ItemTypeElm: int):
        """This function reports the area joint forces for the point elements at each corner of the
        specified plane elements that have plane-type or asolid-type properties (not shell).
        The function returns zero if the forces are successfully recovered, otherwise it
        returns a nonzero value. See Analysis Results Remarks for more information.
    
        Name (input): The name of an existing area object, area element or group of objects
            depending on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the plane elements corresponding to
            the area object specified by the Name item. If this item is Element, the result
            request is for the plane element specified by the Name item. If this item is
            GroupElm, the result request is for the plane elements corresponding to all area
            objects included in the group specified by the Name item. If this item is
            SelectionElm, the result request is for plane elements corresponding to all
            selected area objects and the Name item is ignored.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the area object name associated with
            each result, if any.
        Elm (output): This is an array that includes the plane element name associated with
            each result.
        PointElm (output): This is an array that includes the point element name associated
            with each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.AreaJointForcePlane(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.AreaJointForcePlane falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def AreaJointForceShell(self, Name: str, ItemTypeElm: int):
        """This function reports the area joint forces for the point elements at each corner of the
        specified area elements that have shell-type properties (not plane or asolid). The
        function returns zero if the forces are successfully recovered, otherwise it returns
        a nonzero value. See Analysis Results Remarks for more information.
    
        Name (input): The name of an existing area object, area element or group of objects,
            depending on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the area elements corresponding to
            the area object specified by the Name item. If this item is Element, the result
            request is for the area element specified by the Name item. If this item is
            GroupElm, the result request is for the area elements corresponding to all area
            objects included in the group specified by the Name item. If this item is
            SelectionElm, the result request is for area elements corresponding to all
            selected area objects and the Name item is ignored.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the area object name associated with
            each result, if any.
        Elm (output): This is an array that includes the area element name associated with
            each result.
        PointElm (output): This is an array that includes the point element name associated
            with each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.AreaJointForceShell(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.AreaJointForceShell falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def AreaStrainShell(self, name: str, ItemTypeElm: int):
        """This function reports the area strains for the specified area elements that are assigned
        shell section properties (not plane or asolid properties). Strains are reported at
        each point element associated with the area element. The function returns zero if
        the strains are successfully recovered, otherwise it returns a nonzero value. See
        Analysis Results Remarks for more information.
    
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the area elements corresponding to
            the area object specified by the Name item. If this item is Element, the result
            request is for the area element specified by the Name item. If this item is
            GroupElm, the result request is for the area elements corresponding to all area
            objects included in the group specified by the Name item. If this item is
            SelectionElm, the result request is for area elements corresponding to all
            selected area objects and the Name item is ignored.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the area object name associated with
            each result, if any.
        Elm (output): This is an array that includes the area element name associated with
            each result.
        PointElm (output): This is an array that includes the name of the point element
            where the results are reported.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        GMaxAvg (output): The area element maximum average out-of-plane shear strain. It is
            equal to the square root of the sum of the squares of G13Avg and G23Avg. This
            item is only reported for area elements with properties that allow plate bending
            behavior.
        GAngleAvg (output): The angle measured counter clockwise (when the local 3 axis is
            pointing toward you) from the area local 1 axis to the direction of GMaxAvg.
            This item is only reported for area elements with properties that allow plate
            bending behavior. [deg]
        """
        _r = self._raw.AreaStrainShell(name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.AreaStrainShell falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def AreaStrainShellLayered(self, name: str, ItemTypeElm: int):
        """This function reports the area strains for the specified area elements that are assigned
        layered shell section properties. The function returns zero if the strains are
        successfully recovered, otherwise it returns a nonzero value. See Analysis Results
        Remarks for more information.
    
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the area elements corresponding to
            the area object specified by the Name item. If this item is Element, the result
            request is for the area element specified by the Name item. If this item is
            GroupElm, the result request is for the area elements corresponding to all area
            objects included in the group specified by the Name item. If this item is
            SelectionElm, the result request is for area elements corresponding to all
            selected area objects and the Name item is ignored.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the area object name associated with
            each result, if any.
        Elm (output): This is an array that includes the area element name associated with
            each result.
        Layer (output): This is an array that includes the layer name associated with each
            result.
        IntPtNum (output): This is an array that includes the integration point number
            within the specified layer of the area element.
        IntPtLoc (output): This is an array that includes the integration point relative
            location within the specified layer of the area element. The location is between
            -1 (bottom of layer) and +1 (top of layer), inclusive. The midheight of the
            layer is at a value of 0.
        PointElm (output): This is an array that includes the name of the point element
            where the results are reported.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        EAngle (output): The angle measured counter clockwise (when the local 3 axis is
            pointing toward you) from the area local 1 axis to the direction of the maximum
            principal strain. [deg]
        EVM (output): The area element internal Von Mises strain at the specified point
            element location, for the specified layer and layer integration point.
        GMaxAvg (output): The area element maximum average out-of-plane shear strain for the
            specified layer and layer integration point. It is equal to the square root of
            the sum of the squares of G13Avg and G23Avg.
        GAngleAvg (output): The angle measured counter clockwise (when the local 3 axis is
            pointing toward you) from the area local 1 axis to the direction of GMaxAvg.
            [deg]
        """
        _r = self._raw.AreaStrainShellLayered(name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.AreaStrainShellLayered falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def AreaStressPlane(self, name: str, ItemTypeElm: int):
        """This function reports the stresses for the specified plane elements that are assigned plane
        or asolid section properties (not shell properties). The function returns zero if
        the stresses are successfully recovered, otherwise it returns a nonzero value. See
        Analysis Results Remarks for more information.
    
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the plane elements corresponding to
            the area object specified by the Name item. If this item is Element, the result
            request is for the plane element specified by the Name item. If this item is
            GroupElm, the result request is for the plane elements corresponding to all area
            objects included in the group specified by the Name item. If this item is
            SelectionElm, the result request is for plane elements corresponding to all
            selected area objects, and the Name item is ignored.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the area object name associated with
            each result, if any.
        Elm (output): This is an array that includes the plane element name associated with
            each result.
        PointElm (output): This is an array that includes the name of the point element
            where the results are reported.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        SAngle (output): The angle measured counter clockwise (when the local 3 axis is
            pointing toward you) from the plane element local 1 axis to the direction of the
            maximum principal stress. [deg]
        SVM (output): The plane element internal Von Mises stress at the specified point
            element. [F/L 2 ]
        """
        _r = self._raw.AreaStressPlane(name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.AreaStressPlane falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def AreaStressShell(self, name: str, ItemTypeElm: int):
        """This function reports the area stresses for the specified area elements that are assigned
        shell section properties (not plane or asolid properties). Stresses are reported at
        each point element associated with the area element. The function returns zero if
        the stresses are successfully recovered, otherwise it returns a nonzero value. See
        Analysis Results Remarks for more information.
    
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the area elements corresponding to
            the area object specified by the Name item. If this item is Element, the result
            request is for the area element specified by the Name item. If this item is
            GroupElm, the result request is for the area elements corresponding to all area
            objects included in the group specified by the Name item. If this item is
            SelectionElm, the result request is for area elements corresponding to all
            selected area objects and the Name item is ignored.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the area object name associated with
            each result, if any.
        Elm (output): This is an array that includes the area element name associated with
            each result.
        PointElm (output): This is an array that includes the name of the point element
            where the results are reported.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        SMaxAvg (output): The area element maximum average out-of-plane shear stress. It is
            equal to the square root of the sum of the squares of S13Avg and S23Avg. This
            item is only reported for area elements with properties that allow plate bending
            behavior. [F/L 2 ]
        SAngleAvg (output): The angle measured counter clockwise (when the local 3 axis is
            pointing toward you) from the area local 1 axis to the direction of SMaxAvg.
            This item is only reported for area elements with properties that allow plate
            bending behavior. [deg]
        """
        _r = self._raw.AreaStressShell(name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.AreaStressShell falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def AreaStressShellLayered(self, name: str, ItemTypeElm: int):
        """This function reports the area stresses for the specified area elements that are assigned
        layered shell section properties. The function returns zero if the stresses are
        successfully recovered, otherwise it returns a nonzero value. See Analysis Results
        Remarks for more information.
    
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the area elements corresponding to
            the area object specified by the Name item. If this item is Element, the result
            request is for the area element specified by the Name item. If this item is
            GroupElm, the result request is for the area elements corresponding to all area
            objects included in the group specified by the Name item. If this item is
            SelectionElm, the result request is for area elements corresponding to all
            selected area objects and the Name item is ignored.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the area object name associated with
            each result, if any.
        Elm (output): This is an array that includes the area element name associated with
            each result.
        Layer (output): This is an array that includes the layer name associated with each
            result.
        IntPtNum (output): This is an array that includes the integration point number
            within the specified layer of the area element.
        IntPtLoc (output): This is an array that includes the integration point relative
            location within the specified layer of the area element. The location is between
            -1 (bottom of layer) and +1 (top of layer), inclusive. The midheight of the
            layer is at a value of 0.
        PointElm (output): This is an array that includes the name of the point element
            where the results are reported.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        SAngle (output): The angle measured counter clockwise (when the local 3 axis is
            pointing toward you) from the area local 1 axis to the direction of the maximum
            principal stress. [deg]
        SVM (output): The area element internal Von Mises stress at the specified point
            element location, for the specified layer and layer integration point. [F/L 2 ]
        SMaxAvg (output): The area element maximum average out-of-plane shear stress for the
            specified layer and layer integration point. It is equal to the square root of
            the sum of the squares of S13Avg and S23Avg. [F/L 2 ]
        SAngleAvg (output): The angle measured counter clockwise (when the local 3 axis is
            pointing toward you) from the area local 1 axis to the direction of SMaxAvg.
            [deg]
        """
        _r = self._raw.AreaStressShellLayered(name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.AreaStressShellLayered falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def AssembledJointMass_1(self, MassSourceName: str, Name: str, ItemTypeElm: int):
        """This function reports the assembled joint masses for the specified point elements. The
        function returns zero if the masses are successfully recovered, otherwise it returns
        a nonzero value. See Analysis Results Remarks for more information.
    
        Name (input): The name of an existing point element or group of objects, depending
            on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the point element corresponding to
            the point object specified by the Name item. If this item is Element, the result
            request is for the point element specified by the Name item. If this item is
            GroupElm, the result request is for all point elements directly or indirectly
            specified in the group specified by the Name item. If this item is SelectionElm,
            the result request is for all point elements directly or indirectly selected and
            the Name item is ignored. See Type for Elements for more information.
        PointElm (output): This is an array that includes the point element name associated
            with each result.
        """
        _r = self._raw.AssembledJointMass_1(MassSourceName, Name, ItemTypeElm, [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.AssembledJointMass_1 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def BaseReact(self):
        """This function reports the structure total base reactions. The function returns zero if the
        reactions are successfully recovered, otherwise it returns a nonzero value. See
        Analysis Results Remarks for additional information.
    
        NumberResults (output): The total number of results returned by the program.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.BaseReact(0, [], [], [], [], [], [], [], [], [], 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.BaseReact falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def BaseReactWithCentroid(self):
        """This function reports the structure total base reactions and includes information on the
        centroid of the translational reaction forces. The function returns zero if the
        reactions are successfully recovered, otherwise it returns a nonzero value. See
        Analysis Results Remarks for more information. Note that the reported base reaction
        centroids are not the same as the centroid of the applied loads. See Base Reaction
        Centroids for additional information.
    
        NumberResults (output): The total number of results returned by the program.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.BaseReactWithCentroid(0, [], [], [], [], [], [], [], [], [], 0.0, 0.0, 0.0, [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.BaseReactWithCentroid falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def BridgeSuperCutLongitStress(self, Name: str, CutIndex: int, PointIndex: int):
        """This function returns the longitudinal stresses for multiple cases/combos at a single stress
        point in a superstructure section cut in a bridge object. Use the functions in
        SapModel.Results.Setup to control the loads and steps for which results are to be
        obtained. The function returns zero if the information is successfully retrieved,
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing bridge object.
        CutIndex (input): The index number of section cut in this bridge object. This must
            be from 0 to Count-1, where Count is the value returned by function
            SapModel.BridgeObj.CountSuperCut.
        PointIndex (input): The index number of the stress point in this section cut in this
            bridge object. This must be from 0 to Count-1, where Count is the value returned
            by function SapModel.BridgeObj.CountSuperCutStressPoint.
        NumberResults (output): The total number of results returned.
        LoadCase (output): This is an array that includes the name of the load case or load
            combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        Stress (output): This is an array that includes the longitudinal stress value for
            each result. [F/L 2 ]
        """
        _r = self._raw.BridgeSuperCutLongitStress(Name, CutIndex, PointIndex, 0, [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.BridgeSuperCutLongitStress falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def BucklingFactor(self):
        """This function reports buckling factors obtained from buckling load cases. The function
        returns zero if the factors are successfully recovered, otherwise it returns a
        nonzero value. See Analysis Results Remarks for more information.
    
        NumberResults (output): The total number of results returned by the program.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type for each result. For
            buckling factors, the step type is always Mode.
        Factor (output): This is an array that includes the buckling factors.
        """
        _r = self._raw.BucklingFactor(0, [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.BucklingFactor falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def FrameForce(self, Name: str, ItemTypeElm: int):
        """This function reports the frame forces for the specified line elements. The function returns
        zero if the forces are successfully recovered, otherwise it returns a nonzero value.
        See Analysis Results Remarks for additional information.
    
        Name (input): The name of an existing line object, line element or group of objects
            depending on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the line elements corresponding to
            the line object specified by the Name item. If this item is Element, the result
            request is for the line element specified by the Name item. If this item is
            GroupElm, the result request is for the line elements corresponding to all line
            objects included in the group specified by the Name item. If this item is
            SelectionElm, the result request is for line elements corresponding to all
            selected line objects and the Name item is ignored.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the line object name associated with
            each result, if any.
        ObjSta (output): This is an array that includes the distance measured from the I-end
            of the line object to the result location.
        Elm (output): This is an array that includes the line element name associated with
            each result.
        ElmSta (output): This is an array that includes the distance measured from the I-end
            of the line element to the result location.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.FrameForce(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.FrameForce falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def FrameJointForce(self, Name: str, ItemTypeElm: int):
        """This function reports the frame joint forces for the point elements at each end of the
        specified line elements. The function returns zero if the forces are successfully
        recovered, otherwise it returns a nonzero value. See Analysis Results Remarks for
        additional information.
    
        Name (input): The name of an existing line object, line element or group of objects
            depending on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the line elements corresponding to
            the line object specified by the Name item. If this item is Element, the result
            request is for the line element specified by the Name item. If this item is
            GroupElm, the result request is for the line elements corresponding to all line
            objects included in the group specified by the Name item. If this item is
            SelectionElm, the result request is for line elements corresponding to all
            selected line objects and the Name item is ignored.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the line object name associated with
            each result, if any.
        Elm (output): This is an array that includes the line element name associated with
            each result.
        PointElm (output): This is an array that includes the point element name associated
            with each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.FrameJointForce(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.FrameJointForce falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GeneralizedDispl(self, Name: str):
        """This function reports the displacement values for the specified generalized displacements.
        The function returns zero if the displacements are successfully recovered, otherwise
        it returns a nonzero value. See Analysis Results Remarks for more information.
    
        Name (input): The name of an existing generalized displacement for which results are
            returned. If the program does not recognize this name as a defined generalized
            displacement, it returns results for all selected generalized displacements, if
            any. For example, entering a blank string (i.e., "") for the name will prompt
            the program to return results for all selected generalized displacements.
        NumberResults (output): The total number of results returned by the program.
        GD (output): This is an array that includes the generalized displacement name
            associated with each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        DType (output): This is an array that includes the generalized displacement type for
            each result. It is either Translation or Rotation.
        Value (output): This is an array of the generalized displacement values for each
            result.[L] when DType is Translation , [rad] when DType is Rotation.
        """
        _r = self._raw.GeneralizedDispl(Name, 0, [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.GeneralizedDispl falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def JointAcc(self, Name: str, ItemTypeElm: int):
        """This function reports the joint accelerations for the specified point elements. The
        accelerations reported by this function are relative accelerations. The function
        returns zero if the accelerations are successfully recovered, otherwise it returns a
        nonzero value. See Analysis Results Remarks for additional information.
    
        Name (input): The name of an existing point object, point element, or group of
            objects, depending on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the point element corresponding to
            the point object specified by the Name item. If this item is Element, the result
            request is for the point element specified by the Name item. If this item is
            GroupElm, the result request is for all point elements directly or indirectly
            specified in the group specified by the Name item. If this item is SelectionElm,
            the result request is for all point elements directly or indirectly selected and
            the Name item is ignored. See Item Type for Elements for more information.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the point object name associated with
            each result, if any. Some results will have no point object associated with
            them. For those cases, this item will be blank.
        Elm (output): This is an array that includes the point element name associated with
            each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.JointAcc(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.JointAcc falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def JointAccAbs(self, Name: str, ItemTypeElm: int):
        """This function reports the joint absolute accelerations for the specified point elements.
        Absolute and relative accelerations are the same, except when reported for time
        history load cases subjected to acceleration loading. The function returns zero if
        the accelerations are successfully recovered, otherwise it returns a nonzero value.
        See Analysis Results Remarks for more information.
    
        Name (input): The name of an existing point object, point element, or group of
            objects depending on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the point element corresponding to
            the point object specified by the Name item. If this item is Element, the result
            request is for the point element specified by the Name item. If this item is
            GroupElm, the result request is for all point elements directly or indirectly
            specified in the group specified by the Name item. If this item is SelectionElm,
            the result request is for all point elements directly or indirectly selected and
            the Name item is ignored. See Item Type for Elements for more information.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the point object name associated with
            each result, if any. Some results will have no point object associated with
            them. For those cases, this item will be blank.
        Elm (output): This is an array that includes the point element name associated with
            each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.JointAccAbs(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.JointAccAbs falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def JointDispl(self, Name: str, ItemTypeElm: int):
        """This function reports the joint displacements for the specified point elements. The
        displacements reported by this function are relative displacements. The function
        returns zero if the displacements are successfully recovered, otherwise it returns a
        nonzero value. See Analysis Results Remarks for more information.
    
        Name (input): The name of an existing point object, point element, or group of
            objects depending on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the point element corresponding to
            the point object specified by the Name item. If this item is Element, the result
            request is for the point element specified by the Name item. If this item is
            GroupElm, the result request is for all point elements directly or indirectly
            specified in the group specified by the Name item. If this item is SelectionElm,
            the result request is for all point elements directly or indirectly selected and
            the Name item is ignored. See Item Type for Elements for more information.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the point object name associated with
            each result, if any. Some results will have no point object associated with
            them. For these cases this item will be blank.
        Elm (output): This is an array that includes the point element name associated with
            each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.JointDispl(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.JointDispl falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def JointDisplAbs(self, Name: str, ItemTypeElm: int):
        """This function reports the absolute joint displacements for the specified point elements.
        Absolute and relative displacements are the same except when reported for time
        history load cases subjected to acceleration loading. The function returns zero if
        the displacements are successfully recovered, otherwise it returns a nonzero value.
        See Analysis Results Remarks for more information.
    
        Name (input): The name of an existing point object, point element, or group of
            objects depending on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the point element corresponding to
            the point object specified by the Name item. If this item is Element, the result
            request is for the point element specified by the Name item. If this item is
            GroupElm, the result request is for all point elements directly or indirectly
            specified in the group specified by the Name item. If this item is SelectionElm,
            the result request is for all point elements directly or indirectly selected and
            the Name item is ignored. See Item Type for Elements for more information.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the point object name associated with
            each result, if any. Some results will have no point object associated with
            them. For those cases, this item will be blank.
        Elm (output): This is an array that includes the point element name associated with
            each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.JointDisplAbs(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.JointDisplAbs falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def JointReact(self, Name: str, ItemTypeElm: int):
        """This function reports the joint reactions for the specified point elements. The reactions
        reported are from restraints, springs and grounded (one-joint) links. The function
        returns zero if the reactions are successfully recovered, otherwise it returns a
        nonzero value. See Analysis Results Remarks for more information.
    
        Name (input): The name of an existing point object, point element, or group of
            objects depending on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElmc = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the point element corresponding to
            the point object specified by the Name item. If this item is Element, the result
            request is for the point element specified by the Name item. If this item is
            GroupElm, the result request is for all point elements directly or indirectly
            specified in the group specified by the Name item. If this item is SelectionElm,
            the result request is for all point elements directly or indirectly selected and
            the Name item is ignored. See Item Type for Elements for more information.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the point object name associated with
            each result, if any. Some results will have no point object associated with
            them. For those cases, this item will be blank.
        Elm (output): This is an array that includes the point element name associated with
            each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.JointReact(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.JointReact falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def JointRespSpec(self, Name: str, ItemTypeElm: int, edSet: str):
        """This function reports the joint response spectra values, due to a time history analysis, for
        the specified point elements. The function returns zero if the response spectra data
        is successfully recovered, otherwise it returns a nonzero value. See Analysis
        Results Remarks for more information
    
        Name (input): The name of an existing point object, point element, or group of
            objects depending on the value of the ItemTypeElm item.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the point object name associated with
            each result, if any. Some results will have no point object associated with
            them. For those cases, this item will be blank.
        Elm (output): This is an array that includes the point element name associated with
            each result.
        LoadCase (output): This is an array that includes the name of the load case
            associated with each result.
        CoordSys (output): This is an array that includes the coordinate system in which the
            results are reported.
        Dir (output): This is an array that includes the direction for which the results are
            reported. Valid values for the direction are: 1 = Local 1, Global X, or user-
            defined coordinate system X 2 = Local 2, Global Y, or user-defined coordinate
            system Y 3 = Local 3, Global Z, or user-defined coordinate system Z
        Damping (output): This is an array that includes the critical damping ratio, for
            each result.
        SpecWidening (output): This is an array that includes the percent spectrum widening,
            for each result.
        AbscissaValue (output): This is an array that includes the period or frequency, as
            defined in each named set, for each result. [s or 1/s]
        OrdinateValue (output): This is an array of the response quantity, as defined in
            each named set, for each result. The possible response quantities are spectral
            displacement [L], spectral velocity [L/s], pseudo spectral velocity [L/s],
            spectral acceleration [L/s 2 ], or pseudo spectral acceleration [L/s 2 ].
        """
        _r = self._raw.JointRespSpec(Name, ItemTypeElm, edSet, 0, [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.JointRespSpec falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def JointVel(self, Name: str, ItemTypeElm: int):
        """This function reports the joint velocities for the specified point elements. The velocities
        reported by this function are relative velocities. The function returns zero if the
        velocities are successfully recovered, otherwise it returns a nonzero value. See
        Analysis Results Remarks for more information.
    
        Name (input): The name of an existing point object, point element, or group of
            objects depending on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the point element corresponding to
            the point object specified by the Name item. If this item is Element, the result
            request is for the point element specified by the Name item. If this item is
            GroupElm, the result request is for all point elements directly or indirectly
            specified in the group specified by the Name item. If this item is SelectionElm,
            the result request is for all point elements directly or indirectly selected and
            the Name item is ignored. See Item Type for Elements for more information.
        NumberResults (output): The number total of results returned by the program.
        Obj (output): This is an array that includes the point object name associated with
            each result, if any. Some results will have no point object associated with
            them. For those cases, this item will be blank.
        Elm (output): This is an array that includes the point element name associated with
            each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.JointVel(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.JointVel falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def JointVelAbs(self, Name: str, ItemTypeElm: int):
        """This function reports the joint absolute velocities for the specified point elements.
        Absolute and relative velocities are the same, except when reported for time history
        load cases subjected to acceleration loading. The function returns zero if the
        velocities are successfully recovered, otherwise it returns a nonzero value. See
        Analysis Results Remarks for more information.
    
        Name (input): The name of an existing point object, point element, or group of
            objects depending on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the point element corresponding to
            the point object specified by the Name item. If this item is Element, the result
            request is for the point element specified by the Name item. If this item is
            GroupElm, the result request is for all point elements directly or indirectly
            specified in the group specified by the Name item. If this item is SelectionElm,
            the result request is for all point elements directly or indirectly selected and
            the Name item is ignored. See Item Type for Elements for more information.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the point object name associated with
            each result, if any. Some results will have no point object associated with
            them. For those cases, this item will be blank.
        Elm (output): This is an array that includes the point element name associated with
            each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.JointVelAbs(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.JointVelAbs falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def LinkDeformation(self, Name: str, ItemTypeElm: int):
        """This function reports the link internal deformations. The function returns zero if the
        deformations are successfully recovered, otherwise it returns a nonzero value. See
        Analysis Results Remarks for more information.
    
        Name (input): The name of an existing link object, link element, or group of
            objects, depending on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm= = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the link element corresponding to
            the link object specified by the Name item. If this item is Element, the result
            request is for the link element specified by the Name item. If this item is
            GroupElm, the result request is for all link elements directly or indirectly
            specified in the group specified by the Name item. If this item is SelectionElm,
            the result request is for link elements directly or indirectly selected, and the
            Name item is ignored. For GroupElm and SelectionElm a link element may be
            indirectly specified through point objects that have panel zone assignments and
            through line, area, and solid objects that have spring assignments.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the link object name associated with
            each result, if any.
        Elm (output): This is an array that includes the link element name associated with
            each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.LinkDeformation(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.LinkDeformation falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def LinkForce(self, Name: str, ItemTypeElm: int):
        """This function reports the link forces at the point elements at the ends of the specified
        link elements. The function returns zero if the forces are successfully recovered,
        otherwise it returns a nonzero value. See Analysis Results Remarks for more
        information.
    
        Name (input): The name of an existing link object, link element, or group of objects
            ,depending on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the link element corresponding to
            the link object specified by the Name item. If this item is Element, the result
            request is for the link element specified by the Name item. If this item is
            GroupElm, the result request is for all link elements directly or indirectly
            specified in the group specified by the Name item. If this item is SelectionElm,
            the result request is for link elements directly or indirectly selected and the
            Name item is ignored. For GroupElm and SelectionElm a link element may be
            indirectly specified through point objects that have panel zone assignments and
            through line, area and solid objects that have spring assignments.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the link object name associated with
            each result, if any.
        Elm (output): This is an array that includes the link element name associated with
            each result.
        PointElm (output): This is an array that includes the point element name associated
            with each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        P (output): This is an array that includes the link axial force (in the link local
            1-axis direction) at the specified point element. [F]
        T (output): This is an array that includes the link torsion (about the link local
            1-axis) at the specified point element. [FL]
        """
        _r = self._raw.LinkForce(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.LinkForce falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def LinkJointForce(self, Name: str, ItemTypeElm: int):
        """This function reports the joint forces for the point elements at the ends of the specified
        link elements. The function returns zero if the forces are successfully recovered,
        otherwise it returns a nonzero value. See Analysis Results Remarks for more
        information.
    
        Name (input): The name of an existing link object, link element or group of objects
            depending on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the link element corresponding to
            the link object specified by the Name item. If this item is Element, the result
            request is for the link element specified by the Name item. If this item is
            GroupElm, the result request is for all link elements directly or indirectly
            specified in the group specified by the Name item. If this item is SelectionElm,
            the result request is for link elements directly or indirectly selected and the
            Name item is ignored. For GroupElm and SelectionElm a link element may be
            indirectly specified through point objects that have panel zone assignments and
            through line, area and solid objects that have spring assignments.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the link object name associated with
            each result, if any.
        Elm (output): This is an array that includes the link element name associated with
            each result.
        PointElm (output): This is an array that includes the point element name associated
            with each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.LinkJointForce(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.LinkJointForce falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ModalLoadParticipationRatios(self):
        """This function reports the modal load participation ratios for each selected modal analysis
        case. The function returns zero if the data is successfully recovered; otherwise it
        returns a nonzero value. See Analysis Results Remarks for more information.
    
        NumberResults (output): The total number of results returned by the program.
        LoadCase (output): This is an array that includes the name of the modal load case
            associated with each result.
        ItemType (output): This is an array that includes Load Pattern, Acceleration, Link
            or Panel Zone. It specifies the type of item for which the modal load
            participation is reported.
        Item (output): This is an array whose values depend on the ItemType. If the ItemType
            is Load Pattern, this is the name of the load pattern. If the ItemType is
            Acceleration, this is UX, UY, UZ, RX, RY, or RZ, indicating the acceleration
            direction. If the ItemType is Link, this is the name of the link followed by U1,
            U2, U3, R1, R2, or R3 (in parenthesis), indicating the link degree of freedom
            for which the output is reported. If the ItemType is Panel Zone, this is the
            name of the joint to which the panel zone is assigned, followed by U1, U2, U3,
            R1, R2, or R3 (in parenthesis), indicating the degree of freedom for which the
            output is reported.
        Stat (output): This is an array that includes the percent static load participation
            ratio.
        Dyn (output): This is an array that includes the percent dynamic load participation
            ratio.
        """
        _r = self._raw.ModalLoadParticipationRatios(0, [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.ModalLoadParticipationRatios falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ModalParticipatingMassRatios(self):
        """This function reports the modal participating mass ratios for each mode of each selected
        modal analysis case. The function returns zero if the data is successfully
        recovered; otherwise it returns a nonzero value. See Analysis Results Remarks for
        more information.
    
        NumberResults (output): The total number of results returned by the program.
        LoadCase (output): This is an array that includes the name of the modal load case
            associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result. For modal results, this will always be Mode.
        StepNum (output): This is an array that includes the step number for each result.
            For modal results, this is always the mode number.
        Period (output): This is an array that includes the period for each result. [s]
        Ux (output): This is an array that includes the modal participating mass ratio for
            the structure Ux degree of freedom. The ratio applies to the specified mode.
        Uy (output): This is an array that includes the modal participating mass ratio for
            the structure Uy degree of freedom. The ratio applies to the specified mode.
        Uz (output): This is an array that includes the modal participating mass ratio for
            the structure Uz degree of freedom. The ratio applies to the specified mode.
        SumUx (output): This is an array that includes the cumulative sum of the modal
            participating mass ratios for the structure Ux degree of freedom.
        SumUy (output): This is an array that includes the cumulative sum of the modal
            participating mass ratios for the structure Uy degree of freedom.
        SumUz (output): This is an array that includes the cumulative sum of the modal
            participating mass ratios for the structure Uz degree of freedom.
        Rx (output): This is an array that includes the modal participating mass ratio for
            the structure Rx degree of freedom. The ratio applies to the specified mode.
        Ry (output): This is an array that includes the modal participating mass ratio for
            the structure Ry degree of freedom. The ratio applies to the specified mode.
        Rz (output): This is an array that includes the modal participating mass ratio for
            the structure Rz degree of freedom. The ratio applies to the specified mode.
        SumRx (output): This is an array that includes the cumulative sum of the modal
            participating mass ratios for the structure Rx degree of freedom.
        SumRy (output): This is an array that includes the cumulative sum of the modal
            participating mass ratios for the structure Ry degree of freedom.
        SumRz (output): This is an array that includes the cumulative sum of the modal
            participating mass ratios for the structure Rz degree of freedom.
        """
        _r = self._raw.ModalParticipatingMassRatios(0, [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.ModalParticipatingMassRatios falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ModalParticipationFactors(self):
        """This function reports the modal participation factors for each mode of each selected modal
        analysis case. The function returns zero if the data is successfully recovered;
        otherwise it returns a nonzero value. See Analysis Results Remarks for more
        information.
    
        NumberResults (output): The total number of results returned by the program.
        LoadCase (output): This is an array that includes the name of the modal load case
            associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result. For modal results, this will always be Mode.
        StepNum (output): This is an array that includes the step number for each result.
            For modal results, this will always be the mode number.
        Period (output): This is an array that includes the period for each result. [s]
        Ux (output): This is an array that includes the modal participation factor for the
            structure Ux degree of freedom. The factor applies to the specified mode. [Fs 2
            ]
        Uy (output): This is an array that includes the modal participation factor for the
            structure Uy degree of freedom. The factor applies to the specified mode. [Fs 2
            ]
        Uz (output): This is an array that includes the modal participation factor for the
            structure Uz degree of freedom. The factor applies to the specified mode. [Fs 2
            ]
        Rx (output): This is an array that includes the modal participation factor for the
            structure Rx degree of freedom. The factor applies to the specified mode. [FLs 2
            ]
        Ry (output): This is an array that includes the modal participation factor for the
            structure Ry degree of freedom. The factor applies to the specified mode. [FLs 2
            ]
        Rz (output): This is an array that includes the modal participation factor for the
            structure Rz degree of freedom. The factor applies to the specified mode. [FLs 2
            ]
        ModalMass (output): This is an array that includes the modal mass for the specified
            mode. This is a measure of the kinetic energy in the structure as it is
            deforming in the specified mode. [FLs 2 ]
        ModalStiff (output): This is an array that includes the modal stiffness for the
            specified mode. This is a measure of the strain energy in the structure as it is
            deforming in the specified mode. [FL]
        """
        _r = self._raw.ModalParticipationFactors(0, [], [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.ModalParticipationFactors falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ModalPeriod(self):
        """This function reports the modal period, cyclic frequency, circular frequency and eigenvalue
        for each selected modal load case. The function returns zero if the data is
        successfully recovered, otherwise it returns a nonzero value. See Analysis Results
        Remarks for more information.
    
        NumberResults (output): The number total of results returned by the program.
        LoadCase (output): This is an array that includes the name of the modal analysis
            case associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result. For modal results this is always be Mode.
        StepNum (output): This is an array that includes the step number for each result.
            For modal results this is always the mode number.
        Period (output): This is an array that includes the period for each result. [s]
        Frequency (output): This is an array that includes the cyclic frequency for each
            result. [1/s]
        CircFreq (output): This is an array that includes the circular frequency for each
            result. [rad/s]
        EigenValue (output): This is an array that includes the eigenvalue for the specified
            mode for each result. [rad 2 /s 2 ]
        """
        _r = self._raw.ModalPeriod(0, [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.ModalPeriod falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ModeShape(self, Name: str, ItemTypeElm: int):
        """This function reports the modal displacements (mode shapes) for the specified point
        elements. The function returns zero if the displacements are successfully recovered,
        otherwise it returns a nonzero value. See Analysis Results Remarks for more
        information.
    
        Name (input): The name of an existing point element or group of objects, depending
            on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the point element corresponding to
            the point object specified by the Name item. If this item is Element, the result
            request is for the point element specified by the Name item. If this item is
            GroupElm, the result request is for all point elements directly or indirectly
            specified in the group specified by the Name item. If this item is SelectionElm,
            the result request is for all point elements directly or indirectly selected and
            the Name item is ignored. See Item Type for Elements for more information.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the point object name associated with
            each result, if any. Some results will have no point object associated with
            them. For these cases this item will be blank.
        Elm (output): This is an array that includes the point element name associated with
            each result.
        LoadCase (output): This is an array that includes the name of the modal analysis
            case associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result. For mode shape results, this is always be Mode.
        StepNum (output): This is an array that includes the step number for each result.
            For mode shape results, this is always the mode number.
        """
        _r = self._raw.ModeShape(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.ModeShape falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def PanelZoneDeformation(self, Name: str, ItemTypeElm: int):
        """This function reports the panel zone (link) internal deformations. The function returns zero
        if the deformations are successfully recovered, otherwise it returns a nonzero
        value. See Analysis Results Remarks for more information.
    
        Name (input): The name of an existing link object, link element, or group of
            objects, depending on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the panel zone (link) element
            corresponding to the panel zone assignment to the point object specified by the
            Name item. If this item is Element, the result request is for the panel zone
            (link) element specified by the Name item. If this item is GroupElm, the result
            request is for all panel zone (link) elements directly or indirectly specified
            in the group specified by the Name item. If this item is SelectionElm, the
            result request is for panel zone (link) elements directly or indirectly selected
            and the Name item is ignored. For GroupElm and SelectionElm a panel zone (link)
            element may be indirectly specified through point objects that have panel zone
            assignments.
        NumberResults (output): The total number of results returned by the program.
        Elm (output): This is an array that includes the panel zone (link) element name
            associated with each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.PanelZoneDeformation(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.PanelZoneDeformation falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def PanelZoneForce(self, Name: str, ItemTypeElm: int):
        """This function reports the panel zone (link) forces at the point elements at the ends of the
        specified panel zone (link) elements. The function returns zero if the forces are
        successfully recovered, otherwise it returns a nonzero value. See Analysis Result
        Remarks for more information.
    
        Name (input): The name of an existing point object, point element, or group of
            objects, depending on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the panel zone (link) element
            corresponding to the panel zone assignment to the point object specified by the
            Name item. If this item is Element, the result request is for the panel zone
            (link) element specified by the Name item. If this item is GroupElm, the result
            request is for all panel zone (link) elements directly or indirectly specified
            in the group specified by the Name item. If this item is SelectionElm, the
            result request is for panel zone (link) elements directly or indirectly selected
            and the Name item is ignored. For GroupElm and SelectionElm a panel zone (link)
            element may be indirectly specified through point objects that have panel zone
            assignments.
        NumberResults (output): The total number of results returned by the program.
        Elm (output): This is an array that includes the panel zone (link) element name
            associated with each result.
        PointElm (output): This is an array that includes the point element name associated
            with each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        P (output): This is an array that includes the panel zone (link) axial force (in the
            link local 1-axis direction) at the specified point element. [F]
        T (output): This is an array that includes the panel zone (link) torsion (about the
            link local 1-axis) at the specified point element. [FL]
        """
        _r = self._raw.PanelZoneForce(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.PanelZoneForce falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SectionCutAnalysis(self):
        """This function reports the section cut force for sections cuts that are specified to have an
        Analysis (F1, F2, F3, M1, M2, M3) result type. The function returns zero if the
        section cut forces are successfully recovered, otherwise it returns a nonzero value.
        See Analysis Results Remarks for more information.
    
        NumberResults (output): The number total of results returned by the program.
        SCut (output): This is an array that includes the name of the section cut associated
            with each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.SectionCutAnalysis(0, [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.SectionCutAnalysis falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SectionCutDesign(self):
        """This function reports the section cut force for sections cuts that are specified to have a
        Design (P, V2, V3, T, M2, M3) result type. The function returns zero if the section
        cut forces are successfully recovered, otherwise it returns a nonzero value. See
        Analysis Results Remarks for more information.
    
        NumberResults (output): The total number of results returned by the program.
        SCut (output): This is an array that includes the name of the section cut associated
            with each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.SectionCutDesign(0, [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.SectionCutDesign falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SolidJointForce(self, Name: str, ItemTypeElm: int):
        """This function reports the joint forces for the point elements at each corner of the
        specified solid elements. The function returns zero if the forces are successfully
        recovered, otherwise it returns a nonzero value. See Analysis Results Remarks for
        more information.
    
        Name (input): The name of an existing solid object, solid element, or group of
            objects, depending on the value of the ItemTypeElm item.
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the solid elements corresponding to
            the solid object specified by the Name item. If this item is Element, the result
            request is for the solid element specified by the Name item. If this item is
            GroupElm, the result request is for the solid elements corresponding to all
            solid objects included in the group specified by the Name item. If this item is
            SelectionElm, the result request is for solid elements corresponding to all
            selected solid objects and the Name item is ignored.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the solid object name associated with
            each result, if any.
        Elm (output): This is an array that includes the solid element name associated with
            each result.
        PointElm (output): This is an array that includes the point element name associated
            with each result.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        """
        _r = self._raw.SolidJointForce(Name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.SolidJointForce falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SolidStrain(self, name: str, ItemTypeElm: int):
        """This function reports the strains for the specified solid elements. Strains are reported at
        each point element associated with the solid element. The function returns zero if
        the strains are successfully recovered, otherwise it returns a nonzero value. See
        Analysis Results Remarks for more information.
    
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the solid elements corresponding to
            the solid object specified by the Name item. If this item is Element, the result
            request is for the solid element specified by the Name item. If this item is
            GroupElm, the result request is for the solid elements corresponding to all
            solid objects included in the group specified by the Name item. If this item is
            SelectionElm, the result request is for solid elements corresponding to all
            selected solid objects and the Name item is ignored.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the solid object name associated with
            each result, if any.
        Elm (output): This is an array that includes the solid element name associated with
            each result.
        PointElm (output): This is an array that includes the name of the point element
            where the results are reported.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        EVM (output): The solid element internal Von Mises strain at the specified point
            element location.
        """
        _r = self._raw.SolidStrain(name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.SolidStrain falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SolidStress(self, name: str, ItemTypeElm: int):
        """This function reports the stresses for the specified solid elements. Stresses are reported
        at each point element associated with the solid element. The function returns zero
        if the stresses are successfully recovered, otherwise it returns a nonzero value.
        See Analysis Results Remarks for more information.
    
        ItemTypeElm (input): This is one of the following items in the eItemTypeElm
            enumeration: ObjectElm = 0 Element = 1 GroupElm = 2 SelectionElm = 3 If this
            item is ObjectElm, the result request is for the solid elements corresponding to
            the solid object specified by the Name item. If this item is Element, the result
            request is for the solid element specified by the Name item. If this item is
            GroupElm, the result request is for the solid elements corresponding to all
            solid objects included in the group specified by the Name item. If this item is
            SelectionElm, the result request is for solid elements corresponding to all
            selected solid objects and the Name item is ignored.
        NumberResults (output): The total number of results returned by the program.
        Obj (output): This is an array that includes the solid object name associated with
            each result, if any.
        Elm (output): This is an array that includes the solid element name associated with
            each result.
        PointElm (output): This is an array that includes the name of the point element
            where the results are reported.
        LoadCase (output): This is an array that includes the name of the analysis case or
            load combination associated with each result.
        StepType (output): This is an array that includes the step type, if any, for each
            result.
        StepNum (output): This is an array that includes the step number, if any, for each
            result.
        SVM (output): The solid element internal Von Mises stress at the specified point
            element location. [F/L 2 ]
        """
        _r = self._raw.SolidStress(name, ItemTypeElm, 0, [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.SolidStress falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def StepLabel(self, LoadCase: str, StepNum: float):
        """This function generates the step label for analyzed staged-construction load cases. For load
        case types other then the staged construction, the label will be blank. The function
        returns zero if the step label is successfully generated; otherwise it returns a
        nonzero value.
    
        LoadCase (input): The name of an existing staged-construction load case.
        StepNum (input): This is an overall step number from the specified staged-
            construction load case. The range of values of StepNum for a given load case can
            be obtained from most analysis results calls, such as
            SapObject.SapModel.Results.JointDispl
        Label (output): The is the step label, including the name or number of the stage,
            the step number within the stage, and the age of the structure for time-
            dependent load cases
        """
        _r = self._raw.StepLabel(LoadCase, StepNum, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.StepLabel falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    @cached_property
    def Setup(self):
        return N_Results_Setup(self._raw.Setup)


class N_Results_Setup:
    """Wrapper para SapModel.Results.Setup."""

    def __init__(self, raw):
        self._raw = raw

    def DeselectAllCasesAndCombosForOutput(self):
        """The function deselects all load cases and response combinations for output. The function
        returns zero if the cases and combos are successfully deselected, otherwise it
        returns a nonzero value.
        """
        _r = self._raw.DeselectAllCasesAndCombosForOutput()
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput falhou (ret={_r})".format(_r=_r))
        return None

    def GetCaseSelectedForOutput(self, Name: str, Selected: bool):
        """This function checks if an load case is selected for output. The function returns 0 if the
        selected flag is successfully retrieved, otherwise it returns nonzero.
    
        Name (input): The name of an existing load case.
        Selected (input): This item is True if the specified load case is selected for
            output.
        """
        _r = self._raw.GetCaseSelectedForOutput(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.GetCaseSelectedForOutput falhou (ret={_r})".format(_r=_r))
        return None

    def GetComboSelectedForOutput(self, Name: str, Selected: bool):
        """This function checks if a load combination is selected for output. The function returns 0 if
        the selected flag is successfully retrieved, otherwise it returns nonzero.
    
        Name (input): The name of an existing load combination.
        Selected (input): This item is True if the specified load combination is selected
            for output.
        """
        _r = self._raw.GetComboSelectedForOutput(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.GetComboSelectedForOutput falhou (ret={_r})".format(_r=_r))
        return None

    def GetOptionBaseReactLoc(self):
        """This function retrieves the global coordinates of the location at which the base reactions
        are reported. The function returns 0 if the coordinates are successfully retrieved,
        otherwise it returns nonzero.
        """
        _r = self._raw.GetOptionBaseReactLoc(0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.GetOptionBaseReactLoc falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetOptionBucklingMode(self, BuckModeAll: bool):
        """This function retrieves the buckling modes for which buckling factors are reported. The
        function returns 0 if the modes are successfully retrieved, otherwise it returns
        nonzero.
    
        BuckModeStart (output): The first buckling mode for which the buckling factor is
            reported when the BuckModeAll item is False.
        BuckModeEnd (output): The last buckling mode for which the buckling factor is
            reported when the BuckModeAll item is False.
        BuckModeAll (input): If this item is True, buckling factors are reported for all
            calculated buckling modes. If it is False, buckling factors are reported for the
            buckling modes indicated by the BuckModeStart and BuckModeEnd items.
        """
        _r = self._raw.GetOptionBucklingMode(0, 0, BuckModeAll)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.GetOptionBucklingMode falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetOptionDirectHist(self, Value: int):
        """This function retrieves the output option for direct history results. The function returns 0
        if the output option is successfully retrieved, otherwise it returns nonzero.
    
        Value (input): This item is either 1, 2 or 3 1 = Envelopes 2 = Step-by-Step 3 = Last
            Step
        """
        _r = self._raw.GetOptionDirectHist(Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.GetOptionDirectHist falhou (ret={_r})".format(_r=_r))
        return None

    def GetOptionModalHist(self, Value: int):
        """This function retrieves the output option for modal history results. The function returns 0
        if the output option is successfully retrieved, otherwise it returns nonzero.
    
        Value (input): This item is either 1, 2 or 3 1 = Envelopes 2 = Step-by-Step 3 = Last
            Step
        """
        _r = self._raw.GetOptionModalHist(Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.GetOptionModalHist falhou (ret={_r})".format(_r=_r))
        return None

    def GetOptionModeShape(self, ModeShapesAll: bool):
        """This function retrieves the modes for which mode shape results are reported. The function
        returns 0 if the modes are successfully retrieved, otherwise it returns nonzero.
    
        ModeShapeStart (output): The first mode for which results are reported when the
            ModeShapesAll item is False.
        ModeShapeEnd (output): The last mode for which results are reported when the
            ModeShapesAll item is False.
        ModeShapesAll (input): If this item is True, results are reported for all calculated
            modes. If it is False, results are reported for the modes indicated by the
            ModeShapeStart and ModeShapeEnd items.
        """
        _r = self._raw.GetOptionModeShape(0, 0, ModeShapesAll)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.GetOptionModeShape falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetOptionMultiStepStatic(self, Value: int):
        """This function retrieves the output option for multistep static linear results. The function
        returns 0 if the output option is successfully retrieved, otherwise it returns
        nonzero.
    
        Value (input): This item is either 1, 2 or 3 1 = Envelopes 2 = Step-by-Step 3 = Last
            Step
        """
        _r = self._raw.GetOptionMultiStepStatic(Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.GetOptionMultiStepStatic falhou (ret={_r})".format(_r=_r))
        return None

    def GetOptionMultiValuedCombo(self, Value: int):
        """This function retrieves the output option for multi-valued load combination results. The
        function returns 0 if the output option is successfully retrieved, otherwise it
        returns nonzero.
    
        Value (input): This item is either 1, 2, or 3 1 = Envelopes 2 = Multiple values, if
            possible 3 = Correspondence
        """
        _r = self._raw.GetOptionMultiValuedCombo(Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.GetOptionMultiValuedCombo falhou (ret={_r})".format(_r=_r))
        return None

    def GetOptionNLStatic(self, Value: int):
        """This function retrieves the output option for nonlinear static results. The function returns
        0 if the output option is successfully retrieved, otherwise it returns nonzero.
    
        Value (input): This item is either 1, 2 or 3 1 = Envelopes 2 = Step-by-Step 3 = Last
            Step
        """
        _r = self._raw.GetOptionNLStatic(Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.GetOptionNLStatic falhou (ret={_r})".format(_r=_r))
        return None

    def GetOptionPSD(self, Value: int):
        """This function retrieves the output option for power spectral density results. The function
        returns 0 if the output option is successfully retrieved, otherwise it returns
        nonzero.
    
        Value (input): This item is either 1 or 2 1 = RMS 2 = sqrt(PSD)
        """
        _r = self._raw.GetOptionPSD(Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.GetOptionPSD falhou (ret={_r})".format(_r=_r))
        return None

    def GetOptionSteadyState(self, Value: int):
        """This function retrieves the output option for steady state results. The function returns 0
        if the output option is successfully retrieved, otherwise it returns nonzero.
    
        Value (input): This item is either 1 or 2 1 = Envelopes 2 = At Frequencies
        SteadyStateOption (output): This item is 1, 2 or 3 1 = In and Out of Phase 2 =
            Magnitude 3 = All
        """
        _r = self._raw.GetOptionSteadyState(Value, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.GetOptionSteadyState falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetSectionCutSelectedForOutput(self, Name: str):
        """This function retrieves whether a defined section cut is selected for output. The function
        returns 0 if the selected flag is successfully retrieved, otherwise it returns
        nonzero. Please note that all section cuts are, by default, selected for output when
        they are created.
        """
        _r = self._raw.GetSectionCutSelectedForOutput(Name, False)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.GetSectionCutSelectedForOutput falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SelectAllSectionCutsForOutput(self):
        """This function selects or deselects all section cuts for output. The function returns 0 if
        the selected flag is successfully set, otherwise it returns nonzero. Please note
        that all section cuts are, by default, selected for output when they are created.
        """
        _r = self._raw.SelectAllSectionCutsForOutput(False)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.SelectAllSectionCutsForOutput falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetCaseSelectedForOutput(self, Name: str, Selected: bool = True):
        """This function sets an load case selected for output flag. The function returns 0 if the
        selected flag is successfully set, otherwise it returns nonzero.
    
        Name (input): The name of an existing load case.
        Selected (input): This item is True if the specified load case is to be selected for
            output, otherwise it is False.
        """
        _r = self._raw.SetCaseSelectedForOutput(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.SetCaseSelectedForOutput falhou (ret={_r})".format(_r=_r))
        return None

    def SetComboSelectedForOutput(self, Name: str, Selected: bool = True):
        """This function sets a load combination selected for output flag. The function returns 0 if
        the selected flag is successfully set, otherwise it returns nonzero.
    
        Name (input): The name of an existing load combination.
        Selected (input): This item is True if the specified load combination is to be
            selected for output, otherwise it is False.
        """
        _r = self._raw.SetComboSelectedForOutput(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.SetComboSelectedForOutput falhou (ret={_r})".format(_r=_r))
        return None

    def SetOptionBaseReactLoc(self, gx: float, gy: float, gz: float):
        """This function sets the global coordinates of the location at which the base reactions are
        reported. The function returns 0 if the coordinates are successfully set, otherwise
        it returns nonzero.
        """
        _r = self._raw.SetOptionBaseReactLoc(gx, gy, gz)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.SetOptionBaseReactLoc falhou (ret={_r})".format(_r=_r))
        return None

    def SetOptionBucklingMode(self, BuckModeStart: int, BuckModeEnd: int, BuckModeAll: bool = False):
        """This function sets the buckling modes for which buckling factors are reported. The function
        returns 0 if the modes are successfully set, otherwise it returns nonzero.
    
        BuckModeStart (input): The first buckling mode for which the buckling factor is
            reported when the BuckModeAll item is False.
        BuckModeEnd (input): The last buckling mode for which the buckling factor is
            reported when the BuckModeAll item is False.
        BuckModeAll (input): If this item is True, buckling factors are reported for all
            calculated buckling modes. If it is False, buckling factors are reported for the
            buckling modes indicated by the BuckModeStart and BuckModeEnd items.
        """
        _r = self._raw.SetOptionBucklingMode(BuckModeStart, BuckModeEnd, BuckModeAll)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.SetOptionBucklingMode falhou (ret={_r})".format(_r=_r))
        return None

    def SetOptionDirectHist(self, Value: int):
        """This function sets the output option for direct history results. The function returns 0 if
        the output option is successfully set, otherwise it returns nonzero.
    
        Value (input): This item is 1, 2 or 3 1 = Envelopes 2 = Step-by-Step 3 = Last Step
        """
        _r = self._raw.SetOptionDirectHist(Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.SetOptionDirectHist falhou (ret={_r})".format(_r=_r))
        return None

    def SetOptionModalHist(self, Value: int):
        """This function sets the output option for modal history results. The function returns 0 if
        the output option is successfully set, otherwise it returns nonzero.
    
        Value (input): This item is 1, 2 or 3 1 = Envelopes 2 = Step-by-Step 3 = Last Step
        """
        _r = self._raw.SetOptionModalHist(Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.SetOptionModalHist falhou (ret={_r})".format(_r=_r))
        return None

    def SetOptionModeShape(self, ModeShapeStart: int, ModeShapeEnd: int, ModeShapesAll: bool = False):
        """This function sets the modes for which mode shape results are reported. The function returns
        0 if the modes are successfully set, otherwise it returns nonzero.
    
        ModeShapeStart (input): The first mode for which results are reported when the
            ModeShapesAll item is False.
        ModeShapeEnd (input): The last mode for which results are reported when the
            ModeShapesAll item is False.
        ModeShapesAll (input): If this item is True, results are reported for all calculated
            modes. If it is False, results are reported for the modes indicated by the
            ModeShapeStart and ModeShapeEnd items.
        """
        _r = self._raw.SetOptionModeShape(ModeShapeStart, ModeShapeEnd, ModeShapesAll)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.SetOptionModeShape falhou (ret={_r})".format(_r=_r))
        return None

    def SetOptionMultiStepStatic(self, Value: int):
        """This function sets the output option for multistep static linear results. The function
        returns 0 if the output option is successfully set, otherwise it returns nonzero.
    
        Value (input): This item is 1, 2 or 3 1 = Envelopes 2 = Step-by-Step 3 = Last Step
        """
        _r = self._raw.SetOptionMultiStepStatic(Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.SetOptionMultiStepStatic falhou (ret={_r})".format(_r=_r))
        return None

    def SetOptionMultiValuedCombo(self, Value: int):
        """This function sets the output option for multi-valued load combination results. The function
        returns 0 if the output option is successfully set, otherwise it returns nonzero.
    
        Value (input): This item is either 1, 2, or 3. 1 = Envelopes 2 = Multiple values, if
            possible 3 = Correspondence
        """
        _r = self._raw.SetOptionMultiValuedCombo(Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.SetOptionMultiValuedCombo falhou (ret={_r})".format(_r=_r))
        return None

    def SetOptionNLStatic(self, Value: int):
        """This function sets the output option for nonlinear static results. The function returns 0 if
        the output option is successfully set, otherwise it returns nonzero.
    
        Value (input): This item is 1, 2 or 3 1 = Envelopes 2 = Step-by-Step 3 = Last Step
        """
        _r = self._raw.SetOptionNLStatic(Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.SetOptionNLStatic falhou (ret={_r})".format(_r=_r))
        return None

    def SetOptionPSD(self, Value: int):
        """This function sets the output option for power spectral density results. The function
        returns 0 if the output option is successfully set, otherwise it returns nonzero.
    
        Value (input): This item is either 1 or 2 1 = RMS 2 = sqrt(PSD)
        """
        _r = self._raw.SetOptionPSD(Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.SetOptionPSD falhou (ret={_r})".format(_r=_r))
        return None

    def SetOptionSteadyState(self, Value: int, SteadyStateOption: int):
        """This function sets the output option for steady state results. The function returns 0 if the
        output option is successfully set, otherwise it returns nonzero.
    
        Value (input): This item is either 1 or 2 1 = Envelopes 2 = At Frequencies
        SteadyStateOption (input): This item is 1, 2 or 3 1 = In and Out of Phase 2 =
            Magnitude 3 = All
        """
        _r = self._raw.SetOptionSteadyState(Value, SteadyStateOption)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.SetOptionSteadyState falhou (ret={_r})".format(_r=_r))
        return None

    def SetSectionCutSelectedForOutput(self, Name: str, Selected: bool):
        """This function selects or deselects a defined section cut for output. The function returns 0
        if the selected flag is successfully set, otherwise it returns nonzero. Please note
        that all section cuts are, by default, selected for output when they are created.
        """
        _r = self._raw.SetSectionCutSelectedForOutput(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.Results.Setup.SetSectionCutSelectedForOutput falhou (ret={_r})".format(_r=_r))
        return None


