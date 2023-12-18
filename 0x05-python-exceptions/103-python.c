#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: A PyObject list object
 */ 
void print_python_list(PyObject *p)
{
	char *type = "<class 'list'>";

	if (!PyList_Check(p))
	{
		printf("Invalid PyListObject\n");
		return;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));  
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	printf("Type = %s\n", type);

	fflush(stdout);
}

/**  
 * print_python_bytes - Prints basic info about Python byte objects  
 * @p: A PyObject byte object
 */
void print_python_bytes(PyObject *p)
{
	char *type = "<class 'bytes'>";

	if (!PyBytes_Check(p))
	{
		printf("Invalid PyBytesObject\n");
		return;
	}

	printf("[.] Python bytes info\n");

	if (((PyBytesObject *)(p))->ob_size >= 10)
		printf("First 10 bytes: ");
	else   
		printf("First %ld bytes: ", ((PyBytesObject *)(p))->ob_size);
	
	for (int i = 0; i < 10 && i < ((PyBytesObject *)(p))->ob_size; i++)				
		printf("%02x", ((unsigned char *)(((PyBytesObject *)(p))->ob_sval))[i]);	

	printf("\n");  
	printf("Size = %ld\n", ((PyBytesObject *)p)->ob_size);
	printf("Type = %s\n", type);

	fflush(stdout);
}

/**
 * print_python_float - Prints basic info about Python float objects  
 * @p: A PyObject float object
 */
void print_python_float(PyObject *p)  
{
	char *type = "<class 'float'>";
	
	if (!PyFloat_Check(p))
	{
		printf("Invalid PyFloatObject\n"); 	
		return;
	}		

	double val = ((PyFloatObject *)p)->ob_fval;

	printf("[.] Python float info\n");
	printf("Value = %lf\n", val);
	printf("Type = %s\n", type);

	fflush(stdout);
}
