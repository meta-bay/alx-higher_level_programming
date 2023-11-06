#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - info on the data structure.
 * @p: pointer to object.
*/
void print_python_list_info(PyObject *p)
{
	int long sz = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;
	int i;

	printf("[*] Size of the Python List = %li\n", sz);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (i = 0; i < sz; i++)
		printf("Element %d: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
