#include "lists.h"
#include <stdlib.h>
#include <stddef.h>


/**
 * insert_node - C function that inserts a no into a sorted singly linked list
 * @head: Pointer
 * @number: Number to insert
 *
 * Return: Address of the new node or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	if (node == NULL || node->n >= number)
	{
		newNode->next = node;
		*head = newNode;
		return (newNode);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	newNode->next = node->next;
	node->next = newNode;

	return (newNode);
}
