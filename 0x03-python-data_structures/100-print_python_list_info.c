#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("The given object is not a Python list.\n");
        return;
    }

    printf("Python list information:\n");
    printf(" Total elements: %ld\n", PyList_Size(p));

    PyObject *iter = PyObject_GetIter(p);
    PyObject *item;
    while ((item = PyIter_Next(iter))) {
        printf(" List item: ");
        PyObject_Print(item, stdout, 0);
        printf("\n");
        Py_DECREF(item);
    }
    Py_DECREF(iter);
}
