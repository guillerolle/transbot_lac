import sympy as smp
from ..mobilecarts import MobileCart

"""
    @package mobilebases
    @brief Common Car-Like Robots Definitions
"""

class Bicycle(MobileCart):
    """!
        @brief Elementary Car-Like with only 2 wheels (Bicycle model)
    """

    def __init__(self, name=None, mathname="bi", params = {}, compute_canudas=True, **kwargs):
        """!
            @param params Allowed parameters: 
                xf: position of fixed wheel along cart's x axis
                xs: position of steering wheel along cart's x axis
                r: wheels radius
        """
        #if name is None:
        #    name = self.__class__.__name__

        if not "xf" in params:
            params["xf"] = smp.Symbol("xf", real=True)
        if not "xs" in params:
            params["xs"] = smp.Symbol("xs", real=True)
        if not "r" in params:
            params["r"] = smp.Symbol("r", positive=True)

        super().__init__(name, mathname, compute_canudas = compute_canudas, **kwargs, params = {
            "wheels": [
                {"type": "fixed",
                "params": {
                    "l": params['xf'],
                    "beta": smp.pi/2,
                    "alpha": 0,
                    "phi_actuated": True,
                    "r": params["r"],
                }},
                {"type": "steering",
                "params": {
                    "l": params['xs'],
                    "alpha": 0,
                    "phi_actuated": True,
                    "r": params["r"],
                }},
                ]
            }
    )