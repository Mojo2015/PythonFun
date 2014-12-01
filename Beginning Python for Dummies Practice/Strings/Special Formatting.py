Formatted = "{:d}"
print(Formatted.format(7000))

Formatted = "{:,d}"
print(Formatted.format(7000))

Formatted = "{:^15,d}"
print(Formatted.format(7000))

Formatted = "{:*^15,d}"
print(Formatted.format(7000))

Formatted = "{:*^15.2f}"
print(Formatted.format(7000))

Formatted = "{:*>15X}"
print(Formatted.format(7000))

Formatted = "{:*<#15x}"
print(Formatted.format(7000))

Formatted = "A {0} {1} and a {0} {2}."
print(Formatted.format("blue", "car", "truck"))

