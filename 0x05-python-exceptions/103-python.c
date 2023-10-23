#include <Python.h>


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


/**
 * print_python_bytes - function to print Python byte objects.
 * @p: pointer to PyObject
 * Return: none
 *
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, n;
	PyBytesObject *bytes = (PyBytesObject *)p;


	fflush(stdout);


	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}


	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);


	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;


	printf("  first %ld bytes: ", size);
	for (n = 0; n < size; n++)
	{
		printf("%02hhx", bytes->ob_sval[n]);
		if (n == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}


/**
 * print_python_float - function to print Python float objects.
 * @p: pointer to PyObject
 * Return: none
 *
 */
void print_python_float(PyObject *p)
{
	char *buff = NULL;


	PyFloatObject *float_obj = (PyFloatObject *)p;


	fflush(stdout);


	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}


	buff = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buff);
	PyMem_Free(buff);
}

