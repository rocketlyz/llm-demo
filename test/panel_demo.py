import panel as pn

pn.extension()

component = pn.panel("""
# Wind Turbine

A wind turbine is a device that converts the kinetic energy of wind into \
[electrical energy](https://en.wikipedia.org/wiki/Electrical_energy).

Read more [here](https://en.wikipedia.org/wiki/Wind_turbine).
""")
print(component)

component.servable()
