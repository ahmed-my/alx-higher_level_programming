#include "lists.h"
/**
  3  * check_cycle - function to check for cycle in linked list
  4  * @list: pointer to struct listint_t
  5  * Return: 1 if cycle is present, otherwise 0
  6  *
  7  */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *faster = list;

	if (!list)
		return (0);
	while (fast && faster && faster->next)
	{
		fast = fast->next;
		faster = faster->next->next;
		if (fast == faster)
			return (1);
	}
	return (0);
}
