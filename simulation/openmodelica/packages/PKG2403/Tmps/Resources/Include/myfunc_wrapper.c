#include <Python.h>
#include <stdio.h>

// Function to call the Python function
double call_myfunc(double a, double b, const char* filePath)  {
    /*// Set PYTHONPATH programmatically
    const char* pythonPath = filePath;
    setenv("PYTHONPATH", pythonPath, 1); // Overwrite if it exists//*/
    char* filename;
    
    // Find the last occurrence of '/' or '\' (directory separator)
    const char* lastSlash = strrchr(filePath, '/');
    
    // If no directory separator is found, assume the fullPath is just the filename
    const char* startOfFilename = (lastSlash != NULL) ? lastSlash + 1 : filePath;
    
    // Find the last occurrence of '.' (file extension)
    const char* lastDot = strrchr(startOfFilename, '.');
    
    // If no extension is found, copy the entire filename
    if (lastDot == NULL) {
        strcpy(filename, startOfFilename);
        return -1;
    }

    // Copy the filename without the extension
    strncpy(filename, startOfFilename, lastDot - startOfFilename);
    filename[lastDot - startOfFilename] = '\0'; // Null-terminate the string
    
    
    // Initialize the Python interpreter
    Py_Initialize();

    // Get the system path
    PyObject* sysPath = PySys_GetObject("path");

    // Print the current sysPath
    PyObject* sysPathStr = PyObject_Repr(sysPath);
    const char* sysPathCStr = PyUnicode_AsUTF8(sysPathStr);
    //printf("Current sys.path: %s\n", sysPathCStr);

    // Import the Python module
    PyObject* pModule = PyImport_ImportModule(filename);
    if (pModule == NULL) {
        PyErr_Print();
        printf("Error: Failed to import Python module 'myfunc'.\n");
        return -1;
    }

    // Get the Python function
    PyObject* pFunc = PyObject_GetAttrString(pModule, "myfunc");
    if (pFunc == NULL || !PyCallable_Check(pFunc)) {
        PyErr_Print();
        printf("Error: Failed to get Python function 'myfunc'.\n");
        return -1;
    }

    // Prepare arguments for the Python function
    PyObject* pArgs = PyTuple_New(2);
    PyTuple_SetItem(pArgs, 0, PyFloat_FromDouble(a));
    PyTuple_SetItem(pArgs, 1, PyFloat_FromDouble(b));

    // Call the Python function
    PyObject* pResult = PyObject_CallObject(pFunc, pArgs);
    if (pResult == NULL) {
        PyErr_Print();
        printf("Error: Python function call failed.\n");
        return -1;
    }

    // Convert the result to a C double
    double result = PyFloat_AsDouble(pResult);

    // Clean up
    Py_DECREF(pArgs);
    Py_DECREF(pFunc);
    Py_DECREF(pModule);
    Py_Finalize();

    return result;
}
