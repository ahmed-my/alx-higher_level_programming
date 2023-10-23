#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - function to print basic info about Python lists.
 * @p: pointer to PyObject
 * Return: none
 *
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, tmp, n;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	tmp = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", tmp);

	for (n = 0; n < size; n++)
	{
		type = list->ob_item[n]->ob_type->tp_name;
		printf("Element %ld: %s\n", n, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[n]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[n]);
	}
}

