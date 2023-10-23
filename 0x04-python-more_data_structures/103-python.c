#include <stdio.h>
#include <time.h>
#include <Python.h>
/**
 * print_python_bytes - function to print bytes information
 * @p: pointer to PyObject
 * Return: no return
 *
 */
void print_python_bytes(PyObject *p)
{
	char *s;
	long int size, n, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	s = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", s);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (n = 0; n < limit; n++)
		if (s[n] >= 0)
			printf(" %02x", s[n]);
		else
			printf(" %02x", 256 + s[n]);

	printf("\n");
}

/**
 * print_python_list - function to print list information
 * @p: pointer to pyObject
 * Return: no return
 *
 */
void print_python_list(PyObject *p)
{
	long int size, n;
	PyListObject *list;
	PyObject *object;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (n = 0; n < size; n++)
	{
		object = ((PyListObject *)p)->ob_item[n];
		printf("Element %ld: %s\n", n, ((object)->ob_type)->tp_name);
		if (PyBytes_Check(object))
			print_python_bytes(object);
	}
}
