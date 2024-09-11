document.addEventListener("DOMContentLoaded", function () {
  const conversionTypeElement = document.getElementById("conversionType");
  const fromUnitElement = document.getElementById("fromUnit");
  const toUnitElement = document.getElementById("toUnit");
  const convertButton = document.getElementById("convertButton");
  const resultElement = document.getElementById("result");

  const conversionOptions = {
    length: {
      units: [
        "meters",
        "kilometers",
        "miles",
        "feet",
        "centimeters",
        "inches",
        "yards",
      ],
      conversionFactors: {
        meters: 1,
        kilometers: 0.001,
        miles: 0.000621371,
        feet: 3.28084,
        centimeters: 100,
        inches: 39.3701,
        yards: 1.09361,
      },
    },
    temperature: {
      units: ["celsius", "fahrenheit", "kelvin"],
      conversionFormula: function (value, fromUnit, toUnit) {
        if (fromUnit === toUnit) return value;

        if (fromUnit === "celsius") {
          if (toUnit === "fahrenheit") return (value * 9) / 5 + 32;
          if (toUnit === "kelvin") return value + 273.15;
        }
        if (fromUnit === "fahrenheit") {
          if (toUnit === "celsius") return ((value - 32) * 5) / 9;
          if (toUnit === "kelvin") return ((value - 32) * 5) / 9 + 273.15;
        }
        if (fromUnit === "kelvin") {
          if (toUnit === "celsius") return value - 273.15;
          if (toUnit === "fahrenheit") return ((value - 273.15) * 9) / 5 + 32;
        }
      },
    },
    weight: {
      units: ["grams", "kilograms", "pounds", "ounces"],
      conversionFactors: {
        grams: 1,
        kilograms: 0.001,
        pounds: 0.00220462,
        ounces: 0.035274,
      },
    },
  };

  function populateUnits(type) {
    fromUnitElement.innerHTML = "";
    toUnitElement.innerHTML = "";
    const units = conversionOptions[type].units;
    units.forEach((unit) => {
      const fromOption = document.createElement("option");
      fromOption.value = unit;
      fromOption.textContent = unit;
      fromUnitElement.appendChild(fromOption);

      const toOption = document.createElement("option");
      toOption.value = unit;
      toOption.textContent = unit;
      toUnitElement.appendChild(toOption);
    });
  }

  conversionTypeElement.addEventListener("change", function () {
    populateUnits(conversionTypeElement.value);
  });

  convertButton.addEventListener("click", function () {
    const conversionType = conversionTypeElement.value;
    const value = parseFloat(document.getElementById("valueInput").value);
    const fromUnit = fromUnitElement.value;
    const toUnit = toUnitElement.value;

    if (isNaN(value)) {
      alert("Please enter a valid number.");
      return;
    }

    let convertedValue;

    if (conversionType === "temperature") {
      convertedValue = conversionOptions[conversionType].conversionFormula(
        value,
        fromUnit,
        toUnit
      );
    } else {
      const fromFactor =
        conversionOptions[conversionType].conversionFactors[fromUnit];
      const toFactor =
        conversionOptions[conversionType].conversionFactors[toUnit];
      convertedValue = (value / fromFactor) * toFactor;
    }

    resultElement.textContent = `${convertedValue.toFixed(2)} ${toUnit}`;
  });

  populateUnits(conversionTypeElement.value);
});
