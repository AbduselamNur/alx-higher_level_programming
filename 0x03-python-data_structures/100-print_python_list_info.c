#include "Python.h"

void print_python_list_info(PyObject *p)
{
        PyListObject *l;
        Py_ssize_t size, i;
        PyObject *ob;
        struct _typeobject *type;

        if (strcmp(p->ob_type->tp_name, "list") == 0)
        {
               l = (PyListObject *)p;
               size = l->ob_base.ob_size;
               printf("[*] Size of the Python List = %ld\n", size);
               printf("[*] Allocated = %ld\n", l->allocated);
               for (i = 0; i < size; i++)
	       {
	               ob = l->ob_item[i];
	               type = ob->ob_type;
	               printf("Element %ld: %s\n", i, type->tp_name);
	       }
        }
}
