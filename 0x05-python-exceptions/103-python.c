#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <stdlib.h>
#include <float.h>

/**
 * print_python_list - python lists info
 * @p: the pyobject
*/

void print_python_list(PyObject *p)
{
	unsigned long int size;
	unsigned int i;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	if (!PyList_Check(list))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		type = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, type);
		if (!strcmp(type, "bytes"))
		print_python_bytes(list->ob_item[i]);
		if (!strcmp(type, "float"))
		print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - about python bytes
 * @p: the pyobject
*/

void print_python_bytes(PyObject *p)
{
	unsigned long int size;
	unsigned int i;
	char *the_string = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	the_string = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", the_string);
	if (size < 10)
		printf("  first %lu bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", the_string[i]);
	printf("\n");
}

/**
 * print_python_float - about python float
 * @p: the pyobject
*/

void print_python_float(PyObject *p)
{
	PyFloatObject *_float = (PyFloatObject *)p;
	double _double = _float->ob_fval;
	char *str = NULL;

	printf("[.] float object info\n");
	if (!PyFloat_Check(_float))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	str = PyOS_double_to_string(_double, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
