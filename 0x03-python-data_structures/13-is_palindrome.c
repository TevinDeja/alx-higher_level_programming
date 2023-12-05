#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
* add_nodeint - adds new node at the start of listint_t list
* @head: header
* @n: integer
*
* Return: address of the new element, or NULL if it failed
*/

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = n;
	newNode->next = *head;
	*head = newNode;
	return (newNode);
}

/**
* is_palindrome - C function that checks if singly linked list is palindrome
* @head: header
*
* Return: 0 if its not palindrome 1 if its palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *newHead = *head;
	listint_t *num = NULL, *num2 = NULL;

	if (*head == NULL || newHead->next == NULL)
		return (1);
	while (newHead != NULL)
	{
		add_nodeint(&num, newHead->n);
		newHead = newHead->next;
	}
	num2 = num;
	while (*head != NULL)
	{
		if ((*head)->n != num2->n)
		{
			free_listint(num);
			return (0);
		}
		*head = (*head)->next;
		num2 = num2->next;
	}
	free_listint(num);
	return (1);
}
