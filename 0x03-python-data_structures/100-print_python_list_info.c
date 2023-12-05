#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: A PyObject list
 */
void print_python_list_info(PyObject *p) 
{
    PyListObject *list = (PyListObject*)p;
    int size = PyList_Size(list);
    int allocated = list->allocated;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", allocated);
    printf("[*] Type object address in memory = %p\n", (void *)list->ob_type);
}
