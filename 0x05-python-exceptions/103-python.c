#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - python list info
 * @p: the pyobject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocation, i;
	const char *the_type;
	PyListObject *the_list = (PyListObject *)p;
	PyVarObject *the_var = (PyVarObject *)p;

	size = the_var->ob_size;
	allocation = the_list->allocated;
	fflush(stdout);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocation);
	for (i = 0; i < size; i++)
	{
		the_type = the_list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, the_type);
		if (strcmp(the_type, "bytes") == 0)
			print_python_bytes(the_list->ob_item[i]);
		else if (strcmp(the_type, "float") == 0)
			print_python_float(the_list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Python byte info
 * @p: the pyobject
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	PyBytesObject *no_of_bytes = (PyBytesObject *)p;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", no_of_bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", no_of_bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - python float info
 * @p: the pyobject
 */

void print_python_float(PyObject *p)
{
	char *buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	PyMem_Free(buffer);
}
