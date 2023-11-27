#include "lists.h"

/*
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: singly linked list
 *
 * Return: 0 if there is no cycle 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *x, *z;

	if (list == NULL || list->next == NULL)
		return (0);
	x = list->next;
	z = list->next->next;

	while (x && z && z->next)
	{
		if (x == z)
			return (1);

		x = x->next;
		z = z->next->next;
	}
	return (0);
}
