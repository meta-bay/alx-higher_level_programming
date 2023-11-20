#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - about python list
 * @p: the pyobject
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *the_thing;
	int i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (i < size)
		{
			the_thing = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}


/**
 * print_python_float - abou python float
 * @p: the pyobject
 */

void print_python_float(PyObject *p)
{
	double the_value = 0;
	char *the_string = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	the_value = ((PyFloatObject *)p)->ob_fval;
	the_string = PyOS_double_to_string(the_value, 'r', 0,
										Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", the_string);
}

/**
 * print_python_bytes - about python bytes
 * @p: the pyobject
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, i = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (i < size + 1 && i < 10)
	{
		printf(" %02hhx", str[i]);
		i++;
	}
	printf("\n");
}
