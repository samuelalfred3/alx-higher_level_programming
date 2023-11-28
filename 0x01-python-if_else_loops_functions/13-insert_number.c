#include "lists.h"

/**
 * insert_node - this inserts a number into a sorted singly-linked list.
 * @head: Is a pointer the head of the linked list.
 * @number: Is the number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - A pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;
	return (new);
}
