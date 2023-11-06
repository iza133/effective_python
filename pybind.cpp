#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

int main() {
    // Initialize the Python interpreter
    py::scoped_interpreter guard{};

    try {
        // Import the Python module
        py::module lab5 = py::module::import("lab5");

        // Prepare a C++ vector of Celsius temperatures
        std::vector<double> celsius_temperatures = {0.0, 25.0, 100.0};

        // Call the Python function and get the result as a C++ vector
        py::list result = lab5.attr("celsius_to_fahrenheit")(celsius_temperatures);

        // Convert the Python list to a C++ vector of doubles
        std::vector<double> fahrenheit_temperatures;
        for (const auto& item : result) {
            fahrenheit_temperatures.push_back(item.cast<double>());
        }

        // Print the result
        for (size_t i = 0; i < fahrenheit_temperatures.size(); ++i) {
            printf("Celsius: %lf, Fahrenheit: %lf\n", celsius_temperatures[i], fahrenheit_temperatures[i]);
        }
    } catch (const py::error_already_set& ex) {
        PyErr_Print();
    }

    return 0;
}
