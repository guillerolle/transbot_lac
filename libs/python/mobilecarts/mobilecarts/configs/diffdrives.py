import sympy as smp
from ..mobilecarts import MobileCart

"""
    @package mobilebases
    @brief Common Differential Drive Robots Definitions
"""

class DiffDrive_2Wheels(MobileCart):
    """!
        @brief Elementary Differential Drive with only 2 fixed wheels
    """

    def __init__(self, name=None, mathname="dd", params = {}, compute_canudas=True, **kwargs):
        """!
            @param params Allowed parameters: a, b, r
        """
        #if name is None:
        #    name = self.__class__.__name__

        if not "a" in params:
            params["a"] = smp.Symbol("a", positive=True)
        if not "b" in params:
            params["b"] = smp.Symbol("b", positive=True)
        if not "r" in params:
            params["r"] = smp.Symbol("r", positive=True)

        vpos_diff = smp.Matrix([params["a"], 
                                params["b"]]) # Coordenadas xy de la posición de la rueda relativo al chasis
        l = vpos_diff.norm(2)
        alpha0 = smp.atan2(vpos_diff[1], vpos_diff[0]) 
        beta0 = smp.pi/2 - alpha0
        alpha1 = smp.atan2(-vpos_diff[1], vpos_diff[0]) 
        beta1 = smp.pi/2 - alpha1

        super().__init__(name, mathname, compute_canudas = compute_canudas, **kwargs, params = {
            "wheels": [
                {"type": "fixed",
                "params": {
                    "l": l,
                    "beta": beta0,
                    "alpha": alpha0,
                    "phi_actuated": True,
                    "r": params["r"],
                }},
                {"type": "fixed",
                "params": {
                    "l": l,
                    "beta": beta1,
                    "alpha": alpha1,
                    "phi_actuated": True,
                    "r": params["r"],
                }},
                ]
            }
    )
        
class DiffDrive_3Wheels(MobileCart):
    """!
        @brief Elementary Differential Drive with 2 fixed wheels and 1 centered castor wheels
    """
    def __init__(self, name=None, mathname="dd", params = {}, compute_canudas=True, **kwargs):
        """!
            @param params Allowed parameters: 
                axle_offset (fixed wheels axle offset), 
                track (axle length), 
                r (wheel radius), 
                d (castor distance),
                c (castor position along x axis)
        """
        if name is None:
            name = self.__class__.__name__

        if not "axle_offset" in params:
            params["axle_offset"] = smp.Symbol("axle_offset", real=True) # axle offset
        if not "track" in params:
            params["track"] = smp.Symbol("track", positive=True, real=True) # axle length
        if not "r" in params:
            params["r"] = smp.Symbol("r", positive=True, real=True) # radio ruedas
        if not "d" in params:
            params["d"] = smp.Symbol("d", positive=True, real=True) # distancia caster
        if not "c" in params:
            params["c"] = smp.Symbol("c", real=True) # ubicación caster a lo largo de eje x

        vpos_diff = smp.Matrix([params["axle_offset"], 
                                params["track"]/2]) # Coordenadas xy de la posición de la rueda relativo al chasis
        l = vpos_diff.norm(2)
        alpha1 = smp.atan2(vpos_diff[1], vpos_diff[0])  # trasera izq
        beta1 = smp.pi/2 - alpha1
        alpha2 = smp.atan2(-vpos_diff[1], vpos_diff[0]) # trasera der
        beta2 = smp.pi/2 - alpha2


        super().__init__(name, mathname, compute_canudas = compute_canudas, **kwargs, params = {
            "wheels": [
                {"type": "fixed",
                "params": {
                    "l": l,
                    "beta": beta1,
                    "alpha": alpha1,
                    "phi_actuated": False,
                    "r": params["r"],
                }},
                {"type": "fixed",
                "params": {
                    "l": l,
                    "beta": beta2,
                    "alpha": alpha2,
                    "phi_actuated": False,
                    "r": params["r"],
                }},
                {"type": "castor",
                "params": {
                    "l": params['c'],
                    "alpha": 0,
                    "r": params["r"],
                    "d": -params["d"],
                    "beta_actuated": True,
                    "phi_actuated": True
                }},
                ]
            }
    )

class DiffDrive_4Wheels(MobileCart):
    """!
        @brief Elementary Differential Drive with 2 fixed wheels and 2 castor wheels
    """
    def __init__(self, name=None, mathname="dd", params = {}, compute_canudas=True, **kwargs):
        """!
            @param params Allowed parameters: a (x distance), b (y distance), r (wheel radius), d (castor distance)
        """
        if name is None:
            name = self.__class__.__name__

        if not "a" in params:
            params["a"] = smp.Symbol("a", positive=True) # distancia x ruedas
        if not "b" in params:
            params["b"] = smp.Symbol("b", positive=True) # distancia y ruedas
        if not "r" in params:
            params["r"] = smp.Symbol("r", positive=True) # radio ruedas
        if not "d" in params:
            params["d"] = smp.Symbol("d", positive=True) # distancia caster

        vpos_diff = smp.Matrix([-params["a"], 
                                -params["b"]]) # Coordenadas xy de la posición de la rueda relativo al chasis
        l = vpos_diff.norm(2)
        alpha0 = smp.atan2(vpos_diff[1], vpos_diff[0])  # trasera derecha
        beta0 = smp.pi/2 - alpha0
        alpha1 = smp.atan2(-vpos_diff[1], vpos_diff[0]) # trasera izquierda
        beta1 = smp.pi/2 - alpha1
        alpha2 = smp.atan2(vpos_diff[1], -vpos_diff[0]) # delantera derecha
        alpha3 = smp.atan2(-vpos_diff[1], -vpos_diff[0]) # delantera izquierda

        super().__init__(name, mathname, compute_canudas = compute_canudas, **kwargs, params = {
            "wheels": [
                {"type": "fixed",
                "params": {
                    "l": l,
                    "beta": beta0,
                    "alpha": alpha0,
                    "phi_actuated": True,
                    "r": params["r"],
                }},
                {"type": "fixed",
                "params": {
                    "l": l,
                    "beta": beta1,
                    "alpha": alpha1,
                    "phi_actuated": True,
                    "r": params["r"],
                }},
                {"type": "castor",
                "params": {
                    "l": l,
                    "alpha": alpha2,
                    "r": params["r"],
                    "d": params["d"],
                    "beta_actuated": False,
                }},
                {"type": "castor",
                "params": {
                    "l": l,
                    "alpha": alpha3,
                    "r": params["r"],
                    "d": params["d"],
                }},
                ]
            }
    )