#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (p == NULL || !PyList_Check(p)) {
        printf("Error: Not a valid Python list.\n");
        return;
    }

    Py_ssize_t length = PyList_Size(p);
    printf("Python list of length %zd: [", length);
    for (Py_ssize_t i = 0; i < length; i++) {
        PyObject *element = PyList_GetItem(p, i);
        if (element == NULL) {
            printf(" <list item not found>");
        } else {
            printf(" %S", element);
        }

        if (i < length - 1) {
            printf(",");
        }
    }
    printf(" ]\n");
}

void print_python_bytes(PyObject *p) {
    if (p == NULL || !PyBytes_Check(p)) {
        printf("Error: Not a valid Python bytes object.\n");
        return;
    }

    char *bytes = PyBytes_AS_STRING(p);
    Py_ssize_t length = PyBytes_GET_SIZE(p);

    printf("Python bytes object of length %zd: ", length);
    for (Py_ssize_t i = 0; i < length; i++) {
        printf("%02x", (unsigned char)bytes[i]);

        if (i < length - 1) {
            printf(" ");
        }
    }
    printf("\n");
}
